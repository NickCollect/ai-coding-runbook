---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fa
fetched_at: 2026-10-12T06:53:40.504266+00:00
title: "\u062a\u0648\u0644\u06cc\u062f \u0646\u0648\u0634\u062a\u0627\u0631 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash اکنون در دسترس است. [آن را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fa) .

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# تولید نوشتار

«میانای برنامه‌سازی کاربردی Gemini» می‌تواند از ورودی‌های نوشتار، تصویر، ویدیو، و صدا برونداد نوشتاری تولید کند.

در اینجا یک مثال ساده آورده شده است:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How does AI work?"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How does AI work?",
  });
  console.log(response.text);
}

await main();
```

### رفتن

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

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Explain how AI works in a few words"),
      nil,
  )

  fmt.Println(result.Text())
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithTextInput {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "How does AI work?", null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## اندیشیدن با Gemini

مدل‌های Gemini اغلب به‌طور پیش‌فرض [«تفکر»](https://ai.google.dev/gemini-api/docs/thinking?hl=fa) را فعال دارند که به مدل اجازه می‌دهد قبل‌از پاسخ دادن به درخواست، استدلال کند.

هر مدل از پیکربندی‌های مختلف تفکر پشتیبانی می‌کند که به شما امکان می‌دهد
بر هزینه، تأخیر، و هوش کنترل داشته باشید. برای جزئیات بیشتر،
[راهنمای تفکر](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=fa#set-budget) را ببینید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How does AI work?",
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
    model: "gemini-3.8-flash",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    }
  });
  console.log(response.text);
}

await main();
```

### رفتن

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

  thinkingLevelVal := "low"

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("How does AI work?"),
      &genai.GenerateContentConfig{
        ThinkingConfig: &genai.ThinkingConfig{
            ThinkingLevel: &thinkingLevelVal,
        },
      }
  )

  fmt.Println(result.Text())
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.ThinkingConfig;
import com.google.genai.types.ThinkingLevel;

public class GenerateContentWithThinkingConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .thinkingConfig(ThinkingConfig.builder().thinkingLevel(new ThinkingLevel("low")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "How does AI work?", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "How does AI work?"
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

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'How AI does work?' },
        ],
      },
    ],
    generationConfig: {
      thinkingConfig: {
        thinkingLevel: 'low'
      }
    }
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## دستورالعمل‌های سیستم و پیکربندی‌های دیگر

می‌توانید رفتار مدل‌های Gemini را با دستورالعمل‌های سیستم هدایت کنید. برای انجام این کار،
شیء [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerationConfig)
را بگذرانید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko."),
    contents="Hello there"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Hello there",
    config: {
      systemInstruction: "You are a cat. Your name is Neko.",
    },
  });
  console.log(response.text);
}

await main();
```

### رفتن

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
      SystemInstruction: genai.NewContentFromText("You are a cat. Your name is Neko.", genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Hello there"),
      config,
  )

  fmt.Println(result.Text())
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithSystemInstruction {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config =
        GenerateContentConfig.builder()
            .systemInstruction(
                Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
            .build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "Hello there", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "system_instruction": {
      "parts": [
        {
          "text": "You are a cat. Your name is Neko."
        }
      ]
    },
    "contents": [
      {
        "parts": [
          {
            "text": "Hello there"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const systemInstruction = {
    parts: [{
      text: 'You are a cat. Your name is Neko.'
    }]
  };

  const payload = {
    systemInstruction,
    contents: [
      {
        parts: [
          { text: 'Hello there' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

شیء [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerationConfig)
همچنین به شما امکان می‌دهد پارامترهای تولید پیش‌فرض، مانند
[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerationConfig) را ملغی کنید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=["Explain how AI works"],
    config=types.GenerateContentConfig(
        max_output_tokens=1000
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works",
    config: {
      maxOutputTokens: 1000,
    },
  });
  console.log(response.text);
}

await main();
```

