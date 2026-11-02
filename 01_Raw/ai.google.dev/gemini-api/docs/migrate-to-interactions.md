---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-TW
fetched_at: 2026-11-02T07:20:39.219231+00:00
title: "\u9077\u79fb\u81f3 Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 遷移至 Interactions API

本指南說明如何從 `generateContent` API 遷移至 Interactions API。

Interactions API 是最簡單、最有效率的方法，可讓您使用 Gemini 模型和代理建構應用程式。雖然 `generateContent` 仍獲得完整支援，但建議您在所有新開發項目中使用 Interactions API。

### 為何要遷移？

Interactions API 是最簡單、最有效率的方法，可讓您使用 Gemini 模型和代理建構應用程式：

- **伺服器端記錄管理**：透過 `previous_interaction_id` 簡化多輪對話流程。伺服器預設會啟用狀態 (`store=true`)，但您可以設定 `store=false`，選擇無狀態行為。
- **可觀測的執行步驟**：類型化步驟可輕鬆偵錯複雜流程，並為中繼事件 (例如想法或搜尋小工具) 算繪 UI。
- **工具使用和 Agentic Workflows**：原生支援多步驟工具使用、自動化調度管理，以及透過輸入執行步驟進行複雜的推論流程。
- **長時間執行和背景工作**：支援使用 `background=true` 將 Deep Think 和 Deep Research 等耗時作業卸載至背景程序。

## 基本輸入/輸出

本節說明如何遷移簡單的文字生成要求。

### `generateContent`之前

`generateContent` API 是無狀態，會直接傳回回應。回應結構會將輸出內容包裝在 `candidates` 清單中，每個清單都包含 `content`，以及要剖析的 `parts` 清單。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash-lite",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent("gemini-2.5-flash-lite", "Tell me a joke.", null);
System.out.println(response.text());
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Tell me a joke."),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

Interactions API 會傳回儲存的互動資源，其中包含 `steps` 時間軸。雖然您可以手動檢查 `steps` 陣列來找出中繼
事件，但 Google GenAI SDK 會直接在傳回的 `Interaction` 物件上提供便利屬性
，方便您存取最終輸出內容。

最常見的便利屬性是 **`.output_text`** (字串)，會自動擷取並彙整模型回覆結尾的連續 `TextContent` 區塊。雖然這對簡單的回覆來說非常合適，但不會包含由非文字內容 (例如想法、圖片、音訊或工具呼叫) 分隔的先前文字區塊。如果是複雜或交錯的多模態回覆，則必須手動疊代 `steps`。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a joke."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a joke."),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## 多轉折對話

Interactions API 預設會儲存互動，為多輪對話啟用伺服器端狀態管理。

### `generateContent`之前

在 `generateContent` 中，您必須使用 `contents` 陣列或用戶端 Chat 小幫手，手動管理對話記錄。

### Python

**使用 Chat 小幫手 (建議)**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash-lite")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**手動管理記錄**

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text(text="Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text(text="Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text(text="What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**使用 Chat 小幫手 (建議)**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash-lite' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**手動管理記錄**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

// Using the chat helper (recommended)
Chat chat = client.chats.create("gemini-2.5-flash-lite");
GenerateContentResponse response1 = chat.sendMessage("Hi, my name is Phil.");
System.out.println(response1.text());

GenerateContentResponse response2 = chat.sendMessage("What is my name?");
System.out.println(response2.text());

// Manually managing history
GenerateContentResponse manualResponse =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Arrays.asList(
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("Hi, my name is Phil.")))
                .build(),
            Content.builder()
                .role("model")
                .parts(Arrays.asList(Part.fromText("Hi Phil, how can I help you?")))
                .build(),
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("What is my name?")))
                .build()),
        null);
