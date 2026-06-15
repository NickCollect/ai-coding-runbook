---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=he
fetched_at: 2026-06-15T06:30:00.402317+00:00
title: "\u05d4\u05e1\u05d1\u05e8 \u05e2\u05dc \u05d2\u05e8\u05e1\u05d0\u05d5\u05ea API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [הפניית API](https://ai.google.dev/api?hl=he)

שליחת משוב

# הסבר על גרסאות API

במסמך הזה מפורטת סקירה כללית של ההבדלים בין גרסאות Gemini API‏: `v1` ו-`v1beta`.

- ‫**v1**: גרסה יציבה של ה-API. התכונות בגרסה היציבה נתמכות באופן מלא לאורך חיי הגרסה הראשית. אם יש שינויים שעלולים לשבור את התאימות לאחור, ניצור את הגרסה הראשית הבאה של ה-API ונוציא משימוש את הגרסה הקיימת אחרי תקופה סבירה.
  יכול להיות שיוכנסו שינויים ב-API שלא ישפיעו על התפקוד בלי לשנות את הגרסה הראשית.
- ‫**v1beta**: הגרסה הזו כוללת תכונות מוקדמות שעשויות להיות בשלבי פיתוח, והן כפופות לשינויים שעלולים לגרום לכשלים. בנוסף, אין ערובה לכך שהתכונות בגרסת הבטא יעברו לגרסה היציבה. **אם אתם צריכים יציבות בסביבת הייצור שלכם ולא יכולים להסתכן בשינויים שעלולים לשבור את המערכת, אל תשתמשו בגרסה הזו בסביבת הייצור.**

| תכונה | v1 | v1beta |
| --- | --- | --- |
| יצירת תוכן – קלט טקסט בלבד |  |  |
| יצירת תוכן – קלט של טקסט ותמונה |  |  |
| יצירת תוכן – פלט טקסט |  |  |
| יצירת תוכן – שיחות עם זיכרון (צ'אט) |  |  |
| יצירת תוכן – קריאות לפונקציות |  |  |
| יצירת תוכן – סטרימינג |  |  |
| הטמעת תוכן – הזנה של טקסט בלבד |  |  |
| יצירת תשובה |  |  |
| מאחזר סמנטי |  |  |
| Interactions API |  |  |

- ‫ – נתמך
- ‫ – לא תהיה תמיכה לעולם

## הגדרת גרסת API ב-SDK

ערכות ה-SDK של Gemini API מוגדרות כברירת מחדל לגרסה `v1beta`, אבל אפשר לציין גרסאות באופן מפורש על ידי הגדרת גרסת ה-API כמו בדוגמת הקוד הבאה:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
