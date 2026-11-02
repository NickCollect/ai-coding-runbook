---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=th
fetched_at: 2026-11-02T07:31:16.380646+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e02\u0e2d\u0e07\u0e2a\u0e37\u0e48\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความละเอียดของสื่อ

พารามิเตอร์ `media_resolution` จะควบคุมวิธีที่ Gemini API ประมวลผลอินพุตสื่อ เช่น รูปภาพ วิดีโอ เสียง และเอกสาร PDF โดยกำหนด**จำนวนโทเค็นสูงสุด** ที่จัดสรรไว้สำหรับอินพุตสื่อ ซึ่งช่วยให้คุณปรับสมดุลคุณภาพการตอบสนองกับเวลาในการตอบสนองและค่าใช้จ่ายได้ แม้ว่าอินพุตภาพและเอกสารจะปรับขนาดการจัดสรรโทเค็นตามการตั้งค่าความละเอียด แต่อินพุตเสียงจะมีการแปลงเป็นโทเค็นในอัตราคงที่ต่อวินาทีในทุกระดับความละเอียด สำหรับการตั้งค่าต่างๆ ค่าเริ่มต้น และวิธีที่การตั้งค่าเหล่านั้นสอดคล้องกับโทเค็น โปรดดูส่วน
[จำนวนโทเค็น](#token-counts)

คุณสามารถกำหนดค่าความละเอียดของสื่อสำหรับออบเจ็กต์สื่อ (รายการเนื้อหา) แต่ละรายการภายในคำขอ (โมเดล Gemini 4 และ Gemini 3)

## ความละเอียดของสื่อต่อรายการเนื้อหา (โมเดล Gemini 4 และ Gemini 3)

โมเดล Gemini 4 และ Gemini 3 ช่วยให้คุณกำหนดความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการภายในคำขอได้ ซึ่งช่วยให้คุณเพิ่มประสิทธิภาพการใช้โทเค็นได้อย่างละเอียด คุณสามารถผสมระดับความละเอียดในคำขอเดียวได้ เช่น ใช้ความละเอียดสูงสำหรับแผนภาพที่ซับซ้อน และความละเอียดต่ำสำหรับรูปภาพตามบริบทอย่างง่าย

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## ค่าความละเอียดที่ใช้ได้

Gemini API กำหนดระดับความละเอียดของสื่อไว้ดังนี้

- `unspecified`: การตั้งค่าเริ่มต้น จำนวนโทเค็นสำหรับระดับนี้จะแตกต่างกันอย่างมากระหว่าง Gemini 4/3 กับโมเดล Gemini รุ่นก่อนหน้า
- `low`: จำนวนโทเค็นต่ำกว่า ส่งผลให้การประมวลผลเร็วขึ้นและค่าใช้จ่ายลดลง แต่รายละเอียดน้อยลง
- `medium`: ความสมดุลระหว่างรายละเอียด ค่าใช้จ่าย และเวลาในการตอบสนอง
- `high`: จำนวนโทเค็นสูงกว่า ซึ่งให้รายละเอียดมากขึ้นเพื่อให้โมเดลทำงานได้ แต่เวลาในการตอบสนองและค่าใช้จ่ายจะเพิ่มขึ้น
- `ultra_high` (ต่อรายการเนื้อหาเท่านั้น): จำนวนโทเค็นสูงสุด ซึ่งจำเป็นสำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น [การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

โปรดทราบว่า `high` ให้ประสิทธิภาพสูงสุดสำหรับกรณีการใช้งานส่วนใหญ่

จำนวนโทเค็นที่แน่นอนซึ่งสร้างขึ้นสำหรับแต่ละระดับจะขึ้นอยู่กับทั้ง**ประเภทสื่อ** (รูปภาพ วิดีโอ เสียง, PDF) และ**เวอร์ชันของโมเดล**

## จำนวนโทเค็น

ตารางด้านล่างสรุปจำนวนโทเค็นโดยประมาณสำหรับค่า `media_resolution` และประเภทสื่อแต่ละรายการต่อตระกูลโมเดล

**โมเดล Gemini 4 และ Gemini 3**

| MediaResolution | รูปภาพ | วิดีโอ | เสียง | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (ค่าเริ่มต้น) | 1120 | 70 | 25 (ต่อวินาที) | 560 |
| `low` | 280 | 70 | 25 (ต่อวินาที) | 280 + ข้อความเนทีฟ |
| `medium` | 560 | 70 | 25 (ต่อวินาที) | 560 + ข้อความเนทีฟ |
| `high` | 1120 | 280 | 25 (ต่อวินาที) | 1120 + ข้อความเนทีฟ |
| `ultra_high` | 2240 | ไม่มีข้อมูล | ไม่มี | ไม่มีข้อมูล |

## การเลือกความละเอียดที่เหมาะสม

- **ค่าเริ่มต้น (`unspecified`):** เริ่มต้นด้วยค่าเริ่มต้น ซึ่งได้รับการปรับแต่งให้มีความสมดุลที่ดีระหว่างคุณภาพ เวลาในการตอบสนอง และค่าใช้จ่ายสำหรับกรณีการใช้งานที่พบบ่อยที่สุด
- **`low`:** ใช้ในสถานการณ์ที่ค่าใช้จ่ายและเวลาในการตอบสนองมีความสำคัญสูงสุด และรายละเอียดที่ละเอียดมีความสำคัญน้อยกว่า
- **`medium` / `high`:** เพิ่มความละเอียดเมื่องานต้องใช้ความเข้าใจรายละเอียดที่ซับซ้อนภายในสื่อ ซึ่งมักจำเป็นสำหรับการวิเคราะห์ภาพที่ซับซ้อน การอ่านแผนภูมิ หรือความเข้าใจเอกสารที่มีข้อมูลหนาแน่น
- **`ultra_high`** - ใช้ได้กับการตั้งค่าต่อรายการเนื้อหาเท่านั้น แนะนำสำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น การใช้คอมพิวเตอร์ หรือในกรณีที่การทดสอบแสดงให้เห็นว่า `high` มีการปรับปรุงอย่างชัดเจน
- **การควบคุมต่อรายการเนื้อหา (Gemini 4 และ Gemini 3):** เพิ่มประสิทธิภาพการใช้โทเค็น เช่น ในพรอมต์ที่มีรูปภาพหลายรายการ ให้ใช้ `high` สำหรับแผนภาพที่ซับซ้อน และ `low` หรือ `medium` สำหรับรูปภาพตามบริบทที่ง่ายกว่า

**การตั้งค่าที่แนะนำ**

รายการต่อไปนี้แสดงการตั้งค่าความละเอียดของสื่อที่แนะนำสำหรับสื่อแต่ละประเภทที่รองรับ

| ประเภทสื่อ | การตั้งค่าที่แนะนำ | โทเค็นสูงสุด | คำแนะนำการใช้งาน |
| --- | --- | --- | --- |
| **Google รูปภาพ** | `high` | 1120 | แนะนำสำหรับงานวิเคราะห์รูปภาพส่วนใหญ่เพื่อให้ได้คุณภาพสูงสุด |
| **PDF** | `medium` | 560 | เหมาะที่สุดสำหรับความเข้าใจเอกสาร โดยคุณภาพจะอิ่มตัวที่ `medium` โดยทั่วไป การเพิ่มเป็น `high` ไม่ค่อยปรับปรุงผลลัพธ์ OCR สำหรับเอกสารมาตรฐาน |
| **วิดีโอ** (ทั่วไป) | `low` (หรือ `medium`) | 70 (ต่อเฟรม) | **หมายเหตุ:** สำหรับวิดีโอ ระบบจะถือว่าการตั้งค่า `low` และ `medium` เหมือนกัน (70 โทเค็น) เพื่อเพิ่มประสิทธิภาพการใช้บริบท ซึ่งเพียงพอสำหรับงานการจดจำและการอธิบายการกระทำส่วนใหญ่ |
| **วิดีโอ** (มีข้อความจำนวนมาก) | `high` | 280 (ต่อเฟรม) | จำเป็นเฉพาะเมื่อกรณีการใช้งานเกี่ยวข้องกับการอ่านข้อความที่มีข้อมูลหนาแน่น (OCR) หรือรายละเอียดเล็กๆ ภายในเฟรมวิดีโอ |
| **เสียง** | `unspecified` (ค่าเริ่มต้น) | 25 (ต่อวินาที) | ระบบจะแปลงเสียงเป็นโทเค็นในอัตราคงที่ 25 โทเค็นต่อวินาทีในการตั้งค่าความละเอียดทั้งหมดที่รองรับ (`unspecified`, `low`, `medium` และ `high`) |

ทดสอบและประเมินผลกระทบของการตั้งค่าความละเอียดต่างๆ ในแอปพลิเคชันของคุณเสมอ เพื่อหาจุดสมดุลที่ดีที่สุดระหว่างคุณภาพ เวลาในการตอบสนอง และค่าใช้จ่าย

## ความสัมพันธ์กับโหมดการประมวลผลวิดีโอ

พารามิเตอร์ `media_resolution` และการประมวลผลจะควบคุมอินพุตวิดีโอในด้านต่างๆ ดังนี้

- `media_resolution` ควบคุม**ความละเอียด** ของแต่ละเฟรม (จำนวนโทเค็นต่อเฟรม)
- `processing` / `media_processing` ควบคุม**เนื้อหาใดจากวิดีโอ** ที่โหลดลงในบริบท

คุณสามารถตั้งค่าทั้ง 2 อย่างในอินพุตวิดีโอเดียวกันได้ เช่น คุณอาจใช้การประมวลผลแบบ Agentic ที่มีความละเอียดของสื่อต่ำเพื่อลดการใช้โทเค็นทั้งหมดสำหรับวิดีโอขนาดยาว

ดูรายละเอียดเกี่ยวกับโหมดการประมวลผลวิดีโอได้ที่[คู่มือความเข้าใจวิดีโอแบบ Agentic](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#agentic-video-understanding)

## สรุปความเข้ากันได้กับเวอร์ชัน

- การตั้งค่า `resolution` ในรายการเนื้อหาแต่ละรายการ **รองรับในโมเดล Gemini 4 และ Gemini 3**

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับความสามารถแบบมัลติโมดัลของ Gemini API ได้ในคู่มือ
  [ความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th),
  [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th), [ความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th),
  และ [ความเข้าใจเอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-13 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-13 UTC"],[],[]]
