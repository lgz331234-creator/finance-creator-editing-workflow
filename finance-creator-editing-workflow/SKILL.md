---
name: finance-creator-editing-workflow
description: Produce or revise finance and technology creator videos using an approved visual style, narration-matched footage and collage, precise audio-derived subtitles, portrait covers, and localized editions. Use for an established creator editing workflow or a user-selected style sample; not for investment advice, generic transcription, or automatic publishing.
license: MIT
metadata:
  version: "1.7.0"
---

# Finance Creator Editing Workflow / 财经博主剪辑工作流

A reusable editing standard, not a bundled video editor or an account-publishing service. Apply it to the requested project only. The creator's latest explicit instructions and already-approved project take precedence over these defaults.

## Current editing mode: ChatCut 直男财经 (2026-09-29)

For new 霖公子谈趋势 edits, read [ChatCut 直男财经 SOP](references/chatcut-zhinan-finance.md). It is the creator's current editing default and overrides conflicting house-style, script-production, pacing, transition, subtitle and audio defaults below. Inputs are original presenter A-roll plus an already-approved script. Preserve spoken wording and original voice; do not run topic/copy/operations stages or rewrite approved copy. Target 1080×1920 at 30 fps, 85–92 seconds, with the five specified stages, centered presenter, dark restrained visuals, whole-sentence bilingual captions, yellow left-to-right keyword masks, editable MG, restrained BGM and short impact cues at least 8 seconds apart. Only hard cuts and fades are allowed. In the 40–75 second explanation, update visual information every 8–12 seconds; do not impose the old 3-second switching default. The old opening variety cue, 0.4-second in-video cover hold, nine-block storyboard and fixed music pool do not apply to this mode. Preserve authorized cover assets separately.

Use the official `chatcut-plugin-basics` for the Hosted ChatCut surface; cached skills, Desktop MCP and an authenticated Hosted tool connection are distinct states. Verify actual tool support, create a real editable project, and use original source items on separate tracks. Do not substitute a flattened local render or a JSON plan for a ChatCut project. Until source inputs and the connector are available, initialize a task with pending evidence only. Never claim Whisper, automatic presenter matting, completed reference analysis, listening, or better retention without evidence. Keep the seven per-video deliverables in the SOP; do not invent timestamps before receiving media.

The earlier mixed-collage style remains available for explicitly selected projects and preserved approved exceptions. The global version check does not change an already-running task or re-edit an old film.

## Local entrypoint and online sourcing

For “本地版”, “最新版自动找素材” or a new script requiring sourced visuals, use [local sourcing](references/local-sourcing.md). Run `python3 <this-skill>/scripts/local_workflow.py prepare <project-directory>` to reuse the installed release gate and keep a compact state card; do not load historical chats. The helper supports Commons image/video search, direct webpage snapshots, reviewed asset downloads, and the existing export check. Codex discovers official sources, checks claims and visual relevance, and uses the available editor; this script alone does not render or operate arbitrary editors. Keep original creator assets and current approved style. Save provenance per spoken line, never treat search results as approved event footage, and never claim pending migration or listening is complete.

## AI-shot enhancement

For this creator, AI video is a short **illustrative insert**, never the default picture layer. Keep the presenter as the visual anchor, with a small presenter window, real source cutouts, paper headlines and speech-timed annotations. Use generated motion only where a real factual image cannot explain an abstract mechanism, transition, market mood or conceptual relationship. Do not use generated footage to depict a specific person, company interface, deal, event, chart value or news scene as fact.

Use the installed entrypoint after `prepare` to create a per-project AI-shot plan:

```sh
finance-edit ai-plan <project> --provider vidmuse --shots 8 --duration 3 --ratio 9:16
```

It writes a short shot manifest and Vidmuse-ready prompts under `.finance-workflow/ai-shots/`; it does not connect to an external account, spend credits or claim that a provider/model is available. Generate only the chosen 4–8 inserts for a 60-second cut, normally 2–3 seconds each. After generating in a service the user has actually connected, register a decoded vertical file and its request/model details:

