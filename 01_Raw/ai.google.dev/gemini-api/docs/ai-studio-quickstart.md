---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=th
fetched_at: 2026-08-10T03:19:57.776704+00:00
title: "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Google AI Studio \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# คู่มือเริ่มใช้งาน Google AI Studio อย่างรวดเร็ว

[Google AI Studio](https://aistudio.google.com/?hl=th) ช่วยให้คุณลองใช้
โมเดลและทดลองใช้พรอมต์ต่างๆ ได้อย่างรวดเร็ว เมื่อพร้อมสร้างแล้ว คุณ
สามารถเลือก "รับโค้ด" และภาษาโปรแกรมที่ต้องการเพื่อ
ใช้ [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=th) ได้

## พรอมต์และการตั้งค่า

Google AI Studio มีอินเทอร์เฟซหลายแบบสำหรับพรอมต์ที่ออกแบบมาสำหรับกรณีการใช้งานต่างๆ คู่มือนี้ครอบคลุม**พรอมต์แชท** ซึ่งใช้เพื่อสร้าง
ประสบการณ์การสนทนา เทคนิคการป้อนพรอมต์นี้ช่วยให้มีการป้อนข้อมูล
และตอบกลับหลายรอบเพื่อสร้างเอาต์พุต ดูข้อมูลเพิ่มเติมได้จาก
[ตัวอย่างพรอมต์แชทด้านล่าง](#chat_example)
ตัวเลือกอื่นๆ ได้แก่ **การสตรีมแบบเรียลไทม์**, **การสร้างวิดีโอ** และ
อื่นๆ

นอกจากนี้ AI Studio ยังมีแผง**การตั้งค่าการทำงาน** ซึ่งคุณสามารถปรับ[พารามิเตอร์ของโมเดล](https://ai.google.dev/docs/prompting-strategies?hl=th#model-parameters), [การตั้งค่าความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th) และเปิดใช้เครื่องมือต่างๆ เช่น [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th), [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th), [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) และ [การเชื่อมต่อแหล่งข้อมูล](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

## ตัวอย่างพรอมต์แชท: สร้างแอปพลิเคชันแชทที่กำหนดเอง

หากคุณเคยใช้แชทบ็อตอเนกประสงค์อย่าง
[Gemini](https://gemini.google.com/?hl=th) คุณจะได้รับประสบการณ์โดยตรงว่าโมเดล
Generative AI มีประสิทธิภาพเพียงใดสำหรับการสนทนาแบบเปิด แม้ว่าแชทบ็อตอเนกประสงค์เหล่านี้จะมีประโยชน์ แต่บ่อยครั้งที่ต้องปรับแต่งให้เหมาะกับกรณีการใช้งานเฉพาะ

ตัวอย่างเช่น คุณอาจต้องการสร้างแชทบ็อตฝ่ายบริการลูกค้าที่รองรับเฉพาะการสนทนาเกี่ยวกับผลิตภัณฑ์ของบริษัท หรืออาจต้องการสร้างแชทบ็อตที่พูดด้วยโทนเสียงหรือสไตล์เฉพาะ เช่น บ็อตที่ชอบเล่าเรื่องตลก บ็อตที่ชอบแต่งกลอน หรือบ็อตที่ใช้ Emoji จำนวนมากในคำตอบ

ตัวอย่างนี้แสดงวิธีใช้ Google AI Studio เพื่อสร้างแชทบ็อตที่เป็นมิตรซึ่งสื่อสารราวกับเป็นมนุษย์ต่างดาวที่อาศัยอยู่บนยูโรปา ซึ่งเป็นดวงจันทร์ของดาวพฤหัสบดี

### ขั้นตอนที่ 1 - สร้างพรอมต์แชท

หากต้องการสร้างแชทบ็อต คุณต้องระบุตัวอย่างการโต้ตอบระหว่างผู้ใช้กับแชทบ็อตเพื่อแนะนำให้โมเดลแสดงคำตอบที่คุณต้องการ

วิธีสร้างพรอมต์แชท

1. เปิด [Google AI Studio](https://aistudio.google.com/?hl=th) ระบบจะเปิด**เพลย์กราวด์** โดยค่าเริ่มต้นพร้อมพรอมต์แชทใหม่
2. คลิก**การตั้งค่าการทำงาน** tune ที่มุมขวาบน
   เพื่อขยายแผง แล้วค้นหา
   [**คำแนะนำระบบ**](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions)
   ช่องป้อนข้อมูล วางข้อความต่อไปนี้ลงในช่องป้อนข้อความ

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

หลังจากเพิ่มคำแนะนำระบบแล้ว ให้เริ่มทดสอบแอปพลิเคชันโดยแชทกับโมเดลด้วยวิธีต่อไปนี้

1. ในช่องป้อนข้อความที่มีป้ายกำกับว่า **พิมพ์ข้อความ...** ให้พิมพ์คำถามหรือ
   ข้อสังเกตที่ผู้ใช้อาจถามหรือแสดงความคิดเห็น เช่น

   **ผู้ใช้:**

   ```
   What's the weather like?
   ```
2. คลิกปุ่ม**เรียกใช้** เพื่อรับคำตอบจากแชทบ็อต คำตอบนี้อาจมีลักษณะดังต่อไปนี้

   **โมเดล:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### ขั้นตอนที่ 2 - สอนให้บ็อตแชทได้ดีขึ้น

การให้คำแนะนำเพียงข้อเดียวช่วยให้คุณสร้างแชทบ็อตมนุษย์ต่างดาวจากยูโรปาแบบพื้นฐานได้ อย่างไรก็ตาม คำแนะนำเพียงข้อเดียวอาจไม่เพียงพอที่จะรับประกันความสอดคล้องและคุณภาพของคำตอบจากโมเดล หากไม่มีคำแนะนำที่เฉพาะเจาะจงมากขึ้น คำตอบของโมเดลสำหรับคำถามเกี่ยวกับสภาพอากาศมักจะยาวมากและอาจไม่ตรงกับคำถาม

ปรับแต่งโทนเสียงของแชทบ็อตโดยเพิ่มคำแนะนำระบบดังนี้

1. เริ่มพรอมต์แชทใหม่หรือใช้พรอมต์เดิม คุณสามารถแก้ไขคำแนะนำระบบได้หลังจากเริ่มเซสชันแชทแล้ว
2. ในส่วน**คำแนะนำระบบ** ให้เปลี่ยนคำแนะนำที่มีอยู่เป็นคำแนะนำต่อไปนี้

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. ป้อนคำถาม (`What's the weather like?`) อีกครั้ง แล้วคลิกปุ่ม**เรียกใช้**
   หากไม่ได้เริ่มแชทใหม่ คำตอบอาจมีลักษณะดังนี้

   **โมเดล:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

คุณสามารถใช้วิธีนี้เพื่อเพิ่มรายละเอียดให้กับแชทบ็อต ถามคำถามเพิ่มเติม แก้ไขคำตอบ และปรับปรุงคุณภาพของแชทบ็อต เพิ่มหรือแก้ไขคำแนะนำต่อไป และทดสอบว่าคำแนะนำเหล่านั้นเปลี่ยนลักษณะการทำงานของแชทบ็อตอย่างไร

### ขั้นตอนที่ 3 - ขั้นตอนต่อไป

เช่นเดียวกับพรอมต์ประเภทอื่นๆ เมื่อคุณสร้างต้นแบบพรอมต์จนพอใจแล้ว คุณสามารถใช้ปุ่ม**รับโค้ด** เพื่อเริ่มเขียนโค้ดหรือบันทึกพรอมต์ไว้เพื่อทำงานต่อในภายหลังและแชร์กับผู้อื่น

## อ่านเพิ่มเติม

- หากพร้อมที่จะไปยังโค้ดแล้ว โปรดดู[คู่มือเริ่มต้นใช้งาน
  API](https://ai.google.dev/gemini-api/docs/get-started?hl=th)
- ดูวิธีสร้างพรอมต์ที่ดีขึ้นได้ที่[หลักเกณฑ์
  การออกแบบพรอมต์](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
