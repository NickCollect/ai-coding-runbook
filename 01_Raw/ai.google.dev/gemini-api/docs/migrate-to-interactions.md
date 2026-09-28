---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=th
fetched_at: 2026-09-28T06:18:18.567985+00:00
title: "\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e1b\u0e22\u0e31\u0e07 Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การย้ายข้อมูลไปยัง Interactions API

คู่มือนี้จะช่วยคุณย้ายข้อมูลจาก `generateContent` API ไปยัง Interactions API

Interactions API เป็นวิธีที่ง่ายที่สุดและดีที่สุดในการสร้างด้วยโมเดลและเอเจนต์ Gemini แม้ว่าเราจะยังคงรองรับ `generateContent` อย่างเต็มที่ แต่ขอแนะนำให้ใช้ Interactions API สำหรับการพัฒนาใหม่ทั้งหมด

### ทำไมต้องย้ายข้อมูล

Interactions API เป็นวิธีที่ง่ายที่สุดและดีที่สุดในการสร้างด้วยโมเดลและเอเจนต์ของ Gemini

- **การจัดการประวัติฝั่งเซิร์ฟเวอร์**: ลดความซับซ้อนของโฟลว์การสนทนาไปมาผ่าน `previous_interaction_id` เซิร์ฟเวอร์จะเปิดใช้สถานะโดยค่าเริ่มต้น (`store=true`) แต่คุณเลือกใช้ลักษณะการทำงานแบบไม่มีสถานะได้โดยการตั้งค่า `store=false`
- **ขั้นตอนการดำเนินการที่สังเกตได้**: ขั้นตอนที่พิมพ์ทำให้การแก้ไขข้อบกพร่องของโฟลว์ที่ซับซ้อนและการแสดงผล UI สำหรับเหตุการณ์ระดับกลาง (เช่น ความคิดหรือวิดเจ็ตการค้นหา) เป็นเรื่องง่าย
- **การใช้เครื่องมือและเวิร์กโฟลว์แบบเป็น Agent**: รองรับการใช้เครื่องมือแบบหลายขั้นตอน การจัดการเป็นกลุ่ม และโฟลว์การให้เหตุผลที่ซับซ้อนผ่านขั้นตอนการดำเนินการที่พิมพ์
- **งานที่ใช้เวลานานและงานเบื้องหลัง**: รองรับการส่งต่อการดำเนินการที่ใช้เวลานาน เช่น Deep Think และ Deep Research ไปยังกระบวนการเบื้องหลังโดยใช้ `background=true`

## อินพุต/เอาต์พุตพื้นฐาน

ส่วนนี้แสดงวิธีเปลี่ยนคำขอการสร้างข้อความอย่างง่าย

### ก่อน (`generateContent`)

`generateContent` API ไม่มีการเก็บสถานะและจะแสดงการตอบกลับโดยตรง โครงสร้างการตอบกลับจะรวมเอาต์พุตไว้ในรายการของ `candidates` ซึ่งแต่ละรายการจะมี `content` ที่มีรายการของ `parts` เพื่อแยกวิเคราะห์

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

Interaction API จะแสดงผลแหล่งข้อมูลการโต้ตอบที่จัดเก็บไว้พร้อม`steps`
ไทม์ไลน์ แม้ว่าคุณจะตรวจสอบอาร์เรย์ `steps` ด้วยตนเองเพื่อค้นหาเหตุการณ์ระดับกลางได้ แต่ Google GenAI SDK มีพร็อพเพอร์ตี้ที่สะดวก
ในออบเจ็กต์ `Interaction` ที่ส่งคืนโดยตรงเพื่อให้เข้าถึงเอาต์พุตสุดท้ายได้

พร็อพเพอร์ตี้ความสะดวกที่พบบ่อยที่สุดคือ **`.output_text`** (String) ซึ่งจะ
แยกและรวมบล็อก `TextContent` ที่ต่อเนื่องกันโดยอัตโนมัติที่
ส่วนท้ายของคำตอบของโมเดล แม้ว่าวิธีนี้จะใช้ได้ดีกับคำตอบง่ายๆ
แต่จะไม่มีบล็อกข้อความก่อนหน้าซึ่งคั่นด้วยเนื้อหาที่ไม่ใช่ข้อความ (เช่น
ความคิด รูปภาพ เสียง หรือการเรียกใช้เครื่องมือ) สำหรับคำตอบแบบมัลติโมดอลที่ซับซ้อนหรือสลับกัน คุณต้องวนซ้ำผ่าน `steps` ด้วยตนเองแทน

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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

