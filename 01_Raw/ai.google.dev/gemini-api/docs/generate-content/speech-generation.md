---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id
fetched_at: 2026-10-26T05:59:52.189241+00:00
title: "Pembuatan text-to-speech (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Pembuatan text-to-speech (TTS)

Gemini API dapat mengubah input teks menjadi audio satu pembicara atau beberapa pembicara menggunakan kemampuan pembuatan text-to-speech (TTS) Gemini.
Pembuatan text-to-speech dapat
*[dikontrol](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#controllable)*,
artinya Anda dapat menggabungkan metadata giliran terstruktur (`speech_metadata`) dan tag vokal inline
untuk memandu *gaya*, *aksen*, *kecepatan*, dan *nada* audio.

[Coba di Google AI Studio](https://aistudio.google.com/generate-speech?hl=id)

Kemampuan TTS berbeda dengan pembuatan ucapan yang disediakan melalui
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=id), yang dirancang untuk audio interaktif,
tidak terstruktur, serta input dan output multimodal. Meskipun Live API unggul dalam konteks percakapan dinamis, TTS melalui Gemini API disesuaikan untuk skenario yang memerlukan pembacaan teks yang tepat dengan kontrol yang mendetail atas gaya dan suara, seperti pembuatan podcast atau buku audio.

Panduan ini menunjukkan cara membuat audio satu penutur dan multi-penutur dari
teks menggunakan [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id)
(`gemini-3.8-flash-tts`) dan
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id)
(`gemini-3.8-flash-lite-tts`).

## Sebelum memulai