System.out.println(manualResponse.text());
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

    // Using the chat helper (recommended)
    chat, err := client.Chats.Create(ctx, "gemini-2.5-flash-lite", nil, nil)
    if err != nil {
        log.Fatal(err)
    }
    response1, err := chat.SendMessage(ctx, genai.Part{Text: "Hi, my name is Phil."})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response1.Text())

    response2, err := chat.SendMessage(ctx, genai.Part{Text: "What is my name?"})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response2.Text())

    // Manually managing history
    history := []*genai.Content{
        genai.NewContentFromText("Hi, my name is Phil.", genai.RoleUser),
        genai.NewContentFromText("Hi Phil, how can I help you?", genai.RoleModel),
        genai.NewContentFromText("What is my name?", genai.RoleUser),
    }
    manualResponse, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", history, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(manualResponse.Text())
}
```

### REST

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 之後 (Interactions API)

Interactions API 會管理伺服器上的狀態。您參照 `previous_interaction_id` 繼續對話。

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.8-flash", input="Hi, my name is Phil."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Hi, my name is Phil.'
});
console.log("Response 1:", interaction.output_text);

interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log("Response 2:", interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Phil."))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

CreateModelInteraction req2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .previousInteractionId(interaction1.id().orElse(""))
        .input(InteractionsInput.of("What is my name?"))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res1.Interaction.OutputText != nil {
        fmt.Println("Response 1:", *res1.Interaction.OutputText)
    }

    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            PreviousInteractionID: res1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("What is my name?"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println("Response 2:", *res2.Interaction.OutputText)
    }
}
```

### REST

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## 多模態輸入

這兩個 API 都支援多模態輸入內容 (文字、圖片、影片等)。

### `generateContent`之前

在 `generateContent` 中，您會在 `contents` 陣列中傳遞 `parts` 清單。回應會傳回第一個候選項目的 `parts` 輸出內容。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        {
            inlineData: {
                data: imageBytes,
                mimeType: 'image/jpeg',
            },
        },
        'Describe this image.',
    ],
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("sample.jpg"));

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Content.fromParts(
            Part.fromBytes(imageBytes, "image/jpeg"), Part.fromText("Describe this image.")),
        null);
System.out.println(response.text());
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

    imageBytes, err := os.ReadFile("sample.jpg")
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromParts([]*genai.Part{
            genai.NewPartFromBytes(imageBytes, "image/jpeg"),
            genai.NewPartFromText("Describe this image."),
        }, genai.RoleUser),
    }

    response, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", contents, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 之後 (Interactions API)

在 Interactions API 中，您會將陣列傳遞至 `input` 欄位。在時間軸中找到 `model_output` 步驟，即可擷取輸出內容。

### Python

