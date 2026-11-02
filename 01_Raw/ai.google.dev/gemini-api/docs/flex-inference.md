---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=th
fetched_at: 2026-11-02T07:03:05.803106+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e19\u0e38\u0e21\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e37\u0e14\u0e2b\u0e22\u0e38\u0e48\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอนุมานแบบยืดหยุ่น

Gemini Flex API เป็นระดับการอนุมานที่ช่วยลดต้นทุนได้ 50% เมื่อเทียบกับอัตรามาตรฐาน แลกกับการตอบสนองที่อาจแตกต่างกันไปและความพร้อมให้บริการแบบเต็มความสามารถ โดยออกแบบมาสำหรับเวิร์กโหลดที่ยอมรับการตอบสนองที่อาจแตกต่างกันไปได้ ซึ่งต้องมีการประมวลผลแบบซิงโครนัส แต่ไม่จำเป็นต้องมีประสิทธิภาพแบบเรียลไทม์เหมือน API มาตรฐาน

## วิธีใช้ Flex

หากต้องการใช้ระดับ Flex ให้ระบุ `service_tier` เป็น `flex` ในคำขอ โดยค่าเริ่มต้น คำขอจะใช้ระดับมาตรฐานหากละเว้นช่องนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
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
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
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
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## วิธีทำงานของ Flex Inference

Flex Inference ของ Gemini ช่วยลดช่องว่างระหว่าง API มาตรฐานกับ[API แบบกลุ่ม](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)ที่ใช้เวลาดำเนินการ 24 ชั่วโมง
โดยใช้ความสามารถในการประมวลผลที่ "ลดได้" ในช่วงเวลาที่ไม่ใช่ช่วงเวลาที่มีการใช้งานสูงสุด เพื่อมอบโซลูชันที่คุ้มค่าสำหรับงานเบื้องหลังและเวิร์กโฟลว์แบบลำดับ

| ฟีเจอร์ | Flex | รายการสำคัญ | มาตรฐาน | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | ส่วนลด 50% | สูงกว่ามาตรฐาน 75-100% | ราคาเต็ม | ส่วนลด 50% |
| **การตอบสนอง** | นาที (เป้าหมาย 1-15 นาที) | ต่ำ (วินาที) | วินาทีถึงนาที | สูงสุด 24 ชั่วโมง |
| **ความเสถียร** | เต็มความสามารถ (ลดได้) | สูง (ลดไม่ได้) | สูง / สูงปานกลาง | สูง (สำหรับการส่งข้อความปริมาณมาก) |
| **อินเทอร์เฟซ** | แบบซิงโครนัส | แบบซิงโครนัส | แบบซิงโครนัส | แบบอะซิงโครนัส |

### ประโยชน์สำคัญ

- **ความคุ้มค่า**: ประหยัดค่าใช้จ่ายได้มากสำหรับการประเมินที่ไม่ใช่การใช้งานจริง, เอเจนต์เบื้องหลัง และการเพิ่มคุณค่าของข้อมูล
- **ใช้งานง่าย**: เพียงเพิ่มพารามิเตอร์เดียวลงในคำขอที่มีอยู่
- **เวิร์กโฟลว์แบบซิงโครนัส**: เหมาะอย่างยิ่งสำหรับเชน API แบบลำดับที่คำขอถัดไปขึ้นอยู่กับเอาต์พุตของคำขอก่อนหน้า ซึ่งทำให้มีความยืดหยุ่นมากกว่า API แบบกลุ่มสำหรับเวิร์กโฟลว์แบบเอเจนต์

### กรณีการใช้งาน

- **การประเมินแบบออฟไลน์**: การเรียกใช้การทดสอบการถดถอยหรือลีดเดอร์บอร์ด "LLM-as-a-judge"
- **เอเจนต์เบื้องหลัง**: งานแบบลำดับ เช่น การอัปเดต CRM, การสร้างโปรไฟล์ หรือการกลั่นกรองเนื้อหาที่ยอมรับความล่าช้าได้เป็นนาที
- **การวิจัยที่ถูกจำกัดด้วยงบประมาณ**: การทดลองทางวิชาการที่ต้องใช้โทเค็นจำนวนมากแต่มีงบประมาณจำกัด

