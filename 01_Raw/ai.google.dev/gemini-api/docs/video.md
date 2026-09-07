---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=th
fetched_at: 2026-09-07T05:37:38.402532+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e27\u0e34\u0e14\u0e35\u0e42\u0e2d\u0e43\u0e19 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้างวิดีโอใน Gemini API

Gemini API มีโมเดล 2 แบบสำหรับสร้างวิดีโอ ได้แก่
[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=th) และ [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=th)
ซึ่งแต่ละแบบได้รับการออกแบบมาสำหรับเวิร์กโฟลว์ที่แตกต่างกัน

ใช้ Gemini Omni Flash เป็นโมเดลเริ่มต้นสำหรับการสร้างวิดีโอ เนื่องจากมีความสอดคล้องของวิดีโอที่เหนือกว่า การให้เหตุผลแบบหลายอินพุต (รองรับอินพุตข้อความ รูปภาพ เสียง และวิดีโอพร้อมกัน) ความสอดคล้องของตัวละคร ความถูกต้องของข้อเท็จจริง และการตัดต่อแบบสนทนาหลายรอบ (เช่น การแทนที่องค์ประกอบหรือการเปลี่ยนมุมมอง) ใช้ Veo 3.1 สำหรับความสามารถเฉพาะ เช่น การขยายฉาก การควบคุมเฟรมสุดท้าย หรือการผสานรวมกับไปป์ไลน์เดิม

## Gemini Omni Flash

Gemini Omni Flash เป็นโมเดลมัลติโมดัลที่รวดเร็วสำหรับการสร้างวิดีโอและการตัดต่อวิดีโอแบบสนทนา มีความโดดเด่นในการเปลี่ยนพรอมต์ข้อความและรูปภาพให้เป็นวิดีโอสั้นๆ ได้อย่างรวดเร็ว และช่วยให้คุณปรับแต่งผลลัพธ์ได้หลายรอบโดยใช้ Interactions API

[เริ่มต้นใช้งาน Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=th)

## Veo 3.1

Veo 3.1 เป็นโมเดลสำหรับการสร้างวิดีโอพร้อมเสียงดั้งเดิม รองรับฟีเจอร์ต่างๆ เช่น การขยายวิดีโอ การสร้างเฉพาะเฟรม และการกำหนดทิศทางตามรูปภาพผ่าน `generateContent` API

[เริ่มต้นใช้งาน Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=th)

## การทำความเข้าใจวิดีโอ

หากต้องการนำเข้าและวิเคราะห์เนื้อหาวิดีโอที่มีอยู่แทนที่จะสร้าง
วิดีโอใหม่ โปรดดู[คู่มือการทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-30 UTC"],[],[]]
