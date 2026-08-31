---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=th
fetched_at: 2026-08-31T06:41:14.602879+00:00
title: "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e23\u0e38\u0e48\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บันทึกประจำรุ่น

หน้านี้มีบันทึกการอัปเดตของ Gemini API

## 21 กรกฎาคม 2026

- **Gemini 3.6 Flash และ Gemini 3.5 Flash-Lite พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA)**:
  เปิดตัวโมเดล 3.x Flash ล่าสุดเวอร์ชันที่เสถียรและพร้อมใช้งานจริง

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): มีประสิทธิภาพของโทเค็นที่ดียิ่งขึ้น รวมถึงความสามารถในการวางแผนโค้ด/เอเจนต์ในราคาที่ต่ำกว่า 3.5 Flash ซึ่งช่วยแก้ปัญหาที่นักพัฒนาซอฟต์แวร์แสดงความคิดเห็นเกี่ยวกับความละเอียดของเอาต์พุต
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): มีตัวเลือกเอเจนต์ย่อยที่มีเวลาในการตอบสนองต่ำและคุ้มค่าสูง ซึ่งออกแบบมาเพื่อการทำงานอัตโนมัติที่มีปริมาณมาก

  ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[โมเดล Gemini ล่าสุด](https://ai.google.dev/gemini-api/docs/latest-model?hl=th)
- **พารามิเตอร์ที่เลิกใช้งานแล้ว**: ตอนนี้พารามิเตอร์การสุ่มตัวอย่าง `temperature`, `top_p`
  และ `top_k` เลิกใช้งานแล้ว ดูรายละเอียดได้ที่[โมเดล Gemini ล่าสุด](https://ai.google.dev/gemini-api/docs/latest-model?hl=th#sampling-parameter-deprecation)

## 6 กรกฎาคม 2026

- การรองรับ[บันทึกของนักพัฒนาซอฟต์แวร์](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)สำหรับ
  Interactions API: ตอนนี้คุณดูบันทึกสำหรับการเรียก Interactions API ที่รองรับได้แล้ว
  ใน[แดชบอร์ด AI Studio](https://aistudio.google.com/logs?hl=th)

## 30 มิถุนายน 2026

- **Gemini Omni Flash ในเวอร์ชันตัวอย่างแบบสาธารณะ**: เปิดตัวเมื่อ`gemini-omni-flash-preview`
  โมเดลแบบหลายรูปแบบที่มีประสิทธิภาพสูงซึ่งออกแบบมาสำหรับการสร้างวิดีโอความเร็วสูง
  และการตัดต่อวิดีโอแบบสนทนา การใช้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
  คุณสามารถสร้างวิดีโอความยาว 3-10 วินาทีที่ความละเอียด 720p จากคำอธิบายข้อความหรือภาพเคลื่อนไหว
  จากนั้นแก้ไขและปรับแต่งเอาต์พุตแบบสนทนา หากต้องการเริ่มต้นใช้งาน โปรดดูคู่มือ [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=th) และการ์ดโมเดล [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=th)
- เปิดตัว `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) ให้พร้อมใช้งานทั่วไป (GA) ซึ่งเป็นโมเดลแบบหลายรูปแบบในตัวที่ได้รับการเพิ่มประสิทธิภาพเพื่อเวลาในการตอบสนองที่ต่ำมาก รวมถึงการสร้างและแก้ไขรูปภาพที่คุ้มค่า ดูการ์ดโมเดล[รูปภาพ Gemini 3.1
  Flash Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=th) และคู่มือ[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 24 มิถุนายน 2026

- **การใช้คอมพิวเตอร์**: เปิดตัวการรองรับเวอร์ชันตัวอย่างแบบสาธารณะสำหรับเครื่องมือ[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)ใน Gemini 3.5 Flash การเปิดตัวนี้ประกอบด้วยการดำเนินการที่ง่ายขึ้นด้วย Intent, การรองรับในตัวสำหรับสภาพแวดล้อมของเบราว์เซอร์ อุปกรณ์เคลื่อนที่ และเดสก์ท็อป, นโยบายความปลอดภัยที่กำหนดค่าได้ และการตรวจหาการแทรกพรอมต์ขั้นสูง

## 17 มิถุนายน 2026

- **การรองรับการสตรีมสำหรับการสร้างคำพูด**: ตอนนี้โมเดล `gemini-3.1-flash-tts-preview` รองรับการสตรีมผ่าน `streamGenerateContent`
  (และ `stream: true` ใน Interactions API) แล้ว ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[การอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#streaming)

## 15 มิถุนายน 2026

- **ประกาศการเลิกใช้งาน**: เราจะเลิกใช้งานโมเดลการสร้างรูปภาพต่อไปนี้และจะ[ปิด](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **17 สิงหาคม 2026**

  - **โมเดลรูปภาพ Imagen 4 และ Gemini 3**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    หากต้องการย้ายข้อมูลโค้ดไปยังปลายทางที่เสถียรหรือเวอร์ชันตัวอย่างที่ใหม่กว่า โปรดดูหน้า[การเลิกใช้งาน Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=th#imagen-models)
- **ประกาศการเลิกใช้งาน**: เราจะเลิกใช้งานโมเดลการสร้างวิดีโอต่อไปนี้และจะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **30 มิถุนายน 2026**

  - **โมเดล Veo**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    โปรดอัปเดตการผสานรวมเพื่อใช้รหัสโมเดลเวอร์ชันตัวอย่างของ Veo 3.1
    (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) หรือโมเดล 3.1 GA ที่พร้อมใช้งานผ่าน[แพลตฟอร์มเอเจนต์ Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=th)
    เพื่อหลีกเลี่ยงการหยุดชะงักของบริการ
- **ประกาศการหยุดให้บริการ**: เครื่องมือมุมมองตามบริบทของ GMP เวอร์ชันทดลอง (อินเทอร์เฟซแบบคงที่สำหรับการเชื่อมโยงกับเอาต์พุตของ Google Maps) จะ[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **15 มิถุนายน 2026**

## 1 มิถุนายน 2026

- ตอนนี้เราได้[ปิด](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)โมเดล Gemini 2.0 ต่อไปนี้แล้ว

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  โปรดใช้ [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) หรือ
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th)
  แทน

## 28 พฤษภาคม 2026

- เราได้เปิดตัว `gemini-3.1-flash-image` (Nano Banana 2) และ `gemini-3-pro-image`
  (Nano Banana Pro) ซึ่งเป็นโมเดลภาพเวอร์ชันพร้อมให้บริการแก่บุคคลทั่วไป (GA) ของเรา
  [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=th)
  และ [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=th)
- **รองรับการสร้างรูปภาพจากวิดีโอ**: ตอนนี้คุณสามารถส่งไฟล์วิดีโอ (ผ่านการอัปโหลดโดยตรงหรือเป็น URL ของ YouTube สาธารณะ) เป็นบริบทแบบมัลติโมดอลพร้อมกับพรอมต์ข้อความเพื่อสร้างภาพปกคุณภาพสูง โปสเตอร์ภาพยนตร์ที่สวยงาม หรืออินโฟกราฟิกสรุป ฟีเจอร์นี้รองรับเฉพาะในรุ่น `gemini-3.1-flash-image`
  ดูข้อมูลเพิ่มเติมได้ที่คำแนะนำเกี่ยวกับ[การสร้างรูปภาพจากวิดีโอ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#video-to-image)
- ประกาศการเลิกใช้งาน: เราเลิกใช้งานโมเดล `gemini-3.1-flash-image-preview` และ
  `gemini-3-pro-image-preview` แล้ว
  และจะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 25 มิถุนายน 2026

## 25 พฤษภาคม 2026

- โมเดล `gemini-3.1-flash-lite-preview` ได้[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว โปรดใช้
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) แทน

## 19 พฤษภาคม 2026

- เราได้เปิดตัว`gemini-3.5-flash`เวอร์ชันพร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) ของ
  [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th)
  ซึ่งเป็นโมเดลที่ชาญฉลาดที่สุดของเราสำหรับการทำงานที่ล้ำหน้าอย่างต่อเนื่องใน
  งานที่ต้องใช้เอเจนต์และงานเขียนโค้ด ตอนนี้โมเดลนี้อยู่เบื้องหลัง `gemini-flash-latest`
- เปิดตัว**เอเจนต์ที่ได้รับการจัดการใน Gemini API** ในเวอร์ชันตัวอย่างแบบสาธารณะ ซึ่งช่วยให้
  นักพัฒนาแอปสร้างและทําให้ Agent แบบมีสถานะที่ทํางานโดยอัตโนมัติใช้งานได้ใน
  สภาพแวดล้อมแซนด์บ็อกซ์ Linux ที่ปลอดภัยและแยกต่างหากซึ่งโฮสต์โดย Google ดูข้อมูลเพิ่มเติมได้ที่หน้า[ภาพรวมของเอเจนต์](https://ai.google.dev/gemini-api/docs/agents?hl=th)และ[การเริ่มต้นอย่างรวดเร็ว](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)
- เปิดตัว Agent ที่มีการจัดการ **Antigravity Agent** แบบอเนกประสงค์
  [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=th) ในเวอร์ชันตัวอย่างแบบสาธารณะ
  Agent ของ Antigravity สามารถวางแผน วิเคราะห์ เขียน และเรียกใช้โค้ด จัดการไฟล์ และท่องเว็บภายในคอนเทนเนอร์แซนด์บ็อกซ์ได้โดยอัตโนมัติ
  ดูตัวอย่างโค้ดและข้อกำหนดได้ในคู่มือ [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)

## 7 พฤษภาคม 2026

- เปิดตัว `gemini-3.1-flash-lite` เวอร์ชันพร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) ของ
  [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th)
  ซึ่งได้รับการเพิ่มประสิทธิภาพด้านความเร็ว ความสามารถในการปรับขนาด และความคุ้มค่า
- ประกาศการเลิกใช้งาน: เราจะเลิกใช้งานโมเดล `gemini-3.1-flash-lite-preview` ในวันที่ 11/5/26 และจะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 25 พฤษภาคม 2026

## 6 พฤษภาคม 2026

- **การเปลี่ยนแปลงที่ไม่รองรับการทำงานร่วมกับเวอร์ชันก่อนหน้าที่จะเกิดขึ้น**: สคีมาคำขอและการตอบกลับ (`outputs` → `steps`) และการกำหนดค่ารูปแบบเอาต์พุต (`response_format`) ของ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
  จะมีการเปลี่ยนแปลง โดยสคีมาใหม่จะกลายเป็นสคีมาเริ่มต้นในวันที่ **26 พฤษภาคม** และระบบจะนำสคีมาเดิมออกในวันที่ **8 มิถุนายน**
  ดูรายละเอียดได้จาก[คำแนะนำในการย้ายข้อมูล](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=th)

## 5 พฤษภาคม 2026

- อัปเดต**การค้นหาไฟล์**ให้รองรับการค้นหาหลายรูปแบบ ตอนนี้คุณสามารถฝังและค้นหารูปภาพโดยใช้โมเดล `gemini-embedding-2` ได้โดยตรง
  ตอนนี้การอ้างอิงข้อมูลเมตาจะมี `media_id` สำหรับการอ้างอิงภาพและ
  `page_numbers` ที่ระบุตำแหน่งของข้อมูล ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)

## 4 พฤษภาคม 2026

- เปิดตัวการรองรับ [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=th) ที่ขับเคลื่อนด้วยเหตุการณ์ใน Gemini API เพื่อแทนที่เวิร์กโฟลว์การสำรวจสำหรับ Batch API และการดำเนินการที่ใช้เวลานาน

## 30 เมษายน 2026

- โมเดล `gemini-robotics-er-1.5-preview` ได้[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว โปรดใช้
  [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=th) แทน

## 22 เมษายน 2026

- เปิดตัว `gemini-embedding-2` เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ดูข้อมูลเพิ่มเติมได้ที่หน้า[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

## 21 เมษายน 2026

- เปิดตัวเอเจนต์ [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)
  เวอร์ชันใหม่พร้อมการวางแผนร่วมกัน การรองรับการแสดงภาพ การผสานรวมเซิร์ฟเวอร์ MCP
  และการค้นหาไฟล์

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=th): ออกแบบมาเพื่อ
    ความเร็วและประสิทธิภาพ เหมาะสำหรับการสตรีมกลับไปยัง UI ของไคลเอ็นต์
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=th): ความครอบคลุมสูงสุด
    สำหรับการรวบรวมและสังเคราะห์บริบทอัตโนมัติ

## 15 เมษายน 2026

- เปิดตัว [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=th) ซึ่งเป็นโมเดลข้อความเป็นเสียงที่คุ้มค่า
  สื่ออารมณ์ และควบคุมได้ อ่านเอกสารประกอบ[ข้อความเป็นเสียงพูด](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)เพื่อดูข้อมูลเพิ่มเติม

## 14 เมษายน 2026

- เปิดตัว `gemini-robotics-er-1.6-preview` โมเดลหุ่นยนต์ที่อัปเดตแล้ว
  ตอนนี้โมเดลมีฟีเจอร์ใหม่ๆ เช่น การอ่านเครื่องมือ ความสามารถในการให้เหตุผลเชิงพื้นที่และเชิงกายภาพที่ได้รับการปรับปรุง ดูข้อมูลเพิ่มเติมได้ที่หน้า [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th) และ[บล็อก](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=th)
- ประกาศการเลิกใช้งาน: เราจะ`gemini-robotics-er-1.5-preview`โมเดล
  [ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 30 เมษายน 2026 เวลา 09:00 น.
  PST

## 2 เมษายน 2026

- เปิดตัว `gemma-4-26b-a4b-it` และ `gemma-4-31b-it` พร้อมให้บริการใน
  [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API
  ซึ่งเป็นส่วนหนึ่งของการเปิดตัว [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=th)

## 1 เมษายน 2026

- เปิดตัวระดับการอนุมาน [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th) และ[Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th) ใหม่ ซึ่งมีตัวเลือกเพิ่มเติม
  สำหรับการเพิ่มประสิทธิภาพต้นทุนหรือเวลาในการตอบสนอง

## 31 มีนาคม 2026

- เปิดตัวเวอร์ชันตัวอย่างของ Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=th) ซึ่งเป็นโมเดล[การสร้างวิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)ที่คุ้มค่าที่สุดของเรา ออกแบบมาเพื่อการทำซ้ำอย่างรวดเร็วและการสร้างแอปพลิเคชันที่มีปริมาณสูง
- เราได้ปิดโมเดล `gemini-2.5-flash-lite-preview-09-2025` แล้ว โปรดใช้
  [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th) แทน

## 26 มีนาคม 2026

- เปิดตัว [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=th) โมเดลเสียงต่อเสียง (A2A) ล่าสุดที่ออกแบบมาสำหรับบทสนทนาแบบเรียลไทม์และแอปพลิเคชัน AI ที่ใช้เสียงเป็นหลัก
  อ่านเอกสารประกอบของ [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th) เพื่อเริ่มต้นใช้งาน

## 25 มีนาคม 2026

- เปิดตัวโมเดลการสร้างเพลง [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)
  [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=th)
  (คลิปความยาว 30 วินาที) และ [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=th)
  (เพลงแบบเต็ม) ทั้ง 2 โมเดลยอมรับอินพุตข้อความและรูปภาพ และสร้างเสียงสเตอริโอ 48kHz คุณภาพสูง ดูรายละเอียดและ
  ตัวอย่างโค้ดได้ในคำแนะนำเกี่ยวกับ[การสร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)

## 23 มีนาคม 2026

- เปิดตัว[แพ็กเกจการเรียกเก็บเงินแบบชำระล่วงหน้าและชำระภายหลัง](https://ai.google.dev/gemini-api/docs/billing?hl=th)ใน AI Studio บัญชีที่มีอยู่อาจได้รับผลกระทบ โปรดอ่านข้อมูลเพิ่มเติมในเอกสารประกอบเรื่อง[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)

## 18 มีนาคม 2026

- เปิดตัวฟีเจอร์ใหม่ [การรวมเครื่องมือในตัวและการเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th) ซึ่งช่วยให้ใช้เครื่องมือในตัวของ Gemini ร่วมกับเครื่องมือการเรียกฟังก์ชันที่กำหนดเองได้ในการเรียก API ครั้งเดียว
- [การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th#supported_models)
  รองรับโมเดล Gemini 3 แล้วนับจากนี้เป็นต้นไป

## 16 มีนาคม 2026

- เปิดตัว[ระดับการใช้งาน](https://ai.google.dev/gemini-api/docs/billing?hl=th#about-billing)ที่ปรับปรุงใหม่
  และ[ขีดจำกัดค่าใช้จ่ายของบัญชีสำหรับการเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th#tier-spend-caps)
  เพื่อประสบการณ์การเรียกเก็บเงินจากผู้ใช้ที่ดียิ่งขึ้น

## 12 มีนาคม 2026

- เปิดตัว[ขีดจำกัดการใช้จ่ายระดับโปรเจ็กต์](https://ai.google.dev/gemini-api/docs/billing?hl=th#project-spend-caps)สำหรับการเรียกเก็บเงินใน AI Studio

## 10 มีนาคม 2026

- เปิดตัว `gemini-embedding-2-preview` ซึ่งเป็นโมเดลการฝังหลายรูปแบบตัวแรกของเรา
  โดยรองรับอินพุตข้อความ รูปภาพ วิดีโอ เสียง และ PDF
  ซึ่งจะแมปรูปแบบทั้งหมดลงในพื้นที่การฝังแบบรวม ดูข้อมูลเพิ่มเติมได้ที่
  [การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)
- ประกาศการเลิกใช้งาน: `gemini-2.5-flash-lite-preview-09-2025` โมเดล
  จะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 31 มีนาคม 2026

## 9 มีนาคม 2026

- เราได้[ปิด](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)โมเดล Gemini 3 Pro เวอร์ชันตัวอย่างแล้ว ตอนนี้ `gemini-3-pro-preview` ชี้ไปยัง
  [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th)

## 3 มีนาคม 2026

- เปิดตัว Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง) ซึ่งเป็นโมเดล Flash-Lite ตัวแรกใน
  ซีรีส์ Gemini 3 อ่าน[หน้าโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th)เพื่อดูข้อมูลจำเพาะ ข้อมูลอัปเดตที่เฉพาะเจาะจง และคำแนะนำสำหรับนักพัฒนาซอฟต์แวร์

## 26 กุมภาพันธ์ 2026

- เปิดตัว Nano Banana 2, [ตัวอย่างรูปภาพ Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=th) ซึ่งเป็นโมเดลที่มีประสิทธิภาพสูง
  ซึ่งได้รับการเพิ่มประสิทธิภาพสำหรับความเร็วและกรณีการใช้งานที่มีปริมาณสูง
- ประกาศการเลิกใช้งาน: Gemini 3 Pro เวอร์ชันตัวอย่าง (`gemini-3-pro-preview`)
  จะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 9 มีนาคม 2026

## 19 กุมภาพันธ์ 2026

- เปิดตัว [Gemini 3.1 Pro เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) ซึ่งเป็นรุ่นล่าสุดใน
  ตระกูล Gemini 3 ใหม่
- เปิดตัวปลายทางแยกต่างหาก`gemini-3.1-pro-preview-customtools` ซึ่ง
  จัดลำดับความสำคัญของเครื่องมือที่กำหนดเองได้ดีกว่า สำหรับผู้ใช้ที่สร้างด้วยการผสมผสานระหว่าง Bash
  และเครื่องมือ

## 18 กุมภาพันธ์ 2026

- ประกาศการเลิกใช้งาน: โมเดลต่อไปนี้จะ[ปิดตัว](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 1 มิถุนายน 2026

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 กุมภาพันธ์ 2026

- เราจะ[ปิด](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)โมเดลต่อไปนี้

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 มกราคม 2026

- เปิดตัวการสนับสนุนเครื่องมือการใช้คอมพิวเตอร์ใน `gemini-3-pro-preview` และ
  `gemini-3-flash-preview`

## 21 มกราคม 2026

- เปลี่ยนชื่อแทน `latest` ดังนี้

  - `gemini-pro-latest` เปลี่ยนไปใช้ `gemini-3-pro-preview` แล้ว
  - `gemini-flash-latest` เปลี่ยนไปใช้ `gemini-3-flash-preview` แล้ว

## 15 มกราคม 2026

- ประกาศการเลิกใช้งาน: โมเดลต่อไปนี้จะ[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 17 กุมภาพันธ์ 2026

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- เราได้ปิดโมเดล `gemini-2.5-flash-image-preview` แล้ว

## 14 มกราคม 2026

- [ปิด](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)โมเดล `text-embedding-004` แล้ว

## 13 มกราคม 2026

- เพิ่มความละเอียดเอาต์พุต 4K สำหรับ [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th) และเพิ่ม
  การรองรับวิดีโอแนวตั้งในทุกความละเอียด

## 12 มกราคม 2026

- เปิดตัวฟีเจอร์วงจรการใช้งานโมเดล ตอนนี้บางรุ่นจะระบุวงจร
  ระยะและไทม์ไลน์การเลิกใช้งาน ดูข้อมูลเพิ่มเติมได้ในเอกสารประกอบต่อไปนี้

  - [ขั้นตอนของโมเดล](https://ai.google.dev/api/generate-content?hl=th#ModelStatus)

## 8 มกราคม 2026

- เปิดตัวการรองรับที่เก็บข้อมูล Cloud Storage รวมถึง URL ที่ลงนามล่วงหน้าของ DB สาธารณะและส่วนตัว เป็นแหล่งที่มาของอินพุตข้อมูลสำหรับ Gemini API นอกจากนี้ เรายังเพิ่มขีดจำกัดขนาดไฟล์จาก 20 MB เป็น 100 MB ด้วย โปรดดูรายละเอียดที่[วิธีการป้อนไฟล์
  คำแนะนำ](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

## 19 ธันวาคม 2025

- เปิดตัวการเปลี่ยนแปลงที่ไม่รองรับการทำงานย้อนหลังใน Interactions API ใน
  v1beta ฟิลด์ `total_reasoning_tokens` ได้เปลี่ยนชื่อเป็น
  `total_thought_tokens` เพื่อให้สอดคล้องกับแนวคิดของ "ความคิด" ใน
  โมเดลการคิดมากขึ้น

## 17 ธันวาคม 2025

- เปิดตัวเวอร์ชันตัวอย่างของ Gemini 3 Flash `gemini-3-flash-preview` ซึ่งให้ประสิทธิภาพระดับแนวหน้าอย่างรวดเร็ว
  เทียบเท่าโมเดลขนาดใหญ่กว่าในราคาที่ถูกกว่า
  ด้วยความสามารถด้านการให้เหตุผลเชิงภาพและเชิงพื้นที่ที่อัปเกรดแล้ว รวมถึงการเขียนโค้ดแบบ Agent
  อ่านเอกสารประกอบเกี่ยวกับฟีเจอร์ใหม่ๆ บางอย่าง ซึ่งรวมถึง

  - [การตอบกลับฟังก์ชันหลายรูปแบบ](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#multimodal)
  - [การเรียกใช้โค้ดด้วยรูปภาพ](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#images)

## 12 ธันวาคม 2025

- เปิดตัว `gemini-2.5-flash-native-audio-preview-12-2025`,
  โมเดลเสียงเนทีฟใหม่สำหรับ Live API การอัปเดตนี้จะปรับปรุงความสามารถของโมเดล
  ในการจัดการเวิร์กโฟลว์ที่ซับซ้อน ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th) และ
  [เสียงเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=th)

## 11 ธันวาคม 2025

- เปิดตัว Interactions API API นี้มีอินเทอร์เฟซแบบรวม
  สำหรับการโต้ตอบกับโมเดลและเอเจนต์ของ Gemini ดูข้อมูลเพิ่มเติมได้ที่คู่มือ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
- เปิดตัวเอเจนต์ Deep Research ของ Gemini ในเวอร์ชันตัวอย่าง ฟีเจอร์นี้สามารถ
  วางแผน ดำเนินการ และสังเคราะห์ผลลัพธ์สำหรับงานค้นคว้าข้อมูลแบบหลายขั้นตอน
  ได้โดยอัตโนมัติ ดูรายละเอียดได้ในคำแนะนำเกี่ยวกับ [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)

## 10 ธันวาคม 2025

- เปิดตัวการปรับปรุง[โมเดลข้อความเป็นเสียง](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th), ตัวอย่าง TTS ของ Gemini 2.5 Flash
  (ปรับให้มีเวลาในการตอบสนองต่ำ) และตัวอย่าง TTS ของ Gemini 2.5 Pro (ปรับให้มี
  คุณภาพ) ซึ่งรวมถึงการปรับปรุงความสามารถในการแสดงออก การเว้นวรรคที่แม่นยำ และ
  บทสนทนาที่ราบรื่น

## 9 ธันวาคม 2025

- ตอนนี้เราได้ปิดตัวโมเดล Gemini Live API ต่อไปนี้แล้ว
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 ธันวาคม 2025

- การเรียกเก็บเงินสำหรับ Gemini 3 สำหรับ[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) จะเริ่มในวันที่ 5 มกราคม 2026

## 4 ธันวาคม 2568

- ประกาศการเลิกใช้งาน: โมเดล `gemini-2.5-flash-image-preview` จะ
  ปิดตัวลงในวันที่ 15 มกราคม 2026

## 3 ธันวาคม 2025

- ประกาศการเลิกใช้งาน: เราจะปิดโมเดล `text-embedding-004`
  ในวันที่ 14 มกราคม 2026

## 20 พฤศจิกายน 2025

- เปิดตัวตัวอย่างรูปภาพ Gemini 3 Pro `gemini-3-pro-image-preview` ซึ่งเป็น
  รุ่นถัดไปของโมเดล Nano Banana อ่านรายละเอียดเพิ่มเติมได้ที่หน้า[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 18 พฤศจิกายน 2025

- เปิดตัวโมเดล Gemini 3 Series รุ่นแรก `gemini-3-pro-preview` ซึ่งเป็นโมเดลการให้เหตุผลและการทำความเข้าใจข้อมูลหลายรูปแบบที่ล้ำสมัยของเรา พร้อมความสามารถในการเขียนโค้ดและตัวแทนที่ทรงพลัง

  นอกเหนือจากการปรับปรุงความอัจฉริยะและประสิทธิภาพแล้ว
  รุ่นตัวอย่างของ Gemini 3 Pro ยังมีลักษณะการทำงานใหม่ๆ เกี่ยวกับสิ่งต่อไปนี้

  - [ความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th)
  - [ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th)
  - [ระดับการคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#thinking-levels)

  อ่าน[คู่มือนักพัฒนาซอฟต์แวร์ Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=th) สำหรับ
  การย้ายข้อมูล ฟีเจอร์ใหม่ และข้อกำหนด

## 11 พฤศจิกายน 2025

- ประกาศการเลิกใช้งาน: เราจะปิดโมเดลต่อไปนี้

  - 12 พฤศจิกายน:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 พฤศจิกายน:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 พฤศจิกายน 2025

- ระบบจะปิดโมเดลต่อไปนี้

  - `imagen-3.0-generate-002`

  ให้ใช้ [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=th#imagen-4) แทน ดูรายละเอียดเพิ่มเติมได้ใน[ตารางการเลิกใช้งาน Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)

## 6 พฤศจิกายน 2025

- เปิดตัว File Search API ในเวอร์ชันตัวอย่างแบบสาธารณะ ซึ่งช่วยให้นักพัฒนาซอฟต์แวร์
  อ้างอิงคำตอบจากข้อมูลของตนเองได้ ดูข้อมูลเพิ่มเติมได้ที่หน้า[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)ใหม่

## 4 พฤศจิกายน 2025

- สำหรับ [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=th) เราได้ลดจำนวนโทเค็นอินพุต
  สำหรับรูปภาพจาก 1,290 เป็น 258 เพื่อลดต้นทุน
  ในการแก้ไขรูปภาพ
- ประกาศการเลิกใช้งาน: เราจะปิดโมเดลต่อไปนี้

  - 18 พฤศจิกายน:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 ธันวาคม:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 ธันวาคม:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 ตุลาคม 2025

- เปิดตัวเครื่องมือ[การบันทึกและการสร้างชุดข้อมูล](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)ใหม่
  สำหรับ Gemini API

## 20 ตุลาคม 2025

- ตอนนี้เราได้ปิดตัวโมเดล Gemini Live API ต่อไปนี้แล้ว

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  คุณสามารถใช้ `gemini-2.5-flash-native-audio-preview-09-2025` แทนได้
- ประกาศการเลิกใช้งาน: การปิดตัวของ `gemini-2.0-flash-live-001` และ
  `gemini-live-2.5-flash-preview` ในวันที่ 9 ธันวาคม 2025

## 17 ตุลาคม 2025

- **การเชื่อมต่อแหล่งข้อมูลกับ Google Maps** พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว
  ดูข้อมูลเพิ่มเติมได้ที่เอกสารประกอบ[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)

## 15 ตุลาคม 2025

- เปิดตัวโมเดล [Veo 3.1 และ 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=th#veo-3.1) ในเวอร์ชันตัวอย่างแบบสาธารณะ พร้อมฟีเจอร์ใหม่ๆ ได้แก่

  - การขยายวิดีโอที่สร้างด้วย Veo
  - อ้างอิงรูปภาพได้สูงสุด 3 รูปเพื่อสร้างวิดีโอ
  - การระบุรูปภาพเฟรมแรกและเฟรมสุดท้ายเพื่อสร้างวิดีโอ

  การเปิดตัวนี้ยังเพิ่มตัวเลือกเพิ่มเติมสำหรับระยะเวลาของวิดีโอเอาต์พุตของ Veo 3 ได้แก่ 4, 6 และ 8 วินาที
- ประกาศการเลิกใช้งาน: การปิดตัวสำหรับ `veo-3.0-generate-preview` และ
  `veo-3.0-fast-generate-preview` จะมีขึ้นในวันที่ 12 พฤศจิกายน 2025

## 7 ตุลาคม 2025

- เปิดตัว [Gemini 2.5 Computer Use Preview](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

## 2 ตุลาคม 2025

- เปิดตัว GA ของรูปภาพ Gemini 2.5 Flash: [การสร้างรูปภาพด้วย Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 29 กันยายน 2025

- ตอนนี้เราได้ปิดโมเดล Gemini 1.5 ต่อไปนี้แล้ว
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 กันยายน 2025

- เปิดตัวโมเดล Gemini Robotics-ER 1.5 ในเวอร์ชันตัวอย่าง ดู[ภาพรวมของหุ่นยนต์](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)
  เพื่อดูวิธีใช้โมเดลสำหรับแอปพลิเคชันหุ่นยนต์
- เปิดตัวโมเดลเวอร์ชันตัวอย่างต่อไปนี้

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  ดูรายละเอียดได้ที่หน้า[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

## 23 กันยายน 2025

- เปิดตัว `gemini-2.5-flash-native-audio-preview-09-2025`
  โมเดลเสียงใหม่แบบเนทีฟสำหรับ Live API ที่มีการเรียกใช้ฟังก์ชันที่ปรับปรุงแล้ว
  และการจัดการการตัดเสียงพูด ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th) และ
  [เสียงเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-native-audio)

## 16 กันยายน 2025

- ประกาศการเลิกใช้งาน: เราจะปิดโมเดลต่อไปนี้ในเดือนตุลาคม 2025

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  ดูรายละเอียดเกี่ยวกับโมเดลการฝังล่าสุดได้ที่หน้า[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

## 10 กันยายน 2025

- เปิดตัวการรองรับ[โมเดลการฝังใน Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) และเพิ่ม Batch API ลงใน[ไลบรารีความเข้ากันได้กับ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th#batch) เพื่อให้เริ่มต้นใช้งานการค้นหาแบบกลุ่มได้ง่ายยิ่งขึ้น

## 9 กันยายน 2025

- เปิดตัว Veo 3 และ Veo 3 Fast GA โดยมีราคาที่ต่ำลงและตัวเลือกใหม่สำหรับ
  สัดส่วนภาพ ความละเอียด และการเริ่มต้น อ่านข้อมูลเพิ่มเติมใน
  [เอกสารประกอบของ Veo](https://ai.google.dev/gemini-api/docs/video?hl=th#model-features)

## 26 สิงหาคม 2025

- เปิดตัว[ตัวอย่างรูปภาพ Gemini 2.5](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-image-preview)
  โมเดลการสร้างรูปภาพแบบเนทีฟล่าสุดของเรา

## 18 สิงหาคม 2025

- เปิดตัว[เครื่องมือบริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) ในเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ซึ่งเป็นเครื่องมือสำหรับระบุ URL เป็นบริบทเพิ่มเติมในพรอมต์
  การสนับสนุนการใช้บริบท URL กับโมเดล `gemini-2.0-flash`
  (พร้อมใช้งานในช่วงการเปิดตัวเวอร์ชันทดลอง) จะสิ้นสุดในอีก 1 สัปดาห์

## 14 สิงหาคม 2025

- เปิดตัวโมเดล Imagen 4 Ultra, Standard และ Fast เป็นรุ่นที่พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) ดูข้อมูลเพิ่มเติมได้ที่หน้า [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=th)

## 7 สิงหาคม 2025

- `allow_adult` การตั้งค่าในการสร้างวิดีโอจากภาพพร้อมให้บริการแล้วในภูมิภาคที่ถูกจำกัด ดูรายละเอียดได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=th#veo-model-parameters)

## 31 กรกฎาคม 2025

- เปิดตัวการสร้างวิดีโอจากรูปภาพสำหรับโมเดล Veo 3 เวอร์ชันตัวอย่าง
- เปิดตัวโมเดล Veo 3 Fast Preview
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ Veo 3 ได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)

## 22 กรกฎาคม 2025

- เปิดตัว `gemini-2.5-flash-lite` โมเดล Gemini 2.5 ที่รวดเร็ว ต้นทุนต่ำ และมีประสิทธิภาพสูง ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5
  Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-lite)

## July 17, 2025

- เปิดตัว `veo-3.0-generate-preview` ซึ่งเป็นการอัปเดตล่าสุดของ Veo ที่มาพร้อม
  การสร้างวิดีโอพร้อมเสียง ดูข้อมูลเพิ่มเติมเกี่ยวกับ Veo 3 ได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)
- เพิ่มขีดจำกัดของอัตราสำหรับ Imagen 4 Standard และ Ultra ดูรายละเอียดเพิ่มเติมได้ที่หน้า[ขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)

## 14 กรกฎาคม 2025

- เปิดตัว `gemini-embedding-001` โมเดลการฝังข้อความเวอร์ชันเสถียร
  ดูข้อมูลเพิ่มเติมได้ที่[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th) `gemini-embedding-exp-03-07`
  เราจะเลิกใช้งานโมเดลนี้ในวันที่ 14 สิงหาคม 2025

## 7 กรกฎาคม 2025

- เปิดตัวโหมดกลุ่มของ Gemini API จัดกลุ่มคำขอและส่งไปประมวลผล
  แบบไม่พร้อมกัน ดูข้อมูลเพิ่มเติมได้ที่[โหมดกลุ่ม](https://ai.google.dev/gemini-api/docs/batch-mode?hl=th)

## 26 มิถุนายน 2025

- ตอนนี้โมเดลเวอร์ชันตัวอย่าง `gemini-2.5-pro-preview-05-06` และ `gemini-2.5-pro-preview-03-25` จะเปลี่ยนเส้นทางไปยังเวอร์ชันล่าสุดที่เสถียร `gemini-2.5-pro`
- `gemini-2.5-pro-exp-03-25` ปิดตัวแล้ว

## 24 มิถุนายน 2025

- เปิดตัวโมเดลตัวอย่าง Imagen 4 Ultra และ Standard ดูข้อมูลเพิ่มเติมได้ที่หน้า[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 17 มิถุนายน 2025

- เราได้เปิดตัว `gemini-2.5-pro` ซึ่งเป็นเวอร์ชันเสถียรของโมเดลที่ทรงพลังที่สุด
  ของเรา ซึ่งตอนนี้มาพร้อมการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่
  [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro)
  และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th) `gemini-2.5-pro-preview-05-06`
  จะเปลี่ยนเส้นทางไปยัง `gemini-2.5-pro` ในวันที่ 26 มิถุนายน 2025
- เปิดตัว `gemini-2.5-flash` โมเดล 2.5 Flash ที่เสถียรตัวแรกของเรา ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash)
  `gemini-2.5-flash-preview-04-17` จะเลิกใช้งานในวันที่ 15 กรกฎาคม 2025
- เปิดตัวโมเดล Gemini 2.5 `gemini-2.5-flash-lite-preview-06-17` ที่มีต้นทุนต่ำและประสิทธิภาพสูง
  ดูข้อมูลเพิ่มเติมได้ที่[เวอร์ชันตัวอย่างของ Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-lite)

## 5 มิถุนายน 2025

- เปิดตัว `gemini-2.5-pro-preview-06-05` ซึ่งเป็นโมเดลเวอร์ชันใหม่ที่ทรงพลังที่สุดของเรา
  พร้อมการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่
  [ตัวอย่าง Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-06-05)
  และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
  ระบบจะเปลี่ยนเส้นทาง `gemini-2.5-pro-preview-05-06` ไปยัง `gemini-2.5-pro` ในวันที่ 26 มิถุนายน 2025

## 27 พฤษภาคม 2025

- เราได้ปิดตัวโมเดลการปรับแต่งสุดท้ายที่พร้อมให้บริการอย่าง Gemini 1.5 Flash 001 แล้ว
  ระบบไม่รองรับการปรับแต่งในโมเดลใดๆ อีกต่อไป
  ดู[การปรับแต่งด้วย Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=th)

## 20 พ.ค. 2025

**การอัปเดต API:**

- เปิดตัวการรองรับ
  [การประมวลผลวิดีโอก่อนการแสดงผลที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#customize-video-processing)
  โดยใช้ช่วงการตัดและอัตราการสุ่มตัวอย่างเฟรมที่กำหนดค่าได้
- เปิดตัวการใช้เครื่องมือหลายอย่าง ซึ่งรองรับการกำหนดค่า[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)และ[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th) ในคำขอ`generateContent`เดียวกัน
- เปิดตัวการรองรับ[การเรียกใช้ฟังก์ชันแบบไม่พร้อมกัน](https://ai.google.dev/gemini-api/docs/live-tools?hl=th#async-function-calling)
  ใน Live API
- เปิดตัว[เครื่องมือบริบทของ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)
  เวอร์ชันทดลองสำหรับระบุ URL เป็นบริบทเพิ่มเติมในพรอมต์

**การอัปเดตโมเดล**

- เปิดตัว `gemini-2.5-flash-preview-05-20` ซึ่งเป็นโมเดล[ตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#model-versions)ของ Gemini
  ที่ได้รับการเพิ่มประสิทธิภาพเพื่อ
  ประสิทธิภาพด้านราคาและการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่
  [เวอร์ชันตัวอย่างของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview)
  และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
- เปิดตัวโมเดล
  [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-tts)
  และ
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview-tts)
  ซึ่งสามารถ[สร้างคำพูด](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)จากผู้พูด 1 หรือ 2 คน
- เปิดตัว`lyria-realtime-exp`โมเดล ซึ่ง[สร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)แบบเรียลไทม์
- เปิดตัว `gemini-2.5-flash-preview-native-audio-dialog` และ
  `gemini-2.5-flash-exp-native-audio-thinking-dialog`,
  โมเดล Gemini ใหม่สำหรับ Live API ที่มีความสามารถเอาต์พุตเสียงแบบเนทีฟ ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#native-audio-output) และ[เสียงดั้งเดิมของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-native-audio)
- เปิดตัว`gemma-3n-e4b-it`เวอร์ชันตัวอย่างที่พร้อมใช้งานใน
  [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API
  ซึ่งเป็นส่วนหนึ่งของการเปิดตัว [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=th)

## 7 พฤษภาคม 2025

- เปิดตัว `gemini-2.0-flash-preview-image-generation` ซึ่งเป็นโมเดลเวอร์ชันตัวอย่างสำหรับ
  การสร้างและแก้ไขรูปภาพ ดูข้อมูลเพิ่มเติมได้ที่[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)และ[การสร้างรูปภาพตัวอย่างของ Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.0-flash-preview-image-generation)

## 6 พฤษภาคม 2025

- เปิดตัว `gemini-2.5-pro-preview-05-06` ซึ่งเป็นโมเดลเวอร์ชันใหม่ที่ทรงพลังที่สุดของเรา
  พร้อมการปรับปรุงด้านโค้ดและการเรียกใช้ฟังก์ชัน `gemini-2.5-pro-preview-03-25`
  จะชี้ไปยังโมเดลเวอร์ชันใหม่โดยอัตโนมัติ

## 17 เมษายน 2025

- เปิดตัว `gemini-2.5-flash-preview-04-17` ซึ่งเป็นโมเดล[ตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#model-versions)ของ Gemini
  ที่ได้รับการเพิ่มประสิทธิภาพเพื่อ
  ประสิทธิภาพด้านราคาและการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่
  [เวอร์ชันตัวอย่างของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview)
  และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

## 16 เมษายน 2025

- เปิดตัวการแคชบริบทสำหรับ
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.0-flash)

## 9 เมษายน 2025

**การอัปเดตโมเดล**

- เปิดตัว `veo-2.0-generate-001` ซึ่งเป็นโมเดลข้อความและรูปภาพเป็นวิดีโอที่พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) โดยสามารถสร้างวิดีโอที่มีรายละเอียดและมีความแตกต่างทางศิลปะ
  ดูข้อมูลเพิ่มเติมได้ที่[เอกสารของ Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)
- เปิดตัว`gemini-2.0-flash-live-001`เวอร์ชันตัวอย่างแบบสาธารณะของโมเดล [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ที่เปิดใช้การเรียกเก็บเงิน

  - **การจัดการเซสชันและความน่าเชื่อถือที่ได้รับการปรับปรุง**

    - **การกลับมาใช้เซสชันต่อ:** รักษาเซสชันให้ใช้งานได้แม้เครือข่ายจะหยุดชะงักชั่วคราว
      ตอนนี้ API รองรับการจัดเก็บสถานะเซสชันฝั่งเซิร์ฟเวอร์ (นานสูงสุด 24 ชั่วโมง) และมีแฮนเดิล (session\_resumption) เพื่อเชื่อมต่ออีกครั้งและดำเนินการต่อจากจุดที่คุณค้างไว้
    - **เซสชันที่ยาวขึ้นผ่านการบีบอัดบริบท:** เปิดใช้การโต้ตอบที่ยาวนานขึ้น
      นอกเหนือจากขีดจำกัดเวลาก่อนหน้า กำหนดค่าการบีบอัดหน้าต่างบริบทด้วยกลไกหน้าต่างเลื่อนเพื่อจัดการความยาวบริบทโดยอัตโนมัติ ซึ่งจะช่วยป้องกันการสิ้นสุดอย่างกะทันหันเนื่องจากขีดจำกัดบริบท
    - **การแจ้งเตือนการยกเลิกการเชื่อมต่ออย่างราบรื่น:** รับข้อความจาก`GoAway`เซิร์ฟเวอร์
      ที่ระบุเวลาที่การเชื่อมต่อกำลังจะปิด เพื่อให้จัดการได้อย่างราบรื่นก่อนการสิ้นสุด
  - **ควบคุมการโต้ตอบได้มากขึ้น**
  - **การตรวจจับกิจกรรมเสียงพูด (VAD) ที่กำหนดค่าได้:** เลือกระดับความไว หรือปิดใช้ VAD อัตโนมัติทั้งหมด แล้วใช้เหตุการณ์ไคลเอ็นต์ใหม่ (`activityStart`, `activityEnd`) เพื่อควบคุมการพูดด้วยตนเอง
  - **การจัดการการขัดจังหวะที่กำหนดค่าได้:** กำหนดว่าข้อมูลจากผู้ใช้ ควรขัดจังหวะการตอบกลับของโมเดลหรือไม่
  - **ความครอบคลุมของผลัดที่กำหนดค่าได้:** เลือกว่า API จะประมวลผลอินพุตเสียงและวิดีโอทั้งหมดอย่างต่อเนื่อง หรือจะบันทึกเฉพาะเมื่อตรวจพบว่าผู้ใช้ปลายทางกำลังพูด
  - **ความละเอียดของสื่อที่กำหนดค่าได้:** เพิ่มประสิทธิภาพเพื่อคุณภาพหรือการใช้โทเค็น
    โดยเลือกความละเอียดสำหรับสื่ออินพุต
  - **เอาต์พุตและฟีเจอร์ที่สมบูรณ์ยิ่งขึ้น**
  - **ตัวเลือกเสียงและภาษาที่เพิ่มขึ้น:** เลือกจากเสียงใหม่ 2 แบบและภาษาใหม่ 30 ภาษาสำหรับเอาต์พุตเสียง ตอนนี้คุณกำหนดค่าภาษาเอาต์พุตได้ภายใน `speechConfig` แล้ว
  - **การสตรีมข้อความ:** รับคำตอบที่เป็นข้อความทีละรายการขณะที่ระบบสร้างคำตอบเหล่านั้น ซึ่งจะช่วยให้แสดงต่อผู้ใช้ได้เร็วขึ้น
  - **การรายงานการใช้โทเค็น:** รับข้อมูลเชิงลึกเกี่ยวกับการใช้งานด้วย
    จำนวนโทเค็นโดยละเอียดที่ระบุในฟิลด์ `usageMetadata` ของข้อความเซิร์ฟเวอร์
    ซึ่งแบ่งตามรูปแบบและเฟสของพรอมต์หรือการตอบกลับ

## 4 เมษายน 2025

- เปิดตัว `gemini-2.5-pro-preview-03-25` ซึ่งเป็นเวอร์ชันตัวอย่างแบบสาธารณะของ Gemini 2.5 Pro
  ที่เปิดใช้การเรียกเก็บเงินแล้ว คุณยังสามารถใช้ `gemini-2.5-pro-exp-03-25` ใน
  ระดับฟรีต่อไปได้

## 25 มีนาคม 2025

- เปิดตัว `gemini-2.5-pro-exp-03-25` ซึ่งเป็นโมเดล Gemini เวอร์ชันทดลองแบบสาธารณะ
  โดยเปิดโหมดการคิดไว้เสมอโดยค่าเริ่มต้น
  ดูข้อมูลเพิ่มเติมได้ที่[Gemini 2.5 Pro เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-03-25)

## 12 มีนาคม 2025

**การอัปเดตโมเดล**

- เปิดตัวโมเดล [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#gemini)
  เวอร์ชันทดลองที่สามารถสร้างและแก้ไขรูปภาพได้
- เปิดตัว`gemma-3-27b-it`พร้อมใช้งานใน
  [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API
  ซึ่งเป็นส่วนหนึ่งของการเปิดตัว [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=th)

**การอัปเดต API:**

- เพิ่มการรองรับ[URL ของ YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=th#youtube) เป็นแหล่งที่มาของสื่อ
- เพิ่มการรองรับการใส่[วิดีโอในบรรทัด](https://ai.google.dev/gemini-api/docs/vision?hl=th#inline-video)ที่มีขนาดน้อยกว่า 20 MB

## 11 มีนาคม 2025

**การอัปเดต SDK:**

- เปิดตัว [Google Gen AI SDK สำหรับ TypeScript และ JavaScript](https://googleapis.github.io/js-genai)
  ในเวอร์ชันตัวอย่างแบบสาธารณะ

## 7 มีนาคม 2025

**การอัปเดตโมเดล**

- เปิดตัว `gemini-embedding-exp-03-07` โมเดลการฝังที่อิงตาม Gemini [เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)
  ในเวอร์ชันตัวอย่างแบบสาธารณะ

## 28 กุมภาพันธ์ 2025

**การอัปเดต API:**

- เพิ่มการรองรับ[การค้นหาเป็นเครื่องมือ](https://ai.google.dev/gemini-api/docs/grounding?hl=th)
  ใน `gemini-2.0-pro-exp-02-05` ซึ่งเป็นโมเดลทดลองที่อิงตาม
  Gemini 2.0 Pro

## 25 กุมภาพันธ์ 2025

**การอัปเดตโมเดล**

- เปิดตัว `gemini-2.0-flash-lite` เวอร์ชันพร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) ของ
  [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash-lite)
  ซึ่งได้รับการเพิ่มประสิทธิภาพด้านความเร็ว การปรับขนาด และความคุ้มค่า

## 19 กุมภาพันธ์ 2025

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- รองรับ[ภูมิภาคอื่นๆ](https://ai.google.dev/gemini-api/docs/available-regions?hl=th)
  (โคโซโว กรีนแลนด์ และหมู่เกาะแฟโร)

**การอัปเดต API:**

- รองรับ[ภูมิภาคอื่นๆ](https://ai.google.dev/gemini-api/docs/available-regions?hl=th)
  (โคโซโว กรีนแลนด์ และหมู่เกาะแฟโร)

## 18 กุมภาพันธ์ 2025

**การอัปเดตโมเดล**

- ระบบไม่รองรับ Gemini 1.0 Pro อีกต่อไป ดูรายการโมเดลที่รองรับได้ที่
  [โมเดล Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

## 11 กุมภาพันธ์ 2025

**การอัปเดต API:**

- ข้อมูลอัปเดตเกี่ยวกับ[ความเข้ากันได้ของไลบรารี OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)

## 6 กุมภาพันธ์ 2025

**การอัปเดตโมเดล**

- เปิดตัว `imagen-3.0-generate-002` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ
  [Imagen 3 ใน Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=th)

**การอัปเดต SDK:**

- เปิดตัว [Google Gen AI SDK สำหรับ Java](https://github.com/googleapis/java-genai)
  ในเวอร์ชันตัวอย่างแบบสาธารณะ

## 5 กุมภาพันธ์ 2025

**การอัปเดตโมเดล**

- เปิดตัว `gemini-2.0-flash-001` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash) ที่
  รองรับเอาต์พุตที่เป็นข้อความเท่านั้น
- เปิดตัว `gemini-2.0-pro-exp-02-05`,
  Gemini 2.0 Pro เวอร์ชันตัวอย่าง[ทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)แบบสาธารณะ
- เปิดตัว `gemini-2.0-flash-lite-preview-02-05` ซึ่งเป็น[โมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash-lite)เวอร์ชันทดลอง
  แบบสาธารณะที่เพิ่มประสิทธิภาพเพื่อความคุ้มค่า

**การอัปเดต API:**

- เพิ่มการรองรับ[อินพุตไฟล์และเอาต์พุตกราฟ](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#input-output)
  ลงในการเรียกใช้โค้ด

**การอัปเดต SDK:**

- เปิดตัว[Gen AI SDK ของ Google สำหรับ Python](https://googleapis.github.io/python-genai/)
  ในเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)

## 21 มกราคม 2025

**การอัปเดตโมเดล**

- เปิดตัว`gemini-2.0-flash-thinking-exp-01-21`เวอร์ชันตัวอย่างล่าสุดของ
  โมเดลที่อยู่เบื้องหลัง[โมเดล Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

## 19 ธันวาคม 2024

**การอัปเดตโมเดล**

- เปิดตัวโหมด Gemini 2.0 Flash Thinking สำหรับเวอร์ชันตัวอย่างแบบสาธารณะ โหมดการคิดเป็นโมเดลการคำนวณในเวลาทดสอบที่ช่วยให้คุณเห็นกระบวนการคิดของโมเดลขณะที่โมเดลสร้างคำตอบ และสร้างคำตอบที่มีความสามารถในการให้เหตุผลที่ดียิ่งขึ้น

  อ่านเพิ่มเติมเกี่ยวกับโหมด Gemini 2.0 Flash Thinking ได้ใน[หน้าภาพรวม](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=th)

## 11 ธันวาคม 2024

**การอัปเดตโมเดล**

- เปิดตัว [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash)
  สำหรับเวอร์ชันตัวอย่างแบบสาธารณะ รายการฟีเจอร์บางส่วนของ Gemini 2.0 Flash Experimental มีดังนี้
  - เร็วกว่า Gemini 1.5 Pro ถึง 2 เท่า
  - การสตรีมแบบ 2 ทางด้วย Live API
  - การสร้างคำตอบแบบมัลติโมดัลในรูปแบบข้อความ รูปภาพ และคำพูด
  - การใช้เครื่องมือในตัวร่วมกับการให้เหตุผลแบบการสนทนาไปมาเพื่อใช้ฟีเจอร์ต่างๆ เช่น การเรียกใช้โค้ด การค้นหา การเรียกใช้ฟังก์ชัน และอื่นๆ

อ่านข้อมูลเพิ่มเติมเกี่ยวกับ Gemini 2.0 Flash ได้ใน[หน้าภาพรวม](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=th)

## 21 พฤศจิกายน 2024

**การอัปเดตโมเดล**

- เปิดตัว `gemini-exp-1121` โมเดล Gemini API เวอร์ชันทดลองที่ทรงพลังยิ่งกว่าเดิม

**การอัปเดตโมเดล**

- อัปเดตชื่อแทนของโมเดล `gemini-1.5-flash-latest` และ `gemini-1.5-flash`
  ให้ใช้ `gemini-1.5-flash-002`
  - การเปลี่ยนแปลงพารามิเตอร์ `top_k`: โมเดล `gemini-1.5-flash-002`
    รองรับค่า `top_k` ระหว่าง 1 ถึง 41 (ไม่รวม)
    ค่าที่มากกว่า 40 จะเปลี่ยนเป็น 40

## 14 พฤศจิกายน 2024

**การอัปเดตโมเดล**

- เปิดตัว `gemini-exp-1114` ซึ่งเป็นโมเดล Gemini API เวอร์ชันทดลองที่มีประสิทธิภาพ

## 8 พฤศจิกายน 2024

**การอัปเดต API:**

- เพิ่ม[การรองรับ Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=th) ในไลบรารี / REST API ของ OpenAI

## 31 ตุลาคม 2024

**การอัปเดต API:**

- เพิ่ม[การรองรับการเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

## 3 ตุลาคม 2024

**การอัปเดตโมเดล**

- เปิดตัว `gemini-1.5-flash-8b-001` โมเดล Gemini
  API ที่เล็กที่สุดของเราในเวอร์ชันเสถียร

## 24 กันยายน 2024

**การอัปเดตโมเดล**

- เปิดตัว `gemini-1.5-pro-002` และ `gemini-1.5-flash-002` ซึ่งเป็น Gemini 1.5 Pro และ 1.5 Flash เวอร์ชันเสถียรใหม่ 2 รายการ สำหรับเวอร์ชันสำหรับผู้ใช้ทั่วไป
- อัปเดตโค้ดโมเดล `gemini-1.5-pro-latest` ให้ใช้ `gemini-1.5-pro-002`
  และโค้ดโมเดล `gemini-1.5-flash-latest` ให้ใช้ `gemini-1.5-flash-002`
- เปิดตัว `gemini-1.5-flash-8b-exp-0924` เพื่อแทนที่ `gemini-1.5-flash-8b-exp-0827`
- เปิดตัว[ตัวกรองความปลอดภัยด้านความซื่อสัตย์ของพลเมือง](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th#safety-filters)
  สำหรับ Gemini API และ AI Studio
- เปิดตัวการรองรับพารามิเตอร์ใหม่ 2 รายการสำหรับ Gemini 1.5 Pro และ 1.5 Flash ใน
  Python และ NodeJS:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=th#FIELDS.frequency_penalty) และ
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=th#FIELDS.presence_penalty)

## 19 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มปุ่มชอบและไม่ชอบในคำตอบของโมเดลเพื่อให้ผู้ใช้แสดงความคิดเห็นเกี่ยวกับคุณภาพของคำตอบได้

**การอัปเดต API:**

- เพิ่มการรองรับเครดิต Google Cloud ซึ่งตอนนี้ใช้กับการใช้งาน Gemini API ได้แล้ว

## 17 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มปุ่ม**เปิดใน Colab** ที่ส่งออกพรอมต์และโค้ดเพื่อดำเนินการไปยัง Colab Notebook ฟีเจอร์นี้ยังไม่รองรับ
  การแจ้งด้วยเครื่องมือ (โหมด JSON, การเรียกใช้ฟังก์ชัน หรือการเรียกใช้โค้ด)

## 13 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มการรองรับโหมดเปรียบเทียบ ซึ่งช่วยให้คุณเปรียบเทียบคำตอบในโมเดลและพรอมต์ต่างๆ เพื่อค้นหาคำตอบที่เหมาะกับกรณีการใช้งานของคุณมากที่สุด

## 30 สิงหาคม 2024

**การอัปเดตโมเดล**

- Gemini 1.5 Flash รองรับ[การระบุสคีมา JSON ผ่านการกำหนดค่าโมเดล](https://ai.google.dev/gemini-api/docs/json-mode?hl=th#supply-schema-in-config)

## 27 สิงหาคม 2024

**การอัปเดตโมเดล**

- เปิดตัว[โมเดลทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)ต่อไปนี้
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 สิงหาคม 2024

**การอัปเดต API:**

- เพิ่มการรองรับ[การประมวลผล PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

## 5 สิงหาคม 2024

**การอัปเดตโมเดล**

- เปิดตัวการรองรับการปรับแต่งสำหรับ Gemini 1.5 Flash

## 1 สิงหาคม 2024

**การอัปเดตโมเดล**

- เปิดตัว `gemini-1.5-pro-exp-0801` ซึ่งเป็นเวอร์ชันทดลองใหม่ของ
  [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro)

## 12 กรกฎาคม 2024

**การอัปเดตโมเดล**

- นำการรองรับ Gemini 1.0 Pro Vision ออกจากบริการและเครื่องมือ Google AI

## 27 มิถุนายน 2024

**การอัปเดตโมเดล**

- เปิดตัวเวอร์ชันสำหรับผู้ใช้ทั่วไปสำหรับหน้าต่างบริบทขนาด 2 ล้านโทเค็นของ Gemini 1.5 Pro

**การอัปเดต API:**

- เพิ่มการรองรับ[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)

## 18 มิถุนายน 2024

**การอัปเดต API:**

- เพิ่มการรองรับ[การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)

## 12 มิถุนายน 2024

**การอัปเดตโมเดล**

- เลิกใช้งาน Gemini 1.0 Pro Vision

## 23 พฤษภาคม 2024

**การอัปเดตโมเดล**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) พร้อมให้บริการแก่ผู้ใช้ทั่วไป (GA) แล้ว
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) พร้อมให้บริการสำหรับผู้ใช้ทั่วไป (GA) แล้ว

## 14 พฤษภาคม 2024

**การอัปเดต API:**

- เปิดตัวหน้าต่างบริบทขนาด 2 ล้านโทเค็นสำหรับ Gemini 1.5 Pro (รายชื่อรอ)
- เปิดตัว[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)แบบจ่ายเมื่อใช้สำหรับ Gemini 1.0 Pro โดยการเรียกเก็บเงินสำหรับ Gemini 1.5 Pro และ Gemini 1.5 Flash จะพร้อมให้บริการเร็วๆ นี้
- เปิดตัวขีดจำกัดอัตราที่เพิ่มขึ้นสำหรับระดับการชำระเงินที่กำลังจะเปิดตัวของ Gemini 1.5
  Pro
- เพิ่มการรองรับวิดีโอบิวท์อินลงใน [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th)
- เพิ่มการรองรับข้อความธรรมดาใน [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th)
- เพิ่มการรองรับการเรียกใช้ฟังก์ชันแบบขนาน ซึ่งจะแสดงผลการเรียกมากกว่า 1 รายการพร้อมกัน

## 10 พฤษภาคม 2024

**การอัปเดตโมเดล**

- เปิดตัว [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) ในเวอร์ชันตัวอย่าง

## 9 เมษายน 2024

**การอัปเดตโมเดล**

- เปิดตัว [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) ในเวอร์ชันตัวอย่าง
- เปิดตัวโมเดลการฝังข้อความใหม่ `text-embeddings-004` ซึ่งรองรับ
  [การฝังแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/embeddings?hl=th#elastic-embedding)
  ที่มีขนาดต่ำกว่า 768

**การอัปเดต API:**

- เปิดตัว [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th) สำหรับจัดเก็บไฟล์สื่อชั่วคราวเพื่อใช้ในการแจ้ง
- เพิ่มการรองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ และเสียง หรือที่เรียกว่าการเขียนพรอมต์*แบบหลายรูปแบบ* ดูข้อมูลเพิ่มเติมได้ที่[การแจ้งด้วยสื่อ](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=th)
- เปิดตัว[คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/system-instructions?hl=th)ในเวอร์ชันเบต้า
- เพิ่ม[โหมดการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#function_calling_mode)
  ซึ่งกำหนดลักษณะการทำงานของการเรียกใช้ฟังก์ชัน
- เพิ่มการรองรับ`response_mime_type`ตัวเลือกการกำหนดค่า ซึ่งช่วยให้คุณขอคำตอบใน[รูปแบบ JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=th#json) ได้

## 19 มีนาคม 2024

**การอัปเดตโมเดล**

- เพิ่มการรองรับ[การปรับแต่ง Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  ใน Google AI Studio หรือด้วย Gemini API

## 13 ธันวาคม 2023

**การอัปเดตโมเดล**

- gemini-pro: โมเดลข้อความใหม่สำหรับงานที่หลากหลาย ปรับสมดุลความสามารถ
  และประสิทธิภาพ
- gemini-pro-vision: โมเดลมัลติโมดัลใหม่สำหรับงานที่หลากหลาย
  รักษาสมดุลระหว่างความสามารถและประสิทธิภาพ
- embedding-001: โมเดลการฝังใหม่
- aqa: โมเดลใหม่ที่ได้รับการปรับแต่งเป็นพิเศษซึ่งได้รับการฝึกให้ตอบคำถาม
  โดยใช้ข้อความเพื่ออ้างอิงคำตอบที่สร้างขึ้น

ดูรายละเอียดเพิ่มเติมได้ที่[โมเดล Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

**การอัปเดตเวอร์ชัน API:**

- v1: ช่อง API ที่เสถียร
- v1beta: เวอร์ชันเบต้า ช่องนี้มีฟีเจอร์ที่อาจอยู่ระหว่าง
  การพัฒนา

ดูรายละเอียดเพิ่มเติมได้ที่[หัวข้อเกี่ยวกับเวอร์ชันของ API](https://ai.google.dev/gemini-api/docs/api-versions?hl=th)

**การอัปเดต API:**

- `GenerateContent` เป็นปลายทางแบบรวมเดียวสำหรับแชทและข้อความ
- สตรีมได้ผ่านเมธอด `StreamGenerateContent`
- ความสามารถแบบหลายรูปแบบ: รูปภาพเป็นรูปแบบใหม่ที่รองรับ
- ฟีเจอร์เบต้าใหม่
  - [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=th)
  - การตอบคำถามโดยอิงตามแหล่งที่มา (AQA)
- จำนวนคำตอบที่เป็นไปได้ที่อัปเดตแล้ว: โมเดล Gemini จะแสดงคำตอบที่เป็นไปได้เพียง 1 รายการ
- หมวดหมู่การตั้งค่าความปลอดภัยและการจัดประเภทความปลอดภัยที่แตกต่างกัน ดูรายละเอียดเพิ่มเติมได้ที่[การตั้งค่าความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th)
- ระบบยังไม่รองรับการปรับแต่งโมเดลสำหรับโมเดล Gemini (อยู่ระหว่างดำเนินการ)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
