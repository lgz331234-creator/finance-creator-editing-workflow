#!/usr/bin/env python3
"""Resolve the installed release and gate project reuse on current evidence."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
from datetime import datetime, timezone

CHECKS = ('cover_identity', 'composition_footage', 'captions', 'voice_mix', 'timeline_content', 'project_render_config',
          'approved_template_binding', 'original_voice_policy', 'subtitle_language_policy', 'approved_bgm_selection',
          'ai_shot_provenance')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)

def release(root):
    m = read(root / 'workflow.json')
    errors = []
    for rel, digest in m['files'].items():
        # workflow.json contains this manifest, so hashing it would make every
        # valid manifest self-invalidating after any release update.
        if rel == 'workflow.json':
            continue
        p = (root / rel).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file() or sha(p) != digest:
            errors.append('Invalid release file: ' + rel)
    if not m['files'] or errors:
        raise ValueError('; '.join(errors) or 'Empty release manifest')
    return m, sha(root / 'workflow.json')

def run(action, project, root, allow_takeover=False, task_id=None):
    project = Path(project).resolve()
    if not project.is_dir():
        raise ValueError('Project directory does not exist: ' + str(project))
    m, fingerprint = release(root)
    state = project / '.finance-workflow'
    lockfile = state / 'lock.json'
    reviewfile = state / 'migration-review.json'
    old = read(lockfile) if lockfile.exists() else {}
    card_file = state / 'state.json'
    card = read(card_file) if card_file.exists() else {}
    current = old.get('release_sha256') == fingerprint and old.get('version') == m['version']
    base = {'workflow_version': m['version'], 'release_sha256': fingerprint, 'project': str(project)}
    if action == 'inspect':
        return dict(base, status='CURRENT' if current else 'MIGRATION_REQUIRED', previous_version=old.get('version')), 0
    if action == 'prepare':
        active = card.get('active_task')
        if active and active != (task_id or os.environ.get('CODEX_THREAD_ID')) and not allow_takeover:
            return dict(base, status='ACTIVE_IN_ANOTHER_TASK', active_task=active,
                        instruction='Resume that task or explicitly hand off with finance-edit prepare --takeover.'), 2
        if current:
            return dict(base, status='UNCHANGED', review_exists=reviewfile.exists()), 0
        if state.exists() and (lockfile.exists() or reviewfile.exists()):
            history = state / 'history' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            history.mkdir(parents=True)
            for p in (lockfile, reviewfile):
                if p.exists():
                    shutil.copy2(p, history / p.name)
        save(lockfile, {'version': m['version'], 'release_sha256': fingerprint, 'source': str(root), 'previous_version': old.get('version'), 'migration_status': 'REVIEW_REQUIRED'})
        save(reviewfile, {'version': m['version'], 'release_sha256': fingerprint, 'approved_baseline': '', 'scope': '', 'checks': {k: {'status': 'pending', 'note': '', 'evidence': []} for k in CHECKS}, 'subjective_listening': 'REVIEW_PENDING'})
        return dict(base, status='MIGRATION_PREPARED_NOT_COMPLETED', review=str(reviewfile), instruction='Back up and adapt affected editor files; record actual evidence, then run check.'), 0
    errors = []
    if not current:
        errors.append('Project is not pinned to the installed release; run prepare and migrate.')
    r = read(reviewfile) if reviewfile.exists() else {}
    if r.get('version') != m['version'] or r.get('release_sha256') != fingerprint:
        errors.append('Missing or stale migration review.')
    if not r.get('approved_baseline') or not r.get('scope'):
        errors.append('Record the approved baseline and actual task scope.')
    pending = [key for key in ('release_review', 'script_preflight', 'dependent_timing_review')
               if card.get(key) == 'PENDING']
    if pending:
        errors.append('State card pending: ' + ', '.join(pending))
    if card.get('script_file'):
        script = Path(card['script_file']).expanduser()
        if not script.is_absolute():
            script = project / script
        if not script.is_file() or sha(script) != card.get('script_sha256'):
            errors.append('Script file is missing or changed; rerun prepare --script and rebuild dependent timing.')
    checked = 0
    for key in CHECKS:
        item = r.get('checks', {}).get(key, {})
        status = item.get('status')
        if status not in ('checked', 'not_applicable') or not item.get('note', '').strip():
            errors.append(key + ': pending or missing explanation')
            continue
        if status == 'not_applicable':
            if key in ('timeline_content', 'project_render_config'):
                errors.append(key + ': must inspect the actual project')
            continue
        checked += 1
        evidence = item.get('evidence', [])
        if not evidence:
            errors.append(key + ': needs evidence with file and sha256')
        for e in evidence:
            name = e.get('file', '')
            p = Path(name).expanduser()
            if not p.is_absolute():
                p = project / p
            if not name or not p.is_file() or sha(p) != e.get('sha256'):
                errors.append(key + ': evidence missing or changed: ' + name)
    ai_manifest = state / 'ai-shots' / 'manifest.json'
    if ai_manifest.exists():
        plan = read(ai_manifest)
        if plan.get('script_sha256') != card.get('script_sha256'):
            errors.append('AI shot plan does not match the current script.')
        for shot in plan.get('shots', []):
            if not shot.get('used_in_timeline'):
                continue
            name = shot.get('output_file', '')
            media = project / name
            if not name or not media.is_file() or sha(media) != shot.get('output_sha256'):
                errors.append('AI shot file missing or changed: ' + shot.get('shot_id', '?'))
            if shot.get('rights_review') != 'approved' or shot.get('semantic_review') != 'approved':
                errors.append('AI shot review pending: ' + shot.get('shot_id', '?'))
            if not shot.get('rights_note') or not shot.get('semantic_note'):
                errors.append('AI shot review notes missing: ' + shot.get('shot_id', '?'))
    if checked < 2:
        errors.append('At least the project and timeline must be inspected.')
    return dict(base, status='BLOCKED' if errors else 'VERSION_AND_EVIDENCE_CURRENT', errors=errors, subjective_listening=r.get('subjective_listening', 'REVIEW_PENDING'), limitation='This gate validates versions and recorded file evidence, not subjective picture/sound quality.'), (2 if errors else 0)

def main():
    here = Path(__file__).resolve().parents[1]
    installed = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills' / 'finance-creator-editing-workflow'
    if installed.is_dir() and installed.resolve() != here:
        script = installed / 'scripts' / 'workflow_guard.py'
        if not script.is_file():
            raise ValueError('Installed workflow is outdated; do not fall back to the copied package.')
        os.execv(sys.executable, [sys.executable, str(script), *sys.argv[1:]])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['inspect', 'prepare', 'check'])
    parser.add_argument('project')
    args = parser.parse_args()
    result, code = run(args.action, args.project, here)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'ERROR', 'error': str(exc)}, ensure_ascii=False))
        sys.exit(2)