```
import base64
from google import genai

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("sample.jpg"));
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder().text("Describe this image.").build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    imageBytes, err := os.ReadFile("sample.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe this image.",
                }),
            }),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## 結構化輸出內容

如要讓模型傳回符合特定結構定義的 JSON，請設定回覆格式。

### `generateContent`之前

在 `generateContent` 中，您可以使用巢狀結構在 `config` (或 `generationConfig`) 物件中的 `response_mime_type` 和 `response_schema` 欄位，設定輸出格式。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Give me a recipe for chocolate chip cookies.',
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                recipe_name: { type: Type.STRING },
                ingredients: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING },
                },
            },
            required: ['recipe_name', 'ingredients'],
        },
    },
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema recipeSchema =
    Schema.builder()
        .type(Type.Known.OBJECT)
        .properties(
            Map.of(
                "recipe_name", Schema.builder().type(Type.Known.STRING).build(),
                "ingredients",
                    Schema.builder()
                        .type(Type.Known.ARRAY)
                        .items(Schema.builder().type(Type.Known.STRING).build())
                        .build()))
        .required(Arrays.asList("recipe_name", "ingredients"))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "Give me a recipe for chocolate chip cookies.",
        GenerateContentConfig.builder()
            .responseMimeType("application/json")
            .responseSchema(recipeSchema)
            .build());
System.out.println(response.text());
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

    recipeSchema := &genai.Schema{
        Type: genai.TypeObject,
        Properties: map[string]*genai.Schema{
            "recipe_name": {Type: genai.TypeString},
            "ingredients": {
                Type:  genai.TypeArray,
                Items: &genai.Schema{Type: genai.TypeString},
            },
        },
        Required: []string{"recipe_name", "ingredients"},
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Give me a recipe for chocolate chip cookies."),
        &genai.GenerateContentConfig{
            ResponseMIMEType: "application/json",
            ResponseSchema:   recipeSchema,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseSchema": {
            "type": "OBJECT",
            "properties": {
                "recipe_name": { "type": "STRING" },
                "ingredients": {
                    "type": "ARRAY",
                    "items": { "type": "STRING" }
                }
            },
            "required": ["recipe_name", "ingredients"]
        }
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 之後 (Interactions API)

在 Interactions API 中，輸出格式控制項會移至頂層 `response_format` 欄位。如要要求多種輸出類型，請傳遞單一格式物件，或格式物件陣列。

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for chocolate chip cookies.",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema(),
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                recipe_name: { type: 'string' },
                ingredients: {
                    type: 'array',
                    items: { type: 'string' }
                }
            },
            required: ['recipe_name', 'ingredients']
        }
    }
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("recipe_name", Map.of("type", "string"));
properties.put("ingredients", Map.of("type", "array", "items", Map.of("type", "string")));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("recipe_name", "ingredients"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Give me a recipe for chocolate chip cookies."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();
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

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "recipe_name": map[string]any{"type": "string"},
            "ingredients": map[string]any{
                "type":  "array",
                "items": map[string]any{"type": "string"},
            },
        },
        "required": []string{"recipe_name", "ingredients"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me a recipe for chocolate chip cookies."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "recipe_name": { "type": "string" },
                "ingredients": {
                    "type": "array",
                    "items": { "type": "string" }
                }
            },
            "required": ["recipe_name", "ingredients"]
        }
    }
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## 多模態生成

生成文字以外的生成式媒體內容 (例如圖片或音訊) 時，主要差異在於回覆如何建構生成的媒體。

### `generateContent`之前

在 `generateContent` 中，回覆會直接在候選項目的 `parts` 中傳回生成的媒體，通常是 `inlineData` 中的 base64 資料。

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### 之後 (Interactions API)

在 Interactions API 中，生成的媒體會以獨立項目的形式，顯示在時間軸 `model_output` 步驟的 `content` 陣列中，維持互動的時間順序。

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

這樣一來，回覆剖析作業就會與輸入和文字輸出內容的處理方式保持一致，所有內容都會是時間軸中的一個步驟。

## 伺服器端工具

Gemini 支援內建的伺服器端工具，例如 Google 搜尋基準建立。主要差異在於回覆如何呈現工具執行作業。

### `generateContent`之前

在 `generateContent` 中，伺服器端工具大多不透明。您啟用工具，並透過獨立的 `groundingMetadata` 物件取得最終答案。請注意，引用內容並非內嵌，`groundingSupports`會使用字元索引將文字片段對應回 `groundingChunks` 中的網頁來源。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Candidate;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.GroundingMetadata;
import com.google.genai.types.GroundingSupport;
import com.google.genai.types.Tool;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "Who won Euro 2024?",
        GenerateContentConfig.builder()
            .tools(
                Arrays.asList(
                    Tool.builder().googleSearch(GoogleSearch.builder().build()).build()))
            .build());

List<Candidate> candidates = response.candidates().orElse(Collections.emptyList());
if (!candidates.isEmpty() && candidates.get(0).groundingMetadata().isPresent()) {
  GroundingMetadata metadata = candidates.get(0).groundingMetadata().get();
  if (metadata.searchEntryPoint().isPresent()) {
    System.out.println(
        "Search Entry Point: " + metadata.searchEntryPoint().get().renderedContent().orElse(""));
  }
  for (GroundingSupport support : metadata.groundingSupports().orElse(Collections.emptyList())) {
    Optional<String> segmentText = support.segment().flatMap(s -> s.text());
    segmentText.ifPresent(text -> System.out.println("Citation: " + text));
  }
}
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Who won Euro 2024?"),
        &genai.GenerateContentConfig{
            Tools: []*genai.Tool{
                {GoogleSearch: &genai.GoogleSearch{}},
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    if len(response.Candidates) > 0 && response.Candidates[0].GroundingMetadata != nil {
        metadata := response.Candidates[0].GroundingMetadata
        if metadata.SearchEntryPoint != nil {
            fmt.Println("Search Entry Point:", metadata.SearchEntryPoint.RenderedContent)
        }
        for _, support := range metadata.GroundingSupports {
            if support.Segment != nil {
                fmt.Println("Citation:", support.Segment.Text)
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

### 之後 (Interactions API)

在 Interactions API 中，伺服器端工具可提供完整時間軸透明度。API 會將呼叫和結果記錄為不同的執行 `steps` (`google_search_call` 和 `google_search_result`)，準確顯示模型擷取的資料。

此外，API 會**內嵌**傳回引用來源。`model_output` 步驟中的文字項目包含自己的 `annotations` 陣列，可直接連結至來源，不必從獨立的中繼資料物件對應索引。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.result[0].search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.result[0].search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.GoogleSearchResult;
import com.google.genai.gaos.models.interactions.GoogleSearchResultStep;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won Euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof GoogleSearchResultStep) {
    GoogleSearchResultStep searchStep = (GoogleSearchResultStep) step;
    for (GoogleSearchResult res : searchStep.result().orElse(Collections.emptyList())) {
      System.out.println("Search Suggestions: " + res.searchSuggestions().orElse(""));
    }
  } else if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        TextContent textContent = (TextContent) contentBlock;
        System.out.println("Answer: " + textContent.text().orElse(""));
        for (Annotation anno : textContent.annotations().orElse(Collections.emptyList())) {
          if (anno instanceof URLCitation) {
            URLCitation cit = (URLCitation) anno;
            System.out.println(
                "Citation: " + cit.title().orElse("") + " (" + cit.url().orElse("") + ")");
          }
        }
      }
    }
  }
}
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Who won Euro 2024?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if searchStep := step.GoogleSearchResultStep; searchStep != nil {
            for _, r := range searchStep.Result {
                if r.SearchSuggestions != nil {
                    fmt.Println("Search Suggestions:", *r.SearchSuggestions)
                }
            }
        } else if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Answer:", textContent.Text)
                    for _, anno := range textContent.Annotations {
                        if cit := anno.URLCitation; cit != nil {
                            fmt.Printf("Citation: %s (%s)\n", cit.GetTitle(), cit.GetURL())
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## 函式呼叫

函式呼叫和結果的結構也已變更，以符合 Steps 結構定義。

### `generateContent`之前

在 `generateContent` 中，回應會傳回候選項目中的函式呼叫\*。{Python}

```
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content,
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.FunctionCall;
import com.google.genai.types.FunctionDeclaration;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.Schema;
import com.google.genai.types.Tool;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

