---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=th
fetched_at: 2026-08-10T03:25:57.245462+00:00
title: "\u0e41\u0e01\u0e49\u0e1b\u0e31\u0e0d\u0e2b\u0e32 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# แก้ปัญหา Google AI Studio

หน้านี้มีคำแนะนำในการแก้ปัญหา Google AI Studio หากคุณพบปัญหา

## ทำความเข้าใจข้อผิดพลาด 403 การเข้าถึงถูกจำกัด

หากเห็นข้อผิดพลาด 403 การเข้าถึงถูกจำกัด แสดงว่าคุณใช้ Google AI Studio ในลักษณะที่ไม่เป็นไปตาม[ข้อกำหนดในการให้บริการ](https://ai.google.dev/terms?hl=th) สาเหตุที่พบบ่อยอย่างหนึ่งคือ
คุณไม่ได้อยู่ใน[ภูมิภาคที่รองรับ](https://ai.google.dev/available_regions?hl=th)

## แก้ไขการตอบกลับที่ไม่มีเนื้อหาใน Google AI Studio

ข้อความwarning **ไม่มีเนื้อหา** จะปรากฏใน
Google AI Studio หากเนื้อหาถูกบล็อกด้วยเหตุผลใดก็ตาม หากต้องการดูรายละเอียดเพิ่มเติม
ให้วางตัวชี้เหนือ **ไม่มีเนื้อหา** แล้วคลิก
warning **ความปลอดภัย**

หากการตอบกลับถูกบล็อกเนื่องจากการตั้งค่า[ความปลอดภัย](https://ai.google.dev/docs/safety_setting?hl=th) และ
คุณพิจารณา[ความเสี่ยงด้านความปลอดภัย](https://ai.google.dev/docs/safety_guidance?hl=th)สำหรับกรณีการใช้งานแล้ว คุณ
สามารถแก้ไข
[การตั้งค่าความปลอดภัย](https://ai.google.dev/docs/safety_setting?hl=th#safety_settings_in_makersuite)
เพื่อส่งผลต่อการตอบกลับที่แสดง

หากการตอบกลับถูกบล็อกแต่ไม่ใช่เนื่องจากการตั้งค่าความปลอดภัย แสดงว่าคําค้นหาหรือ
การตอบกลับอาจละเมิด[ข้อกำหนดในการให้บริการ](https://ai.google.dev/terms?hl=th)หรือไม่ได้รับการรองรับ

## ตรวจสอบการใช้โทเค็นและขีดจำกัด

เมื่อคุณเปิดพรอมต์ไว้ ปุ่ม**แสดงตัวอย่างข้อความ** ที่ด้านล่างของหน้าจอจะแสดงโทเค็นปัจจุบันที่ใช้สำหรับเนื้อหาของพรอมต์และจำนวนโทเค็นสูงสุดสำหรับโมเดลที่ใช้

## สิทธิ์ Google Cloud IAM สำหรับ AI Studio

สมาชิกของโปรเจ็กต์ Google Cloud ต้องมีสิทธิ์ Identity and Access Management (IAM) ที่เฉพาะเจาะจงเพื่อดำเนินการใน Google AI Studio ดูข้อมูลเพิ่มเติมเกี่ยวกับข้อมูลประจำตัวเหล่านี้ได้ที่[ภาพรวมของพรินซิเพิล IAM](https://cloud.google.com/iam/docs/principals?hl=th)

ผู้ใช้ที่มีบทบาท**ผู้แก้ไข** หรือ**เจ้าของ** ในโปรเจ็กต์ Google Cloud ที่เชื่อมโยงจะมีสิทธิ์เต็มรูปแบบในการดูแดชบอร์ดและจัดการคีย์ Gemini API ผู้ใช้ที่มีบทบาท**ผู้มีสิทธิ์ดู** จะดูแดชบอร์ดและคีย์ API ได้ แต่จะสร้าง อัปเดต หรือลบไม่ได้

หากต้องการควบคุมแบบละเอียดมากขึ้น โปรดดูตารางต่อไปนี้เพื่อดูสิทธิ์เฉพาะที่จำเป็นสำหรับฟีเจอร์แต่ละรายการของ AI Studio ดูวิธีการให้สิทธิ์เหล่านี้ได้ที่[การให้ เปลี่ยน และเพิกถอนสิทธิ์เข้าถึงทรัพยากร](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=th)ในเอกสารประกอบของ Google Cloud

| ฟีเจอร์ AI Studio | สิทธิ์ IAM ที่จำเป็น | ข้อกำหนดเพิ่มเติม |
| --- | --- | --- |
| **ค้นหาโปรเจ็กต์** (นำเข้าโปรเจ็กต์) | `resourcemanager.projects.get` |  |
| **เปลี่ยนชื่อโปรเจ็กต์** | `resourcemanager.projects.update` |  |
| **แสดงระดับโควต้า** | ไม่มี |  |
| **สร้างคีย์ API** | มีสิทธิ์**ค้นหาโปรเจ็กต์** และมีสิทธิ์ต่อไปนี้  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **แสดงรายการคีย์ API** | มีสิทธิ์**ค้นหาโปรเจ็กต์** และมีสิทธิ์ต่อไปนี้  `apikeys.keys.list` `serviceusage.services.get` | โปรเจ็กต์ Google Cloud ต้องเปิดใช้ [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=th) |
| **เปลี่ยนชื่อคีย์ API** | `apikeys.keys.update` |  |
| **ลบคีย์ API** | `apikeys.keys.delete` |  |
| **แดชบอร์ดการใช้งาน** | มีสิทธิ์**ค้นหาโปรเจ็กต์** และมีสิทธิ์ต่อไปนี้  `monitoring.timeSeries.list` |  |
| **แดชบอร์ดการจำกัดอัตรา** | มีสิทธิ์**แดชบอร์ดการใช้งาน** และมีสิทธิ์ต่อไปนี้  `cloudquotas.quotas.get` |  |
| **ค่าใช้จ่าย (ขีดจำกัดการเรียกเก็บเงิน)** | `billing.resourceCosts.get` (เพื่อดูค่าใช้จ่าย) `billing.resourcebudgets.read` (เพื่อดูขีดจำกัด) `billing.resourcebudgets.write` (เพื่อกำหนดขีดจำกัด) |  |
| **แดชบอร์ดการเรียกเก็บเงิน** | `billing.accounts.get` |  |

### การตรวจสอบสิทธิ์เข้าถึงอื่นๆ

นอกเหนือจากสิทธิ์ Google Cloud IAM แล้ว AI Studio ยังทำการตรวจสอบความปลอดภัยและการปฏิบัติตามข้อกำหนดด้วย คุณอาจพบข้อผิดพลาด `PERMISSION_DENIED` หรือข้อผิดพลาดการจำกัดการเข้าถึงในอินเทอร์เฟซ AI Studio หรือในการตอบกลับของ API หากไม่เป็นไปตามข้อกำหนดต่อไปนี้

- **การตรวจสอบความปลอดภัย:** คำขอของคุณต้องผ่านการตรวจสอบความปลอดภัยอัตโนมัติ
- **ข้อกำหนดในการให้บริการ:** คุณต้องยอมรับข้อกำหนดในการให้บริการของ Google และข้อกำหนดในการให้บริการเพิ่มเติมของ Generative AI
- **ภูมิภาคที่รองรับ:** คุณต้องอยู่ใน[ภูมิภาคที่รองรับ](https://ai.google.dev/gemini-api/docs/available-regions?hl=th)
- **ความน่าเชื่อถือและความปลอดภัย:** โปรเจ็กต์ Google Cloud ต้องไม่ถูกตั้งค่าสถานะว่ามีการละเมิด

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-29 UTC"],[],[]]