### رفتن

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
    MaxOutputTokens:   1000,
    ResponseMIMEType:  "application/json",
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    genai.Text("What is the average size of a swallow?"),
    config,
  )

  fmt.Println(result.Text())
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config = GenerateContentConfig.builder().maxOutputTokens(1000).build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", "Explain how AI works", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ],
    "generationConfig": {
      "stopSequences": [
        "Title"
      ],
      "maxOutputTokens": 1000
    }
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const generationConfig = {
    maxOutputTokens: 1000,
    responseFormat: { text: { mimeType: "text/plain" } },
  };

  const payload = {
    generationConfig,
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

برای فهرست کامل پارامترهای پیکربندی‌شدنی و توضیحات آن‌ها، به [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerationConfig)
در مرجع API ما مراجعه کنید.

## ورودی‌های چندحالته

«میانای برنامه‌سازی کاربردی Gemini» از ورودی‌های چندحالته پشتیبانی می‌کند و به شما امکان می‌دهد نوشتار را با فایل‌های رسانه‌ای ترکیب کنید. مثال زیر نحوه ارائه تصویر را نشان می‌دهد:

### Python

```
from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const image = await ai.files.upload({
    file: "/path/to/organ.png",
  });
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
      createUserContent([
        "Tell me about this instrument",
        createPartFromUri(image.uri, image.mimeType),
      ]),
    ],
  });
  console.log(response.text);
}

await main();
```

### رفتن

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

  imagePath := "/path/to/organ.jpg"
  imgData, _ := os.ReadFile(imagePath)

  parts := []*genai.Part{
      genai.NewPartFromText("Tell me about this instrument"),
      &genai.Part{
          InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imgData,
          },
      },
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

public class GenerateContentWithMultiModalInputs {
  public static void main(String[] args) {

    Client client = new Client();

    Content content =
      Content.fromParts(
          Part.fromText("Tell me about this instrument"),
          Part.fromUri("/path/to/organ.jpg", "image/jpeg"));

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.8-flash", content, null);

    System.out.println(response.text());
  }
}
```

### REST

```
# Use a temporary file to hold the base64 encoded image data
TEMP_B64=$(mktemp)
trap 'rm -f "$TEMP_B64"' EXIT
base64 $B64FLAGS $IMG_PATH > "$TEMP_B64"

# Use a temporary file to hold the JSON payload
TEMP_JSON=$(mktemp)
trap 'rm -f "$TEMP_JSON"' EXIT

cat > "$TEMP_JSON" << EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": "Tell me about this instrument"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "$(cat "$TEMP_B64")"
          }
        }
      ]
    }
  ]
}
EOF

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d "@$TEMP_JSON"
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const imageUrl = 'https://example.com/image.jpg';
  const image = getImageData(imageUrl);
  const payload = {
    contents: [
      {
        parts: [
          { image },
          { text: 'Tell me about this instrument' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}

function getImageData(url) {
  const blob = UrlFetchApp.fetch(url).getBlob();

  return {
    mimeType: blob.getContentType(),
    data: Utilities.base64Encode(blob.getBytes())
  };
}
```

برای روش‌های جایگزین ارائه تصاویر و پردازش تصویر پیشرفته‌تر،
به [راهنمای درک تصویر](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fa) ما مراجعه کنید.
این API از ورودی‌ها و درک [سند](https://ai.google.dev/gemini-api/docs/document-processing?hl=fa)،
[ویدیو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa)، و
[صوت](https://ai.google.dev/gemini-api/docs/audio?hl=fa) نیز پشتیبانی می‌کند.

## جاری‌سازی پاسخ‌ها

به‌طور پیش‌فرض، مدل تنها پس‌از تکمیل کل فرایند تولید پاسخ می‌دهد.

برای تعاملات روان‌تر، از جاری‌سازی برای دریافت
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerateContentResponse)
نمونه‌ها به‌صورت افزایشی درحین تولید شدن استفاده کنید.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works",
  });

  for await (const chunk of response) {
    console.log(chunk.text);
  }
}

await main();
```

### رفتن

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

  stream := client.Models.GenerateContentStream(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Write a story about a magic backpack."),
      nil,
  )

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentStream {
  public static void main(String[] args) {

    Client client = new Client();

    ResponseStream<GenerateContentResponse> responseStream =
      client.models.generateContentStream(
          "gemini-3.8-flash", "Write a story about a magic backpack.", null);

    for (GenerateContentResponse res : responseStream) {
      System.out.print(res.text());
    }

    // To save resources and avoid connection leaks, it is recommended to close the response
    // stream after consumption (or using try block to get the response stream).
    responseStream.close();
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## مکالمه‌های چندنوبتی (گپ)

«کیت‌های توسعه نرم‌افزار» ما قابلیت جمع‌آوری چندین دور پیام‌واره و پاسخ در گپ را فراهم می‌کنند و به شما روشی آسان برای پیگیری سابقه مکالمه ارائه می‌دهند.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.8-flash")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const response1 = await chat.sendMessage({
    message: "I have 2 dogs in my house.",
  });
  console.log("Chat response 1:", response1.text);

  const response2 = await chat.sendMessage({
    message: "How many paws are in my house?",
  });
  console.log("Chat response 2:", response2.text);
}

await main();
```

### رفتن

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

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
  res, _ := chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})

  if len(res.Candidates) > 0 {
      fmt.Println(res.Candidates[0].Content.Parts[0].Text)
  }
}
```

### جاوا

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversation {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.8-flash");

    GenerateContentResponse response =
        chatSession.sendMessage("I have 2 dogs in my house.");
    System.out.println("First response: " + response.text());

    response = chatSession.sendMessage("How many paws are in my house?");
    System.out.println("Second response: " + response.text());

    // Get the history of the chat session.
    // Passing 'true' to getHistory() returns the curated history, which excludes
    // empty or invalid parts.
    // Passing 'false' here would return the comprehensive history, including
    // empty or invalid parts.
    ImmutableList<Content> history = chatSession.getHistory(true);
    System.out.println("History: " + history);
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

از جاری‌سازی می‌توان برای مکالمه‌های چند نوبتی نیز استفاده کرد.

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.8-flash")

response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: [
      {
        role: "user",
        parts: [{ text: "Hello" }],
      },
      {
        role: "model",
        parts: [{ text: "Great to meet you. What would you like to know?" }],
      },
    ],
  });

  const stream1 = await chat.sendMessageStream({
    message: "I have 2 dogs in my house.",
  });
  for await (const chunk of stream1) {
    console.log(chunk.text);
    console.log("_".repeat(80));
  }

  const stream2 = await chat.sendMessageStream({
    message: "How many paws are in my house?",
  });
  for await (const chunk of stream2) {
    console.log(chunk.text);
    console.log("_".repeat(80));
  }
}

await main();
```

### رفتن

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

  history := []*genai.Content{
      genai.NewContentFromText("Hi nice to meet you! I have 2 dogs in my house.", genai.RoleUser),
      genai.NewContentFromText("Great to meet you. What would you like to know?", genai.RoleModel),
  }

  chat, _ := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
  stream := chat.SendMessageStream(ctx, genai.Part{Text: "How many paws are in my house?"})

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### جاوا

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversationWithStreaming {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.8-flash");

    ResponseStream<GenerateContentResponse> responseStream =
        chatSession.sendMessageStream("I have 2 dogs in my house.", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    responseStream = chatSession.sendMessageStream("How many paws are in my house?", null);

    for (GenerateContentResponse response : responseStream) {
      System.out.print(response.text());
    }

    // Get the history of the chat session. History is added after the stream
    // is consumed and includes the aggregated response from the stream.
    System.out.println("History: " + chatSession.getHistory(false));
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent?alt=sse \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Great to meet you. What would you like to know?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "I have two dogs in my house. How many paws are in my house?"
          }
        ]
      }
    ]
  }'
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const payload = {
    contents: [
      {
        role: 'user',
        parts: [
          { text: 'Hello' },
        ],
      },
      {
        role: 'model',
        parts: [
          { text: 'Great to meet you. What would you like to know?' },
        ],
      },
      {
        role: 'user',
        parts: [
          { text: 'I have two dogs in my house. How many paws are in my house?' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

## نکته‌های پیام‌واره

برای دریافت پیشنهادهایی درباره استفاده حداکثری از Gemini، به [راهنمای مهندسی پیام‌واره](https://ai.google.dev/gemini/docs/prompting-strategies?hl=fa) ما مراجعه کنید.

## قدم بعدی چیست

- ‫[Gemini در Google AI Studio](https://aistudio.google.com?hl=fa) را امتحان کنید.
- برای پاسخ‌های شبیه به JSON، [بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa) را آزمایش کنید.
- قابلیت‌های درک [تصویر](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fa)،
  [ویدیو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa)، [صدا](https://ai.google.dev/gemini-api/docs/audio?hl=fa)
  ، و [سند](https://ai.google.dev/gemini-api/docs/document-processing?hl=fa) Gemini را کاوش کنید.
- درباره
  [استراتژی‌های پیام‌واره فایل](https://ai.google.dev/gemini-api/docs/files?hl=fa#prompt-guide) چندوجهی بیشتر بدانید.

## تولید محتوا

این نقطه پایانی مرکزی برای ارسال پیام‌واره به مدل است. دو نقطه پایانی برای تولید محتوا وجود دارد، تفاوت اصلی در نحوه دریافت پاسخ است:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=fa#method:-models.generatecontent)
  (REST)**:
  درخواستی دریافت می‌کند و پس‌از اینکه مدل کل تولید خود را به‌پایان رساند،
  یک پاسخ واحد ارائه می‌دهد.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=fa#method:-models.streamgeneratecontent)
  (SSE)**: همان درخواست را دریافت می‌کند، اما مدل بخش‌هایی از پاسخ را به‌محض تولید جاری‌سازی می‌کند. این کار تجربه کاربری بهتری برای
  برنامه‌های تعاملی ارائه می‌دهد زیرا به شما امکان می‌دهد نتایج جزئی را بلافاصله نمایش دهید.

### ساختار متن درخواست

[بدنه درخواست](https://ai.google.dev/api/generate-content?hl=fa#request-body) یک شیء JSON است که برای هر دو حالت استاندارد و جاری‌سازی **یکسان** است و از چند شیء اصلی ساخته شده است:

- شیء [`Content`](https://ai.google.dev/api/caching?hl=fa#Content): نشان‌دهنده یک نوبت در مکالمه است.
- [`Part`](https://ai.google.dev/api/caching?hl=fa#Part) شیء: بخشی از داده‌ها در `Content` نوبت
  (مثل نوشتار یا تصویر).
- ‫`inline_data` ([`Blob`](https://ai.google.dev/api/caching?hl=fa#Blob)): محتوی بایت‌های رسانه خام
  و نوع MIME آن‌ها.

در بالاترین سطح، بدنه درخواست حاوی یک شیء `contents` است که فهرستی از اشیای `Content` است و هرکدام نشان‌دهنده نوبت در مکالمه است. در اکثر موارد، برای تولید نوشتار پایه، یک `Content` شیء خواهید داشت، اما اگر می‌خواهید سابقه مکالمه را حفظ کنید، می‌توانید از چندین `Content` شیء استفاده کنید.

در زیر، متن درخواست `generateContent` معمولی نشان داده شده است:

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
          "role": "user",
          "parts": [
              // A list of Part objects goes here
          ]
      },
      {
          "role": "model",
          "parts": [
              // A list of Part objects goes here
          ]
      }
    ]
  }'
```

### ساختار بدنه پاسخ

[بدنه پاسخ](https://ai.google.dev/api/generate-content?hl=fa#response-body) برای هر دو حالت جاری‌سازی و استاندارد مشابه است، به‌جز موارد زیر:

- حالت استاندارد: بدنه پاسخ حاوی نمونه‌ای از
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerateContentResponse) است.
- حالت جاری‌سازی: بدنه پاسخ حاوی جاری‌سازی
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerateContentResponse)
  نمونه است.