FunctionDeclaration weatherFunc =
    FunctionDeclaration.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(Map.of("location", Schema.builder().type(Type.Known.STRING).build()))
                .build())
        .build();

Tool weatherTool = Tool.builder().functionDeclarations(Arrays.asList(weatherFunc)).build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "What's the weather in Boston?",
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build());

FunctionCall functionCall = response.functionCalls().get(0);
System.out.println("Requested tool: " + functionCall.name().orElse(""));

String result = "52°F and rain";

GenerateContentResponse finalResponse =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Arrays.asList(
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("What's the weather in Boston?")))
                .build(),
            response.candidates().get().get(0).content().get(),
            Content.builder()
                .role("user")
                .parts(
                    Arrays.asList(
                        Part.fromFunctionResponse(
                            functionCall.name().orElse(""), Map.of("result", result))))
                .build()),
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build());
System.out.println(finalResponse.text());
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

    weatherTool := &genai.Tool{
        FunctionDeclarations: []*genai.FunctionDeclaration{
            {
                Name:        "get_weather",
                Description: "Gets weather",
                Parameters: &genai.Schema{
                    Type: genai.TypeObject,
                    Properties: map[string]*genai.Schema{
                        "location": {Type: genai.TypeString},
                    },
                },
            },
        },
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{weatherTool},
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("What's the weather in Boston?"),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    calls := response.FunctionCalls()
    if len(calls) > 0 {
        functionCall := calls[0]
        fmt.Println("Requested tool:", functionCall.Name)

        result := "52°F and rain"
        history := []*genai.Content{
            genai.NewContentFromText("What's the weather in Boston?", genai.RoleUser),
            response.Candidates[0].Content,
            genai.NewContentFromParts([]*genai.Part{
                genai.NewPartFromFunctionResponse(functionCall.Name, map[string]any{"result": result}),
            }, genai.RoleUser),
        }

        finalResponse, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", history, config)
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(finalResponse.Text())
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 之後 (Interactions API)

工具呼叫和結果現在是時間軸中的不同步驟。

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        result = "52°F and rain"

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        const nextInteraction = await client.interactions.create({
            model: 'gemini-3.8-flash',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        console.log(nextInteraction.output_text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("location", Map.of("type", "string"));

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's the weather in Boston?"))
        .tools(Arrays.asList(weatherTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    FunctionCallStep fcStep = (FunctionCallStep) step;
    System.out.println(
        "Executing "
            + fcStep.name().orElse("")
            + " for "
            + fcStep.arguments().orElse(Collections.emptyMap()));

    String result = "52°F and rain";

    FunctionResultStep funcResult =
        FunctionResultStep.builder()
            .callId(fcStep.id().orElse(""))
            .name(fcStep.name().orElse(""))
            .result(
                FunctionResultStepResultUnion.of(
                    Arrays.asList(TextContent.builder().text(result).build())))
            .build();

    CreateModelInteraction nextRequest =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .previousInteractionId(interaction.id().orElse(""))
            .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
            .build();

    Interaction nextInteraction =
        client.interactions.create(CreateInteractionRequestBody.of(nextRequest)).interaction().get();
    System.out.println(nextInteraction.outputText().orElse(""));
  }
}
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

    weatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets weather"),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{"type": "string"},
            },
            "required": []string{"location"},
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What's the weather in Boston?"),
            Tools: []interactions.Tool{weatherTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Printf("Executing %s for %v\n", fcStep.Name, fcStep.Arguments)

            result := "52°F and rain"
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                CallID: fcStep.ID,
                Name:   genai.Ptr(fcStep.Name),
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{Text: result}),
                }),
            })

            nextRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3.8-flash"),
                    PreviousInteractionID: res.Interaction.ID,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if nextRes.Interaction.OutputText != nil {
                fmt.Println(*nextRes.Interaction.OutputText)
            }
        }
    }
}
```

### REST

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## 串流

串流的主要差異在於，Interactions API 使用相同的端點，並在要求主體中加入 `"stream": true`，而 `generateContent` API 則需要呼叫專屬端點 (`:streamGenerateContent`)。

此外，串流事件現在會使用專門類型，監控互動生命週期，並追蹤時間軸上的執行步驟。

### `generateContentStream`之前

使用 `generateContent` 時，您會取用回覆區塊串流。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

try (ResponseStream<GenerateContentResponse> responseStream =
    client.models.generateContentStream("gemini-2.5-flash-lite", "Tell me a story", null)) {
  for (GenerateContentResponse chunk : responseStream) {
    System.out.print(chunk.text());
  }
}
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

    for chunk, err := range client.Models.GenerateContentStream(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Tell me a story"),
        nil,
    ) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Print(chunk.Text())
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### 之後 (Interactions API)

在 Interactions API 中，串流會使用伺服器傳送事件 (SSE) 和特殊差異類型，在執行步驟發生時呈現。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a story"))
        .stream(true)
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(request)).events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    if (streamEvent.data().isPresent()) {
      InteractionSSEEvent event = streamEvent.data().get();
      if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.delta().isPresent() && stepDelta.delta().get() instanceof TextDelta) {
          TextDelta textDelta = (TextDelta) stepDelta.delta().get();
          System.out.print(textDelta.text().orElse(""));
        }
      } else if (event instanceof InteractionCompletedEvent) {
        System.out.println("\n\n--- Stream Finished ---");
      }
    }
  }
}
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
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Tell me a story"),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        } else if event.GetDataInteractionCompleted() != nil {
            fmt.Println("\n\n--- Stream Finished ---")
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

# Example SSE stream output
**event: interaction.created
data: {"interaction": {"id": "int\_xyz", "status": "in\_progress"}, "event\_type": "interaction.created"}
event: interaction.status\_update
data: {"interaction\_id": "int\_xyz", "status": "in\_progress", "event\_type": "interaction.status\_update"}
event: step.start
data: {"index": 0, "step": {"type": "thought"}, "event\_type": "step.start"}
event: step.delta
data: {"index": 0, "delta": {"type": "thought\_summary", "content": {"type": "text", "text": "User wants an explanation."}}, "event\_type": "step.delta"}
event: step.stop
data: {"index": 0, "event\_type": "step.stop"}
event: step.start
data: {"index": 1, "step": {"type": "model\_output"}, "event\_type": "step.start"}
event: step.delta
data: {"index": 1, "delta": {"type": "text", "text": "Hello"}, "event\_type": "step.delta"}
event: step.stop
data: {"index": 1, "event\_type": "step.stop"}
event: interaction.completed
data: {"interaction": {"id": "int\_xyz", "status": "completed", "usage": {"total\_input\_tokens": 10, "total\_output\_tokens": 5, "total\_tokens": 15}}, "event\_type": "interaction.completed"}**
```

