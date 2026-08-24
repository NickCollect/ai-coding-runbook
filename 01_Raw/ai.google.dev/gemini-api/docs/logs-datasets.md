---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=he
fetched_at: 2026-08-24T02:30:42.454236+00:00
title: "\u05d9\u05d5\u05de\u05e0\u05d9\u05dd \u05d5\u05de\u05e2\u05e8\u05db\u05d9 \u05e0\u05ea\u05d5\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יומנים ומערכי נתונים

במדריך הזה נסביר איך לצפות ביומנים של השימוש ב-Gemini API בלוח הבקרה של Google AI Studio, כדי להבין טוב יותר את התנהגות המודל ואת האינטראקציות של המשתמשים עם האפליקציות שלכם. אפשר להשתמש ברישום ביומן כדי לצפות, לנפות באגים ו*לשתף משוב על השימוש עם Google כדי לעזור לשפר את Gemini בתרחישי שימוש שונים של מפתחים*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=he)

כל הקריאות ל-API‏ `GenerateContent`,‏ `BatchGenerateContent` ו-`StreamGenerateContent`, וקריאות ל-API של [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=he), נתמכות, למעט קריאות ל-API של סוכנים מנוהלים. המידע הזה כולל שיחות שמתבצעות דרך נקודות קצה (endpoints) של [תאימות ל-OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he).

## הגדרת רישום ביומן של פרויקט

כברירת מחדל, ה-API שומר את כל אובייקטי האינטראקציה (`store=true`) כדי לפשט את השימוש בתכונות של ניהול מצב בצד השרת. לעומת זאת, ב-Generate Content API, הבקשות לא נשמרות כברירת מחדל, וצריך להפעיל את השמירה לכל בקשה או ברמת הפרויקט מ-AI Studio.

ב-[AI Studio](https://aistudio.google.com/logs?hl=he) של Google אפשר להפעיל או להשבית את הרישום ביומן לכל הפרויקטים או לפרויקטים ספציפיים, ולשנות את ההעדפות האלה בכל שלב דרך החלונית **הגדרות** בדף [יומנים ומערכי נתונים](https://aistudio.google.com/logs?hl=he). אפשר להפעיל או להשבית את הרישום ביומן בנפרד עבור `generateContent` API ו-[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=he) API כדי לשנות את התנהגות ברירת המחדל של האחסון בפרויקט.

### רישום ביומן ברמת הבקשה

ההתנהגות של האחסון והרישום ביומן שונה בהתאם ל-API:

- ‫**[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he):** שומר בקשות כברירת מחדל (`store=true`) כדי לפשט את ניהול המצב בצד השרת.
- **יצירת Content API ‏ (`generateContent`):** לא שומר בקשות כברירת מחדל (`store=false`).

כך מגדירים את המאפיין `store`:

‫**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## צפייה ביומני הפרויקט ב-AI Studio

1. עוברים לדף 'יומנים' ב-[AI Studio](https://aistudio.google.com/logs?hl=he).
2. בוחרים פרויקט מהתפריט הנפתח.
3. אם יש יומנים של Interactions API, הם יופיעו בטבלה בסדר כרונולוגי הפוך.
4. כדי לראות את יומני הפרויקט של Generate Content API, צריך קודם להפעיל את האפשרות הזו ב[חלונית ההגדרות](#configure-logging).

כדי לראות תצוגה מקדימה של המטען הייעודי (payload), לוחצים על רשומה. אתם יכולים לבדוק את ההנחיה המלאה ואת התשובה מ-Gemini, ואת ההקשר מהתורות הקודמות. בבקשות של **Interactions API**, היומנים כוללים גם קישור ישיר אל `previous_interaction_id`.

## הגדרת תקופת השמירה של נתוני האחסון בפרויקט

היומנים יאבדו תוקף ויסומנו למחיקה אחרי תקופת שמירה שמוגדרת כברירת מחדל של 55 ימים (אלא אם [נשמרו במערך נתונים](#create), שאז הם לא יאבדו תוקף).
אפשר להגדיר את חלון השמירה של יומני פרויקט ל-7, 14, 28 או 55 ימים לכל היותר.

## יצירה ושיתוף של מערכי נתונים

אפשר לשמור יומנים במערכי נתונים כדי לארגן אותם ולייצא אותם בצורה יעילה יותר.

- בדף [Logs](https://aistudio.google.com/logs?hl=he), מאתרים את סרגל הסינון בחלק העליון ובוחרים מאפיין לסינון.
- בתצוגה המסוננת, מסמנים את התיבות כדי לבחור את כל היומנים או יומנים ספציפיים.
- לוחצים על הלחצן **Create dataset** (יצירת מערך נתונים) שמופיע בראש הרשימה.
- נותנים שם למערך הנתונים החדש, ואפשר גם להוסיף תיאור.
- מערך הנתונים שיצרתם יופיע עם קבוצת היומנים שנאספו.
- אפשר לייצא את מערך הנתונים לניתוח נוסף כקובצי CSV או JSONL, או ל-Google Sheets.

מערכי נתונים יכולים לעזור במגוון תרחישי שימוש שונים.

- **יצירת קבוצות של אתגרים:** אתם יכולים להשתמש בהן כדי לשפר את התחומים שבהם אתם רוצים שה-AI ישתפר.
- **יצירת קבוצות של דוגמאות:** לדוגמה, דוגמה משימוש אמיתי כדי ליצור תגובות ממודל אחר, או אוסף של מקרים קיצוניים לבדיקות שגרתיות לפני הפריסה.
- **קבוצות הערכה:** קבוצות שמייצגות שימוש אמיתי ביכולות חשובות, לצורך השוואה בין מודלים אחרים או איטרציות של הוראות מערכת.

אתם יכולים לתרום למחקר ולפיתוח של Gemini על ידי שיתוף מערכי הנתונים שלכם עם Google כדוגמאות להדגמה.

## מגבלות

כרגע אין תמיכה ברישום ביומן עבור הפעולות הבאות:

- מודלים של Imagen ו-Veo
- מודלים של Gemini להטמעה
- מודל Gemini Robotics
- קלטים שמכילים סרטונים, קובצי GIF או קובצי PDF
- סוכנים בתוכנית Public Preview ב-Gemini API

## המאמרים הבאים

- **יצירת אב טיפוס עם היסטוריית סשנים:** אפשר להשתמש ב-[AI Studio Build](https://aistudio.google.com/apps?hl=he) כדי ליצור אפליקציות עם קוד ולצרף את מפתח ה-API כדי לאפשר היסטוריה של יומני Gemini API לתכונות AI.
- **הפעלה מחדש של יומנים באמצעות Gemini Batch API:** אפשר להשתמש במערכי נתונים לדגימת תגובות ולהערכה של מודלים או של לוגיקת אפליקציה באמצעות הפעלה מחדש של יומנים באמצעות [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-22 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-22 (שעון UTC)."],[],[]]
