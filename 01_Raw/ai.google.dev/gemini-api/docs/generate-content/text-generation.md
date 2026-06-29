---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja
fetched_at: 2026-06-29T05:29:50.535165+00:00
title: "Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# テキスト生成

Gemini API は、テキスト、画像、動画、音声の入力からテキスト出力を生成できます。

基本的な例を以下に示します。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      genai.Text("Explain how AI works in a few words"),
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithTextInput {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.5-flash", "How does AI work?", null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

## Gemini を使用した思考

Gemini モデルでは、多くの場合、[「思考」](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)がデフォルトで有効になっています
。これにより、モデルはリクエストに応答する前に推論できます。

各モデルは、さまざまな思考構成をサポートしており、費用、レイテンシ、インテリジェンスを制御できます。詳細については、
[思考ガイド](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#set-budget)をご覧ください。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
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

### Java

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
        client.models.generateContent("gemini-3.5-flash", "How does AI work?", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

## システム指示とその他の構成

システム指示を使用して、Gemini モデルの動作をガイドできます。これを行うには、
[`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerationConfig)
オブジェクトを渡します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      genai.Text("Hello there"),
      config,
  )

  fmt.Println(result.Text())
}
```

### Java

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
        client.models.generateContent("gemini-3.5-flash", "Hello there", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

[`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerationConfig)
オブジェクトを使用すると、
[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerationConfig)などのデフォルトの生成パラメータをオーバーライドすることもできます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
    "gemini-3.5-flash",
    genai.Text("What is the average size of a swallow?"),
    config,
  )

  fmt.Println(result.Text())
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentWithConfig {
  public static void main(String[] args) {

    Client client = new Client();

    GenerateContentConfig config = GenerateContentConfig.builder().maxOutputTokens(1000).build();

    GenerateContentResponse response =
        client.models.generateContent("gemini-3.5-flash", "Explain how AI works", config);

    System.out.println(response.text());
  }
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

構成可能なパラメータとその
説明の完全なリストについては、API リファレンスの [`GenerateContentConfig`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerationConfig)
をご覧ください。

## マルチモーダル入力

Gemini API はマルチモーダル入力をサポートしており、テキストとメディア ファイルを組み合わせることができます。次の例は、画像を提供する方法を示しています。

### Python

```
from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("/path/to/organ.png")
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### Java

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
        client.models.generateContent("gemini-3.5-flash", content, null);

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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

画像の提供方法や高度な画像処理については、
[画像理解ガイド](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)をご覧ください。
この API は、[ドキュメント](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)、[動画](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)、[音声](https://ai.google.dev/gemini-api/docs/audio?hl=ja)
の入力と理解もサポートしています。

## ストリーミング レスポンス

デフォルトでは、モデルは生成プロセス全体が完了した後にのみレスポンスを返します。

よりスムーズなインタラクションを実現するには、ストリーミングを使用して、[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerateContentResponse) インスタンスが生成されるたびに増分で受信します。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      genai.Text("Write a story about a magic backpack."),
      nil,
  )

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class GenerateContentStream {
  public static void main(String[] args) {

    Client client = new Client();

    ResponseStream<GenerateContentResponse> responseStream =
      client.models.generateContentStream(
          "gemini-3.5-flash", "Write a story about a magic backpack.", null);

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent?alt=sse" \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent';
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

## マルチターンの会話（チャット）

SDK には、複数ラウンドのプロンプトとレスポンスをチャットに収集する機能が用意されているため、会話履歴を簡単に追跡できます。

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash")

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
    model: "gemini-3.5-flash",
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

  chat, _ := client.Chats.Create(ctx, "gemini-3.5-flash", nil, history)
  res, _ := chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})

  if len(res.Candidates) > 0 {
      fmt.Println(res.Candidates[0].Content.Parts[0].Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversation {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.5-flash");

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
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent';
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

ストリーミングは、マルチターンの会話にも使用できます。

### Python

```
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash")

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
    model: "gemini-3.5-flash",
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

  chat, _ := client.Chats.Create(ctx, "gemini-3.5-flash", nil, history)
  stream := chat.SendMessageStream(ctx, genai.Part{Text: "How many paws are in my house?"})

  for chunk, _ := range stream {
      part := chunk.Candidates[0].Content.Parts[0]
      fmt.Print(part.Text)
  }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

public class MultiTurnConversationWithStreaming {
  public static void main(String[] args) {

    Client client = new Client();
    Chat chatSession = client.chats.create("gemini-3.5-flash");

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
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent?alt=sse \
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

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent';
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

## プロンプトに関するヒント

Gemini を最大限に活用するための提案については、[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini/docs/prompting-strategies?hl=ja)を
ご覧ください。

## 次のステップ

- Google AI Studio で [Gemini を試す](https://aistudio.google.com?hl=ja)。
- JSON のようなレスポンスの[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を
  試す。
- Gemini の [画像](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)、
  [動画](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)、[音声](https://ai.google.dev/gemini-api/docs/audio?hl=ja)
  、[ドキュメント](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)の理解機能を調べる。
- マルチモーダル
  [ファイルのプロンプト戦略](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide)について学習する。

## コンテンツの生成

これは、モデルにプロンプトを送信するための中央エンドポイントです。コンテンツを生成するためのエンドポイントは 2 つあり、主な違いはレスポンスの受信方法です。

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=ja#method:-models.generatecontent)
  （REST）** : リクエストを受け取り、モデルが生成を完了した後に単一のレスポンスを提供します。
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=ja#method:-models.streamgeneratecontent)
  （SSE）**: まったく同じリクエストを受け取りますが、モデルはレスポンスのチャンクを生成時にストリーミングで返します。これにより、部分的な結果をすぐに表示できるため、インタラクティブ アプリケーションのユーザー エクスペリエンスが向上します。

### リクエスト本文の構造

[リクエストの本文](https://ai.google.dev/api/generate-content?hl=ja#request-body)は、標準モードとストリーミング モードで
**同じ** JSON オブジェクトで、いくつかのコア
オブジェクトから構築されます。

- [`Content`](https://ai.google.dev/api/caching?hl=ja#Content) オブジェクト: 会話の 1 ターンを表します。
- [`Part`](https://ai.google.dev/api/caching?hl=ja#Part) オブジェクト: `Content` ターンのデータの一部（テキストや画像など）。
- `inline_data`（[`Blob`](https://ai.google.dev/api/caching?hl=ja#Blob)）: 未加工のメディア バイト
  とその MIME タイプのコンテナ。

最上位レベルでは、リクエストの本文に `contents` オブジェクトが含まれます。これは `Content` オブジェクトのリストで、それぞれが会話のターンを表します。ほとんどの場合、基本的なテキスト生成では単一の `Content` オブジェクトを使用しますが、会話履歴を維持する場合は複数の `Content` オブジェクトを使用できます。

一般的な `generateContent` リクエストの本文を次に示します。

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### レスポンス本文の構造

[レスポンスの本文](https://ai.google.dev/api/generate-content?hl=ja#response-body)は、
ストリーミング モードと標準モードでほぼ同じですが、次の点が異なります。

- 標準モード: レスポンスの本文には
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerateContentResponse)のインスタンスが含まれます。
- ストリーミング モード: レスポンスの本文には
  [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerateContentResponse)
  インスタンスのストリームが含まれます。

上位レベルでは、レスポンスの本文に `candidates` オブジェクトが含まれます。これは `Candidate` オブジェクトのリストです。`Candidate` オブジェクトには、モデルから返された生成されたレスポンスを含む `Content` オブジェクトが含まれます。

## REST API の例

### マルチモーダル プロンプト（テキストと画像）

プロンプトでテキストと画像の両方を提供するには、`parts` 配列に 2 つの `Part` オブジェクトを含める必要があります。1 つはテキスト用、もう 1 つは画像 `inline_data` 用です。

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### マルチターンの会話（チャット）

複数のターンで会話を構築するには、複数の `Content` オブジェクトを使用して `contents` 配列を定義します。API は、この履歴全体を次のレスポンスのコンテキストとして使用します。各 `Content` オブジェクトの `role` は、`user` と `model` を交互に切り替える必要があります。

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### 重要ポイント

- `Content` はエンベロープです。ユーザーまたはモデルからのメッセージ ターンに対する最上位のコンテナです。
- `Part` はマルチモダリティを有効にします。1 つの `Content` オブジェクト内で複数の `Part` オブジェクトを使用して、さまざまな種類のデータ（テキスト、画像、動画 URI など）を組み合わせます。
- データ方法を選択します。
  - 小さいメディア（ほとんどの画像など）を直接埋め込む場合は、`inline_data` を使用して `Part` を使用します。
  - 大きなファイルや、リクエスト間で再利用するファイルの場合は、File API を使用してファイルをアップロードし、`file_data` パーツで参照します。
- 会話履歴を管理する: REST API を使用するチャット アプリケーションの場合は、
  `contents` 配列を、ターンごとに `Content` オブジェクトを追加して作成し、
  `"user"` ロールと `"model"` ロールを交互に切り替えます。SDK を使用している場合は、会話履歴を管理するおすすめの方法について SDK ドキュメントをご覧ください。

## レスポンスの例

次の例は、さまざまなタイプのリクエストでこれらのコンポーネントがどのように組み合わされるかを示しています。

### テキストのみのレスポンス

デフォルトのテキスト レスポンスは、モデルのレスポンスを含む 1 つ以上の `content` オブジェクトを含む `candidates` 配列で構成されます。

**標準** レスポンスの例を次に示します。

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

以下は、一連の**ストリーミング** レスポンスです。各レスポンスには、完全なレスポンスをまとめる `responseId` が含まれています。

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
  "modelVersion": "gemini-3.5-flash",
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
  "modelVersion": "gemini-3.5-flash",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## Live API（BidiGenerateContent）WebSockets API

Live API は、双方向ストリーミング用のステートフル WebSocket ベースの API を提供し、リアルタイム ストリーミングのユースケースを可能にします。詳細については、
[Live API ガイド](https://ai.google.dev/gemini-api/docs/live?hl=ja)と[Live API リファレンス](https://ai.google.dev/api/live?hl=ja)
をご覧ください。

## 特殊モデル

Gemini API は、Gemini モデル ファミリーに加えて、
[Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ja)、
[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja)、
[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja) モデルなどの特殊モデルのエンドポイントを提供します。これらのガイドは、モデル セクションで確認できます。

## プラットフォーム API

残りのエンドポイントでは、これまで説明したメイン エンドポイントで使用できる追加機能が有効になります。詳細については、ガイド セクションのトピック
[バッチモード](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ja)と
[File API](https://ai.google.dev/gemini-api/docs/files?hl=ja)をご覧ください。

## 次のステップ

使い始めたばかりの場合は、Gemini API プログラミング モデルの理解に役立つ次のガイドをご覧ください。

- [Gemini API スタートガイド](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [Gemini モデルガイド](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)

また、さまざまな Gemini API 機能を紹介し、コード例を提供する機能ガイドもご覧ください。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- [コンテキストのキャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)
- [エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-24 UTC。"],[],[]]
