---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th
fetched_at: 2026-07-27T04:34:45.443399+00:00
title: "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e41\u0e25\u0e30\u0e0a\u0e38\u0e14\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บันทึกและชุดข้อมูล

ในคู่มือนี้ คุณจะได้เรียนรู้วิธีดูบันทึกจากการใช้งาน Gemini API ในแดชบอร์ด Google AI Studio เพื่อทำความเข้าใจพฤติกรรมของโมเดลและวิธีที่ผู้ใช้อาจโต้ตอบกับแอปพลิเคชันของคุณได้ดียิ่งขึ้น ใช้การบันทึกเพื่อสังเกต แก้ไขข้อบกพร่อง และ *แชร์ความคิดเห็นเกี่ยวกับการใช้งาน
กับ Google เพื่อช่วยปรับปรุง Gemini ใน Use Case ของนักพัฒนาซอฟต์แวร์ (ไม่บังคับ)*[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=th)

ระบบรองรับการเรียก API ทั้งหมดของ `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` และการเรียก API ของ [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=th) ยกเว้น Agent ที่ได้รับการจัดการ ซึ่งรวมถึงการเรียกที่ทำผ่าน
[ปลายทางความเข้ากันได้ของ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)

## กำหนดค่าการบันทึกโปรเจ็กต์

โดยค่าเริ่มต้น API จะจัดเก็บออบเจ็กต์การโต้ตอบทั้งหมด (`store=true`) เพื่อลดความซับซ้อนในการใช้ฟีเจอร์การจัดการสถานะฝั่งเซิร์ฟเวอร์ ในทางตรงกันข้าม Generate Content API จะไม่จัดเก็บคำขอโดยค่าเริ่มต้น และต้องเปิดใช้การจัดเก็บต่อคำขอหรือที่ระดับโปรเจ็กต์จาก AI Studio

ใน Google [AI Studio](https://aistudio.google.com/logs?hl=th) คุณสามารถเปิดหรือ
ปิดใช้การบันทึกสำหรับโปรเจ็กต์ทั้งหมดหรือโปรเจ็กต์ที่เฉพาะเจาะจง และเปลี่ยนการตั้งค่าเหล่านี้ได้ทุกเมื่อผ่านแผง**การตั้งค่า** ในหน้า
[บันทึกและชุดข้อมูล](https://aistudio.google.com/logs?hl=th) คุณสามารถเปิดหรือปิดใช้การบันทึก
แยกกันสำหรับ API `generateContent` และ
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=th) API
เพื่อเปลี่ยนลักษณะการทำงานของการจัดเก็บเริ่มต้นสำหรับโปรเจ็กต์

### การบันทึกระดับคำขอ

ลักษณะการทำงานของการจัดเก็บและการบันทึกจะแตกต่างกันไปตาม API ดังนี้

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th):** จัดเก็บคำขอโดยค่าเริ่มต้น (`store=true`) เพื่อลดความซับซ้อนในการจัดการสถานะฝั่งเซิร์ฟเวอร์
- **Generate Content API (`generateContent`):** ไม่จัดเก็บคำขอโดยค่าเริ่มต้น (`store=false`)

วิธีตั้งค่าพร็อพเพอร์ตี้ `store`

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## ดูบันทึกโปรเจ็กต์ใน AI Studio

