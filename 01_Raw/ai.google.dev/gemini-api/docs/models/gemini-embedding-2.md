---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2?hl=th
fetched_at: 2026-08-17T02:31:45.187281+00:00
title: "\u0e42\u0e21\u0e40\u0e14\u0e25 Gemini Embedding 2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# โมเดล Gemini Embedding 2

โมเดลการฝังแบบหลายรูปแบบตัวแรกของเรา ซึ่งให้การแมปตัวเลขที่มีประสิทธิภาพของ
ข้อความ รูปภาพ วิดีโอ เสียง และ PDF ลงในพื้นที่การฝังแบบรวมเดียว โมเดล Gemini Embedding 2 เหมาะที่สุดสำหรับการค้นหาเชิงความหมายแบบข้ามโมดอล การดึงข้อมูลเอกสาร และระบบคำแนะนำที่ต้องมีการคำนวณความคล้ายคลึงที่รวดเร็วและปรับขนาดได้ในชุดข้อมูลมัลติโมดอลขนาดใหญ่

## เอกสารประกอบ

ไปที่หน้า[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)เพื่อดูฟีเจอร์และความสามารถทั้งหมด

## gemini-embedding-2

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | **Gemini API**  `gemini-embedding-2` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ, รูปภาพ, วิดีโอ, เสียง, PDF  **เอาต์พุต**  การฝังข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  8,192  **ขนาดมิติข้อมูลเอาต์พุต**  ยืดหยุ่น รองรับ: 128 - 3072, แนะนำ: 768, 1536, 3072 |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - เสถียร: `gemini-embedding-2` |
| calendar\_monthการอัปเดตล่าสุด | เมษายน 2026 |

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
