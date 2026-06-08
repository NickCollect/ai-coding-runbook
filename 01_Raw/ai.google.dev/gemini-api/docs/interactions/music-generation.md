---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=th
fetched_at: 2026-06-08T05:36:52.796676+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สร้างเพลงด้วย Lyria 3

Lyria 3 เป็นกลุ่มโมเดลการสร้างเพลงของ Google ซึ่งพร้อมใช้งานผ่าน Gemini API Lyria 3 ช่วยให้คุณสร้างเสียงสเตอริโอคุณภาพสูง 44.1 kHz จากพรอมต์ข้อความหรือจากรูปภาพได้ โมเดลเหล่านี้ให้ความสอดคล้องเชิงโครงสร้าง ซึ่งรวมถึงเสียงร้อง เนื้อเพลงที่กำหนดเวลา และดนตรีบรรเลงแบบเต็ม

กลุ่ม Lyria 3 มี 2 โมเดล ได้แก่

| รุ่น | รหัสโมเดล | เหมาะสำหรับ | ระยะเวลา | เอาต์พุต |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | คลิปสั้น ลูป ตัวอย่าง | 30 วินาที | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | เพลงแบบเต็มความยาวที่มีท่อน Verse, Chorus และ Bridge | 2-3 นาที (ควบคุมได้โดยใช้พรอมต์) | MP3 |

ทั้ง 2 โมเดลสามารถใช้ได้โดยใช้
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th) ใหม่ ซึ่งรองรับอินพุตหลายรูปแบบ (ข้อความและรูปภาพ) และสร้างเสียง **สเตอริโอความสมจริงสูง 44.1 kHz**

## สร้างคลิปเพลง

โมเดล Lyria 3 Clip จะสร้างคลิปความยาว **30 วินาที** เสมอ หากต้องการสร้างคลิป ให้เรียกใช้เมธอด `interactions.create` ด้วยพรอมต์ข้อความ การตอบกลับจะมีเนื้อเพลงและโครงสร้างเพลงที่สร้างขึ้นเสมอ รวมถึงเสียงในสคีมา `steps`

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

