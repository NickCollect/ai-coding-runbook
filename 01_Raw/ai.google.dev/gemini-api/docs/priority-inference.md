---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=th
fetched_at: 2026-05-05T19:45:06.872990+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e19\u0e38\u0e21\u0e32\u0e19\u0e15\u0e32\u0e21\u0e25\u0e33\u0e14\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e33\u0e04\u0e31\u0e0d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอนุมานตามลำดับความสำคัญ

Gemini Priority API เป็นระดับการอนุมานแบบพรีเมียมที่ออกแบบมาสำหรับภาระงานที่สำคัญต่อธุรกิจซึ่งต้องมีเวลาในการตอบสนองที่ต่ำกว่าและความน่าเชื่อถือสูงสุดในราคาพรีเมียม การเข้าชมระดับ Priority จะมีความสำคัญเหนือกว่า
การเข้าชม API มาตรฐานและการเข้าชมระดับ Flex

การอนุมานตามลำดับความสำคัญพร้อมให้บริการแก่ผู้ใช้[ระดับ 2 และระดับ 3](https://ai.google.dev/gemini-api/docs/billing?hl=th#about-billing) ในปลายทาง GenerateContent API และ Interactions API

## วิธีใช้รายการสำคัญ

หากต้องการใช้ระดับลำดับความสำคัญ ให้ตั้งค่าฟิลด์ `service_tier` ในส่วนเนื้อหาของคำขอเป็น
`priority` ระดับเริ่มต้นคือมาตรฐานหากไม่ระบุฟิลด์

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3-flash-preview",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
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
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## วิธีการทำงานของการอนุมานตามลำดับความสำคัญ

เส้นทางการอนุมานที่มีลำดับความสำคัญจะส่งคำขอไปยังคิวการประมวลผลที่มีความสำคัญสูง ซึ่งให้ประสิทธิภาพที่รวดเร็วและคาดการณ์ได้สำหรับแอปพลิเคชันที่แสดงต่อผู้ใช้ กลไกหลักของฟีเจอร์นี้คือการลดระดับฝั่งเซิร์ฟเวอร์อย่างเหมาะสมเป็นการประมวลผลมาตรฐานสำหรับการรับส่งข้อมูลที่เกินขีดจำกัดแบบไดนามิก เพื่อให้มั่นใจว่าแอปพลิเคชันจะมีความเสถียรแทนที่จะทำให้คำขอไม่สำเร็จ

| ฟีเจอร์ | ลำดับความสำคัญ | มาตรฐาน | พับ | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | มากกว่ารุ่น Standard 75-100% | ตั๋วราคาเต็ม | ส่วนลด 50% | ส่วนลด 50% |
| **เวลาในการตอบสนอง** | วินาที | วินาทีถึงนาที | นาที (เป้าหมาย 1-15 นาที) | สูงสุด 24 ชั่วโมง |
| **ความน่าเชื่อถือ** | สูง (ไม่หลุดร่วง) | สูง / สูงปานกลาง | ดีที่สุดเท่าที่ทำได้ (ลดภาระได้) | สูง (สำหรับปริมาณงาน) |
| **อินเทอร์เฟซ** | พร้อมกัน | พร้อมกัน | พร้อมกัน | อะซิงโครนัส |

### ประโยชน์สำคัญ

- **เวลาในการตอบสนองต่ำ**: ออกแบบมาให้มีเวลาในการตอบสนองเป็นวินาทีสำหรับเครื่องมือ AI แบบอินเทอร์แอกทีฟที่ผู้ใช้ใช้งาน
- **ความน่าเชื่อถือสูง**: ระบบจะจัดการการเข้าชมด้วยความสำคัญสูงสุดและ
  ไม่สามารถทิ้งได้
- **การลดลงอย่างค่อยเป็นค่อยไป**: การรับส่งข้อมูลที่เพิ่มขึ้นเกินขีดจำกัดแบบไดนามิกจะลดระดับเป็นระดับ Standard โดยอัตโนมัติเพื่อประมวลผลแทนที่จะล้มเหลว ซึ่งจะป้องกันไม่ให้เกิดการหยุดทำงานของบริการ
- **ราบรื่น**: ใช้วิธีการ `generateContent` แบบซิงโครนัสเดียวกันกับแพ็กเกจมาตรฐานและแพ็กเกจ Flex

### กรณีการใช้งาน

การประมวลผลที่มีลำดับความสำคัญเหมาะสำหรับเวิร์กโฟลว์ที่สำคัญต่อธุรกิจซึ่งประสิทธิภาพ
และความน่าเชื่อถือเป็นสิ่งสำคัญที่สุด

- **แอปพลิเคชัน AI แบบอินเทอร์แอกทีฟ**: แชทบ็อตและโคไพลอตฝ่ายบริการลูกค้าที่ผู้ใช้
  จ่ายเงินในราคาพรีเมียมและคาดหวังการตอบกลับที่รวดเร็วและสม่ำเสมอ
- **เครื่องมือตัดสินใจแบบเรียลไทม์**: ระบบที่ต้องการผลลัพธ์ที่มีความน่าเชื่อถือสูงและมีความหน่วงต่ำ
  เช่น การจัดลำดับความสำคัญของคำขอแจ้งปัญหาแบบเรียลไทม์หรือการตรวจจับการประพฤติมิชอบ
- **ฟีเจอร์สำหรับลูกค้าพรีเมียม**: นักพัฒนาแอปที่ต้องการรับประกันเป้าหมายระดับการให้บริการ (SLO) ที่สูงขึ้นสำหรับลูกค้าที่ชำระเงิน

### ขีดจำกัดอัตรา

การใช้ทรัพยากรที่มีลำดับความสำคัญจะมีอัตราคำขอที่จำกัดของตัวเอง แม้ว่าระบบจะนับการใช้ทรัพยากร รวมกับ[อัตราคำขอที่จำกัดของการรับส่งข้อมูลแบบอินเทอร์แอกทีฟโดยรวม](https://aistudio.google.com/rate-limit?hl=th) ขีดจำกัดอัตราเริ่มต้นสำหรับการอนุมานตามลำดับความสำคัญคือ**ขีดจำกัดอัตรามาตรฐาน 0.3 เท่าสำหรับโมเดล / ระดับ**

### ตรรกะการดาวน์เกรดอย่างค่อยเป็นค่อยไป

หากคำขอเกินขีดจำกัดของลำดับความสำคัญเนื่องจากมีการใช้งานหนาแน่น ระบบจะ**ลดระดับคำขอที่เกินมาเป็นแบบมาตรฐานโดยอัตโนมัติและราบรื่น**แทนที่จะแสดงข้อผิดพลาด 503 หรือ 429 ระบบจะเรียกเก็บเงินสำหรับคำขอที่ลดระดับในอัตรามาตรฐาน ไม่ใช่ในอัตราพรีเมียมแบบมีลำดับความสำคัญ

### ความรับผิดชอบของลูกค้า

- **การตรวจสอบการตอบกลับ**: นักพัฒนาซอฟต์แวร์ควรตรวจสอบ`x-gemini-service-tier`ส่วนหัว`standard`ในการตอบกลับ API เพื่อตรวจหาว่ามีการลดระดับคำขอเป็น
  `standard`บ่อยหรือไม่
- **การลองใหม่**: ไคลเอ็นต์ต้องใช้ตรรกะการลองใหม่/Exponential Backoff สำหรับ
  ข้อผิดพลาดมาตรฐาน เช่น `DEADLINE_EXCEEDED`

## ราคา

การอนุมานที่มีลำดับความสำคัญมีราคาแพงกว่า [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th) 75-100% และจะเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

โมเดลต่อไปนี้รองรับการอนุมานแบบมีลำดับความสำคัญ

| รุ่น | การอนุมานตามลำดับความสำคัญ |
| --- | --- |
| [Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [ตัวอย่างรูปภาพ Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [รูปภาพ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

อ่านเกี่ยวกับตัวเลือก[การอนุมานและการเพิ่มประสิทธิภาพ](https://ai.google.dev/gemini-api/docs/optimization?hl=th)อื่นๆ ของ Gemini

- [การอนุมานแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)เพื่อลดต้นทุน 50%
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) สำหรับการประมวลผลแบบไม่พร้อมกันภายใน 24 ชั่วโมง
- [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)เพื่อลดต้นทุนโทเค็นอินพุต

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
