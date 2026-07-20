---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=th
fetched_at: 2026-07-20T04:45:01.609664+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e44\u0e14\u0e49\u0e08\u0e32\u0e01 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำให้ใช้งานได้จาก Google AI Studio

Google AI Studio ช่วยให้คุณสามารถทําให้แอปพลิเคชัน Full Stack ใช้งานได้โดยตรง
จากโหมดสร้าง ซึ่งช่วยให้เปลี่ยนจากต้นแบบไปสู่
สภาพแวดล้อมการผลิตที่มีการจัดการและปรับขนาดได้ได้อย่างรวดเร็ว

## ตัวเลือกการติดตั้งใช้งาน

หากต้องการติดตั้งใช้งานแอปพลิเคชันจากโหมด AI Studio Build ข้อกำหนดจะขึ้นอยู่กับระดับที่คุณใช้ ดังนี้

- [**ระดับเริ่มต้นของ Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=th):
  ช่วยให้คุณเผยแพร่แอปพลิเคชันแบบฟูลสแต็กได้สูงสุด 2 รายการโดยไม่ต้องตั้งค่า
  โปรเจ็กต์ Google Cloud หรือบัญชีสำหรับการเรียกเก็บเงิน
- **การติดตั้งใช้งานมาตรฐาน**: ต้องมีโปรเจ็กต์ Google Cloud ที่ลิงก์กับบัญชี AI Studio และเปิดใช้การเรียกเก็บเงินในโปรเจ็กต์นั้น

## เกี่ยวกับ Starter Tier

Google Cloud Starter Tier มีเส้นทางที่คล่องตัวในการทำให้แอปพลิเคชันใช้งานได้ใน Google Cloud โดยตรงจาก Google AI Studio โดยไม่ต้องตั้งค่าสภาพแวดล้อม Google Cloud แบบเต็มหรือบัญชีสำหรับการเรียกเก็บเงิน

การทำให้ใช้งานได้แต่ละครั้งใน Google AI Studio จะสร้างบริการที่เกี่ยวข้องใน
Cloud Run สำหรับบริการที่ใช้งานใน Google AI Studio ด้วย Starter
Tier จะมีข้อจำกัดต่อไปนี้