در سطح بالا، بدنه پاسخ حاوی یک شیء `candidates` است که
فهرستی از اشیای `Candidate` است. شیء `Candidate` حاوی شیء `Content`
است که پاسخ تولیدشده برگشتی از مدل را دارد.

## نمونه‌های REST API

### پیام‌واره چندحالته (نوشتار و تصویر)

برای ارائه هم نوشتار و هم تصویر در پیام‌واره، آرایه `parts` باید حاوی
دو شیء `Part` باشد: یکی برای نوشتار و یکی برای تصویر `inline_data`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{
    "parts":[
        {
            "inline_data": {
            "mime_type":"image/jpeg",
            "data": "/9j/4AAQSkZJRgABAQ... (base64-encoded image)"
            }
        },
        {"text": "What is in this picture?"},
      ]
    }]
  }'
```

### مکالمه‌های چندنوبتی (گپ)

برای ساختن مکالمه‌ای با چند نوبت، آرایه `contents` را با چند شیء `Content` تعریف می‌کنید. «میانای برنامه‌سازی کاربردی» از کل این سابقه به‌عنوان بافت
برای پاسخ بعدی استفاده خواهد کرد. `role` برای هر شیء `Content` باید بین `user` و `model` متناوب باشد.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          { "text": "Hello." }
        ]
      },
      {
        "role": "model",
        "parts": [
          { "text": "Hello! How can I help you today?" }
        ]
      },
      {
        "role": "user",
        "parts": [
          { "text": "Please write a four-line poem about the ocean." }
        ]
      }
    ]
  }'
```

