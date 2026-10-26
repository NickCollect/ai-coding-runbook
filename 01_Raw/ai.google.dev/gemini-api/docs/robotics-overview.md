---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th
fetched_at: 2026-10-26T06:01:56.798655+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Gemini Robotics ER

โมเดล Gemini Robotics ER (การให้เหตุผลแบบเป็นรูปธรรม) เป็นโมเดลภาษาภาพ (VLM) ที่ช่วยให้หุ่นยนต์รับรู้และโต้ตอบกับโลกทางกายภาพได้ โดยจะตีความข้อมูลภาพ ทำการให้เหตุผลเชิงพื้นที่และเชิงเวลา วางแผนงานที่มีหลายขั้นตอน และควบคุมหุ่นยนต์และเครื่องมือต่างๆ

## โมเดล

โมเดล Gemini Robotics ER 2 เป็นโมเดลล่าสุดใน Gemini Robotics
ซึ่งเป็นโมเดลการให้เหตุผลที่อัปเดตแล้วของเราที่ช่วยให้หุ่นยนต์เข้าใจสภาพแวดล้อมได้อย่างแม่นยำ โมเดลนี้เชี่ยวชาญด้านความสามารถในการให้เหตุผลแบบเป็นรูปธรรม เช่น การจัดระเบียบหุ่นยนต์แบบ Agentic (เช่น การใช้ VLA) ความเข้าใจวิดีโอของหุ่นยนต์ รวมถึงความเข้าใจความคืบหน้าและการตรวจจับความสำเร็จ การอ่านเครื่องมือ การชี้ และการให้เหตุผลเชิงพื้นที่

โมเดล Gemini Robotics ER 2 มีปลายทางโมเดล 2 รายการดังนี้

- **`gemini-robotics-er-2-preview`**: โมเดล ER 2 มาตรฐาน ต่อยอดจาก Gemini 3.5 Flash ด้วยการปรับปรุงการให้เหตุผลเชิงพื้นที่ การค้นหาช่วงเวลาในวิดีโอ การจัดประเภทความคืบหน้าของวิดีโอ การจัดระเบียบหุ่นยนต์หลายตัว และการใช้เครื่องมือแบบหลายขั้นตอน
- **`gemini-robotics-er-2-streaming-preview`**: เพิ่มประสิทธิภาพสำหรับการสตรีมแบบเรียลไทม์โดยใช้ [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) ใช้โมเดลนี้สำหรับเอเจนต์หุ่นยนต์ที่มีเวลาในการตอบสนองต่ำซึ่งประมวลผลอินพุตเสียงและวิดีโออย่างต่อเนื่อง

