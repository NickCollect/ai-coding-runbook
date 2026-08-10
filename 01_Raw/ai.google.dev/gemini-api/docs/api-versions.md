---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=he
fetched_at: 2026-08-10T03:09:23.480556+00:00
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

במסמך הזה מפורטת סקירה כללית של ההבדלים בין גרסאות `v1` ו-`v1beta` של Gemini API.

- ‫**v1**: גרסה יציבה של ה-API. התכונות בגרסה היציבה נתמכות באופן מלא במהלך מחזור החיים של הגרסה הראשית. אם יש שינויים שעלולים לשבור את התאימות לאחור, ניצור גרסה ראשית חדשה של ה-API והגרסה הקיימת תוצא משימוש אחרי תקופה סבירה.
  יכול להיות שיוכנסו שינויים שלא ישפיעו על התפקוד של ממשק ה-API בלי לשנות את הגרסה הראשית. ‫**Interactions API** והתכונות העיקריות שלו זמינים בדרך כלל ב-`v1`.
- ‫**v1beta**: הגרסה הזו כוללת תכונות ויכולות מוקדמות שנמצאות בפיתוח פעיל. יכול להיות שנבצע שינויים בתכונות ב-`v1beta` כדי לשפר אותן על סמך המשוב שנקבל, אבל תוכלו לנסות יכולות חדשות לפני שהן יהפכו ליציבות.

## תמיכה ביכולות ובתכונות

בטבלה הבאה מפורטת הזמינות של היכולות ב-`v1` (GA) וב-`v1beta` (בטא). היכולות והכלים העיקריים של API חלים על Interactions API ועל `generateContent` אלא אם צוין אחרת:

| תכונה | v1 | v1beta |
| --- | --- | --- |
| **יכולות הליבה של ה-API** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=he) |  |  |
| [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) |  |  |
| [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) |  |  |
| [חשיבה / חשיבה רציונלית](https://ai.google.dev/gemini-api/docs/thinking?hl=he) |  |  |
| [הוראות מערכת](https://ai.google.dev/gemini-api/docs/system-instructions?hl=he) |  |  |
| [פלט אודיו (הגדרות דיבור)](https://ai.google.dev/gemini-api/docs/audio?hl=he) |  |  |
| [רמת השירות (עדיפות / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he) |  |  |
| **כלים** |  |  |
| [כלי להרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) |  |  |
| [הארקה בחיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) |  |  |
| [הארקה של מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he) |  |  |
| [הכלי לניתוח הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he) |  |  |
| [כלי לחיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he) |  |  |
| [כלי לשימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he) |  |  |
| [כלי שרתי MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=he) |  |  |
| **ממשקי API בזמן אמת** |  |  |
| ‫[Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=he) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=he) |  |  |
| [טוקנים זמניים (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=he) |  |  |
| **Platform APIs** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=he) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=he) |  |  |
| [File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search?hl=he) |  |  |
| ‫[Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=he) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=he) |  |  |
| [Context Caching](https://ai.google.dev/gemini-api/docs/caching?hl=he) |  |  |

- ‫ – נתמך

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
    "input": "Explain how AI works",
  }'
```

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-28 (שעון UTC)."],[],[]]
