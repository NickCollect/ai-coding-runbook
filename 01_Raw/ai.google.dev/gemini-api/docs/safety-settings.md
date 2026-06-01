---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=he
fetched_at: 2026-06-01T05:59:59.888125+00:00
title: "\u05d4\u05d2\u05d3\u05e8\u05d5\u05ea \u05d1\u05d8\u05d9\u05d7\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הגדרות בטיחות

ממשק Gemini API מספק הגדרות בטיחות שאפשר לשנות בשלב יצירת אב טיפוס, כדי לקבוע אם האפליקציה דורשת הגדרת בטיחות מגבילה יותר או פחות. אתם יכולים לשנות את ההגדרות האלה בארבע קטגוריות של מסננים כדי להגביל סוגים מסוימים של תוכן או לאפשר אותם.

במדריך הזה מוסבר איך Gemini API מטפל בהגדרות בטיחות ובסינון, ואיך אפשר לשנות את הגדרות הבטיחות של האפליקציה.

## מסנני בטיחות

מסנני הבטיחות המתכווננים של Gemini API מכסים את הקטגוריות הבאות:

| קטגוריה | תיאור |
| --- | --- |
| הטרדה | תגובות שליליות או פוגעניות שמכוונות לזהות ו/או למאפיינים מוגנים. |
| דברי שטנה | תוכן גס, לא מכבד או חילול קודש. |
| תוכן מיני בוטה | מכיל התייחסויות למעשים מיניים או לתוכן מגונה אחר. |
| תוכן מסוכן | מקדם גרימת נזק, מעודד גרימת נזק או עוזר לבצע פעולות מזיקות. |