### 串流工具和函式呼叫

`generateContent`起，工具在訊息串中的運作方式有大幅變動，可提供更精細的控制選項和瀏覽權限。

#### `generateContent`之前

使用 `generateContent` 時，串流函式呼叫會以單一區塊完整傳送。您無法即時查看產生的引數，因此處理常式只會檢查完整的 `functionCall` 物件。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.FunctionCall;
import com.google.genai.types.FunctionDeclaration;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Tool;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

FunctionDeclaration weatherFunc =
    FunctionDeclaration.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(Map.of("location", Schema.builder().type(Type.Known.STRING).build()))
                .build())
        .build();

Tool weatherTool = Tool.builder().functionDeclarations(Arrays.asList(weatherFunc)).build();

try (ResponseStream<GenerateContentResponse> stream =
    client.models.generateContentStream(
        "gemini-2.5-flash-lite",
        "What's the weather in Boston?",
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build())) {
  for (GenerateContentResponse chunk : stream) {
    if (chunk.functionCalls() != null && !chunk.functionCalls().isEmpty()) {
      FunctionCall fc = chunk.functionCalls().get(0);
      System.out.println("Call: " + fc.name().orElse("") + "(" + fc.args().orElse(Map.of()) + ")");
    } else if (chunk.text() != null) {
      System.out.print(chunk.text());
    }
  }
}
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

    weatherTool := &genai.Tool{
        FunctionDeclarations: []*genai.FunctionDeclaration{
            {
                Name:        "get_weather",
                Description: "Gets weather",
                Parameters: &genai.Schema{
                    Type: genai.TypeObject,
                    Properties: map[string]*genai.Schema{
                        "location": {Type: genai.TypeString},
                    },
                },
            },
        },
    }

    for chunk, err := range client.Models.GenerateContentStream(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("What's the weather in Boston?"),
        &genai.GenerateContentConfig{
            Tools: []*genai.Tool{weatherTool},
        },
    ) {
        if err != nil {
            log.Fatal(err)
        }
        if calls := chunk.FunctionCalls(); len(calls) > 0 {
            fc := calls[0]
            fmt.Printf("Call: %s(%v)\n", fc.Name, fc.Args)
        } else if text := chunk.Text(); text != "" {
            fmt.Print(text)
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What is the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### 之後 (Interactions API)

Interactions API 會以 `arguments_delta` 事件的形式，逐字元串流函式呼叫引數。整個工具生命週期 (思考、呼叫、結果和輸出) 會以一系列不同的步驟進行。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start" and event.step:
        if getattr(event.step, "type", None) == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "arguments_delta":
            print(f"  args: {event.delta.arguments}")
        elif getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start' && event.step) {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'arguments_delta' && event.delta.arguments) {
            console.log(`  args: ${event.delta.arguments}`);
        } else if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ArgumentsDelta;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.StepStart;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("location", Map.of("type", "string"));

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function getWeatherTool =
    Function.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's the weather in Boston?"))
        .tools(Arrays.asList(getWeatherTool))
        .stream(true)
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(request)).events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    if (streamEvent.data().isPresent()) {
      InteractionSSEEvent event = streamEvent.data().get();
      if (event instanceof StepStart) {
        StepStart stepStart = (StepStart) event;
        if (stepStart.step().isPresent() && stepStart.step().get() instanceof FunctionCallStep) {
          FunctionCallStep fcStep = (FunctionCallStep) stepStart.step().get();
          System.out.println("Calling: " + fcStep.name().orElse(""));
        }
      } else if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.delta().isPresent()) {
          StepDeltaData delta = stepDelta.delta().get();
          if (delta instanceof ArgumentsDelta) {
            System.out.println("  args: " + ((ArgumentsDelta) delta).arguments().orElse(""));
          } else if (delta instanceof TextDelta) {
            System.out.print(((TextDelta) delta).text().orElse(""));
          }
        }
      } else if (event instanceof InteractionCompletedEvent) {
        System.out.println("\n--- Done ---");
      }
    }
  }
}
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

    getWeatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets weather"),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{"type": "string"},
            },
            "required": []string{"location"},
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("What's the weather in Boston?"),
            Tools:  []interactions.Tool{getWeatherTool},
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepStart := event.GetDataStepStart(); stepStart != nil {
            if fcStep := stepStart.GetStepFunctionCall(); fcStep != nil {
                fmt.Println("Calling:", fcStep.Name)
            }
        } else if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if argsDelta := stepDelta.GetDeltaArgumentsDelta(); argsDelta != nil {
                fmt.Println("  args:", argsDelta.GetArguments())
            } else if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        } else if event.GetDataInteractionCompleted() != nil {
            fmt.Println("\n--- Done ---")
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What is the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Stream 1: the model calls the function
event: interaction.created
data: {"interaction": {"id": "int_1", "status": "in_progress"}, "event_type": "interaction.created"}

event: interaction.status_update
data: {"interaction_id": "int_1", "status": "in_progress", "event_type": "interaction.status_update"}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"index": 0, "step": {"type": "thought"}, "event_type": "step.start"}

