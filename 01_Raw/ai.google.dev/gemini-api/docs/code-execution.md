---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=he
fetched_at: 2026-06-22T06:31:19.659592+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הרצת קוד

‫Gemini API כולל כלי להרצת קוד שמאפשר למודל ליצור ולהריץ קוד Python. לאחר מכן המודל יכול ללמוד באופן איטרטיבי מתוצאות הביצוע של הקוד עד שהוא מגיע לפלט סופי. אתם יכולים להשתמש בהרצת קוד כדי ליצור אפליקציות שמרוויחות מחשיבה רציונלית מבוססת קוד. לדוגמה, אפשר להשתמש בהרצת קוד כדי לפתור משוואות או לעבד טקסט. אפשר גם להשתמש ב[ספריות](#supported-libraries) שכלולות בסביבת ההפעלה של הקוד כדי לבצע משימות ספציפיות יותר.

‫Gemini יכול להריץ קוד ב-Python בלבד. עדיין אפשר לבקש מ-Gemini ליצור קוד בשפה אחרת, אבל המודל לא יכול להשתמש בכלי להרצת קוד כדי להריץ אותו.

## הפעלת ביצוע קוד

כדי להפעיל את הרצת הקוד, צריך להגדיר את כלי הרצת הקוד במודל. כך המודל יכול ליצור ולהריץ קוד.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
}'
```

הפלט יכול להיראות כך, אחרי שעיצבנו אותו כדי שיהיה קל לקריאה:

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

הפלט הזה משלב כמה חלקי תוכן שהמודל מחזיר כשמשתמשים בהרצת קוד:

- ‫`text`: טקסט מוטבע שנוצר על ידי המודל
- ‫`executableCode`: קוד שנוצר על ידי המודל ומיועד להרצה
- `codeExecutionResult`: התוצאה של קוד ההפעלה

מוסכמות השמות של החלקים האלה משתנות בהתאם לשפת התכנות.

## הפעלת קוד עם תמונות (Gemini 3)

מודל Gemini 3 Flash יכול עכשיו לכתוב ולהריץ קוד Python כדי לשנות ולבדוק תמונות באופן פעיל.

**תרחישים לדוגמה**

- **זום ובדיקה**: המודל מזהה באופן מובנה מתי הפרטים קטנים מדי (למשל, קריאת מד מרחק) וכותב קוד לחיתוך ולבדיקה מחדש של האזור ברזולוציה גבוהה יותר.
- **מתמטיקה ויזואלית**: המודל יכול לבצע חישובים מרובי-שלבים באמצעות קוד (למשל, סיכום פריטים בקבלה).
- **הערות לתמונות**: המודל יכול להוסיף הערות לתמונות כדי לענות על שאלות, למשל לצייר חצים כדי להראות קשרים.

### הפעלת ביצוע קוד באמצעות תמונות

החל מ-Gemini 3 Flash, יש תמיכה רשמית בהרצת קוד עם תמונות. כדי להפעיל את ההתנהגות הזו, צריך להפעיל את ההגדרה 'הפעלת קוד ככלי' ואת ההגדרה 'חשיבה'.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
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
    "io"
    "log"
    "net/http"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.5-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## איך משתמשים בהרצת קוד בצ'אט

אפשר גם להשתמש בהרצת קוד כחלק משיחה.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3.5-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3.5-flash",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## קלט/פלט (I/O)

הפעלת קוד תומכת בקלט של קבצים ובפלט של גרפים. בעזרת היכולות האלה של קלט ופלט, אתם יכולים להעלות קובצי CSV וקובצי טקסט, לשאול שאלות לגבי הקבצים ולקבל תשובה שכוללת גרפים של [Matplotlib](https://matplotlib.org/). קבצי הפלט מוחזרים כתמונות מוטמעות בתשובה.

### תמחור של קלט/פלט

כשמשתמשים ב-I/O של ביצוע קוד, התשלום הוא על טוקנים של קלט וטוקנים של פלט:

**טוקנים של קלט:**

- הנחיה למשתמש

**טוקנים בפלט:**

- קוד שנוצר על ידי המודל
- פלט של הרצת קוד בסביבת הקוד
- טוקנים של חשיבה
- סיכום שנוצר על ידי המודל

### פרטי I/O

כשעובדים עם קלט/פלט של הרצת קוד, חשוב לשים לב לפרטים הטכניים הבאים:

- זמן הריצה המקסימלי של סביבת הקוד הוא 30 שניות.
- אם סביבת הקוד יוצרת שגיאה, יכול להיות שהמודל יחליט ליצור מחדש את פלט הקוד. המצב הזה יכול לקרות עד 5 פעמים.
- הגודל המקסימלי של קובץ קלט מוגבל על ידי חלון הטוקנים של המודל. ב-AI Studio, גודל הקובץ המקסימלי של קובץ קלט הוא מיליון טוקנים (בערך 2MB לקובצי טקסט מסוגי הקלט הנתמכים). אם תעלו קובץ גדול מדי, לא תוכלו לשלוח אותו ב-AI Studio.
- הכי טוב להשתמש בהרצת קוד עם קובצי טקסט ו-CSV.
- אפשר להעביר את קובץ הקלט בפורמט `part.inlineData` או `part.fileData` (העלאה דרך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he)), וקובץ הפלט תמיד מוחזר בפורמט `part.inlineData`.

## חיוב

אין עלות נוספת על הפעלת ביצוע קוד מ-Gemini API.
תחויבו לפי התעריף הנוכחי של טוקנים של קלט ופלט, בהתאם למודל Gemini שבו אתם משתמשים.

ריכזנו כאן כמה דברים נוספים שכדאי לדעת על חיוב על הפעלת קוד:

- אתם מחויבים רק פעם אחת על טוקני הקלט שאתם מעבירים למודל, ועל טוקני הפלט הסופי שהמודל מחזיר לכם.
- טוקנים שמייצגים קוד שנוצר נספרים כטוקנים של פלט. הקוד שנוצר יכול לכלול טקסט ופלט מולטי-מודאלי כמו תמונות.
- תוצאות של הרצת קוד נספרות גם הן כאסימוני פלט.

מודל החיוב מוצג בתרשים הבא:

![מודל חיוב על הרצת קוד](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=he)

- החיוב מתבצע לפי התעריף הנוכחי של טוקנים של קלט ופלט, בהתאם למודל Gemini שבו אתם משתמשים.
- אם Gemini משתמש בהרצת קוד כדי ליצור את התשובה, ההנחיה המקורית, הקוד שנוצר והתוצאה של הקוד שהורץ מסומנים בתווית *intermediate tokens* (טוקנים ביניים) והחיוב עליהם הוא כ*input tokens* (טוקנים של קלט).
- ‫Gemini יוצר סיכום ומחזיר את הקוד שנוצר, את התוצאה של הקוד שהופעל ואת הסיכום הסופי. הם מחויבים כ*אסימוני פלט*.
- תגובת ה-API של Gemini כוללת ספירה של אסימוני ביניים, כדי שתדעו למה אתם מקבלים אסימוני קלט נוספים מעבר להנחיה הראשונית.

## מגבלות

- המודל יכול רק ליצור ולהריץ קוד. הוא לא יכול להחזיר פריטים אחרים, כמו קובצי מדיה.
- במקרים מסוימים, הפעלת ביצוע קוד עלולה להוביל לרגרסיות בתחומים אחרים של פלט המודל (לדוגמה, כתיבת סיפור).
- יש הבדלים בין המודלים השונים ביכולת שלהם להשתמש בהרצת קוד בהצלחה.

## שילובים נתמכים של כלים

אפשר לשלב את הכלי להרצת קוד עם [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) כדי להפעיל תרחישי שימוש מורכבים יותר.

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו הפעלת קוד) עם כלים מותאמים אישית (הפעלת פונקציות). כדי שהשילוב של כלי העריכה יפעל, צריך להעביר בחזרה את השדות `id` ו-`thought_signature`. מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

## ספריות נתמכות

סביבת ההפעלה של הקוד כוללת את הספריות הבאות:

- attrs
- שחמט
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- מארז
- פנדות
- כרית
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- שש
- striprtf
- sympy
- לרכז בטבלה
- tensorflow
- toolz
- xlrd

אי אפשר להתקין ספריות משלכם.

## המאמרים הבאים

- אפשר לנסות את [הקוד להרצת Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=he).
- מידע על כלים אחרים של Gemini API:
  - [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
  - [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-19 (שעון UTC)."],[],[]]
