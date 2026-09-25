# Finance Creator Editing Workflow: prompt and execution report

Version 1.0.0 · Updated 2026-09-25

## Copyable master prompt

```text
Use $finance-creator-editing-workflow to edit my final script using my approved reference and project. First check the existing project, relevant installed skills, and actual tool availability. Continue the approved project and choose the fastest end-to-end route that preserves quality, using ChatCut, Remotion, or FFmpeg as available. Report the tools actually used; an installed skill is not a completed edit.

Treat my final script as the content authority. Do not add or remove viewpoints, institutional endorsements, return promises, or promotion schemes. Remove only confirmed repeated takes, recording remarks, and unnatural pauses. Preserve the complete ending. Pronounce brand names naturally rather than spelling every letter. Recheck the captions and visuals whenever the voice changes.

Visuals: use 1080×1920 at 30 fps. Start with about 0.4 seconds of my authorized suit-portrait cover: a large yellow brand/topic title, separate white secondary text, no overlaps. Deliver both 9:16 and 3:4 covers. The current FREYA body uses my authorized voice over visual material after the suit-portrait cover, with no talking-head opening. Use full-screen moving material that matches the current sentence, with a fresh visual subject roughly every 2–3 seconds. Do not repeat clips within the video or fill time with unrelated footage. Use actual event material for a real event; restrained movement on a still photograph must not pass for live-action recording.

Screen elements: keep the two top-left lines “For information only” and “Not investment advice”, localized as needed, and a low-opacity account wordmark. Do not add bottom production notes such as “functional illustration, not the actual product interface”. Do not add a default progress bar or persistent chapter bar. Keep sources and production evidence in the delivery manifest; do not use the removal of small print to create a misleading impression.

Audio: keep my voice clear, natural, and prominent. Let music provide light support, using the track specified for this task or an existing permitted source. Use varied short sound effects at meaningful cuts rather than one effect everywhere. Keep authorized local voice references local; do not upload them or activate paid generation on your own.

Synchronization: derive every sentence boundary from the exact PCM samples written to the final narration master. Align captions using current word timestamps and necessary listening, never text-length proportions. Do not fix timing by editing only a duration field. Any trim, speed change, or voice replacement requires rebuilding affected captions, scene cuts, sound cues, and total duration from the same timeline.

For Korean or Japanese editions: localize the voice, main subtitles, covers, and graphic text; use English secondary subtitles close to the main line. Preserve all numbers, dates, proportions, and meaning. Rebuild timing from the actual target-language audio rather than forcing it into the Chinese duration.

Delivery: use the sample duration selected for this task; the current FREYA showcase request is 60 seconds. If I have already approved the sample and requested the full edit, finish the full video. Check the current export's complete decode, unexpected black/frozen frames, first and last speech, captions and cuts, cover crops, and narration offset after mixing. Only claim listening if you actually listened. Organize video, both covers, subtitles, script, and asset evidence in my requested date/topic folder; separate samples and previous versions, and open the latest preview.

After completion, update a private local edit log with the version, approved baseline, requested changes, actual tools, output files, checks, pending review, new explicit preferences, and confirmed lessons. Only promote explicit preferences or verified reusable findings into workflow defaults; experiments must not replace an approved baseline. Never automatically publish private logs or media. Use authorization already given for the current upload, scheduling, or public skill release; ask only when a necessary authorization is actually missing.
```

The user chooses sample duration per task. The 60-second duration here applies only to this FREYA showcase, not to all future projects. An already-authorized full edit does not need another approval. Identity, track, language, and platform remain task-specific inputs.

## Copyable revision prompt

```text
Continue the approved version and fix only the problems I identified, preserving the rest of its content, style, and audio. Check current files and prior evidence to locate the defect. If narration changes, preserve correct audio and repair only the required phrase, then rebuild all dependent captions, shots, and effects from actual PCM sample counts. Validate the new export; old-version checks do not prove the new version passed. Preserve the previous version, deliver the revision, and update the private local log.
```

## Execution report: invariants and adjustable choices

| Area | Preserve | Adjust for this video |
| --- | --- | --- |
| Project | Approved baseline, sources, current authorization | Fastest genuinely available tools |
| Script | Approved meaning, exact quantities, full ending | Authorized repeats and pauses |
| Cover | Creator portrait, yellow title, white secondary copy, two ratios | Crop, type size, title length |
| Visuals | Full-screen relevance and no repeated filler | Natural cuts around the 2–3-second target |
| Audio | Authorized voice, clear speech, correct timing | Music and effect levels |
| Captions | Current audio timestamps and complete meaning | Language-specific phrasing and line breaks |
| Verification | Evidence from this export; honest listening status | Checks relevant to the actual change |
| Updates | Private logs; explicit preferences become defaults | Verified reusable public improvements |

## Confirmed lessons

One repaired narration was shorter than its historical sentence metadata, producing approximately 1.7 seconds of late-section drift. Editing a duration label, changing visible text, or padding the tail could not resolve the cause. Recalculate the entire timeline from PCM samples actually written, then map the current word timestamps to captions and semantic cuts.

A recent export is also not necessarily the approved export. Identify the accepted baseline before revisions, and do not replace an approved visual style while fixing one small detail.

## Private completion record

Write the run record inside the private project, for example `.local-edit-log/run-log.md`, outside the public repository.

| Field | Record |
| --- | --- |
| Version and baseline | Date, current version, accepted prior version |
| Changes | Explicit request, actual modifications, reason |
| Tools and outputs | Actual tools, current outputs, useful checksums |
| Evidence | Decode, timing, captions, cover, audio measurements, listening status |
| Pending review | Unverified items or required owner actions |
| New preferences | Explicit rule and its intended scope |
| Lessons | Confirmed cause and repair; suitability as a default |

Public releases contain reusable rules, original templates, and reviewed change notes. Raw voice references, portrait source files, restricted media, full delivery logs, account details, and tokens stay private. Only explicitly authorized and reviewed finished showcase media may appear separately in the examples area, outside the MIT documentation license.

Add the creator-selected opening cue once in the first second of each edition. Separate speech from a mixed reference, duck beneath the first words, keep body cues varied, and retain the private source manifest. Do not bundle reference audio publicly by default.
