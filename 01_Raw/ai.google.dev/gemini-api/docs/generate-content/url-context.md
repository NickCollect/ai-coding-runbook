---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=he
fetched_at: 2026-07-06T05:15:03.386378+00:00
title: "\u05d4\u05d4\u05e7\u05e9\u05e8 \u05e9\u05dc \u05db\u05ea\u05d5\u05d1\u05ea \u05d4-URL \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ההקשר של כתובת ה-URL

הכלי 'הקשר של כתובת URL' מאפשר לכם לספק למודלים הקשר נוסף בצורה של כתובות URL. אם תכללו כתובות URL בבקשה, המודל יוכל לגשת לתוכן מהדפים האלה (כל עוד כתובת ה-URL לא שייכת לסוג שמופיע [בקטע המגבלות](#limitations)) כדי לשפר את התשובה שלו.

הכלי 'הקשר של כתובת URL' שימושי למשימות כמו:

- **חילוץ נתונים**: שליפת מידע ספציפי כמו מחירים, שמות או ממצאים מרכזיים מכמה כתובות URL.
- **השוואת מסמכים**: ניתוח של כמה דוחות, מאמרים או קובצי PDF כדי לזהות הבדלים ולעקוב אחרי מגמות.
- **סינתזה ויצירת תוכן**: שילוב מידע מכמה כתובות URL של מקורות כדי ליצור סיכומים מדויקים, פוסטים בבלוג או דוחות.
- **ניתוח קוד ומסמכים**: אפשר להפנות למאגר GitHub או למסמכים טכניים כדי לקבל הסבר על קוד, ליצור הוראות הגדרה או לקבל תשובות לשאלות.

בדוגמה הבאה אפשר לראות איך משווים בין שני מתכונים מאתרים שונים.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## איך זה עובד

הכלי 'הקשר כתובת ה-URL' משתמש בתהליך אחזור דו-שלבי כדי לאזן בין מהירות, עלות וגישה לנתונים עדכניים. כשמספקים כתובת URL, הכלי מנסה קודם לשלוף את התוכן ממטמון אינדקס פנימי. הוא פועל כמטמון שעבר אופטימיזציה גבוהה. אם כתובת URL לא זמינה באינדקס (למשל, אם מדובר בדף חדש מאוד), הכלי יבצע באופן אוטומטי אחזור של הגרסה הפעילה.
הכלי ניגש ישירות לכתובת ה-URL כדי לאחזר את התוכן שלה בזמן אמת.

## שילוב עם כלים אחרים

אפשר לשלב את הכלי להקשר של כתובת URL עם כלים אחרים כדי ליצור תהליכי עבודה יעילים יותר.

[מודלים של Gemini 3](#supported-models) תומכים בשילוב של כלים מובנים (כמו הקשר של כתובת URL) עם כלים מותאמים אישית (הפעלת פונקציות). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

### עיגון בנתונים באמצעות חיפוש

אם מפעילים גם את ההגדרה 'הקשר של כתובת URL' וגם את ההגדרה [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he), המודל יכול להשתמש ביכולות החיפוש שלו כדי למצוא מידע רלוונטי באינטרנט, ואז להשתמש בכלי 'הקשר של כתובת URL' כדי לקבל הבנה מעמיקה יותר של הדפים שהוא מוצא. הגישה הזו יעילה במיוחד להנחיות שדורשות חיפוש רחב וניתוח מעמיק של דפים ספציפיים.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## הסבר על התשובה

כשהמודל משתמש בכלי ההקשר של כתובת ה-URL, התשובה כוללת אובייקט `url_context_metadata`. באובייקט הזה מפורטות כתובות ה-URL שהמודל אחזר מהן תוכן, והסטטוס של כל ניסיון אחזור. המידע הזה שימושי לאימות ולניפוי באגים.

זוהי דוגמה לחלק הזה של התגובה (השמטנו חלקים מהתגובה כדי שהיא תהיה קצרה יותר):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

לפרטים מלאים על האובייקט הזה , אפשר לעיין ב[הפניית API של `UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=he#UrlContextMetadata).

### בדיקות אבטחה

המערכת מבצעת בדיקה של ניהול התוכן בכתובת ה-URL כדי לוודא שהיא עומדת בתקני הבטיחות. אם כתובת ה-URL שסיפקתם תיכשל בבדיקה הזו, תקבלו הודעת שגיאה `url_retrieval_status` עם קוד `URL_RETRIEVAL_STATUS_UNSAFE`.

### ספירת הטוקנים

התוכן שאוחזר מכתובות ה-URL שציינתם בהנחיה נספר כחלק מאסימוני הקלט. אפשר לראות את מספר הטוקנים של ההנחיה והשימוש בכלים באובייקט [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=he#UsageMetadata) של פלט המודל. דוגמה לפלט:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

המחיר לכל טוקן תלוי במודל שבו משתמשים. פרטים נוספים זמינים בדף [התמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he).

## מודלים נתמכים

| מודל | ההקשר של כתובת ה-URL |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## שיטות מומלצות

- **צריך לספק כתובות URL ספציפיות**: כדי לקבל את התוצאות הטובות ביותר, צריך לספק כתובות URL ישירות לתוכן שרוצים שהמודל ינתח. המודל יאחזר תוכן רק מכתובות ה-URL שתספקו, ולא תוכן מקישורים מוטמעים.
- **בודקים את הנגישות**: מוודאים שכתובות ה-URL שציינתם לא מובילות לדפים שנדרשת בהם התחברות או שהם נמצאים מאחורי חומת תשלום.
- **שימוש בכתובת ה-URL המלאה**: צריך לציין את כתובת ה-URL המלאה, כולל הפרוטוקול (למשל, https://www.google.com ולא רק google.com).

## מגבלות

- קריאה לפונקציה: שימוש בכלי (הקשר של כתובת URL, עיגון באמצעות חיפוש Google וכו')
  עם קריאה לפונקציה לא נתמך כרגע.
- מגבלת בקשות: הכלי יכול לעבד עד 20 כתובות URL לכל בקשה.
- גודל התוכן של כתובת URL: הגודל המקסימלי של תוכן שאוחזר מכתובת URL יחידה הוא 34MB.
- נגישות לכולם: כתובות ה-URL צריכות להיות נגישות לכולם באינטרנט.
  אין תמיכה בכתובות localhost (לדוגמה, localhost,‏ 127.0.0.1), ברשתות פרטיות ובשירותי מנהור (לדוגמה, ngrok,‏ pinggy).
- ‫Gemini API בלבד: הקשר של כתובת ה-URL זמין רק ב-Gemini API, ולא דרך Gemini Enterprise Agent Platform.

### סוגי תוכן נתמכים ולא נתמכים

הכלי יכול לחלץ תוכן מכתובות URL עם סוגי התוכן הבאים:

- טקסט (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- תמונה (image/png, ‏ image/jpeg, ‏ image/bmp, ‏ image/webp)
- ‫PDF (application/pdf)

סוגי התוכן הבאים **לא** נתמכים:

- תוכן שזמין רק לאחר תשלום
- סרטונים ב-YouTube (במאמר בנושא [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he#youtube) מוסבר איך לעבד כתובות URL של סרטונים ב-YouTube)
- קבצים ב-Google Workspace, כמו מסמכים או גיליונות אלקטרוניים של Google
- קובצי וידאו ואודיו

## המאמרים הבאים

- אפשר לעיין ב[אוסף הפתרונות של הקשר כתובת ה-URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=he#url-context) כדי לראות דוגמאות נוספות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-23 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-23 (שעון UTC)."],[],[]]
