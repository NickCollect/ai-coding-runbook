---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th
fetched_at: 2026-10-26T05:42:19.201184+00:00
title: "\u0e42\u0e17\u0e40\u0e04\u0e47\u0e19\u0e0a\u0e31\u0e48\u0e27\u0e04\u0e23\u0e32\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# โทเค็นชั่วคราว

โทเค็นชั่วคราวคือโทเค็นการตรวจสอบสิทธิ์ที่มีอายุสั้นสำหรับเข้าถึง Gemini API ผ่าน [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) โดยได้รับการออกแบบมาเพื่อเพิ่มความปลอดภัยเมื่อคุณเชื่อมต่อจากอุปกรณ์ของผู้ใช้ไปยัง API โดยตรง (การติดตั้งใช้งาน[ไคลเอ็นต์ไปยังเซิร์ฟเวอร์](https://ai.google.dev/gemini-api/docs/live?hl=th#implementation-approach))
โทเค็นชั่วคราวสามารถดึงข้อมูลจากแอปพลิเคชันฝั่งไคลเอ็นต์ เช่น เว็บเบราว์เซอร์หรือแอปบนอุปกรณ์เคลื่อนที่ ได้เช่นเดียวกับคีย์ API มาตรฐาน แต่เนื่องจากโทเค็นชั่วคราวจะหมดอายุอย่างรวดเร็วและอาจถูกจำกัด จึงช่วยลดความเสี่ยงด้านความปลอดภัยในสภาพแวดล้อมฮาร์ดแวร์และซอฟต์แวร์ได้อย่างมาก คุณควรใช้เมื่อเข้าถึง Live API โดยตรงจากแอปพลิเคชันฝั่งไคลเอ็นต์เพื่อเพิ่มความปลอดภัยของคีย์ API

## วิธีการทำงานของโทเค็นชั่วคราว

โทเค็นชั่วคราวทำงานในระดับสูงดังนี้

1. ไคลเอ็นต์ (เช่น เว็บแอป) จะตรวจสอบสิทธิ์กับแบ็กเอนด์
2. แบ็กเอนด์ของคุณขอโทเค็นชั่วคราวจากบริการจัดสรรของ Gemini API
3. Gemini API จะออกโทเค็นที่มีอายุสั้น
4. แบ็กเอนด์จะส่งโทเค็นไปยังไคลเอ็นต์สำหรับการเชื่อมต่อ WebSocket ไปยัง Live
   API คุณทำได้โดยการสลับคีย์ API กับโทเค็นชั่วคราว
5. จากนั้นไคลเอ็นต์จะใช้โทเค็นราวกับว่าเป็นคีย์ API

![ภาพรวมของโทเค็นชั่วคราว](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=th)

ซึ่งจะช่วยเพิ่มความปลอดภัยเนื่องจากโทเค็นมีอายุสั้นแม้ว่าจะมีการดึงข้อมูลออกมา
ซึ่งแตกต่างจากคีย์ API ที่มีอายุยาวนานซึ่งติดตั้งใช้งานฝั่งไคลเอ็นต์ เนื่องจากไคลเอ็นต์ส่งข้อมูลไปยัง Gemini โดยตรง การดำเนินการนี้จึงช่วยปรับปรุงเวลาในการตอบสนองและหลีกเลี่ยงไม่ให้แบ็กเอนด์ต้องทำหน้าที่เป็นพร็อกซีข้อมูลแบบเรียลไทม์

## สร้างโทเค็นชั่วคราว

ต่อไปนี้เป็นตัวอย่างแบบง่ายๆ เกี่ยวกับวิธีรับโทเค็นชั่วคราวจาก Gemini
โดยค่าเริ่มต้น คุณจะมีเวลา 1 นาทีในการเริ่มเซสชัน Live API ใหม่โดยใช้โทเค็น
จากคำขอนี้ (`newSessionExpireTime`) และ 30 นาทีในการส่งข้อความผ่าน
การเชื่อมต่อดังกล่าว (`expireTime`)

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

ดูข้อจำกัดของค่า `expireTime` ค่าเริ่มต้น และข้อกำหนดอื่นๆ ของฟิลด์ได้ที่[เอกสารอ้างอิง API](https://ai.google.dev/api/live?hl=th#ephemeral-auth-tokens)
ภายใน`expireTime`กรอบเวลา คุณจะต้อง
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=th#session-resumption)
เชื่อมต่อการโทรอีกครั้งทุก 10 นาที (สามารถทำได้ด้วยโทเค็นเดียวกันแม้ว่า`uses: 1`)

นอกจากนี้ คุณยังล็อกโทเค็นชั่วคราวกับการกำหนดค่าชุดหนึ่งได้ด้วย ซึ่งอาจมีประโยชน์ในการปรับปรุงความปลอดภัยของแอปพลิเคชันเพิ่มเติมและเก็บคำสั่งของระบบไว้ที่ฝั่งเซิร์ฟเวอร์

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.8-live',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.8-live',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.8-live",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

นอกจากนี้ คุณยังล็อกฟิลด์บางส่วนได้ด้วย ดูข้อมูลเพิ่มเติมได้ใน[เอกสารประกอบ SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)

## เชื่อมต่อกับ Live API ด้วยโทเค็นชั่วคราว

เมื่อมีโทเค็นชั่วคราวแล้ว คุณจะใช้โทเค็นนั้นได้ราวกับเป็นคีย์ API (แต่โปรดทราบว่าโทเค็นนี้ใช้ได้กับ API ที่ใช้งานจริงเท่านั้น และใช้ได้กับ API เวอร์ชัน `v1beta` เท่านั้น)

การใช้โทเค็นชั่วคราวจะเพิ่มมูลค่าได้ก็ต่อเมื่อมีการติดตั้งใช้งานแอปพลิเคชัน
ที่ใช้แนวทาง[การติดตั้งใช้งานจากไคลเอ็นต์ไปยังเซิร์ฟเวอร์](https://ai.google.dev/gemini-api/docs/live?hl=th#implementation-approach)

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

ดูตัวอย่างเพิ่มเติมได้ที่[เริ่มต้นใช้งาน Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)

## แนวทางปฏิบัติแนะนำ

- กำหนดระยะเวลาหมดอายุสั้นๆ โดยใช้พารามิเตอร์ `expire_time`
- โทเค็นจะหมดอายุ ซึ่งต้องเริ่มกระบวนการจัดสรรใหม่
- ยืนยันการตรวจสอบสิทธิ์ที่ปลอดภัยสำหรับแบ็กเอนด์ของคุณเอง โทเค็นชั่วคราวจะ
  ปลอดภัยเท่ากับวิธีการตรวจสอบสิทธิ์แบ็กเอนด์เท่านั้น
- โดยทั่วไปแล้ว ให้หลีกเลี่ยงการใช้โทเค็นชั่วคราวสำหรับการเชื่อมต่อจากแบ็กเอนด์ไปยัง Gemini
  เนื่องจากโดยปกติแล้วเส้นทางนี้ถือว่าปลอดภัย

## ข้อจำกัด

ขณะนี้โทเค็นชั่วคราวใช้ได้กับ [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) เท่านั้น

## ขั้นตอนถัดไป

- อ่านข้อมูลเพิ่มเติมเกี่ยวกับโทเค็นชั่วคราวได้ใน[ข้อมูลอ้างอิง](https://ai.google.dev/api/live?hl=th#ephemeral-auth-tokens)ของ Live API

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-17 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-17 UTC"],[],[]]
