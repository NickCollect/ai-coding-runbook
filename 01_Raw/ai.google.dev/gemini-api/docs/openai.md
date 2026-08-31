---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=he
fetched_at: 2026-08-31T06:36:21.656696+00:00
title: "\u05ea\u05d0\u05d9\u05de\u05d5\u05ea \u05dc-OpenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# תאימות ל-OpenAI

אפשר לגשת למודלים של Gemini באמצעות ספריות OpenAI (Python ו-TypeScript / Javascript) ו-API בארכיטקטורת REST. כדי לעשות זאת, צריך לעדכן שלוש שורות קוד ולהשתמש ב[מפתח Gemini API](https://aistudio.google.com/apikey?hl=he). אם אתם עדיין לא משתמשים בספריות של OpenAI, מומלץ להתקשר ישירות אל [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=he).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

מה השתנה? רק שלוש שורות!

- ‫**`api_key="GEMINI_API_KEY"`**: מחליפים את `GEMINI_API_KEY` במפתח Gemini API בפועל, שאפשר לקבל ב-[Google AI Studio](https://aistudio.google.com?hl=he).
- ‫**`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** הפרמטר הזה מציין לספריית OpenAI לשלוח בקשות לנקודת קצה ל-API של Gemini במקום לכתובת ה-URL שמוגדרת כברירת מחדל.
- ‫**`model="gemini-3.5-flash"`**: בחירת מודל Gemini תואם

## העמקה

המודלים של Gemini מאומנים לחשוב על פתרון בעיות מורכבות, וכתוצאה מכך יכולות החשיבה הרציונלית שלהם משופרות באופן משמעותי. ‫Gemini API כולל [פרמטרים של חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he) שמאפשרים שליטה מדויקת ברמת החשיבה של המודל.

למודלים שונים של Gemini יש הגדרות שונות של יכולות חשיבה רציונלית. אפשר לראות איך הם ממופים למאמצי החשיבה הרציונלית של OpenAI באופן הבא:

| ‫`reasoning_effort` (OpenAI) | ‫`thinking_level` (Gemini 3.1 Pro) | ‫`thinking_level` (Gemini 3.1 Flash-Lite) | ‫`thinking_level` (Gemini 3 Flash) | ‫`thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

אם לא מציינים `reasoning_effort`, Gemini משתמש ב[רמה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#levels) או ב[תקציב](https://ai.google.dev/gemini-api/docs/thinking?hl=he#set-budget) ברירת המחדל של המודל.

אם רוצים להשבית את התכונה 'חשיבה', אפשר להגדיר את `reasoning_effort` לערך `"none"` עבור מודלים של 2.5. אי אפשר להשבית את החשיבה הרציונלית במודלים Gemini 2.5 Pro או 3.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    reasoning_effort: "low",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

מודלים של חשיבה ב-Gemini יוצרים גם [סיכומי מחשבות](https://ai.google.dev/gemini-api/docs/thinking?hl=he#summaries).
אתם יכולים להשתמש בשדה [`extra_body`](#extra-body) כדי לכלול שדות של Gemini בבקשה.

שימו לב: הפונקציונליות של `reasoning_effort` ושל `thinking_level`/`thinking_budget` חופפת, ולכן אי אפשר להשתמש בהן בו-זמנית.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": "Explain to me how AI works"}],
    extra_body={
      'extra_body': {
        "google": {
          "thinking_config": {
            "thinking_level": "low",
            "include_thoughts": True
          }
        }
      }
    }
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [{role: "user", content: "Explain to me how AI works",}],
    extra_body: {
      "google": {
        "thinking_config": {
          "thinking_level": "low",
          "include_thoughts": true
        }
      }
    }
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
        "messages": [{"role": "user", "content": "Explain to me how AI works"}],
        "extra_body": {
          "google": {
            "thinking_config": {
              "thinking_level": "low",
              "include_thoughts": true
            }
          }
        }
      }'
```

‫Gemini 3 תומך בתאימות ל-OpenAI לחתימות מחשבה בממשקי API להשלמת צ'אט. דוגמה מלאה מופיעה בדף [חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=he#openai).

## סטרימינג

‫Gemini API תומך ב[הזרמת תשובות](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=he#generate-a-text-stream).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {   "role": "user",
        "content": "Hello!"
    }
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
          "role": "system",
          "content": "You are a helpful assistant."
      },
      {
          "role": "user",
          "content": "Hello!"
      }
    ],
    stream: true,
  });

  for await (const chunk of completion) {
    console.log(chunk.choices[0].delta.content);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## בקשה להפעלת פונקציה

התכונה 'קריאה לפונקציה' מאפשרת לקבל בקלות פלט של נתונים מובְנים ממודלים גנרטיביים, והיא [נתמכת ב-Gemini API](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=he).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}]
response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}];
  const tools = [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. Chicago, IL",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
          },
        }
      }
  ];

  const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: messages,
    tools: tools,
    tool_choice: "auto",
  });

  console.log(response);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Chicago today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. Chicago, IL"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

## הבנת תמונות

מודלים של Gemini הם מולטימודאליים באופן טבעי, ומספקים את הביצועים הכי טובים בכיתה ב[משימות ראייה נפוצות רבות](https://ai.google.dev/gemini-api/docs/vision?hl=he).

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

### JavaScript

```
import OpenAI from "openai";
import fs from 'fs/promises';

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function encodeImage(imagePath) {
  try {
    const imageBuffer = await fs.readFile(imagePath);
    return imageBuffer.toString('base64');
  } catch (error) {
    console.error("Error encoding image:", error);
    return null;
  }
}

async function main() {
  const imagePath = "Path/to/agi/image.jpeg";
  const base64Image = await encodeImage(imagePath);

  const messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": `data:image/jpeg;base64,${base64Image}`
          },
        },
      ],
    }
  ];

  try {
    const response = await openai.chat.completions.create({
      model: "gemini-3.5-flash",
      messages: messages,
    });

    console.log(response.choices[0]);
  } catch (error) {
    console.error("Error calling Gemini API:", error);
  }
}

