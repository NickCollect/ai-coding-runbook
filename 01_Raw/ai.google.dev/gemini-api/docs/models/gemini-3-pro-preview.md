---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-preview?hl=he
fetched_at: 2026-08-31T06:41:43.930651+00:00
title: "\u05d2\u05e8\u05e1\u05ea \u05d8\u05e8\u05d5\u05dd-\u05d4\u05e9\u05e7\u05d4 \u05e9\u05dc Gemini 3 Pro \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# גרסת טרום-השקה של Gemini 3 Pro

כדי למנוע שיבושים בשירות, כדאי לעבור ל-[Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he).

## gemini-3-pro-preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `gemini-3-pro-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט, תמונה, סרטון, אודיו ו-PDF  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  1,048,576  **Output token limit**  65,536 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  לא נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  נתמך  **[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he)**  לא נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  לא נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  נתמך  **[הסקת מסקנות ב-Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - *כיבוי*: `gemini-3-pro-preview` |
| calendar\_monthהעדכון האחרון | נובמבר 2025 |
| id\_cardכרטיס מודל | [כרטיס מודל](https://deepmind.google/models/model-cards/gemini-3-pro/?hl=he) |

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-08-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-08-19 (שעון UTC)."],[],[]]
