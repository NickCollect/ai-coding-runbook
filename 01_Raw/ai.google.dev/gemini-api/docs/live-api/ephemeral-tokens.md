---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=he
fetched_at: 2026-10-05T06:27:48.917403+00:00
title: "\u05d0\u05e1\u05d9\u05de\u05d5\u05e0\u05d9\u05dd \u05d6\u05de\u05e0\u05d9\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# אסימונים זמניים

אסימונים זמניים הם אסימוני אימות לטווח קצר לגישה ל-Gemini API דרך [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). הם נועדו לשפר את האבטחה כשמתחברים ישירות ממכשיר של משתמש ל-API (הטמעה של [לקוח לשרת](https://ai.google.dev/gemini-api/docs/live?hl=he#implementation-approach)). בדומה למפתחות API רגילים, אפשר לחלץ טוקנים זמניים מאפליקציות בצד הלקוח, כמו דפדפני אינטרנט או אפליקציות לנייד. אבל מכיוון שאסימונים זמניים פוקעים במהירות ואפשר להגביל אותם, הם מפחיתים באופן משמעותי את סיכוני האבטחה בסביבת ייצור. מומלץ להשתמש בהם כשניגשים ישירות ל-Live API מאפליקציות בצד הלקוח, כדי לשפר את האבטחה של מפתחות ה-API.

## איך פועלים טוקנים זמניים

כך פועלים טוקנים זמניים ברמה גבוהה:

1. הלקוח (לדוגמה, אפליקציית אינטרנט) עובר אימות עם ה-Backend.
2. הבקשות מהקצה העורפי שולחות טוקן זמני משירות ההקצאה של Gemini API.
3. ‫Gemini API מנפיק אסימון לטווח קצר.
4. הקצה העורפי שולח את האסימון ללקוח לחיבורי WebSocket ל-Live
   API. כדי לעשות זאת, צריך להחליף את מפתח ה-API באסימון זמני.
5. לאחר מכן, הלקוח משתמש באסימון כאילו היה מפתח API.

![סקירה כללית על טוקנים זמניים](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=he)

השימוש באסימון משפר את האבטחה, כי גם אם הוא נשלף, הוא תקף לזמן קצר, בניגוד למפתח API תקף לזמן ארוך שמוטמע בצד הלקוח. מכיוון שהלקוח שולח נתונים ישירות ל-Gemini, זה גם משפר את זמן האחזור ומונע את הצורך בשרתי קצה עורפיים (back-end) שיפעלו כשרתי proxy לנתונים בזמן אמת.

## יצירת טוקן זמני

הנה דוגמה פשוטה שמראה איך לקבל מ-Gemini טוקן זמני.
כברירת מחדל, יש לכם דקה אחת להתחיל סשנים חדשים של Live API באמצעות האסימון מהבקשה הזו (`newSessionExpireTime`), ו-30 דקות לשלוח הודעות דרך החיבור הזה (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

ב[הפניית ה-API](https://ai.google.dev/api/live?hl=he#ephemeral-auth-tokens) מפורטים אילוצים, ערכי ברירת מחדל ומפרטים אחרים של השדה `expireTime`.
במהלך `expireTime` הזמן הזה, תצטרכו [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=he#session-resumption) להתחבר מחדש לשיחה כל 10 דקות (אפשר לעשות את זה עם אותו אסימון גם אם `uses: 1`).

אפשר גם לנעול טוקן זמני לקבוצה של הגדרות. האפשרות הזו יכולה להיות שימושית לשיפור נוסף של האבטחה באפליקציה ולשמירה על הוראות המערכת בצד השרת.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.8-live',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.8-live',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.8-live",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

אפשר גם לנעול קבוצת משנה של שדות. מידע נוסף זמין ב[מסמכי התיעוד של ה-SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields).

## התחברות ל-Live API באמצעות טוקן זמני

אחרי שמקבלים אסימון זמני, משתמשים בו כאילו היה מפתח API (אבל חשוב לזכור שהוא פועל רק עם ה-API הפעיל, ורק עם גרסה `v1beta` של ה-API).

השימוש בטוקנים זמניים מוסיף ערך רק כשפורסים אפליקציות שפועלות לפי גישת [הטמעה מלקוח לשרת](https://ai.google.dev/gemini-api/docs/live?hl=he#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

דוגמאות נוספות מופיעות במאמר [תחילת העבודה עם Live API](https://ai.google.dev/gemini-api/docs/live?hl=he).

## שיטות מומלצות

- מגדירים משך תפוגה קצר באמצעות הפרמטר `expire_time`.
- התוקף של האסימונים פג, ולכן צריך להפעיל מחדש את תהליך ההקצאה.
- אימות מאובטח של ה-Backend שלכם. האבטחה של טוקנים זמניים תהיה זהה לזו של שיטת האימות של ה-Backend.
- בדרך כלל, מומלץ להימנע משימוש בטוקנים זמניים לחיבורים בין קצה העורפי ל-Gemini, כי הנתיב הזה נחשב בדרך כלל למאובטח.

## מגבלות

בשלב הזה, טוקנים זמניים תואמים רק ל-[Live API](https://ai.google.dev/gemini-api/docs/live?hl=he).

## המאמרים הבאים

- מידע נוסף על טוקנים זמניים זמין [במאמר בנושא Live API](https://ai.google.dev/api/live?hl=he#ephemeral-auth-tokens).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-17 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-17 (שעון UTC)."],[],[]]