main();
```

### REST

```
bash -c '
  base64_image=$(base64 -i "Path/to/agi/image.jpeg");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"What is in this image?\" },
            {
              \"type\": \"image_url\",
              \"image_url\": { \"url\": \"data:image/jpeg;base64,${base64_image}\" }
            }
          ]
        }
      ]
    }"
'
```

## יצירת תמונה

יוצרים תמונה באמצעות `gemini-2.5-flash-image` או `gemini-3-pro-image-preview`. הפרמטרים הנתמכים כוללים את `prompt`,‏ `model`,‏ `n`,‏ `size` ו-`response_format`. פרמטרים אחרים שלא מפורטים כאן או בקטע [`extra_body`](#extra-body) יקבלו התעלמות שקטה בשכבת התאימות.

### Python

```
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="a portrait of a sheepadoodle wearing a cape",
    response_format='b64_json',
    n=1,
)

for image_data in response.data:
  image = Image.open(BytesIO(base64.b64decode(image_data.b64_json)))
  image.show()
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const image = await openai.images.generate(
    {
      model: "gemini-2.5-flash-image",
      prompt: "a portrait of a sheepadoodle wearing a cape",
      response_format: "b64_json",
      n: 1,
    }
  );

  console.log(image.data);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
        "model": "gemini-2.5-flash-image",
        "prompt": "a portrait of a sheepadoodle wearing a cape",
        "response_format": "b64_json",
        "n": 1,
      }'