```sh
finance-edit ai-register <project> --shot-id ai01 --file <generated.mp4> --request-id <provider-request-id> --model <actual-model>
finance-edit ai-review <project> --shot-id ai01 --rights-status approved --rights-note 'provider terms permit this account use' --semantic-status approved --semantic-note 'abstract insert for the cited spoken mechanism' --used-in-timeline
```

`ai-register` copies the original result into `素材/AI生成/`, records its hash and validates that it is decodable vertical video. `ai-review` requires a concrete rights and semantic note before an asset is marked for the timeline. See [AI-shot workflow](references/ai-shots.md) before planning or generating shots. Do not put API keys, provider cookies or private media into the project.

## Always resolve the current workflow

At each new editing task or resumed phase, freshly read this installed SKILL.md and workflow.json from disk. Conversation summaries, old project snapshots, ZIPs, and remote repositories are not the local default. Current explicit user instructions still take precedence. Validate the installed release with scripts/workflow_guard.py; do not silently use an older or damaged copy.

Before editing a project, run: python3 <this-skill>/scripts/workflow_guard.py prepare <project-directory>. This backs up the previous workflow lock and records required migration; it does not rewrite media or make an editor compatible. Follow [migration rules](references/migration.md) and complete necessary project edits before rendering. Preserve source media, approved outputs, and the project's talking-head or voice-only choice. Automatic migration within editing tasks is authorized; do not ask again for each project.

Run workflow_guard.py check <project-directory> before final export. It fails on stale versions or absent/stale migration evidence. A passing version check is not visual or audio acceptance. Never mark a project migrated merely by changing its version field. This helper does not intercept arbitrary app exports or hot-reload already-running tasks; reload the entrypoint when resuming.

## Context budget protocol

For each video, use one active editing task. Start or resume with `finance-edit prepare <project> --script <script-file>`; the tool records the current Codex thread in the private state card. If another task owns the project, resume it or intentionally transfer ownership with `--takeover` after checking its brief handoff. Do not run two editors against the same project. On completing the editing task, run `finance-edit finish <project>`. This is a coordination check, not a way to stop another running Codex task automatically.

Carry one short project handoff card: approved baseline, current script hash, assets already verified, per-video exceptions, last export/check, and the next requested change. Read only this card and changed evidence on resumption. A per-video exception, such as Muse's original voice plus short sound effects and **no BGM**, stays with that video; it does not change the creator's default music pool. Run `finance-edit check <project>` after any script/audio/timeline change. It blocks while script preflight or dependent timing is pending, or the recorded script file has changed. Record actual rebuild evidence before clearing those flags.

Keep the workflow effective without replaying the full conversation:

- At task start, read this entrypoint and `workflow.json` once. After that, pass a short state card containing only: workflow version, project path, approved script id/hash, source assets, requested changes, current phase, and last check result.
- Do not paste old conversations, full run logs, unchanged scripts, or prior storyboard blocks into later phases. Read the specific file or diff only when a field changed or a check failed.
- Carry approved copy by a stable script id/hash. Carry edits as a concise diff (`add`, `remove`, `replace`, `reason`), then regenerate dependent audio timing, captions, scenes, and effects only for changed sections.
- Keep private evidence and raw media local. Summarize completed checks once; do not repeat unchanged evidence in every handoff.
- Use the three stages in `references/script-production.md` as compact handoffs within the current task: topic, approved spoken copy, storyboard. A stage handoff must not include unrelated history. Create a new task only when the user asks for one.

This reduces repeated context, not quality checks. Script fluency, pronunciation, audio timing, semantic visual matching, and the two release reviews remain mandatory.

## Resume the right work

