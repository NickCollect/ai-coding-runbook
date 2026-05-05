---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/multilingual-support.md
source_url: https://platform.claude.com/docs/en/build-with-claude/multilingual-support
title: "Multilingual support"
summarized_at: 2026-05-05
entities_referenced: [Extended-thinking]
concepts_referenced: []
---

Claude offers strong cross-lingual performance, with consistent relative quality across widely-spoken and lower-resource languages. The page reports zero-shot CoT MMLU scores **relative to English (= 100%)**, computed with extended thinking enabled, using human-translated MMLU sets from OpenAI's simple-evals repository.

## Performance — % relative to English (with extended thinking)

| Language | Opus 4.1 | Opus 4 (deprecated) | Sonnet 4.5 | Sonnet 4 (deprecated) | Haiku 4.5 |
|---|---|---|---|---|---|
| English (baseline) | 100% | 100% | 100% | 100% | 100% |
| Spanish | 98.1 | 98.0 | 98.2 | 97.5 | 96.4 |
| Portuguese (Brazil) | 97.8 | 97.3 | 97.8 | 97.2 | 96.1 |
| Italian | 97.7 | 97.5 | 97.9 | 97.3 | 96.0 |
| French | 97.9 | 97.7 | 97.5 | 97.1 | 95.7 |
| Indonesian | 97.3 | 97.2 | 97.3 | 96.2 | 94.2 |
| German | 97.7 | 97.1 | 97.0 | 94.7 | 94.3 |
| Arabic | 97.1 | 96.9 | 97.2 | 96.1 | 92.5 |
| Chinese (Simplified) | 97.1 | 96.7 | 96.9 | 95.9 | 94.2 |
| Korean | 96.6 | 96.4 | 96.7 | 95.9 | 93.3 |
| Japanese | 96.9 | 96.2 | 96.8 | 95.6 | 93.5 |
| Hindi | 96.8 | 96.7 | 96.7 | 95.8 | 92.4 |
| Bengali | 95.7 | 95.2 | 95.4 | 94.4 | 90.4 |
| Swahili | 89.8 | 89.5 | 91.1 | 87.1 | 78.3 |
| Yoruba | 80.3 | 78.9 | 79.7 | 76.4 | 52.7 |

Yoruba and Swahili clearly weakest, especially on Haiku 4.5. Consider testing your specific languages — Claude is capable in many beyond those benchmarked.

## Best practices

1. **Provide clear language context** — explicitly state desired input/output language; for fluency, prompt to use "idiomatic speech as if it were a native speaker."
2. **Use native scripts** — submit in native script, not transliteration.
3. **Consider cultural context** — beyond raw translation.

## Notes

- Claude processes input/output in most world languages using standard Unicode.
- Even low-resource languages retain meaningful capabilities (with caveats per table above).
