---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th
fetched_at: 2026-09-28T06:26:02.407447+00:00
title: "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e41\u0e25\u0e30\u0e0a\u0e38\u0e14\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บันทึกและชุดข้อมูล

ในคู่มือนี้ คุณจะได้เรียนรู้วิธี
ดูบันทึกจากการใช้งาน Gemini API ในแดชบอร์ด Google AI Studio
เพื่อให้เข้าใจพฤติกรรมของโมเดลได้ดียิ่งขึ้น และวิธีที่ผู้ใช้อาจโต้ตอบกับแอปพลิเคชันของคุณ ใช้การบันทึกเพื่อสังเกต แก้ไขข้อบกพร่อง และ*แชร์ความคิดเห็นเกี่ยวกับการใช้งานกับ Google (ไม่บังคับ) เพื่อช่วยปรับปรุง Gemini ในกรณีการใช้งานของนักพัฒนาซอฟต์แวร์*[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=th)

ระบบรองรับการเรียก API ทั้งหมดของ `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` และการเรียก API ของ [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=th) ยกเว้น Agent ที่ได้รับการจัดการ ซึ่งรวมถึงการโทรผ่านปลายทาง[ความเข้ากันได้กับ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)

## กำหนดค่าการบันทึกโปรเจ็กต์

โดยค่าเริ่มต้น API จะจัดเก็บออบเจ็กต์การโต้ตอบทั้งหมด (`store=true`) เพื่อ
ลดความซับซ้อนในการใช้ฟีเจอร์การจัดการสถานะฝั่งเซิร์ฟเวอร์ ในทางตรงกันข้าม Generate Content API จะไม่จัดเก็บคำขอโดยค่าเริ่มต้น และต้องเปิดใช้พื้นที่เก็บข้อมูลต่อคำขอหรือที่ระดับโปรเจ็กต์จาก AI Studio

ใน [AI Studio](https://aistudio.google.com/logs?hl=th) ของ Google คุณสามารถเปิดหรือปิดใช้การบันทึกสำหรับทุกโปรเจ็กต์หรือโปรเจ็กต์ที่เฉพาะเจาะจง และเปลี่ยนค่ากำหนดเหล่านี้ได้ทุกเมื่อผ่านแผง**การตั้งค่า**ในหน้า[บันทึกและชุดข้อมูล](https://aistudio.google.com/logs?hl=th) คุณสามารถเปิดหรือปิดการบันทึก
แยกกันสำหรับ `generateContent` API และ
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=th) API
เพื่อเปลี่ยนลักษณะการทำงานของการจัดเก็บเริ่มต้นสำหรับโปรเจ็กต์

### การบันทึกระดับคำขอ

ลักษณะการทำงานของพื้นที่เก็บข้อมูลและการบันทึกจะแตกต่างกันไปตาม API ดังนี้

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th):** จัดเก็บคำขอโดยค่าเริ่มต้น (`store=true`) เพื่อลดความซับซ้อนในการจัดการสถานะฝั่งเซิร์ฟเวอร์
- **สร้าง Content API (`generateContent`):** ไม่จัดเก็บคำขอโดยค่าเริ่มต้น (`store=false`)

วิธีตั้งค่าพร็อพเพอร์ตี้ `store` มีดังนี้

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

// The GenerateContent API does not store requests by default
GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder().build());

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

    // The GenerateContent API does not store requests by default
    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{},
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
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
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
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
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
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

## ดูบันทึกของโปรเจ็กต์ใน AI Studio