```

## יצירת סרטון

יצירת סרטון באמצעות `veo-3.1-generate-preview` דרך נקודת הקצה שתואמת ל-Sora.
`/v1/videos` הפרמטרים הנתמכים ברמה העליונה הם `prompt` ו-`model`. צריך להעביר פרמטרים נוספים כמו `duration_seconds`,‏ `image` ו-`aspect_ratio` עם `extra_body`. בקטע [`extra_body`](#extra-body) מפורטים כל הפרמטרים הזמינים.

יצירת סרטון היא פעולה ממושכת שמחזירה מזהה פעולה שאפשר לבדוק כדי לראות אם היא הסתיימה.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Returns a Long Running Operation (status: processing)
response = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="A cinematic drone shot of a waterfall",
)

print(f"Operation ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Returns a Long Running Operation (status: processing)
    const response = await openai.videos.create({
        model: "veo-3.1-generate-preview",
        prompt: "A cinematic drone shot of a waterfall",
    });

    console.log(`Operation ID: ${response.id}`);
    console.log(`Status: ${response.status}`);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=A cinematic drone shot of a waterfall"
```

### בדיקת סטטוס הסרטון

יצירת הסרטון היא אסינכרונית. משתמשים ב-`GET /v1/videos/{id}` כדי לבדוק את הסטטוס ולאחזר את כתובת ה-URL הסופית של הסרטון כשהפעולה מסתיימת:

### Python

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Poll until video is ready
video_id = response.id  # From the create call
while True:
    video = client.videos.retrieve(video_id)
    if video.status == "completed":
        print(f"Video URL: {video.url}")
        break
    elif video.status == "failed":
        print(f"Generation failed: {video.error}")
        break
    print(f"Status: {video.status}. Waiting...")
    time.sleep(10)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Poll until video is ready
    const videoId = response.id;  // From the create call
    while (true) {
        const video = await openai.videos.retrieve(videoId);
        if (video.status === "completed") {
            console.log(`Video URL: ${video.url}`);
            break;
        } else if (video.status === "failed") {
            console.log(`Generation failed: ${video.error}`);
            break;
        }
        console.log(`Status: ${video.status}. Waiting...`);
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos/VIDEO_ID" \
  -H "Authorization: Bearer $GEMINI_API_KEY"
```

## הבנת אודיו

ניתוח קלט אודיו:

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("/path/to/your/audio/file.wav", "rb") as audio_file:
  base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio",
        },
        {
              "type": "input_audio",
              "input_audio": {
                "data": base64_audio,
                "format": "wav"
          }
        }
      ],
    }
  ],
)

print(response.choices[0].message.content)
```

### JavaScript

```
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

const audioFile = fs.readFileSync("/path/to/your/audio/file.wav");
const base64Audio = Buffer.from(audioFile).toString("base64");

async function main() {
  const response = await client.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Transcribe this audio",
          },
          {
            type: "input_audio",
            input_audio: {
              data: base64Audio,
              format: "wav",
            },
          },
        ],
      },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### REST

```
bash -c '
  base64_audio=$(base64 -i "/path/to/your/audio/file.wav");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"Transcribe this audio file.\" },
            {
              \"type\": \"input_audio\",
              \"input_audio\": {
                \"data\": \"${base64_audio}\",
                \"format\": \"wav\"
              }
            }
          ]
        }
      ]
    }"
'
```

## פלט מובנה

מודלים של Gemini יכולים להפיק אובייקטים מסוג JSON בכל [מבנה שתגדירו](https://ai.google.dev/gemini-api/docs/structured-output?hl=he).

### Python

```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### JavaScript

```
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai"
});

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.chat.completions.parse({
  model: "gemini-3.5-flash",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## הטמעות

הטמעות טקסט מודדות את הקשר בין מחרוזות טקסט, ואפשר ליצור אותן באמצעות [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=he). אפשר להשתמש ב-`gemini-embedding-2-preview` להטמעות מולטימודאליות או ב-`gemini-embedding-001` להטמעות של טקסט בלבד.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="gemini-embedding-2-preview"
)

print(response.data[0].embedding)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const embedding = await openai.embeddings.create({
    model: "gemini-embedding-2-preview",
    input: "Your text string goes here",
  });

  console.log(embedding);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/embeddings" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
    "input": "Your text string goes here",
    "model": "gemini-embedding-2-preview"
  }'
```

## Batch API