## การสนทนาไปมา

Interactions API จะจัดเก็บการโต้ตอบโดยค่าเริ่มต้น ซึ่งช่วยให้การจัดการสถานะฝั่งเซิร์ฟเวอร์สำหรับการสนทนาไปมา

### ก่อน (`generateContent`)

ใน `generateContent` คุณต้องจัดการประวัติการสนทนาด้วยตนเองโดยใช้อาร์เรย์ `contents` หรือตัวช่วยแชทฝั่งไคลเอ็นต์

### Python

**ใช้ผู้ช่วยแชท (แนะนำ)**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash-lite")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**การจัดการประวัติด้วยตนเอง**

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

**ใช้ผู้ช่วยแชท (แนะนำ)**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash-lite' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**การจัดการประวัติด้วยตนเอง**

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

### After (Interactions API)

Interactions API จัดการสถานะในเซิร์ฟเวอร์ คุณสนทนาต่อได้โดยอ้างอิงถึง `previous_interaction_id`

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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

## อินพุตหลายรูปแบบ

API ทั้ง 2 รายการรองรับอินพุตหลายรูปแบบ (ข้อความ รูปภาพ วิดีโอ ฯลฯ)

### ก่อน (`generateContent`)

ใน `generateContent` คุณจะส่งรายการ `parts` ภายในอาร์เรย์ `contents` การตอบกลับจะแสดงเอาต์พุตใน `parts` ของผู้สมัครคนแรก

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

### After (Interactions API)

ใน Interactions API คุณจะส่งอาร์เรย์ไปยังฟิลด์ `input` คุณดึงเนื้อหาเอาต์พุตได้โดยค้นหา`model_output`ในไทม์ไลน์

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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

## เอาต์พุตที่มีโครงสร้าง

หากต้องการให้โมเดลแสดงผล JSON ที่ตรงกับสคีมาที่เฉพาะเจาะจง ให้กำหนดค่ารูปแบบการตอบกลับ

### ก่อน (`generateContent`)

ใน `generateContent` คุณจะกำหนดค่ารูปแบบเอาต์พุตโดยใช้ฟิลด์ `response_mime_type` และ `response_schema` ที่ซ้อนอยู่ภายในออบเจ็กต์ `config` (หรือ `generationConfig`)

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

### After (Interactions API)

ใน Interactions API การควบคุมรูปแบบเอาต์พุตจะย้ายไปอยู่ที่อาร์เรย์ `response_format` ระดับบนสุด

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
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe.model_json_schema(),
        }
    ],
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
    response_format: [
        {
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
    ]
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
                Arrays.asList(
                    ResponseFormat.of(
                        TextResponseFormat.builder()
                            .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                            .schema(schema)
                            .build()))))
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
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
    ]
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

## การสร้างแบบหลายรูปแบบ

เมื่อสร้างเนื้อหาในรูปแบบอื่นๆ นอกเหนือจากข้อความ (เช่น รูปภาพหรือเสียง) ความแตกต่างหลักคือวิธีที่คำตอบจัดโครงสร้างสื่อที่สร้างขึ้น

### ก่อน (`generateContent`)

ใน `generateContent` คำตอบจะแสดงสื่อที่สร้างขึ้นโดยตรงใน `parts` ของผู้สมัคร โดยปกติจะเป็นข้อมูล base64 ใน `inlineData`

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

### After (Interactions API)

ใน Interactions API สื่อที่สร้างขึ้นจะปรากฏเป็นรายการที่แตกต่างกันภายในอาร์เรย์ `content` ของขั้นตอน `model_output` ในไทม์ไลน์ ซึ่งจะรักษาลำดับเวลาของการโต้ตอบไว้

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

วิธีนี้จะช่วยให้การแยกวิเคราะห์การตอบกลับสอดคล้องกับวิธีจัดการอินพุตและเอาต์พุตข้อความ โดยทุกอย่างจะเป็นขั้นตอนในไทม์ไลน์

## เครื่องมือฝั่งเซิร์ฟเวอร์

Gemini รองรับเครื่องมือฝั่งเซิร์ฟเวอร์ในตัว เช่น การอ้างอิงข้อมูลของ Google Search ความแตกต่างหลักๆ คือวิธีที่คำตอบแสดงการดำเนินการของเครื่องมือ

### ก่อน (`generateContent`)

