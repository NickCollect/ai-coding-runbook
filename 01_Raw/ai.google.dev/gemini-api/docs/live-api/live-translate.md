---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th
fetched_at: 2026-08-17T02:21:54.135265+00:00
title: "\u0e01\u0e32\u0e23\u0e41\u0e1b\u0e25\u0e2a\u0e14\u0e14\u0e49\u0e27\u0e22 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การแปลสดด้วย Gemini Live API

Gemini Live API รองรับการแปลคำพูดเป็นคำพูดแบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำระหว่างภาษาต่างๆ กว่า 70 ภาษาโดยใช้โมเดล [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=th) การกำหนดค่า Live API ด้วยการตั้งค่าการแปลจะช่วยให้คุณสตรีมเสียงในภาษาหนึ่งและรับเอาต์พุตเสียงที่แปลแล้วในอีกภาษาหนึ่งได้ ซึ่งจะช่วยให้การแปลเสียงเป็นเสียงแบบเรียลไทม์เป็นไปอย่างราบรื่น

[ลองใช้การแปลสดใน Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=th)
[โคลนแอปตัวอย่างจาก GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[ใช้ทักษะของเอเจนต์การเขียนโค้ดterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#gemini-live-api-dev)

## เจ้าหน้าที่บริการลูกค้าเทียบกับการแปลสด

แม้ว่าทั้ง 2 อย่างจะใช้ Live API แต่โมเดลทางความคิดสำหรับการแปลสดจะแตกต่างจากการโต้ตอบของเอเจนต์แบบเรียลไทม์ผ่านการสนทนา

| ตัวแทนแบบเรียลไทม์ | การแปลสด |
| --- | --- |
| **โมเดลจะทำหน้าที่เป็นผู้ช่วย** โดยจะรับฟัง ให้เหตุผล และดำเนินการในนามของคุณ | **โมเดลจะทำหน้าที่เป็นล่าม** โดยจะทำงานเป็นไปป์ไลน์การแปลแบบเรียลไทม์ |
| **ใช้การโต้ตอบแบบผลัดกัน** ใช้การหยุดชั่วคราว การตรวจหาเจตนา และจัดการการหยุดชะงัก | **ใช้การประมวลผลสตรีมอย่างต่อเนื่อง** แปลขณะที่ผู้พูดพูดโดยไม่ต้องรอให้ถึงคิว |
| **รองรับเครื่องมือและตัวแทน** รองรับการเรียกใช้ฟังก์ชัน, Google Search และคำสั่งโดยตรง | **รองรับการแปลเท่านั้น** การแปลที่มีเวลาในการตอบสนองต่ำอย่างแท้จริง โดยไม่มีการรองรับเครื่องมือหรือคำสั่ง |
| **Multimodal อย่างเต็มรูปแบบ** รองรับอินพุตข้อความ เสียง วิดีโอ และรูปภาพ | **เสียงถูกจำกัด** โดยจะจำกัดเฉพาะเสียงเพื่อรักษาระดับเวลาในการตอบสนองแบบเรียลไทม์ที่เข้มงวด |
| **การกำหนดค่าแบบละเอียด** ใช้คำสั่งการสร้าง คำสั่งเสียง เครื่องมือ และคำสั่งของระบบ | **การกำหนดค่าที่ง่ายขึ้น** ตั้งค่า `target_language_code` และเปิด/ปิด เช่น `echo_target_language` |

## เริ่มต้นใช้งาน

ตัวอย่างต่อไปนี้แสดงวิธีเริ่มต้นไคลเอ็นต์และเชื่อมต่อกับ Live API ด้วยการกำหนดค่าการแปล

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## การส่งเสียง

หากต้องการสตรีมอินพุตเสียงเพื่อการแปล ให้ส่งเสียง PCM แบบ 16 บิต, Little-Endian ที่ยังไม่ได้ประมวลผล

- **รูปแบบเสียงอินพุต**: PCM แบบ 16 บิตดิบที่ 16 kHz (โมโน, Little-Endian)
- **รูปแบบเสียงเอาต์พุต**: PCM แบบ 16 บิตดิบที่ 24 kHz (โมโน, Little-Endian)
- **ขนาดกลุ่มและเวลาในการตอบสนอง**: ส่งเสียงเป็นกลุ่มขนาด 100 มิลลิวินาที

ตัวอย่างต่อไปนี้แสดงวิธีส่งกลุ่มเสียงไปยังเซสชัน

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## การกำหนดค่า

หากต้องการเปิดใช้การแปล คุณต้องระบุ `translationConfig` ภายใน `generationConfig` ระหว่างการตั้งค่าเซสชัน

### การกำหนดค่าข้อความเกี่ยวกับการตั้งค่า

`generationConfig` รองรับฟิลด์ต่อไปนี้เพื่อเปิดใช้ข้อความถอดเสียง

- **`inputAudioTranscription`**: ออบเจ็กต์ที่เมื่อมีอยู่จะช่วยให้โมเดลส่งข้อความถอดเสียงของเสียงที่ป้อนได้
- **`outputAudioTranscription`**: ออบเจ็กต์ที่เมื่อมีอยู่จะช่วยให้โมเดลส่งข้อความถอดเสียงของเอาต์พุต (เสียงที่แปลแล้ว) ได้

`translationConfig` รองรับฟิลด์ต่อไปนี้

- **`targetLanguageCode`**: [รหัสภาษา BCP-47](#supported-languages) ของภาษาที่คุณต้องการให้โมเดลแปล (เช่น `"pl"` สำหรับภาษาโปแลนด์ `"es"` สำหรับภาษาสเปน) ค่าเริ่มต้นคือ `"en"`
- **`echoTargetLanguage`**: บูลีนที่ระบุวิธีจัดการเสียงอินพุตที่เป็นภาษาเป้าหมายอยู่แล้ว หากตั้งค่าเป็น `true` โมเดลจะพูดตามเสียงที่ป้อนซึ่งเป็นภาษาเป้าหมายอยู่แล้ว หากตั้งค่าเป็น `false` โมเดลจะเงียบเมื่อเสียงพูดอินพุตเป็นภาษาเป้าหมายอยู่แล้ว ค่าเริ่มต้นคือ `false`

ตัวอย่างโครงสร้างข้อความการตั้งค่ามีดังนี้

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## ใช้โทเค็นชั่วคราวในแอปพลิเคชันฝั่งไคลเอ็นต์

สำหรับแอปพลิเคชันไคลเอ็นต์ต่อเซิร์ฟเวอร์ คุณสามารถใช้[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th) (ปัจจุบันอยู่ใน`v1beta`) เพื่อหลีกเลี่ยงการเปิดเผยคีย์ API

เมื่อใช้โทเค็นชั่วคราวกับการแปลสด ให้ทำดังนี้

1. คุณต้องใช้ปลายทาง `v1beta`
2. **การกำหนดค่าการล็อก:** โดยค่าเริ่มต้น คุณควรกำหนด `translationConfig` ในข้อจำกัดการสร้างโทเค็นบนเซิร์ฟเวอร์ ซึ่งจะช่วยให้มั่นใจได้ว่าการกำหนดค่าการแปลจะล็อกไว้และไคลเอ็นต์จะแก้ไขไม่ได้
3. **การกำหนดค่าการปลดล็อก:** หากต้องการตั้งค่า `translationConfig` ในฝั่งไคลเอ็นต์ (เช่น เพื่อให้ผู้ใช้เลือกภาษาเป้าหมายของตนเองได้) คุณต้องละเว้นค่านี้จากคำขอสร้างโทเค็นและตั้งค่า `"lock_additional_fields": []` แทน ซึ่งจะปลดล็อก `translationConfig` เพื่อตั้งค่าในฝั่งไคลเอ็นต์

### สร้างโทเค็นชั่วคราวที่จำกัด

ตัวอย่างต่อไปนี้แสดงวิธีสร้างโทเค็นชั่วคราวที่มีข้อจำกัดด้านการแปล

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
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
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## ข้อจำกัด

- **รูปแบบอินพุต**: รองรับเฉพาะอินพุตเสียงสำหรับการแปล ไม่รองรับการป้อนข้อความ
- **การจำลองเสียง**: การจำลองเสียงอาจไม่สอดคล้องกัน เสียงอาจเปลี่ยนหลังจากหยุดพูดนานๆ ระบบอาจกำหนดเพศผิดตามวิธีที่เริ่มพูด หรืออาจใช้เสียงเดียวตลอดการสนทนาแบบหลายคนพูดอย่างรวดเร็ว
- **การตรวจหาภาษา**: การตรวจหาภาษาอาจมีปัญหาเมื่อมีสำเนียงที่หนัก ภาษาที่คล้ายกัน (เช่น สเปนกับโปรตุเกส) หรือการเปลี่ยนภาษาอย่างรวดเร็ว **หมายเหตุ:** การดำเนินการนี้ควรส่งผลต่อเฉพาะข้อความถอดเสียงที่ป้อน รหัสภาษาและคำแปลสุดท้ายควรยังคงถูกต้อง
- **เสียงเบื้องหลัง**: โมเดลได้รับการออกแบบมาเพื่อกรองเสียงรบกวนและเพลงออกเพื่อให้ได้เสียงพูดที่ชัดเจน แต่อาจไม่สามารถกรองเสียงเบื้องหลังบางอย่างได้
- **ภาษาเป้าหมายของเสียงก้อง**: เมื่อ`echoTargetLanguage: true` เสียงรบกวนรอบข้างหรือเพลงอาจทำให้เกิดอาร์ติแฟกต์ในเสียงที่แปลเมื่อเสียงอินพุตเป็นภาษาเป้าหมายอยู่แล้ว

## ภาษาที่รองรับ

ระบบรองรับการแปลสดในภาษาต่อไปนี้

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| แอฟริคานส์ | af | คาซัค | kk |
| อะคัน | ak | เขมร | กม. |
| แอลเบเนีย | sq | คินยารวันดา | rw |
| อัมฮาริก | am | เกาหลี | ko |
| อาหรับ | ar | ภาษาลาว | lo |
| อาร์เมเนีย | hy | ลัตเวีย | lv |
| อาร์เซอร์ไบจัน | az | ลิทัวเนีย | lt |
| บาสก์ | eu | มาซีโดเนีย | mk |
| เบลารุส | be | มาเลย์ | มิลลิวินาที |
| เบงกอล | bn | มาลายาลัม | ml |
| บัลแกเรีย | bg | มราฐี | mr |
| พม่า (เมียนมา) | my | มองโกเลีย | mn |
| คาตาลัน | ca | เนปาล | ne |
| จีน (ตัวย่อ) | zh-Hans | นอร์เวย์ | no, nb |
| จีน (ดั้งเดิม) | zh-Hant | เปอร์เซีย | fa |
| โครเอเชีย | ชม. | โปแลนด์ | pl |
| เช็ก | cs | โปรตุเกส (บราซิล) | pt-BR |
| เดนมาร์ก | da | โปรตุเกส (โปรตุเกส) | pt-PT |
| ดัตช์ | nl | ปัญจาบ | pa |
| อังกฤษ | en | โรมาเนีย | ro |
| เอสโตเนีย | et | รัสเซีย | ru |
| ฟิลิปปินส์ | fil | เซอร์เบีย | sr |
| ฟินแลนด์ | fi | สินธี | SD |
| ฝรั่งเศส | fr | สิงหล | si |
| กาลิเชียน | gl | สโลวัก | sk |
| จอร์เจีย | ka | สโลวีเนีย | sl |
| เยอรมัน | de | สเปน | es |
| กรีก | el | ซุนดา | su |
| คุชราต | gu | สวาฮิลี | sw |
| เฮาซา | ha | สวีเดน | sv |
| ฮีบรู | เขา | ทมิฬ | ta |
| ฮินดี | hi | เตลูกู | te |
| ฮังการี | hu | ไทย | th |
| ไอซ์แลนด์ | is | ตุรกี | tr |
| อินโดนีเซีย | id | ยูเครน | uk |
| อิตาลี | it | อูรดู | ur |
| ญี่ปุ่น | ja | อุซเบก | uz |
| ชวา | jv | เวียดนาม | vi |
| กันนาดา | kn | ซูลู | zu |

## ขั้นตอนถัดไป

- อ่านคู่มือ[ความสามารถ](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th)ของ Live API ฉบับเต็ม
- อ่านคู่มือ[เริ่มต้นใช้งาน SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th)
- อ่านคู่มือ[เริ่มต้นใช้งาน WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=th)
- อ่านคู่มือ[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th)เพื่อดูการตรวจสอบสิทธิ์ที่ปลอดภัยในแอปพลิเคชันไคลเอ็นต์ต่อเซิร์ฟเวอร์
- โคลน[ตัวอย่าง API ที่ใช้งานจริง](https://github.com/google-gemini/gemini-live-api-examples)จาก GitHub

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-23 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-23 UTC"],[],[]]