- Resolve the actual creator assets, not just the workflow version. For 霖公子谈趋势, read `~/.codex/creator-profiles/lin-gongzi.json` when available; it is a private local binding, never part of a public package. Preserve the approved cover/layout and subtitle prototype. The workflow lock does not bind an editor to them automatically.
- For a supplied spoken recording, preserve the original recorded voice by default. Voice-only describes the picture, not permission to synthesize speech. A prior project's voice-cloning authorization does not authorize replacing a usable recording in this project. Keep transcription/display corrections separate from spoken rewriting; resolve a material script/recording mismatch before rendering.
- This creator's Chinese editions default to Chinese main captions plus nearby English translations, including previews. Localization or an explicit per-video exception takes precedence. Validate both rendered languages against the final PCM; an English brand name within Chinese text is not a translated subtitle track.
- For the earlier mixed-collage mode, select music from the creator-approved pool (the supplied versions of MY WAY by Veysigz, Into, and Fight), rotating within that pool. For ChatCut 直男财经, apply its stricter instrumental/low-drum music filter and documented selection exception. Generic library music is not a substitute for a missing preferred track. Record the selected source and inspect the actual mix. Missing private assets must be reported before rendering; do not silently replace them.
- Find the last **approved** export, editable project, script, and current change list. A newer export is not automatically the approved baseline. Preserve the baseline and source media.
- Check relevant installed skills and actual tool availability first. Reuse verified findings. Distinguish documentation read, skill installed, tool connected, and successful export; do not claim a capability from installation alone.
- Choose the fastest route that preserves the required result: the existing ChatCut project when available, Remotion for established motion layouts, FFmpeg for media processing and final muxing. A bundled FFmpeg binary alone is not proof that ChatCut performed the edit. Do not rebuild a working project just to change tools.
- For a requested sample, use the duration explicitly chosen for that task and preserve complete spoken phrases. The current FREYA showcase request is 60 seconds; neither 12 nor 60 seconds is a universal default. If the user has already approved the style and requested a full cut, finish it without inventing another approval gate.

## Script comprehension and spoken-flow preflight

The script is the first production asset. Before selecting footage, generating captions, or building a timeline:

1. Read the complete script for meaning, audience, claims, and the intended emotional turn. For an approved script or editing-only task, inspect and flag mismatches without rewriting; spoken-copy rewriting applies only when separately requested.
2. Produce a `script-preflight` alignment record with sentence breaks, breath groups, recording repeats and mismatches. In editing-only mode preserve approved words, remove only authorized recording errors/repeats and flag unresolved wording; do not create a new spoken script.
3. Verify pronunciation and spelling of product, organization, event, and English names. Read names as complete words (for example, FREYA and NEXUS), never as individual letters unless the user explicitly requests spelling.
4. Get the exact approved spoken script before timing captions or choosing shots. If the preflight is unresolved, stop the edit and report the specific phrase that needs repair.

Every spoken unit must then map to a matching visual, caption, and effect cue. Do not place a generic chart, stock clip, or animated sticker over a sentence whose meaning it does not show. After narration changes, regenerate PCM-derived captions, scene boundaries, and effect timing.

## Staged script production

This section applies only when topic or spoken-script production is separately requested. For the current editing-only ChatCut mode, use its five-stage SOP instead. Read [script production](references/script-production.md) before creating a topic, spoken script, or storyboard. Keep the work in three compact stages within the current task: topic selection, approved spoken copy, then the fixed nine-block 9:16 storyboard. Do not carry historical conversation text into a new generation stage. Generate the storyboard only after the spoken copy is approved, keep each line's visual meaning aligned with the narration, target a cut about every 3 seconds, use only the four allowed transitions, highlight key subtitle terms, and select a tense, light, fast finance BGM. The two upstream prompts remain explicit inputs; never invent missing prompt text.

## Earlier mixed-collage mode (when explicitly selected)

For projects explicitly retaining the 2026-09-28 reference, the picture mode is **host-led mixed collage**: actual presenter narration, speaker small windows, real photo/video cutouts, paper-style headlines, and arrows entering at the matching spoken word. Alternate these layouts with selective full-screen footage; do not cover the whole film with full-screen stock. This explicit 2026-09-28 choice supersedes the earlier all-full-screen default. Preserve the authorized original voice, XMoney subtitle prototype, portrait cover and quiet music balance. A voice-only exception still takes precedence for that specific project. Read the private creator profile for the exact binding; do not silently return to the old full-screen-only or generic cartoon treatment.

