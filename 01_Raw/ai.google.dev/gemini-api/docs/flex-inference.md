---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=he
fetched_at: 2026-06-08T05:38:43.938020+00:00
title: "\u05d4\u05e1\u05e7\u05ea \u05de\u05e1\u05e7\u05e0\u05d5\u05ea \u05d2\u05de\u05d9\u05e9\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הסקת מסקנות גמישה

‫Gemini Flex API הוא מסלול היקש שמציע עלות נמוכה ב-50% בהשוואה לתעריפים הרגילים, בתמורה לזמן אחזור משתנה ולזמינות של 'הכי טוב שאפשר'. הוא מיועד לעומסי עבודה שסובלים השהיה ודורשים עיבוד סינכרוני, אבל לא צריכים את הביצועים בזמן אמת של ה-API הרגיל.

## איך משתמשים ב-Flex

כדי להשתמש בשכבת Flex, מציינים את `service_tier` כ-`flex` בגוף הבקשה. אם לא מציינים ערך בשדה הזה, בקשות משתמשות בשכבה הרגילה כברירת מחדל.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## איך פועל הסקת המסקנות הגמישה

ההסקה של Gemini Flex מגשרת על הפער בין ה-API הרגיל לבין זמן התגובה של 24 שעות של [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he). הוא משתמש בקיבולת מחשוב מחוץ לשעות השיא, שאפשר להקצות מחדש, כדי לספק פתרון חסכוני למשימות ברקע ולתהליכי עבודה רציפים.

| תכונה | שרירים של סלע | עדיפות | רגיל | Batch |
| --- | --- | --- | --- | --- |
| **תמחור** | הנחה של 50% | ‫75% עד 100% יותר מבתוכנית Standard | מחיר מלא | הנחה של 50% |
| **זמן אחזור** | דקות (יעד של 15-1 דקות) | נמוך (שניות) | שניות לדקות | עד 24 שעות |
| **אמינות** | ללא התחייבות (ניתן להשמטה) | גבוהה (לא ניתן להסרה) | גבוהה / בינונית-גבוהה | גבוהה (לתפוקה) |
| **ממשק** | סינכרוני | סינכרוני | סינכרוני | אסינכרוני |

### יתרונות עיקריים

- **יעילות בעלויות**: חיסכון משמעותי בהערכות שאינן בסביבת ייצור, בסוכני רקע ובהעשרת נתונים.
- **פשוט וקל**: לא צריך לנהל אובייקטים של קבוצות, מזהי משימות או בדיקות. פשוט מוסיפים פרמטר יחיד לבקשות הקיימות.
- **תהליכי עבודה סינכרוניים**: מתאימים לשרשראות API רציפות שבהן הבקשה הבאה תלויה בפלט של הבקשה הקודמת, ולכן הם גמישים יותר מ-Batch לתהליכי עבודה של סוכנים.

### תרחישים לדוגמה

- **הערכות אופליין**: הרצת בדיקות רגרסיה או טבלאות השוואה של מודלים גדולים של שפה (LLM) בתור שופטים.
- **סוכנים ברקע**: משימות רציפות כמו עדכוני CRM, בניית פרופילים או משימות של מודרציה של תוכן, שבהן עיכוב של כמה דקות הוא סביר.
- **מחקרים בהגבלת תקציב**: ניסויים אקדמיים שנדרש בהם נפח גבוה של טוקנים בהגבלת תקציב.

### מגבלות קצב

