---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=th
fetched_at: 2026-10-12T07:06:29.721663+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e23\u0e39\u0e1b\u0e20\u0e32\u0e1e\u0e42\u0e14\u0e22\u0e43\u0e0a\u0e49 Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)

ส่งความคิดเห็น

# สร้างรูปภาพโดยใช้ Imagen

Imagen เป็นโมเดลการสร้างรูปภาพรุ่นเดิมของ Google ตอนนี้เราได้ปิดตัวลงแล้ว
และจะไม่พร้อมใช้งานใน Gemini API อีกต่อไป

## ย้ายไปใช้ Nano Banana

ย้ายข้อมูลไปยัง Nano Banana เพื่อสร้างรูปภาพ

- **ชื่อโมเดล**: ใช้ `gemini-2.5-flash-image` (หรือโมเดล Nano Banana 2 เช่น `gemini-3.1-flash-image`) แทนชื่อโมเดล Imagen
- **วิธีการ**: ใช้ `client.models.generate_content` แทน
  `client.models.generate_images`
- **การจัดการการตอบกลับ**: Nano Banana จะแสดงผลชิ้นส่วนเนื้อหาที่มีข้อมูลรูปภาพ
  แทนออบเจ็กต์การตอบกลับรูปภาพที่เฉพาะเจาะจง

ดูรายละเอียดและตัวอย่างได้ที่[คำแนะนำการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-18 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-18 UTC"],[],[]]
