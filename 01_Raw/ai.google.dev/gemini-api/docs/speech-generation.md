---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=th
fetched_at: 2026-09-07T05:45:17.635010+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e01\u0e32\u0e23\u0e2d\u0e48\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้างการอ่านออกเสียงข้อความ (TTS)

Gemini API สามารถเปลี่ยนอินพุตข้อความเป็นเสียงแบบผู้พูดคนเดียวหรือหลายคน
โดยใช้ความสามารถในการสร้างข้อความเป็นเสียง (TTS) ของ Gemini
การสร้างการอ่านออกเสียงข้อความ (TTS) เป็นแบบ*[ควบคุมได้](#controllable)*
ซึ่งหมายความว่าคุณสามารถใช้ภาษาธรรมชาติเพื่อจัดโครงสร้างการโต้ตอบและกำหนด*สไตล์* *สำเนียง* *จังหวะ* และ*โทนเสียง*ของเสียงได้

ความสามารถของ TTS แตกต่างจากการสร้างคำพูดที่ให้บริการผ่าน [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ซึ่งออกแบบมาสำหรับเสียงแบบโต้ตอบที่ไม่มีโครงสร้าง รวมถึงอินพุตและเอาต์พุตแบบหลายรูปแบบ แม้ว่า Live API จะโดดเด่น
ในบริบทการสนทนาแบบไดนามิก แต่ TTS ผ่าน Gemini API
ได้รับการปรับแต่งสำหรับสถานการณ์ที่ต้องมีการอ่านข้อความที่แน่นอนพร้อมการควบคุม
สไตล์และเสียงอย่างละเอียด เช่น การสร้างพอดแคสต์หรือหนังสือเสียง

คู่มือนี้จะแสดงวิธีสร้างเสียงแบบผู้พูดคนเดียวและแบบผู้พูดหลายคนจากข้อความ

## ก่อนเริ่มต้น

ตรวจสอบว่าคุณใช้โมเดล Gemini 2.5 ที่มีฟีเจอร์ข้อความเป็นเสียง (TTS) ของ Gemini ตามที่ระบุไว้ในส่วน[โมเดลที่รองรับ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#supported-models)
โปรดพิจารณาว่าโมเดลใดเหมาะกับกรณีการใช้งานเฉพาะของคุณมากที่สุดเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

คุณอาจเห็นว่าการ[ทดสอบโมเดล TTS ของ Gemini ใน AI Studio](https://aistudio.google.com/generate-speech?hl=th) มีประโยชน์ก่อนที่จะเริ่มสร้าง

## TTS แบบผู้พูดคนเดียว

หากต้องการแปลงข้อความเป็นเสียงแบบลำโพงเดียว ให้ตั้งค่ารูปแบบการตอบกลับเป็น "เสียง"
และส่งออบเจ็กต์ `speech_config` พร้อมชื่อเสียง
คุณจะต้องเลือกชื่อเสียงจาก[เสียงเอาต์พุต](#voices)ที่สร้างไว้ล่วงหน้า

ตัวอย่างนี้จะบันทึกเสียงเอาต์พุตจากโมเดลในไฟล์ Wave

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
       "type": "audio"
     },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

คุณสามารถดึงข้อมูลเสียงที่สร้างขึ้นได้โดยใช้พร็อพเพอร์ตี้ `interaction.output_audio`
ซึ่งจะแสดงผลบล็อกเสียงที่สร้างล่าสุด ดูรายละเอียดเกี่ยวกับพร็อพเพอร์ตี้ความสะดวกได้ที่[ภาพรวมของการโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th#convenience-properties)

## TTS แบบหลายผู้พูด

สำหรับเสียงแบบหลายลำโพง คุณจะต้องมีออบเจ็กต์ `multi_speaker_voice_config` ที่กำหนดค่าลำโพงแต่ละตัว (สูงสุด 2 ตัว) เป็น `speaker_voice_config`
คุณจะต้องกําหนด `speaker` แต่ละรายการด้วยชื่อเดียวกันกับที่ใช้ใน[พรอมต์](#controllable) ดังนี้

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_format={"type": "audio"},
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_format": {
       "type": "audio"
     },
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## ควบคุมสไตล์การพูดด้วยพรอมต์

คุณควบคุมสไตล์ น้ำเสียง สำเนียง และจังหวะได้โดยใช้พรอมต์ภาษาธรรมชาติ
สำหรับการอ่านออกเสียงข้อความ (TTS) แบบเสียงเดียวและหลายเสียง
ตัวอย่างเช่น ในพรอมต์ที่มีผู้พูดคนเดียว คุณอาจพูดว่า

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

ในพรอมต์ที่มีผู้พูดหลายคน ให้ระบุชื่อของผู้พูดแต่ละคนและ
ข้อความถอดเสียงที่เกี่ยวข้องแก่โมเดล นอกจากนี้ คุณยังให้คำแนะนำแก่ผู้พูดแต่ละคน
ได้ด้วย

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

ลองใช้[ตัวเลือกเสียง](#voices)ที่สอดคล้องกับสไตล์หรืออารมณ์ที่คุณต้องการสื่อ เพื่อเน้นย้ำให้ชัดเจนยิ่งขึ้น เช่น ในพรอมต์ก่อนหน้า เสียงลมของ *Enceladus* อาจเน้นคำว่า "เหนื่อย" และ "เบื่อ" ในขณะที่โทนเสียงที่ร่าเริงของ *Puck* อาจเสริมคำว่า "ตื่นเต้น" และ "มีความสุข"

## สร้างพรอมต์เพื่อแปลงเป็นเสียง

โมเดล TTS จะแสดงผลเฉพาะเสียง แต่คุณสามารถใช้[โมเดลอื่นๆ](https://ai.google.dev/gemini-api/docs/models?hl=th) เพื่อสร้างข้อความถอดเสียงก่อน
แล้วส่งข้อความถอดเสียงนั้นไปยังโมเดล TTS เพื่ออ่านออกเสียง

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.6-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_format={"type": "audio"},
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.6-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_format: { type: 'audio' },
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## การสร้างคำพูดแบบสตรีมมิง

คุณสามารถสตรีมเสียงที่โมเดลสร้างขึ้นขณะที่โมเดลกำลังสร้างเสียงได้โดยการตั้งค่า `stream: true`

### Python

```
from google import genai
import base64

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
      stream: true
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"       -H "x-goog-api-key: $GEMINI_API_KEY"       -H "Content-Type: application/json"       -H "Api-Revision: 2026-05-20"       --no-buffer       -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## ตัวเลือกเสียง

โมเดล TTS รองรับตัวเลือกเสียง 30 แบบต่อไปนี้ในฟิลด์ `voice_name`

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** - *Upbeat* | **Charon** - *ให้ข้อมูล* |
| **เกาหลี** -- *Firm* | **Fenrir** - *ตื่นเต้นง่าย* | **Leda** -- *วัยรุ่น* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *สบายๆ* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *สบายๆ* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *ล้าง* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *ให้ข้อมูล* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *ผู้ใหญ่* | **Pulcherrima** -- *Forward* |
| **Achird** -- *เป็นมิตร* | **Zubenelgenubi** -- *สบายๆ* | **Vindemiatrix** -- *อ่อนโยน* |
| **Sadachbia** -- *มีชีวิตชีวา* | **Sadaltager** -- *มีความรู้* | **Sulafat** -- *Warm* |

คุณสามารถฟังตัวเลือกเสียงทั้งหมดได้ใน [AI Studio](https://aistudio.google.com/generate-speech?hl=th)

## ภาษาที่รองรับ

โมเดล TTS จะตรวจหาภาษาที่ป้อนโดยอัตโนมัติ ภาษาที่รองรับมีดังนี้

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| อาหรับ | ar | ฟิลิปปินส์ | fil |
| เบงกอล | bn | ฟินแลนด์ | fi |
| ดัตช์ | nl | กาลิเชียน | gl |
| อังกฤษ | en | จอร์เจีย | ka |
| ฝรั่งเศส | fr | กรีก | el |
| เยอรมัน | de | คุชราต | gu |
| ฮินดี | hi | เฮติครีโอล | ht |
| อินโดนีเซีย | id | ฮีบรู | เขา |
| อิตาลี | it | ฮังการี | hu |
| ญี่ปุ่น | ja | ไอซ์แลนด์ | is |
| เกาหลี | ko | ชวา | jv |
| มราฐี | mr | กันนาดา | kn |
| โปแลนด์ | pl | กงกณี | kok |
| โปรตุเกส | pt | ภาษาลาว | lo |
| โรมาเนีย | ro | ลาติน | la |
| รัสเซีย | ru | ลัตเวีย | lv |
| สเปน | es | ลิทัวเนีย | lt |
| ทมิฬ | ta | ลักเซมเบิร์ก | ปอนด์ |
| เตลูกู | te | มาซีโดเนีย | mk |
| ไทย | th | ไมถิลี | mai |
| ตุรกี | tr | มาลากาซี | มก. |
| ยูเครน | uk | มาเลย์ | มิลลิวินาที |
| เวียดนาม | vi | มาลายาลัม | ml |
| อาฟรีกานส์ | af | มองโกเลีย | mn |
| แอลเบเนีย | sq | เนปาล | ne |
| อัมฮาริก | am | นอร์เวย์ (บ็อกมอล) | nb |
| อาร์เมเนีย | hy | นอร์เวย์ (นีนอสก์) | nn |
| อาร์เซอร์ไบจัน | az | โอเดีย | หรือ |
| บาสก์ | eu | พาชตู | ps |
| เบลารุส | be | เปอร์เซีย | fa |
| บัลแกเรีย | bg | ปัญจาบ | pa |
| พม่า | my | เซอร์เบีย | sr |
| คาตาลัน | ca | สินธี | SD |
| ซีบัวโน | ceb | สิงหล | si |
| จีนกลาง | cmn | สโลวัก | sk |
| โครเอเชีย | ชม. | สโลวีเนีย | sl |
| เช็ก | cs | สวาฮิลี | sw |
| เดนมาร์ก | da | สวีเดน | sv |
| เอสโตเนีย | et | อูรดู | ur |

## รุ่นที่รองรับ

| รุ่น | ผู้พูดคนเดียว | Multispeaker |
| --- | --- | --- |
| [ตัวอย่าง TTS ของ Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=th) | ✔️ | ✔️ |
| [TTS ของ Gemini 2.5 Flash (เวอร์ชันตัวอย่าง)](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=th) | ✔️ | ✔️ |
| [TTS เวอร์ชันตัวอย่างของ Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=th) | ✔️ | ✔️ |

## คำแนะนำในการเขียนพรอมต์

โมเดล**การสร้างเสียงแบบเนทีฟของ Gemini Native Audio Generation Text-to-Speech (TTS)** แตกต่างจากโมเดล TTS ทั่วไปโดยใช้โมเดลภาษาขนาดใหญ่ที่***ไม่เพียงรู้ว่าจะพูดอะไร แต่ยังรู้วิธีพูดด้วย***

คุณอาจมองว่าพรอมต์ขั้นสูงเป็นคำสั่งของระบบที่โมเดลต้อง
ทำตาม ซึ่งเป็นวิธีให้บริบทแก่โมเดลมากขึ้นและควบคุมประสิทธิภาพได้

หากต้องการปลดล็อกความสามารถนี้ ผู้ใช้สามารถคิดว่าตนเองเป็นผู้กำกับที่กำลังจัดฉาก
ให้ผู้พากย์เสมือนจริงแสดง เราขอแนะนำให้คุณพิจารณาส่วนประกอบต่อไปนี้ในการสร้างพรอมต์
**โปรไฟล์เสียง**ที่กำหนดตัวตนหลักและต้นแบบของตัวละคร
**คำอธิบายฉาก**ที่สร้างสภาพแวดล้อมทางกายภาพและ"กลิ่นอาย" ทางอารมณ์ และ**หมายเหตุของผู้กำกับ**ที่ให้คำแนะนำด้านการแสดงที่แม่นยำยิ่งขึ้นเกี่ยวกับสไตล์ สำเนียง และการควบคุมจังหวะ

การให้คำสั่งที่ละเอียด เช่น สำเนียงเฉพาะภูมิภาค ลักษณะทางภาษาที่เฉพาะเจาะจง (เช่น เสียงลม) หรือจังหวะ จะช่วยให้ผู้ใช้ใช้ประโยชน์จากการรับรู้บริบทของโมเดลเพื่อสร้างเสียงที่มีความเคลื่อนไหว เป็นธรรมชาติ และสื่ออารมณ์สูง เราขอแนะนำให้**ข้อความถอดเสียง**และพรอมต์ของผู้กำกับสอดคล้องกันเพื่อให้  *"ใครเป็นคนพูด"* ตรงกับ *"สิ่งที่พูด"* และ *"วิธีการพูด"* เพื่อให้ได้ประสิทธิภาพสูงสุด

จุดประสงค์ของคู่มือนี้คือการให้คำแนะนำพื้นฐานและจุดประกายไอเดียเมื่อ
พัฒนาประสบการณ์ด้านเสียงโดยใช้การสร้างเสียง TTS ของ Gemini เราตื่นเต้น
ที่จะได้เห็นผลงานของคุณ

### แท็กเสียง

แท็กคือตัวแก้ไขในบรรทัด เช่น `[whispers]` หรือ `[laughs]` ที่ช่วยให้คุณควบคุมการนำส่งได้อย่างละเอียด
คุณสามารถใช้เครื่องหมายเหล่านี้เพื่อเปลี่ยนน้ำเสียง จังหวะ และ
อารมณ์ของบรรทัดหรือส่วนของข้อความถอดเสียงได้ คุณยังใช้สติกเกอร์เหล่านี้เพื่อ
เพิ่มคำอุทานและเสียงอื่นๆ ที่ไม่ใช่คำพูดลงในการแสดงได้ด้วย เช่น
`[cough]`, `[sighs]` หรือ `[gasp]`

ไม่มีรายการที่ครอบคลุมว่าแท็กใดใช้ได้และใช้ไม่ได้ เราขอแนะนําให้
ทดลองใช้อารมณ์และคำพูดต่างๆ เพื่อดูว่าเอาต์พุต
เปลี่ยนแปลงไปอย่างไร

หากข้อความถอดเสียงไม่ได้เป็นภาษาอังกฤษ เราขอแนะนำให้คุณ
ยังคงใช้แท็กเสียงภาษาอังกฤษเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

**ใช้แท็กเสียงอย่างสร้างสรรค์**

เพื่อแสดงให้เห็นถึงความหลากหลายที่คุณจะได้รับจากแท็กเสียง ต่อไปนี้คือชุด
ตัวอย่างที่แต่ละตัวอย่างพูดถึงสิ่งเดียวกัน แต่การนำส่งจะเปลี่ยนแปลงไปตาม
แท็กที่ใช้

คุณเปลี่ยนการเน้นการนำส่งได้โดยเพิ่มแท็กที่จุดเริ่มต้นของ
บรรทัดเพื่อให้ผู้พูดตื่นเต้น เบื่อ หรือไม่เต็มใจ

- `[excitedly]` สวัสดี ฉันเป็นโมเดลแปลงข้อความเป็นคำพูดตัวใหม่ และพูดได้หลายแบบ
  วันนี้มีอะไรให้ช่วยบ้าง
- `[bored]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…
- `[reluctantly]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…

นอกจากนี้ คุณยังใช้แท็กเพื่อเปลี่ยนจังหวะการอ่านหรือรวมจังหวะ
กับการเน้นได้ด้วย

- `[very fast]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…
- `[very slow]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…
- `[sarcastically, one painfully slow word at a time]` สวัสดี ฉันเป็นโมเดลใหม่สำหรับ
  การแปลงข้อความเป็นคำพูด…

นอกจากนี้ คุณยังควบคุมส่วนต่างๆ ได้อย่างแม่นยำ ซึ่งหมายความว่าคุณสามารถกระซิบ
ส่วนหนึ่งและตะโกนอีกส่วนหนึ่งได้

- `[whispers]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงรุ่นใหม่ `[shouting]` และพูดได้หลายแบบ
  `[whispers]` วันนี้คุณต้องการความช่วยเหลือเรื่องใด

นอกจากนี้ คุณยังทดลองใช้ไอเดียครีเอทีฟโฆษณาที่ต้องการได้ด้วย

- `[like a cartoon dog]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…
- `[like dracula]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดใหม่…

แท็กที่ใช้กันโดยทั่วไป ได้แก่

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

แท็กช่วยให้ควบคุมการส่งข้อความถอดเสียงได้อย่างรวดเร็ว หากต้องการควบคุมมากยิ่งขึ้น คุณสามารถใช้ร่วมกับพรอมต์บริบทเพื่อกำหนดโทนและบรรยากาศโดยรวมของประสิทธิภาพได้

### โครงสร้างพรอมต์

พรอมต์ที่มีประสิทธิภาพควรมีองค์ประกอบต่อไปนี้ซึ่งทำงานร่วมกันเพื่อ
สร้างประสิทธิภาพที่ยอดเยี่ยม

- **โปรไฟล์เสียง** - สร้างลักษณะตัวตนของเสียง โดยกำหนดเอกลักษณ์ของตัวละคร ต้นแบบ และลักษณะอื่นๆ เช่น อายุ ภูมิหลัง ฯลฯ
- **ฉาก** - เตรียมความพร้อม อธิบายทั้งสภาพแวดล้อมทางกายภาพและ"บรรยากาศ"
- **หมายเหตุจากผู้กำกับ** - คำแนะนำด้านประสิทธิภาพที่คุณสามารถแจกแจงคำสั่งที่สำคัญสำหรับพรสวรรค์เสมือนให้จดบันทึกได้ ตัวอย่างเช่น
  สไตล์การพูด การหายใจ การเว้นจังหวะ การออกเสียง และสำเนียง
- **บริบทตัวอย่าง** - ให้จุดเริ่มต้นตามบริบทแก่โมเดล เพื่อให้
  นักแสดงเสมือนเข้าสู่ฉากที่คุณตั้งค่าไว้อย่างเป็นธรรมชาติ
- **ข้อความ** - ข้อความที่โมเดลจะพูด โปรดทราบว่าหัวข้อของข้อความถอดเสียงและรูปแบบการเขียนควรสอดคล้องกับ
  คำสั่งที่คุณให้เพื่อประสิทธิภาพที่ดีที่สุด
- **แท็กเสียง** - ตัวแก้ไขที่คุณใส่ลงในข้อความถอดเสียงเพื่อเปลี่ยนวิธีแสดงข้อความบางส่วน เช่น `[whispers]` หรือ `[shouting]`

ตัวอย่างพรอมต์แบบเต็ม

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### กลยุทธ์การแจ้งโดยละเอียด

แยกย่อยแต่ละองค์ประกอบของพรอมต์ดังนี้

#### โปรไฟล์เสียง

อธิบายตัวตนของตัวละครโดยย่อ

- **ชื่อ** การตั้งชื่อตัวละครจะช่วยให้โมเดลและ
  การแสดงเชื่อมโยงกันอย่างใกล้ชิด โปรดอ้างอิงถึงตัวละครด้วยชื่อเมื่อตั้งค่าฉากและ
  บริบท
- **บทบาท** ตัวตนหลักและต้นแบบของตัวละครที่กำลังแสดงในฉาก เช่น ดีเจวิทยุ ผู้จัดพอดแคสต์ ผู้สื่อข่าว เป็นต้น

ตัวอย่าง

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### บรรยากาศ

กำหนดบริบทของฉาก รวมถึงสถานที่ อารมณ์ และรายละเอียดด้านสิ่งแวดล้อม
ที่สร้างโทนและบรรยากาศ อธิบายสิ่งที่เกิดขึ้นรอบตัว
ตัวละครและผลกระทบที่มีต่อตัวละคร ฉากจะให้บริบทด้านสภาพแวดล้อม
สำหรับการโต้ตอบทั้งหมดและเป็นแนวทางในการแสดง
อย่างเป็นธรรมชาติ

ตัวอย่าง

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### หมายเหตุของผู้กำกับ

ส่วนสำคัญนี้มีคำแนะนำด้านประสิทธิภาพที่เฉพาะเจาะจง คุณข้ามองค์ประกอบอื่นๆ ทั้งหมดได้ แต่เราขอแนะนำให้รวมองค์ประกอบนี้ไว้

กำหนดเฉพาะสิ่งที่สำคัญต่อประสิทธิภาพ โดยระมัดระวังไม่ให้
ระบุมากเกินไป กฎที่เข้มงวดมากเกินไปจะจำกัดความคิดสร้างสรรค์ของโมเดลและอาจ
ส่งผลให้ประสิทธิภาพแย่ลง ปรับสมดุลบทบาทและคำอธิบายฉากกับ
กฎการแสดงเฉพาะ

คำแนะนำที่พบบ่อยที่สุดคือ**สไตล์ จังหวะ และสำเนียง** แต่โมเดลไม่ได้จำกัดอยู่เพียงคำแนะนำเหล่านี้ และไม่จำเป็นต้องใช้คำแนะนำเหล่านี้ คุณสามารถใส่คำสั่งที่กำหนดเองเพื่อระบุรายละเอียดเพิ่มเติมที่สำคัญต่อประสิทธิภาพ และระบุรายละเอียดมากหรือน้อยเท่าที่จำเป็น

เช่น

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**รูปแบบ:**

กำหนดโทนและสไตล์ของเสียงพูดที่สร้างขึ้น ระบุอารมณ์ เช่น สดใส
กระตือรือร้น ผ่อนคลาย เบื่อ ฯลฯ เพื่อเป็นแนวทางในการแสดง อธิบายให้ชัดเจนและ
ให้รายละเอียดมากที่สุดเท่าที่จำเป็น: *"ความกระตือรือร้นที่แพร่หลาย ผู้ฟัง
ควรรู้สึกเหมือนเป็นส่วนหนึ่งของกิจกรรมชุมชนที่ยิ่งใหญ่และน่าตื่นเต้น"* ได้ผลดีกว่าการพูดว่า *"กระตือรือร้นและกระปรี้กระเปร่า"*

คุณอาจลองใช้คำที่ได้รับความนิยมในอุตสาหกรรมเสียงบรรยาย เช่น "เสียง
ยิ้ม" คุณซ้อนลักษณะสไตล์ได้มากเท่าที่ต้องการ

ตัวอย่าง

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

ความลึกมากขึ้น

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

ซับซ้อน

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**เครื่องหมายแสดงการเน้นเสียง:**

อธิบายสำเนียงที่เลือก ยิ่งเจาะจงมากเท่าไหร่ ผลลัพธ์ก็จะยิ่งดีขึ้นเท่านั้น เช่น ใช้ "*สำเนียงภาษาอังกฤษแบบอังกฤษที่ได้ยินในครอยดอน
ประเทศอังกฤษ*" แทน "*สำเนียงอังกฤษ*"

ตัวอย่าง

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**การกำหนดอัตราการแสดงโฆษณา:**

การกำหนดจังหวะโดยรวมและความหลากหลายของจังหวะตลอดทั้งเพลง

ตัวอย่าง

เรียบง่าย

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

ความลึกเพิ่มเติม

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

ซับซ้อน

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**ลองใช้เลย**

ลองใช้ตัวอย่างเหล่านี้ด้วยตัวคุณเองใน[แอป TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=th) แล้วให้ Gemini
เป็นผู้กำกับ โปรดคำนึงถึงเคล็ดลับต่อไปนี้เพื่อสร้างการแสดงเสียงร้องที่ยอดเยี่ยม

- อย่าลืมทำให้พรอมต์ทั้งหมดสอดคล้องกัน โดยสคริปต์และคำสั่งจะทำงานร่วมกันในการสร้างการแสดงที่ยอดเยี่ยม
- คุณไม่จำเป็นต้องอธิบายทุกอย่าง บางครั้งการเว้นช่องว่างให้โมเดลเติมเต็มจะช่วยให้เป็นธรรมชาติมากขึ้น (เหมือนนักแสดงมากความสามารถ)
- หากคุณรู้สึกตัน ให้ Gemini ช่วยคุณร่างสคริปต์หรือการแสดง

## ข้อจำกัด

- โมเดล TTS รับได้เฉพาะข้อความที่ป้อนและสร้างเอาต์พุตเสียงเท่านั้น
- เซสชัน TTS มีขีดจำกัด[หน้าต่างบริบท](https://ai.google.dev/gemini-api/docs/long-context?hl=th)ที่ 32,000 โทเค็น
- ดูส่วน[ภาษา](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#languages)เพื่อดูการรองรับภาษา
- TTS ไม่รองรับการสตรีม ยกเว้นเมื่อใช้ `gemini-3.1-flash-tts-preview`

ข้อจำกัดต่อไปนี้จะมีผลเฉพาะเมื่อใช้โมเดลตัวอย่าง TTS ของ Gemini 3.1 Flash
สำหรับการสร้างคำพูด

- **เสียงไม่สอดคล้องกับวิธีการในพรอมต์:** เอาต์พุตของโมเดลอาจไม่ตรงกับ
  ลำโพงที่เลือกเสมอไป ซึ่งทำให้เสียงที่ได้แตกต่างจากที่คาดไว้
  หากต้องการหลีกเลี่ยงการใช้เสียงที่ไม่ตรงกัน (เช่น เสียงผู้ชายทุ้ม
  พยายามพูดเหมือนเด็กผู้หญิง) ให้ตรวจสอบว่าโทนและบริบทที่เขียนในพรอมต์สอดคล้องกับโปรไฟล์ของลำโพงที่เลือกอย่างเป็นธรรมชาติ
- **คุณภาพของเอาต์พุตที่ยาวขึ้น:** คุณภาพและความสอดคล้องของคำพูดอาจเริ่ม
  เปลี่ยนแปลงไปเมื่อเอาต์พุตที่สร้างขึ้นยาวกว่า 2-3 นาที เราขอแนะนำให้แบ่งข้อความถอดเสียงออกเป็นส่วนเล็กๆ
- **การแสดงผลโทเค็นข้อความเป็นครั้งคราว:** โมเดลจะแสดงผลโทเค็นข้อความ
  แทนโทเค็นเสียงเป็นครั้งคราว ซึ่งทำให้เซิร์ฟเวอร์ไม่สามารถดำเนินการตามคำขอ
  และแสดงข้อผิดพลาด `500` เนื่องจากปัญหานี้เกิดขึ้นแบบสุ่มในคำขอเพียงไม่กี่เปอร์เซ็นต์ คุณจึงควรใช้ตรรกะการลองใหม่โดยอัตโนมัติในแอปพลิเคชันเพื่อจัดการกับปัญหาเหล่านี้
- **การปฏิเสธที่ผิดพลาดของเครื่องมือคัดแยกพรอมต์:** พรอมต์ที่คลุมเครืออาจไม่ทริกเกอร์
  เครื่องมือคัดแยกการสังเคราะห์เสียงพูด ทำให้คำขอถูกปฏิเสธ
  (`PROHIBITED_CONTENT`) หรือทำให้โมเดลอ่านคำสั่งสไตล์และหมายเหตุของผู้กำกับ
  ออกมา ตรวจสอบความถูกต้องของพรอมต์โดยเพิ่มคำนำที่ชัดเจน
  ซึ่งสั่งให้โมเดลสังเคราะห์เสียงพูด และติดป้ายกำกับอย่างชัดเจนว่า
  ข้อความถอดเสียงที่พูดจริงเริ่มต้นที่ใด

## ขั้นตอนถัดไป

- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ของ Gemini มีตัวเลือกการสร้างเสียงแบบอินเทอร์แอกทีฟ
  ที่คุณสามารถสลับกับรูปแบบอื่นๆ ได้
- หากต้องการทำงานกับ*อินพุต*เสียง โปรดไปที่คู่มือ[การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
