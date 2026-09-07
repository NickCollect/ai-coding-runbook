---
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=he
fetched_at: 2026-09-07T05:39:40.601590+00:00
title: "\u05ea\u05e6\u05d5\u05d2\u05d4 \u05de\u05e7\u05d3\u05d9\u05de\u05d4 \u05e9\u05dc \u05e7\u05d8\u05e2 \u05d1-Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תצוגה מקדימה של קטע ב-Lyria 3

‫Lyria 3 Clip Preview הוא מודל של Google שעבר אופטימיזציה ליצירת קליפים קצרים של מוזיקה, לופים ותצוגות מקדימות. הוא יוצר אודיו סטריאו באיכות גבוהה של 48kHz באורך 30 שניות מהנחיות טקסט או מקלט תמונה.

[לניסיון ב-Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=lyria-3-clip-preview&hl=he)

## מאמרי עזרה

במדריך [יצירת מוזיקה](https://ai.google.dev/gemini-api/docs/music-generation?hl=he) מוסבר על כל התכונות והיכולות.

## lyria-3-clip-preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | `lyria-3-clip-preview` |
| saveסוגי נתונים נתמכים | **קלטים**  טקסט ותמונה  **פלט**  אודיו (MP3), טקסט (מילים) |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  131,072 |
| handymanיכולות | **[יצירת אודיו](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)**  נתמך  **[שמירת נתונים במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he)**  לא נתמך  **[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he)**  לא נתמך  **[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)**  לא נתמך  **[בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)**  לא נתמך  **[עיגון בעזרת מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)**  לא נתמך  **[יצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he)**  לא נתמך  ‫**[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he)**  לא נתמך  **[חיפוש עם עיגון בנתונים](https://ai.google.dev/gemini-api/docs/google-search?hl=he)**  לא נתמך  **[פלטים מובנים](https://ai.google.dev/gemini-api/docs/structured-output?hl=he)**  לא נתמך  **[חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he)**  לא נתמך  **[הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)**  לא נתמך |
| speedאפשרויות צריכה | ‫**[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he)**  לא נתמך  **[הסקת מסקנות גמישה](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he)**  לא נתמך  **[הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)**  לא נתמך |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [תבניות של גרסאות מודל](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `lyria-3-clip-preview` - תצוגה מקדימה: `lyria-3-pro-preview` |
| calendar\_monthהעדכון האחרון | מרץ 2026 |

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-08-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-08-19 (שעון UTC)."],[],[]]
