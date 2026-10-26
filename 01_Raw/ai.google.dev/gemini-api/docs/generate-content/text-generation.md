---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar
fetched_at: 2026-10-26T05:49:37.977207+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0627\u0644\u0646\u0635 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# إنشاء النص

يمكن لواجهة Gemini API إنشاء نصوص من خلال إدخال نصوص وصور وفيديوهات وملفات صوتية.

إليك مثال أساسي:

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

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      genai.Text("Explain how AI works in a few words"),
      nil,
  )

  fmt.Println(result.Text())
}
```

### جافا

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

### برمجة التطبيقات

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

## التفكير باستخدام Gemini

غالبًا ما تكون ميزة ["المفكّر"](https://ai.google.dev/gemini-api/docs/thinking?hl=ar) مفعَّلة تلقائيًا في نماذج Gemini، ما يتيح للنموذج الاستدلال قبل الردّ على طلب.

يتيح كل نموذج إعدادات تفكير مختلفة تمنحك التحكّم في التكلفة ووقت الاستجابة والذكاء. لمزيد من التفاصيل، يُرجى الاطّلاع على
[دليل التفكير](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar#set-budget).

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

### جافا

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

### برمجة التطبيقات

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

## تعليمات النظام والإعدادات الأخرى

يمكنك توجيه سلوك نماذج Gemini باستخدام تعليمات النظام. لإجراء ذلك،
مرِّر عنصر [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerationConfig).

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

### جافا

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

### برمجة التطبيقات

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

يتيح لك عنصر [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerationConfig) أيضًا إلغاء مَعلمات الإنشاء التلقائية، مثل [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerationConfig) أو [`thinking_config`](https://ai.google.dev/api/generate-content?hl=ar#ThinkingConfig).

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

### جافا

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

### برمجة التطبيقات

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');

function main() {
  const generationConfig = {
    maxOutputTokens: 1000,
    responseFormat: { text: { mimeType: "TEXT_PLAIN" } },
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

راجِع [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerationConfig) في مرجع واجهة برمجة التطبيقات للحصول على قائمة كاملة بالمعلّمات القابلة للإعداد وأوصافها.

## إدخالات متعددة الوسائط

تتيح Gemini API استخدام الإدخالات المتعددة الوسائط، ما يسمح لك بدمج النصوص مع ملفات الوسائط. يوضّح المثال التالي كيفية تقديم صورة:

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

### جافا

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

### برمجة التطبيقات

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

للاطّلاع على طرق بديلة لتقديم الصور ومعالجة الصور بشكل أكثر تقدّمًا،
يمكنك مراجعة [دليل فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar).
تتيح واجهة برمجة التطبيقات أيضًا إدخال وفهم [المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar) و[الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar) و[الملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar).

## عرض الردود تدريجيًا

بشكل تلقائي، يعرض النموذج ردًا فقط بعد اكتمال عملية الإنشاء بالكامل.

للحصول على تفاعلات أكثر سلاسة، يمكنك استخدام ميزة البث لتلقّي نُسخ
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerateContentResponse)
بشكل تدريجي أثناء إنشائها.

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

### جافا

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

### برمجة التطبيقات

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

## المحادثات المتعددة الأدوار (المحادثة)

توفّر حزم تطوير البرامج (SDK) وظائف لجمع جولات متعددة من الطلبات
والردود في محادثة، ما يمنحك طريقة سهلة لتتبُّع سجلّ
المحادثة.

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

### جافا

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

### برمجة التطبيقات

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

يمكن أيضًا استخدام البث للمحادثات المتعددة الجولات.

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

### جافا

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

### برمجة التطبيقات

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

## نصائح حول الطلبات

يمكنك مراجعة [دليل هندسة الطلبات](https://ai.google.dev/gemini/docs/prompting-strategies?hl=ar) للحصول على اقتراحات حول كيفية الاستفادة إلى أقصى حدّ من Gemini.

## الخطوات التالية

- جرِّب [Gemini في Google AI Studio](https://aistudio.google.com?hl=ar).
- جرِّب [المخرجات المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) للحصول على ردود بتنسيق JSON.
- استكشِف إمكانات Gemini في فهم [الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar) و[الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar) و[الملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar) و[المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar).
- تعرَّف على [استراتيجيات الطلبات المتعلقة بالملفات](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide)
  المتعددة الوسائط.

## إنشاء المحتوى

هذه هي نقطة النهاية المركزية لإرسال الطلبات إلى النموذج. هناك نقطتا نهاية لإنشاء المحتوى، والفرق الرئيسي بينهما هو كيفية تلقّي الردّ:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=ar#method:-models.generatecontent)
  (REST)**:
  يتلقّى طلبًا ويقدّم
  ردًا واحدًا بعد أن ينتهي النموذج من عملية الإنشاء بالكامل.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=ar#method:-models.streamgeneratecontent)
  (SSE)**: يتلقّى الطلب نفسه
  بالضبط، ولكن النموذج يعرض أجزاء من الردّ أثناء
  إنشائها. يوفّر ذلك تجربة أفضل للمستخدم في التطبيقات التفاعلية، لأنّه يتيح لك عرض نتائج جزئية على الفور.

### بنية نص الطلب

[نص الطلب](https://ai.google.dev/api/generate-content?hl=ar#request-body) هو عنصر JSON **متطابق** لكل من الوضع العادي ووضع البث، ويتم إنشاؤه من بعض العناصر الأساسية:

- [`Content`](https://ai.google.dev/api/caching?hl=ar#Content): يمثّل دورًا واحدًا في
  محادثة.
- [عنصر `Part`](https://ai.google.dev/api/caching?hl=ar#Part): هو جزء من البيانات ضمن دورة `Content` (مثل نص أو صورة).
- ‫`inline_data` ([`Blob`](https://ai.google.dev/api/caching?hl=ar#Blob)): حاوية لوحدات بايت الوسائط الأولية
  ونوع MIME الخاص بها

على أعلى مستوى، يحتوي نص الطلب على عنصر `contents`، وهو عبارة عن قائمة بعناصر `Content`، يمثّل كل منها دورًا في المحادثة. في معظم الحالات، لإنشاء نص أساسي، سيكون لديك كائن `Content` واحد، ولكن إذا أردت الاحتفاظ بسجلّ المحادثات، يمكنك استخدام كائنات `Content` متعددة.

في ما يلي نموذج لطلب `generateContent`:

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

### بنية نص الاستجابة

يتشابه [نص الاستجابة](https://ai.google.dev/api/generate-content?hl=ar#response-body) في كل من وضع البث والوضع العادي باستثناء ما يلي:

- الوضع العادي: يحتوي نص الاستجابة على مثال [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerateContentResponse).
- وضع العرض التدريجي: يحتوي نص الاستجابة على سلسلة من مثيلات [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ar#v1beta.GenerateContentResponse).

بشكل عام، يحتوي نص الاستجابة على عنصر `candidates`، وهو عبارة عن قائمة بعناصر `Candidate`. يحتوي الكائن `Candidate` على الكائن `Content` الذي يتضمّن الردّ الذي أنشأه النموذج.

## أمثلة على REST API

### طلب متعدّد الوسائط (نص وصورة)

لتوفير نص وصورة في الطلب، يجب أن تحتوي مصفوفة `parts` على عنصرَين من النوع `Part`: أحدهما للنص والآخر للصورة `inline_data`.

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

### المحادثات المترابطة (الدردشة)

لإنشاء محادثة تتضمّن عدة أدوار، عليك تحديد مصفوفة `contents` التي تتضمّن عدة عناصر `Content`. ستستخدم واجهة برمجة التطبيقات سجلّ المحادثات بالكامل هذا كسياق للرد التالي. يجب أن تتناوب قيمة `role` لكل عنصر `Content` بين `user` و`model`.

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

### الخلاصات الرئيسية

- ‫`Content` هو المغلّف: وهو الحاوية ذات المستوى الأعلى لدور الرسالة،
  سواء كانت من المستخدم أو النموذج.
- يتيح `Part` استخدام الوسائط المتعددة: يمكنك استخدام عدة عناصر `Part` ضمن عنصر
  `Content`
  واحد لدمج أنواع مختلفة من البيانات (النص والصورة ومعرّف الموارد المنتظم للفيديو وما إلى ذلك).
- اختَر طريقة البيانات:
  - بالنسبة إلى الوسائط الصغيرة المضمّنة مباشرةً (مثل معظم الصور)، استخدِم `Part` مع `inline_data`.
  - بالنسبة إلى الملفات الأكبر حجمًا أو الملفات التي تريد إعادة استخدامها في طلبات متعددة، استخدِم
    File API لتحميل الملف والإشارة إليه باستخدام جزء `file_data`.
- إدارة سجلّ المحادثات: بالنسبة إلى تطبيقات المحادثة التي تستخدم REST API، يمكنك إنشاء
  مصفوفة `contents` من خلال إلحاق عناصر `Content` لكل دور،
  والتبديل بين دورَي `"user"` و`"model"`. إذا كنت تستخدم حزمة SDK، يُرجى الرجوع إلى مستندات حزمة SDK لمعرفة الطريقة المقترَحة لإدارة سجلّ المحادثات.

## أمثلة على الردود

توضح الأمثلة التالية كيفية تجميع هذه المكونات معًا لأنواع مختلفة من الطلبات.

### ردّ نصي فقط

يتكوّن الردّ النصي التلقائي من مصفوفة `candidates` تحتوي على عنصر `content` واحد أو أكثر يتضمّن ردّ النموذج.

في ما يلي مثال على ردّ **عادي**:

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

في ما يلي سلسلة من الردود **المتتابعة**. يحتوي كل ردّ على
`responseId` يربط الردّ الكامل معًا:

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

## واجهة برمجة التطبيقات Live API ‏ (BidiGenerateContent) وWebSockets API

توفّر Live API واجهة برمجة تطبيقات مستندة إلى WebSocket مع الاحتفاظ بالبيانات للبث الثنائي الاتجاه، ما يتيح حالات استخدام البث في الوقت الفعلي. يمكنك مراجعة
[دليل Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) و[مرجع واجهة برمجة التطبيقات Live](https://ai.google.dev/api/live?hl=ar)
لمزيد من التفاصيل.

## النماذج المتخصّصة

بالإضافة إلى مجموعة نماذج Gemini، توفّر Gemini API نقاط نهاية لنماذج متخصّصة، مثل [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) و[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar) ونماذج [التضمين](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar). يمكنك الاطّلاع على هذه الأدلة ضمن قسم "نماذج".

## واجهات برمجة التطبيقات للمنصة

تتيح نقاط النهاية المتبقية إمكانات إضافية يمكن استخدامها مع نقاط النهاية الرئيسية الموضّحة حتى الآن. يمكنك الاطّلاع على موضوعَي
[وضع الدفعات](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ar) و[File API](https://ai.google.dev/gemini-api/docs/files?hl=ar) في قسم "الأدلة" لمزيد من المعلومات.

## الخطوات التالية

إذا كنت في بداية رحلتك، يمكنك الاطّلاع على الأدلة التالية التي ستساعدك في فهم نموذج برمجة Gemini API:

- [دليل البدء في Gemini API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [دليل نماذج Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar)

يمكنك أيضًا الاطّلاع على أدلة الإمكانات التي تعرض ميزات مختلفة في Gemini API وتقدّم أمثلة على الرموز البرمجية:

- [إنشاء النص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar)
- [التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
