---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=th
fetched_at: 2026-10-26T05:46:46.351305+00:00
title: "\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ภาพรวมของตัวแทน

Agent ที่ได้รับการจัดการใน Gemini API จะช่วยให้คุณมีชุดเครื่องมือ Agent ที่กำหนดค่าได้
การเรียก API ครั้งเดียวจะจัดสรรแซนด์บ็อกซ์ Linux ที่เอเจนต์ใช้ในการให้เหตุผล
รันโค้ด จัดการไฟล์ และท่องเว็บโดยอัตโนมัติ

[rocket\_launch

คู่มือเริ่มใช้งานฉบับย่อ

โทรหา Agent รายการแรก สตรีมคำตอบ และสร้าง Agent ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)
[smart\_toy

Agent ของ Antigravity

ความสามารถ เครื่องมือ อินพุตมัลติโมดัล และราคาสำหรับเอเจนต์เริ่มต้น](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)
[experiment

Agent ใน AI Studio

พื้นที่ทดลองแบบภาพสำหรับการสร้างต้นแบบเอเจนต์โดยไม่ต้องเขียนโค้ด](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=th)

## Agent ที่มีการจัดการที่พร้อมใช้งาน

- **[Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)**: Agent แบบจัดการอเนกประสงค์
  ที่สร้างขึ้นด้วย Gemini 3.8 Flash เรียกใช้โค้ด จัดการไฟล์ และ
  ค้นหาเว็บภายในแซนด์บ็อกซ์ Linux ที่ปลอดภัยซึ่งโฮสต์โดย Google คุณสามารถ
  กำหนดค่าโมเดลพื้นฐาน (เช่น Gemini 3.6 Flash หรือ Gemini 3.5
  Flash-Lite) โดยใช้ `agent_config` และขยายโมเดลด้วยคำสั่ง ทักษะ และข้อมูลของคุณเองเพื่อ[สร้างเอเจนต์ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th)
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)**: Agent การค้นคว้าข้อมูลแบบอัตโนมัติ ที่วางแผน ดำเนินการ และสังเคราะห์งานค้นคว้าข้อมูลแบบหลายขั้นตอนสำหรับกรณีการใช้งาน เช่น การวิเคราะห์ตลาด การสอบทานธุรกิจ และการทบทวนวรรณกรรม

## ความปลอดภัยและแนวทางปฏิบัติแนะนำ

เอเจนต์ทุกตัวจะทำงานในสภาพแวดล้อมแซนด์บ็อกซ์ที่แยกกันในระดับระบบปฏิบัติการ
แซนด์บ็อกซ์มีการเข้าถึงเครือข่ายขาออกแบบไม่จำกัดโดยค่าเริ่มต้น คุณ
จำกัดหรือปิดใช้การเข้าถึงเครือข่ายได้โดยใช้รายการที่อนุญาต

### การเข้าถึงเครือข่าย