### برداشت‌های کلیدی

- `Content` پاکت است: این پاکت ظرف سطح بالای پیام است،
  چه از کاربر باشد چه از مدل.
- `Part` امکان چندحالتی بودن را فراهم می‌کند: از چندین شیء `Part` در یک شیء `Content`
  استفاده کنید تا انواع مختلف داده‌ها (نوشتار، تصویر، نشانی وب ویدیو، و غیره) را ترکیب کنید.
- روش داده را انتخاب کنید:
  - برای رسانه‌های کوچک و مستقیماً جاسازی‌شده (مثل اکثر تصاویر)، از `Part` با
    `inline_data` استفاده کنید.
  - برای فایل‌های بزرگ‌تر یا فایل‌هایی که می‌خواهید در درخواست‌های مختلف از آن‌ها استفاده کنید، از
    File API برای بارگذاری فایل و ارجاع دادن به آن با بخش `file_data` استفاده کنید.
- مدیریت سابقه مکالمه: برای برنامه‌های گپ که از REST API استفاده می‌کنند،
  با پیوست کردن `Content` شیء برای هر نوبت، آرایه `contents` را بسازید و
  نقش‌های `"user"` و `"model"` را به‌صورت متناوب استفاده کنید. اگر از کیت توسعه نرم‌افزار استفاده می‌کنید،
  برای اطلاع از روش توصیه‌شده برای مدیریت
  سابقه مکالمه، به اسناد کیت توسعه نرم‌افزار مراجعه کنید.