1. ไปที่หน้าบันทึกใน [AI Studio](https://aistudio.google.com/logs?hl=th)
2. เลือกโปรเจ็กต์จากเมนูแบบเลื่อนลง
3. บันทึกจะปรากฏในตารางตามลำดับเวลาแบบย้อนหลังสำหรับ Interactions API หากมี
4. หากต้องการดูบันทึกของโปรเจ็กต์สำหรับ Generate Content API ให้เปิดใช้ใน[แผงการตั้งค่า](#configure-logging)ก่อน

คลิกรายการเพื่อดูตัวอย่างเพย์โหลด คุณสามารถ
ตรวจสอบพรอมต์และคำตอบทั้งหมดจาก Gemini รวมถึงบริบทจาก
การสนทนาก่อนหน้าได้ สำหรับคำขอ **Interactions API** บันทึกจะรวมลิงก์โดยตรงไปยัง `previous_interaction_id` ด้วย

## กำหนดค่าการเก็บรักษาพื้นที่เก็บข้อมูลของโปรเจ็กต์

บันทึกจะหมดอายุและมีการทำเครื่องหมายว่าต้องลบหลังจากระยะเวลาเก็บรักษาเริ่มต้นที่ 55 วัน (เว้นแต่จะ[บันทึกลงในชุดข้อมูล](#create) ซึ่งจะไม่มีวันหมดอายุ)
คุณกำหนดค่ากรอบเวลาการเก็บรักษาบันทึกของโปรเจ็กต์ได้สูงสุด 7, 14, 28 หรือ 55 วัน

## สร้างและแชร์ชุดข้อมูล

คุณสามารถบันทึกบันทึกลงในชุดข้อมูลเพื่อจัดระเบียบและส่งออกได้อย่างมีประสิทธิภาพมากขึ้น

- จาก[หน้าบันทึก](https://aistudio.google.com/logs?hl=th) ให้ค้นหาแถบตัวกรอง
  ที่ด้านบนเพื่อเลือกพร็อพเพอร์ตี้ที่จะใช้กรอง
- จากมุมมองที่กรองแล้ว ให้ใช้ช่องทําเครื่องหมายเพื่อเลือกบันทึกทั้งหมดหรือบันทึกแต่ละรายการ
- คลิกปุ่ม**สร้างชุดข้อมูล**ที่ปรากฏที่ด้านบนของรายการ
- ตั้งชื่อและใส่คำอธิบาย (ไม่บังคับ) ให้กับชุดข้อมูลใหม่
- คุณจะเห็นชุดข้อมูลที่เพิ่งสร้างขึ้นพร้อมชุดบันทึกที่ดูแลจัดการแล้ว
- ส่งออกชุดข้อมูลเพื่อวิเคราะห์เพิ่มเติมเป็นไฟล์ CSV, JSONL หรือไปยัง Google ชีต

ชุดข้อมูลอาจเป็นประโยชน์สำหรับ Use Case ที่แตกต่างกันจำนวนหนึ่ง

- **ดูแลชุดความท้าทาย:** ขับเคลื่อนการปรับปรุงในอนาคตซึ่งมุ่งเน้นไปยังส่วนที่คุณต้องการให้ AI ปรับปรุง
- **ดูแลชุดตัวอย่าง:** เช่น ตัวอย่างจากการใช้งานจริงเพื่อสร้างคำตอบจากโมเดลอื่น หรือรวบรวมกรณีที่พบได้ยากเพื่อตรวจสอบตามปกติก่อนการติดตั้งใช้งาน
- **ชุดการประเมิน:** ชุดที่แสดงถึงการใช้งานจริงในความสามารถที่สำคัญ เพื่อใช้เปรียบเทียบกับโมเดลอื่นๆ หรือการทำซ้ำคำสั่งของระบบ

คุณสามารถมีส่วนร่วมในการวิจัยและพัฒนา Gemini ได้โดยเลือกแชร์
ชุดข้อมูลกับ Google เป็นตัวอย่างการสาธิต

## ข้อจำกัด

ปัจจุบันระบบยังไม่รองรับการบันทึกสำหรับรายการต่อไปนี้

- โมเดล Imagen และ Veo
- โมเดลการฝังของ Gemini
- โมเดล Gemini Robotics
- อินพุตที่มีวิดีโอ, GIF หรือ PDF
- Agent เวอร์ชันตัวอย่างแบบสาธารณะใน Gemini API

## ขั้นตอนถัดไป

- **สร้างต้นแบบด้วยประวัติเซสชัน:** ใช้ [AI Studio Build](https://aistudio.google.com/apps?hl=th) เพื่อสร้างแอปโค้ดและเพิ่มคีย์ API เพื่อเปิดใช้ประวัติบันทึก Gemini API สำหรับฟีเจอร์ AI
- **เรียกใช้บันทึกอีกครั้งด้วย Gemini Batch API:** ใช้ชุดข้อมูลสำหรับการสุ่มตัวอย่างคำตอบ
  และการประเมินโมเดลหรือตรรกะของแอปพลิเคชันโดยการเรียกใช้บันทึกอีกครั้งด้วย
  [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
