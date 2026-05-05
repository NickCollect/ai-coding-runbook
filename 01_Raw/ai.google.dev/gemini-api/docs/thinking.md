---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=he
fetched_at: 2026-05-05T20:45:14.261858+00:00
title: "\u05d7\u05e9\u05d9\u05d1\u05d4 \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# חשיבה של Gemini

[למודלים מסדרות Gemini 3 ו-2.5](https://ai.google.dev/gemini-api/docs/models?hl=he) יש תהליך חשיבה פנימי שמשפר באופן משמעותי את יכולות החשיבה הרציונלית והתכנון שלהם, ולכן הם יעילים מאוד במשימות מורכבות כמו כתיבת קוד, מתמטיקה מתקדמת וניתוח נתונים.

במדריך הזה מוסבר איך להשתמש ביכולות החשיבה של Gemini באמצעות Gemini API.

## יצירת תוכן עם חשיבה

הגשת בקשה באמצעות מודל חשיבה דומה להגשת בקשה ליצירת תוכן. ההבדל העיקרי הוא שצריך לציין את אחד [המודלים עם תמיכה בחשיבה](#supported-models) בשדה `model`, כמו בדוגמה הבאה של [יצירת טקסט](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3-flash-preview"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## סיכומי מחשבות

סיכומי מחשבות הם גרסאות מסוכמות של המחשבות הגולמיות של המודל, והם מספקים תובנות לגבי תהליך ההיגיון הפנימי של המודל. חשוב לזכור שרמות החשיבה והתקציבים חלים על המחשבות הגולמיות של המודל ולא על סיכומי המחשבות.

כדי להפעיל סיכומי מחשבות, צריך להגדיר את `includeThoughts` לערך `true` בהגדרות הבקשה. אחר כך אפשר לגשת לסיכום על ידי איטרציה בפרמטר `response` של `parts` ובדיקה של הערך הבוליאני `thought`.

הנה דוגמה שמראה איך להפעיל את סיכומי המחשבות ולאחזר אותם בלי סטרימינג. בדוגמה הזו, המערכת מחזירה סיכום מחשבות סופי יחיד עם התגובה:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

דוגמה לשימוש ב-thinking with streaming, שמחזירה סיכומים מצטברים מתגלגלים במהלך היצירה:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3-flash-preview"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## שליטה בחשיבה

מודלים של Gemini חושבים באופן דינמי כברירת מחדל, ומתאימים אוטומטית את כמות המאמץ של ההסקה על סמך מורכבות הבקשה של המשתמש.
עם זאת, אם יש לכם אילוצים ספציפיים לגבי זמן האחזור או שאתם רוצים שהמודל יבצע חשיבה רציונלית מעמיקה יותר מהרגיל, אתם יכולים להשתמש בפרמטרים כדי לשלוט בהתנהגות החשיבה.

### רמות ההעמקה (Gemini 3)

הפרמטר `thinkingLevel`, שמומלץ לשימוש במודלים של Gemini 3 ואילך, מאפשר לכם לשלוט בהתנהגות של חשיבה רציונלית.

בטבלה הבאה מפורטות ההגדרות של `thinkingLevel` לכל סוג מודל:

| רמת ההעמקה | ‫Gemini 3.1 Pro | ‫Gemini 3.1 Flash-Lite | Gemini 3 Flash | תיאור |
| --- | --- | --- | --- | --- |
| **`minimal`** | לא נתמך | נתמך (ברירת מחדל) | נתמך | מתאים להגדרה 'ללא חשיבה' ברוב השאילתות. יכול להיות שהמודל יחשוב בצורה מינימלית מאוד על משימות מורכבות של כתיבת קוד. ממזער את זמן האחזור של אפליקציות צ'אט או אפליקציות עם תפוקה גבוהה. הערה: `minimal` לא מבטיח שהחשיבה מושבתת. |
| **`low`** | נתמך | נתמך | נתמך | מצמצם את זמן האחזור והעלות. הכי טוב למעקב אחרי הוראות פשוטות, לצ'אט או לאפליקציות עם תפוקה גבוהה. |
| **`medium`** | נתמך | נתמך | נתמך | חשיבה מאוזנת לרוב המשימות. |
| **`high`** | נתמך (ברירת מחדל, דינמי) | נתמך (דינמי) | נתמך (ברירת מחדל, דינמי) | העומק המקסימלי של החשיבה הרציונלית. יכול להיות שייקח למודל הרבה יותר זמן להגיע לטוקן הפלט הראשון (שאינו טוקן חשיבה), אבל הפלט יהיה מנומק יותר. |

בדוגמה הבאה אפשר לראות איך מגדירים את רמת החשיבה.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

אי אפשר להשבית את החשיבה של Gemini 3.1 Pro. בנוסף, במודלים Gemini 3 Flash ו-Flash-Lite אין תמיכה בהשבתה מלאה של התכונה 'חשיבה', אבל הגדרה של `minimal`
פירושה שהמודל כנראה לא יחשוב (אבל עדיין יש לו פוטנציאל לעשות זאת).
אם לא מציינים רמת חשיבה, Gemini ישתמש ברמת החשיבה הדינמית שמוגדרת כברירת מחדל במודלים של Gemini 3, ‏ `"high"`.

מודלים מסדרת Gemini 2.5 לא תומכים ב-`thinkingLevel`. במקום זאת, צריך להשתמש ב-`thinkingBudget`
.

### תקציבים לשיקול

הפרמטר `thinkingBudget`, שהוצג בסדרת Gemini 2.5, מכוון את המודל לגבי מספר האסימונים הספציפיים של החשיבה שבהם צריך להשתמש לצורך חשיבה רציונלית.

בהמשך מפורטים פרטי ההגדרה של כל סוג מודל.`thinkingBudget`
כדי להשבית את החשיבה, צריך להגדיר את `thinkingBudget` ל-0.
הגדרת הערך `thinkingBudget` כ-‎-1 מפעילה **חשיבה דינמית**, כלומר המודל ישנה את התקציב בהתאם למורכבות הבקשה.

| דגם | הגדרת ברירת המחדל (התקציב לא מוגדר) | טווח | השבתת תהליך החשיבה | הפעלת חשיבה דינמית |
| --- | --- | --- | --- | --- |
| ‫**2.5 Pro** | חשיבה דינמית | `128` עד `32768` | לא רלוונטי: אי אפשר להשבית את החשיבה | ‫`thinkingBudget = -1` (ברירת מחדל) |
| ‫**2.5 Flash** | חשיבה דינמית | `0` עד `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (ברירת מחדל) |
| **‫2.5 Flash Preview** | חשיבה דינמית | `0` עד `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (ברירת מחדל) |
| ‫**2.5 Flash Lite** | המודל לא חושב | `512` עד `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| ‫**2.5 Flash Lite Preview** | המודל לא חושב | `512` עד `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | חשיבה דינמית | `0` עד `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (ברירת מחדל) |
| ‫**2.5 Flash Live Native Audio Preview (09-2025)** | חשיבה דינמית | `0` עד `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (ברירת מחדל) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

בהתאם להנחיה, יכול להיות שהמודל יחרוג מהתקציב של הטוקנים או ישתמש בפחות טוקנים מהתקציב.

## חתימות של מחשבות

ממשק Gemini API הוא חסר מצב (stateless), ולכן המודל מתייחס לכל בקשת API באופן עצמאי ואין לו גישה להקשר של מחשבות משיחות קודמות באינטראקציות מרובות.

כדי לאפשר שמירה של הקשר המחשבתי באינטראקציות מרובות, Gemini מחזיר חתימות מחשבתיות, שהן ייצוגים מוצפנים של תהליך החשיבה הפנימי של המודל.

- **מודלים של Gemini 2.5** מחזירים חתימות של מחשבות כשהחשיבה מופעלת והבקשה כוללת [בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#thinking), ובמיוחד [הצהרות על פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#step-2).
- **מודלים של Gemini 3** עשויים להחזיר חתימות של מחשבות לכל סוגי [החלקים](https://ai.google.dev/api/caching?hl=he#Part).
  מומלץ תמיד להעביר את כל החתימות בחזרה כמו שהן התקבלו, אבל *חובה* לעשות את זה לחתימות של קריאות לפונקציות. מידע נוסף זמין בדף [חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=he).

הגבלות שימוש נוספות שכדאי לקחת בחשבון כשמשתמשים בהפעלת פונקציות:

- החתימות מוחזרות מהמודל בתוך חלקים אחרים בתגובה, למשל קריאה לפונקציה או חלקי טקסט.
  [החזרת התשובה המלאה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#step-4) עם כל החלקים למודל בתורות הבאות.
- אל תשרשרו חלקים עם חתימות יחד.
- אל תמזגו חלק אחד עם חתימה עם חלק אחר ללא חתימה.

## תמחור

כשהתכונה 'חשיבה' מופעלת, התמחור של התגובה הוא סכום האסימונים של הפלט והאסימונים של החשיבה. אפשר לקבל את המספר הכולל של טוקנים של חשיבה שנוצרו מהשדה `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

מודלים של חשיבה יוצרים מחשבות מלאות כדי לשפר את האיכות של התשובה הסופית, ואז יוצרים [סיכומים](#summaries) כדי לספק תובנות לגבי תהליך החשיבה. לכן, התמחור מבוסס על האסימונים המלאים של המחשבה שהמודל צריך ליצור כדי ליצור סיכום, למרות שרק הסיכום הוא הפלט של ה-API.

מידע נוסף על טוקנים זמין במדריך [ספירת טוקנים](https://ai.google.dev/gemini-api/docs/tokens?hl=he).

## שיטות מומלצות

בקטע הזה מופיעות כמה הנחיות לשימוש יעיל במודלים של חשיבה.
כמו תמיד, כדי להשיג את התוצאות הטובות ביותר, מומלץ לפעול לפי [ההנחיות והשיטות המומלצות שלנו לכתיבת הנחיות](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=he).

### ניפוי באגים והכוונה

- **בדיקת חשיבה רציונלית**: אם לא מקבלים את התשובה הרצויה מהמודלים החושבים, כדאי לנתח בקפידה את סיכומי החשיבה של Gemini.
  תוכלו לראות איך הוא פירק את המשימה והגיע למסקנה, ולהשתמש במידע הזה כדי לתקן את התוצאות.
- **מתן הנחיות לגבי תהליך החשיבה הרציונלית**: אם אתם רוצים לקבל פלט ארוך במיוחד, כדאי לתת הנחיות בהנחיה כדי להגביל את [כמות החשיבה](#set-budget) שהמודל משתמש בה. כך תוכלו להקצות יותר מהפלט של הטוקן לתגובה שלכם.

### מורכבות המשימה

- **משימות פשוטות (העמקה יכולה להיות מושבתת):** לבקשות פשוטות שלא דורשות חשיבה רציונלית מורכבת, כמו שליפת עובדות או סיווג, אין צורך בחשיבה. דוגמאות:
  - "?Where was DeepMind founded"
  - "האם האימייל הזה הוא הזמנה לפגישה או שהוא רק מספק מידע?"
- **משימות בינוניות (ברירת מחדל/חלק מהחשיבה):** הרבה בקשות נפוצות נהנות ממידה מסוימת של עיבוד שלב אחר שלב או מהבנה מעמיקה יותר. ‫Gemini יכול להשתמש ביכולת החשיבה באופן גמיש כדי לבצע משימות כמו:
  - השוואה בין פוטוסינתזה לבין גדילה.
  - השוו והבדילו בין מכוניות חשמליות למכוניות היברידיות.
- **משימות קשות (יכולת חשיבה מקסימלית):** כדי להתמודד עם אתגרים מורכבים במיוחד, כמו פתרון בעיות מתמטיות מסובכות או משימות תכנות, מומלץ להגדיר תקציב חשיבה גבוה. כדי לבצע את סוגי המשימות האלה, המודל צריך להשתמש בכל יכולות החשיבה הרציונלית והתכנון שלו, ולרוב הוא מבצע הרבה שלבים פנימיים לפני שהוא מספק תשובה. דוגמאות:
  - פתרון בעיה 1 ב-AIME 2025: צריך למצוא את הסכום של כל הבסיסים השלמים b > 9 שעבורם 17b הוא מחלק של 97b.
  - לכתוב קוד Python לאפליקציית אינטרנט שמציגה נתונים של שוק המניות בזמן אמת, כולל אימות משתמשים. להקפיד על יעילות מקסימלית.

## מודלים, כלים ויכולות נתמכים

תכונות החשיבה נתמכות בכל המודלים מסדרות 3 ו-2.5.
בדף [סקירה כללית של הדגם](https://ai.google.dev/gemini-api/docs/models?hl=he) אפשר לראות את כל היכולות של הדגם.

מודלים מסוג Thinking פועלים עם כל הכלים והיכולות של Gemini. היכולת הזו מאפשרת למודלים ליצור אינטראקציה עם מערכות חיצוניות, להריץ קוד או לגשת למידע בזמן אמת, ולשלב את התוצאות בהסקה ובתשובה הסופית שלהם.

אפשר לנסות דוגמאות לשימוש בכלים עם מודלים חושבים ב[ספר המתכונים של Thinking](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb?hl=he).

## מה השלב הבא?

- מידע על כיסוי המחשבה זמין במדריך שלנו בנושא [תאימות ל-OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=he#thinking).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
