---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=id
fetched_at: 2026-07-27T04:34:51.232133+00:00
title: "Terjemahan langsung dengan Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Terjemahan langsung dengan Gemini Live API

Gemini Live API mendukung terjemahan ucapan ke ucapan real-time dengan latensi rendah antara lebih dari 70 bahasa menggunakan model [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=id). Dengan mengonfigurasi Live API dengan setelan terjemahan, Anda dapat melakukan streaming audio dalam satu bahasa dan menerima output audio yang diterjemahkan dalam bahasa lain, sehingga memungkinkan terjemahan suara-ke-suara real-time yang lancar.

[Coba Terjemahan Lisan di Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=id)
[Clone aplikasi contoh dari GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Gunakan keterampilan agen codingterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id#gemini-live-api-dev)

## Agen Langsung vs. Terjemahan Langsung

Meskipun keduanya menggunakan Live API, model mental untuk Terjemahan Langsung berbeda dengan interaksi agen real-time percakapan.

| Agen Langsung | Terjemahan Langsung |
| --- | --- |
| **Model bertindak sebagai asisten.** Agen ini mendengarkan, menganalisis, dan mengambil tindakan atas nama Anda. | **Model bertindak sebagai penerjemah.** Pipeline ini berfungsi sebagai pipeline penerjemah real-time. |
| **Menggunakan interaksi berbasis giliran.** Mengandalkan jeda, deteksi niat, dan menangani gangguan. | **Menggunakan pemrosesan stream berkelanjutan.** Menerjemahkan saat pembicara berbicara tanpa menunggu giliran. |
| **Mendukung alat dan agen.** Dukungan native untuk pemanggilan fungsi, Google Penelusuran, dan petunjuk. | **Hanya mendukung terjemahan.** Terjemahan latensi rendah murni; tidak ada dukungan untuk alat atau petunjuk. |
| **Multimodal sepenuhnya.** Mendukung input teks, audio, video, dan gambar. | **Audio dibatasi.** Input terbatas pada audio untuk memastikan nilai minimum latensi real-time yang ketat. |
| **Konfigurasi terperinci.** Menggunakan pembuatan, ucapan, alat, dan petunjuk sistem. | **Konfigurasi yang disederhanakan.** Tetapkan `target_language_code` dan tombol seperti `echo_target_language`. |

## Mulai

Contoh berikut menunjukkan cara melakukan inisialisasi klien dan terhubung ke Live API dengan konfigurasi terjemahan.

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

## Mengirim audio

Untuk melakukan streaming input suara untuk terjemahan, Anda mengirimkan audio PCM 16-bit mentah, little-endian.

- **Format audio input**: PCM 16-bit mentah pada 16 kHz (mono, little-endian).
- **Format audio output**: PCM 16-bit mentah pada 24 kHz (mono, little-endian).
- **Ukuran Chunk dan Latensi**: Kirim audio dalam chunk 100 md.

Contoh berikut menunjukkan cara mengirimkan potongan audio ke sesi.

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

## Konfigurasi

Untuk mengaktifkan terjemahan, Anda harus menentukan `translationConfig` dalam `generationConfig` selama penyiapan sesi.

### Konfigurasi pesan penyiapan

`generationConfig` mendukung kolom berikut untuk mengaktifkan transkrip:

- **`inputAudioTranscription`**: Objek yang, jika ada, memungkinkan model mengirimkan transkrip teks dari audio input.
- **`outputAudioTranscription`**: Objek yang, jika ada, memungkinkan model mengirimkan transkrip teks dari audio output (yang diterjemahkan).

`translationConfig` mendukung kolom berikut:

- **`targetLanguageCode`**: [Kode bahasa BCP-47](#supported-languages) dari bahasa yang Anda inginkan untuk terjemahan model (misalnya, `"pl"` untuk Polandia, `"es"` untuk Spanyol). Nilai defaultnya adalah `"en"`.
- **`echoTargetLanguage`**: Boolean yang menunjukkan cara menangani audio input yang sudah dalam bahasa target. Jika disetel ke `true`, model akan mengulangi (menirukan) audio input yang sudah dalam bahasa target. Jika disetel ke `false`, model akan tetap diam saat ucapan input sudah dalam bahasa target. Nilai defaultnya adalah `false`.

Berikut adalah contoh struktur pesan penyiapan:

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

## Menggunakan token sementara di aplikasi sisi klien

Untuk aplikasi klien-ke-server, Anda dapat menggunakan [token sementara](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=id) (saat ini dalam `v1beta`) untuk menghindari pemaparan kunci API Anda.

Saat menggunakan token sementara dengan Terjemahan Langsung:

1. Anda harus menggunakan endpoint `v1beta`.
2. **Mengunci konfigurasi:** Secara default, Anda harus menentukan `translationConfig` dalam batasan pembuatan token di server Anda. Hal ini memastikan konfigurasi terjemahan dikunci dan tidak dapat dirusak oleh klien.
3. **Membuka kunci konfigurasi:** Jika Anda ingin dapat menyetel `translationConfig` di sisi klien (misalnya, untuk mengizinkan pengguna memilih bahasa targetnya sendiri), Anda harus menghapusnya dari permintaan pembuatan token dan menyetel `"lock_additional_fields": []` sebagai gantinya. Tindakan ini akan membuka kunci `translationConfig` untuk ditetapkan di sisi klien.

### Membuat token sementara yang dibatasi

Contoh berikut menunjukkan cara membuat token sementara dengan batasan terjemahan.

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

## Batasan

- **Modalitas Input**: Hanya input audio yang didukung untuk terjemahan. Input teks tidak didukung.
- **Replikasi Suara**: Replikasi suara dapat tidak konsisten. Suara dapat berubah setelah jeda yang panjang, menetapkan gender yang salah berdasarkan cara ucapan dimulai, atau macet pada satu suara selama percakapan multi-pembicara yang cepat.
- **Deteksi Bahasa**: Deteksi bahasa mengalami kesulitan dengan aksen berat, bahasa yang serupa (misalnya, Spanyol vs. Portugis), atau peralihan bahasa yang cepat. **Catatan:** Hal ini hanya akan memengaruhi transkrip input. Kode bahasa dan terjemahan akhir harus tetap akurat.
- **Audio Latar Belakang**: Model ini dirancang untuk memfilter suara bising dan musik guna menghasilkan ucapan yang jelas, tetapi tidak semua audio latar belakang dapat diabaikan.
- **Bahasa Target Gema (Echo)**: Jika `echoTargetLanguage: true`, suara bising di latar belakang atau musik dapat menimbulkan artefak dalam audio yang diterjemahkan jika audio input sudah dalam bahasa target.

## Bahasa yang didukung

Bahasa berikut didukung untuk Terjemahan Langsung.

| Language | Kode BCP-47 | Language | Kode BCP-47 |
| --- | --- | --- | --- |
| Afrika | af | Kazak | kk |
| Akan | ak | Khmer | km |
| Albania | sq | Kinyarwanda | rw |
| Amharik | am | Korea | ko |
| Arab | ar | Laos | lo |
| Armenia | hy | Latvia | lv |
| Azerbaijan | az | Lituania | lt |
| Basque | eu | Makedonia | mk |
| Belarusia | be | Melayu | md |
| Bengali | bn | Malayalam | ml |
| Bulgaria | bg | Marathi | mr |
| Burma (Myanmar) | my | Mongolia | mn |
| Katalan | ca | Nepal | ne |
| China (Aksara Sederhana) | zh-Hans | Norwegia | no, nb |
| China (Aksara Tradisional) | zh-Hant | Persia | fa |
| Kroasia | jam | Polandia | pl |
| Ceko | cs | Portugis (Brasil) | pt-BR |
| Denmark | da | Portugis (Portugal) | pt-PT |
| Belanda | nl | Punjabi | pa |
| Inggris | en | Rumania | ro |
| Estonia | et | Rusia | ru |
| Filipino | fil | Serbia | sr |
| Finlandia | fi | Sindhi | sd |
| Prancis | fr | Sinhala | si |
| Galisia | gl | Slovakia | sk |
| Georgia | ka | Slovenia | sl |
| Jerman | de | Spanyol | es |
| Yunani | el | Sunda | su |
| Gujarat | gu | Swahili | sw |
| Hausa | ha | Swedia | sv |
| Ibrani | dia | Tamil | ta |
| Hindi | hi | Telugu | te |
| Hungaria | hu | Thai | th |
| Islandia | is | Turki | tr |
| Indonesia | id | Ukraina | uk |
| Italia | it | Urdu | ur |
| Jepang | ja | Uzbek | uz |
| Jawa | jv | Vietnam | vi |
| Kannada | kn | Zulu | zu |

## Langkah berikutnya

- Baca panduan [Kemampuan](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=id) Live API selengkapnya.
- Baca panduan [Mulai menggunakan SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=id).
- Baca panduan [Mulai menggunakan WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=id).
- Baca panduan [Token sementara](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=id) untuk autentikasi yang aman di aplikasi klien ke server.
- Clone [Contoh API aktif](https://github.com/google-gemini/gemini-live-api-examples) dari GitHub.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-23 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-23 UTC."],[],[]]