ใน `generateContent` เครื่องมือฝั่งเซิร์ฟเวอร์ส่วนใหญ่จะทำงานแบบไม่โปร่งใส คุณเปิดใช้เครื่องมือและรับคำตอบสุดท้ายพร้อม`groundingMetadata`ออบเจ็กต์แยกต่างหาก ที่สำคัญคือ การอ้างอิงไม่ได้อยู่ในบรรทัด `groundingSupports` ใช้ดัชนีอักขระเพื่อแมปข้อความกลับไปยังแหล่งที่มาบนเว็บใน `groundingChunks`

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

### After (Interactions API)

ใน Interactions API เครื่องมือฝั่งเซิร์ฟเวอร์จะให้ความโปร่งใสของไทม์ไลน์ทั้งหมด API จะบันทึกการเรียกและผลลัพธ์เป็นการดำเนินการที่แตกต่างกัน `steps` (`google_search_call` และ `google_search_result`) ซึ่งจะแสดงข้อมูลที่โมเดลดึงมาอย่างชัดเจน

นอกจากนี้ API ยังแสดงการอ้างอิง**ในบรรทัด**ด้วย รายการข้อความภายใน`model_output` ขั้นตอนจะมีอาร์เรย์ `annotations` ของตัวเองที่ลิงก์ไปยังแหล่งที่มาโดยตรง แทนที่จะแมปดัชนีจากออบเจ็กต์ข้อมูลเมตาแยกต่างหาก

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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

## การเรียกใช้ฟังก์ชัน

นอกจากนี้ โครงสร้างของการเรียกใช้ฟังก์ชันและผลลัพธ์ยังเปลี่ยนไปเพื่อให้เข้ากับสคีมาขั้นตอน

### ก่อน (`generateContent`)

ใน `generateContent` คำตอบจะแสดงการเรียกใช้ฟังก์ชันภายในผู้สมัคร\* {Python}

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

### After (Interactions API)

ตอนนี้การเรียกใช้เครื่องมือและผลลัพธ์เป็นขั้นตอนที่แยกกันในไทม์ไลน์แล้ว

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
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

## สตรีมมิง

ความแตกต่างที่สำคัญในการสตรีมคือ Interactions API ใช้ปลายทางเดียวกันกับ `"stream": true` ในเนื้อหาคำขอ ในขณะที่ `generateContent` API ต้องเรียกปลายทางเฉพาะ (`:streamGenerateContent`)

นอกจากนี้ ตอนนี้กิจกรรมการสตรีมยังใช้ประเภทเฉพาะเพื่อตรวจสอบวงจรการโต้ตอบและติดตามขั้นตอนการดำเนินการตามไทม์ไลน์ด้วย

### ก่อน (`generateContentStream`)

เมื่อใช้ `generateContent` คุณจะใช้สตรีมของก้อนการตอบกลับ

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

### After (Interactions API)

ใน Interactions API การสตรีมจะใช้เหตุการณ์ที่เซิร์ฟเวอร์ส่ง (SSE) และประเภทเดลต้าเฉพาะเพื่อแสดงขั้นตอนการดำเนินการตามที่เกิดขึ้น

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

# เอาต์พุตสตรีม SSE ตัวอย่าง
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### เครื่องมือการสตรีมและการเรียกฟังก์ชัน

ลักษณะการทำงานของเครื่องมือในสตรีมเปลี่ยนไปอย่างมากจาก `generateContent` เพื่อให้การควบคุมและการมองเห็นที่ละเอียดยิ่งขึ้น

#### ก่อน (`generateContent`)

เมื่อใช้ `generateContent` ฟังก์ชันการโทรแบบสตรีมมิงจะมาถึงอย่างสมบูรณ์ในก้อนเดียว คุณไม่สามารถดูอาร์กิวเมนต์ที่สร้างขึ้นแบบเรียลไทม์ได้ ตัวแฮนเดิลจึงเพียงตรวจสอบออบเจ็กต์ `functionCall` ที่สมบูรณ์

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

#### After (Interactions API)

Interactions API จะสตรีมอาร์กิวเมนต์การเรียกฟังก์ชันทีละอักขระเป็นเหตุการณ์ `arguments` วงจรทั้งหมดของเครื่องมือ ซึ่งประกอบด้วย ความคิด การเรียกใช้ ผลลัพธ์ และเอาต์พุต จะทำงานเป็นชุดขั้นตอนที่แตกต่างกัน

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
        if getattr(event.delta, "type", None) == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
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
        if (event.delta.type === 'arguments' && event.delta.partial_arguments) {
            console.log(`  args: ${event.delta.partial_arguments}`);
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What is the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
