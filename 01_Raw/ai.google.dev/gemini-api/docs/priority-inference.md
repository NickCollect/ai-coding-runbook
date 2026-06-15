---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=th
fetched_at: 2026-06-15T06:28:18.452089+00:00
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

Gemini Priority API เป็นระดับการอนุมานแบบพรีเมียมที่ออกแบบมาสำหรับภาระงานที่สำคัญต่อธุรกิจ ซึ่งต้องใช้เวลาในการตอบสนองที่ต่ำกว่าและความน่าเชื่อถือสูงสุดในราคาพรีเมียม การเข้าชมระดับพรีเมียมจะได้รับความสำคัญเหนือการเข้าชม API มาตรฐานและการเข้าชมระดับ Flex

การอนุมานแบบลำดับความสำคัญพร้อมให้บริการแก่ผู้ใช้[ระดับที่ 2 และระดับที่ 3](https://ai.google.dev/gemini-api/docs/billing?hl=th#about-billing) ในปลายทาง GenerateContent API
และ Interactions API

## วิธีใช้รายการสำคัญ

หากต้องการใช้ระดับ Priority ให้ตั้งค่าฟิลด์ `service_tier` ในเนื้อหาคำขอเป็น `priority` ระดับเริ่มต้นคือระดับมาตรฐานหากละเว้นฟิลด์นี้

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
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
          model: "gemini-3.5-flash",
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
        "gemini-3.5-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## วิธีการทำงานของการอนุมานแบบพรีเมียม

การอนุมานแบบลำดับความสำคัญจะกำหนดเส้นทางคำขอไปยังคิวการประมวลผลที่มีความสำคัญสูง ซึ่งให้ประสิทธิภาพที่รวดเร็วและคาดการณ์ได้สำหรับแอปพลิเคชันที่แสดงต่อผู้ใช้ กลไกหลักคือการลดระดับฝั่งเซิร์ฟเวอร์อย่างค่อยเป็นค่อยไปเป็นการประมวลผลมาตรฐานสำหรับการเข้าชมที่เกินขีดจำกัดแบบไดนามิก ซึ่งช่วยให้แอปพลิเคชันมีความเสถียรแทนที่จะทำให้คำขอไม่สำเร็จ

| ฟีเจอร์ | รายการสำคัญ | มาตรฐาน | Flex | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | มากกว่าระดับมาตรฐาน 75-100% | ราคาเต็ม | ส่วนลด 50% | ส่วนลด 50% |
| **เวลาในการตอบสนอง** | วินาที | วินาทีถึงนาที | นาที (เป้าหมาย 1-15 นาที) | สูงสุด 24 ชั่วโมง |
| **ความน่าเชื่อถือ** | สูง (ไม่สามารถลดระดับได้) | สูง / สูงปานกลาง | อย่างเต็มที่ (สามารถลดระดับได้) | สูง (สำหรับอัตราการส่งข้อมูล) |
| **อินเทอร์เฟซ** | แบบซิงโครนัส | แบบซิงโครนัส | แบบซิงโครนัส | แบบอะซิงโครนัส |

### สิทธิประโยชน์ที่สำคัญ

- **เวลาในการตอบสนองต่ำ**: ออกแบบมาให้ใช้เวลาตอบสนองเป็นวินาทีสำหรับเครื่องมือ AI แบบอินเทอร์แอกทีฟที่ผู้ใช้มองเห็น
- **ความน่าเชื่อถือสูง**: การเข้าชมจะได้รับการปฏิบัติด้วยความสำคัญสูงสุดและ
  ไม่สามารถลดระดับได้
- **การลดลงอย่างค่อยเป็นค่อยไป**: การเข้าชมที่เพิ่มขึ้นซึ่งเกินขีดจำกัดแบบไดนามิกจะ
  ลดระดับลงเป็นระดับมาตรฐานโดยอัตโนมัติเพื่อทำการประมวลผลแทนที่จะทำให้คำขอไม่สำเร็จ
  ซึ่งจะช่วยป้องกันไม่ให้เกิดการหยุดทำงานของบริการ
- **ความยุ่งยากต่ำ**: ใช้วิธี `generateContent` แบบซิงโครนัสแบบเดียวกับระดับ
  มาตรฐานและระดับ Flex

### กรณีการใช้งาน

การประมวลผลแบบพรีเมียมเหมาะอย่างยิ่งสำหรับเวิร์กโฟลว์ที่สำคัญต่อธุรกิจ ซึ่งประสิทธิภาพและความน่าเชื่อถือมีความสำคัญสูงสุด

- **แอปพลิเคชัน AI แบบอินเทอร์แอกทีฟ**: แชทบ็อตและผู้ช่วยเสมือนสำหรับฝ่ายบริการลูกค้าที่
  ผู้ใช้จ่ายเงินในราคาพรีเมียมและคาดหวังการตอบสนองที่รวดเร็วและสม่ำเสมอ
- **กลไกการตัดสินใจแบบเรียลไทม์**: ระบบที่ต้องใช้ผลลัพธ์ที่น่าเชื่อถือสูงและมีเวลาในการตอบสนองต่ำ
  เช่น การจัดลำดับความสำคัญของตั๋วแบบสดหรือการตรวจจับการฉ้อโกง
- **ฟีเจอร์สำหรับลูกค้าพรีเมียม**: นักพัฒนาแอปที่ต้องรับประกันวัตถุประสงค์ระดับการให้บริการ
  ที่สูงขึ้นสำหรับลูกค้าที่ชำระเงิน

### ขีดจำกัดอัตรา

การใช้งานระดับพรีเมียมจะมีขีดจำกัดอัตราของตัวเอง แม้ว่าการใช้งานจะนับรวมใน [ขีดจำกัดอัตราการรับส่งข้อมูลแบบอินเทอร์แอกทีฟโดยรวมก็ตาม](https://aistudio.google.com/rate-limit?hl=th) ขีดจำกัดอัตราเริ่มต้นสำหรับการอนุมานแบบพรีเมียมคือ**ขีดจำกัดอัตรามาตรฐาน 0.3 เท่าสำหรับโมเดล / ระดับ**

### ตรรกะการลดระดับอย่างค่อยเป็นค่อยไป

หากมีการใช้งานเกินขีดจำกัดระดับ Priority เนื่องจากความหนาแน่น คำขอที่ล้นจะ**ลดระดับลงเป็นการประมวลผล Standard โดยอัตโนมัติและอย่างค่อยเป็นค่อยไป** แทนที่จะทำให้คำขอไม่สำเร็จด้วยข้อผิดพลาด 503 หรือ 429 ระบบจะเรียกเก็บเงินสำหรับคำขอที่ลดระดับลงในอัตรามาตรฐาน ไม่ใช่อัตราพรีเมียมของระดับพรีเมียม

### ความรับผิดชอบของไคลเอ็นต์

- **การตรวจสอบการตอบสนอง**: นักพัฒนาแอปควรตรวจสอบส่วนหัว `x-gemini-service-tier`
  ในการตอบสนองของ API เพื่อตรวจหาว่าคำขอถูกลดระดับลงเป็น
  `standard` บ่อยหรือไม่
- **การลองใหม่**: ไคลเอ็นต์ต้องใช้ตรรกะการลองใหม่/Exponential Backoff สำหรับ
  ข้อผิดพลาดมาตรฐาน เช่น `DEADLINE_EXCEEDED`

## การกำหนดราคา

การอนุมานแบบพรีเมียมมีราคามากกว่า [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th) 75-100% และเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

โมเดลต่อไปนี้รองรับการอนุมานแบบลำดับความสำคัญ

| โมเดล | การอนุมานแบบลำดับความสำคัญ |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Pro เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3 Flash เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 3 Pro เวอร์ชันตัวอย่างรูปภาพ](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [รูปภาพ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

อ่านเกี่ยวกับตัวเลือก[การอนุมานและการเพิ่มประสิทธิภาพ](https://ai.google.dev/gemini-api/docs/optimization?hl=th)อื่นๆ ของ Gemini ได้ที่

- [การอนุมานแบบ Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th) เพื่อลดต้นทุน 50%
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) สำหรับการประมวลผลแบบอะซิงโครนัสภายใน 24 ชั่วโมง
- [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th) เพื่อลดต้นทุนโทเค็นอินพุต

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-28 UTC"],[],[]]
