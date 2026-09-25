# Timing and audio

## The failure this prevents

A repaired narration track in a real editing run was shorter than its old sentence metadata. Reusing metadata caused about 1.7 seconds of late-section drift. Correct-looking JSON and a plausible total duration did not prove synchronization. The reusable lesson is to measure the new audio itself, not preserve a historical offset.

## One clock for every dependency

1. Normalize approved voice pieces to a consistent PCM format, for example 48 kHz mono. Measure **after** resampling, trimming, or speed changes. Preserve source recordings and edit decisions.
2. Assemble the exact samples into the narration master. For sample rate `R`, current write position `P`, and next clip length `N`: `start=P/R`, `end=(P+N)/R`. Advance `P` by the actual `N` samples and the actual gap samples written. Represent fixed gaps as integer sample counts.
3. A 0.4-second cover at 48 kHz is 19,200 samples; a chosen 0.17-second sentence gap is 8,160 samples. These are examples, not universal pacing requirements. Do not insert silence blindly where the clip already contains a suitable pause.
4. Generate sentence metadata from that assembly. Derive subtitle offsets, semantic cut points, sound-effect cues, and total duration from the same source of truth. Quantize display cuts to frames only at the rendering boundary. A 30 fps rounding discrepancy within half a frame is expected; accumulated timing drift is not.
5. Re-transcribe the current edited voice where needed. Use word timestamps and approved text to establish phrase boundaries. Keep a normalization map for equivalent spoken forms such as brand names and acronyms; normalization must not change the displayed claim.

Never derive subtitle timing from text-length proportions. Never “repair” synchronization by changing only a JSON duration, stretching an image sequence to match stale timestamps, or adding tail silence to hide missing speech.

## Local voice repairs

Preserve good audio. Re-synthesize only the requested phrase using the already-authorized voice and an available local model. Use a natural pause as the splice; inspect both sides for doubled words, consonants cut off, breaths, clicks, and long silence. A crossfade is an implementation choice, not evidence that a bad splice became natural.

Keep a separate pronunciation form for synthesis and a display form for subtitles. Brand names should sound like their normal spoken names; do not spell letters unless that is the accepted pronunciation. Verify names in short context before generating a whole version.

After a changed phrase, rebuild every dependent time. Do not assume metadata remains correct because the preceding text is unchanged. Full-file ASR may omit a repeated recording take; inspect suspicious 2–5-second windows with surrounding context and listen when possible. Retain complete approved meaning, including a closing question or invitation after an account sign-off.

## Mix without moving the voice

Keep narration, music, and sound effects as separate stems. Use clean music sources permitted for the intended use. Speech should stay clear and in front; music provides light support. Adjust against the current recording rather than blindly copying previous gains. Rotate short impacts, whooshes, springs, chimes, or other fitting cues; avoid identical sound effects on every cut or long noisy tails.

For this creator's approved opening cue, place one short hit in the first second, normally at frame zero over the portrait cover. Duck the cue when narration starts; do not delay the hook just to fit its tail. Preserve a separate stem so localization and future voice changes do not require rendering the picture again. A separated reference may retain accompaniment or faint speech: record separation and listening status honestly, and do not distribute the source recording as part of a public skill without permission for that asset.

Check limiter/filter latency, sample rate conversion, encoder delay, mux offsets, and start timestamps. When picture is rendered silent, mux one approved mixed master once. Do not accidentally layer both the old render audio and the new master.

## Verification evidence

- Read and decode the final delivered file, not a source or earlier export.
- Compare source PCM at measured positions with assembled narration; verify clip boundaries and gaps.
- Correlate recognizable narration windows against the final mixed/encoded audio at the beginning, middle, ending, and repaired joins. Examine the best offset, not correlation strength alone. The target is zero unexplained offset; documented codec tolerance must not accumulate by sentence.
- Check subtitle range, monotonic timing, overlaps, missing words, and last-caption coverage. Check cut points at the words that introduce the next subject.
- Check complete decode, unexpected black/frozen frames, true peaks/clipping, and first/last audio. Review designed static frames before treating detector output as a defect.
- Actually play/listen when tooling permits, and inspect representative frames from the same export. Record “not listened” if no subjective listening occurred. ASR success is not proof of natural delivery or pronunciation.

Stop broadening verification once required checks pass and no new defect or change justifies another pass. Keep evidence with the version it validates.