Read [visuals and covers](references/visuals-and-covers.md) when composing scenes or covers. Defaults are customizable for another creator:

- Portrait 1080×1920, 30 fps. Start with about 0.4 seconds of the creator-approved authorized portrait cover. Center the large yellow brand/topic title; keep the white secondary text legible and in a separate box without overlap. Export separate 9:16 and 3:4 covers.
- Body narration uses only the creator's authorized voice; the current FREYA treatment uses a suit-portrait cover followed by visuals and voice, with no talking-head opening. Other creators may explicitly choose a different treatment. Never substitute a reference creator's face or voice. Use existing consented local voice assets locally; do not upload them to a service without authorization.
- Resolve the selected style from the private creator profile before choosing layout. For this creator's current reference, use narrator-led mixed composition: talking head, a small narrator window, real subject cutouts/photo collage, paper labels, and speech-timed annotations. Read [reference-driven composition](references/reference-driven-composition.md) for the supplied workflow/case-pack method. Full-screen footage is one option, not a mandatory layout for every sentence. Change or add narration-matched material at intervals no longer than 3 seconds; preserve complete phrases and avoid repetitive filler. A host zoom alone is insufficient.
- Treat every release as a distinct visual package: vary the material subject, motion treatment, subtitle emphasis, sticker/overlay language, and transition rhythm between videos. Use the narration to select the visual; do not use a generic motion loop as a substitute for semantic footage. High-impact contrast is allowed, but the image, caption, and spoken claim must remain aligned.
- Before export, compare this release with the immediately previous approved release using a reuse ledger. Record the BGM ID, effect palette, material subjects, subtitle emphasis, overlay style, and transition rhythm. Repeated generic footage, repeated animated stickers, or the same BGM requires a documented editorial reason or a replacement.
- Use the approved “直男财经” editing principles as method only: sharp contrast, colloquial explanation, dense but intelligible cuts, and concrete charts/screenshots. Never copy another creator's face, voice, script, watermark, or source footage.
- Real events need their actual event material. Still photos may receive restrained movement, but do not present them as recorded live action. Keep source evidence in the delivery manifest.
- Do not add bottom-of-frame production notes such as “功能逻辑示意·非实际产品界面”. Keep the two top-left informational lines (“视频仅知识分享” / “不构成投资建议”, localized when needed) and a low-opacity account wordmark. No default progress bar or persistent chapter bar.
- Removing production notes is not permission to imply that stock footage is genuine event or product footage. Choose unambiguous material; preserve any context that materially changes what the viewer would understand.

## Narration is the timeline authority

Read [timing and audio](references/timing-and-audio.md) before editing narration, subtitles, speed, or muxing. Derive all sentence starts and ends from the exact PCM sample counts **actually written** to the new narration master, after transformations. Historical duration metadata is not authoritative.

In the earlier mixed-collage mode, each visible Chinese subtitle line must contain at most 10 characters, counting punctuation and embedded Latin text conservatively. Split into natural timed units instead of shrinking text. Use word timestamps from the current audio plus necessary listening at ambiguous spots. Do not estimate subtitle boundaries by character counts or patch a duration field without rebuilding downstream timing. Any voice edit invalidates dependent captions, scenes, sound-effect cues, and duration calculations.

Keep speech prominent, music underneath, and short varied sound effects attached to meaningful cuts. Use the same saved creator voice-processing target on every video, rotate BGM across releases unless explicitly selected, and verify the opening/body effects in the current export. See the consistency rules in the timing and audio reference. Pronounce brand names as names rather than spelling every letter. Preserve the approved script and required closing sentence; remove only authorized repeats and recording remarks.

### Voice, BGM, and narration QA

