---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=th
fetched_at: 2026-09-28T06:13:02.022651+00:00
title: "\u0e17\u0e4d\u0e32\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e41\u0e25\u0e30\u0e19\u0e31\u0e1a\u0e42\u0e17\u0e40\u0e04\u0e47\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ทําความเข้าใจและนับโทเค็น

Gemini และโมเดล Generative AI อื่นๆ จะประมวลผลอินพุตและเอาต์พุตที่ระดับความละเอียด
ที่เรียกว่า*โทเค็น*

**สำหรับโมเดล Gemini โทเค็นจะเท่ากับอักขระประมาณ 4 ตัว
โดย 100 โทเค็นจะเท่ากับคำภาษาอังกฤษประมาณ 60-80 คำ**

## เกี่ยวกับโทเค็น

โทเค็นอาจเป็นอักขระเดียว เช่น `z` หรือทั้งคำ เช่น `cat` คำยาวๆ
จะถูกแบ่งออกเป็นหลายโทเค็น ชุดโทเค็นทั้งหมดที่โมเดลใช้เรียกว่า
คำศัพท์ และกระบวนการแยกข้อความเป็นโทเค็นเรียกว่า
*การโทเค็น*

เมื่อเปิดใช้การเรียกเก็บเงิน [ค่าใช้จ่ายในการเรียกใช้ Gemini API](https://ai.google.dev/pricing?hl=th) จะขึ้นอยู่กับจำนวนโทเค็นอินพุตและเอาต์พุตบางส่วน ดังนั้นการทราบวิธีนับโทเค็นจึงอาจเป็นประโยชน์

## นับโทเค็น

อินพุตและเอาต์พุตทั้งหมดจาก Gemini API จะได้รับการโทเค็น รวมถึงข้อความ ไฟล์รูปภาพ และรูปแบบอื่นๆ ที่ไม่ใช่ข้อความ

คุณนับโทเค็นได้ด้วยวิธีต่อไปนี้

- **โทรหา `count_tokens` พร้อมข้อมูลคำขอ** แสดงผลจำนวนโทเค็นทั้งหมดใน*อินพุตเท่านั้น* เรียกใช้ฟังก์ชันนี้ก่อนส่งอินพุต
  เพื่อตรวจสอบขนาดของคำขอ
- **ใช้ `usage` ในการตอบกลับการโต้ตอบ** แสดงจำนวนโทเค็น
  สำหรับอินพุต (`total_input_tokens`), เอาต์พุต (`total_output_tokens`),
  การคิด (`total_thought_tokens`), เนื้อหาที่แคช
  (`total_cached_tokens`), การใช้เครื่องมือ (`total_tool_use_tokens`)
  และทั้งหมด (`total_tokens`)

### นับโทเค็นข้อความ

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CountTokensResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
CountTokensResponse countResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println("total_tokens: " + countResponse.totalTokens().orElse(0));

// Get usage from interaction
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
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

    modelInfo, err := client.Models.Get(ctx, "gemini-3.8-flash", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Input token limit: %d\n", modelInfo.InputTokenLimit)
    fmt.Printf("Output token limit: %d\n", modelInfo.OutputTokenLimit)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### นับโทเค็นการสนทนาไปมา

นับโทเค็นในประวัติการสนทนาโดยใช้ `previous_interaction_id` ดังนี้

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// First interaction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Bob"))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Second interaction continues the conversation
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's my name?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Usage includes tokens from both turns
if (interaction2.usage().isPresent()) {
  Usage usage = interaction2.usage().get();
  System.out.println("Input tokens: " + usage.totalInputTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
  System.out.println("Total tokens: " + usage.totalTokens().orElse(0));
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

    prompt := "The quick brown fox jumps over the lazy dog."

    // Count input tokens before sending
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", genai.Text(prompt), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("total_tokens: %d\n", totalTokens.TotalTokens)

    // Create the interaction and inspect the returned usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil {
        if interaction.Usage.TotalInputTokens != nil {
            fmt.Printf("Input tokens: %d\n", *interaction.Usage.TotalInputTokens)
        }
        if interaction.Usage.TotalOutputTokens != nil {
            fmt.Printf("Output tokens: %d\n", *interaction.Usage.TotalOutputTokens)
        }
        if interaction.Usage.TotalThoughtTokens != nil {
            fmt.Printf("Thought tokens: %d\n", *interaction.Usage.TotalThoughtTokens)
        }
        if interaction.Usage.TotalTokens != nil {
            fmt.Printf("Total tokens: %d\n", *interaction.Usage.TotalTokens)
        }
    }
}
```

### นับโทเค็นหลายรูปแบบ

อินพุตทั้งหมดไปยัง Gemini API จะได้รับการแปลงเป็นโทเค็น ซึ่งรวมถึงรูปภาพ วิดีโอ และเสียง
ประเด็นสำคัญเกี่ยวกับการแปลงเป็นโทเค็น

- **รูปภาพ**: รูปภาพที่มีขนาด ≤384 พิกเซลทั้ง 2 ด้านจะนับเป็น 258 โทเค็น ระบบจะแบ่งรูปภาพที่ใหญ่กว่า
  ออกเป็นไทล์ขนาด 768x768 พิกเซล โดยแต่ละไทล์จะนับเป็น 258 โทเค็น
- **วิดีโอ**: 263 โทเค็นต่อวินาที (ใช้กับการประมวลผลแบบคงที่) สำหรับการประมวลผลแบบเอเจนต์ การใช้โทเค็นจะแตกต่างกันไป ดู[การใช้โทเค็นวิดีโอตามโหมดการประมวลผล](#video-token-usage)
- **เสียง**: 32 โทเค็นต่อวินาที

#### โทเค็นรูปภาพ

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
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
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/image.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

// Count tokens for image + text
CountTokensResponse countResponse =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromText("Tell me about this image"),
                Part.fromUri(
                    uploadedFile.uri().orElse(""), uploadedFile.mimeType().orElse("image/jpeg")))),
        null);
System.out.println("Total tokens: " + countResponse.totalTokens().orElse(0));

// Generate with image
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("Tell me about this image").build(),
                    ImageContent.builder()
                        .uri(uploadedFile.uri().orElse(""))
                        .mimeType(
                            ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
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
            Input:  interactions.NewInteractionsInput("Explain the history of the internet in 3 paragraphs."),
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
        }
        if completed := event.GetDataInteractionCompleted(); completed != nil {
            usage := completed.Interaction.Usage
            if usage != nil && usage.TotalTokens != nil {
                fmt.Printf("\nTotal tokens: %d\n", *usage.TotalTokens)
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

**ตัวอย่างข้อมูลในบรรทัด**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### โทเค็นวิดีโอ

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 100 * 60 = 6,000 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### การใช้โทเค็นวิดีโอตามโหมดการประมวลผล

การใช้โทเค็นสำหรับวิดีโอจะขึ้นอยู่กับโหมดการประมวลผล ดังนี้

| **โหมดการประมวลผล** | **การคำนวณโทเค็น** | **การใช้งานทั่วไป** |
| --- | --- | --- |
| **คงที่** (ค่าเริ่มต้น) | โดยค่าเริ่มต้นจะอยู่ที่ประมาณ 100 โทเค็น/วินาที (ความละเอียดต่ำ) หรือประมาณ 300 โทเค็น/วินาที (ความละเอียดสูง) เฟรมทั้งหมดจะสุ่มตัวอย่างที่ 1 FPS | คาดการณ์ได้ตามสัดส่วนของความยาววิดีโอ |
| **การทำงานแบบเป็น Agent** | แตกต่างกันไปตามความซับซ้อนของเนื้อหา โมเดลจะโหลดเฉพาะข้อความถอดเสียงและ/หรือเฟรมและ/หรือเสียงที่จำเป็นต่อการตอบพรอมต์ | โทเค็นน้อยลงสูงสุด 88% สำหรับเนื้อหาแบบยาว |

การประมวลผลแบบเอเจนต์อาจใช้โทเค็นประมาณ 108,000 รายการสำหรับเลคเชอร์ 1 ชั่วโมง ซึ่งในโหมดคงที่จะใช้โทเค็นประมาณ 1.08 ล้านรายการ ทั้งนี้ขึ้นอยู่กับพรอมต์และเนื้อหา

หากต้องการตรวจสอบการใช้โทเค็นจริงสำหรับคำขอ ให้ตรวจสอบ `interaction.usage` ระบบจะรายงานโทเค็นวิดีโอของเอเจนต์ในช่องต่อไปนี้

- **พรอมต์เริ่มต้น** (วิดีโออ้างอิง + พรอมต์ของผู้ใช้): `total_input_tokens`
- **การคิดเกี่ยวกับการนำทาง**: `total_thought_tokens`
- **ข้อความถอดเสียง เฟรม และเสียงจะโหลดตามคำขอ**: `total_tool_use_tokens`
- **คำตอบสุดท้าย**: `total_output_tokens`

#### โทเค็นเสียง

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### นับโทเค็นคำสั่งของระบบ

คำสั่งของระบบจะนับเป็นส่วนหนึ่งของโทเค็นอินพุต

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### โทเค็นเครื่องมือนับ

ระบบจะนับรวมเครื่องมือ (ฟังก์ชัน การเรียกใช้โค้ด Google Search) ด้วย

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## หน้าต่างบริบท

โมเดล Gemini แต่ละรุ่นมีจำนวนโทเค็นสูงสุดที่จัดการได้ บริบท
หน้าต่างกำหนดขีดจำกัดรวมของโทเค็นอินพุตและเอาต์พุต

### รับขนาดหน้าต่างบริบทโดยใช้โปรแกรม

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.8-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.8-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Model;

Client client = new Client();

Model modelInfo = client.models.get("gemini-3.8-flash", null);
System.out.println("Input token limit: " + modelInfo.inputTokenLimit().orElse(0));
System.out.println("Output token limit: " + modelInfo.outputTokenLimit().orElse(0));
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

    prompt := "Tell me about this instrument"
    imageBytes, err := os.ReadFile("/path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    // Count tokens before creating the interaction
    parts := []*genai.Part{
        genai.NewPartFromText(prompt),
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    }
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Estimated input tokens: %d\n", totalTokens.TotalTokens)

    // Create the multimodal interaction and inspect the usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Total tokens billed: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

ดูขนาดหน้าต่างบริบทได้ในหน้า[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

## ขั้นตอนถัดไป

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th): พื้นฐานการสร้าง
- [การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th): ลดค่าใช้จ่ายด้วยการแคช
- [ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th): ทำความเข้าใจค่าใช้จ่าย

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