event: step.delta
data: {"index": 0, "delta": {"type": "thought_summary", "content": {"type": "text", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}, "event_type": "step.delta"}

event: step.stop
data: {"index": 0, "event_type": "step.stop"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather", "arguments": {}}, "event_type": "step.start"}

event: step.delta
data: {"index": 1, "delta": {"type": "arguments_delta", "arguments": "{\"location\": \"Boston, MA\"}"}, "event_type": "step.delta"}

event: step.stop
data: {"index": 1, "event_type": "step.stop"}

// The stream ends with status requires_action: the model needs the tool result.
event: interaction.completed
data: {"interaction": {"id": "int_1", "status": "requires_action", "usage": {"total_input_tokens": 34, "total_output_tokens": 15, "total_tokens": 49}}, "event_type": "interaction.completed"}

event: done
data: [DONE]

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and previous_interaction_id set to "int_1". This opens a new stream.

// Stream 2: the model uses the result
event: interaction.created
data: {"interaction": {"id": "int_2", "status": "in_progress"}, "event_type": "interaction.created"}

event: interaction.status_update
data: {"interaction_id": "int_2", "status": "in_progress", "event_type": "interaction.status_update"}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"index": 0, "step": {"type": "thought"}, "event_type": "step.start"}

event: step.delta
data: {"index": 0, "delta": {"type": "thought_summary", "content": {"type": "text", "text": "Got weather data. Composing the final response."}}, "event_type": "step.delta"}

event: step.stop
data: {"index": 0, "event_type": "step.stop"}

// ── Step 1: Model Output (text streamed) ─────────────
event: step.start
data: {"index": 1, "step": {"type": "model_output"}, "event_type": "step.start"}

event: step.delta
data: {"index": 1, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}, "event_type": "step.delta"}

event: step.stop
data: {"index": 1, "event_type": "step.stop"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"interaction": {"id": "int_2", "status": "completed", "usage": {"total_input_tokens": 256, "total_output_tokens": 128, "total_tokens": 384}}, "event_type": "interaction.completed"}

event: done
data: [DONE]
```

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-27 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-27 (世界標準時間)。"],[],[]]
