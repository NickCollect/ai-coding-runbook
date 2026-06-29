---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=th
fetched_at: 2026-06-29T05:28:27.139764+00:00
title: "\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e02\u0e2d\u0e07 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ภาพรวมของ Gemini Live API

Live API ช่วยให้การโต้ตอบด้วยเสียงและภาพกับ Gemini เป็นไปแบบเรียลไทม์และมีความหน่วงต่ำ โดยจะประมวลผลสตรีมเสียง รูปภาพ และข้อความอย่างต่อเนื่องเพื่อแสดงเสียงตอบกลับที่เหมือนมนุษย์ในทันที ซึ่งสร้างประสบการณ์การสนทนาที่เป็นธรรมชาติให้กับผู้ใช้

![ภาพรวม Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=th)

[ลองใช้ Live API ใน Google AI Studiomic](https://aistudio.google.com/live?hl=th)
[โคลนแอปตัวอย่างจาก GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[ใช้ทักษะของ Agent ในการเขียนโค้ดterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)

## กรณีการใช้งาน

คุณสามารถใช้ Live API เพื่อสร้าง Agent ที่ใช้เสียงแบบเรียลไทม์สำหรับอุตสาหกรรมต่างๆ ได้แก่

- **อีคอมเมิร์ซและการค้าปลีก:** ผู้ช่วยช็อปปิ้งที่ให้คำแนะนำที่ปรับให้เหมาะกับแต่ละบุคคลและ Agent ฝ่ายสนับสนุนที่แก้ไขปัญหาของลูกค้า
- **เกม:** ตัวละครที่ไม่ใช่ผู้เล่น (NPC) แบบอินเทอร์แอกทีฟ ผู้ช่วยในเกม และการแปลเนื้อหาในเกมแบบเรียลไทม์
- **อินเทอร์เฟซยุคใหม่:** ประสบการณ์ที่ใช้เสียงและวิดีโอได้ในหุ่นยนต์ แว่นตาอัจฉริยะ และยานพาหนะ
- **การดูแลสุขภาพ:** เพื่อนดูแลสุขภาพเพื่อสนับสนุนและให้ความรู้แก่ผู้ป่วย
- **บริการทางการเงิน:** ที่ปรึกษา AI สำหรับการจัดการความมั่งคั่งและคำแนะนำด้านการลงทุน
- **การศึกษา:** ครูฝึก AI และเพื่อนร่วมเรียนที่ให้คำแนะนำและข้อเสนอแนะที่ปรับให้เหมาะกับแต่ละบุคคล
- **การแปลและการแปลเป็นภาษาท้องถิ่น:** การแปลบทสนทนาแบบเรียลไทม์ที่มีความหน่วงต่ำ ซึ่งช่วยให้การสื่อสารหลายภาษาเป็นไปอย่างราบรื่น

## ฟีเจอร์หลัก

Live API มีชุดฟีเจอร์ที่ครอบคลุมสำหรับการสร้าง Agent ที่ใช้เสียงได้อย่างมีประสิทธิภาพ ดังนี้

- [**การรองรับหลายภาษา**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#supported-languages):
  สนทนาในภาษาที่รองรับ 70 ภาษา
- [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#interruptions):
  ผู้ใช้สามารถขัดจังหวะโมเดลได้ทุกเมื่อเพื่อการโต้ตอบที่ตอบสนอง
- [**การใช้เครื่องมือ**](https://ai.google.dev/gemini-api/docs/live-tools?hl=th):
  ผสานรวมเครื่องมือต่างๆ เช่น การเรียกใช้ฟังก์ชันและการค้นหาของ Google เพื่อการโต้ตอบแบบไดนามิก
- [**การถอดเสียง**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#audio-transcription):
  ให้ข้อความถอดเสียงทั้งข้อมูลจากผู้ใช้และเอาต์พุตโมเดล
- [**เสียงเชิงรุก**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#proactive-audio):
  ให้คุณควบคุมได้ว่าโมเดลจะตอบกลับเมื่อใดและในบริบทใด
- [**การสนทนาเชิงอารมณ์**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#affective-dialog):
  ปรับรูปแบบและน้ำเสียงในการตอบกลับให้ตรงกับคำพูดของผู้ใช้
- [**การแปลสด**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th):
  การแปลเสียงเป็นเสียงแบบเรียลไทม์ในภาษาต่างๆ มากกว่า 70 ภาษา

## ข้อกำหนดทางเทคนิค

ตารางต่อไปนี้แสดงข้อกำหนดทางเทคนิคของ Live API

| หมวดหมู่ | รายละเอียด |
| --- | --- |
| รูปแบบอินพุต | เสียง (เสียง PCM แบบดิบ 16 บิต, 16 kHz, little-endian), รูปภาพ (JPEG <= 1 FPS), ข้อความ |
| รูปแบบเอาต์พุต | เสียง (เสียง PCM แบบดิบ 16 บิต, 24 kHz, little-endian) |
| โปรโตคอล | การเชื่อมต่อ WebSocket แบบมีสถานะ (WSS) |

## เลือกวิธีการนำไปใช้งาน

เมื่อผสานรวมกับ Live API คุณจะต้องเลือกวิธีการนำไปใช้งานวิธีใดวิธีหนึ่งต่อไปนี้

- **เซิร์ฟเวอร์ต่อเซิร์ฟเวอร์**: แบ็กเอนด์ของคุณเชื่อมต่อกับ Live API โดยใช้
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) โดยปกติแล้ว ไคลเอ็นต์จะส่งข้อมูลสตรีม (เสียง วิดีโอ ข้อความ) ไปยังเซิร์ฟเวอร์ ซึ่งจะส่งต่อข้อมูลไปยัง Live API
- **ไคลเอ็นต์ต่อเซิร์ฟเวอร์**: โค้ดส่วนหน้าของคุณเชื่อมต่อกับ Live API โดยตรง
  โดยใช้ [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) เพื่อสตรีมข้อมูล โดยข้ามแบ็กเอนด์

## เริ่มต้นใช้งาน

เลือกคำแนะนำที่ตรงกับสภาพแวดล้อมในการพัฒนาซอฟต์แวร์ของคุณ

เซิร์ฟเวอร์ต่อเซิร์ฟเวอร์

### [บทแนะนำเกี่ยวกับ GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th)

เชื่อมต่อกับ Gemini Live API โดยใช้ GenAI SDK เพื่อสร้างแอปพลิเคชันมัลติโมดัลแบบเรียลไทม์ด้วยแบ็กเอนด์ Python

ไคลเอ็นต์ต่อเซิร์ฟเวอร์

### [บทแนะนำเกี่ยวกับ WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=th)

เชื่อมต่อกับ Gemini Live API โดยใช้ WebSocket เพื่อสร้างแอปพลิเคชันมัลติโมดัลแบบเรียลไทม์ด้วยส่วนหน้า JavaScript และโทเค็นชั่วคราว

ชุดเครื่องมือพัฒนา Agent

### [บทแนะนำเกี่ยวกับ ADK](https://google.github.io/adk-docs/streaming/)

สร้าง Agent และใช้การสตรีมชุดเครื่องมือพัฒนา Agent (ADK) เพื่อเปิดใช้การสื่อสารด้วยเสียงและวิดีโอ

## การผสานรวมพาร์ทเนอร์

คุณสามารถใช้
การผสานรวมของบุคคลที่สามที่รองรับ Gemini Live
API ผ่าน WebRTC หรือ WebSocket เพื่อเพิ่มประสิทธิภาพการพัฒนาแอปเสียงและวิดีโอแบบเรียลไทม์

[LiveKit

ใช้ Gemini Live API กับ LiveKit Agent](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

สร้างแชทบ็อต AI แบบเรียลไทม์โดยใช้ Gemini Live และ Pipecat](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam by Software Mansion

สร้างแอปพลิเคชันการสตรีมวิดีโอสดและเสียงด้วย Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agents by Stream

สร้างแอปพลิเคชัน AI ที่ใช้เสียงและวิดีโอแบบเรียลไทม์ด้วย Vision Agents](https://visionagents.ai/integrations/gemini)
[Voximplant

เชื่อมต่อการโทรขาเข้าและขาออกกับ Live API ด้วย Voximplant](https://voximplant.com/products/gemini-client)
[Agora

สร้างแอปพลิเคชัน AI สำหรับการสนทนาแบบเรียลไทม์ด้วย Agora](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

เริ่มต้นใช้งาน Gemini Live API โดยใช้ Firebase AI Logic](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-12 UTC"],[],[]]
