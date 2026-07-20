---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=th
fetched_at: 2026-07-20T04:47:45.237409+00:00
title: "\u0e44\u0e25\u0e1a\u0e23\u0e32\u0e23\u0e35 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ไลบรารี Gemini API

เมื่อสร้างด้วย Gemini API เราขอแนะนำให้ใช้ **Google GenAI SDK**
ซึ่งเป็นไลบรารีอย่างเป็นทางการที่พร้อมใช้งานจริงที่เราพัฒนาและดูแลรักษาสำหรับภาษาที่ได้รับความนิยมมากที่สุด โดยไลบรารีเหล่านี้พร้อมใช้งาน[ทั่วไป](https://ai.google.dev/gemini-api/docs/libraries?hl=th#new-libraries)และใช้ในเอกสารประกอบและตัวอย่างอย่างเป็นทางการทั้งหมดของเรา

หากเพิ่งเคยใช้ Gemini API ให้ทำตาม[คู่มือเริ่มต้นใช้งาน](https://ai.google.dev/gemini-api/docs/get-started?hl=th)เพื่อเริ่มใช้งาน

## ภาษาที่รองรับและการติดตั้ง

Google GenAI SDK พร้อมใช้งานสำหรับภาษา Python, JavaScript/TypeScript, Go และ Java คุณสามารถติดตั้งไลบรารีของแต่ละภาษาได้โดยใช้เครื่องมือจัดการแพ็กเกจ หรือไปที่ที่เก็บใน GitHub ของภาษาเหล่านั้นเพื่อดูข้อมูลเพิ่มเติม

### Python

- ไลบรารี: [`google-genai`](https://pypi.org/project/google-genai)
- ที่เก็บใน GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- การติดตั้ง: `pip install google-genai`

### JavaScript

- ไลบรารี: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- ที่เก็บใน GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- การติดตั้ง: `npm install @google/genai`

### Go

- ไลบรารี: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- ที่เก็บใน GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- การติดตั้ง: `go get google.golang.org/genai`

### Java

- ไลบรารี: `google-genai`
- ที่เก็บใน GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- การติดตั้ง: หากใช้ Maven ให้เพิ่มข้อมูลต่อไปนี้ลงในทรัพยากร Dependency

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- ไลบรารี: `Google.GenAI`
- ที่เก็บใน GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- การติดตั้ง: `dotnet add package Google.GenAI`

## เวอร์ชันสำหรับผู้ใช้ทั่วไป

ณ เดือนพฤษภาคม 2025 Google GenAI SDK พร้อมใช้งานทั่วไป (GA) ในทุกแพลตฟอร์มที่รองรับ และเป็นไลบรารีที่แนะนำสำหรับการเข้าถึง Gemini API
โดยไลบรารีเหล่านี้มีความเสถียร รองรับการใช้งานจริงอย่างเต็มที่ และได้รับการดูแลรักษาอย่างต่อเนื่อง
นอกจากนี้ยังให้สิทธิ์เข้าถึงฟีเจอร์ล่าสุดและมอบประสิทธิภาพที่ดีที่สุดในการทำงานร่วมกับ Gemini

หากคุณใช้ไลบรารีแบบเดิมของเรา ขอแนะนำอย่างยิ่งให้เปลี่ยนไปใช้ไลบรารีใหม่เพื่อให้เข้าถึงฟีเจอร์ล่าสุดและได้รับประสิทธิภาพที่ดีที่สุดในการทำงานร่วมกับ Gemini ดูข้อมูลเพิ่มเติมได้ในส่วน[ไลบรารีแบบเดิม](https://ai.google.dev/gemini-api/docs/libraries?hl=th#previous-sdks)

## ไลบรารีแบบเดิมและการเปลี่ยนไปใช้ไลบรารีใหม่

หากคุณใช้ไลบรารีแบบเดิมของเรา ขอแนะนำให้
[เปลี่ยนไปใช้ไลบรารีใหม่](https://ai.google.dev/gemini-api/docs/migrate?hl=th)

ไลบรารีแบบเดิมไม่ให้สิทธิ์เข้าถึงฟีเจอร์ล่าสุด (เช่น
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) และ [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)) และจะ
เลิกใช้งานในวันที่ 30 พฤศจิกายน 2025

สถานะการรองรับของไลบรารีแบบเดิมแต่ละรายการจะแตกต่างกันไปตามรายละเอียดในตารางต่อไปนี้

| ภาษา | ไลบรารีแบบเดิม | สถานะการรองรับ | ไลบรารีที่แนะนำ |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | `google.golang.org/genai` |
| **Dart และ Flutter** | `google_generative_ai` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | ใช้ [Genkit Dart](https://genkit.dev/docs/dart/get-started/) หรือ [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | ใช้ [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=th) |
| **Android** | `generative-ai-android` | ไม่ได้ดูแลรักษาอย่างต่อเนื่อง | ใช้ [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=th) |

**หมายเหตุสำหรับนักพัฒนาซอฟต์แวร์ Java:** ไม่มี Java SDK ที่ Google จัดหาให้แบบเดิมสำหรับ Gemini API คุณจึงไม่จำเป็นต้องเปลี่ยนจากไลบรารีของ Google เวอร์ชันก่อนหน้า คุณ
สามารถเริ่มต้นใช้งานไลบรารีใหม่ได้โดยตรงใน
[ส่วนภาษาที่รองรับและการติดตั้ง](#install)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-22 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-22 UTC"],[],[]]
