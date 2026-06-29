---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=th
fetched_at: 2026-06-29T05:31:41.572017+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)

# เร่งการค้นพบด้วย Gemini สำหรับการวิจัย

[รับคีย์ Gemini API](https://aistudio.google.com/apikey?hl=th)

คุณสามารถใช้โมเดล Gemini เพื่อต่อยอดงานวิจัยพื้นฐานในสาขาวิชาต่างๆ
วิธีที่คุณใช้ Gemini เพื่อการวิจัยได้มีดังนี้

- **วิเคราะห์และควบคุมเอาต์พุตของโมเดล**: คุณสามารถตรวจสอบตัวเลือกคำตอบที่โมเดลสร้างขึ้นโดยใช้เครื่องมือต่างๆ เช่น `CitationMetadata` เพื่อทำการวิเคราะห์เพิ่มเติมได้ นอกจากนี้ คุณยังกำหนดค่าตัวเลือกสำหรับการสร้างโมเดลและ
  เอาต์พุตได้ด้วย เช่น `responseSchema`, `topP` และ `topK` [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/api/generate-content?hl=th)
- **อินพุตแบบหลายรูปแบบ**: Gemini สามารถประมวลผลรูปภาพ เสียง และวิดีโอ ซึ่งช่วยให้มี
  แนวทางการวิจัยที่น่าสนใจมากมาย [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/gemini-api/docs/vision?hl=th)
- **ความสามารถด้านบริบทแบบยาว**: Gemini 3.0 Flash และ Pro มาพร้อมหน้าต่างบริบทขนาด 1 ล้านโทเค็น
  [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
- **Grow with Google**: เข้าถึงโมเดล Gemini อย่างรวดเร็วผ่าน API และ Google AI
  Studio สำหรับกรณีการใช้งานในการผลิต หากคุณกำลังมองหาแพลตฟอร์มที่ใช้ Google Cloud
  แพลตฟอร์มเอเจนต์ Gemini Enterprise สามารถมอบโครงสร้างพื้นฐานเพิ่มเติมที่รองรับได้

Google ให้สิทธิ์เข้าถึงเครดิต Gemini API สำหรับนักวิทยาศาสตร์และนักวิจัยทางวิชาการผ่าน[โปรแกรม Gemini สำหรับสถาบันการศึกษา](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=th#gemini-academic-program) เพื่อสนับสนุนการวิจัยทางวิชาการและขับเคลื่อนการวิจัยที่ล้ำสมัย

## เริ่มต้นใช้งาน Gemini

Gemini API และ Google AI Studio ช่วยให้คุณเริ่มต้นใช้งานโมเดลล่าสุดของ Google
และเปลี่ยนไอเดียของคุณให้เป็นแอปพลิเคชันที่ปรับขนาดได้

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## นักวิชาการที่แนะนำ

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=th)

"การวิจัยของเราตรวจสอบ Gemini ในฐานะโมเดลภาษาภาพ (VLM) และพฤติกรรมแบบเอเจนต์ในสภาพแวดล้อมที่หลากหลายจากมุมมองด้านความแข็งแกร่งและความปลอดภัย จนถึงตอนนี้ เราได้ประเมินความแข็งแกร่งของ Gemini ในการรับมือกับสิ่งรบกวนต่างๆ เช่น หน้าต่างป๊อปอัป เมื่อเอเจนต์ VLM ทำงานบนคอมพิวเตอร์ และได้ใช้ประโยชน์จาก Gemini ในการวิเคราะห์การโต้ตอบทางโซเชียล เหตุการณ์ตามลำดับเวลา รวมถึงปัจจัยเสี่ยงตามข้อมูลวิดีโอที่ป้อน"

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=th)

"Gemini Pro และ Flash ที่มีหน้าต่างบริบทแบบยาวช่วยเราใน OK-Robot ซึ่งเป็นโปรเจ็กต์การจัดการบนอุปกรณ์เคลื่อนที่แบบเปิดคำศัพท์ Gemini ช่วยให้สามารถใช้คำสั่งและคำค้นหาภาษาธรรมชาติที่ซับซ้อนกับ "หน่วยความจำ" ของหุ่นยนต์ได้ ในกรณีนี้คือการสังเกตการณ์ก่อนหน้าที่หุ่นยนต์ดำเนินการเป็นเวลานาน นอกจากนี้ ผมและ Mahi Shafiullah ยังใช้ Gemini เพื่อแยกย่อยงานเป็นโค้ดที่หุ่นยนต์สามารถดำเนินการในโลกแห่งความเป็นจริงได้ด้วย"

## โปรแกรม Gemini Academic

นักวิจัยด้านวิชาการที่มีคุณสมบัติ (เช่น คณาจารย์ เจ้าหน้าที่ และนักศึกษาปริญญาเอก) ใน[ประเทศที่รองรับ](https://ai.google.dev/gemini-api/docs/available-regions?hl=th)สามารถสมัครรับเครดิต Gemini API
และขีดจำกัดอัตราที่สูงขึ้นสำหรับโปรเจ็กต์วิจัย การสนับสนุนนี้ช่วยให้การทดลองทางวิทยาศาสตร์มีอัตราการส่งข้อมูลสูงขึ้นและช่วยพัฒนาการวิจัย

เราสนใจเป็นพิเศษในสาขาการวิจัยในส่วนต่อไปนี้
แต่ก็ยินดีรับใบสมัครจากสาขาวิทยาศาสตร์ต่างๆ

- **การประเมินและเกณฑ์มาตรฐาน**: วิธีการประเมินที่ชุมชนรับรองซึ่ง
  สามารถให้สัญญาณประสิทธิภาพที่แข็งแกร่งในด้านต่างๆ เช่น ความถูกต้อง ความปลอดภัย
  การปฏิบัติตามคำสั่ง การให้เหตุผล และการวางแผน
- **เร่งการค้นพบทางวิทยาศาสตร์เพื่อประโยชน์ของมวลมนุษยชาติ**: ศักยภาพ
  ในการประยุกต์ใช้ AI ในการวิจัยทางวิทยาศาสตร์แบบสหวิทยาการ ซึ่งรวมถึงสาขาต่างๆ
  เช่น โรคหายากและโรคที่ถูกละเลย ชีววิทยาเชิงทดลอง วิทยาศาสตร์วัสดุ
  และความยั่งยืน
- **การจำลองและการโต้ตอบ**: ใช้โมเดลภาษาขนาดใหญ่เพื่อ
  ตรวจสอบการโต้ตอบใหม่ๆ ในสาขา AI แบบฝังตัว การโต้ตอบรอบข้าง
  หุ่นยนต์ และการโต้ตอบระหว่างมนุษย์กับคอมพิวเตอร์
- **ความสามารถที่เกิดขึ้นใหม่**: การสำรวจความสามารถด้าน Agentic AI ใหม่ที่จำเป็นต่อการปรับปรุงการให้เหตุผลและการวางแผน รวมถึงวิธีขยายความสามารถระหว่างการอนุมาน (เช่น โดยใช้ Gemini Flash)
- **การโต้ตอบและการทำความเข้าใจแบบมัลติโมดัล**: ระบุช่องว่างและโอกาสสำหรับโมเดลพื้นฐานแบบมัลติโมดัลเพื่อการวิเคราะห์ การให้เหตุผล และการวางแผนในงานต่างๆ

การมีสิทธิ์: เฉพาะบุคคลธรรมดา (คณาจารย์ นักวิจัย หรือเทียบเท่า)
ที่สังกัดสถาบันการศึกษาหรือองค์กรวิจัยทางวิชาการที่ถูกต้อง
เท่านั้นที่จะสมัครได้ โปรดทราบว่า Google จะเป็นผู้พิจารณาให้สิทธิ์เข้าถึง API และเครดิต รวมถึงการนำสิทธิ์เข้าถึงและเครดิตออก
เราตรวจสอบใบสมัครเป็นรายเดือน

### เริ่มค้นคว้าด้วย Gemini API

[สมัครเลย](https://forms.gle/HMviQstU8PxC5iCt5)

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-22 UTC

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-22 UTC"],[],[]]