โดยค่าเริ่มต้น สภาพแวดล้อมจะมีสิทธิ์เข้าถึงเครือข่ายขาออกแบบไม่จำกัด ใช้`network`รายการที่อนุญาตเพื่อจำกัดการเข้าชมขาออกไปยังโดเมนที่เฉพาะเจาะจงหรือ
รูปแบบไวลด์การ์ด โปรดดูรายละเอียดการกำหนดค่าที่
[รายการที่อนุญาตของเครือข่าย](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=th#network_allow_list) (AI
Studio) หรือ[กฎเครือข่าย](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th#with_network_rules)
(API)

### เครื่องมือและ API ภายนอก

คุณเชื่อมต่อเครื่องมือและ API ภายนอกเพื่อขยายความสามารถของเอเจนต์ได้ ใช้เฉพาะเครื่องมือจากแหล่งที่มาที่เชื่อถือได้และกำหนดขอบเขตสิทธิ์ให้ต่ำที่สุดเท่าที่จำเป็น จัดเก็บ
ข้อมูลลับเป็นข้อมูลเข้าสู่ระบบที่มีการจัดการและอ้างอิงตามรหัส เพื่อให้พร็อกซีขาออก
แทรกข้อมูลลับเหล่านั้นในเวลาที่ส่งคำขอและไม่แสดงข้อมูลลับภายในแซนด์บ็อกซ์
เอเจนต์อาจใช้ข้อมูลเข้าสู่ระบบใดก็ได้ที่เข้าถึงได้ ดังนั้นโปรดระบุเฉพาะข้อมูลเข้าสู่ระบบที่มี
ขอบเขตทั้งหมดที่คุณยินดีให้สิทธิ์

- ใช้บัญชีบริการหรือคีย์ API ที่มีสิทธิ์น้อยที่สุด
- เลือกใช้โทเค็นที่มีอายุสั้นแทนคีย์ที่มีอายุยาว
- โปรดระบุเฉพาะข้อมูลเข้าสู่ระบบที่คุณยินดีให้สิทธิ์ขอบเขตทั้งหมด
- หมุนเวียนข้อมูลเข้าสู่ระบบตามกำหนดการปกติ

ดูประเภทข้อมูลเข้าสู่ระบบและการดำเนินการจัดการได้ที่
[ข้อมูลเข้าสู่ระบบ](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=th) นอกจากนี้ คุณยังตั้งค่าส่วนหัว
แบบอินไลน์ในกฎรายการที่อนุญาตได้ด้วย โปรดดู[การกำหนดค่า
เครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration)

### การควบคุมดูแลโดยเจ้าหน้าที่

โปรดตรวจสอบเอาต์พุต (โค้ดที่สร้างขึ้น การเปลี่ยนรูปแบบข้อมูล การเปลี่ยนแปลงการกำหนดค่า) ทุกครั้งก่อนที่จะนําไปใช้ โดยเฉพาะอย่างยิ่งสําหรับงานที่แก้ไขข้อมูลหรือโต้ตอบกับระบบภายนอก

## ราคา

Agent ที่ได้รับการจัดการใช้[โมเดลแบบจ่ายเมื่อใช้](https://ai.google.dev/gemini-api/docs/pricing?hl=th#pricing-for-agents)
ตามโทเค็นโมเดล Gemini และการใช้เครื่องมือ การโต้ตอบครั้งเดียวสามารถทริกเกอร์ลูปการให้เหตุผลหลายลูป ซึ่งโดยปกติจะใช้โทเค็น 100, 000 ถึง 3 ล้านโทเค็น ระบบ**จะไม่เรียกเก็บเงิน**ค่าคอมพิวเตอร์ของสภาพแวดล้อมในระหว่างเวอร์ชันตัวอย่าง ดูรายละเอียดค่าใช้จ่ายต่อชิ้นงานได้ที่[ค่าใช้จ่ายโดยประมาณ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#availability-and-pricing)
นอกจากนี้ Agent ที่ได้รับการจัดการยังพร้อมให้บริการในรุ่นฟรีด้วยการจำกัดอัตราคำขอและโควต้าการใช้งานฟรี

## จำกัดสูงสุด

| ขีดจำกัด | คำอธิบาย |
| --- | --- |
| **อายุการใช้งานของสภาพแวดล้อม** | ระบบจะลบสภาพแวดล้อมอย่างถาวรหลังจากไม่มีการใช้งานเป็นเวลา 7 วัน |
| **การปิด VM** | VM จะปิดหลังจากไม่มีการใช้งานเป็นระยะเวลาสั้นๆ เพื่อประหยัดทรัพยากร คำขอถัดไปจะคืนค่าสถานะ (ด้วย Cold Start) |
| **ซอฟต์แวร์ที่ติดตั้งไว้ล่วงหน้า** | สภาพแวดล้อมที่ใช้ Ubuntu พร้อม Python 3.12 และ Node.js 22 ดูข้อมูลเพิ่มเติมเกี่ยวกับรูปภาพฐานของสภาพแวดล้อมได้ที่[ซอฟต์แวร์ที่ติดตั้งไว้ล่วงหน้า](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#pre-installed-software) |
| **Max agents** | คุณมีตัวแทนที่มีการจัดการได้สูงสุด 1,000 ราย |

## เฟรมเวิร์กของ Agent

นอกจากนี้ คุณยังสร้างเอเจนต์ด้วย Gemini โดยใช้เฟรมเวิร์กและ SDK ต่อไปนี้ได้ด้วย

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=th): สร้าง
  โฟลว์แอปพลิเคชันที่ซับซ้อนแบบมีสถานะและระบบ Multi-Agent โดยใช้โครงสร้างกราฟ
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=th): เชื่อมต่อเอเจนต์ Gemini กับ
  ข้อมูลส่วนตัวของคุณสำหรับเวิร์กโฟลว์ที่ได้รับการปรับปรุงด้วย RAG
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=th): จัดระเบียบ AI Agent แบบอัตโนมัติที่ทำงานร่วมกันและสวมบทบาท
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=th): สร้าง
  อินเทอร์เฟซผู้ใช้และเอเจนต์ที่ทำงานด้วยระบบ AI ใน JavaScript/TypeScript
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): เฟรมเวิร์กโอเพนซอร์สสําหรับสร้างและจัดระเบียบเอเจนต์ AI ที่ทํางานร่วมกันได้
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=th): สร้าง
  AI Agent ที่ทำงานได้เองโดยใช้เครื่องมือ, ลูปของ Agent และการจัดการบริบทเดียวกัน
  ที่ขับเคลื่อน Google Antigravity ซึ่งตั้งโปรแกรมใน Python ได้

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-09 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-09 UTC"],[],[]]
