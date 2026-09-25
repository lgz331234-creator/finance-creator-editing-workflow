# Korean / Japanese voice and bilingual captions

The requested target language controls voice, main captions, cover copy, and text inside graphics. English is the secondary subtitle language. Preserve official Latin-script brand spellings in display text where appropriate. These are the supported workflow modes, not bundled translation or speech engines.

## Translation handoff

Use a compact per-language document:

```json
{
  "language": "ko",
  "voice_language": "korean",
  "segments": [
    {
      "index": 0,
      "text": "AI 퀀트가 왜 갑자기 이렇게 뜨는 걸까요?",
      "speech": "에이아이 퀀트가 왜 갑자기 이렇게 뜨는 걸까요?",
      "parts": [
        {"text": "AI 퀀트가", "en": "Why is AI quant trading"},
        {"text": "왜 갑자기 이렇게 뜨는 걸까요?", "en": "suddenly taking off?"}
      ]
    }
  ],
  "visual_texts": {"AI量化": "AI 퀀트"},
  "cover": {"title": "FREYA", "subtitle": ["AI 퀀트", "왜 갑자기 뜰까?"], "brand": "Creator"}
}
```

For Japanese, use `language: "ja"`, `voice_language: "japanese"`, and Japanese main text. Display and speech fields have the same meaning; the speech form can normalize names and numbers. The union of subtitle parts, ignoring spacing and punctuation, must reproduce the complete approved translation.

## Preserve meaning and numbers

Translate the currently approved script, not a superseded draft. Do not invent guarantees, institutional endorsements, credentials, sponsorship tiers, or additional benefits. Keep questions as questions. Preserve the exact event identity, date, attribution, financial quantities, leverage ceiling, and term lengths. Verify items such as 90%, 10%, 10×, 60/180/360 days, and event number 2140 against source text whenever they occur.

Use natural spoken language rather than mechanically copying Chinese word order. Split captions by target-language phrase and breath; a useful starting point is 2–5 compact phrases per sentence, roughly no more than 28 Korean syllable blocks or a similarly readable Japanese line. That is a layout target, not permission to omit content. Long statements can use more phrases when necessary.

## Brand pronunciation and authorized voice

Maintain a pronunciation glossary. FREYA can be synthesized as 프레이야 in Korean or フレイヤ in Japanese; NEXUS as 넥서스 or ネクサス. Check the project owner's preferred pronunciation where supplied. These spellings are aids, not a license to change brand names in visible titles.

Use only the creator's already-authorized voice assets. Confirm that the selected local model actually supports the target language. Do not silently switch to a generic speaker, upload a reference voice, purchase voice generation, or claim a tested clone when it has only been configured. Surface a real capability gap while completing independent translation and layout work.

## Rebuild the language-specific timeline

Generate or obtain the actual approved target-language voice first. Measure its real PCM samples and align its words. Rebuild scenes, captions, sound-effect cues, and duration for that voice, following [timing and audio](timing-and-audio.md). Never force a complete translation into the original Chinese duration by cutting words or applying extreme speed.

Translate graph nodes, small labels, titles, disclaimers, and cover text. Keep proper names or account branding consistent. Verify that no unintended source-language text remains; do not mistake the intentional English secondary captions for untranslated content. Use actual fonts with Korean/Japanese glyph coverage and inspect text bounds in the rendered export.

Keep English secondary captions close to the main line without overlapping. Inspect long lines, mixed numbers/scripts, and safe areas separately for each language. Verify exact numbers and the closing invitation in each output; a passed Chinese export does not validate another language.