אתם יכולים ליצור [עבודות באצווה](https://ai.google.dev/gemini-api/docs/batch-mode?hl=he), לשלוח אותן ולבדוק את הסטטוס שלהן באמצעות ספריית OpenAI.

תצטרכו להכין את קובץ ה-JSONL בפורמט הקלט של OpenAI. לדוגמה:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

תאימות ל-OpenAI עבור Batch תומכת ביצירת אצווה, במעקב אחר סטטוס המשימה ובהצגת תוצאות האצווה.

תאימות להעלאה ולהורדה אינה נתמכת כרגע. במקום זאת, בדוגמה הבאה נעשה שימוש בלקוח `genai` להעלאה ולהורדה של [קבצים](https://ai.google.dev/gemini-api/docs/files?hl=he), כמו בשימוש ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=he#input-file) של Gemini.

### Python

```
from openai import OpenAI

# Regular genai client for uploads & downloads
from google import genai
client = genai.Client()

openai_client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Upload the JSONL file in OpenAI input format, using regular genai SDK
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

# Create batch
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Wait for batch to finish (up to 24h)
while True:
    batch = client.batches.retrieve(batch.id)
    if batch.status in ('completed', 'failed', 'cancelled', 'expired'):
        break
    print(f"Batch not finished. Current state: {batch.status}. Waiting 30 seconds...")
    time.sleep(30)
print(f"Batch finished: {batch}")

# Download results in OpenAI output format, using regular genai SDK
file_content = genai_client.files.download(file=batch.output_file_id).decode('utf-8')

# See batch_output JSONL in OpenAI output format
for line in file_content.splitlines():
    print(line)
```

‫OpenAI SDK תומך גם ב[יצירת הטמעות באמצעות Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he#batch-embeddings). כדי לעשות את זה, מחליפים את השדה `endpoint` של השיטה `create` בנקודת קצה של הטמעה, וגם את המפתחות `url` ו-`model` בקובץ JSONL:

```
# JSONL file using embeddings model and endpoint
# {"custom_id": "request-1", "method": "POST", "url": "/v1/embeddings", "body": {"model": "ggemini-embedding-001", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
# {"custom_id": "request-2", "method": "POST", "url": "/v1/embeddings", "body": {"model": "gemini-embedding-001", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}

# ...

# Create batch step with embeddings endpoint
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/embeddings",
    completion_window="24h"
)
```

דוגמה מלאה מופיעה בקטע [Batch embedding generation](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb) (יצירת הטמעה של קבוצת נתונים) במדריך התאימות של OpenAI.

## הסקת מסקנות לגבי Flex ועדיפות

הפרמטר `service_tier` ב-Gemini API זהה לפרמטר `service_tier` ב-OpenAI בשם ובלוגיקה, ומאפשר לאכוף מגבלות ולנתב תעבורה בצורה חלקה בשתי רמות ההיקש: Flex ו-Priority.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

אם לא מקצים ערך במפורש, ברירת המחדל של `service_tier` היא `standard`, ששווה ל-`default` ב-OpenAI.
מידע נוסף על רמות של הסקה זמין במסמכי התיעוד בנושא [אופטימיזציה](https://ai.google.dev/gemini-api/docs/optimization?hl=he).

## הפעלת התכונות של Gemini באמצעות `extra_body`

יש כמה תכונות שנתמכות על ידי Gemini ולא זמינות במודלים של OpenAI, אבל אפשר להפעיל אותן באמצעות השדה `extra_body`.

| פרמטר | סוג | נקודת קצה | תיאור |
| --- | --- | --- | --- |
| **`cached_content`** | טקסט | צ'אט | מתאים למטמון התוכן הכללי של Gemini. |
| **`thinking_config`** | אובייקט | צ'אט | תואם ל-ThinkingConfig של Gemini. |
| **`aspect_ratio`** | טקסט | תמונות | יחס גובה-רוחב של הפלט (לדוגמה, `"16:9"`, ‏ `"1:1"`, ‏ `"9:16"`). |
| **`generation_config`** | אובייקט | תמונות | אובייקט הגדרות של יצירה באמצעות Gemini (לדוגמה, `{"responseModalities": ["IMAGE"], "candidateCount": 2}`). |
| **`safety_settings`** | רשימה | תמונות | מסננים של סף בטיחות בהתאמה אישית (לדוגמה, `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`). |
| **`tools`** | רשימה | תמונות | הפעלת ביסוס (לדוגמה, `[{"google_search": {}}]`). רק ל-`gemini-3-pro-image-preview`. |
| **`aspect_ratio`** | טקסט | וידאו | מידות סרטון הפלט (`16:9` לרוחב, `9:16` לאורך). אם לא מציינים ערך, ברירת המחדל היא מפות מ-`size`. |
| **`resolution`** | טקסט | וידאו | רזולוציית הפלט (`720p`, `1080p`, `4K`). הערה: `1080p` ו-`4K` מפעילים את צינור העיבוד של הגדלת הרזולוציה. |
| **`duration_seconds`** | מספר שלם | וידאו | אורך היצירה (ערכים: `4`,‏ `6`,‏ `8`). הערך חייב להיות `8` כשמשתמשים ב-`reference_images`, באינטרפולציה או בהרחבה. |
| **`frame_rate`** | טקסט | וידאו | קצב הפריימים של פלט הווידאו (למשל, `"24"`). |
| **`input_reference`** | טקסט | וידאו | קלט של קובץ עזר ליצירת סרטונים. |
| **`extend_video_id`** | טקסט | וידאו | מזהה של סרטון קיים שרוצים להאריך. |
| **`negative_prompt`** | טקסט | וידאו | פריטים להחרגה (לדוגמה, `"shaky camera"`). |
| **`seed`** | מספר שלם | וידאו | מספר שלם ליצירה דטרמיניסטית. |
| **`style`** | טקסט | וידאו | עיצוב חזותי (`cinematic` ברירת מחדל, `creative` אופטימיזציה לרשתות חברתיות). |
| **`person_generation`** | טקסט | וידאו | אמצעי בקרה ליצירת תמונות של אנשים (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | רשימה | וידאו | עד 3 תמונות לדוגמה של סגנון או דמות (נכסי base64). |
| **`image`** | טקסט | וידאו | תמונת קלט ראשונית בקידוד Base64 כדי להתנות את יצירת הסרטון. |
| **`last_frame`** | אובייקט | וידאו | תמונה סופית לאינטרפולציה (נדרש `image` כפריים הראשון). |

### דוגמה לשימוש ב-`extra_body`

דוגמה לשימוש ב-`extra_body` כדי להגדיר את `cached_content`:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.5-flash",
    n=1,
    messages=[
        {
            "role": "user",
            "content": "Summarize the video"
        }
    ],
    stream=True,
    stream_options={'include_usage': True},
    extra_body={
        'extra_body':
        {
            'google': {
              'cached_content': "cachedContents/0000aaaa1111bbbb2222cccc3333dddd4444eeee"
          }
        }
    }
)

for chunk in stream:
    print(chunk)
    print(chunk.usage.to_dict())
```

## רשימת המודלים

כדי לקבל רשימה של מודלים זמינים של Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

models = client.models.list()
for model in models:
  print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## אחזור מודל

שליפת מודל Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.5-flash")
print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3.5-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.5-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## מגבלות נוכחיות

התמיכה בספריות של OpenAI עדיין בגרסת בטא, בזמן שאנחנו מרחיבים את התמיכה בתכונות.

אם יש לכם שאלות לגבי פרמטרים נתמכים, תכונות חדשות או בעיות בהתחלת השימוש ב-Gemini, אתם מוזמנים להצטרף ל[פורום המפתחים](https://discuss.ai.google.dev/c/gemini-api/4?hl=he) שלנו.

## המאמרים הבאים

כדי לראות דוגמאות מפורטות יותר, אפשר לנסות את [התאימות ל-OpenAI ב-Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-22 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-22 (שעון UTC)."],[],[]]
