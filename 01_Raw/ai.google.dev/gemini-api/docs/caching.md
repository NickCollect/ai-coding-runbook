---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=he
fetched_at: 2026-08-31T06:39:01.929046+00:00
title: "\u05e9\u05de\u05d9\u05e8\u05d4 \u05d1\u05de\u05d8\u05de\u05d5\u05df \u05e9\u05dc \u05d4\u05e7\u05e9\u05e8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שמירה במטמון של הקשר

בתהליך עבודה טיפוסי של AI, יכול להיות שתעבירו את אותם אסימוני קלט שוב ושוב למודל. ‫Gemini API מציע שמירה מרומזת במטמון כדי לשפר את הביצועים ולצמצם את העלויות.

## שמירה מרומזת במטמון

האפשרות 'שמירת נתונים במטמון באופן מרומז' מופעלת כברירת מחדל בכל המודלים של Gemini 2.5 ומעלה. הוא תומך במצבי שיחה [עם שמירת מצב](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#multi-turn-conversations) (באמצעות `previous_interaction_id`) ו[ללא שמירת מצב](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#stateless-conversations).
אם הבקשה שלכם מגיעה למטמון, אנחנו מעבירים לכם באופן אוטומטי את החיסכון בעלויות. לא צריך לעשות שום דבר כדי להפעיל את התכונה הזו. בטבלה הבאה מפורטת כמות הטוקנים המינימלית של הקלט לכל מודל שנדרש כדי להשתמש במטמון ההקשר:

| מודל | מגבלת טוקנים מינימלית |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| ‫Gemini 3.1 Pro Preview | 4096 |
| Gemini ‎2.5 Flash | 2048 |
| Gemini ‎2.5 Pro | 2048 |

כדי להגדיל את הסיכוי לפגיעה במטמון משתמע:

- כדאי לנסות להוסיף בתחילת ההנחיה תוכן גדול ונפוץ
- ניסיון לשלוח בקשות עם קידומת דומה בפרק זמן קצר

אפשר לראות את מספר הטוקנים שהיו פגיעות במטמון בשדה `usage.total_cached_tokens` (Python ו-JavaScript) של אובייקט התגובה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
