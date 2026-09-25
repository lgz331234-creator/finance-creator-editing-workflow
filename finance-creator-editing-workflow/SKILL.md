---
name: finance-creator-editing-workflow
description: Produce or revise finance and technology creator videos using an approved visual style, narration-matched full-screen footage, precise audio-derived subtitles, portrait covers, and localized editions. Use for an established creator editing workflow or a user-selected style sample; not for investment advice, generic transcription, or automatic publishing.
license: MIT
metadata:
  version: "1.0.0"
---

# Finance Creator Editing Workflow / 财经博主剪辑工作流

A reusable editing standard, not a bundled video editor or an account-publishing service. Apply it to the requested project only. The creator's latest explicit instructions and already-approved project take precedence over these defaults.

## Resume the right work

- Find the last **approved** export, editable project, script, and current change list. A newer export is not automatically the approved baseline. Preserve the baseline and source media.
- Check relevant installed skills and actual tool availability first. Reuse verified findings. Distinguish documentation read, skill installed, tool connected, and successful export; do not claim a capability from installation alone.
- Choose the fastest route that preserves the required result: the existing ChatCut project when available, Remotion for established motion layouts, FFmpeg for media processing and final muxing. A bundled FFmpeg binary alone is not proof that ChatCut performed the edit. Do not rebuild a working project just to change tools.
- For a requested sample, use the duration explicitly chosen for that task and preserve complete spoken phrases. The current FREYA showcase request is 60 seconds; neither 12 nor 60 seconds is a universal default. If the user has already approved the style and requested a full cut, finish it without inventing another approval gate.

## Current house style

Read [visuals and covers](references/visuals-and-covers.md) when composing scenes or covers. Defaults are customizable for another creator:

- Portrait 1080×1920, 30 fps. Start with about 0.4 seconds of the creator's authorized suit-portrait cover. Use a large yellow brand/topic title, white secondary text, and distinct text boxes. Export separate 9:16 and 3:4 covers.
- Body narration uses only the creator's authorized voice; the current FREYA treatment uses a suit-portrait cover followed by visuals and voice, with no talking-head opening. Other creators may explicitly choose a different treatment. Never substitute a reference creator's face or voice. Use existing consented local voice assets locally; do not upload them to a service without authorization.
- Prefer full-screen, moving, semantically relevant footage. Aim for a new visual subject every 2–3 seconds; keep phrases intact, avoid repeating clips in one video, and avoid reusing the same generic footage across releases.
- Real events need their actual event material. Still photos may receive restrained movement, but do not present them as recorded live action. Keep source evidence in the delivery manifest.
- Do not add bottom-of-frame production notes such as “功能逻辑示意·非实际产品界面”. Keep the two top-left informational lines (“视频仅知识分享” / “不构成投资建议”, localized when needed) and a low-opacity account wordmark. No default progress bar or persistent chapter bar.
- Removing production notes is not permission to imply that stock footage is genuine event or product footage. Choose unambiguous material; preserve any context that materially changes what the viewer would understand.

## Narration is the timeline authority

Read [timing and audio](references/timing-and-audio.md) before editing narration, subtitles, speed, or muxing. Derive all sentence starts and ends from the exact PCM sample counts **actually written** to the new narration master, after transformations. Historical duration metadata is not authoritative.

Use word timestamps from the current audio plus necessary listening at ambiguous spots. Do not estimate subtitle boundaries by character counts or patch a duration field without rebuilding downstream timing. Any voice edit invalidates dependent captions, scenes, sound-effect cues, and duration calculations.

Keep speech prominent, music underneath, and short varied sound effects attached to meaningful cuts. Pronounce brand names as names rather than spelling every letter. Preserve the approved script and required closing sentence; remove only authorized repeats and recording remarks.

For the current creator, add the user-selected short variety-show sound once at the start of every new or currently revised video, including localized versions. Keep the first words intelligible and retain the varied body sound effects. If the reference mixes speech and effects, separate and inspect it before use; never paste another speaker's opening line into the edit. This cue is a private creator preference, not a bundled public audio asset. See the project's local sound-effect manifest for the selected file and verification limits.

## Localized editions

For Korean or Japanese voice/main captions plus English secondary captions, read [localization](references/localization.md). Translate text inside graphics and covers too. Rebuild the timing for each actual localized voice track; do not reuse the Chinese timeline. Never imply that this package includes a particular voice model, a connected service, or media rights.

## Verify this export and deliver

1. Validate the exported file's full decode, dimensions, fps, duration, first/last voice, and subtitle boundaries. Check black/frozen frames in context; a designed still cover is not a fault.
2. Match the exact narration against the final mixed/encoded audio at the start, middle, late section, and edited joins. Require no unexplained offset or accumulating drift; inspect mux timestamps as well as waveform correlation.
3. Inspect cover, scene cuts, longest captions, bilingual spacing, and the last spoken phrase. Play/listen to the actual export when a playback/listening tool is available. Automated transcription or loudness checks alone are not subjective listening; explicitly state checks not performed.
4. Deliver current video, two covers, subtitle files, approved script, and a concise asset/evidence manifest in the user's requested folder. Keep samples and historical versions separate. Open a preview when available.
5. Editing does not grant upload, scheduling, or publishing authorization. Inherit authorization already given for this exact work, and report only the state actually verified.

## Improve after each completed edit

Append a **local-only** run log inside the private project, for example `.local-edit-log/run-log.md`: version, approved baseline, requested changes, actual tools, output filenames/checksums, checks and results, pending review, new explicit preferences, and confirmed lessons. Do not add private run logs to this public skill repository.

Update defaults only for explicit user preferences or confirmed reusable findings. An experiment or one-off exception must not silently replace an approved baseline. Keep public changes in `CHANGELOG.md` only after removing private information. A public release requires current authorization and a review for personal media, voice assets, local paths, tokens, account details, and unlicensed source material. A local delivery log is never automatically a public release.