Pastikan Anda menggunakan model Gemini TTS yang tercantum di bagian [Model yang didukung](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#supported-models). Untuk hasil yang optimal, tinjau
[Kapan harus menggunakan model yang mana](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#when-to-use-which-model)
untuk memilih model terbaik untuk workload Anda.

Anda mungkin perlu
[menguji model Gemini TTS di AI Studio](https://aistudio.google.com/generate-speech?hl=id)
sebelum mulai membangun.

## TTS satu penutur

Untuk mengonversi teks menjadi audio satu penutur dengan model Gemini 3.8 TTS, teruskan transkrip kata demi kata dalam `parts[].text`, lampirkan gaya tingkat giliran dalam
`parts[].speech_metadata`, dan konfigurasi suara Anda dalam
`speechConfig.voiceConfig`. Anda dapat meneruskan nama suara bawaan, ID Extended
Voice Library, ID
[Voice design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id) kustom (`voice_...`),
atau ID [Voice replication](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=id)
(`voice_...`, atau `voicekey_...` stateless opsional).

Contoh ini menyimpan audio output dari model dalam file WAV:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## TTS multi-pembicara

Untuk dialog multi-pembicara, konfigurasikan dua pembicara di
`multiSpeakerVoiceConfig.speakerVoiceConfigs` menggunakan `prebuiltVoiceConfig` dan
terus berikan setiap giliran dialog sebagai `part` terpisah dengan `speech_metadata` yang menentukan
`speaker` dan `style` tingkat giliran opsional:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## Mengontrol gaya ucapan dengan metadata dan tag

Gemini 3.8 TTS memperlakukan kolom `text` secara ketat sebagai transkrip verbatim. Untuk mengontrol penyampaian tanpa membacakan petunjuk panggung, bagi petunjuk Anda berdasarkan cakupan:

- **Penyampaian berkelanjutan di tingkat giliran (`speech_metadata.style`):** Masukkan emosi,
  gaya penyampaian, prosodi, kecepatan, dan volume yang berlaku di seluruh giliran
  dalam `speech_metadata.style` (misalnya, `"style": "whispered urgently"`,
  `"style": "out of breath"`, atau `"style": "warm and enthusiastic"`).
- **Peristiwa pada titik waktu tertentu (tag inline):** Tempatkan jeda atau ledakan vokal non-ucapan sesaat langsung di dalam transkrip menggunakan tanda kurung sudut (misalnya, `"Wait... <short pause> did you hear that? <sigh>"` atau
  `"Excuse me <cough> as I was saying..."`).

Lihat
[Panduan perintah](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#prompting-guide)
untuk mengetahui praktik terbaik yang komprehensif.

## Pilihan suara

Gemini 3.8 TTS mendukung empat cara untuk memilih atau membuat suara:

1. **Suara studio bawaan:** 30 suara pilihan yang tercantum dalam tabel berikut.
2. **Extended Voice Library:** Ratusan suara tambahan dalam berbagai bahasa, aksen, dan arketipe karakter yang dapat diakses menggunakan `client.voices.list()` (`GET /v1beta/voices`).
3. **[Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id):** Buat
   persona vokal kustom dari deskripsi bahasa alami di
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=id) atau menggunakan
   `POST /v1beta/voices` (`type="prompted"`, yang menampilkan ID
   `voice_...` persisten dan pratinjau WAV `sample_audio` di `CreateVoice` dan
   `GetVoice`).
4. **[Replikasi suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=id):**
   Replikasi suara pembicara dari audio referensi dan izin di
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=id) atau menggunakan
   `POST /v1beta/voices` (`type="replicated"`, `store=True` persisten secara
   default atau `store=False` stateless opsional).

### Batas suara kustom dan TTL

| Jenis suara | Mode penyimpanan | Kuota / batas | Retensi (TTL) |
| --- | --- | --- | --- |
| **Suara penting** (`voice_...`, diminta atau direplikasi) | `store=True` | **200 suara per project** (dibagikan di seluruh suara yang diminta dan direplikasi) | **1 tahun sejak penggunaan terakhir\*** |
| **Kunci suara stateless** (`voicekey_...`, direplikasi) | `store=False` | Dikelola klien | **7 hari** |

\* **Perpanjangan TTL:** Jendela retensi 1 tahun direset setiap kali suara digunakan secara aktif (baik dengan menyintesis ucapan dengan suara tersebut atau menggunakannya sebagai suara dasar untuk remix). Suara yang tidak memiliki aktivitas selama 1 tahun akan otomatis dihapus.

### Suara bawaan

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Ceria* | **Charon** -- *Informatif* |
| **Kore** -- *Firm* | **Fenrir** -- *Mudah Terangsang* | **Leda** -- *Muda* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *Santai* |
| **Autonoe** -- *Terang* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *Santai* | **Algieba** -- *Halus* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** -- *Berbatu* | **Rasalgethi** -- *Informatif* |
| **Laomedeia** -- *Ceria* | **Achernar** -- *Lembut* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Matang* | **Pulcherrima** -- *Meneruskan* |
| **Achird** -- *Ramah* | **Zubenelgenubi** -- *Kasual* | **Vindemiatrix** -- *Lembut* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Berpengetahuan* | **Sulafat** -- *Hangat* |

### Library Suara dan pemfilteran yang diperluas

Selain 30 suara studio unggulan dalam tabel sebelumnya, **Extended
Voice Library** menyediakan ratusan suara tambahan dalam berbagai bahasa,
aksen regional, persona karakter, dan domain. Anda dapat menjelajahi, memfilter, dan
mendengarkan Voice Library lengkap secara interaktif di
[Google AI Studio](https://aistudio.google.com/generate-speech?hl=id), atau membuat kueri
secara terprogram menggunakan `client.voices.list()` (`GET /v1beta/voices`, menggunakan
`google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` menampilkan suara tersimpan kustom Anda (diurutkan dari yang terbaru terlebih dahulu), diikuti dengan suara katalog bawaan yang cocok dengan kriteria filter Anda. Jika beberapa nilai
diteruskan untuk filter daftar, suara yang cocok dengan **nilai apa pun** dalam filter tersebut akan
ditampilkan (`OR`), sementara parameter filter yang berbeda digabungkan dengan `AND`:

| Parameter | Jenis | Deskripsi |
| --- | --- | --- |
| `language_code` | `list[str]` | Tag bahasa BCP-47 (misalnya, `["en-US", "en-GB"]`). Pencocokan persis yang tidak peka huruf besar/kecil. |
| `region_code` | `list[str]` | Kode wilayah ISO 3166-1 alpha-2 atau UN M.49 (misalnya, `["US", "GB"]`). |
| `accent` | `list[str]` | Deskripsi aksen regional (misalnya, `["American", "British"]`). |
| `gender` | `list[str]` | Presentasi gender yang terlihat (`"female"`, `"male"`, atau `"neutral"`). |
| `pitch` | `list[str]` | Klasifikasi nada suara (`"low"`, `"medium"`, atau `"high"`). |
| `persona` | `list[str]` | Persona vokal atau arketipe karakter (misalnya, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` di REST) | `list[str]` | Domain penggunaan optimal (misalnya, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` di Python) | `list[str]` | Filter menurut sumber suara: `"prebuilt"`, `"prompted"` ([Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id)), atau `"replicated"` ([Replikasi suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=id)). |
| `search` | `str` | Penelusuran substring teks bebas dicocokkan tanpa peka huruf besar/kecil dengan `display_name` dan `description`. |
| `page_size` | `int` | Jumlah maksimum suara yang ditampilkan per halaman (default `50`, maksimum `1000`). |
| `page_token` | `str` | Token dari `response.next_page_token` untuk mengambil halaman hasil berikutnya. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Bahasa yang didukung

Model TTS mendeteksi bahasa input secara otomatis.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id)
(`gemini-3.8-flash-tts`) mendukung **lebih dari 130 bahasa**, dan
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id)
(`gemini-3.8-flash-lite-tts`) mendukung **lebih dari 100 bahasa**:

| Language | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Aceh (Aksara Arab) | ✔️ | ✔️ |
| Afrika | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amharik | ✔️ | ✔️ |
| Armenia | ✔️ | ✔️ |
| Assam | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Bali | ✔️ | ✔️ |
| Bangla | ✔️ | ✔️ |
| Banjar (skrip Arab) | ✔️ | — |
| Banjar (Skrip Latn) | ✔️ | ✔️ |
| Bashkir | ✔️ | — |
| Basque | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Bhojpuri | ✔️ | ✔️ |
| Bosnia | ✔️ | ✔️ |
| Bugis | ✔️ | ✔️ |
| Bulgaria | ✔️ | ✔️ |
| Burma | ✔️ | — |
| Kanton | ✔️ | ✔️ |
| Katalan | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Kurdi Tengah | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| China (skrip Hans) | ✔️ | ✔️ |
| China (skrip Hant) | ✔️ | ✔️ |
| Crimean Tatar | ✔️ | — |
| Kroasia | ✔️ | ✔️ |
| Ceko | ✔️ | ✔️ |
| Denmark | ✔️ | ✔️ |
| Belanda | ✔️ | ✔️ |
| Dyula | ✔️ | — |
| Dzongkha | ✔️ | — |
| Arab Mesir | ✔️ | ✔️ |
| Inggris | ✔️ | ✔️ |
| Estonia | ✔️ | ✔️ |
| Filipino | ✔️ | ✔️ |
| Finlandia | ✔️ | — |
| Prancis | ✔️ | ✔️ |
| Galisia | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Georgia | ✔️ | ✔️ |
| Jerman | ✔️ | ✔️ |
| Yunani | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Gujarat | ✔️ | ✔️ |
| Kreol Haiti | ✔️ | ✔️ |
| Halh Mongolia | ✔️ | ✔️ |
| Hausa | ✔️ | ✔️ |
| Ibrani | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Hungaria | ✔️ | ✔️ |
| Islandia | ✔️ | ✔️ |
| Igbo | ✔️ | — |
| Iloko | ✔️ | ✔️ |
| Indonesia | ✔️ | ✔️ |
| Persia Iran | ✔️ | ✔️ |
| Italia | ✔️ | ✔️ |
| Jepang | ✔️ | ✔️ |
| Jawa | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Kashmir (skrip Arab) | ✔️ | ✔️ |
| Kashmir (skrip Deva) | ✔️ | ✔️ |
| Kazak | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Kinyarwanda | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Korea | ✔️ | ✔️ |
| Kirgiz | ✔️ | ✔️ |
| Laos | ✔️ | ✔️ |
| Latgalia | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituania | ✔️ | — |
| Luksemburg | ✔️ | — |
| Makedonia | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malayalam | ✔️ | ✔️ |
| Malta | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabau (skrip Arab) | ✔️ | ✔️ |
| Minangkabau (skrip Latn) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Nepali (bahasa individual) | ✔️ | ✔️ |
| Fulfulde Nigeria | ✔️ | ✔️ |
| Azerbaijan Utara | ✔️ | ✔️ |
| Sotho Utara | ✔️ | ✔️ |
| Uzbek Utara | ✔️ | ✔️ |
| Bokmål Norwegia | ✔️ | ✔️ |
| Nynorsk Norwegia | ✔️ | ✔️ |
| Nyanja | ✔️ | ✔️ |
| Occitan | ✔️ | — |
| Odia (bahasa individual) | ✔️ | ✔️ |
| Pangasinan | ✔️ | — |
| Persia (Afganistan) | ✔️ | ✔️ |
| Polandia | ✔️ | ✔️ |
| Portugis | ✔️ | ✔️ |
| Punjabi | ✔️ | ✔️ |
| Rumania | ✔️ | ✔️ |
| Rusia | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Serbia | ✔️ | ✔️ |
| Sindhi | ✔️ | — |
| Sinhala | ✔️ | ✔️ |
| Slovakia | ✔️ | ✔️ |
| Slovenia | ✔️ | — |
| Somali | ✔️ | — |
| Azerbaijan Selatan | ✔️ | ✔️ |
| Pashto Selatan | ✔️ | ✔️ |
| Sotho Selatan | ✔️ | — |
| Spanyol | ✔️ | ✔️ |
| Arab Standar (aksara Arab) | ✔️ | ✔️ |
| Arab Standar (skrip Latn) | ✔️ | ✔️ |
| Latvia Standar | ✔️ | ✔️ |
| Melayu Standar | ✔️ | ✔️ |
| Swahili (bahasa individual) | ✔️ | — |
| Swati | ✔️ | — |
| Swedia | ✔️ | — |
| Tajik | ✔️ | — |
| Tamil | ✔️ | ✔️ |
| Telugu | ✔️ | ✔️ |
| Thai | ✔️ | — |
| Tigrinya | ✔️ | — |
| Tosk Albania | ✔️ | — |
| Turki | ✔️ | ✔️ |
| Uyghur | ✔️ | — |
| Vietnam | ✔️ | ✔️ |

## Model yang didukung

| Model | Satu penutur | Multi-penutur | Desain suara | Replikasi suara |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Pratinjau Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=id) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=id) | ✔️ | ✔️ | — | — |