תנועת ההסקה של Flex נספרת במסגרת [מגבלות הקצב](https://aistudio.google.com/rate-limit?hl=he) הכלליות, ולא מוצעות לה מגבלות קצב מורחבות כמו ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he).

### קיבולת שניתן להקצות

התנועה הגמישה מקבלת עדיפות נמוכה יותר. אם יש עלייה חדה בתנועה הרגילה, יכול להיות שבקשות Flex יידחו או יבוטלו כדי להבטיח קיבולת למשתמשים בעדיפות גבוהה. אם אתם מחפשים הסקה בעדיפות גבוהה, כדאי לעיין במאמר בנושא [הסקה בעדיפות גבוהה](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)

### קודי שגיאה

אם הקיבולת הגמישה לא זמינה או שהמערכת עמוסה, ה-API יחזיר קודי שגיאה רגילים:

- ‫**503 השירות לא זמין**: יש כרגע עומס גדול מהרגיל.
- ‫**429 Too Many Requests**: חריגה ממגבלות קצב או ניצול יתר של משאבים.

### באחריות הלקוח

- **אין מעבר אוטומטי לגיבוי בצד השרת:** כדי למנוע חיובים לא צפויים, המערכת לא תשדרג אוטומטית בקשת Flex לרמה Standard אם קיבולת ה-Flex מלאה.
- **ניסיונות חוזרים**: אתם צריכים להטמיע לוגיקה משלכם לביצוע ניסיונות חוזרים בצד הלקוח, עם השהיה מעריכית לפני ניסיון חוזר (exponential backoff).
- **פסק זמן (timeout)**: בקשות Flex עשויות להמתין בתור, ולכן מומלץ להגדיל את פסק הזמן בצד הלקוח ל-10 דקות או יותר כדי למנוע סגירה מוקדמת של החיבור.

## שינוי חלונות הזמן הקצוב לתפוגה

אפשר להגדיר פסק זמן לכל בקשה עבור ה-API בארכיטקטורת REST וספריות הלקוח, ופסק זמן גלובלי רק כשמשתמשים בספריות הלקוח.

חשוב לוודא תמיד שזמן הקצוב לתפוגה בצד הלקוח מכסה את חלון הזמן המיועד להמתנה בשרת (לדוגמה, 600 שניות ומעלה לתורי המתנה של Flex). ערכי הזמן הקצוב לתפוגה ב-SDK צריכים להיות באלפיות שנייה.

### זמני קצוב לתפוגה לכל בקשה

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.5-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.5-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.5-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.5-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

כשמבצעים קריאות REST, אפשר לשלוט בערכי הזמן הקצוב לתפוגה באמצעות שילוב של כותרות HTTP ואפשרויות `curl`:

- **הכותרת `X-Server-Timeout` (זמן קצוב לתפוגה בצד השרת)**: הכותרת הזו מציעה משך זמן קצוב לתפוגה (ברירת מחדל 600 שניות) לשרת Gemini API. השרת ינסה לפעול בהתאם, אבל אין לכך ערובה. הערך צריך להיות בשניות.
- ‫**`--max-time` ב-`curl` (זמן קצוב לתפוגה בצד הלקוח)**: האפשרות `curl --max-time
  <seconds>` מגדירה מגבלה קשיחה על הזמן הכולל (בשניות) שבו `curl` ימתין עד להשלמת הפעולה כולה. זהו אמצעי הגנה מצד הלקוח.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### הגדרת פסק זמן גלובלי

אם רוצים שכל הקריאות ל-API שמתבצעות דרך מופע `genai.Client` ספציפי (רק בספריות לקוח) יכללו פסק זמן שמוגדר כברירת מחדל, אפשר להגדיר את זה כשמפעילים את הלקוח באמצעות `http_options` ו-`genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.5-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## הטמעה של ניסיונות חוזרים

‫Flex היא תכונה שאפשר להשבית, והיא נכשלת עם שגיאות 503. הנה דוגמה להטמעה אופציונלית של לוגיקה של ניסיון חוזר כדי להמשיך עם בקשות שנכשלו:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.5-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.5-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.5-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.5-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## תמחור

התמחור של Flex inference הוא 50% מ[ה-API הרגיל](https://ai.google.dev/gemini-api/docs/pricing?hl=he), והחיוב הוא לפי טוקן.

## מודלים נתמכים

המודלים הבאים תומכים בהסקת מסקנות גמישה:

| מודל | הסקת מסקנות גמישה |
| --- | --- |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| ‫[Gemini 3.1 Pro (גרסת טרום-השקה)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של תמונות ב-Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## המאמרים הבאים

אפשר לקרוא על אפשרויות נוספות של [היקש ואופטימיזציה](https://ai.google.dev/gemini-api/docs/optimization?hl=he) ב-Gemini:

- [הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he) לזמן טעינה קצר במיוחד.
- ‫[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he) לעיבוד אסינכרוני תוך 24 שעות.
- [שמירת מטמון של הקשר](https://ai.google.dev/gemini-api/docs/caching?hl=he) כדי להפחית את העלויות של טוקנים של קלט.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
