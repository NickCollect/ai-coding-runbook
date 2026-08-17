---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=he
fetched_at: 2026-08-17T02:30:07.409732+00:00
title: "\u202bGemini Robotics ER 2 Streaming Preview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ‫Gemini Robotics ER 2 Streaming Preview

‫Gemini Robotics ER 2 Streaming הוא מודל ראייה-שפה (VLM) לרובוטיקה שעבר אופטימיזציה לסטרימינג של טקסט בזמן אמת באמצעות Live API. הוא מקבל קלט של טקסט, תמונות, סרטונים ואודיו, ותומך בהזרמה דו-כיוונית עם קריאה לפונקציות.

[לניסיון ב-Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=he)

## מאמרי עזרה

בדף [Live API for robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he) אפשר לקרוא על כל התכונות והיכולות.

## gemini-robotics-er-2-streaming-preview

### ‫Gemini Robotics ER 2 Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-2-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-2-preview` |
| calendar\_monthהעדכון האחרון | יולי 2026 |
| id\_cardכרטיס מודל | [כרטיס מודל](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=he) |

### ‫Gemini Robotics ER 2 Streaming Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-2-streaming-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  לא נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  לא נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  לא נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  לא נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  לא נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  לא נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  לא נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  לא נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthהעדכון האחרון | יולי 2026 |
| id\_cardכרטיס מודל | [כרטיס מודל](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=he) |

### ‫Gemini Robotics ER 1.6 Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-robotics-er-1.6-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונות, סרטונים, אודיו  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-robotics-er-1.6-preview` |
| calendar\_monthהעדכון האחרון | דצמבר 2025 |
| cognition\_2תאריך סף הידע | ינואר 2025 |

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
