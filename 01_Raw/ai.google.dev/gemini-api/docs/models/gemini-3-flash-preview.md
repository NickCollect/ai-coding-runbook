---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th
fetched_at: 2026-11-02T07:10:02.306338+00:00
title: "\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 Gemini 3 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ตัวอย่าง Gemini 3 Flash

โมเดลที่ดีที่สุดในโลกสำหรับการทำความเข้าใจข้อมูลหลายรูปแบบ และโมเดลแบบเป็น Agent และ Vibe Coding ที่ทรงพลังที่สุดของเราในปัจจุบัน โดยนำเสนอภาพที่สมบูรณ์ยิ่งขึ้นและการโต้ตอบที่ลึกซึ้งยิ่งขึ้น ทั้งหมดนี้สร้างขึ้นบนพื้นฐานของการให้เหตุผลที่ล้ำสมัย

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=th)

## เอกสารประกอบ

ไปที่หน้า[คู่มือนักพัฒนาซอฟต์แวร์ Gemini 3](https://ai.google.dev/gemini-api/docs/latest-model?hl=th) เพื่อดูข้อมูลฟีเจอร์และความสามารถทั้งหมด

## gemini-3-flash-preview

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| id\_cardรหัสโมเดล | `gemini-3-flash-preview` |
| saveประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง และ PDF  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  1,048,576  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำได้  **[กำลังคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำได้  **[Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำได้  **[การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำได้ |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ที่[รูปแบบเวอร์ชันโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - `Preview: gemini-3-flash-preview` |
| calendar\_monthข้อมูลอัปเดตล่าสุด | ธันวาคม 2025 |
| id\_cardModel card | [การ์ดโมเดล](https://deepmind.google/models/model-cards/gemini-3-flash/?hl=th) |
| paidPricing | [การกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3-flash-preview) |

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-29 UTC"],[],[]]