คุณสามารถดึงข้อมูลเพลงที่สร้างขึ้นได้โดยใช้พร็อพเพอร์ตี้ `interaction.output_audio` ซึ่งจะแสดงผลบล็อกเสียงที่สร้างขึ้นล่าสุด นอกจากนี้ คุณยังดึงเนื้อเพลงและโครงสร้างของเพลงได้โดยใช้พร็อพเพอร์ตี้ `interaction.output_text` ดูรายละเอียดเกี่ยวกับพร็อพเพอร์ตี้ที่สะดวกได้ที่
[ภาพรวมของ Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=th#convenience-properties)

## สร้างเพลงแบบเต็มความยาว

ใช้โมเดล `lyria-3-pro-preview` เพื่อสร้างเพลงแบบเต็มความยาวที่ใช้เวลา 2-3 นาที โมเดล Pro เข้าใจโครงสร้างดนตรีและสามารถสร้างเพลงที่มีท่อน Verse, Chorus และ Bridge ที่แตกต่างกันได้ คุณสามารถกำหนด
ระยะเวลาได้โดยระบุในพรอมต์ (เช่น "สร้างเพลงความยาว 2 นาที") หรือ
ใช้ [การประทับเวลา](#timing) เพื่อกำหนดโครงสร้าง

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## เลือกรูปแบบเอาต์พุต

โดยค่าเริ่มต้น โมเดล Lyria 3 จะสร้างเสียงในรูปแบบ **MP3** สำหรับ Lyria 3 Pro คุณยังขอเอาต์พุตในรูปแบบ **WAV** ได้ด้วยโดยการตั้งค่า `response_format`

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## แยกวิเคราะห์การตอบกลับ

การตอบกลับจาก Lyria 3 มีบล็อกเนื้อหาหลายรายการภายในสคีมา `steps`
Interactions จะแสดงผลลำดับขั้นตอน โดยขั้นตอน `model_output` จะมีเนื้อหาที่สร้างขึ้น
บล็อกเนื้อหาข้อความจะมีเนื้อเพลงที่สร้างขึ้นหรือคำอธิบาย JSON ของโครงสร้างเพลง
บล็อกเนื้อหาที่มีประเภท `audio` จะมีข้อมูลเสียงที่เข้ารหัสแบบ Base64

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### เนื้อเพลงและเพลงที่สลับกัน

เนื่องจากเอาต์พุตจาก Lyria 3 มีความซับซ้อน โดยมีขั้นตอนและบล็อกแยกกันสำหรับเนื้อเพลง (ข้อความ) และเพลงเอง (เสียง) พร็อพเพอร์ตี้ที่สะดวกจึงเป็นทางลัดที่รวดเร็วและแนะนำ

อย่างไรก็ตาม หากต้องการควบคุมไทม์ไลน์แบบดิบของขั้นตอนที่เซิร์ฟเวอร์แสดงผลแบบเป็นโปรแกรมอย่างเต็มรูปแบบ (เช่น การบันทึกบล็อกเนื้อหาแต่ละรายการเมื่อได้รับ) คุณสามารถวนซ้ำ `steps` ด้วยตนเองแทนได้ดังนี้

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## สร้างเพลงจากรูปภาพ

Lyria 3 รองรับอินพุตหลายรูปแบบ โดยคุณสามารถใส่รูปภาพได้สูงสุด **10 รูป** พร้อมกับพรอมต์ข้อความในรายการ `input` และโมเดลจะแต่งเพลงที่ได้รับแรงบันดาลใจจากเนื้อหาภาพ

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## ใส่เนื้อเพลงที่กำหนดเอง

คุณสามารถเขียนเนื้อเพลงของคุณเองและใส่ไว้ในพรอมต์ได้ ใช้แท็กส่วนต่างๆ เช่น `[Verse]`, `[Chorus]` และ `[Bridge]` เพื่อช่วยให้โมเดลเข้าใจโครงสร้างเพลง

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## ควบคุมเวลาและโครงสร้าง

คุณสามารถระบุสิ่งที่เกิดขึ้นในบางช่วงเวลาของเพลงได้อย่างแม่นยำโดยใช้การประทับเวลา ซึ่งมีประโยชน์สำหรับการควบคุมเวลาที่เครื่องดนตรีเริ่มเล่น เวลาที่เนื้อเพลงเริ่มร้อง และความคืบหน้าของเพลง

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## สร้างแทร็กดนตรีบรรเลง

สำหรับเพลงประกอบ เกม หรือ Use Case ที่ไม่จำเป็นต้องมีเสียงร้อง คุณสามารถแจ้งให้โมเดลสร้างแทร็กดนตรีบรรเลงเท่านั้นได้

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## สร้างเพลงในภาษาต่างๆ

Lyria 3 จะสร้างเนื้อเพลงในภาษาของพรอมต์ หากต้องการสร้างเพลงที่มีเนื้อเพลงเป็นภาษาฝรั่งเศส ให้เขียนพรอมต์เป็นภาษาฝรั่งเศส โมเดลจะปรับสไตล์การร้องและการออกเสียงให้เข้ากับภาษา

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## ความสามารถของโมเดล

Lyria 3 จะวิเคราะห์กระบวนการพรอมต์ที่โมเดลใช้เหตุผลผ่านโครงสร้างดนตรี (Intro, Verse, Chorus, Bridge ฯลฯ) ตามพรอมต์ของคุณ
กระบวนการนี้จะเกิดขึ้นก่อนที่จะสร้างเสียง และช่วยให้มั่นใจได้ถึงความสอดคล้องเชิงโครงสร้างและความเป็นดนตรี

## คำแนะนำในการเขียนพรอมต์

พรอมต์ที่เฉพาะเจาะจงมากขึ้นจะให้ผลลัพธ์ที่ดีขึ้น สิ่งที่คุณใส่ได้เพื่อแนะนำการสร้างมีดังนี้

- **ประเภท**: ระบุประเภทหรือการผสมผสานของประเภท (เช่น "Lo-fi Hip Hop",
  "Jazz Fusion", "Cinematic Orchestral")
- **เครื่องดนตรี**: ระบุชื่อเครื่องดนตรี (เช่น "เปียโน Fender Rhodes",
  "กีตาร์สไลด์", "เครื่องดรัม TR-808")
- **BPM**: กำหนดจังหวะ (เช่น "120 BPM", "จังหวะช้าประมาณ 70 BPM")
- **คีย์/สเกล**: ระบุคีย์ดนตรี (เช่น "ในคีย์ G เมเจอร์", "D ไมเนอร์")
- **อารมณ์และบรรยากาศ**: ใช้คำคุณศัพท์เชิงพรรณนา (เช่น "คิดถึงอดีต",
  "ดุดัน", "เหนือจริง", "ชวนฝัน")
- **โครงสร้าง**: ใช้แท็กต่างๆ เช่น `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` หรือการประทับเวลาเพื่อควบคุมความคืบหน้าของเพลง
- **ระยะเวลา**: โมเดล Clip จะสร้างคลิปความยาว 30 วินาทีเสมอ สำหรับโมเดล Pro ให้ระบุความยาวที่ต้องการในพรอมต์ (เช่น "สร้างเพลงความยาว 2 นาที") หรือใช้การประทับเวลาเพื่อควบคุมระยะเวลา

### ตัวอย่างพรอมต์

ตัวอย่างพรอมต์ที่มีประสิทธิภาพมีดังนี้

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## แนวทางปฏิบัติแนะนำ

- **วนซ้ำด้วย Clip ก่อน** ใช้โมเดล `lyria-3-clip-preview` ที่เร็วกว่าเพื่อทดลองใช้พรอมต์ก่อนที่จะสร้างเพลงแบบเต็มความยาวด้วย `lyria-3-pro-preview`
- **ใช้คำที่เฉพาะเจาะจง** พรอมต์ที่คลุมเครือจะให้ผลลัพธ์ทั่วไป ระบุเครื่องดนตรี BPM คีย์ อารมณ์ และโครงสร้างเพื่อให้ได้เอาต์พุตที่ดีที่สุด
- **ใช้ภาษาที่ต้องการ** เขียนพรอมต์ในภาษาที่ต้องการให้เนื้อเพลงเป็น
- **ใช้แท็กส่วนต่างๆ** แท็ก `[Verse]`, `[Chorus]`, `[Bridge]` จะให้โครงสร้างที่ชัดเจนแก่โมเดลเพื่อทำตาม
- **แยกเนื้อเพลงออกจากคำแนะนำ** เมื่อใส่เนื้อเพลงที่กำหนดเอง ให้แยกเนื้อเพลงออกจากคำแนะนำเกี่ยวกับทิศทางดนตรีอย่างชัดเจน

## ข้อจำกัด

- **ความปลอดภัย**: ระบบจะตรวจสอบพรอมต์ทั้งหมดด้วยตัวกรองความปลอดภัย ระบบจะบล็อกพรอมต์ที่ทริกเกอร์ตัวกรอง ซึ่งรวมถึงพรอมต์ที่ขอเสียงร้องของศิลปินที่เฉพาะเจาะจงหรือการสร้างเนื้อเพลงที่มีลิขสิทธิ์
- **การใส่ลายน้ำ**: เสียงที่สร้างขึ้นทั้งหมดจะมี
  [ลายน้ำเสียง SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=th) เพื่อ
  การระบุ ลายน้ำนี้หูของมนุษย์ไม่สามารถรับรู้ได้และไม่ส่งผลต่อประสบการณ์การฟัง
- **การแก้ไขแบบผ่านการสนทนาไปมา**: การสร้างเพลงเป็นกระบวนการแบบผ่านการสนทนาไปมาครั้งเดียว
  Lyria 3 เวอร์ชันปัจจุบันไม่รองรับการแก้ไขซ้ำๆ หรือการปรับแต่งคลิปที่สร้างขึ้นผ่านพรอมต์หลายรายการ
- **ความยาว**: โมเดล Clip จะสร้างคลิปความยาว 30 วินาทีเสมอ โมเดล Pro จะสร้างเพลงที่ใช้เวลา 2-3 นาที โดยคุณสามารถกำหนดระยะเวลาที่แน่นอนได้ผ่านพรอมต์
- **ความแน่นอน**: ผลลัพธ์อาจแตกต่างกันไปในแต่ละการเรียกใช้ แม้จะใช้พรอมต์เดียวกันก็ตาม

## ขั้นตอนถัดไป

- ตรวจสอบ[ราคา](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=th)ของโมเดล Lyria 3
- [ลองสร้างเพลงแบบสตรีมมิงแบบเรียลไทม์
  ด้วย Lyria RealTime](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=th)
- สร้างการสนทนาของผู้พูดหลายคนด้วยโมเดล
  [TTS](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=th)
- ดูวิธีสร้าง[รูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=th)หรือ[วิดีโอ](https://ai.google.dev/gemini-api/docs/interactions/video?hl=th)
- ดูวิธีที่ Gemini สามารถ[เข้าใจไฟล์เสียง](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=th)
- สนทนาแบบเรียลไทม์กับ Gemini โดยใช้
  [Live API](https://ai.google.dev/gemini-api/docs/interactions/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