הקטגוריות האלה מוגדרות ב[`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=he). אפשר להשתמש במסננים האלה כדי להתאים את התוצאות למקרה השימוש שלכם. לדוגמה, אם אתם יוצרים דיאלוג למשחק וידאו, יכול להיות שתחליטו לאפשר יותר תוכן שסווג כ*מסוכן* בגלל אופי המשחק.

בנוסף למסנני הבטיחות שניתנים להתאמה, ל-Gemini API יש אמצעי הגנה מובנים מפני נזקים מהותיים, כמו תוכן שמסכן את בטיחות הילדים.
סוגי הנזק האלה תמיד נחסמים ואי אפשר לשנות את זה.

### רמת הסינון של בטיחות התוכן

‫Gemini API מסווג את רמת ההסתברות לכך שהתוכן לא בטוח כ-`HIGH`, `MEDIUM`, `LOW` או `NEGLIGIBLE`.

‫Gemini API חוסם תוכן על סמך הסבירות שהתוכן לא בטוח, ולא על סמך חומרת הבעיה. חשוב לקחת את זה בחשבון כי יש תכנים שהסיכוי שהם לא בטוחים הוא נמוך, אבל חומרת הנזק שעלולה להיגרם מהם עדיין גבוהה. לדוגמה, אם משווים בין המשפטים:

1. הרובוט נתן לי אגרוף.
2. הרובוט חתך אותי.

המשפט הראשון עלול להוביל לסבירות גבוהה יותר של תוצאה לא בטוחה, אבל יכול להיות שהמשפט השני ייחשב לחמור יותר מבחינת אלימות.
לכן, חשוב לבדוק בקפידה ולשקול מהי רמת החסימה המתאימה שנדרשת כדי לתמוך בתרחישי השימוש העיקריים שלכם, תוך מזעור הפגיעה במשתמשי הקצה.

### סינון בטיחות לכל בקשה

אתם יכולים לשנות את הגדרות הבטיחות לכל בקשה שאתם שולחים ל-API. כששולחים בקשה, התוכן נותח ומוקצה לו סיווג בטיחות. דירוג הבטיחות כולל את הקטגוריה ואת הסיווג של הסבירות לפגיעה. לדוגמה, אם התוכן נחסם כי הסבירות שהוא משתייך לקטגוריית ההטרדה גבוהה, דירוג הבטיחות שיוחזר יהיה עם קטגוריה ששווה ל-`HARASSMENT` וסבירות לפגיעה שמוגדרת כ-`HIGH`.

בגלל הבטיחות המובנית של המודל, מסננים נוספים **מושבתים** כברירת מחדל.
אם תבחרו להפעיל אותן, תוכלו להגדיר את המערכת לחסימת תוכן על סמך הסבירות שהוא לא בטוח. התנהגות ברירת המחדל של המודל מתאימה לרוב תרחישי השימוש, ולכן כדאי לשנות את ההגדרות האלה רק אם נדרשת עקביות באפליקציה.

בטבלה הבאה מתוארות הגדרות החסימה שאפשר לשנות לכל קטגוריה. לדוגמה, אם מגדירים את הגדרת החסימה ל**חסימה של חלק מהתוכן** בקטגוריה **דברי שטנה**, כל מה שיש לו סיכוי גבוה להיות תוכן של דברי שטנה ייחסם. אבל מותר להשתמש בכל ערך עם הסתברות נמוכה יותר.

| סף (Google AI Studio) | סף (API) | תיאור |
| --- | --- | --- |
| מושבת | `OFF` | השבתת מסנן הבטיחות |
| לא לחסום אף אחד | `BLOCK_NONE` | הצגה תמיד, ללא קשר להסתברות של תוכן לא בטוח |
| חסימה של כמה אנשים | `BLOCK_ONLY_HIGH` | חסימה כשיש סבירות גבוהה לתוכן לא בטוח |
| חסימת חלק מהמשתמשים | `BLOCK_MEDIUM_AND_ABOVE` | חסימה כשיש הסתברות בינונית או גבוהה לתוכן לא בטוח |
| חסימה של רוב האנשים | `BLOCK_LOW_AND_ABOVE` | חסימה כשההסתברות לתוכן לא בטוח נמוכה, בינונית או גבוהה |
| לא רלוונטי | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | לא צוין סף, חסימה באמצעות סף ברירת המחדל |

אם לא מגדירים את הסף, ברירת המחדל של סף החסימה היא **מושבת** למודלים של Gemini 2.5 ו-3.

אפשר להגדיר את ההגדרות האלה לכל בקשה ששולחים לשירות הגנרטיבי.
פרטים נוספים זמינים במאמר בנושא [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=he#harmblockthreshold) API.

### משוב בנושא בטיחות

‫[`generateContent`](https://ai.google.dev/api/generate-content?hl=he#method:-models.generatecontent)
מחזירה את
‫[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=he#generatecontentresponse) שכוללת משוב בנושא בטיחות.

המשוב על ההנחיות כלול ב-[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=he#promptfeedback). אם הערך של `promptFeedback.blockReason` מוגדר, סימן שהתוכן של ההנחיה נחסם.

המשוב על המועמדים לתשובה נכלל ב-[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=he#candidate) וב-[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=he#candidate). אם תוכן התשובה נחסם והערך של `finishReason` היה `SAFETY`, אפשר לבדוק את `safetyRatings` כדי לקבל פרטים נוספים. התוכן שנחסם לא יוחזר.

## שינוי הגדרות הבטיחות

בקטע הזה מוסבר איך לשנות את הגדרות הבטיחות ב-Google AI Studio ובקוד.

### Google AI Studio

אתם יכולים לשנות את הגדרות הבטיחות ב-Google AI Studio.

לוחצים על **הגדרות בטיחות** בקטע **הגדרות מתקדמות** בחלונית **הגדרות ההרצה** כדי לפתוח את תיבת הדו-שיח **הגדרות בטיחות של ההרצה**. בחלון הקופץ, אפשר להשתמש בפסי ההזזה כדי לשנות את רמת סינון התוכן לפי קטגוריית בטיחות:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=he)

כששולחים בקשה (למשל, שואלים את המודל שאלה), מופיעה ההודעה warning
**התוכן חסום** אם התוכן של הבקשה חסום. כדי לראות פרטים נוספים, מעבירים את מצביע העכבר מעל הטקסט **התוכן נחסם** כדי לראות את הקטגוריה ואת הסבירות לסיווג הנזק.

### דוגמאות לקוד

בקטע הקוד הבא מוצג איך מגדירים הגדרות בטיחות בקריאה ל-`GenerateContent`. הפעולה הזו מגדירה את ערך הסף לקטגוריה 'דברי שטנה' (`HARM_CATEGORY_HATE_SPEECH`). אם מגדירים את הקטגוריה הזו לערך
`BLOCK_LOW_AND_ABOVE`, כל תוכן שיש לו סבירות נמוכה או גבוהה יותר להיות דברי שטנה ייחסם. כדי להבין את הגדרות הסף, אפשר לעיין במאמר [סינון בטיחותי לכל בקשה](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,
    BlockThreshold.LOW_AND_ABOVE);

GenerativeModel gm = new GenerativeModel(
    "gemini-3.5-flash",
    BuildConfig.apiKey,
    null, // generation config is optional
    Arrays.asList(hateSpeechSafety)
);

GenerativeModelFutures model = GenerativeModelFutures.from(gm);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## השלבים הבאים

- מידע נוסף על ה-API המלא מופיע ב[הפניית ה-API](https://ai.google.dev/api?hl=he).
- כדאי לעיין ב[הנחיות הבטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he) כדי לקבל סקירה כללית של שיקולי הבטיחות כשמפתחים באמצעות מודלים של שפה גדולה (LLM).
- מידע נוסף על הערכת ההסתברות לעומת חומרת הבעיה זמין ב[צוות Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score)
- מידע נוסף על המוצרים שמשמשים לפתרונות בטיחות כמו [Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).
  \* אפשר להשתמש בהגדרות הבטיחות האלה כדי ליצור מסווג רעילות. כדי להתחיל, אפשר לעיין [בדוגמה של סיווג](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