- Match the creator's final speech loudness and intelligibility to the approved 蔡公子 reference level as a technical mix target only; never imitate or clone that creator's identity. Measure the final encoded speech stem and confirm it remains clearly above the music.
- Resolve the original reference recording and its SHA-256 from the private creator profile's `voice.reference_asset`, then read `voice.mix_preferences` and the reference measurements. The original user-selected reference supersedes historical processed narration bearing a similar name. Match measured speech clarity and balance while preserving the creator's original recording; never treat a full-mix LUFS reading as an isolated voice/BGM measurement. Honor the creator's quieter BGM preference and disclose unresolved listening or separation limits.
- Rotate BGM by project/topic and keep a small local usage ledger. Do not reuse the same track by default across consecutive videos; vary the track and the effect palette while preserving the creator's voice front and center. The ledger is part of the release evidence, not an optional note.
- Listen through the narration after every edit for stutters, duplicated words, clipped joins, unnatural gaps, and brand-name mispronunciation. A clean transcript alone is not sufficient; rebuild the PCM-derived timing after any repair. Record the listened windows and any repaired phrase.
- Use two independent release reviews: Pass 1 covers decode, timing, loudness/true peak, narration continuity, caption bounds, and duplicate-source checks; Pass 2 covers narration-to-visual meaning, subject variety, subtitle/overlay readability, impact, pacing, and the 直男财经 method. Each pass must cite concrete evidence in the private run log before delivery.

For a project explicitly retaining the earlier mixed-collage sound treatment, add the user-selected short variety-show sound once at the start, including localized versions. The current ChatCut 直男财经 mode excludes this cue. Keep the first words intelligible and retain the varied body sound effects. If the reference mixes speech and effects, separate and inspect it before use; never paste another speaker's opening line into the edit. This cue is a private creator preference, not a bundled public audio asset. See the project's local sound-effect manifest for the selected file and verification limits.

## Localized editions

For Korean or Japanese voice/main captions plus English secondary captions, read [localization](references/localization.md). Translate text inside graphics and covers too. Rebuild the timing for each actual localized voice track; do not reuse the Chinese timeline. Never imply that this package includes a particular voice model, a connected service, or media rights.

## Verify this export and deliver

1. Validate the exported file's full decode, dimensions, fps, duration, first/last voice, and subtitle boundaries. Check black/frozen frames in context; a designed still cover is not a fault.
2. Match the exact narration against the final mixed/encoded audio at the start, middle, late section, and edited joins. Require no unexplained offset or accumulating drift; inspect mux timestamps as well as waveform correlation.
3. Inspect cover, scene cuts, longest captions, bilingual spacing, and the last spoken phrase. Play/listen to the actual export when a playback/listening tool is available. Automated transcription or loudness checks alone are not subjective listening; explicitly state checks not performed.
4. Perform two separate review passes before delivery. Pass 1 is technical: decode, timing, black/frozen frames, audio peaks/loudness, narration stutters, subtitle bounds, and duplicate-source checks. Pass 2 is editorial: narration-to-visual meaning, material variety, subtitle/overlay readability, impact, pacing, and reference-style compliance. Record both results separately in the private run log with file paths, hashes or measurements, and listening status; do not call a single automated check “two reviews”.
5. Deliver current video, two covers, subtitle files, approved script, and a concise asset/evidence manifest in the user's requested folder. Keep samples and historical versions separate. Open a preview when available.
5. Editing does not grant upload, scheduling, or publishing authorization. Inherit authorization already given for this exact work, and report only the state actually verified.

## Improve after each completed edit

Append a **local-only** run log inside the private project, for example `.local-edit-log/run-log.md`: version, approved baseline, requested changes, actual tools, output filenames/checksums, checks and results, pending review, new explicit preferences, and confirmed lessons. Do not add private run logs to this public skill repository.

Update defaults only for explicit user preferences or confirmed reusable findings. An experiment or one-off exception must not silently replace an approved baseline. Keep public changes in `CHANGELOG.md` only after removing private information. A public release requires current authorization and a review for personal media, voice assets, local paths, tokens, account details, and unlicensed source material. A local delivery log is never automatically a public release.
