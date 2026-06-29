---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=he
fetched_at: 2026-06-29T05:39:29.388067+00:00
title: "\u05d4\u05e1\u05e7\u05ea \u05e2\u05d3\u05d9\u05e4\u05d5\u05ea \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הסקת עדיפות

תיאור: איך מבצעים אופטימיזציה של זמן האחזור באמצעות רמת ההסקה Priority

‫Gemini Priority API הוא מסלול פרימיום להסקת מסקנות, שמיועד לעומסי עבודה קריטיים לעסק שדורשים זמן אחזור נמוך ואמינות גבוהה ביותר, במחיר פרימיום. תעבורת נתונים ברמת עדיפות גבוהה מקבלת עדיפות על פני תעבורת נתונים של API רגיל ושל רמת Flex.

הסקת עדיפות זמינה למשתמשי [Tier 2 ו-Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=he#about-billing) בנקודות הקצה של GenerateContent API ו-Interactions API.

## איך משתמשים בעדיפות

כדי להשתמש ברמת העדיפות, מגדירים את השדה `service_tier` בגוף הבקשה ל-`priority`. אם השדה לא מצוין, רמת ברירת המחדל היא רגילה.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.5-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
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
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## איך פועל הסקת עדיפות

הסקת עדיפות מפנה בקשות לתורים של מחשוב ברמת קריטיות גבוהה, ומציעה ביצועים מהירים וצפויים לאפליקציות שפונות למשתמשים. המנגנון העיקרי שלו הוא שדרוג לאחור בצד השרת לעיבוד רגיל של תנועה שחורגת מהמגבלות הדינמיות, כדי להבטיח את יציבות האפליקציה במקום לגרום לכשל בבקשה.

| תכונה | עדיפות | רגיל | שרירים של סלע | Batch |
| --- | --- | --- | --- | --- |
| **תמחור** | ‫75% עד 100% יותר מבתוכנית Standard | מחיר מלא | 50% הנחה | 50% הנחה |
| **זמן אחזור** | שניות | שניות לדקות | דקות (יעד של 15-1 דקות) | עד 24 שעות |
| **אמינות** | גבוהה (לא ניתן להסרה) | גבוהה / בינונית-גבוהה | ללא התחייבות (ניתן להשמטה) | גבוהה (לתפוקה) |
| **ממשק** | סינכרוני | סינכרוני | סינכרוני | אסינכרוני |

### יתרונות עיקריים

- **זמן אחזור נמוך**: מיועד לזמני תגובה של שנייה אחת עבור כלי AI אינטראקטיביים שפונים למשתמשים.
- **אמינות גבוהה**: התנועה מטופלת ברמת קריטיות גבוהה ביותר, ואין אפשרות להפחית אותה.
- **הפחתה הדרגתית של רמת השירות**: אם יש עליות פתאומיות בתנועה שחורגות מהמגבלות הדינמיות, המערכת מורידה אוטומטית את רמת השירות לרמה רגילה לצורך עיבוד, במקום שהעיבוד ייכשל. כך נמנעים שיבושים בשירות.
- **חיכוך נמוך**: משתמש באותה שיטה סינכרונית `generateContent` כמו בתוכניות הרגילה והגמישה.

### תרחישים לדוגמה

עיבוד בעדיפות גבוהה מתאים במיוחד לתהליכי עבודה קריטיים לעסק שבהם הביצועים והמהימנות הם בעלי חשיבות עליונה.

- **אפליקציות אינטראקטיביות מבוססות-AI**: צ'אט-בוטים וטייסים וירטואליים לשירות לקוחות שבהם המשתמשים משלמים מחיר פרימיום ומצפים לתשובות מהירות ועקביות.
- **מנועי החלטות בזמן אמת**: מערכות שנדרשים בהן תוצאות מהימנות עם זמן אחזור נמוך, כמו תעדוף כרטיסים בשידור חי או זיהוי הונאות.
- **תכונות ללקוחות פרימיום**: מפתחים שצריכים להבטיח יעדים גבוהים יותר למדידת רמת השירות (SLO) ללקוחות משלמים.

### הגבלות קצב

לצריכה בעדיפות יש מגבלות קצב משלה, גם אם הצריכה נספרת במסגרת [מגבלות הקצב הכוללות של תנועה אינטראקטיבית](https://aistudio.google.com/rate-limit?hl=he). מגבלות ברירת המחדל על קצב הבקשות להסקת עדיפות הן **0.3x ממגבלת קצב הבקשות הרגילה לדגם או לרמת השירות**

### לוגיקה של שדרוג לאחור

אם יש עומס ומתרחשת חריגה ממגבלות העדיפות, הבקשות העודפות **משודרגות אוטומטית בצורה חלקה** לעיבוד רגיל במקום להיכשל עם שגיאה 503 או 429. בקשות ששודרגו לאחור יחויבו בתעריף הרגיל, ולא בתעריף הפרימיום של Priority.

### באחריות הלקוח

- **מעקב אחר תגובות**: מפתחים צריכים לעקוב אחרי `x-gemini-service-tier`
  הכותרת בתגובת ה-API כדי לזהות אם הבקשות משודרגות לעיתים קרובות ל`standard`.
- **ניסיונות חוזרים**: לקוחות צריכים להטמיע לוגיקה של ניסיונות חוזרים או השהיה מעריכית לפני ניסיון חוזר (exponential backoff) לשגיאות רגילות, כמו `DEADLINE_EXCEEDED`.

## תמחור

המחיר של הסקת עדיפות גבוה ב-75% עד 100% מהמחיר של [ה-API הרגיל](https://ai.google.dev/gemini-api/docs/pricing?hl=he), והחיוב הוא לפי טוקן.

## מודלים נתמכים

המודלים הבאים תומכים בהסקת מסקנות בעדיפות גבוהה:

| מודל | הסקת עדיפות |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של תמונות ב-Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## המאמרים הבאים

מידע נוסף על אפשרויות אחרות של [הסקת מסקנות ואופטימיזציה](https://ai.google.dev/gemini-api/docs/optimization?hl=he) ב-Gemini:

- [הסקת מסקנות לגבי גמישות](https://ai.google.dev/gemini-api/docs/flex-inference?hl=he) כדי להפחית את העלות ב-50%.
- ‫[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he) לעיבוד אסינכרוני תוך 24 שעות.
- [שמירת מטמון של ההקשר](https://ai.google.dev/gemini-api/docs/caching?hl=he) כדי להפחית את העלויות של טוקנים של קלט.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-23 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-23 (שעון UTC)."],[],[]]