### การจำกัดอัตราคำขอ

การเข้าชมการอนุมานแบบ Flex จะนับรวมใน[ขีดจำกัดอัตรา](https://aistudio.google.com/rate-limit?hl=th)ทั่วไป และไม่มี
ขีดจำกัดอัตราที่ขยายออกไปเหมือน [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)

### ความสามารถที่ลดได้

ระบบจะถือว่าการเข้าชมแบบ Flex มีลำดับความสำคัญต่ำกว่า หากมีการเข้าชมมาตรฐานเพิ่มขึ้นอย่างรวดเร็ว ระบบอาจขัดจังหวะหรือนำคำขอแบบ Flex ออกเพื่อให้มีความสามารถสำหรับผู้ใช้ที่มีลำดับความสำคัญสูง หากต้องการการอนุมานที่มีลำดับความสำคัญสูง โปรดดู
[การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)

### รหัสข้อผิดพลาด

เมื่อความสามารถแบบ Flex ไม่พร้อมใช้งานหรือระบบมีการใช้งานหนาแน่น API จะแสดงรหัสข้อผิดพลาดมาตรฐานดังนี้

- **503 ไม่พร้อมให้บริการ**: ขณะนี้ระบบมีผู้ใช้เต็มแล้ว
- **429 คำขอมากเกินไป**: การจำกัดอัตราคำขอหรือทรัพยากรหมด

### ความรับผิดชอบของไคลเอ็นต์

- **ไม่มีการย้อนกลับฝั่งเซิร์ฟเวอร์**: ระบบจะไม่
  ยกระดับคำขอแบบ Flex เป็นระดับมาตรฐานโดยอัตโนมัติหากความสามารถแบบ Flex
  เต็ม เพื่อป้องกันค่าใช้จ่ายที่ไม่คาดคิด
- **การลองอีกครั้ง**: คุณต้องใช้ตรรกะการลองอีกครั้งฝั่งไคลเอ็นต์ของคุณเองด้วย
  Exponential Backoff
- **การหมดเวลา**: เนื่องจากคำขอแบบ Flex อาจอยู่ในคิว เราจึงแนะนำให้
  เพิ่มระยะหมดเวลาฝั่งไคลเอ็นต์เป็น 10 นาทีขึ้นไปเพื่อหลีกเลี่ยงการ
  ปิดการเชื่อมต่อก่อนเวลา

## ปรับกรอบเวลาหมดเวลา

คุณสามารถกำหนดค่าระยะหมดเวลาต่อคำขอสำหรับ REST API และไลบรารีของไคลเอ็นต์
ตรวจสอบเสมอว่าระยะหมดเวลาฝั่งไคลเอ็นต์ครอบคลุมกรอบเวลาที่เซิร์ฟเวอร์รอได้ (เช่น 600 วินาทีขึ้นไปสำหรับคิวรอแบบ Flex) SDK คาดหวังค่าหมดเวลาเป็นมิลลิวินาที

### ระยะหมดเวลาต่อคำขอ

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## ใช้การลองอีกครั้ง

เนื่องจาก Flex ลดได้และล้มเหลวด้วยข้อผิดพลาด 503 ต่อไปนี้คือตัวอย่างการใช้ตรรกะการลองอีกครั้ง (ไม่บังคับ) เพื่อดำเนินการต่อกับคำขอที่ล้มเหลว

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.8-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.8-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## การกำหนดราคา

Flex Inference มีราคาอยู่ที่ 50% ของ [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
และเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

โมเดลต่อไปนี้รองรับ Flex Inference

| โมเดล | การอนุมานแบบ Flex |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=th) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=th) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Pro เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3 Flash เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

- [การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)สำหรับเวลาในการตอบสนองต่ำมาก
- [โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th): ทำความเข้าใจโทเค็น

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-13 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-13 UTC"],[],[]]