- คุณสามารถติดตั้งใช้งานบริการได้สูงสุด 2 รายการ
- ระบบจะทําให้บริการของคุณใช้งานได้ใน[ภูมิภาค Cloud Run เดียว](https://docs.cloud.google.com/run/docs/locations?hl=th)

## ขั้นตอนการติดตั้งใช้งาน Starter Tier

หลังจากออกแบบแอปในโหมดสร้างแล้ว ให้ทำให้แอปใช้งานได้ด้วย Starter Tier โดยทำดังนี้

1. คลิกปุ่ม**เผยแพร่**ที่มุมขวาบน
2. คลิก**เริ่มต้น**
3. คลิก**เผยแพร่แอป**

เมื่อการติดตั้งใช้งานเสร็จสมบูรณ์แล้ว AI Studio จะให้ URL ของ Cloud Run ซึ่งคุณสามารถใช้เพื่อเข้าถึงแอปพลิเคชันที่ใช้งานจริงได้

## URL ที่กำหนดเองสำหรับ AI Studio

เมื่อเผยแพร่แอปพลิเคชันจาก Google AI Studio คุณจะตั้งค่าโดเมนย่อยที่กำหนดเองและจดจำง่ายได้ในส่วน `ai.studio` (เช่น `https://your-app-name.ai.studio`)

Google AI Studio กำหนดให้โดเมนย่อยต้องไม่ซ้ำกันทั่วโลกในทุกโปรเจ็กต์
และจะกำหนดโดเมนย่อยตามลำดับการลงทะเบียน หากโปรเจ็กต์อื่น
ใช้ชื่ออยู่แล้ว AI Studio จะแจ้งให้คุณเลือกชื่ออื่น หากคุณ
เลิกเผยแพร่หรือลบแอปพลิเคชัน ระบบจะปล่อย URL แบบกำหนดเองของแอปพลิเคชันนั้นและ
เปิดให้ผู้ใช้รายอื่นอ้างสิทธิ์ได้

### ตั้ง URL ที่กำหนดเอง

วิธีตั้งค่าหรืออัปเดต URL ที่กำหนดเองสำหรับแอปพลิเคชัน

1. เปิดแอปพลิเคชันใน Google AI Studio ในโหมด**สร้าง**
2. คลิก**เผยแพร่**ที่มุมขวาบน
3. ในการกำหนดค่าการติดตั้งใช้งาน ให้ป้อนโดเมนย่อยที่ต้องการในช่อง **URL ที่กำหนดเอง** หรือยอมรับ URL ที่แนะนำ
4. คลิก**เผยแพร่แอป**

หากต้องการโอน URL ที่กำหนดเองที่มีอยู่ไปยังแอปพลิเคชันอื่น คุณต้องเลิกเผยแพร่หรือลบแอปพลิเคชันที่กำหนด URL ที่กำหนดเองนั้นก่อน แล้วจึงเผยแพร่แอปพลิเคชันใหม่โดยใช้โดเมนย่อยที่เลือก

### รายงานปัญหาเกี่ยวกับเครื่องหมายการค้าหรือลิขสิทธิ์

โดเมนย่อยที่กำหนดเองต้องเป็นไปตาม[ข้อกำหนดในการให้บริการของ Google](https://policies.google.com/terms?hl=th) หากพบ
URL ที่กำหนดเองซึ่งละเมิดเครื่องหมายการค้าหรือใช้ชื่อที่มีลิขสิทธิ์โดยไม่ได้รับ
อนุญาต คุณสามารถรายงานได้โดยใช้[เครื่องมือแก้ปัญหาทางกฎหมายของ Google](https://support.google.com/legal/troubleshooter/1114905?hl=th)

## การติดตั้งใช้งานมาตรฐาน

เมื่อแอปพลิเคชันของคุณพัฒนาขึ้น คุณอาจต้องใช้ความสามารถที่นอกเหนือจากระดับ Starter
Tier เช่น โควต้าที่สูงขึ้น ทรัพยากรการประมวลผลที่เพิ่มขึ้น หรือผลิตภัณฑ์อื่นๆ ของ
Google Cloud ที่ไม่มีให้บริการในระดับ Starter Tier หากต้องการปลดล็อก
ความสามารถเหล่านี้ คุณสามารถแปลงโปรเจ็กต์ระดับเริ่มต้นที่มีการจัดการเต็มรูปแบบเป็น
โปรเจ็กต์ Google Cloud มาตรฐานได้

ซึ่งจะช่วยให้คุณปรับขนาดได้อย่างราบรื่นโดยไม่สูญเสีย
ความคืบหน้า ทำตามขั้นตอนเพื่อ
[สร้างบัญชีสำหรับการเรียกเก็บเงินใน Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=th#create-new-billing-account)
ยอมรับข้อกำหนดในการให้บริการมาตรฐานของ Google Cloud อย่างเป็นทางการ และ
[อัปเกรดเป็นโปรเจ็กต์ Google Cloud มาตรฐาน](https://docs.cloud.google.com/docs/starter-tier?hl=th#upgradee)
ดูข้อมูลเพิ่มเติมได้ที่
[การตั้งค่าสำหรับบัญชีแบบชำระเงิน](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=th#paid-setup)

ดูข้อมูลเพิ่มเติมเกี่ยวกับระดับการเรียกเก็บเงินได้ที่[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)

## ลบแอปพลิเคชัน

หากไม่ต้องการใช้แอปแล้ว คุณสามารถลบแอปใน Google AI Studio ได้
โดยทำตามวิธีการต่อไปนี้

1. ไปที่[หน้าแอป](https://aistudio.google.com/app/apps?hl=th)ใน Google AI Studio
2. เลือก**แอป**ในเมนูด้านซ้าย
3. วางเคอร์เซอร์เหนือแอปที่ต้องการลบ
4. คลิกไอคอนถังขยะทางด้านขวาของแถวเพื่อลบแอป

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับ
  [รุ่นเริ่มต้นของ Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=th)
- อ่านเกี่ยวกับ[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)ใน Gemini API

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-10 UTC"],[],[]]
