---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=he
fetched_at: 2026-10-19T05:41:16.096011+00:00
title: "\u05d4\u05d5\u05e6\u05d0\u05d4 \u05de\u05e9\u05d9\u05de\u05d5\u05e9 \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הוצאה משימוש של Gemini

בדף הזה מפורטים לוחות הזמנים הידועים להוצאה משימוש של מודלים [יציבים (GA)](https://ai.google.dev/gemini-api/docs/models?hl=he#stable) ו[בגרסת טרום-השקה (Preview)](https://ai.google.dev/gemini-api/docs/models?hl=he#preview), ושל סוכנים מנוהלים ב-Gemini API. **הוצאה משימוש** היא הודעה על כך שאנחנו כבר לא מספקים תמיכה במודל מסוים, ושהוא **יושבת** בעתיד הקרוב. אחרי שמודל **מושבת**, הוא מושבת לחלוטין ונקודת הקצה כבר לא זמינה.

הודעות על הוצאה משימוש מתפרסמות בדף [נתוני הגרסה](https://ai.google.dev/gemini-api/docs/changelog?hl=he), והתאריכים המוקדמים ביותר להשבתה שפורסמו מופיעים בדף הזה.
מודלים שכבר הושבתו מסומנים ברקע אפור.

## המודלים של Gemini 3

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | ‫22 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.8-flash-lite-tts` | ‫22 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.8-live` | ‫15 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.8-live-extended-thinking` | ‫15 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.8-flash` | ‫2 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.7-flash` | ‫13 באוגוסט 2026 | לא רלוונטי | ‫`gemini-3.8-flash` (לא זמין לבחירה ב-Google AI Studio; נקודת הקצה לא מושבתת ומנתבת אוטומטית בקשות API אל `gemini-3.8-flash`) |
| `gemini-3.6-flash` | ‫21 ביולי 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.5-flash-lite` | ‫21 ביולי 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.5-flash` | 19 במאי 2026 | לא רלוונטי | ‫`gemini-3.6-flash` (לא זמין לבחירה ב-Google AI Studio; נקודת הקצה לא מושבתת ומנתבת באופן אוטומטי בקשות API אל `gemini-3.6-flash`) |
| `gemini-3.1-flash-lite` | ‫7 במאי 2026 | ‫7 במאי 2027 | `gemini-3.5-flash-lite` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-3.1-flash-tts-preview` | ‫26 בפברואר 2026 | ‫17 בנובמבר 2026 | `gemini-3.8-flash-tts` או `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | ‫19 בפברואר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3-flash-preview` | ‫17 בדצמבר 2025 | לא הוכרז תאריך להפסקת התמיכה | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | ‫18 בנובמבר 2025 | ‫9 במרץ 2026 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | ‫3 במרץ 2026 | ‫25 במאי 2026 | `gemini-3.1-flash-lite` |

## מודלים של Gemini 2.5 Pro

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | ‫17 ביוני 2025 | לא הוכרז תאריך להפסקת התמיכה |  |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-2.5-computer-use-preview-10-2025` | ‫7 באוקטובר 2025 | ‫28 ביולי 2026 | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | ‫3 במרץ 2025 | ‫2 בדצמבר 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | ‫6 במאי 2025 | ‫2 בדצמבר 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | ‫5 ביוני 2025 | ‫2 בדצמבר 2025 | `gemini-3.1-pro-preview` |

## מודלים של Gemini 2.5 Flash

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | ‫17 ביוני 2025 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-2.5-flash-lite` | ‫22 ביולי 2025 | לא הוכרז תאריך להפסקת התמיכה |  |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | ‫25 בספטמבר 2025 | ‫31 במרץ 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | ‫20 במאי 2025 | ‫18 בנובמבר 2025 | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | ‫25 בספטמבר 2025 | ‫17 בפברואר 2026 | `gemini-3.6-flash` |

## מודלים של Gemini 2.0

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | ‫5 בפברואר 2025 | ‫1 ביוני 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | ‫5 בפברואר 2025 | ‫1 ביוני 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | ‫25 בפברואר 2025 | ‫1 ביוני 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | ‫25 בפברואר 2025 | ‫1 ביוני 2026 | `gemini-3.1-flash-lite` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-2.0-flash-lite-preview` | ‫5 בפברואר 2025 | ‫9 בדצמבר 2025 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | ‫5 בפברואר 2025 | ‫9 בדצמבר 2025 | `gemini-2.5-flash-lite` |

## מודלים של Live API

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | ‫15 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.8-live-extended-thinking` | ‫15 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.5-transcribe-live` | אוגוסט 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-2.0-flash-live-001` | 9 באפריל 2025 | ‫9 בדצמבר 2025 | `gemini-3.8-live` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-3.5-live-translate-preview` | יוני 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.1-flash-live-preview` | ‫11 במרץ 2026 | ‫17 בנובמבר 2026 | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | ‫12 בדצמבר 2025 | ‫17 בנובמבר 2026 | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | ‫17 ביוני 2025 | ‫9 בדצמבר 2025 | `gemini-3.8-live` |

## מודלים של אודיו

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | אוגוסט 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-2.5-flash-preview-tts` | ‫20 במאי 2025 | ‫17 בנובמבר 2026 | `gemini-3.8-flash-tts` או `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | ‫20 במאי 2025 | ‫17 בנובמבר 2026 | `gemini-3.8-flash-tts` או `gemini-3.8-flash-lite-tts` |

## מודלים של הטמעה

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | ‫22 באפריל 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-embedding-001` | ‫14 ביולי 2025 | ‫14 במאי 2028 | `gemini-embedding-2` |
| `text-embedding-004` | ‫9 באפריל 2024 | ‫14 בינואר 2026 | `gemini-embedding-2` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `embedding-2-preview` | ‫10 במרץ 2026 | ‫10 באוגוסט 2026 | `gemini-embedding-2` |
| `embedding-001` | ‫9 באפריל 2024 | ‫30 באוקטובר 2025 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | ‫30 באוקטובר 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | ‫30 באוקטובר 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | ‫30 באוקטובר 2025 | `gemini-embedding-2` |

## מודלים של Nano Banana

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | ‫6 באוקטובר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.1-flash-lite-image` | ‫30 ביוני 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-3.1-flash-image` | ‫28 במאי 2026 | לא הוכרז תאריך להפסקת התמיכה | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | ‫28 במאי 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `gemini-2.5-flash-image` | ‫2 באוקטובר 2025 | ‫15 במרץ 2027 | `gemini-3.1-flash-lite-image` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-3.1-flash-image-preview` | ‫26 בפברואר 2026 | ‫25 ביוני 2026 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | ‫20 בנובמבר 2025 | ‫25 ביוני 2026 | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | ‫7 במאי 2025 | ‫15 בינואר 2026 | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | ‫7 במאי 2025 | ‫14 בנובמבר 2025 | `gemini-nano-banana-2.1` |

## מודלים של Imagen

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | ‫24 ביוני 2025 | ‫17 באוגוסט 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | ‫24 ביוני 2025 | ‫17 באוגוסט 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | ‫24 ביוני 2025 | ‫17 באוגוסט 2026 | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | ‫6 בפברואר 2025 | ‫10 בנובמבר 2025 | `imagen-4.0-generate-001` |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `imagen-4.0-generate-preview-06-06` | ‫24 ביוני 2025 | ‫17 בפברואר 2026 | `imagen-4.0-generate-001` |
| `imagen-4.0-ultra-generate-preview-06-06` | ‫24 ביוני 2025 | ‫17 בפברואר 2026 | `imagen-4.0-ultra-generate-001` |

## מודלים של Veo

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | ‫9 בספטמבר 2025 | ‫30 ביוני 2026 | `veo-3.1-generate-preview` או במודלים של GA ב-[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=he) |
| `veo-3.0-fast-generate-001` | ‫9 בספטמבר 2025 | ‫30 ביוני 2026 | ‫`veo-3.1-fast-generate-preview` או המודלים של GA ב-[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=he) |
| `veo-2.0-generate-001` | 9 באפריל 2025 | ‫30 ביוני 2026 | `veo-3.1-generate-preview` או במודלים של GA ב-[Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=he) |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `veo-3.1-lite-generate-preview` | ‫31 במרץ 2026 | ‫22 באוקטובר 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | ‫15 באוקטובר 2025 | ‫22 באוקטובר 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | ‫15 באוקטובר 2025 | ‫22 באוקטובר 2026 | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | ‫31 ביולי 2024 | ‫12 בנובמבר 2025 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-preview` | ‫31 ביולי 2024 | ‫12 בנובמבר 2025 | `veo-3.1-fast-generate-preview` |

## מודלים מסוג Gemini Omni Flash

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | ‫27 באוגוסט 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-omni-flash-preview` | ‫30 ביוני 2026 | ‫22 באוקטובר 2026 | `gemini-omni-1.1-flash` |

## מודלים של Lyria

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| `lyria-3.5` | ‫3 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `lyria-3-clip-preview` | ‫25 במרץ 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `lyria-3-pro-preview` | ‫25 במרץ 2026 | לא הוכרז תאריך להפסקת התמיכה | `lyria-3.5` |
| `lyria-realtime-exp` | ‫20 במאי 2025 | לא הוכרז תאריך להפסקת התמיכה |  |

## מודלים של רובוטיקה

| **מודל** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| מודלים בגרסת טרום-השקה (Preview) | | | |
| `gemini-robotics-er-1.6-preview` | ‫14 באפריל 2026 | ‫31 באוגוסט 2026 | gemini-robotics-er-2-preview |
| `gemini-robotics-er-1.5-preview` | ‫25 בספטמבר 2025 | ‫30 באפריל 2026 | `gemini-robotics-er-1.6-preview` |

## סוכנים מנוהלים

| **Agent** | **תאריך השקה** | **תאריך הפסקת התמיכה** | **החלפה מומלצת** |
| --- | --- | --- | --- |
| תצוגה מקדימה של סוכנים | | | |
| `antigravity-preview-09-2026` | ‫17 בספטמבר 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `antigravity-preview-05-2026` | 19 במאי 2026 | ‫5 באוקטובר 2026 | `antigravity-preview-09-2026` |
| `deep-research-preview-04-2026` | ‫21 באפריל 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `deep-research-max-preview-04-2026` | ‫21 באפריל 2026 | לא הוכרז תאריך להפסקת התמיכה |  |
| `deep-research-pro-preview-12-2025` | ‫11 בדצמבר 2025 | ‫23 באוקטובר 2026 | `deep-research-preview-04-2026` |

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-12 (שעון UTC)."],[],[]]