1. ไปที่หน้าบันทึกใน [AI Studio](https://aistudio.google.com/logs?hl=th)
2. เลือกโปรเจ็กต์จากเมนูแบบเลื่อนลง
3. บันทึกจะปรากฏในตารางตามลำดับเวลาแบบย้อนกลับสำหรับ Interactions API หากมี
4. หากต้องการดูบันทึกโปรเจ็กต์สำหรับ Generate Content API ให้เปิดใช้ API นี้ใน[แผงการตั้งค่า](#configure-logging)ก่อน

คลิกรายการเพื่อดูตัวอย่างเพย์โหลด คุณสามารถตรวจสอบพรอมต์และการตอบกลับแบบเต็มจาก Gemini รวมถึงบริบทจากรอบก่อนหน้าได้ สำหรับคำขอ **Interactions API** บันทึกจะมีลิงก์โดยตรงไปยัง `previous_interaction_id` ด้วย

## กำหนดค่าการเก็บรักษาพื้นที่เก็บข้อมูลของโปรเจ็กต์

บันทึกจะหมดอายุและถูกทำเครื่องหมายว่าให้ลบหลังจากผ่านกรอบเวลาการเก็บรักษาเริ่มต้น
55 วัน (เว้นแต่จะ[บันทึกลงในชุดข้อมูล](#create) ซึ่งจะไม่มีวันหมดอายุ)
คุณสามารถกำหนดค่ากรอบเวลาการเก็บรักษาบันทึกของโปรเจ็กต์เป็น 7, 14, 28 หรือสูงสุด 55 วัน

## สร้างและแชร์ชุดข้อมูล

คุณสามารถบันทึกบันทึกลงในชุดข้อมูลเพื่อจัดระเบียบและส่งออกบันทึกได้อย่างมีประสิทธิภาพมากขึ้น

- จากหน้า [บันทึก](https://aistudio.google.com/logs?hl=th) ให้ค้นหาแถบตัวกรอง
  ที่ด้านบนเพื่อเลือกพร็อพเพอร์ตี้ที่จะใช้กรอง
- จากมุมมองที่กรองแล้ว ให้ใช้ช่องทำเครื่องหมายเพื่อเลือกบันทึกทั้งหมดหรือบันทึกแต่ละรายการ
- คลิกปุ่ม**สร้างชุดข้อมูล** ที่ปรากฏที่ด้านบนของรายการ
- ตั้งชื่อและใส่คำอธิบาย (ไม่บังคับ) ให้กับชุดข้อมูลใหม่
- คุณจะเห็นชุดข้อมูลที่สร้างขึ้นพร้อมชุดบันทึกที่คัดสรรแล้ว
- ส่งออกชุดข้อมูลเพื่อวิเคราะห์เพิ่มเติมเป็นไฟล์ CSV, JSONL หรือไปยัง Google ชีต

ชุดข้อมูลมีประโยชน์สำหรับ Use Case ที่แตกต่างกันหลายกรณี

- **ดูแลจัดการชุดภารกิจ:** ขับเคลื่อนการปรับปรุงในอนาคตที่มุ่งเน้นไปยังส่วนที่คุณต้องการให้ AI ปรับปรุง
- **คัดสรรชุดตัวอย่าง:** เช่น ตัวอย่างจากการใช้งานจริงเพื่อสร้างการตอบกลับจากโมเดลอื่น หรือคอลเล็กชันของกรณีที่พบได้ยากสำหรับการตรวจสอบตามปกติก่อนการใช้งาน
- **ชุดการประเมิน:** ชุดที่แสดงถึงการใช้งานจริงในความสามารถที่สำคัญ เพื่อใช้เปรียบเทียบกับโมเดลอื่นๆ หรือการทำซ้ำคำแนะนำของระบบ

คุณสามารถมีส่วนร่วมในการวิจัยและพัฒนา Gemini ได้โดยเลือกแชร์ชุดข้อมูลกับ Google เป็นตัวอย่างการสาธิต

## ข้อจำกัด

ปัจจุบันระบบยังไม่รองรับการบันทึกสำหรับรายการต่อไปนี้

- โมเดล Imagen และ Veo
- โมเดลการฝังของ Gemini
- โมเดล Gemini Robotics
- อินพุตที่มีวิดีโอ, GIF หรือ PDF
- Agent รุ่นพับลิกเบต้าใน Gemini API

## ขั้นตอนถัดไป

- **สร้างต้นแบบด้วยประวัติเซสชัน:** ใช้ [AI Studio Build](https://aistudio.google.com/apps?hl=th) เพื่อสร้างแอปโค้ดและเพิ่มคีย์ API เพื่อเปิดใช้ประวัติบันทึก Gemini API สำหรับฟีเจอร์ AI
- **เรียกใช้บันทึกอีกครั้งด้วย Gemini Batch API:** ใช้ชุดข้อมูลสำหรับการสุ่มตัวอย่างการตอบกลับ
  และการประเมินโมเดลหรือตรรกะของแอปพลิเคชันโดยการเรียกใช้บันทึกอีกครั้งด้วย
  [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-22 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-22 UTC"],[],[]]
