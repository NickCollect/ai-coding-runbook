---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=th
fetched_at: 2026-10-19T05:59:14.876659+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a\u0e40\u0e2a\u0e35\u0e22\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การออกแบบเสียง

การออกแบบเสียงช่วยให้คุณสร้างลักษณะเสียงใหม่ถาวรจาก
คำอธิบายภาษาธรรมชาติโดยใช้ปลายทางเสียงของ Gemini API
(`POST /v1beta/voices`) แทนที่จะจำกัดอยู่แค่เสียงที่สร้างไว้ล่วงหน้าหรือ
การบันทึกเสียงอ้างอิง คุณสามารถอธิบายอายุของตัวละคร น้ำเสียง
สำเนียง และการเปล่งเสียงพื้นฐาน แล้วรับรหัส `voice_...` ที่นำกลับมาใช้ใหม่ได้ซึ่งบันทึกไว้ใน
โปรเจ็กต์ของคุณ

วิธีที่เร็วที่สุดในการออกแบบ ทดลอง และทำซ้ำเสียงที่กำหนดเองคือการใช้สตูดิโอ**การออกแบบเสียง**แบบอินเทอร์แอกทีฟใน [Google AI Studio](https://aistudio.google.com/generate-speech?hl=th) คุณสามารถ สร้างลักษณะตัวตนที่กำหนดเองจากพรอมต์ข้อความ ทดสอบด้วยสคริปต์ตัวอย่าง และ คัดลอก`voice_...`รหัสที่ได้ลงในโค้ดของแอปพลิเคชันได้โดยตรง

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/generate-speech?hl=th)

ทั้ง [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
(`gemini-3.8-flash-tts`) และ
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
(`gemini-3.8-flash-lite-tts`) รองรับการออกแบบเสียง

## สร้างเสียงที่ออกแบบ

ใช้ Google GenAI SDK (`google-genai` 2.25.0 ขึ้นไป / `@google/genai` 2.24.0 ขึ้นไป) หรือ REST API
เพื่อสร้างเสียงที่กำหนดเองจากคำอธิบายข้อความ สำหรับเสียง `"prompted"` ทั้ง `voices.create` (`CreateVoice`) และ `voices.get` (`GetVoice`) จะแสดงฟิลด์ `sample_audio` ที่เป็นเอาต์พุตเท่านั้น (`mime_type: "audio/wav"`, `data` ที่เข้ารหัส Base64) เพื่อให้คุณทดลองฟังเสียงที่สร้างขึ้นได้ทันที

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## วิธีการออกแบบเสียง

1. **สร้างเสียงที่พร้อมใช้งาน:** โทรหา `voices.create` (`POST /v1beta/voices`)
   ด้วย `type="prompted"` และ `store=True`
2. **รับตัวอย่าง `voice_id` และ `sample_audio` แบบถาวร:** API จะสร้างเอกลักษณ์เสียง จัดเก็บไว้ในโปรเจ็กต์ และแสดงรหัสถาวร (เช่น `voice_abc123...`) พร้อมกับ `sample_audio`
   (`mime_type: "audio/wav"`, `data` ที่เข้ารหัส Base64) ซึ่งมีตัวอย่างเสียงที่สร้างขึ้นสำหรับเสียงนั้น
3. **สังเคราะห์เสียง:** ส่ง `voice_id` ในตำแหน่งใดก็ได้ที่ยอมรับชื่อเสียง
   ในคำขอการสังเคราะห์

## สังเคราะห์เสียงด้วยเสียงที่คุณออกแบบ

เมื่อสร้างเสียงแล้ว ให้ส่ง `id` (`voice_...`) ของเสียงนั้นไปยัง Interactions
API เพื่อสร้างคำพูดโดยทำดังนี้

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## จัดการเสียงของคุณ

คุณสามารถแสดง กรอง ตรวจสอบ และลบเสียงที่จัดเก็บไว้ได้ทุกเมื่อโดยใช้
Voices API (ดู
[คลังเสียงและการกรองเพิ่มเติม](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#voice-library)
สำหรับพารามิเตอร์ตัวกรองทั้งหมด)

- **ขีดจำกัดพื้นที่เก็บข้อมูลและ TTL:** เสียงแบบมีสถานะ (`store=True` แชร์ใน
  เสียงที่พรอมต์และเสียงที่จำลอง) มีขีดจำกัดอยู่ที่ **200 เสียงต่อโปรเจ็กต์**
  และมี **TTL 1 ปี** (Time to Live)
- **ความพร้อมใช้งานของ `sample_audio`:** `voices.create()` (`CreateVoice`) และ
  `voices.get()` (`GetVoice`) จะแสดง `sample_audio` (`mime_type:
  "audio/wav"`, `data` ที่เข้ารหัส Base64) สำหรับเสียง `"prompted"` `voices.list()` (`ListVoices`) จะไม่รวม `sample_audio` เพื่อให้ข้อมูลมีขนาดเล็ก
  (และจะไม่มีการตั้งค่า `sample_audio` สำหรับเสียง `"replicated"` และ `"prebuilt"`)

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## แนวทางปฏิบัติแนะนำในการเขียนพรอมต์สำหรับการออกแบบเสียง

- **ใส่ลักษณะเสียงร้องถาวรในการออกแบบเสียง ไม่ใช่`style`:** กำหนดลักษณะที่ไม่เปลี่ยนแปลง เช่น อายุ เพศ โทนเสียง ลักษณะเสียงร้อง และสำเนียงท้องถิ่น เมื่อสร้างเสียงใน `voices.create`
- **เก็บ `speech_metadata.style` ไว้สำหรับอารมณ์ตามสถานการณ์:** เมื่อสร้าง
  เสียงที่กำหนดเองแล้ว ให้ใช้พรอมต์สั้นๆ `style` (เช่น
  `"whispered urgently"` หรือ `"cheerful and energetic"`) เพื่อควบคุมการแสดงตามคำสั่ง
  แบบเลี้ยวต่อเลี้ยวโดยไม่เปลี่ยนตัวตนหลักของผู้พูด
- **ให้ข้อมูลที่เฉพาะเจาะจงและกระชับ:** คำอธิบายที่ชัดเจน 1-2 ประโยค (เช่น *"ผู้ประกาศข่าวกีฬาที่กระตือรือร้นและเฉียบคมในวัย 30 ปีที่มีสำเนียง
  เล็กน้อยแบบมิดเวสต์"*) จะให้ผลลัพธ์ที่สะอาดและสม่ำเสมอกว่าย่อหน้าที่ขัดแย้งกันหรือยาวเกินไป

## ขั้นตอนถัดไป

- ดูวิธีจำลองเสียงของลำโพงที่มีอยู่แล้วใน[การจำลองเสียง](https://ai.google.dev/gemini-api/docs/voice-replication?hl=th)
- ดูข้อมูลเกี่ยวกับการจัดรูปแบบระดับคำ การใช้แท็กในบรรทัด และบทสนทนาแบบหลายผู้พูดได้ใน[คู่มือ Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
