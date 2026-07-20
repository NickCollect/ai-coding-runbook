---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th
fetched_at: 2026-07-20T04:37:41.122791+00:00
title: "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e02\u0e2d\u0e07 Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# คู่มือความสามารถของ Live API

นี่คือคู่มือที่ครอบคลุมความสามารถและการกำหนดค่า
ที่พร้อมใช้งานกับ Live API
ดูหน้า[เริ่มต้นใช้งาน Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) เพื่อดูภาพรวมและโค้ดตัวอย่างสำหรับกรณีการใช้งานทั่วไป

## ก่อนเริ่มต้น

- **ทำความคุ้นเคยกับแนวคิดหลัก:** หากยังไม่ได้อ่าน โปรดอ่านหน้า[เริ่มต้นใช้งาน Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)  ก่อน
  ซึ่งจะแนะนำหลักการพื้นฐานของ Live API วิธีการทำงาน และ[แนวทางการติดตั้งใช้งาน](https://ai.google.dev/gemini-api/docs/live?hl=th#implementation-approach)ต่างๆ
- **ลองใช้ Live API ใน AI Studio:** คุณอาจพบว่าการลองใช้ Live API ใน [Google AI Studio](https://aistudio.google.com/app/live?hl=th) มีประโยชน์ก่อนที่จะเริ่มสร้าง หากต้องการใช้
  Live API ใน Google AI Studio ให้เลือก**สตรีม**

## การเปรียบเทียบรูปแบบ

ตารางต่อไปนี้จะสรุปความแตกต่างที่สําคัญระหว่างโมเดล[Gemini 3.1 Flash เวอร์ชันตัวอย่างแบบสด](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=th)กับโมเดล [Gemini 2.5 Flash เวอร์ชันตัวอย่างแบบสด](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=th)

| ฟีเจอร์ | เวอร์ชันตัวอย่างของ Gemini 3.1 Flash Live | ตัวอย่าง Gemini 2.5 Flash แบบเรียลไทม์ |
| --- | --- | --- |
| **[การคิด](#native-audio-output-thinking)** | ใช้ `thinkingLevel` เพื่อควบคุมระดับความลึกของการคิดด้วยการตั้งค่าต่างๆ เช่น `minimal`, `low`, `medium` และ `high` โดยค่าเริ่มต้นจะตั้งเป็น `minimal` เพื่อเพิ่มประสิทธิภาพให้มีความหน่วงต่ำที่สุด ดู[ระดับการคิดและงบประมาณ](https://ai.google.dev/gemini-api/docs/thinking?hl=th#levels-budgets) | ใช้ `thinkingBudget` เพื่อตั้งค่าจำนวนโทเค็นการคิด ระบบจะเปิดใช้การคิดแบบไดนามิกโดยค่าเริ่มต้น ตั้งค่า `thinkingBudget` เป็น `0` เพื่อปิดใช้ ดู[ระดับและงบประมาณการทดสอบ](https://ai.google.dev/gemini-api/docs/thinking?hl=th#levels-budgets) |
| **[การรับคำตอบ](https://ai.google.dev/api/live?hl=th#bidigeneratecontentservercontent)** | เหตุการณ์ฝั่งเซิร์ฟเวอร์เดียวอาจมีเนื้อหาหลายส่วนพร้อมกัน (เช่น `inlineData`และข้อความถอดเสียง) ตรวจสอบว่าโค้ดประมวลผลทุกส่วนในแต่ละเหตุการณ์เพื่อไม่ให้พลาดเนื้อหา | เหตุการณ์ฝั่งเซิร์ฟเวอร์แต่ละรายการจะมีเนื้อหาเพียงส่วนเดียว โดยระบบจะส่งส่วนต่างๆ ในเหตุการณ์แยกกัน |
| **[เนื้อหาของลูกค้า](#incremental-updates)** | `send_client_content` ใช้ได้เฉพาะสำหรับการเริ่มต้นประวัติบริบทเริ่มต้น (ต้องตั้งค่า `initial_history_in_client_content` ในการกำหนดค่าเซสชัน) หากต้องการส่งการอัปเดตข้อความระหว่างการสนทนา ให้ใช้ `send_realtime_input` แทน | `send_client_content` ได้รับการรองรับตลอดการสนทนาสำหรับการส่งการอัปเดตเนื้อหาแบบเพิ่มทีละรายการและการสร้างบริบท |
| **[เปิดความครอบคลุม](https://ai.google.dev/api/live?hl=th#turncoverage)** | ค่าเริ่มต้นคือ `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO` เทิร์นของโมเดลประกอบด้วยกิจกรรมเสียงที่ตรวจพบและเฟรมวิดีโอทั้งหมด | ค่าเริ่มต้นคือ `TURN_INCLUDES_ONLY_ACTIVITY` เทิร์นของโมเดลจะรวมเฉพาะกิจกรรมที่ตรวจพบ |
| **[VAD ที่กำหนดเอง](#disable-automatic-vad)** (`activity_start`/`activity_end`) | รองรับ ปิดใช้ VAD อัตโนมัติและส่งข้อความ `activityStart` และ `activityEnd` ด้วยตนเองเพื่อควบคุมขอบเขตการพูด | รองรับ ปิดใช้ VAD อัตโนมัติและส่งข้อความ `activityStart` และ `activityEnd` ด้วยตนเองเพื่อควบคุมขอบเขตการพูด |
| **[การกำหนดค่า VAD อัตโนมัติ](#configure-automatic-vad)** | รองรับ กำหนดค่าพารามิเตอร์ เช่น `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` และ `silence_duration_ms` | รองรับ กำหนดค่าพารามิเตอร์ เช่น `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` และ `silence_duration_ms` |
| **[การเรียกใช้ฟังก์ชันแบบไม่พร้อมกัน](https://ai.google.dev/gemini-api/docs/live-tools?hl=th#async-function-calling)** (`behavior: NON_BLOCKING`) | ไม่รองรับ การเรียกใช้ฟังก์ชันจะทำได้ตามลำดับเท่านั้น โมเดลจะไม่เริ่มตอบจนกว่าคุณจะส่งการตอบกลับของเครื่องมือ | รองรับ ตั้งค่า `behavior` เป็น `NON_BLOCKING` ในการประกาศฟังก์ชันเพื่อให้โมเดลโต้ตอบต่อไปได้ในขณะที่ฟังก์ชันทำงาน ควบคุมวิธีที่โมเดลจัดการคำตอบด้วยพารามิเตอร์ `scheduling` (`INTERRUPT`, `WHEN_IDLE` หรือ `SILENT`) |
| **[เสียงแบบเชิงรุก](#proactive-audio)** | สิ่งที่ทำไม่ได้ | รองรับ เมื่อเปิดใช้ โมเดลจะตัดสินใจได้ล่วงหน้าว่าจะไม่ตอบหากเนื้อหาอินพุตไม่เกี่ยวข้อง ตั้งค่า `proactive_audio` เป็น `true` ในการกำหนดค่า `proactivity` (ต้องใช้ `v1alpha`) |
| **[การโต้ตอบที่สะท้อนถึงความรู้สึก](#affective-dialog)** | สิ่งที่ทำไม่ได้ | รองรับ โมเดลจะปรับรูปแบบคำตอบให้ตรงกับการแสดงออกและน้ำเสียงของอินพุต ตั้งค่า `enable_affective_dialog` เป็น `true` ในการกำหนดค่าเซสชัน (ต้องใช้ `v1alpha`) |

หากต้องการย้ายข้อมูลจาก Gemini 2.5 Flash Live ไปยัง Gemini 3.1 Flash Live โปรดดู[คำแนะนำในการย้ายข้อมูล](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=th#migrating)

## การสร้างการเชื่อมต่อ

ตัวอย่างต่อไปนี้แสดงวิธีสร้างการเชื่อมต่อด้วยคีย์ API

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## รูปแบบการโต้ตอบ

ส่วนต่อไปนี้จะแสดงตัวอย่างและบริบทที่รองรับสำหรับรูปแบบอินพุตและเอาต์พุตต่างๆ ที่มีใน Live API

### การส่งเสียง

ต้องส่งเสียงเป็นข้อมูล PCM ดิบ (เสียง PCM ดิบ 16 บิต, 16 kHz, little-endian)

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

### รูปแบบเสียง

ข้อมูลเสียงใน Live API จะเป็น PCM แบบ 16 บิตแบบ Little-Endian ดิบเสมอ
เอาต์พุตเสียงจะใช้อัตราการสุ่มตัวอย่าง 24kHz เสมอ
เสียงอินพุตมีอัตราการสุ่มตัวอย่าง 16kHz โดยค่าเริ่มต้น แต่ Live API จะสุ่มตัวอย่างใหม่หากจำเป็น
เพื่อให้ส่งอัตราการสุ่มตัวอย่างใดก็ได้ หากต้องการระบุอัตราการสุ่มตัวอย่างของเสียงอินพุต ให้ตั้งค่า
ประเภท MIME ของ [Blob](https://ai.google.dev/api/caching?hl=th#Blob) ที่มีเสียงแต่ละรายการเป็นค่า
เช่น `audio/pcm;rate=16000`

### การรับเสียง

ระบบจะรับคำตอบเสียงของโมเดลเป็นกลุ่มข้อมูล

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### กำลังส่งข้อความ

คุณส่งข้อความได้โดยใช้ `send_realtime_input` (Python) หรือ `sendRealtimeInput` (JavaScript)

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### กำลังส่งวิดีโอ

ระบบจะส่งเฟรมวิดีโอเป็นรูปภาพแต่ละรูป (เช่น JPEG หรือ PNG) ที่อัตราเฟรมที่เฉพาะเจาะจง (สูงสุด 1 เฟรมต่อวินาที)

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### การอัปเดตเนื้อหาแบบเพิ่มทีละรายการ

ใช้การอัปเดตแบบเพิ่มทีละรายการเพื่อส่งอินพุตข้อความ สร้างบริบทของเซสชัน หรือ
กู้คืนบริบทของเซสชัน สำหรับบริบทสั้นๆ คุณสามารถส่งการโต้ตอบแบบเลี้ยวต่อเลี้ยว
เพื่อแสดงลำดับเหตุการณ์ที่แน่นอนได้โดยทำดังนี้

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

สำหรับบริบทที่ยาวขึ้น เราขอแนะนำให้สรุปข้อความเดียวเพื่อเพิ่ม
พื้นที่ในหน้าต่างบริบทสำหรับการโต้ตอบครั้งต่อๆ ไป โปรดดู[การกลับมาใช้เซสชันต่อ](https://ai.google.dev/gemini-api/docs/live-session?hl=th#session-resumption)เพื่อดูอีกวิธีในการ
โหลดบริบทของเซสชัน

### การถอดเสียงเป็นคำ

นอกจากคำตอบของโมเดลแล้ว คุณยังรับข้อความถอดเสียงของทั้งเอาต์พุตเสียงและอินพุตเสียงได้ด้วย

หากต้องการเปิดใช้การถอดเสียงเอาต์พุตเสียงของโมเดล ให้ส่ง
`output_audio_transcription` ในการกำหนดค่าการตั้งค่า ระบบจะอนุมานภาษาในการถอดเสียงเป็นคำจากคำตอบของโมเดล

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

หากต้องการเปิดใช้การถอดเสียงเป็นคำของอินพุตเสียงของโมเดล ให้ส่ง
`input_audio_transcription` ในการกำหนดค่าการตั้งค่า

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### เปลี่ยนเสียงและภาษา

โมเดล[เอาต์พุตเสียงเนทีฟ](#native-audio-output)รองรับเสียงใดก็ได้
ที่พร้อมใช้งานสำหรับโมเดล[การอ่านออกเสียงข้อความ (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#voices)
คุณฟังเสียงทั้งหมดได้ใน [AI Studio](https://aistudio.google.com/app/live?hl=th)

หากต้องการระบุเสียง ให้ตั้งชื่อเสียงภายในออบเจ็กต์ `speechConfig` เป็นส่วนหนึ่ง
ของการกำหนดค่าเซสชัน

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API รองรับ[หลายภาษา](#supported-languages)
โมเดล[เอาต์พุตเสียงดั้งเดิม](#native-audio-output)จะเลือกภาษาที่เหมาะสมโดยอัตโนมัติ
และไม่รองรับการตั้งค่ารหัสภาษาอย่างชัดเจน

## ความสามารถด้านเสียงแบบเนทีฟ

โมเดลล่าสุดของเรามี[เอาต์พุตเสียงในตัว](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=th)
ซึ่งให้เสียงพูดที่เป็นธรรมชาติและสมจริง รวมถึงประสิทธิภาพแบบหลายภาษาที่ดียิ่งขึ้น

### กำลังคิด

โมเดล Gemini 3.1 ใช้ `thinkingLevel` เพื่อควบคุมระดับความลึกของการคิด โดยมีการตั้งค่าต่างๆ เช่น `minimal`, `low`, `medium` และ `high` ค่าเริ่มต้นคือ `minimal` เพื่อ
เพิ่มประสิทธิภาพให้มีเวลาในการตอบสนองต่ำที่สุด โมเดล Gemini 2.5 ใช้
`thinkingBudget` เพื่อตั้งค่าจำนวนโทเค็นการคิดแทน ดูรายละเอียดเพิ่มเติม
เกี่ยวกับระดับเทียบกับงบประมาณได้ที่
[การพิจารณาระดับและงบประมาณ](https://ai.google.dev/gemini-api/docs/thinking?hl=th#levels-budgets)

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

นอกจากนี้ คุณยังเปิดใช้สรุปความคิดได้โดยตั้งค่า `includeThoughts` เป็น
`true` ในการกำหนดค่า ดูข้อมูลเพิ่มเติมได้ที่[สรุปความคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#summaries)

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### การโต้ตอบที่สะท้อนถึงความรู้สึก

ฟีเจอร์นี้ช่วยให้ Gemini ปรับรูปแบบคำตอบให้เข้ากับรูปแบบการป้อนข้อมูลและ
โทนเสียง

หากต้องการใช้การโต้ตอบที่สะท้อนถึงความรู้สึก ให้ตั้งค่าเวอร์ชัน API เป็น `v1alpha` และตั้งค่า
`enable_affective_dialog` เป็น `true` ในข้อความการตั้งค่า

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### เสียงเชิงรุก

เมื่อเปิดใช้ฟีเจอร์นี้ Gemini จะตัดสินใจไม่ตอบได้
หากเนื้อหาไม่เกี่ยวข้อง

หากต้องการใช้ ให้ตั้งค่าเวอร์ชัน API เป็น `v1alpha` และกำหนดค่าฟิลด์ `proactivity`
ในข้อความการตั้งค่า แล้วตั้งค่า `proactive_audio` เป็น `true` ดังนี้

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## การแปลสด

Live API รองรับการแปลการสนทนาด้วยเสียงแบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำ ความสามารถนี้ช่วยให้คุณสร้างแอปพลิเคชันการแปลเสียงเป็นเสียงแบบเรียลไทม์ได้

ดูข้อมูลเพิ่มเติมและตัวอย่างได้ที่[คู่มือการแปลสด](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th)

## การตรวจจับกิจกรรมเสียง (VAD)

การตรวจจับกิจกรรมเสียง (VAD) ช่วยให้โมเดลจดจำได้เมื่อมีคนพูด
ซึ่งจำเป็นอย่างยิ่งต่อการสร้างการสนทนาที่เป็นธรรมชาติ เนื่องจากช่วยให้ผู้ใช้
ขัดจังหวะโมเดลได้ทุกเมื่อ

เมื่อ VAD ตรวจพบการหยุดชะงัก ระบบจะยกเลิกและ
ทิ้งการสร้างที่กำลังดำเนินการอยู่ และจะเก็บเฉพาะข้อมูลที่ส่งไปยังไคลเอ็นต์แล้วไว้ใน
ประวัติเซสชัน จากนั้นเซิร์ฟเวอร์จะส่งข้อความ [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentservercontent) เพื่อรายงานการหยุดชะงัก

จากนั้นเซิร์ฟเวอร์ Gemini จะทิ้งการเรียกใช้ฟังก์ชันที่รอดำเนินการและส่ง`BidiGenerateContentServerContent`ข้อความพร้อมรหัสของการเรียกที่ยกเลิก

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### VAD อัตโนมัติ

โดยค่าเริ่มต้น โมเดลจะดำเนินการ VAD โดยอัตโนมัติใน
สตรีมอินพุตเสียงอย่างต่อเนื่อง คุณกำหนดค่า VAD ได้ด้วยฟิลด์
[`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=th#RealtimeInputConfig.AutomaticActivityDetection)
ของ[การกำหนดค่าการตั้งค่า](https://ai.google.dev/api/live?hl=th#BidiGenerateContentSetup)

เมื่อหยุดสตรีมเสียงชั่วคราวเป็นเวลานานกว่า 1 วินาที (เช่น เนื่องจากผู้ใช้ปิดไมโครโฟน) ควรส่งเหตุการณ์
[`audioStreamEnd`](https://ai.google.dev/api/live?hl=th#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end)
เพื่อล้างเสียงที่แคชไว้ ไคลเอ็นต์สามารถกลับมาส่งข้อมูลเสียงได้ทุกเมื่อ

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

เมื่อใช้ `send_realtime_input` API จะตอบกลับเสียงโดยอัตโนมัติตาม VAD ส่วน `send_client_content` จะเพิ่มข้อความลงในบริบทของโมเดลตามลำดับ ขณะที่ `send_realtime_input` ได้รับการเพิ่มประสิทธิภาพเพื่อการตอบสนองโดยยอมให้ลำดับไม่แน่นอน

### การกำหนดค่า VAD อัตโนมัติ

หากต้องการควบคุมกิจกรรม VAD เพิ่มเติม คุณสามารถกําหนดค่าพารามิเตอร์ต่อไปนี้ได้
ดูข้อมูลเพิ่มเติมได้ที่[เอกสารอ้างอิง API](https://ai.google.dev/api/live?hl=th#automaticactivitydetection)

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### ปิดใช้ VAD อัตโนมัติ

หรือจะปิดใช้ VAD อัตโนมัติโดยตั้งค่า
`realtimeInputConfig.automaticActivityDetection.disabled` เป็น `true` ในข้อความการตั้งค่า
ก็ได้ ในการกำหนดค่านี้ ไคลเอ็นต์มีหน้าที่ตรวจหาคำพูดของผู้ใช้และส่งข้อความ
[`activityStart`](https://ai.google.dev/api/live?hl=th#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start)
และ [`activityEnd`](https://ai.google.dev/api/live?hl=th#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end)
ในเวลาที่เหมาะสม ระบบจะไม่ส่ง `audioStreamEnd` ในการกำหนดค่านี้ แต่จะมีการทำเครื่องหมายการหยุดชะงักของสตรีมด้วยข้อความ `activityEnd` แทน

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### ทำความเข้าใจพารามิเตอร์ VAD และผลกระทบต่อคุณภาพ

เมื่อใช้ VAD อัตโนมัติ พารามิเตอร์หลัก 2 รายการจะควบคุมวิธี
การแบ่งเสียงเป็นช่วงคำพูดก่อนส่งไปยังโมเดล ดังนี้

- **`prefixPaddingMs`**: ปริมาณเสียงที่จะรวม*ก่อน*ตรวจพบคำพูด
  การ "มองย้อนกลับ" นี้ช่วยให้โมเดลจับภาพการเริ่มต้นของคำพูดทั้งหมด
  รวมถึงพยางค์แรกซึ่งอาจเริ่มก่อนที่
  VAD จะทริกเกอร์ ค่า `0` อาจทำให้มีการตัดคำที่จุดเริ่มต้น
- **`silenceDurationMs`**: ระยะเวลาที่เซิร์ฟเวอร์รอในขณะที่ไม่มีเสียงพูด
  ก่อนที่จะสิ้นสุดการพูด ซึ่งจะเป็นตัวกำหนดว่าระบบจะยอมรับ
  การหยุดพูดกลางประโยคตามธรรมชาติได้มากน้อยเพียงใด (เช่น การคิด การหายใจ หรือ
  ขอบเขตของอนุประโยค)

#### ผลกระทบของ `silenceDurationMs` ต่อคุณภาพเสียง

ค่า `silenceDurationMs` จะส่งผลโดยตรงต่อขนาดและความสมบูรณ์
ของกลุ่มเสียงที่โมเดลได้รับเพื่อประมวลผล

- **แนะนำ (500-800 มิลลิวินาที):** ให้ความสมดุลที่ดี โดยโมเดลจะได้รับ
  เสียงที่สมบูรณ์และมีบริบทที่หลากหลายในขณะที่ยังคงรักษาเวลาในการตอบสนอง
  ให้อยู่ในระดับที่เหมาะสม ค่าเริ่มต้นภายในของเซิร์ฟเวอร์คือประมาณ 800 มิลลิวินาที
- **ต่ำเกินไป (เช่น 100-200 มิลลิวินาที):** ระบบจะสิ้นสุดการพูดในระหว่าง
  การหยุดชั่วคราวตามธรรมชาติ ซึ่งจะแบ่งคำพูดเดียวออกเป็นเสียงขนาดเล็กหลายส่วน
  โมเดลจะได้รับเสียงเหล่านี้ทีละส่วน ทำให้สูญเสียบริบทข้ามส่วนและส่งผลให้คุณภาพการถอดเสียงและการตอบกลับต่ำลง
- **สูงเกินไป (เช่น 2000 มิลลิวินาทีขึ้นไป):** ระบบจะรอนานหลังจากที่ผู้ใช้หยุดพูด ซึ่งจะเพิ่มเวลาในการตอบสนองที่รับรู้ได้ก่อนที่โมเดลจะตอบกลับ

#### แนวทางปฏิบัติแนะนำสำหรับ VAD ด้วยตนเอง (ฝั่งไคลเอ็นต์)

เมื่อปิดใช้ VAD อัตโนมัติและจัดการสัญญาณ `activityStart`/`activityEnd`
จากการตรวจจับเสียงฝั่งไคลเอ็นต์ของคุณเอง โปรดทราบว่าระบบจะข้ามกลไกการบัฟเฟอร์เสียงในตัวของเซิร์ฟเวอร์ ซึ่งหมายความว่า

1. **ไม่มีบัฟเฟอร์ก่อนการพูด:** เซิร์ฟเวอร์จะไม่เพิ่มเสียงก่อน
   การเริ่มต้นการพูดที่ตรวจพบอีกต่อไป ลูกค้าควรใส่บริบทเสียงที่เพียงพอก่อนส่ง `activityStart`
2. **ไม่ยอมรับความเงียบ:** เซิร์ฟเวอร์จะดำเนินการกับสัญญาณ
   `activityEnd`ทันทีโดยไม่ต้องรอเพิ่มเติม หาก VAD ฝั่งไคลเอ็นต์
   ใช้เกณฑ์สิ้นสุดการพูดที่เข้มงวด (เช่น เงียบ 200 มิลลิวินาที)
   ระบบอาจตัดคำพูดกลางประโยคระหว่างหยุดพูดตามปกติ

หากต้องการรักษาคุณภาพเสียงด้วย VAD แบบกำหนดเอง ให้ใช้เกณฑ์ความเงียบเมื่อสิ้นสุดการพูดอย่างน้อย **500 มิลลิวินาที**ในเครื่องตรวจจับกิจกรรมการใช้เสียงของไคลเอ็นต์
โดยปกติแล้วค่าเกณฑ์ที่ต่ำกว่าค่านี้มักทำให้เสียงขาดหาย ซึ่งจะทำให้คุณภาพการถอดเสียงและการตอบกลับของโมเดลลดลง

## จำนวนโทเค็น

คุณดูจำนวนโทเค็นที่ใช้ทั้งหมดได้ในฟิลด์ [usageMetadata](https://ai.google.dev/api/live?hl=th#usagemetadata) ของข้อความเซิร์ฟเวอร์ที่ส่งคืน

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## ความละเอียดของสื่อ

คุณระบุความละเอียดของสื่อสำหรับสื่ออินพุตได้โดยตั้งค่าฟิลด์
`mediaResolution` เป็นส่วนหนึ่งของการกำหนดค่าเซสชัน

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## ข้อจำกัด

โปรดคำนึงถึงข้อจำกัดต่อไปนี้ของ Live API
เมื่อวางแผนโปรเจ็กต์

### รูปแบบการตอบสนอง

โมเดลเสียงเนทีฟรองรับเฉพาะรูปแบบการตอบกลับ `AUDIO` หากต้องการ
คำตอบของโมเดลเป็นข้อความ ให้ใช้ฟีเจอร์[การถอดเสียงจากเสียงเอาต์พุต](#audio-transcription)

### การตรวจสอบสิทธิ์ไคลเอ็นต์

Live API จะให้การตรวจสอบสิทธิ์แบบเซิร์ฟเวอร์ต่อเซิร์ฟเวอร์เท่านั้น
โดยค่าเริ่มต้น หากคุณใช้แอปพลิเคชัน Live API โดยใช้[แนวทางไคลเอ็นต์ต่อเซิร์ฟเวอร์](https://ai.google.dev/gemini-api/docs/live?hl=th#implementation-approach) คุณต้องใช้[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=th)เพื่อลดความเสี่ยงด้านความปลอดภัย

### ระยะเวลาเซสชัน

เซสชันเสียงอย่างเดียวจะจำกัดไว้ที่ 15 นาที
และเซสชันเสียงและวิดีโอจะจำกัดไว้ที่ 2 นาที
อย่างไรก็ตาม คุณสามารถกำหนดค่า[เทคนิคการจัดการเซสชัน](https://ai.google.dev/gemini-api/docs/live-session?hl=th)ที่แตกต่างกันเพื่อขยายระยะเวลาเซสชันได้ไม่จำกัด

### หน้าต่างบริบท

เซสชันมีขีดจํากัดของหน้าต่างบริบทดังนี้

- 128,000 โทเค็นสำหรับโมเดล[เอาต์พุตเสียงดั้งเดิม](#native-audio-output)
- 32,000 โทเค็นสำหรับโมเดล Live API อื่นๆ

## ภาษาที่รองรับ

Live API รองรับภาษาต่อไปนี้ 97 ภาษา

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| แอฟริคานส์ | `af` | ลัตเวีย | `lv` |
| อะคัน | `ak` | ลิทัวเนีย | `lt` |
| แอลเบเนีย | `sq` | มาซีโดเนีย | `mk` |
| อัมฮาริก | `am` | มาเลย์ | `ms` |
| อาหรับ | `ar` | มาลายาลัม | `ml` |
| อาร์เมเนีย | `hy` | มอลตา | `mt` |
| อัสสัม | `as` | เมารี | `mi` |
| อาร์เซอร์ไบจัน | `az` | มราฐี | `mr` |
| บาสก์ | `eu` | มองโกเลีย | `mn` |
| เบลารุส | `be` | เนปาล | `ne` |
| เบงกอล | `bn` | นอร์เวย์ | `no` |
| บอสเนีย | `bs` | โอเดีย | `or` |
| บัลแกเรีย | `bg` | โอโรโม | `om` |
| พม่า | `my` | พาชตู | `ps` |
| คาตาลัน | `ca` | เปอร์เซีย | `fa` |
| ซีบัวโน | `ceb` | โปแลนด์ | `pl` |
| จีน | `zh` | โปรตุเกส | `pt` |
| โครเอเชีย | `hr` | ปัญจาบ | `pa` |
| เช็ก | `cs` | เคชัว | `qu` |
| เดนมาร์ก | `da` | โรมาเนีย | `ro` |
| ดัตช์ | `nl` | โรมานช์ | `rm` |
| อังกฤษ | `en` | รัสเซีย | `ru` |
| เอสโตเนีย | `et` | เซอร์เบีย | `sr` |
| แฟโร | `fo` | สินธี | `sd` |
| ฟิลิปปินส์ | `fil` | สิงหล | `si` |
| ฟินแลนด์ | `fi` | สโลวัก | `sk` |
| ฝรั่งเศส | `fr` | สโลวีเนีย | `sl` |
| กาลิเชียน | `gl` | โซมาลี | `so` |
| จอร์เจีย | `ka` | โซโทใต้ | `st` |
| เยอรมัน | `de` | สเปน | `es` |
| กรีก | `el` | สวาฮิลี | `sw` |
| คุชราต | `gu` | สวีเดน | `sv` |
| เฮาซา | `ha` | ทาจิก | `tg` |
| ฮีบรู | `iw` | ทมิฬ | `ta` |
| ฮินดี | `hi` | เตลูกู | `te` |
| ฮังการี | `hu` | ไทย | `th` |
| ไอซ์แลนด์ | `is` | ซวานา | `tn` |
| อินโดนีเซีย | `id` | ตุรกี | `tr` |
| ไอริช | `ga` | เติร์กเมน | `tk` |
| อิตาลี | `it` | ยูเครน | `uk` |
| ญี่ปุ่น | `ja` | อูรดู | `ur` |
| กันนาดา | `kn` | อุซเบก | `uz` |
| คาซัค | `kk` | เวียดนาม | `vi` |
| เขมร | `km` | เวลส์ | `cy` |
| คินยารวันดา | `rw` | ฟริเซียนตะวันตก | `fy` |
| เกาหลี | `ko` | วูลอฟ | `wo` |
| เคิร์ด | `ku` | โยรูบา | `yo` |
| คีร์กิซ | `ky` | ซูลู | `zu` |
| ภาษาลาว | `lo` |  |  |

## ขั้นตอนถัดไป

- อ่านคำแนะนำ[การใช้เครื่องมือ](https://ai.google.dev/gemini-api/docs/live-tools?hl=th)และ
  [การจัดการเซสชัน](https://ai.google.dev/gemini-api/docs/live-session?hl=th)เพื่อดูข้อมูลสำคัญ
  เกี่ยวกับการใช้ Live API อย่างมีประสิทธิภาพ
- ลองใช้ Live API ใน [Google AI Studio](https://aistudio.google.com/app/live?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับโมเดล Live API ได้ที่[เสียงเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-native-audio)
  ในหน้าโมเดล
- ลองดูตัวอย่างเพิ่มเติมใน[ตำราการใช้ Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=th)
  [ตำราการใช้เครื่องมือ Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=th)
  และ[สคริปต์การเริ่มต้นใช้งาน Live API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-09 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-09 UTC"],[],[]]
