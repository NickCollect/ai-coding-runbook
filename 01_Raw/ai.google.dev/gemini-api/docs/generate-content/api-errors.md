---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=th
fetched_at: 2026-08-31T06:43:02.378530+00:00
title: "\u0e02\u0e49\u0e2d\u0e1c\u0e34\u0e14\u0e1e\u0e25\u0e32\u0e14\u0e02\u0e2d\u0e07 API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ข้อผิดพลาดของ API

หน้านี้แสดงข้อมูลอ้างอิงสำหรับรหัสข้อผิดพลาดของแบ็กเอนด์ที่ API `GenerateContent` แสดงผล อธิบายรูปแบบการตอบกลับข้อผิดพลาดของ gRPC และระบุขั้นตอนการแก้ปัญหา

## รหัสข้อผิดพลาด HTTP

ตารางต่อไปนี้แสดงรหัสข้อผิดพลาดของแบ็กเอนด์ที่พบบ่อย คำอธิบายสาเหตุ และวิธีแก้ปัญหาที่แนะนำ

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **รหัส HTTP** | **สถานะ** | **คำอธิบาย** | **ตัวอย่าง** | **Solution** |
| 400 | INVALID\_ARGUMENT | เนื้อหาของคำขอมีรูปแบบไม่ถูกต้อง | คำขอของคุณมีการพิมพ์ผิดหรือไม่มีข้อมูลในช่องที่ต้องกรอก | ตรวจสอบ[เอกสารอ้างอิง API](https://ai.google.dev/api?hl=th) เพื่อดูรูปแบบคำขอ ตัวอย่าง และเวอร์ชันที่รองรับ การใช้ฟีเจอร์จาก API เวอร์ชันใหม่กว่ากับปลายทางเวอร์ชันเก่าอาจทำให้เกิดข้อผิดพลาด |
| 400 | FAILED\_PRECONDITION | Gemini API ระดับฟรีไม่พร้อมให้บริการในประเทศของคุณ โปรดเปิดใช้การเรียกเก็บเงินในโปรเจ็กต์ของคุณใน Google AI Studio | คุณส่งคำขอในภูมิภาคที่ไม่รองรับระดับฟรี และคุณไม่ได้เปิดใช้การเรียกเก็บเงินในโปรเจ็กต์ของคุณใน Google AI Studio | หากต้องการใช้ Gemini API คุณจะต้องตั้งค่าแพ็กเกจแบบชำระเงินโดยใช้ [Google AI Studio](https://aistudio.google.com/apikey?hl=th) |
| 403 | PERMISSION\_DENIED | คีย์ API ของคุณไม่มีสิทธิ์ที่จำเป็น | คุณใช้คีย์ API ที่ไม่ถูกต้อง หรือพยายามใช้โมเดลที่ปรับแต่งแล้วโดยไม่ได้ผ่านการตรวจสอบสิทธิ์ที่[เหมาะสม](https://ai.google.dev/gemini-api/docs/model-tuning?hl=th) | ตรวจสอบว่าได้ตั้งค่าคีย์ API และคีย์ API มีสิทธิ์เข้าถึงที่ถูกต้อง และตรวจสอบว่าได้ผ่านการตรวจสอบสิทธิ์ที่เหมาะสมเพื่อใช้โมเดลที่ปรับแต่งแล้ว |
| 404 | NOT\_FOUND | ไม่พบทรัพยากรที่ขอ | ไม่พบไฟล์รูปภาพ เสียง หรือวิดีโอที่อ้างอิงในคำขอ | ตรวจสอบว่าพารามิเตอร์ทั้งหมดในคำขอใช้ได้กับ API เวอร์ชันของคุณ |
| 429 | RESOURCE\_EXHAUSTED | คุณใช้เกินขีดจำกัดอัตราอย่างน้อย 1 รายการของ API (RPM, TPM, RPD, ค่าใช้จ่าย ฯลฯ) | คุณส่งคำขอมากเกินไป ใช้โทเค็นมากเกินไป หรือใช้เกินขีดจำกัดตามค่าใช้จ่ายสำหรับประวัติการเรียกเก็บเงินและระดับของบัญชี | ตรวจสอบว่าคุณอยู่ภายใน[ขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)ของโมเดล รอสักครู่แล้วลองอีกครั้ง ลดอัตราหรือขนาดของคำขอ [ขอเพิ่มขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th#request-rate-limit-increase) หากจำเป็น |
| 499 | CANCELLED | การดำเนินการถูกยกเลิก ซึ่งโดยปกติแล้วจะเป็นผู้เรียก | ไคลเอ็นต์ปิดการเชื่อมต่อก่อนที่ API จะตอบกลับเสร็จ | ตรวจสอบว่าโครงสร้างพื้นฐานของไคลเอ็นต์หรือเครือข่ายปิดการเชื่อมต่อก่อนเวลาอันควร (เช่น เนื่องจากไทม์เอาต์ฝั่งไคลเอ็นต์) |
| 500 | ภายใน | เกิดข้อผิดพลาดที่ไม่คาดคิดจากทางฝั่ง Google | บริบทอินพุตยาวเกินไป | ตรวจสอบ[หน้าสถานะ Gemini API](https://aistudio.google.com/status?hl=th) เพื่อดูเหตุการณ์ที่เกิดขึ้น ลดบริบทอินพุตหรือเปลี่ยนไปใช้โมเดลอื่นชั่วคราว (เช่น จาก Gemini 2.5 Pro เป็น Gemini 2.5 Flash) แล้วดูว่าได้ผลหรือไม่ หรือรอสักครู่แล้วลองส่งคำขออีกครั้ง หากปัญหายังคงอยู่หลังจากลองอีกครั้ง โปรดรายงานปัญหาโดยใช้ปุ่ม**ส่งความคิดเห็น** ใน Google AI Studio |
| 503 | UNAVAILABLE | บริการอาจทำงานหนักเกินไปหรือหยุดทำงานชั่วคราว | บริการมีขีดความสามารถไม่เพียงพอชั่วคราว | ตรวจสอบ[หน้าสถานะ Gemini API](https://aistudio.google.com/status?hl=th) เพื่อดูเหตุการณ์ที่เกิดขึ้น เปลี่ยนไปใช้โมเดลอื่นชั่วคราว (เช่น จาก Gemini 2.5 Pro เป็น Gemini 2.5 Flash) แล้วดูว่าได้ผลหรือไม่ หรือรอสักครู่แล้วลองส่งคำขออีกครั้ง หากปัญหายังคงอยู่หลังจากลองอีกครั้ง โปรดรายงานปัญหาโดยใช้ปุ่ม**ส่งความคิดเห็น** ใน Google AI Studio |
| 504 | DEADLINE\_EXCEEDED | บริการไม่สามารถประมวลผลให้เสร็จสิ้นภายในกำหนดเวลา | พรอมต์ (หรือบริบท) มีขนาดใหญ่เกินกว่าจะประมวลผลได้ทันเวลา | ตั้งค่า "ไทม์เอาต์" ที่ใหญ่ขึ้นในคำขอของไคลเอ็นต์เพื่อหลีกเลี่ยงข้อผิดพลาดนี้ |

## รูปแบบการตอบกลับข้อผิดพลาด

เมื่อคำขอ `GenerateContent` ล้มเหลว API จะตั้งค่ารหัสสถานะ HTTP (เช่น `400 Bad Request`, `403 Forbidden` หรือ `429 Too Many Requests`) และแสดงผลเนื้อหาการตอบกลับ JSON ที่มีรายละเอียดสถานะ gRPC ดังนี้

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `code` | จำนวนเต็ม | รหัสสถานะ HTTP |
| `message` | สตริง | คำอธิบายข้อผิดพลาดที่มนุษย์อ่านได้ |
| `status` | สตริง | รหัสสถานะ gRPC ใน `SCREAMING_CASE` |
| `details` | อาร์เรย์ | บริบทข้อผิดพลาดเพิ่มเติม เช่น `ErrorInfo` หรือ `LocalizedMessage` |

## ขั้นตอนถัดไป

- [การแก้ปัญหา API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=th): แก้ปัญหาและสถานการณ์ข้อผิดพลาดที่พบบ่อย
- [ขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th): ดูข้อมูลเกี่ยวกับขีดจำกัดคำขอและการจัดการโควต้า

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
