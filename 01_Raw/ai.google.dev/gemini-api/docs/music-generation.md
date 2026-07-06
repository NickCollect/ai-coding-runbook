---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=id
fetched_at: 2026-07-06T05:15:38.833082+00:00
title: "Membuat musik dengan Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Membuat musik dengan Lyria 3

Lyria 3 adalah rangkaian model pembuatan musik Google, yang tersedia melalui Gemini API. Dengan Lyria 3, Anda dapat membuat audio stereo berkualitas tinggi 44, 1 kHz dari perintah teks atau dari gambar. Model ini memberikan koherensi struktural, termasuk vokal, lirik yang diberi stempel waktu, dan aransemen instrumental lengkap.

Rangkaian Lyria 3 mencakup dua model:

| Model | ID Model | Paling cocok untuk | Durasi | Output |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Klip, loop, pratinjau singkat | 30 detik | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Lagu berdurasi penuh dengan bait, chorus, bridge | Beberapa menit (dapat dikontrol menggunakan perintah) | MP3 |

Kedua model dapat digunakan menggunakan
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) baru, yang mendukung input multimodal (teks dan gambar), dan menghasilkan audio **stereo fidelitas tinggi 44,1 kHz**
.

## Membuat klip musik

Model Lyria 3 Clip selalu membuat klip **30 detik**. Untuk membuat klip, panggil metode `interactions.create` dengan perintah teks. Respons selalu menyertakan lirik dan struktur lagu yang dibuat bersama dengan audio dalam skema `steps`.

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
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Anda dapat mengambil data musik yang dibuat menggunakan properti `interaction.output_audio`, yang menampilkan blok audio terakhir yang dibuat. Anda juga dapat mengambil lirik dan struktur lagu menggunakan properti `interaction.output_text`. Untuk mengetahui detail properti praktis, lihat
[Ringkasan interaksi](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id#convenience-properties).

## Membuat lagu berdurasi penuh

Gunakan model `lyria-3-pro-preview` untuk membuat lagu berdurasi penuh yang berlangsung selama beberapa menit. Model Pro memahami struktur musik dan dapat membuat komposisi dengan bait, chorus, dan bridge yang berbeda. Anda dapat memengaruhi
durasi dengan menentukannya dalam perintah (misalnya, "buat lagu 2 menit") atau dengan
menggunakan [stempel waktu](#timing) untuk menentukan struktur.

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
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Memilih format output

Secara default, model Lyria 3 membuat audio dalam format **MP3**. Untuk Lyria 3 Pro, Anda juga dapat meminta output dalam format **WAV** dengan menetapkan `response_format`.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Mengurai respons

Respons dari Lyria 3 berisi beberapa blok konten dalam skema `steps`.
Interaksi menampilkan urutan langkah, dengan langkah `model_output` berisi konten yang dibuat.
Blok konten teks berisi lirik yang dibuat atau deskripsi JSON dari struktur lagu.
Blok konten dengan jenis `audio` berisi data audio berenkode base64.

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

#### Lirik dan musik yang disisipkan

Karena output dari Lyria 3 kompleks—berisi langkah dan blok terpisah untuk lirik yang dibuat (teks) dan lagu itu sendiri (audio)—properti praktis menawarkan pintasan yang cepat dan direkomendasikan.

Namun, jika Anda menginginkan kontrol terprogram penuh atas linimasa langkah mentah yang ditampilkan oleh server (seperti mencatat blok konten individual saat diterima), Anda dapat melakukan iterasi `steps` secara manual:

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

## Membuat musik dari gambar

Lyria 3 mendukung input multimodal — Anda dapat memberikan hingga **10 gambar** bersama dengan perintah teks dalam daftar `input` dan model akan membuat musik yang terinspirasi dari konten visual.

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
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Memberikan lirik kustom

Anda dapat menulis lirik sendiri dan menyertakannya dalam perintah. Gunakan tag bagian seperti `[Verse]`, `[Chorus]`, dan `[Bridge]` untuk membantu model memahami struktur lagu:

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Mengontrol waktu dan struktur

Anda dapat menentukan dengan tepat apa yang terjadi pada momen tertentu dalam lagu menggunakan stempel waktu. Hal ini berguna untuk mengontrol kapan instrumen masuk, kapan lirik disampaikan, dan bagaimana lagu berjalan:

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Membuat trek instrumental

Untuk musik latar, soundtrack game, atau kasus penggunaan apa pun yang tidak memerlukan vokal, Anda dapat meminta model untuk membuat trek khusus instrumental:

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Membuat musik dalam berbagai bahasa

Lyria 3 membuat lirik dalam bahasa perintah Anda. Untuk membuat lagu dengan lirik bahasa Prancis, tulis perintah Anda dalam bahasa Prancis. Model ini menyesuaikan gaya vokal dan pengucapannya agar sesuai dengan bahasa.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Kecerdasan model

Lyria 3 menganalisis proses perintah Anda saat model mempertimbangkan struktur musik (intro, bait, chorus, bridge, dll.) berdasarkan perintah Anda.
Hal ini terjadi sebelum audio dibuat dan memastikan koherensi struktural dan musikalitas.

## Panduan penulisan perintah

Makin spesifik perintah Anda, makin bagus hasilnya. Berikut hal-hal yang dapat Anda sertakan untuk memandu pembuatan:

- **Genre**: Tentukan genre atau campuran genre (misalnya, "lo-fi hip hop",
  "jazz fusion", "cinematic orchestral").
- **Instrumen**: Sebutkan instrumen tertentu (misalnya, "piano Fender Rhodes",
  "gitar slide", "mesin drum TR-808").
- **BPM**: Tetapkan tempo (misalnya, "120 BPM", "tempo lambat sekitar 70 BPM").
- **Kunci/Skala**: Tentukan kunci musik (misalnya, "dalam G mayor", "D minor").
- **Suasana hati dan atmosfer**: Gunakan kata sifat deskriptif (misalnya, "nostalgia",
  "agresif", "halus", "melamun").
- **Struktur**: Gunakan tag seperti `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` atau stempel waktu untuk mengontrol perkembangan lagu.
- **Durasi**: Model Klip selalu menghasilkan klip 30 detik. Untuk model Pro, tentukan panjang yang diinginkan dalam perintah Anda (misalnya, "buat lagu 2 menit") atau gunakan stempel waktu untuk mengontrol durasi.

### Contoh perintah

Berikut beberapa contoh perintah yang efektif:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Praktik terbaik

- **Lakukan iterasi dengan Klip terlebih dahulu.** Gunakan model `lyria-3-clip-preview` yang lebih cepat untuk bereksperimen dengan perintah sebelum melakukan pembuatan berdurasi penuh dengan `lyria-3-pro-preview`.
- **Jadilah spesifik.** Perintah yang tidak jelas akan menghasilkan hasil yang umum. Sebutkan instrumen, BPM, kunci, suasana hati, dan struktur untuk output terbaik.
- **Sesuaikan bahasa Anda.** Buat perintah dalam bahasa yang Anda inginkan untuk lirik.
- **Gunakan tag bagian.** Tag `[Verse]`, `[Chorus]`, `[Bridge]` memberikan struktur yang jelas kepada model untuk diikuti.
- **Pisahkan lirik dari petunjuk.** Saat memberikan lirik kustom, pisahkan lirik tersebut dengan jelas dari petunjuk arah musik Anda.

## Batasan

- **Keamanan**: Semua perintah diperiksa oleh filter keamanan. Perintah yang memicu filter akan diblokir. Hal ini mencakup perintah yang meminta suara artis tertentu atau pembuatan lirik yang dilindungi hak cipta.
- **Watermarking**: Semua audio yang dibuat menyertakan
  [watermark audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=id) untuk
  identifikasi. Watermark ini tidak dapat didengar oleh telinga manusia dan tidak memengaruhi pengalaman mendengarkan.
- **Pengeditan berkelanjutan**: Pembuatan musik adalah proses satu kali.
  Pengeditan berulang atau menyempurnakan klip yang dibuat melalui beberapa perintah tidak didukung dalam versi Lyria 3 saat ini.
- **Panjang**: Model Klip selalu membuat klip 30 detik. Model Pro membuat lagu yang berlangsung selama beberapa menit; durasi yang tepat dapat dipengaruhi melalui perintah Anda.
- **Determinisme**: Hasil dapat bervariasi antar-panggilan, bahkan dengan perintah yang sama.

## Langkah berikutnya

- Periksa [harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk model Lyria 3,
- Coba [pembuatan musik streaming real-time](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=id)
  dengan Lyria RealTime,
- Buat percakapan multi-pembicara dengan model
  [TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id),
- Temukan cara membuat [gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) atau [video](https://ai.google.dev/gemini-api/docs/video?hl=id),
- Cari tahu cara Gemini dapat [memahami file audio](https://ai.google.dev/gemini-api/docs/audio?hl=id),
- Lakukan percakapan real-time dengan Gemini menggunakan the
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-22 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-22 UTC."],[],[]]
