---
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=th
fetched_at: 2026-05-25T05:25:06.405822+00:00
title: "\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e04\u0e25\u0e34\u0e1b Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ตัวอย่างคลิป Lyria 3

Lyria 3 Clip Preview เป็นโมเดลของ Google ที่ได้รับการเพิ่มประสิทธิภาพเพื่อสร้างคลิป
ดนตรีสั้นๆ ลูป และตัวอย่าง โดยจะสร้างเสียงสเตอริโอ 48kHz คุณภาพสูงความยาว 30 วินาที
จากพรอมต์ข้อความหรืออินพุตรูปภาพ

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=lyria-3-clip-preview&hl=th)

## เอกสารประกอบ

ไปที่คู่มือ[การสร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)เพื่อดูข้อมูลทั้งหมดเกี่ยวกับฟีเจอร์และความสามารถ

## lyria-3-clip-preview

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | `lyria-3-clip-preview` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความและรูปภาพ  **เอาต์พุต**  เสียง (MP3), ข้อความ (เนื้อเพลง) |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072 |
| handymanความสามารถ | **การสร้างเสียง**  สิ่งที่ทำได้  **Batch API**  สิ่งที่ทำไม่ได้  **การแคช**  สิ่งที่ทำไม่ได้  **การรันโค้ด**  สิ่งที่ทำไม่ได้  **ค้นหาไฟล์**  สิ่งที่ทำไม่ได้  **การเรียกใช้ฟังก์ชัน**  สิ่งที่ทำไม่ได้  **การเชื่อมต่อแหล่งข้อมูลกับ Google Maps**  สิ่งที่ทำไม่ได้  **การสร้างรูปภาพ**  สิ่งที่ทำไม่ได้  **Live API**  สิ่งที่ทำไม่ได้  **การเชื่อมต่อแหล่งข้อมูลของ Search**  สิ่งที่ทำไม่ได้  **เอาต์พุตที่มีโครงสร้าง**  สิ่งที่ทำไม่ได้  **การคิด**  สิ่งที่ทำไม่ได้  **บริบทของ URL**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - ตัวอย่าง: `lyria-3-clip-preview` - ตัวอย่าง: `lyria-3-pro-preview` |
| calendar\_monthการอัปเดตล่าสุด | มีนาคม 2026 |

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