### Kapan harus menggunakan model tertentu

Kedua model TTS Gemini 3.8 memiliki skema API dan format perintah yang sama persis,
sehingga Anda dapat beralih di antara keduanya dengan satu perubahan parameter:

- **Gunakan [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id)
  (`gemini-3.8-flash-tts`)** jika fidelitas akustik maksimum, akting yang bernuansa, dan kontrol ekspresif menjadi prioritas utama. Model ini ideal untuk karya kreatif
  tingkat studio, dialog kompleks dengan banyak pembicara, tag burst vokal yang berat,
  pengucapan yang sulit, dialek regional atau minoritas, dan narasi panjang
  yang memerlukan stabilitas suara dan nada ruang yang sangat kuat.
- **Gunakan [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id)
  (`gemini-3.8-flash-lite-tts`)** sebagai pengganti `gemini-3.1-flash-tts-preview` yang cepat dan hemat biaya. Model ini dioptimalkan untuk
  produksi massal bervolume tinggi, kaskade agen suara percakapan, fitur
  baca lisan, replikasi suara yang andal, dan ucapan satu penutur sehari-hari
  dalam berbagai bahasa utama.

### Panduan migrasi

Saat mengupgrade dari model pratinjau sebelumnya (`gemini-3.1-flash-tts-preview` atau
`gemini-2.5-pro-preview-tts`) ke TTS Gemini 3.8 (`gemini-3.8-flash-tts` atau
`gemini-3.8-flash-lite-tts`), tinjau lima perubahan penting berikut:

