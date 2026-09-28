---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=th
fetched_at: 2026-09-28T06:19:38.905279+00:00
title: "\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e14\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e04\u0e33 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การถอดเสียงเป็นคำ

Gemini API จะแปลงเสียงพูดในไฟล์เสียงเป็นข้อความโดยใช้โมเดล Gemini 3.5 Transcribe (`gemini-3.5-transcribe`) โดยอิงตามความสามารถในการทำความเข้าใจเสียงของ Gemini ซึ่งจะให้การถอดเสียงที่แม่นยำพร้อมการระบุภาษาอัตโนมัติ การระบุผู้พูด การประทับเวลาที่ระดับคำ และคำแนะนำคำศัพท์ที่กำหนดเอง นอกจากนี้ ยังมีโหมด[การถอดเสียงอัจฉริยะ](#transcription-modes)ที่มาพร้อมการนำคำพูดที่ไม่ต่อเนื่องออกและการจัดรูปแบบอัจฉริยะ

หากต้องการถอดเสียงไฟล์เสียง ให้อัปโหลดเสียงและส่งไปยัง `gemini-3.5-transcribe`

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## ภาพรวม

Gemini 3.5 Transcribe ได้รับการเพิ่มประสิทธิภาพสำหรับงานแปลงเสียงพูดเป็นข้อความ โดยจะจัดการกับสำเนียงที่หลากหลาย เสียงรบกวนรอบข้าง และการสนทนาหลายภาษา

ความสามารถหลักๆ มีดังนี้

- **การรู้จำคำพูดอัตโนมัติ (ASR):** ตรวจหาภาษาโดยอัตโนมัติใน[กว่า 85 ภาษา](#supported-languages) จัดการการสลับภาษาภายในประโยคและระหว่างประโยคโดยไม่ต้องกำหนดค่าด้วยตนเอง
- **คำศัพท์ที่กำหนดเอง:** ช่วยให้ระบบจดจำคำศัพท์ ตัวย่อ และชื่อเฉพาะในโดเมนได้โดยส่งวลีได้สูงสุด 1,000 รายการ
- **การระบุผู้พูด:** แยกแยะผู้พูดหลายคนและเชื่อมโยงส่วนที่พูดกับป้ายกำกับที่แตกต่างกัน
- **การประทับเวลาที่ระดับคำ:** สร้างออฟเซ็ตเวลาเริ่มต้นและเวลาสิ้นสุดที่แน่นอนสำหรับแต่ละคำที่ระบบจดจำ
- **การถอดเสียงอัจฉริยะ:** ล้างคำพูดที่ไม่มีความหมาย การพูดซ้ำ และใช้การจัดรูปแบบที่มีโครงสร้าง
- **การจัดรูปแบบและการทำให้เป็นมาตรฐาน:** ใช้การใช้อักษรตัวพิมพ์ใหญ่ เครื่องหมายวรรคตอน และการทำให้ข้อความเป็นมาตรฐานแบบผกผัน เช่น การแปลง "ยี่สิบหกล้านดอลลาร์" เป็น "$26M"

หากต้องการใช้การให้เหตุผลหรือตอบคำถามเกี่ยวกับเนื้อหาเสียงทั่วไป ให้ใช้[การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=th) สำหรับการสังเคราะห์เสียงของการอ่านออกเสียงข้อความ ให้ใช้ [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th)

## การตรวจหาภาษาและคำแนะนำ

โดยค่าเริ่มต้น โมเดลจะตรวจจับภาษาที่พูดโดยอัตโนมัติ โดยจะสลับภาษาแบบไดนามิกเมื่อผู้พูดเปลี่ยนภาษา

หากต้องการใช้การตรวจหาอัตโนมัติ ให้ละเว้น `language_codes` หรือระบุรายการว่าง

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

หากทราบภาษาล่วงหน้า ให้ระบุรหัสภาษา BCP-47 ใน `language_codes` เพื่อปรับปรุงความแม่นยำของการถอดเสียง (ดู[ภาษาที่รองรับ](#supported-languages))

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## คำศัพท์ที่กำหนดเอง

คุณสามารถนำโมเดลการพูดไปยังคำที่ไม่ค่อยมีคนใช้ คำศัพท์เฉพาะทาง ชื่อแบรนด์ หรือคำนามเฉพาะได้ ระบุคำศัพท์ได้สูงสุด 1,000 คำใน`custom_vocabulary`อาร์เรย์ (โดยปกติแล้วจะให้ผลลัพธ์ที่ดีที่สุดเมื่อใช้คำศัพท์ไม่เกิน 100 คำ)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## การแยกแยะเสียงผู้พูด

การระบุผู้พูดจะระบุเสียงที่แตกต่างกันในการบันทึกและติดแท็กแต่ละส่วนด้วยตัวระบุผู้พูด เช่น `spk_1` หรือ `spk_2` รองรับลำโพงสูงสุด 8 ตัว (การระบุแหล่งที่มาสำหรับลำโพงตั้งแต่ 3 ตัวขึ้นไปเป็นเวอร์ชันทดลอง)

เปิดใช้การแยกแยะเสียงผู้พูดโดยตั้งค่า `diarization` เป็น `True` ดังนี้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## การประทับเวลาระดับคำ

การประทับเวลาระดับคำจะระบุออฟเซ็ตเริ่มต้นและสิ้นสุดที่แน่นอนสำหรับทุกคำที่ระบบจดจำได้ในสตรีมเสียง

เปิดใช้การประทับเวลาโดยตั้งค่า `word_timestamp` เป็น `True` ดังนี้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

คุณสามารถรวม `diarization` และ `word_timestamp` ไว้ในคำขอเดียวเพื่อรับทั้งป้ายกำกับผู้พูดและการประทับเวลาของคำได้โดยทำดังนี้

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true
    }
  }
}
```

## โหมดการถอดเสียงเป็นคำ

Gemini 3.5 Transcribe รองรับโหมดการถอดเสียงเป็นคำ 2 โหมดผ่านพารามิเตอร์ `mode` ดังนี้

- **`VERBATIM` (ค่าเริ่มต้น)**: แสดงข้อความถอดเสียงแบบคำต่อคำที่ตรงกันทุกประการของทุกสิ่งที่พูด โดยจะเก็บคำฟุ่มเฟือยดิบ ("เอ่อ", "อืม", "แบบว่า", "ก็") การพูดซ้ำ การหยุดชั่วคราว และการพูดติดขัด ต้องระบุเมื่อใช้การประทับเวลาหรือการระบุผู้พูด
- **`SMART` (การถอดเสียงอัจฉริยะ)**: เพิ่มประสิทธิภาพข้อความถอดเสียงสำหรับการอ่านโดยใช้การประมวลผลหลังการประมวลผลอัจฉริยะ
  - **การนำคำพูดติดขัดออก**: นำคำพูดติดขัด คำพูดซ้ำ และการเริ่มต้นที่ไม่ถูกต้องออก
  - **การแก้ไขตัวเองในบรรทัด**: แก้ไขคำที่พูดผิดโดยตรง (เช่น *"มาเจอกันวันอังคาร ไม่สิ วันพุธตอน 14:00 น."* จะกลายเป็น *"มาเจอกันวันพุธตอน 14:00 น."*)
  - **การจัดรูปแบบที่มีโครงสร้างอัตโนมัติ**: จัดโครงสร้างความคิดที่พูดเป็นย่อหน้า รายการที่มีหมายเลข หัวข้อย่อย วันที่ สกุลเงิน และตัวเลขที่จัดรูปแบบโดยอัตโนมัติ
  - **การแก้ไขไวยากรณ์**: ใช้เครื่องหมายวรรคตอน การจัดรูปแบบประโยค และลำดับการนำเสนอที่เป็นธรรมชาติ

| เสียงพูด | `VERBATIM` เอาต์พุต | `SMART` เอาต์พุต (การถอดเสียงอัจฉริยะ) |
| --- | --- | --- |
| "เอ่อ สำหรับการประชุม ฉันคิดว่าเราควรเชิญ เอ่อ ขวัญใจและ เอ่อ ไม่ใช่ บัญชาและแคโรล" | "เอ่อ สำหรับการประชุม ฉันคิดว่าเราควรเชิญอลิซ เอ่อ ไม่ใช่ บ็อบกับแครอล" | "สำหรับการประชุม ฉันคิดว่าเราควรเชิญบ็อบและแครอล" |
| "งบประมาณสำหรับการตรวจสอบรายการแรก ไทม์ไลน์การสรุปรายการที่สอง ส่งสรุป" | "งบประมาณการตรวจสอบรายการแรก ไทม์ไลน์การสรุปรายการที่สอง ส่งสรุปรายการที่สาม" | "1. ตรวจสอบงบประมาณ 2. สรุปไทม์ไลน์ 3. ส่งสรุป" |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## การแยกวิเคราะห์เอาต์พุตการถอดเสียงเป็นคำ

ระบบจะแสดงข้อความถอดเสียงทั้งหมดใน `response.text`

เมื่อเปิดใช้ `word_timestamp` หรือ `diarization` แล้ว API จะแสดงคำอธิบายประกอบระดับคำโดยละเอียดและป้ายกำกับผู้พูดที่แนบมากับส่วนที่ต้องการด้วย

วิธีแยกและวนซ้ำการประทับเวลาของคำและการเปลี่ยนลำโพงมีดังนี้

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## ภาษาที่รองรับ

Gemini 3.5 Transcribe รองรับภาษาและรหัสภาษา BCP-47 ต่อไปนี้

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

## รูปแบบเสียงที่รองรับ

Gemini 3.5 Transcribe รองรับประเภท MIME ของรูปแบบเสียงต่อไปนี้

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

ดูรายการประเภท MIME และสคีมาพารามิเตอร์ที่รองรับทั้งหมดได้ใน[เอกสารอ้างอิง Interactions API](https://ai.google.dev/api/interactions-api?hl=th#Resource:Content)

## ข้อมูลอ้างอิงพารามิเตอร์

กำหนดค่าการถอดเสียงเป็นคำโดยการตั้งค่าฟิลด์ภายในออบเจ็กต์ `audio_transcription_config` ใน `GenerateContentConfig` ดังนี้

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `language_codes` | อาร์เรย์ของสตริง | รหัสภาษา BCP-47 (เช่น `["en-US"]`) หากเว้นว่างหรือไม่มีค่า (`[]`) โมเดลจะตรวจหาภาษาโดยอัตโนมัติและจัดการการสลับภาษา |
| `custom_vocabulary` | อาร์เรย์ของสตริง | คำที่กำหนดเอง ตัวย่อ หรือชื่อเฉพาะสูงสุด 1,000 รายการเพื่อปรับการจดจำคำพูด ใช้ร่วมกับการระบุผู้พูดและแสตมป์เวลาระดับคำไม่ได้ |
| `word_timestamp` | บูลีน | ตั้งค่าเป็น `True` เพื่อรวมออฟเซ็ตเริ่มต้นและสิ้นสุดของคำ หากละเว้นหรือ `False` ระบบจะไม่แสดงการประทับเวลาของคำ ใช้ร่วมกับคำศัพท์ที่กำหนดเองไม่ได้ |
| `diarization` | บูลีน | ตั้งค่าเป็น `True` เพื่อระบุและติดป้ายกำกับผู้พูดแต่ละคน ใช้ร่วมกับคำศัพท์ที่กำหนดเองไม่ได้ |
| `mode` | สตริง | โหมดการถอดเสียงเป็นคำ ค่าที่รองรับ: `"VERBATIM"` (ค่าเริ่มต้น) และ `"SMART"` ใช้ร่วมกับการประทับเวลาและการแยกแยะเสียงพูดไม่ได้ |

## แนวทางปฏิบัติแนะนำ

- **ให้เสียงที่ชัดเจน:** ตรวจสอบว่าไฟล์บันทึกเสียงมีการแยกเสียงพูดที่ชัดเจนและหลีกเลี่ยงการตัดเสียงที่รุนแรง
- **ระบุคำแนะนำเกี่ยวกับภาษาเมื่อทราบ:** หากทราบภาษาของเสียงล่วงหน้า ให้ระบุ `language_codes` เพื่อเพิ่มความแม่นยำให้สูงสุด
- **คำศัพท์ที่กำหนดเองเป้าหมาย:** ใส่เฉพาะคำในโดเมน ชื่อแบรนด์ หรือคำนามเฉพาะที่แตกต่างกันใน `custom_vocabulary` แทนที่จะใช้คำทั่วไปในชีวิตประจำวัน
- **ใช้ Files API สำหรับการบันทึกขนาดใหญ่:** สำหรับไฟล์ที่ยาวกว่า 2-3 วินาที ให้อัปโหลดไฟล์โดยใช้ `client.files.upload` และส่งไฟล์ที่ส่งคืนไปยังเนื้อหาของโมเดล

## ข้อจำกัด

- **ระยะเวลาเสียง:** คำขอแบบเอกภาคมาตรฐานรองรับไฟล์เสียงได้นานสูงสุด 1 ชั่วโมง การประมวลผลเสียงจะจำกัดไว้ที่ 30 นาทีเมื่อเปิดใช้ฟีเจอร์ต่างๆ เช่น การระบุผู้พูดหรือการประทับเวลาที่ระดับคำ
- **การประทับเวลาที่ระดับคำ:** การเปิดใช้การประทับเวลาที่ระดับคำอาจลดความแม่นยำในการถอดเสียงเป็นคำโดยรวม
- **การแยกแยะเสียงผู้พูด:** การแยกแยะเสียงผู้พูดรองรับผู้พูดได้สูงสุด 8 คน การระบุแหล่งที่มาของลำโพงสำหรับลำโพง 3 ตัวขึ้นไปอยู่ในขั้นทดลอง
- **คำศัพท์ที่กำหนดเอง:** คุณระบุคำได้สูงสุด 1,000 คำใน `custom_vocabulary` แต่โดยปกติแล้วการระบุคำสูงสุด 100 คำจะให้ผลลัพธ์ที่ดีที่สุด คุณใช้ `custom_vocabulary` ร่วมกับการระบุผู้พูดหรือการประทับเวลาที่ระดับคำไม่ได้ โดย API จะปฏิเสธคำขอที่ระบุ `custom_vocabulary` พร้อมกับฟีเจอร์ใดฟีเจอร์หนึ่ง
- **ความเข้ากันได้ของโหมด:** การถอดเสียงอัจฉริยะ (`mode: "SMART"`) ใช้ร่วมกับ `word_timestamp` หรือ `diarization` ไม่ได้

## ขั้นตอนถัดไป

- สตรีมเสียงแบบเรียลไทม์ด้วย[คู่มือการถอดเสียงเป็นคำแบบสด](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=th)โดยใช้ Live API
- สำรวจ[การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=th)เพื่อวิเคราะห์ สรุป หรือค้นหาเนื้อหาเสียง
- ดูวิธีสังเคราะห์เสียงจากข้อความโดยใช้[การอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th)
- ดูราคาของโมเดลและขีดจำกัดโทเค็นได้ใน[หน้าการกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.5-transcribe)
- โปรดดูรายละเอียดเกี่ยวกับการอัปโหลดและจัดการไฟล์สื่อในคู่มือ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-08 UTC"],[],[]]
