---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=he
fetched_at: 2026-09-28T06:32:36.995904+00:00
title: "\u05d4\u05e1\u05e7\u05ea \u05de\u05e1\u05e7\u05e0\u05d5\u05ea \u05d2\u05de\u05d9\u05e9\u05d4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הסקת מסקנות גמישה

‫Gemini Flex API הוא מסלול מחירים להסקת מסקנות שמציע הפחתה של 50% בעלויות בהשוואה למחירים הרגילים, בתמורה לזמן אחזור משתנה ולזמינות של 'הכי טוב שאפשר'. הוא מיועד לעומסי עבודה שסובלים השהיה ודורשים עיבוד סינכרוני, אבל לא דורשים את הביצועים בזמן אמת של ה-API הרגיל.

## איך משתמשים ב-Flex

כדי להשתמש במסלול Flex, מציינים את הערך `service_tier` כ-`flex` בבקשה. אם לא מציינים ערך בשדה הזה, כברירת מחדל הבקשות משתמשות ברמה הרגילה.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## איך פועל היקש ברמת Flex

היקש ברמת Flex של Gemini מגשר על הפער בין ה-API הרגיל לבין זמן התגובה של 24 שעות של [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he). הוא משתמש בקיבולת מחשוב 'ניתנת להפחתה' מחוץ לשעות השיא כדי לספק פתרון חסכוני למשימות ברקע ולתהליכי עבודה רציפים.

| תכונה | שרירים של סלע | עדיפות | רגיל | Batch |
| --- | --- | --- | --- | --- |
| **תמחור** | הנחה של 50% | ‫75% עד 100% יותר מבתוכנית Standard | מחיר מלא | הנחה של 50% |
| **זמן אחזור** | דקות (יעד של 1 עד 15 דקות) | נמוכה (שניות) | שניות לדקות | עד 24 שעות |
| **אמינות** | הטובה ביותר האפשרית (ניתן להשמטה) | גבוהה (לא נושרת) | גבוהה / בינונית-גבוהה | גבוהה (לתפוקה) |
| **ממשק** | סינכרוני | סינכרוני | סינכרוני | אסינכרוני |

### יתרונות עיקריים

- **יעילות בעלויות**: חיסכון משמעותי בהערכות שאינן בסביבת ייצור, בסוכני רקע ובהעשרת נתונים.
- **קלות שימוש**: פשוט מוסיפים פרמטר אחד לבקשות הקיימות.
- **תהליכי עבודה סינכרוניים**: מתאימים במיוחד לשרשראות רצופות של API שבהן הבקשה הבאה תלויה בפלט של הבקשה הקודמת, ולכן הם גמישים יותר מ-Batch לתהליכי עבודה אג'נטיים.

### תרחישים לדוגמה

- **הערכות אופליין**: הרצת בדיקות רגרסיה או טבלאות השוואה של מודלים גדולים של שפה (LLM) בתור שופטים.
- **סוכנים ברקע**: משימות רציפות כמו עדכוני CRM, בניית פרופילים או משימות של מודרציה של תוכן, שבהן עיכוב של כמה דקות הוא סביר.
- **מחקר בהגבלת תקציב**: ניסויים אקדמיים שנדרש בהם נפח גבוה של טוקנים בתקציב מוגבל.

### מגבלות קצב

היקש ברמת Flex נספר במסגרת [מגבלות הקצב](https://aistudio.google.com/rate-limit?hl=he) הכלליות, ולא במסגרת מגבלות קצב מורחבות כמו ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he).

### קיבולת שאפשר להקצות

התנועה הגמישה מקבלת עדיפות נמוכה יותר. אם יש עלייה חדה בתנועה הרגילה, יכול להיות שבקשות Flex יידחו או יבוטלו כדי להבטיח קיבולת למשתמשים בעדיפות גבוהה. אם אתם מחפשים הסקה בעדיפות גבוהה, כדאי לעיין במאמר בנושא [הסקה בעדיפות גבוהה](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he)

### קודי שגיאה

אם הקיבולת הגמישה לא זמינה או שהמערכת עמוסה, ה-API יחזיר קודי שגיאה רגילים:

- ‫**503 השירות לא זמין**: המערכת עמוסה כרגע.
- ‫**429 Too Many Requests**: חריגה ממגבלות קצב או ניצול יתר של משאבים.

### באחריות הלקוח

- **אין מעבר אוטומטי לגיבוי בצד השרת**: כדי למנוע חיובים לא צפויים, המערכת לא תשדרג אוטומטית בקשת Flex לרמה Standard אם קיבולת Flex מלאה.
- **ניסיונות חוזרים**: אתם צריכים להטמיע לוגיקה משלכם לביצוע ניסיונות חוזרים בצד הלקוח, עם השהיה מעריכית לפני ניסיון חוזר (exponential backoff).
- **פסק זמן (timeout)**: בקשות Flex עשויות להמתין בתור, ולכן מומלץ להגדיל את פסק הזמן בצד הלקוח ל-10 דקות או יותר כדי למנוע סגירה מוקדמת של החיבור.

## שינוי חלונות הזמן הקצוב לתפוגה

אפשר להגדיר פסק זמן לכל בקשה עבור API בארכיטקטורת REST וספריות לקוח.
חשוב לוודא תמיד שזמן הקצוב לתפוגה בצד הלקוח מכסה את חלון הזמן המיועד להמתנה בשרת (לדוגמה, 600 שניות ומעלה לתורי המתנה של Flex). ערכי הזמן הקצוב לפעילות בערכות ה-SDK צריכים להיות באלפיות שנייה.

### זמני קצוב לתפוגה לכל בקשה

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## הטמעה של ניסיונות חוזרים

‫Flex ניתן להסרה, והוא נכשל עם שגיאות 503. הנה דוגמה להטמעה אופציונלית של לוגיקה של ניסיון חוזר כדי להמשיך עם בקשות שנכשלו:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.8-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.8-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
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
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## תמחור

התמחור של היקש ברמת Flex הוא 50% מ[התמחור הרגיל של ה-API](https://ai.google.dev/gemini-api/docs/pricing?hl=he), והחיוב הוא לפי טוקן.

## מודלים נתמכים

המודלים הבאים תומכים בהיקש ברמת Flex:

| מודל | היקש ברמת Flex |
| --- | --- |
| ‫[Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=he) | ✔️ |
| ‫[Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=he) | ✔️ |
| ‫[Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=he) | ✔️ |
| ‫[Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=he) | ✔️ |
| ‫[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## המאמרים הבאים

- [הסקת עדיפות](https://ai.google.dev/gemini-api/docs/priority-inference?hl=he) לזמן אחזור נמוך במיוחד.
- [טוקנים](https://ai.google.dev/gemini-api/docs/tokens?hl=he): הסבר על טוקנים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-24 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-24 (שעון UTC)."],[],[]]
