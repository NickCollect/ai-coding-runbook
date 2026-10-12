---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=th
fetched_at: 2026-10-12T07:07:52.367212+00:00
title: "\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e14\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e2a\u0e14\u0e14\u0e49\u0e27\u0e22 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การถอดเสียงสดด้วย Gemini Live API

Gemini Live API รองรับการถอดเสียงพูดเป็นข้อความแบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำโดยใช้โมเดล [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=th) การเชื่อมต่อกับ Live API ผ่าน WebSockets หรือการใช้ Google Gen AI SDK จะช่วยให้คุณสตรีมอินพุตเสียงอย่างต่อเนื่องและรับการถอดเสียงเป็นข้อความแบบเรียลไทม์ที่เพิ่มขึ้นได้เมื่อมีการพูด

[ลองใช้การถอดเสียงแบบเรียลไทม์ใน Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=th)
[เปิด Colab Cookbookcode](https://github.com/google-gemini/cookbook)
[ใช้ทักษะของ Coding Agentterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#gemini-live-api-dev)

การใช้ประโยชน์จาก Gemini Live API แพลตฟอร์มสำหรับนักพัฒนาแอป เช่น
[Agora](https://docs.agora.io/en/ai/models/asr/gemini)
[Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration)
[LiveKit](https://docs.livekit.io/agents/models/stt/gemini/)
[Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google)
[Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) และ
[Vision Agents](https://visionagents.ai/integrations/stt/gemini)
ช่วยให้นักพัฒนาแอปสร้างและติดตั้งใช้งานอินเทอร์เฟซที่ขับเคลื่อนด้วยเสียงประสิทธิภาพสูง
ได้อย่างง่ายดาย แพลตฟอร์มเหล่านี้จัดการโครงสร้างพื้นฐานการสตรีมสื่อแบบเรียลไทม์ที่ซับซ้อน
เบื้องหลัง ซึ่งช่วยให้นักพัฒนาแอปมุ่งเน้นไปที่การสร้างประสบการณ์ของผู้ใช้ได้อย่างเต็มที่

## เจ้าหน้าที่บริการลูกค้าเทียบกับการถอดเสียงแบบเรียลไทม์

แม้ว่าทั้ง 2 อย่างจะใช้การเชื่อมต่อสตรีมแบบ 2 ทางของ Live API แต่การถอดเสียงสดจะทำงานเป็นไปป์ไลน์การจดจำเสียงพูดที่มีเวลาในการตอบสนองที่รวดเร็วโดยเฉพาะ แทนที่จะเป็นเอเจนต์การสนทนา

| ฟีเจอร์ | ตัวแทนแบบเรียลไทม์ | การถอดเสียงเป็นคำแบบเรียลไทม์ |
| --- | --- | --- |
| **บทบาทหลัก** | ผู้ช่วยแบบสนทนาที่ฟัง คิด และตอบกลับ | ไปป์ไลน์การแปลงเสียงพูดเป็นข้อความแบบเรียลไทม์ที่ถอดเสียงจากเสียงที่เข้ามา |
| **รูปแบบการตอบกลับ** | เสียงพูดและข้อความ (`response_modalities=["AUDIO"]`) | การถอดเสียงข้อความที่สตรีม (`response_modalities=["TEXT"]`) |
| **รูปแบบการโต้ตอบ** | การสนทนาแบบผลัดกันพูดพร้อมการตรวจหาการหยุดพูดและการขัดจังหวะ | การประมวลผลสตรีมอย่างต่อเนื่องขณะที่ผู้พูดพูด |
| **ฟีเจอร์ที่รองรับ** | การเรียกใช้ฟังก์ชัน, Google Search, คำสั่งของระบบ | การเลือกคำพูด (`custom_vocabulary`), การตรวจหาภาษา, VAD แบบกำหนดเองและแบบผสม, การถอดเสียงอัจฉริยะ |
| **สตรีมอินพุต** | หลายรูปแบบ: เสียง วิดีโอ รูปภาพ ข้อความ | อินพุตเสียง (PCM 16 บิตแบบดิบ) |

## เริ่มต้นใช้งาน

ตัวอย่างต่อไปนี้แสดงวิธีเปิดเซสชันการสตรีมแบบ 2 ทางด้วย `gemini-3.5-transcribe-live` และรับการถอดเสียงแบบเรียลไทม์

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## การถอดเสียงเป็นคำชั่วคราวและฉบับสมบูรณ์

เมื่อสตรีมเสียงเข้าสู่ Live API เซิร์ฟเวอร์จะปล่อยฟิลด์การถอดเสียงเป็นคำ 2 ฟิลด์ที่เสริมกันภายใน `server_content` ดังนี้

- **`interim_input_transcription`**: สมมติฐานบางส่วนแบบคาดการณ์ที่มีเวลาในการตอบสนองต่ำจะได้รับการอัปเดตขณะที่ผู้พูดกำลังพูดอยู่ การอัปเดตบางส่วนเหล่านี้เกิดขึ้นอย่างรวดเร็วโดยมีความล่าช้าน้อยที่สุด ใช้ `interim_input_transcription` เพื่อแสดงผลคำบรรยายแทนเสียง UI แบบสดที่ปรับเปลี่ยนตามอุปกรณ์หรือคำบรรยายแทนเสียงตัวอย่าง
- **`input_transcription`**: ข้อความถอดเสียงที่เสร็จสมบูรณ์แล้วซึ่งจะแสดงเมื่อผู้พูดหยุดชั่วคราว พูดจบ หรือพูดเสร็จ เมื่อส่งออกแล้ว ข้อความนี้จะแสดงการถอดเสียงที่เชื่อถือได้ของโมเดลสำหรับส่วนคำพูดนั้น ในโหมดการถอดเสียงอัจฉริยะ การตอบกลับนี้จะรวมถึงการตอบกลับที่จัดรูปแบบและทำความสะอาดแล้ว

ตัวอย่างต่อไปนี้แสดงวิธีแสดงผลการถอดเสียงบางส่วนชั่วคราวแบบสตรีมมิงและส่งการถอดเสียงสุดท้าย

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## การส่งเสียง

สตรีมเสียงเป็นกลุ่มๆ ผ่านการเชื่อมต่อที่ใช้งานอยู่เป็นเสียง PCM 16 บิตแบบดิบ

- **รูปแบบเสียง:** PCM แบบ 16 บิตดิบที่ 16kHz (โมโน, little-endian)
- **ขนาดก้อนข้อมูล:** ส่งเสียงเป็นก้อนข้อมูลขนาด 100 มิลลิวินาที (1,024 ถึง 2,048 เฟรม)
- **ประเภท MIME:** `audio/pcm;rate=16000` (หรืออัตราการสุ่มตัวอย่างที่ตรงกัน)

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## ฟีเจอร์การถอดเสียงเป็นคำ

### การตรวจหาภาษาอัตโนมัติ

โดยค่าเริ่มต้น การละเว้น `language_codes` หรือการตั้งค่า `language_codes=[]` จะเปิดใช้การระบุภาษาอัตโนมัติ โมเดลจะตรวจจับภาษาที่พูดในคำพูดต่างๆ แบบไดนามิก รวมถึงการสนทนาหลายภาษาและการสลับภาษา

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### คำแนะนำภาษาที่เฉพาะเจาะจง

ระบุรหัสภาษา BCP-47 อย่างชัดเจน (เช่น `["es-ES"]` สำหรับภาษาสเปนหรือ `["fr-FR"]` สำหรับภาษาฝรั่งเศส) เพื่อให้การจดจำภาษาเฉพาะเจาะจงมีความแม่นยำมากขึ้น (ดู[ภาษาที่รองรับ](#supported-languages))

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### การเอนเอียงคำศัพท์ที่กำหนดเอง

ระบุรายการวลี คำนามเฉพาะ ชื่อแบรนด์ หรือคำศัพท์ทางเทคนิคได้สูงสุด 1,000 รายการใน `custom_vocabulary` เพื่อให้การจดจำเสียงเอนเอียงไปทางคำศัพท์เฉพาะ (โดยปกติแล้วจะได้รับผลลัพธ์ที่ดีที่สุดเมื่อใช้คำศัพท์ไม่เกิน 100 รายการ)

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### การถอดเสียงเป็นคำอัจฉริยะ

กำหนดค่าการจัดรูปแบบเอาต์พุตการถอดเสียงโดยใช้พารามิเตอร์ `mode` ใน `input_audio_transcription`

- **`VERBATIM` (ค่าเริ่มต้น)**: สร้างข้อความถอดเสียงตามตัวอักษรที่ตรงกันทุกประการของทุกสิ่งที่พูด โดยเก็บคำฟุ่มเฟือยดิบ ("เอ่อ", "อืม", "แบบว่า"), การพูดซ้ำ และการพูดที่เริ่มต้นไม่ถูกต้อง
- **`SMART` (การถอดเสียงอัจฉริยะ)**: จัดระเบียบและจัดโครงสร้างข้อความถอดเสียงเพื่อให้สามารถอ่านได้

  - **การนำคำพูดที่ไม่มีความหมายออก**: นำคำพูดที่ไม่มีความหมาย การพูดติดขัด และการเริ่มต้นที่ไม่ถูกต้องออก
  - **การแก้คำพูดของตัวเองในบรรทัด**: แก้คำพูดที่พูดผิดอย่างเป็นธรรมชาติ
  - **การจัดรูปแบบที่มีโครงสร้าง**: จัดรูปแบบรายการ สัญลักษณ์หัวข้อย่อย ตัวเลข วันที่ และการขึ้นย่อหน้าโดยอัตโนมัติ
  - **ไวยากรณ์และการใช้อักษรตัวพิมพ์**: ใช้การใช้อักษรตัวพิมพ์ใหญ่และการปรับเครื่องหมายวรรคตอนที่เป็นธรรมชาติ

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## กลยุทธ์การตรวจจับกิจกรรมเสียงพูด (VAD)

### VAD อัตโนมัติ (ค่าเริ่มต้น)

โดยค่าเริ่มต้น การตรวจหาการพูดอัตโนมัติฝั่งเซิร์ฟเวอร์จะตรวจหาเมื่อผู้พูดเริ่มและหยุดพูด

### VAD แบบไฮบริด

[VAD แบบไฮบริด](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th#hybrid-vad)จะรวมการตรวจหาจุดเริ่มต้นของคำพูดอัตโนมัติฝั่งเซิร์ฟเวอร์กับการตรวจหาจุดสิ้นสุดของคำพูดฝั่งไคลเอ็นต์เพื่อสรุปคำพูดโดยไม่มีเวลาในการตอบสนอง

1. **ระบบจะยังคงเปิดใช้ VAD อัตโนมัติฝั่งเซิร์ฟเวอร์**เพื่อตรวจจับจุดเริ่มต้นของคำพูดได้อย่างแม่นยำด้วยการเพิ่มเสียงนำหน้า ซึ่งจะช่วยป้องกันไม่ให้คำแรกขาดหายไป
2. **VAD ฝั่งไคลเอ็นต์ตรวจจับความเงียบ**: เมื่อ VAD ในอุปกรณ์ตรวจจับว่าผู้พูดหยุดพูดแล้ว ไคลเอ็นต์จะส่งสัญญาณ `audio_stream_end` ทันที
3. **การสรุปอย่างรวดเร็ว**: เซิร์ฟเวอร์จะถือว่า `audio_stream_end` เป็นพรอมต์การสรุปแบบทันที โดยข้ามเวลาในการรอให้ฝั่งเซิร์ฟเวอร์เงียบตามค่าเริ่มต้น และแสดงข้อความถอดเสียงที่สรุปแล้วโดยมีเวลาในการตอบสนองน้อยที่สุด
4. **การสำรอง**: หาก VAD ฝั่งไคลเอ็นต์ไม่ทริกเกอร์ VAD ฝั่งเซิร์ฟเวอร์จะทำหน้าที่เป็นการสำรองอัตโนมัติ

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### VAD ด้วยตนเอง (กดเพื่อพูด)

สำหรับอินเทอร์เฟซวอล์คกี้ทอล์คกี้หรือปุ่มกดเพื่อพูด ให้ปิดใช้ VAD อัตโนมัติทั้งหมดและควบคุมขอบเขตการพูดอย่างชัดเจนโดยใช้ `activity_start` และ `activity_end` ดังนี้

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## โทเค็นชั่วคราวในแอปพลิเคชันไคลเอ็นต์

สำหรับแอปพลิเคชันไคลเอ็นต์ต่อเซิร์ฟเวอร์ (เช่น แอปบนอุปกรณ์เคลื่อนที่หรือเว็บแอปที่สตรีมจากไมโครโฟนโดยตรง) ให้ใช้[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th)เพื่อหลีกเลี่ยงการเปิดเผยคีย์ API ในโค้ดฝั่งไคลเอ็นต์

สร้างโทเค็นชั่วคราวที่จำกัดในเซิร์ฟเวอร์ก่อนเริ่มการเชื่อมต่อไคลเอ็นต์

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
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
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## ภาษาที่รองรับ

Gemini 3.5 Transcribe Live รองรับภาษาและรหัสภาษา BCP-47 ต่อไปนี้

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| อาฟรีกานส์ | `af-ZA` | ญี่ปุ่น | `ja-JP` |
| อัมฮาริก | `am-ET` | ชวา | `jv-ID` |
| อาหรับ (อียิปต์) | `ar-EG` | คาบูเวอร์เดียนู | `kea-CV` |
| อาร์เมเนีย | `hy-AM` | กันนาดา | `kn-IN` |
| อัสสัม | `as-IN` | คาซัค | `kk-KZ` |
| อาร์เซอร์ไบจัน | `az-AZ` | เกาหลี | `ko-KR` |
| เบลารุส | `be-BY` | คีร์กิซ | `ky-KG` |
| เบงกาลี (บังกลาเทศ) | `bn-BD` | ลัตเวีย | `lv-LV` |
| เบงกาลี (อินเดีย) | `bn-IN` | ลิงกาลา | `ln-CD` |
| บอสเนีย | `bs-BA` | ลิทัวเนีย | `lt-LT` |
| บัลแกเรีย | `bg-BG` | มาซีโดเนีย | `mk-MK` |
| บัลแกเรีย (อโรมาเนีย) | `rup-BG` | มาเลย์ | `ms-MY` |
| พม่า | `my-MM` | มาลายาลัม | `ml-IN` |
| จีนกวางตุ้ง (ตัวเต็ม) | `yue-Hant-HK` | มอลตา | `mt-MT` |
| คาตาลัน | `ca-ES` | จีนกลาง (ตัวย่อ) | `cmn-Hans-CN` |
| ซีบัวโน | `ceb` | มราฐี | `mr-IN` |
| เขมรตอนกลาง | `km-KH` | มองโกเลีย | `mn-MN` |
| โครเอเชีย | `hr-HR` | เนปาล | `ne-NP` |
| เช็ก | `cs-CZ` | นอร์เวย์ | `nb-NO` |
| เดนมาร์ก | `da-DK` | โอริยา | `or-IN` |
| ดัตช์ | `nl-NL` | โปแลนด์ | `pl-PL` |
| อังกฤษ (บริเตนใหญ่) | `en-GB` | โปรตุเกส (บราซิล) | `pt-BR` |
| อังกฤษ (อินเดีย) | `en-IN` | โปรตุเกส (โปรตุเกส) | `pt-PT` |
| อังกฤษ (สหรัฐอเมริกา) | `en-US` | ปัญจาบ | `pa-IN` |
| เอสโตเนีย | `et-EE` | ปัญจาบ (สคริปต์คุรมุขี) | `pa-Guru-IN` |
| ฟาร์ซี | `fa-IR` | โรมาเนีย | `ro-RO` |
| ฟิลิปปินส์ | `fil-PH` | รัสเซีย | `ru-RU` |
| ฟินแลนด์ | `fi-FI` | เซอร์เบีย | `sr-RS` |
| ฝรั่งเศส | `fr-FR` | ภาษาสินธี (อักษรอาหรับ) | `sd-Arab-IN` |
| กาลิเชียน | `gl-ES` | สโลวัก | `sk-SK` |
| จอร์เจีย | `ka-GE` | สโลวีเนีย | `sl-SI` |
| เยอรมัน | `de-DE` | สเปน (ลาตินอเมริกา) | `es-419` |
| กรีก | `el-GR` | สเปน (สหรัฐอเมริกา) | `es-US` |
| คุชราต | `gu-IN` | สวาฮีลี (เคนยา) | `sw-KE` |
| เฮาซา | `ha-NG` | สวีเดน | `sv-SE` |
| ฮีบรู | `he-IL` | ทาจิก | `tg-TJ` |
| ฮินดี | `hi-IN` | เตลูกู | `te-IN` |
| ฮังการี | `hu-HU` | ไทย | `th-TH` |
| ไอซ์แลนด์ | `is-IS` | ตุรกี | `tr-TR` |
| อังกฤษ (อินเดีย) | `en-IN` | ยูเครน | `uk-UA` |
| อินโดนีเซีย | `id-ID` | อุซเบก | `uz-UZ` |
| อิตาลี | `it-IT` | เวียดนาม | `vi-VN` |

## ข้อมูลอ้างอิงพารามิเตอร์

กำหนดค่าการถอดเสียงเป็นคำแบบสดโดยใช้ช่องใน `input_audio_transcription` และ `realtime_input_config` ดังนี้

| พารามิเตอร์ | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `language_codes` | อาร์เรย์ของสตริง | รหัสภาษา BCP-47 (เช่น `["en-US"]`) หากเว้นว่างหรือไม่มีค่า (`[]`) โมเดลจะตรวจหาภาษาโดยอัตโนมัติและจัดการคำพูดหลายภาษา |
| `custom_vocabulary` | อาร์เรย์ของสตริง | คำที่กำหนดเอง ตัวย่อ ชื่อแบรนด์ หรือคำนามเฉพาะสูงสุด 1,000 คำเพื่อปรับการจดจำเสียง |
| `mode` | สตริง | โหมดการถอดเสียงเป็นคำ: `"VERBATIM"` (ค่าเริ่มต้น) หรือ `"SMART"` (การถอดเสียงเป็นคำอัจฉริยะ) เมื่อตั้งค่าเป็น `"SMART"` โมเดลจะนำคำพูดที่ไม่มีความหมายออก จัดรูปแบบรายการ และแก้ไขความไม่คล่องแคล่ว |
| `automatic_activity_detection.disabled` | บูลีน | ตั้งค่าเป็น `true` เพื่อปิดใช้การตรวจจับกิจกรรมเสียงพูดอัตโนมัติ และส่งสัญญาณ `activityStart` และ `activityEnd` ด้วยตนเอง |

### ฟิลด์การตอบกลับของเซิร์ฟเวอร์

| ช่อง | คำอธิบาย |
| --- | --- |
| `server_content.interim_input_transcription` | สมมติฐานการถอดเสียงบางส่วนชั่วคราวที่มีเวลาในการตอบสนองต่ำจะแสดงอย่างต่อเนื่องขณะที่ผู้ใช้กำลังพูด |
| `server_content.input_transcription` | ข้อความถอดเสียงอินพุตที่เชื่อถือได้และสรุปแล้วจะแสดงเมื่อการพูดจบลง |

## ข้อจำกัด

- **ระยะเวลาเซสชัน:** เซสชันการถอดเสียงเป็นคำแบบสดรองรับการสตรีมอย่างต่อเนื่องได้นานสูงสุด 10 นาที
- **การระบุผู้พูด:** เซสชันไลฟ์สดไม่รองรับการระบุผู้พูด สำหรับการระบุผู้พูด ให้ใช้ปลายทาง[การถอดเสียงเป็นคำ](https://ai.google.dev/gemini-api/docs/transcribe?hl=th#speaker-diarization)แบบไม่สตรีม
- **การประทับเวลาระดับคำ:** ระบบไม่รองรับการประทับเวลาระดับคำผ่าน Live API Live API จะปล่อยการประทับเวลาระดับคำพูด (`interim_input_transcription` และ `input_transcription`)
- **คำศัพท์ที่กำหนดเอง:** คุณระบุคำได้สูงสุด 1,000 คำใน `custom_vocabulary` แต่โดยปกติแล้วการระบุคำสูงสุด 100 คำจะให้ผลลัพธ์ที่ดีที่สุด
- **ความเข้ากันได้ของโหมด:** การถอดเสียงอัจฉริยะ (`"mode": "SMART"`) จะนำคำฟุ่มเฟือยออกและจัดรูปแบบข้อความที่รับรู้เจตนา แต่จะใช้ร่วมกับคำอธิบายประกอบของคำไม่ได้

## ขั้นตอนถัดไป

- อ่าน[เอกสารประกอบการถอดเสียงของ Gemini](https://ai.google.dev/gemini-api/docs/transcribe?hl=th) สำหรับไฟล์เสียงที่ไม่ได้สตรีม
- อ่าน[ภาพรวมของ Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th) สำหรับเอเจนต์เสียงแบบสนทนา
- อ่าน[คู่มือการแปลสด](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th)สำหรับการแปลเสียงพูดเป็นคำพูดแบบเรียลไทม์
- ดูราคาการสตรีมผ่าน Live API ได้ที่[หน้าการกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.5-transcribe-live)
- ดู[คู่มือความสามารถของ Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-10 UTC"],[],[]]
