---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=th
fetched_at: 2026-10-26T05:54:24.663683+00:00
title: "\u0e01\u0e33\u0e25\u0e31\u0e07\u0e04\u0e34\u0e14 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# กำลังคิด

[โมเดล Gemini](https://ai.google.dev/gemini-api/docs/models?hl=th) ใช้"กระบวนการคิด" ซึ่งช่วยปรับปรุงความสามารถในการให้เหตุผลและการวางแผนแบบหลายขั้นตอนได้อย่างมาก ทำให้โมเดลมีประสิทธิภาพสูงสำหรับงานที่ซับซ้อน เช่น การเขียนโค้ด คณิตศาสตร์ขั้นสูง และการวิเคราะห์ข้อมูล

เมื่อคุณใช้โมเดลการคิด Gemini จะให้เหตุผลภายในก่อนที่จะตอบ Interactions API จะแสดงการให้เหตุผลนี้ผ่านขั้นตอน `thought` ซึ่งเป็นขั้นตอนเฉพาะที่ปรากฏตามลำดับเวลาควบคู่ไปกับการเรียกใช้ฟังก์ชัน อินพุตของผู้ใช้ หรือเอาต์พุตโมเดลในอาร์เรย์ `steps`

ขั้นตอนการคิดแต่ละขั้นตอนจะมี 2 ฟิลด์ดังนี้

| ช่อง | ต้องระบุ | คำอธิบาย |
| --- | --- | --- |
| `signature` | ✅ ใช่ | การแสดงการเข้ารหัสของสถานะการให้เหตุผลภายในของโมเดล จะปรากฏอยู่เสมอ แม้ว่าโมเดลจะให้เหตุผลเพียงเล็กน้อยก็ตาม |
| `summary` | ❌ ไม่ | อาร์เรย์ของเนื้อหา (ข้อความและ/หรือรูปภาพ) ที่สรุปเหตุผล อาจว่างเปล่า ทั้งนี้ขึ้นอยู่กับการกำหนดค่า [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=th) ว่าโมเดลให้เหตุผลเพียงพอหรือไม่ หรือประเภทเนื้อหา (เช่น รูปภาพที่ซ่อนอยู่อาจไม่มีข้อมูลสรุปที่เป็นข้อความ) |

## การโต้ตอบกับการคิด

การเริ่มการโต้ตอบกับโมเดลการคิดจะคล้ายกับคำขอการโต้ตอบอื่นๆ ระบุหนึ่งใน [โมเดลที่รองรับการคิด](#thinking-levels)ในช่อง `model` ดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
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

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain the concept of Occam's Razor and provide a simple, everyday example."),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## ข้อมูลสรุปความคิด

ข้อมูลสรุปความคิดจะให้ข้อมูลเชิงลึกเกี่ยวกับกระบวนการให้เหตุผลภายในของโมเดล
โดยค่าเริ่มต้น ระบบจะแสดงเฉพาะเอาต์พุตสุดท้าย คุณสามารถเปิดใช้ข้อมูลสรุปความคิดด้วย `thinking_summaries` ดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
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
            Input: interactions.NewInteractionsInput("Provide a list of 3 famous physicists and their key contributions"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

บล็อกความคิดอาจมี**เฉพาะลายเซ็นที่ไม่มีข้อมูลสรุป** ในกรณีต่อไปนี้

- คำขออย่างง่ายที่โมเดลให้เหตุผลไม่เพียงพอที่จะสร้างข้อมูลสรุป
- `thinking_summaries: "none"` ซึ่งมีการปิดใช้ข้อมูลสรุปอย่างชัดเจน
- เนื้อหาความคิดบางประเภท เช่น รูปภาพ อาจไม่มีข้อมูลสรุปที่เป็นข้อความ

โค้ดของคุณควรจัดการบล็อกความคิดที่ `summary` ว่างเปล่าหรือไม่มีอยู่เสมอ

## การสตรีมด้วยการคิด

ใช้การสตรีมเพื่อรับข้อมูลสรุปความคิดแบบเพิ่มทีละน้อยระหว่างการสร้าง
ระบบจะส่งบล็อกความคิดโดยใช้ Server-Sent Events (SSE) ที่มีเดลต้า 2 ประเภทที่แตกต่างกัน ดังนี้

| ประเภทเดลต้า | มี | กรณีที่ส่ง |
| --- | --- | --- |
| `thought_summary` | เนื้อหาข้อมูลสรุปที่เป็นข้อความหรือรูปภาพ | เดลต้าอย่างน้อย 1 รายการที่มีข้อมูลสรุปแบบเพิ่มขึ้นทีละน้อย |
| `thought_signature` | ลายเซ็นการเข้ารหัส | เดลต้าสุดท้ายก่อน `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
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
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought summary:\n%s\n\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

การตอบกลับแบบสตรีมมิงใช้ Server-Sent Events (SSE) และประกอบด้วยขั้นตอนและเหตุการณ์ เช่น

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## การควบคุมการคิด

โมเดล Gemini จะคิดแบบไดนามิกโดยค่าเริ่มต้น ซึ่งจะปรับปริมาณความพยายามในการให้เหตุผลโดยอัตโนมัติตามความซับซ้อนของคำขอ คุณสามารถควบคุมลักษณะการทำงานนี้ได้โดยใช้พารามิเตอร์ `thinking_level`

| รุ่น | การคิดเริ่มต้น | ระดับที่รองรับ |
| --- | --- | --- |
| gemini-4-argon | เปิด (ปานกลาง) | ต่ำ ปานกลาง สูง |
| gemini-3.8-flash | เปิด (ปานกลาง) | ต่ำ ปานกลาง สูง |
| gemini-3.6-flash | เปิด (ปานกลาง) | น้อย ต่ำ ปานกลาง สูง |
| gemini-3.5-flash-lite | เปิด (น้อย) | น้อย ต่ำ ปานกลาง สูง |
| gemini-3.1-pro-preview | เปิด (สูง) | ต่ำ ปานกลาง สูง |
| gemini-3.1-flash-lite-image | เปิด (น้อย) | น้อย สูง |
| gemini-3-flash-preview | เปิด (สูง) | น้อย ต่ำ ปานกลาง สูง |
| gemini-3-pro-preview | เปิด (สูง) | ต่ำ สูง |
| gemini-2.5-pro | เปิด | ต่ำ ปานกลาง สูง |
| gemini-2.5-flash | เปิด | ต่ำ ปานกลาง สูง |
| gemini-2.5-flash-lite | ปิด | ต่ำ ปานกลาง สูง |
| gemini-robotics-er-2-preview | เปิด (สูง) | น้อย ต่ำ ปานกลาง สูง |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
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
            if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("[Thought Summary] %s\n", textContent.Text)
                }
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### ขีดจำกัดของโทเค็นและ `max_output_tokens`

พารามิกเตอร์การสร้าง [`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=th#request-body) จะกำหนดจำนวนโทเค็นสูงสุดที่การตอบกลับสร้างได้ ซึ่งรวมถึงโทเค็นการคิด

เมื่อตั้งค่า พารามิเตอร์นี้จะทำหน้าที่เป็นขีดจำกัดที่กำหนดโดยโครงสร้างพื้นฐานโดยไม่เปลี่ยนวิธีที่โมเดลจัดสรรงบประมาณการคิด (`thinking_level`)

หากโมเดลถึงขีดจำกัดนี้ขณะให้เหตุผล โมเดลจะหยุดสร้างโดยมีสถานะ
`"incomplete"` และแสดงเอาต์พุตที่ถูกตัดทอนหรือว่างเปล่า (พร้อมทั้งเรียกเก็บเงินสำหรับ
โทเค็นการคิดที่สร้างขึ้น) หากต้องการลดต้นทุนหรือเวลาในการตอบสนองโดยไม่ตัดทอนการตอบกลับ ให้ลด `thinking_level` (`low` หรือ `medium`) แทนที่จะตั้งค่า `max_output_tokens` เป็นค่าต่ำ

สำหรับโมเดล Gemini 4 (`gemini-4-argon`) โปรดคำนึงถึงขีดจำกัดของบริบทและเอาต์พุตต่อไปนี้

- **หน้าต่างบริบทขนาด 1 ล้านโทเค็นที่แชร์:** โทเค็นอินพุต การคิด และเอาต์พุตจะแชร์หน้าต่างบริบทขนาด 1 ล้านโทเค็น (`1,048,576` โทเค็น) หากโทเค็นอินพุตบวก `max_output_tokens` เกิน 1,048,576 โทเค็น API จะจำกัดเอาต์พุตโดยอัตโนมัติให้เหลือพื้นที่ในหน้าต่างบริบท (`1,048,576` ลบด้วยโทเค็นอินพุต)
- **ขีดจำกัดเอาต์พุตแบบซิงโครนัสเริ่มต้น (64,000):** เมื่อ `background=False` (สำหรับคำขอแบบสตรีมมิงและไม่ใช่แบบสตรีมมิง) ขีดจำกัด `max_output_tokens` เริ่มต้นและสูงสุดคือ `65,536` โทเค็น การตั้งค่า `max_output_tokens > 65536` โดยมี `background=False` จะแสดงข้อผิดพลาด `400`
- **การถอดรหัสแบบยาว (สูงสุด 1 ล้านโทเค็น):** หากต้องการให้ Gemini 4 ให้เหตุผลและสร้างโทเค็นเกิน `65,536` โทเค็น (สูงสุด `1,048,576` โทเค็น) ให้ตั้งค่า `background=True` และกำหนดค่า `max_output_tokens` มากกว่า `65,536` ดูรายละเอียดได้ที่[การถอดรหัสแบบยาว](https://ai.google.dev/gemini-api/docs/long-decode?hl=th)

## ลายเซ็นความคิด

ลายเซ็นความคิดเป็นการแสดงการเข้ารหัสของการให้เหตุผลภายในของโมเดล จำเป็นต้องใช้ลายเซ็นความคิดเพื่อรักษาความต่อเนื่องของการให้เหตุผลในการโต้ตอบแบบหลายรอบ

Interactions API ช่วยให้การจัดการลายเซ็นความคิดง่ายกว่า `generateContent` API มาก

### โหมดเก็บสถานะ (แนะนำ)

โดยค่าเริ่มต้น เมื่อคุณใช้ Interactions API ในโหมดเก็บสถานะ (โดยตั้งค่า `store: true` และส่ง `previous_interaction_id` ในรอบถัดไป) เซิร์ฟเวอร์จะจัดการสถานะการสนทนาโดยอัตโนมัติ ซึ่งรวมถึงบล็อกความคิดและลายเซ็นทั้งหมด ในโหมดนี้ คุณไม่จำเป็นต้องดำเนินการใดๆ เกี่ยวกับลายเซ็น เนื่องจากเซิร์ฟเวอร์จะจัดการลายเซ็นทั้งหมด

### โหมดไม่เก็บสถานะ

หากคุณจัดการสถานะการสนทนาด้วยตนเอง (โหมดไม่เก็บสถานะ) และส่งประวัติอินพุตและเอาต์พุตทั้งหมดในแต่ละคำขอ

- คุณ**ต้อง** ส่งบล็อก `thought` ทั้งหมดอีกครั้งตามที่ได้รับจากโมเดลทุกประการ
- คุณ**ไม่ควร** นำบล็อกความคิดออกจากประวัติหรือแก้ไขบล็อกความคิด เนื่องจากบล็อกความคิดมีลายเซ็นที่โมเดลต้องใช้เพื่อดำเนินการให้เหตุผลต่อไป
- เมื่อเปลี่ยนโมเดลภายในเซสชัน คุณควรส่งบล็อกความคิดของโมเดลก่อนหน้าอีกครั้ง แบ็กเอนด์จะจัดการความเข้ากันได้

## ราคา

เมื่อเปิดการคิด ราคาการตอบกลับจะเป็นผลรวมของโทเค็นเอาต์พุตและโทเค็นการคิด คุณสามารถดูจำนวนโทเค็นการคิดทั้งหมดที่สร้างขึ้นได้จากช่อง `total_thought_tokens`

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
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

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
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

    // Turn 1: Execute a reasoning + tool use interaction
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Compare the GDP growth of Japan and Germany in 2025."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Pass PreviousInteractionID so thought signatures are automatically preserved
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-pro"),
            PreviousInteractionID: turn1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Now summarize that comparison in a 3-row markdown table."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

โมเดลการคิดจะสร้างความคิดทั้งหมดเพื่อปรับปรุงคุณภาพของการตอบกลับสุดท้าย
แล้วแสดงข้อมูลสรุปเพื่อแสดงข้อมูลเชิงลึกเกี่ยวกับกระบวนการคิด
ราคาจะอิงตามโทเค็นความคิดทั้งหมดที่โมเดลต้องสร้าง แม้ว่า API จะแสดงเฉพาะข้อมูลสรุปก็ตาม

ดูข้อมูลเพิ่มเติมเกี่ยวกับโทเค็นได้ในคู่มือ[การนับโทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

## แนวทางปฏิบัติแนะนำ

ใช้โมเดลการคิดอย่างมีประสิทธิภาพโดยทำตามหลักเกณฑ์ต่อไปนี้

- **ตรวจสอบการให้เหตุผล**: วิเคราะห์ข้อมูลสรุปความคิดเพื่อทำความเข้าใจข้อผิดพลาดและปรับปรุงพรอมต์
- **ควบคุมงบประมาณการคิด**: แจ้งให้โมเดลคิดน้อยลงสำหรับเอาต์พุตที่ยาวเพื่อประหยัดโทเค็น
- **งานง่ายๆ**: ใช้การคิดน้อยหรือต่ำสำหรับการดึงข้อมูลข้อเท็จจริงหรือการจัดประเภท (เช่น "DeepMind ก่อตั้งขึ้นที่ไหน")
- **งานปานกลาง**: ใช้การคิดเริ่มต้นสำหรับการเปรียบเทียบแนวคิดหรือการให้เหตุผลเชิงสร้างสรรค์ (เช่น เปรียบเทียบรถยนต์ไฟฟ้าและรถยนต์ไฮบริด)
- **งานที่ซับซ้อน**: ใช้การคิดสูงสุดสำหรับการเขียนโค้ด คณิตศาสตร์ หรือการวางแผนแบบหลายขั้นตอนขั้นสูง (เช่น แก้ปัญหาคณิตศาสตร์ AIME)

## ขั้นตอนถัดไป

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th): การตอบกลับที่เป็นข้อความพื้นฐาน
- [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th): เชื่อมต่อกับเครื่องมือ
- [คู่มือ Gemini 4](https://ai.google.dev/gemini-api/docs/latest-model?hl=th): มีอะไรใหม่ใน Gemini 4
- [คู่มือ Gemini 3](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=th): ฟีเจลร์เฉพาะของโมเดล

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-14 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-14 UTC"],[],[]]
