---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=he
fetched_at: 2026-09-14T05:36:44.273902+00:00
title: "\u05d4\u05e1\u05d1\u05e8 \u05e2\u05dc \u05d2\u05e8\u05e1\u05d0\u05d5\u05ea API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [הפניית API](https://ai.google.dev/api?hl=he)

שליחת משוב

# הסבר על גרסאות API

במסמך הזה מפורטת סקירה כללית של ההבדלים בין גרסאות Gemini API‏: `v1` ו-`v1beta`.

- ‫**v1**: גרסה יציבה של ה-API. התכונות בגרסה היציבה נתמכות באופן מלא במהלך מחזור החיים של הגרסה הראשית. אם יש שינויים שעלולים לשבור את התאימות לאחור, תיצור גרסה ראשית חדשה של ה-API והגרסה הקיימת תצא משימוש אחרי תקופה סבירה.
  יכול להיות שיוכנסו שינויים שלא ישפיעו על התפקוד של ממשק ה-API בלי לשנות את הגרסה הראשית. החל מיוני 2026, **Interactions API** זמין באופן כללי ונתמך ב-`v1`.
- ‫**v1beta**: הגרסה הזו כוללת תכונות ויכולות מוקדמות שנמצאות בפיתוח פעיל. יכול להיות שנבצע שינויים בתכונות ב-`v1beta` כדי לשפר אותן על סמך המשוב שנקבל, אבל תוכלו לנסות יכולות חדשות לפני שהן יהפכו ליציבות.

| תכונה | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| יצירת תוכן – קלט טקסט בלבד |  |  |
| יצירת תוכן – קלט של טקסט ותמונה |  |  |
| יצירת תוכן – פלט טקסט |  |  |
| יצירת תוכן – שיחות רב-שלביות (צ'אט) |  |  |
| יצירת תוכן – קריאות לפונקציות |  |  |
| יצירת תוכן – סטרימינג |  |  |
| הטמעת תוכן – הזנה של טקסט בלבד |  |  |
| יצירת תשובה |  |  |
| מאחזר סמנטי |  |  |

- ‫ – נתמך
- ‫ – לא תהיה תמיכה לעולם

## הגדרת גרסת API ב-SDK

ערכות ה-SDK של Gemini API מוגדרות כברירת מחדל לגרסה `v1beta`, אבל אפשר לציין גרסאות באופן מפורש על ידי הגדרת גרסת ה-API כמו בדוגמת הקוד הבאה:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works"
  }'
```

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-12 (שעון UTC)."],[],[]]