Gemini Robotics ER 1.6 [เลิกใช้งานแล้วเมื่อวันที่ 31 สิงหาคม 2026](https://ai.google.dev/gemini-api/docs/deprecations?hl=th#robotics-models)
หากคุณยังใช้ Gemini Robotics ER 1.6 อยู่ ให้อัปเกรดเป็น Gemini Robotics ER 2 โดยแทนที่ `model="gemini-robotics-er-1.6-preview"` ด้วย `model="gemini-robotics-er-2-preview"` หรือ `model="gemini-robotics-er-2-streaming-preview"` ในการเรียก API

[ลองใช้ Gemini Robotics ER 2 ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=th)

## ความสามารถด้านวิทยาการหุ่นยนต์

Gemini Robotics ER รองรับความสามารถในการให้เหตุผลแบบเป็นรูปธรรมที่หลากหลาย
เลือกความสามารถเพื่อดูข้อมูลเพิ่มเติม

| ความสามารถ | คำอธิบาย | คู่มือ |
| --- | --- | --- |
| การให้เหตุผลเชิงพื้นที่ | ชี้ไปที่วัตถุ ติดตามวัตถุในวิดีโอ ตรวจจับด้วยกรอบล้อมรอบ วางแผนวิถีการเคลื่อนที่ | [การให้เหตุผลเชิงพื้นที่](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=th) |
| วิสัยทัศน์เกี่ยวกับ Agentic AI | ใช้การเรียกใช้โค้ดเพื่อเพิ่มประสิทธิภาพความสามารถอื่นๆ โดยใช้เครื่องมือจัดการรูปภาพ | [วิสัยทัศน์ของ Agentic](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=th) |
| การจัดการงาน | รวมการให้เหตุผลเชิงพื้นที่เข้ากับ API ของหุ่นยนต์ที่กำหนดเองเพื่อทำงานระยะยาวให้เสร็จสมบูรณ์ | [การเรียบเรียงงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) |
| สตรีมมิง (ปลายทางสตรีมมิง Gemini Robotics ER 2 เท่านั้น) | การสตรีมแบบ 2 ทิศทางสำหรับเอเจนต์หุ่นยนต์แบบเรียลไทม์ที่มีการเรียกใช้ฟังก์ชันเวลาในการตอบสนองต่ำ | [สตรีมมิงสำหรับหุ่นยนต์](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) |
| ความคืบหน้าของวิดีโอ (Gemini Robotics ER 2 เท่านั้น) | การค้นหาช่วงเวลาและการแยกประเภทความคืบหน้าจากฟีดวิดีโอต่อเนื่อง | [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) |

## ก่อนเริ่มต้น

โมเดล ER ของ Gemini Robotics พร้อมให้บริการผ่าน **Gemini Developer API** หากต้องการเริ่มต้นใช้งาน ให้สร้าง[คีย์ Gemini API](https://ai.google.dev/gemini-api/docs/api-key?hl=th) จาก [Google AI Studio](https://aistudio.google.com/apikey?hl=th) หรือ[คอนโซล Google Cloud](https://ai.google.dev/gemini-api/docs/api-key?hl=th#cloud-console) แล้ว[ตั้งค่าสภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/api-key?hl=th#setup-environment)

ดูรายละเอียดเกี่ยวกับประเภทคีย์ ความปลอดภัย และวิธีกำหนดค่าคีย์ใน Python, JavaScript และภาษาอื่นๆ ได้ที่หัวข้อ[การใช้คีย์ Gemini API](https://ai.google.dev/gemini-api/docs/api-key?hl=th)

## เริ่มต้นใช้งาน

ตัวอย่างต่อไปนี้จะค้นหาวัตถุในรูปภาพและแสดงผลพิกัดและป้ายกำกับ 2 มิติที่ปรับมาตรฐานแล้ว คุณสามารถส่งเอาต์พุตนี้ไปยัง API หุ่นยนต์หรือโมเดล VLA โดยตรงเพื่อสร้างการทำงานของหุ่นยนต์

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
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

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
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
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

เอาต์พุตจะเป็นอาร์เรย์ JSON ที่มีออบเจ็กต์ โดยแต่ละออบเจ็กต์จะมี `point` (พิกัด `[y, x]` ที่ปรับมาตรฐานแล้ว) และ `label` ที่ระบุออบเจ็กต์

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

รูปภาพต่อไปนี้เป็นตัวอย่างวิธีแสดงคะแนนเหล่านี้

![ตัวอย่างที่แสดงจุดของวัตถุในรูปภาพ](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=th)

## วิธีการทำงาน

Gemini Robotics ER รับอินพุตรูปภาพ วิดีโอ หรือเสียงด้วยพรอมต์ภาษาธรรมชาติ โดยจะระบุวัตถุ พิจารณาบริบทของฉากและความสัมพันธ์เชิงพื้นที่ และแสดงผลลัพธ์ที่มีโครงสร้าง เช่น พิกัดหรือกรอบล้อมรอบ

Gemini Robotics ER ยังเป็นแบบ Agentic ด้วย โดยจะแบ่งงานที่ซับซ้อนออกเป็นงานย่อยๆ และดำเนินการโดยเรียกใช้ฟังก์ชันหุ่นยนต์หรือเรียกใช้โค้ดที่สร้างขึ้น ตัวอย่างเช่น "วางแอปเปิลลงในชาม" จะกลายเป็นลำดับขั้นตอนการค้นหา การหยิบ และการวาง

ดูรายละเอียดเกี่ยวกับวิธีที่ Gemini เรียกใช้เครื่องมือได้ที่[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=th#how-it-works)

## ความปลอดภัย

แม้ว่า Gemini Robotics ER จะสร้างขึ้นโดยคำนึงถึงความปลอดภัย แต่คุณก็มีหน้าที่รับผิดชอบในการรักษาสภาพแวดล้อมที่ปลอดภัยรอบๆ หุ่นยนต์ โมเดล Generative AI อาจทำงานผิดพลาดได้ และหุ่นยนต์จริงอาจก่อให้เกิดความเสียหาย ดูข้อมูลเพิ่มเติมได้ที่[หน้าความปลอดภัยของ Gemini Robotics](https://deepmind.google/models/gemini-robotics/safety?hl=th)

## แนวทางปฏิบัติแนะนำ

1. ใช้ภาษาธรรมชาติที่เรียบง่าย อธิบายสิ่งที่คุณต้องการให้หุ่นยนต์ทำเหมือนกับที่คุณอธิบายให้คนฟัง หากคำใดใช้ไม่ได้ผล ให้ลองใช้คำพ้องความหมายที่ใช้กันทั่วไป
2. เพิ่มประสิทธิภาพอินพุตภาพ ครอบตัดหรือซูมวัตถุขนาดเล็กหรือไม่ชัดเจนก่อนส่งรูปภาพ แสงและคอนทราสต์ของสีที่ต่ำอาจส่งผลต่อการตรวจจับ
3. แบ่งงานที่ซับซ้อนออกเป็นขั้นตอนต่างๆ ส่งแต่ละขั้นตอนเป็นพรอมต์แยกกันเพื่อให้โมเดลโฟกัสและปรับปรุงความแม่นยำ
4. ค้นหาหลายครั้งและหาค่าเฉลี่ยของผลลัพธ์สำหรับงานที่ต้องการความแม่นยำสูง วิธีการที่ใช้ฉันทามตินี้จะช่วยลดความแปรปรวนของเอาต์พุตเชิงพื้นที่

## ข้อจำกัด

โปรดคำนึงถึงข้อจำกัดต่อไปนี้เมื่อพัฒนาด้วย Gemini Robotics ER

- **ข้อจำกัดของคีย์ API:** Gemini API ไม่ยอมรับคำขอจากคีย์ API ที่ไม่จำกัด และจะแสดงข้อผิดพลาด `403 Forbidden` รักษาความปลอดภัยของคีย์ API โดยเพิ่มข้อจำกัดใน [AI Studio](https://aistudio.google.com/api-keys?hl=th)
  ดูรายละเอียดได้ที่[รักษาความปลอดภัยคีย์ API ที่ไม่มีการจำกัด](https://ai.google.dev/gemini-api/docs/api-key?hl=th#secure-unrestricted-keys)
- **เวลาในการตอบสนองเทียบกับประสิทธิภาพ:** คำถามที่ซับซ้อน ข้อมูลที่ป้อนที่มีความละเอียดสูง หรือระดับการคิดที่สูงอาจทำให้ใช้เวลาประมวลผลนานขึ้น สำหรับระดับการคิด
  ให้ใช้ระดับปานกลางเพื่อความสมดุลที่ดีระหว่างเวลาในการตอบสนองและประสิทธิภาพ
- **อาการหลอน:** โมเดล ER ของ Gemini Robotics อาจ "หลอน" หรือให้ข้อมูลที่ไม่ถูกต้องเป็นครั้งคราว เช่นเดียวกับโมเดลภาษาขนาดใหญ่ทั้งหมด โดยเฉพาะอย่างยิ่งสำหรับพรอมต์ที่กำกวมหรืออินพุตที่อยู่นอกการกระจาย
- **ขึ้นอยู่กับคุณภาพของพรอมต์:** คุณภาพของเอาต์พุตจะขึ้นอยู่กับความชัดเจนของพรอมต์ที่ป้อน ใช้พรอมต์ที่เฉพาะเจาะจงและมีโครงสร้างที่ดี
- **ต้นทุนการประมวลผล:** การเรียกใช้โมเดล โดยเฉพาะอย่างยิ่งเมื่อมีอินพุตวิดีโอหรือ `thinking_budget` สูง จะใช้ทรัพยากรการประมวลผลและทำให้เกิดค่าใช้จ่าย
  ดูรายละเอียดเพิ่มเติมได้ที่หน้า[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
- **ประเภทอินพุต:** ดูรายละเอียดเกี่ยวกับข้อจำกัดของแต่ละโหมดได้ในหัวข้อต่อไปนี้
  - [อินพุตรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th#technical-details-image)
  - [อินพุตวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#supported-formats)
  - [อินพุตเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th#supported-formats)

## ประกาศเกี่ยวกับนโยบายความเป็นส่วนตัว

คุณรับทราบว่าโมเดลที่อ้างอิงในเอกสารนี้ ("โมเดลหุ่นยนต์") ใช้ประโยชน์จากข้อมูลวิดีโอและเสียงเพื่อใช้งานและเคลื่อนย้ายฮาร์ดแวร์ตามวิธีการของคุณ ดังนั้น คุณจึงอาจใช้งานโมเดลหุ่นยนต์ในลักษณะที่โมเดลหุ่นยนต์จะเก็บรวบรวมข้อมูลจากบุคคลที่ระบุตัวตนได้ เช่น ข้อมูลเสียง ภาพ และรูปลักษณ์ ("ข้อมูลส่วนตัว") หากคุณเลือกที่จะใช้งานโมเดลหุ่นยนต์ในลักษณะที่รวบรวมข้อมูลส่วนตัว คุณตกลงว่าจะไม่อนุญาตให้บุคคลที่ระบุตัวตนได้โต้ตอบกับโมเดลหุ่นยนต์หรืออยู่ในบริเวณรอบๆ โมเดลหุ่นยนต์ เว้นแต่และจนกว่าบุคคลที่ระบุตัวตนได้ดังกล่าวจะได้รับแจ้งอย่างเพียงพอและยินยอมให้ Google ได้รับและใช้ข้อมูลส่วนตัวของตนตามที่ระบุไว้ในข้อกำหนดในการให้บริการเพิ่มเติมของ Gemini API ที่ [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=th) ("ข้อกำหนด") รวมถึงเป็นไปตามส่วนที่ชื่อว่า "วิธีที่ Google ใช้ข้อมูลของคุณ" คุณจะตรวจสอบว่าประกาศดังกล่าวอนุญาตให้มีการเก็บรวบรวมและใช้ข้อมูลส่วนตัวตามที่ระบุไว้ในข้อกำหนด และคุณจะใช้ความพยายามที่สมเหตุสมผลในเชิงพาณิชย์เพื่อลดการเก็บรวบรวมและการเผยแพร่ข้อมูลส่วนตัวโดยใช้เทคนิคต่างๆ เช่น การเบลอใบหน้าและการใช้งานโมเดลหุ่นยนต์ในพื้นที่ที่ไม่มีบุคคลที่ระบุตัวตนได้เท่าที่ทำได้

## ราคา

ดูข้อมูลโดยละเอียดเกี่ยวกับราคาและภูมิภาคที่พร้อมให้บริการได้ที่หน้า[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## ปลายทางของโมเดล

### Gemini Robotics ER 2 เวอร์ชันตัวอย่าง

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| id\_cardรหัสรุ่น | `gemini-robotics-er-2-preview` |
| saveประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำได้  **[กำลังคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำได้  **[Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่าน[รูปแบบเวอร์ชันโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)เพื่อดูรายละเอียดเพิ่มเติม  - ตัวอย่าง: `gemini-robotics-er-2-preview` |
| calendar\_monthอัปเดตล่าสุด | กรกฎาคม 2569 |
| id\_cardModel card | [การ์ดโมเดล](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=th) |

### Gemini Robotics ER 2 Streaming Preview

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| id\_cardรหัสรุ่น | `gemini-robotics-er-2-streaming-preview` |
| saveประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำไม่ได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำไม่ได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำไม่ได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำไม่ได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำไม่ได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำไม่ได้  **[กำลังคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำไม่ได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำไม่ได้  **[Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่าน[รูปแบบเวอร์ชันโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)เพื่อดูรายละเอียดเพิ่มเติม  - ตัวอย่าง: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthอัปเดตล่าสุด | กรกฎาคม 2569 |
| id\_cardModel card | [การ์ดโมเดล](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=th) |

### Gemini Robotics ER 1.6 เวอร์ชันตัวอย่าง

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| id\_cardรหัสรุ่น | `gemini-robotics-er-1.6-preview` |
| saveประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำได้  **[กำลังคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำได้  **[Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่าน[รูปแบบเวอร์ชันโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)เพื่อดูรายละเอียดเพิ่มเติม  - ปิด: `gemini-robotics-er-1.6-preview` |
| calendar\_monthอัปเดตล่าสุด | ธันวาคม 2025 |
| cognition\_2การตัดข้อมูล | มกราคม 2025 |

## ขั้นตอนถัดไป

- [การให้เหตุผลเชิงพื้นที่](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=th) — การชี้ การติดตาม กรอบล้อมรอบ วิถี
- [ความสามารถด้าน Agentic AI](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=th) — การเรียกใช้โค้ด การอ่านเครื่องมือวัด คำอธิบายประกอบรูปภาพ
- [การเรียบเรียงงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) — งานระยะยาวที่มี API หุ่นยนต์ที่กำหนดเอง
- [วิทยาการหุ่นยนต์พร้อมการสตรีม](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) - การสตรีมแบบ 2 ทิศทางแบบเรียลไทม์ (Gemini Robotics ER 2 เท่านั้น)
- [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) - การค้นหาช่วงเวลาและการจัดประเภทความคืบหน้า (Gemini Robotics ER 2 เท่านั้น)
- [ความปลอดภัยของ Gemini Robotics](https://deepmind.google/models/gemini-robotics/safety?hl=th) — การวิจัยด้านความปลอดภัยเบื้องหลังโมเดลตระกูลนี้

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-21 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-21 UTC"],[],[]]
