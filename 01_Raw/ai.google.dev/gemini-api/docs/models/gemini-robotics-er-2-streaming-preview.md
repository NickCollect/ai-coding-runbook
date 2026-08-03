---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=th
fetched_at: 2026-08-03T04:38:53.399511+00:00
title: "Gemini Robotics ER 2 Streaming Preview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Gemini Robotics ER 2 Streaming Preview

Gemini Robotics ER 2 Streaming เป็นโมเดลภาษาภาพ (VLM) สำหรับหุ่นยนต์
ที่ได้รับการเพิ่มประสิทธิภาพสำหรับการสตรีมข้อความแบบเรียลไทม์โดยใช้ Live API โดยรับอินพุตข้อความ รูปภาพ วิดีโอ และเสียง รวมถึงรองรับการสตรีมแบบ 2 ทางด้วยการเรียกใช้ฟังก์ชัน

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=th)

## เอกสารประกอบ

ไปที่หน้า [Live API สำหรับหุ่นยนต์](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th)เพื่อดู
ความครอบคลุมของฟีเจอร์และความสามารถทั้งหมด

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 (เวอร์ชันตัวอย่าง)

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | `gemini-robotics-er-2-preview` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำได้  **[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบทของ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำได้  **[การอนุมานแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานตามลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - ตัวอย่าง: `gemini-robotics-er-2-preview` |
| calendar\_monthการอัปเดตล่าสุด | กรกฎาคม 2026 |
| id\_cardการ์ดโมเดล | [การ์ดโมเดล](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=th) |

### Gemini Robotics ER 2 Streaming Preview

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | `gemini-robotics-er-2-streaming-preview` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำไม่ได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำไม่ได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำไม่ได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำไม่ได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำไม่ได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำไม่ได้  **[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบทของ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำไม่ได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานตามลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - ตัวอย่าง: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthการอัปเดตล่าสุด | กรกฎาคม 2026 |
| id\_cardการ์ดโมเดล | [การ์ดโมเดล](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=th) |

### Gemini Robotics ER 1.6 (เวอร์ชันตัวอย่าง)

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | `gemini-robotics-er-1.6-preview` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  131,072  **ขีดจำกัดโทเค็นเอาต์พุต**  65,536 |
| handymanความสามารถ | **[การสร้างเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**  สิ่งที่ทำได้  **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**  สิ่งที่ทำได้  **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**  สิ่งที่ทำได้  **[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**  สิ่งที่ทำได้  **[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**  สิ่งที่ทำได้  **[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)**  สิ่งที่ทำไม่ได้  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)**  สิ่งที่ทำไม่ได้  **[การเชื่อมต่อแหล่งข้อมูลของ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)**  สิ่งที่ทำได้  **[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)**  สิ่งที่ทำได้  **[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)**  สิ่งที่ทำได้  **[บริบทของ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**  สิ่งที่ทำได้ |
| speedตัวเลือกการรับชม | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**  สิ่งที่ทำได้  **[การอนุมานแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)**  สิ่งที่ทำไม่ได้  **[การอนุมานตามลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)**  สิ่งที่ทำไม่ได้ |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - ตัวอย่าง: `gemini-robotics-er-1.6-preview` |
| calendar\_monthการอัปเดตล่าสุด | ธันวาคม 2025 |
| cognition\_2การตัดข้อมูล | มกราคม 2025 |

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