1. **Pisahkan gaya dari transkrip:** Pindahkan petunjuk akting, nada, prosodi, dan tempo yang berkelanjutan (seperti `"whispering"`, `"out of breath"`, atau `"speaking slowly"`) dari teks biasa ke `speech_metadata.style`.
   Pertahankan `text` hanya sebagai transkrip kata demi kata ditambah tag vokal inline.
2. **Desain persona di awal dengan Desain suara:** Ganti blok multi-paragraf
   `"Audio Profile"` atau `"Director's Notes"` dengan suara kustom yang dibuat
   di [Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id), lalu
   bawa ID `voice_...` tersebut melalui permintaan TTS Anda dengan string
   `style` minimal atau kosong.
3. **Gunakan giliran dialog terstruktur:** Untuk dialog multi-pembicara, teruskan satu
   `part` per giliran pembicara dengan `speech_metadata.speaker`, bukan menyematkan
   prefiks `Speaker: ...` di dalam satu blok teks.
4. **Gunakan tanda kurung sudut untuk tag vokal inline:** Gunakan tanda kurung sudut (`<laugh>`,
   `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) untuk jeda dan vokalisasi manusia pada satu titik waktu. Hindari tag efek suara non-vokal (seperti
   tepuk tangan atau bunyi gedebuk).
5. **Perhitungkan output WAV (`AUDIO_WAV`) default pada permintaan unary:** Tidak seperti
   `gemini-3.1-flash-tts-preview` (yang menampilkan PCM mentah tanpa header
   `AUDIO_L16` secara default), model TTS Gemini 3.8 menampilkan audio **WAV
   (`AUDIO_WAV`)** lengkap dengan header RIFF (24 kHz, mono, PCM 16-bit) pada
   permintaan unary:
   - Jika kode Anda sebelumnya menggabungkan byte PCM mentah dalam header WAV (misalnya, menggunakan modul `wave` Python atau paket `wav` Node), hapus wrapper header manual dan tulis byte audio yang didekode langsung ke file `.wav`.
   - Jika pipeline yang ada memerlukan audio PCM mentah, mu-law, atau A-law tanpa header, tetapkan `generationConfig.responseFormat.audio.mimeType` secara eksplisit ke `"AUDIO_L16"`, `"AUDIO_MULAW"`, atau `"AUDIO_ALAW"` menggunakan REST API (misalnya, `{"responseFormat": {"audio": {"mimeType": "AUDIO_L16"}}}` di `generateContent`; penggantian `responseFormat` kustom di `generateContent` didukung menggunakan REST API, sedangkan dukungan Python dan JavaScript SDK untuk `response_format` di `GenerateContentConfig` masih tertunda, atau gunakan `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` di Interactions API). Lihat
     [Format output audio](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#audio-output-formats).

## Panduan menulis perintah

Model Gemini 3.8 TTS memperlakukan teks input secara ketat sebagai **transkrip verbatim**.
Tidak seperti model pratinjau sebelumnya yang menyematkan petunjuk panggung dalam teks biasa, Gemini 3.8 TTS memisahkan petunjuk tingkat giliran yang berkelanjutan (`speech_metadata`) dari tag vokal inline point-in-time.

### Kolom gaya versus tag inline

Pisahkan petunjuk performa Anda berdasarkan cakupan:

- **Penyampaian tingkat giliran (`speech_metadata.style`):** Masukkan atribut penyampaian berkelanjutan—seperti emosi, prosodi, kecepatan keseluruhan, atau gaya penyampaian (seperti `"whispering"`, `"out of breath"`, `"muttering"`, atau `"sarcastic"`)—ke dalam kolom `style` dari `speech_metadata`. Untuk membuat karakter dan
  performa yang stabil di seluruh giliran, desain persona di awal dalam
  [Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id) dan gunakan
  `style` hanya untuk penyesuaian opsional di tingkat giliran.
- **Peristiwa pada waktu tertentu (tag inline):** Tempatkan letupan vokal non-ucapan, napas, atau jeda sesaat secara inline di dalam transkrip menggunakan tanda kurung sudut (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Gunakan tanda kurung sudut (`<...>`) untuk kualitas audio tertinggi, dan gunakan vokalisasi manusia, bukan efek suara non-vokal.

| Cakupan | Tempat penempatan | Contoh |
| --- | --- | --- |
| **Tingkat giliran** (dipertahankan di seluruh giliran) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Point-in-time** (terjadi pada kata tertentu) | Inline di `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Kecepatan dan jeda

Anda dapat mengontrol ritme dan keheningan pada tiga tingkat perincian:

- **Tanda baca dan elipsis:** Gunakan koma, tanda hubung (`--`), dan elipsis (`...`)
  untuk keraguan percakapan yang alami.
- **Tag jeda inline:** Sisipkan `<short pause>` atau `<long pause>` pada titik yang tepat dalam skrip saat pembicara harus menjeda:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Kecepatan tingkat giliran:** Tetapkan `"style": "speaking rapidly"` atau
  `"style": "speaking slowly"` di `speech_metadata` untuk mengontrol kecepatan
  bicara di seluruh giliran.

### Prosodi dan nada

Gunakan **`speech_metadata.style`** untuk mengontrol prosodi, nada, dan infleksi di seluruh
giliran bicara (misalnya, `"style": "high pitch, cheerful and excited inflection"` atau
`"style": "monotone and flat"`). Jika emosi atau prosodi berubah di tengah dialog,
pisahkan skrip menjadi giliran bicara terpisah dengan nilai `style` yang berbeda untuk setiap giliran bicara.

### Penekanan

Gunakan huruf kapital untuk kata-kata tertentu dalam transkrip, yang dikombinasikan dengan tanda baca dan tag vokal inline, untuk memberikan penekanan vokal yang alami pada kata-kata kunci:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Suara vokal dan suara non-ucapan

Tempatkan vokalisasi manusia non-ucapan secara inline menggunakan tanda kurung sudut (`<...>`) pada
titik yang tepat di mana suara tersebut seharusnya muncul. Tag vokal yang direkomendasikan meliputi:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Saluran belakang dan ucapan yang tumpang-tindih

Dalam dialog multi-pembicara, gabungkan reaksi pendengar dalam karakter pipa
(`|reaction|`) di dalam giliran pembicara untuk membuat backchannel alami atau
ucapan yang tumpang tindih tanpa memecah menjadi giliran terpisah per reaksi.

- **Pertukaran backchannel singkat:** Lapisi reaksi singkat pendengar (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) di dalam giliran pembicara aktif:
  - **Giliran 1 (Pembicara A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Giliran 2 (Pembicara B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Giliran 3 (Pembicara A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Ucapan yang tumpang-tindih dan berselang-seling:** Gunakan beberapa segmen pipa untuk
  mensimulasikan ucapan simultan atau berselang-seling antara dua penutur (berfungsi paling baik
  dengan `gemini-3.8-flash-tts`):
  - **Hitung mundur/chorus serentak:** `"Let's surprise him on three |ok| ready?"` diikuti dengan `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Tumpang-tindih pembicara penuh:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Konsistensi di seluruh generasi dan hal yang harus dihindari

Ikuti panduan berikut untuk menjaga identitas vokal tetap stabil di seluruh giliran:

- **Desain persona di awal dalam Desain suara, bukan blok gaya panjang:**
  Paragraf `"Audio Profile"` panjang dan `"Director's Notes"` multi-butir
  yang dipertahankan dari model sebelumnya adalah penyebab paling umum terjadinya penyimpangan suara.
  Gunakan intuisi kreatif yang sama di awal dalam
  [Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id) untuk menghasilkan
  persona `voice_...` kustom yang persisten, lalu bawa ID suara tersebut melalui
  panggilan TTS Anda.
- **Mengandalkan referensi suara untuk stabilitas (menghilangkan meta-petunjuk):**
  Model TTS Gemini 3.8 dilatih untuk berfokus pada referensi audio terlebih dahulu.
  Jangan sertakan petunjuk yang meminta model untuk menjaga kestabilan suara (seperti
  `"do not switch speaker identity"` atau `"maintain identical timbre"`)—teks
  perintah tambahan meningkatkan penyimpangan. Hapus petunjuk gaya yang tidak diperlukan dan biarkan
  model bervariasi secara alami di sekitar titik stabil yang disediakan oleh referensi suara.
- **Jangan mencoba mengubah karakteristik penutur yang tidak dapat diubah di `style`:** Hindari memasukkan perubahan usia, gender, nama, atau aksen permanen di `speech_metadata.style`.
  Sebagai gantinya, pilih suara regional dari Extended Voice Library atau buat suara
  dengan [Voice design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id).

### Alur kerja yang direkomendasikan

1. **Buat karakter sekali:** Buat karakter Anda di
   [Voice design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id) atau pilih
   suara regional dari Extended Voice Library yang cocok dengan bahasa target
   dan persona Anda.
2. **Tulis transkrip lisan alami dengan ketidaklancaran:** Untuk mendapatkan kealamian
   maksimal, tulis `text` sebagai transkrip lisan yang nyata—termasuk ketidaklancaran dan keraguan percakapan alami (misalnya,
   `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Uji TTS biasa terlebih dahulu:** Sintesiskan transkrip Anda dengan kolom `style`
   kosong terlebih dahulu—sebagian besar permintaan tidak memerlukan petunjuk `style` sama sekali.
4. **Tambahkan perintah `style` singkat hanya untuk penyesuaian:** Tambahkan string `style` singkat
   (seperti `"casual, friendly"` atau `"muttering, then reassuring"`) hanya untuk
   belokan yang memerlukan penyesuaian pengiriman tertentu, dan gunakan kembali string
   singkat yang sama di seluruh belokan saat Anda menginginkan dasar pengukuran yang konsisten.

### Agen suara dan dialog multi-giliran

Saat membangun agen suara percakapan real-time atau aplikasi multi-giliran:

- Lakukan **satu panggilan TTS per giliran** saat potongan teks LLM tiba.
- Biarkan `voice` yang dikonfigurasi (`voice_...` bawaan, yang didesain, atau `voice_...` / `voicekey_...` yang direplikasi) membawa identitas pembicara di seluruh giliran—jangan pernah mengirim ulang persona karakter yang panjang di setiap giliran.
- Kosongkan kolom `style` per giliran, atau kirim satu string konstan pendek
  (seperti `"casual, friendly"`) untuk seluruh percakapan.
- Membagi respons agen yang panjang menjadi giliran yang lebih pendek daripada menggunakan perintah gaya yang lebih kuat.

## Pembuatan ucapan streaming

Anda dapat melakukan streaming audio yang dihasilkan saat disintesis oleh model. Tidak seperti
permintaan unary (yang menampilkan file WAV lengkap dengan header RIFF),
**permintaan streaming menampilkan potongan PCM linear 16-bit bertanda tangan little-endian mentah tanpa header (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, mono) secara
default** sehingga potongan audio dapat diputar atau digabungkan secara terus-menerus tanpa
header penampung:

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## Format output audio

Model TTS Gemini 3.8 menggunakan format audio default yang berbeda, bergantung pada apakah
permintaan bersifat unary atau streaming:

- **Permintaan unary (`models.generate_content`):** Menampilkan audio **WAV (`AUDIO_WAV`)** lengkap dengan header RIFF (24 kHz, mono, PCM little-endian bertanda tangan 16-bit). Anda dapat menulis byte audio yang didekode langsung ke file `.wav` tanpa menambahkan penampung WAV secara manual.
- **Permintaan streaming (`models.generate_content_stream` / `streamGenerateContent`):**
  Secara default, menampilkan potongan **PCM Linear mentah tanpa header (`AUDIO_L16`)** (PCM little-endian bertanda 16-bit, mono, 24 kHz) sehingga potongan dapat di-streaming atau digabungkan secara terus-menerus tanpa header penampung di setiap potongan.

Anda dapat mengganti encoding audio output dan frekuensi sampel menggunakan
`generationConfig.responseFormat.audio`:

| Nilai `mimeType` | Format | Deskripsi |
| --- | --- | --- |
| `"AUDIO_WAV"` *(default unary)* | WAV (`audio/wav`) | File WAV lengkap dengan header RIFF (24 kHz, mono, PCM 16-bit). |
| `"AUDIO_L16"` *(streaming default)* | PCM Linear (`audio/l16`) | PCM linear little-endian bertanda 16-bit mentah tanpa header. Paling cocok untuk streaming, pipeline audio kustom, atau menggabungkan klip multi-turn. |
| `"AUDIO_MULAW"` | μ-law (`audio/basic` / `audio/mulaw`) | Audio yang dikompresi dengan hukum μ G.711. Umumnya digunakan dalam telefoni Amerika Utara dan Jepang (8 kHz). |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | Audio companded A-law G.711. Umumnya digunakan dalam telefoni Eropa dan internasional (8 kHz). |

Anda juga dapat secara opsional menentukan `sampleRate` (misalnya, `24000`, `16000`, atau
`8000` Hz; defaultnya adalah `24000` Hz).

Contoh REST berikut meminta PCM 16-bit mentah tanpa header (`AUDIO_L16`) pada
24 kHz:

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## Batasan

- Model TTS menerima input khusus teks dan menghasilkan output khusus audio.
- Pembuatan multi-pembicara dengan satu permintaan (`multiSpeakerVoiceConfig`) mendukung
  hingga 2 pembicara menggunakan suara bawaan. Untuk menggabungkan suara yang didesain khusus
  (`voice_...`) atau direplikasi (`voice_...` / `voicekey_...`) dalam
  dialog multi-karakter, sintesiskan setiap giliran bicara secara terpisah.
  Karena permintaan unary menampilkan `audio/wav` dengan header RIFF 44 byte secara default, minta PCM mentah (`AUDIO_L16`) atau hapus header WAV dari setiap giliran sebelum menggabungkan frame audio PCM 24 kHz.
- **Batas penyimpanan suara kustom dan TTL:**
  - **Suara stateful (`store=True`, dipromosikan atau direplikasi):** Maksimum
    **200 suara per project** dengan **TTL 1 tahun** (time-to-live).
  - **Kunci suara stateless (`store=False`, `voicekey_...`):** **TTL 7 hari**
    (time-to-live).
- Tinjau bagian
  [Bahasa yang didukung](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#languages)
  untuk mengetahui cakupan bahasa.

## Langkah berikutnya

- Buat persona vokal kustom dari bahasa alami dengan
  [Desain suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id).
- Mereplikasi suara pembicara yang ada di
  [Replikasi suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=id).
- Bandingkan spesifikasi model di halaman model [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id) dan [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id).
- Pelajari audio dua arah interaktif dengan
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-12 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-12 UTC."],[],[]]
