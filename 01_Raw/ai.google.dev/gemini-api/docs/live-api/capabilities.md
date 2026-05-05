---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=id
fetched_at: 2026-05-05T13:15:36.095399+00:00
title: "Live API capabilities guide \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/live-api/Deep Research Gemini) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

- [Beranda](https://ai.google.dev/gemini-api/docs/live-api/Beranda)
- [Gemini API](https://ai.google.dev/gemini-api/docs/live-api/Gemini API)
- [Dokumen](https://ai.google.dev/gemini-api/docs/live-api/Dokumen)

Kirim masukan

# Live API capabilities guide

Ini adalah panduan komprehensif yang mencakup kemampuan dan konfigurasi yang tersedia dengan Live API.
Lihat halaman [Mulai menggunakan Live API](https://ai.google.dev/gemini-api/docs/live-api/Mulai menggunakan Live API) untuk mengetahui ringkasan dan contoh kode untuk kasus penggunaan umum.

## Sebelum memulai

- **Pahami konsep inti:** Jika belum melakukannya,
  baca halaman [Mulai menggunakan Live API](https://ai.google.dev/gemini-api/docs/live-api/Mulai menggunakan Live API)  terlebih dahulu.
  Bagian ini akan memperkenalkan Anda pada prinsip-prinsip dasar Live API, cara kerjanya, dan berbagai [pendekatan penerapan](https://ai.google.dev/gemini-api/docs/live-api/pendekatan penerapan).
- **Coba Live API di AI Studio:** Anda mungkin merasa berguna untuk mencoba
  Live API di [Google AI Studio](https://ai.google.dev/gemini-api/docs/live-api/Google AI Studio) sebelum mulai membangun. Untuk menggunakan
  Live API di Google AI Studio, pilih **Stream**.

## Perbandingan model

Tabel berikut merangkum perbedaan utama antara model
[Pratinjau Langsung Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/live-api/Pratinjau Langsung Gemini 3.1 Flash) dan [Pratinjau Langsung Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/live-api/Pratinjau Langsung Gemini 2.5 Flash):

| Fitur | Pratinjau Langsung Gemini 3.1 Flash | Pratinjau Langsung Gemini 2.5 Flash |
| --- | --- | --- |
| **[Berpikir](https://ai.google.dev/gemini-api/docs/live-api/Berpikir)** | Menggunakan `thinkingLevel` untuk mengontrol kedalaman penalaran dengan setelan seperti `minimal`, `low`, `medium`, dan `high`. Defaultnya adalah `minimal` untuk mengoptimalkan latensi terendah. Lihat [Tingkat dan anggaran yang perlu dipertimbangkan](https://ai.google.dev/gemini-api/docs/live-api/Tingkat dan anggaran yang perlu dipertimbangkan). | Menggunakan `thinkingBudget` untuk menetapkan jumlah token penalaran. Pemikiran dinamis diaktifkan secara default. Tetapkan `thinkingBudget` ke `0` untuk menonaktifkan. Lihat [Tingkat dan anggaran yang perlu dipertimbangkan](https://ai.google.dev/gemini-api/docs/live-api/Tingkat dan anggaran yang perlu dipertimbangkan). |
| **[Menerima respons](https://ai.google.dev/gemini-api/docs/live-api/Menerima respons)** | Satu peristiwa server dapat berisi beberapa bagian konten secara bersamaan (misalnya, `inlineData` dan transkrip). Pastikan kode Anda memproses semua bagian dalam setiap peristiwa untuk menghindari hilangnya konten. | Setiap peristiwa server hanya berisi satu bagian konten. Bagian dikirim dalam acara terpisah. |
| **[Konten klien](https://ai.google.dev/gemini-api/docs/live-api/Konten klien)** | `send_client_content` hanya didukung untuk mengisi histori konteks awal (memerlukan setelan `initial_history_in_client_content` dalam konfigurasi sesi). Untuk mengirim pembaruan teks selama percakapan, gunakan `send_realtime_input`. | `send_client_content` didukung di seluruh percakapan untuk mengirim update konten inkremental dan menetapkan konteks. |
| **[Cakupan belokan](https://ai.google.dev/gemini-api/docs/live-api/Cakupan belokan)** | Default-nya adalah `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. Giliran model mencakup aktivitas audio yang terdeteksi dan semua frame video. | Default-nya adalah `TURN_INCLUDES_ONLY_ACTIVITY`. Giliran model hanya mencakup aktivitas yang terdeteksi. |
| **[VAD Kustom](https://ai.google.dev/gemini-api/docs/live-api/VAD Kustom)** (`activity_start`/`activity_end`) | Didukung. Nonaktifkan VAD otomatis dan kirim pesan `activityStart` dan `activityEnd` secara manual untuk mengontrol batas giliran. | Didukung. Nonaktifkan VAD otomatis dan kirim pesan `activityStart` dan `activityEnd` secara manual untuk mengontrol batas giliran. |
| **[Konfigurasi VAD otomatis](https://ai.google.dev/gemini-api/docs/live-api/Konfigurasi VAD otomatis)** | Didukung. Konfigurasi parameter seperti `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms`, dan `silence_duration_ms`. | Didukung. Konfigurasi parameter seperti `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms`, dan `silence_duration_ms`. |
| **[Panggilan fungsi asinkron](https://ai.google.dev/gemini-api/docs/live-api/Panggilan fungsi asinkron)** (`behavior: NON_BLOCKING`) | Tidak didukung. Panggilan fungsi hanya berurutan. Model tidak akan mulai merespons hingga Anda mengirimkan respons alat. | Didukung. Tetapkan `behavior` ke `NON_BLOCKING` pada deklarasi fungsi agar model dapat terus berinteraksi saat fungsi berjalan. Kontrol cara model menangani respons dengan parameter `scheduling` (`INTERRUPT`, `WHEN_IDLE`, atau `SILENT`). |
| **[Audio proaktif](https://ai.google.dev/gemini-api/docs/live-api/Audio proaktif)** | Tidak didukung | Didukung. Jika diaktifkan, model dapat secara proaktif memutuskan untuk tidak merespons jika konten input tidak relevan. Tetapkan `proactive_audio` ke `true` dalam konfigurasi `proactivity` (memerlukan `v1alpha`). |
| **[Dialog afektif](https://ai.google.dev/gemini-api/docs/live-api/Dialog afektif)** | Tidak didukung | Didukung. Model menyesuaikan gaya responsnya agar sesuai dengan ekspresi dan nada bahasa input. Tetapkan `enable_affective_dialog` ke `true` dalam konfigurasi sesi (memerlukan `v1alpha`). |

Untuk bermigrasi dari Gemini 2.5 Flash Live ke Gemini 3.1 Flash Live, lihat [panduan migrasi](https://ai.google.dev/gemini-api/docs/live-api/panduan migrasi).

## Membuat koneksi

Contoh berikut menunjukkan cara membuat koneksi dengan kunci API:

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

## Modalitas interaksi

Bagian berikut memberikan contoh dan konteks pendukung untuk berbagai modalitas input dan output yang tersedia di Live API.

### Mengirim audio

Audio harus dikirim sebagai data PCM mentah (audio PCM 16-bit mentah, 16 kHz, little-endian).

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

### Format audio

Data audio di Live API selalu berupa PCM 16-bit mentah, little-endian. Output audio selalu menggunakan frekuensi sampling 24 kHz. Audio input
secara native adalah 16 kHz, tetapi Live API akan melakukan pengambilan sampel ulang jika diperlukan
sehingga frekuensi sampel apa pun dapat dikirim. Untuk menyampaikan sample rate audio input, tetapkan
jenis MIME setiap [Blob](https://ai.google.dev/gemini-api/docs/live-api/Blob) yang berisi audio ke nilai
seperti `audio/pcm;rate=16000`.

### Menerima audio

Respons audio model diterima sebagai potongan data.

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

### Mengirim SMS

Teks dapat dikirim menggunakan `send_realtime_input` (Python) atau `sendRealtimeInput` (JavaScript).

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

### Mengirim video

Frame video dikirim sebagai gambar individual (misalnya, JPEG atau PNG) pada kecepatan frame tertentu (maks. 1 frame per detik).

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

#### Pembaruan konten inkremental

Gunakan update inkremental untuk mengirim input teks, membuat konteks sesi, atau
memulihkan konteks sesi. Untuk konteks singkat, Anda dapat mengirimkan interaksi belokan demi belokan untuk merepresentasikan urutan peristiwa yang tepat:

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

Untuk konteks yang lebih panjang, sebaiknya berikan ringkasan pesan tunggal untuk mengosongkan jendela konteks untuk interaksi berikutnya. Lihat [Melanjutkan Sesi](https://ai.google.dev/gemini-api/docs/live-api/Melanjutkan Sesi) untuk metode lain dalam memuat konteks sesi.

### Transkripsi audio

Selain respons model, Anda juga dapat menerima transkripsi
output audio dan input audio.

Untuk mengaktifkan transkripsi output audio model, kirim
`output_audio_transcription` dalam konfigurasi penyiapan. Bahasa transkripsi disimpulkan dari respons model.

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

Untuk mengaktifkan transkripsi input audio model, kirim
`input_audio_transcription` dalam konfigurasi penyiapan.

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

### Mengubah suara dan bahasa

Model [output audio bawaan](https://ai.google.dev/gemini-api/docs/live-api/output audio bawaan) mendukung suara apa pun yang tersedia untuk model [Text-to-Speech (TTS)](https://ai.google.dev/gemini-api/docs/live-api/Text-to-Speech (TTS)) kami. Anda dapat mendengarkan semua suara di [AI Studio](https://ai.google.dev/gemini-api/docs/live-api/AI Studio).

Untuk menentukan suara, tetapkan nama suara dalam objek `speechConfig` sebagai bagian
dari konfigurasi sesi:

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

Live API mendukung [beberapa bahasa](https://ai.google.dev/gemini-api/docs/live-api/beberapa bahasa).
Model [output audio native](https://ai.google.dev/gemini-api/docs/live-api/output audio native) secara otomatis memilih
bahasa yang sesuai dan tidak mendukung penetapan kode
bahasa secara eksplisit.

## Kemampuan audio native

Model terbaru kami memiliki [output audio bawaan](https://ai.google.dev/gemini-api/docs/live-api/output audio bawaan), yang memberikan ucapan yang terdengar alami dan realistis serta peningkatan performa multibahasa.

### Penalaran

Model Gemini 3.1 menggunakan `thinkingLevel` untuk mengontrol kedalaman pemikiran, dengan setelan seperti `minimal`, `low`, `medium`, dan `high`. Defaultnya adalah `minimal` untuk mengoptimalkan latensi terendah. Model Gemini 2.5 menggunakan
`thinkingBudget` untuk menetapkan jumlah token penalaran. Untuk mengetahui detail selengkapnya
tentang tingkat vs. anggaran, lihat
[Memikirkan tingkat dan anggaran](https://ai.google.dev/gemini-api/docs/live-api/Memikirkan tingkat dan anggaran).

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

Selain itu, Anda dapat mengaktifkan ringkasan pemikiran dengan menyetel `includeThoughts` ke
`true` dalam konfigurasi Anda. Lihat [ringkasan pemikiran](https://ai.google.dev/gemini-api/docs/live-api/ringkasan pemikiran)
untuk mengetahui info selengkapnya:

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

### Dialog afektif

Fitur ini memungkinkan Gemini menyesuaikan gaya responsnya dengan ekspresi dan nada bahasa input.

Untuk menggunakan dialog afektif, tetapkan versi API ke `v1alpha` dan tetapkan
`enable_affective_dialog` ke `true`dalam pesan penyiapan:

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

### Audio proaktif

Jika fitur ini diaktifkan, Gemini dapat secara proaktif memutuskan untuk tidak merespons
jika konten tidak relevan.

Untuk menggunakannya, tetapkan versi API ke `v1alpha` dan konfigurasi kolom `proactivity` dalam pesan penyiapan, lalu tetapkan `proactive_audio` ke `true`:

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

## Deteksi Aktivitas Suara (VAD)

Deteksi Aktivitas Suara (VAD) memungkinkan model mengenali saat seseorang sedang berbicara. Hal ini penting untuk menciptakan percakapan yang alami, karena memungkinkan pengguna menginterupsi model kapan saja.

Saat VAD mendeteksi gangguan, pembuatan yang sedang berlangsung akan dibatalkan dan
dihapus. Hanya informasi yang sudah dikirim ke klien yang dipertahankan dalam histori sesi. Server kemudian mengirimkan pesan [`BidiGenerateContentServerContent`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentServerContent`) untuk melaporkan gangguan.

Server Gemini kemudian akan membatalkan semua panggilan fungsi yang tertunda dan mengirim pesan `BidiGenerateContentServerContent` dengan ID panggilan yang dibatalkan.

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

### VAD otomatis

Secara default, model akan otomatis melakukan VAD pada
aliran input audio berkelanjutan. VAD dapat dikonfigurasi dengan kolom
[`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/gemini-api/docs/live-api/`realtimeInputConfig.automaticActivityDetection`)
dari [konfigurasi penyiapan](https://ai.google.dev/gemini-api/docs/live-api/konfigurasi penyiapan).

Saat aliran audio dijeda selama lebih dari satu detik (misalnya,
karena pengguna menonaktifkan mikrofon), peristiwa
[`audioStreamEnd`](https://ai.google.dev/gemini-api/docs/live-api/`audioStreamEnd`)
harus dikirim untuk menghapus semua audio yang di-cache. Klien dapat melanjutkan pengiriman data audio kapan saja.

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

Dengan `send_realtime_input`, API akan merespons audio secara otomatis berdasarkan
VAD. Meskipun `send_client_content` menambahkan pesan ke konteks model secara berurutan, `send_realtime_input` dioptimalkan untuk responsivitas dengan mengorbankan pengurutan deterministik.

### Konfigurasi VAD otomatis

Untuk kontrol yang lebih besar atas aktivitas VAD, Anda dapat mengonfigurasi parameter berikut. Lihat [referensi API](https://ai.google.dev/gemini-api/docs/live-api/referensi API) untuk mengetahui info selengkapnya.

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

### Menonaktifkan VAD otomatis

Atau, VAD otomatis dapat dinonaktifkan dengan menyetel
`realtimeInputConfig.automaticActivityDetection.disabled` ke `true` dalam pesan
penyiapan. Dalam konfigurasi ini, klien bertanggung jawab untuk mendeteksi ucapan pengguna dan mengirim pesan
[`activityStart`](https://ai.google.dev/gemini-api/docs/live-api/`activityStart`)
dan [`activityEnd`](https://ai.google.dev/gemini-api/docs/live-api/`activityEnd`)
pada waktu yang tepat. `audioStreamEnd` tidak dikirim dalam konfigurasi ini. Sebagai gantinya, setiap gangguan streaming ditandai dengan pesan `activityEnd`.

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

## Jumlah token

Anda dapat menemukan jumlah total token yang digunakan di kolom
[usageMetadata](https://ai.google.dev/gemini-api/docs/live-api/usageMetadata) dari pesan server yang ditampilkan.

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

## Resolusi media

Anda dapat menentukan resolusi media untuk media input dengan menyetel kolom
`mediaResolution` sebagai bagian dari konfigurasi sesi:

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

## Batasan

Pertimbangkan batasan Live API berikut saat Anda merencanakan project.

### Modalitas respons

Model audio native hanya mendukung modalitas respons `AUDIO`. Jika Anda memerlukan
respons model sebagai teks, gunakan fitur [transkripsi audio output](https://ai.google.dev/gemini-api/docs/live-api/transkripsi audio output).

### Autentikasi klien

Live API hanya menyediakan autentikasi server-ke-server secara default. Jika Anda menerapkan aplikasi Live API menggunakan [pendekatan client-to-server](https://ai.google.dev/gemini-api/docs/live-api/pendekatan client-to-server), Anda harus menggunakan [token sementara](https://ai.google.dev/gemini-api/docs/live-api/token sementara) untuk mengurangi risiko keamanan.

### Durasi sesi

Sesi audio saja dibatasi hingga 15 menit,
dan sesi audio plus video dibatasi hingga 2 menit.
Namun, Anda dapat mengonfigurasi berbagai [teknik pengelolaan sesi](https://ai.google.dev/gemini-api/docs/live-api/teknik pengelolaan sesi) untuk perpanjangan tanpa batas pada durasi sesi.

### Jendela konteks

Sesi memiliki batas jendela konteks:

- 128 ribu token untuk model [output audio native](https://ai.google.dev/gemini-api/docs/live-api/output audio native)
- 32 ribu token untuk model Live API lainnya

## Bahasa yang didukung

Live API mendukung 97 bahasa berikut.

| Language | Kode BCP-47 | Language | Kode BCP-47 |
| --- | --- | --- | --- |
| Afrika | `af` | Latvia | `lv` |
| Akan | `ak` | Lituania | `lt` |
| Albania | `sq` | Makedonia | `mk` |
| Amharik | `am` | Melayu | `ms` |
| Arab | `ar` | Malayalam | `ml` |
| Armenia | `hy` | Malta | `mt` |
| Assam | `as` | Maori | `mi` |
| Azerbaijan | `az` | Marathi | `mr` |
| Basque | `eu` | Mongolia | `mn` |
| Belarusia | `be` | Nepal | `ne` |
| Bengali | `bn` | Norwegia | `no` |
| Bosnia | `bs` | Odia | `or` |
| Bulgaria | `bg` | Oromo | `om` |
| Burma | `my` | Pashto | `ps` |
| Katalan | `ca` | Persia | `fa` |
| Cebuano | `ceb` | Polandia | `pl` |
| China | `zh` | Portugis | `pt` |
| Kroasia | `hr` | Punjabi | `pa` |
| Ceko | `cs` | Quechua | `qu` |
| Denmark | `da` | Rumania | `ro` |
| Belanda | `nl` | Romansh | `rm` |
| Inggris | `en` | Rusia | `ru` |
| Estonia | `et` | Serbia | `sr` |
| Faroe | `fo` | Sindhi | `sd` |
| Filipino | `fil` | Sinhala | `si` |
| Finlandia | `fi` | Slovakia | `sk` |
| Prancis | `fr` | Slovenia | `sl` |
| Galisia | `gl` | Somali | `so` |
| Georgia | `ka` | Sotho Selatan | `st` |
| Jerman | `de` | Spanyol | `es` |
| Yunani | `el` | Swahili | `sw` |
| Gujarat | `gu` | Swedia | `sv` |
| Hausa | `ha` | Tajik | `tg` |
| Ibrani | `iw` | Tamil | `ta` |
| Hindi | `hi` | Telugu | `te` |
| Hungaria | `hu` | Thai | `th` |
| Islandia | `is` | Tswana | `tn` |
| Indonesia | `id` | Turki | `tr` |
| Irlandia | `ga` | Turkmen | `tk` |
| Italia | `it` | Ukraina | `uk` |
| Jepang | `ja` | Urdu | `ur` |
| Kannada | `kn` | Uzbek | `uz` |
| Kazak | `kk` | Vietnam | `vi` |
| Khmer | `km` | Wales | `cy` |
| Kinyarwanda | `rw` | Frisia Barat | `fy` |
| Korea | `ko` | Wolof | `wo` |
| Kurdi | `ku` | Yoruba | `yo` |
| Kirgiz | `ky` | Zulu | `zu` |
| Laos | `lo` |  |  |

## Langkah berikutnya

- Baca panduan [Penggunaan Alat](https://ai.google.dev/gemini-api/docs/live-api/Penggunaan Alat) dan
  [Pengelolaan Sesi](https://ai.google.dev/gemini-api/docs/live-api/Pengelolaan Sesi) untuk mendapatkan informasi penting tentang cara menggunakan Live API secara efektif.
- Coba Live API di [Google AI Studio](https://ai.google.dev/gemini-api/docs/live-api/Google AI Studio).
- Untuk mengetahui info selengkapnya tentang model Live API, lihat [Audio Native Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/live-api/Audio Native Gemini 2.5 Flash)
  di halaman Model.
- Coba contoh lainnya di [buku resep Live API](https://ai.google.dev/gemini-api/docs/live-api/buku resep Live API),
  [buku resep Alat Live API](https://ai.google.dev/gemini-api/docs/live-api/buku resep Alat Live API),
  dan [skrip Memulai Live API](https://ai.google.dev/gemini-api/docs/live-api/skrip Memulai Live API).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/live-api/Lisensi Creative Commons Attribution 4.0), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://ai.google.dev/gemini-api/docs/live-api/Lisensi Apache 2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://ai.google.dev/gemini-api/docs/live-api/Kebijakan Situs Google Developers). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?