## نمونه‌های پاسخ

مثال‌های زیر نشان می‌دهد که چگونه این عناصر برای انواع مختلف درخواست‌ها با هم ترکیب می‌شوند.

### پاسخ فقط نوشتاری

پاسخ نوشتاری پیش‌فرض از آرایه‌ای `candidates` با یک یا چند
`content` شیء تشکیل شده است که حاوی پاسخ مدل است.

در زیر نمونه‌ای از پاسخ **استاندارد** آورده شده است:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "At its core, Artificial Intelligence works by learning from vast amounts of data ..."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 1
    }
  ],
}
```

در ادامه، مجموعه‌ای از پاسخ‌های **جاری‌سازی** آمده است. هر پاسخ حاوی
`responseId` است که پاسخ کامل را به هم پیوند می‌دهد:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "The image displays"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  },
  "modelVersion": "gemini-3.8-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}

...

{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": " the following materials:\n\n*   **Wood:** The accordion and the violin are primarily"
          }
        ],
        "role": "model"
      },
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  }
  "modelVersion": "gemini-3.8-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## Live API (BidiGenerateContent) WebSockets API

‫Live API یک میانای برنامه‌سازی کاربردی مبتنی بر WebSocket حالت‌دار برای جاری‌سازی دوطرفه ارائه می‌دهد تا موارد استفاده از جاری‌سازی هم‌زمان را فعال کند. برای جزئیات بیشتر می‌توانید
[راهنمای Live API](https://ai.google.dev/gemini-api/docs/live?hl=fa) و [مرجع Live API](https://ai.google.dev/api/live?hl=fa)
را بررسی کنید.

## مدل‌های تخصصی

علاوه‌بر خانواده مدل‌های Gemini، «میانای برنامه‌سازی کاربردی Gemini» نقطه‌های پایانی برای مدل‌های تخصصی مثل [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)،
[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=fa)، و مدل‌های
[جاسازی](https://ai.google.dev/gemini-api/docs/embeddings?hl=fa) ارائه می‌دهد. می‌توانید این راهنماها را در بخش «مدل‌ها» بررسی کنید.

## میاناهای برنامه‌سازی کاربردی پلاتفرم

بقیه نقطه‌های پایانی قابلیت‌های بیشتری را برای استفاده با نقطه‌های پایانی اصلی که تاکنون توضیح داده شده است فعال می‌کنند. برای کسب اطلاعات بیشتر، موضوعات
[حالت دسته‌ای](https://ai.google.dev/gemini-api/docs/batch-mode?hl=fa) و
[میانای برنامه‌سازی کاربردی فایل](https://ai.google.dev/gemini-api/docs/files?hl=fa) را در بخش «راهنماها» بررسی کنید.

## قدم بعدی چیست

اگر تازه شروع کرده‌اید، راهنماهای زیر را بررسی کنید که به شما کمک می‌کند
مدل برنامه‌نویسی «میانای برنامه‌سازی کاربردی Gemini» را درک کنید:

- [راهنمای شروع کار با Gemini API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [راهنمای مدل Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa)

همچنین می‌توانید راهنمای قابلیت‌ها را بررسی کنید که ویژگی‌های مختلف
Gemini API را معرفی می‌کند و نمونه‌های کد ارائه می‌دهد:

- [تولید نوشتار](https://ai.google.dev/gemini-api/docs/text-generation?hl=fa)
- [ذخیره کردن بافت در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa)
- [جاسازی‌ها](https://ai.google.dev/gemini-api/docs/embeddings?hl=fa)

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی."],[],[]]
