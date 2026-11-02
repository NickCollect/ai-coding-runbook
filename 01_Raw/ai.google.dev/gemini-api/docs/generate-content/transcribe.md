---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=id
fetched_at: 2026-11-02T07:18:51.895587+00:00
title: "Transkripsi audio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Transkripsi audio

Gemini API mengonversi ucapan dalam file audio menjadi teks menggunakan model Transcribe Gemini 3.5 (`gemini-3.5-transcribe`). Berdasarkan kemampuan pemahaman audio Gemini, API ini memberikan transkripsi yang akurat dengan identifikasi bahasa otomatis, diarisasi penutur, stempel waktu tingkat kata, dan petunjuk kosakata kustom. Fitur ini juga menyediakan mode [transkripsi cerdas](#transcription-modes) yang menampilkan penghapusan ketidaklancaran dan pemformatan cerdas.

Untuk mentranskripsikan file audio, upload audio dan teruskan ke `gemini-3.5-transcribe`:

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

## Ringkasan

Transkripsi Gemini 3.5 dioptimalkan untuk tugas speech-to-text. Model ini dapat menangani beragam aksen, suara bising di latar belakang, dan percakapan multi-bahasa.

Kemampuan utama meliputi:

- **Pengenalan ucapan otomatis (ASR):** Mendeteksi bahasa secara otomatis di [lebih dari 85 lokalitas](#supported-languages). Menangani peralihan kode intra-kalimat dan antar-kalimat tanpa konfigurasi manual.
- **Kosakata kustom:** Memiringkan pengenalan terhadap istilah khusus domain, akronim, dan nama diri dengan meneruskan hingga 1.000 frasa.
- **Diarisasi pembicara:** Membedakan beberapa pembicara dan mengatribusikan segmen yang diucapkan ke label yang berbeda.
- **Stempel waktu tingkat kata:** Membuat offset waktu mulai dan berakhir yang akurat untuk setiap kata yang dikenali.
- **Transkripsi pintar:** Menghapus ketidaklancaran, kata pengisi, pengulangan, dan menerapkan format terstruktur.
- **Pemformatan dan normalisasi:** Menerapkan kapitalisasi, tanda baca, dan normalisasi teks terbalik, seperti mengonversi "dua puluh enam juta dolar" menjadi "$26M".

Untuk penalaran audio umum atau menjawab pertanyaan terkait konten audio, gunakan [Pemahaman audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=id). Untuk sintesis audio text-to-speech, gunakan [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id).

## Deteksi dan petunjuk bahasa

Secara default, model akan mendeteksi bahasa lisan secara otomatis. Fitur ini beralih antarbahasa secara dinamis saat pembicara berganti kode.

Untuk menggunakan deteksi otomatis, hapus `language_codes` atau berikan daftar kosong:

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

Jika Anda mengetahui bahasa sebelumnya, tentukan kode bahasa BCP-47 di `language_codes` untuk meningkatkan akurasi transkripsi (lihat [Bahasa yang didukung](#supported-languages)):

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

## Kosakata kustom

Anda dapat mengarahkan model ucapan ke kata-kata yang tidak umum, jargon teknis, nama merek, atau nama diri. Berikan hingga 1.000 istilah dalam array `custom_vocabulary` (hasil terbaik biasanya dicapai dengan hingga 100 istilah):

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

## Diarisasi pembicara

Diarisasi pembicara mengidentifikasi suara yang berbeda dalam rekaman dan memberi tag pada setiap segmen dengan ID pembicara seperti `spk_1` atau `spk_2`. Hingga 8 speaker didukung (atribusi untuk 3 speaker atau lebih bersifat eksperimental).

Aktifkan pemisahan pembicara dengan menyetel `diarization` ke `True`:

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

## Stempel waktu tingkat kata

Stempel waktu tingkat kata memberikan offset awal dan akhir yang tepat untuk setiap kata yang dikenali dalam aliran audio.

Aktifkan stempel waktu dengan menyetel `word_timestamp` ke `True`:

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

Anda dapat menggabungkan `diarization` dan `word_timestamp` dalam satu permintaan untuk menerima label pembicara dan stempel waktu kata:

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

## Mode transkripsi

Gemini 3.5 Transcribe mendukung dua mode transkripsi melalui parameter `mode`:

- **`VERBATIM` (default)**: Menampilkan transkrip kata demi kata yang persis dari semua yang diucapkan, dengan mempertahankan kata pengisi mentah ("um", "eh", "kayak", "tahu"), pengulangan, jeda, dan awal yang salah. Diperlukan saat menggunakan stempel waktu atau diarization speaker.
- **`SMART` (Transkripsi cerdas)**: Mengoptimalkan transkrip untuk dibaca dengan menerapkan pasca-pemrosesan cerdas:
  - **Penghapusan ketidaklancaran**: Menghapus kata pengisi percakapan, gagap, dan permulaan yang salah.
  - **Koreksi mandiri inline**: Menyelesaikan koreksi lisan secara langsung (misalnya, *"Mari bertemu pada hari Selasa, eh tidak, hari Rabu pukul dua"* menjadi *"Mari bertemu pada hari Rabu pukul 14.00"*).
  - **Pemformatan terstruktur otomatis**: Secara otomatis menyusun pemikiran yang diucapkan menjadi paragraf, daftar bernomor, poin-poin, tanggal, mata uang, dan angka yang diformat.
  - **Pembersihan tata bahasa**: Menerapkan tanda baca, kapitalisasi kalimat, dan alur yang alami.

| Audio lisan | `VERBATIM` output | Output `SMART` (Transkripsi cerdas) |
| --- | --- | --- |
| "Um, jadi untuk rapat, saya pikir kita harus, eh, mengundang Alice dan, tunggu, bukan, Bob dan Carol." | "Jadi untuk rapat, menurutku kita harus mengundang Alice, eh bukan, Bob dan Carol." | "Untuk rapat, sebaiknya kita mengundang Budi dan Ari." |
| "Item pertama tinjau anggaran item kedua selesaikan linimasa item ketiga kirim ringkasan" | "tinjau anggaran item pertama selesaikan linimasa item kedua kirim ringkasan item ketiga" | "1. Tinjau anggaran 2. Menyelesaikan linimasa 3. Kirim ringkasan" |

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

## Mengurai output transkripsi

Teks transkrip lengkap ditampilkan di `response.text`.

Jika `word_timestamp` atau `diarization` diaktifkan, API juga akan menampilkan anotasi tingkat kata yang mendetail dan label pembicara yang dilampirkan ke bagian kandidat.

Berikut cara mengekstrak dan melakukan iterasi pada stempel waktu kata dan pergantian pembicara:

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
                  "endOffset": "0.400s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.800s"
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

## Bahasa yang didukung

Bahasa dan kode bahasa BCP-47 berikut didukung untuk Transkripsi Gemini 3.5:

| Language | Kode BCP-47 | Language | Kode BCP-47 |
| --- | --- | --- | --- |
| Afrika | `af-ZA` | Jepang | `ja-JP` |
| Amharik | `am-ET` | Jawa | `jv-ID` |
| Arab (Mesir) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenia | `hy-AM` | Kannada | `kn-IN` |
| Assam | `as-IN` | Kazak | `kk-KZ` |
| Azerbaijan | `az-AZ` | Korea | `ko-KR` |
| Belarusia | `be-BY` | Kirgiz | `ky-KG` |
| Bengali (Bangladesh) | `bn-BD` | Latvia | `lv-LV` |
| Bengali (India) | `bn-IN` | Lingala | `ln-CD` |
| Bosnia | `bs-BA` | Lituania | `lt-LT` |
| Bulgaria | `bg-BG` | Makedonia | `mk-MK` |
| Bulgaria (Aromania) | `rup-BG` | Melayu | `ms-MY` |
| Burma | `my-MM` | Malayalam | `ml-IN` |
| Kanton (Tradisional) | `yue-Hant-HK` | Malta | `mt-MT` |
| Katalan | `ca-ES` | China Mandarin (Aksara Sederhana) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer Tengah | `km-KH` | Mongolia | `mn-MN` |
| Kroasia | `hr-HR` | Nepal | `ne-NP` |
| Ceko | `cs-CZ` | Norwegia | `nb-NO` |
| Denmark | `da-DK` | Oriya | `or-IN` |
| Belanda | `nl-NL` | Polandia | `pl-PL` |
| Inggris (Britania Raya) | `en-GB` | Portugis (Brasil) | `pt-BR` |
| Inggris (India) | `en-IN` | Portugis (Portugal) | `pt-PT` |
| Inggris (Amerika Serikat) | `en-US` | Punjabi | `pa-IN` |
| Estonia | `et-EE` | Punjabi (skrip Gurmukhi) | `pa-Guru-IN` |
| Persia | `fa-IR` | Rumania | `ro-RO` |
| Filipino | `fil-PH` | Rusia | `ru-RU` |
| Finlandia | `fi-FI` | Serbia | `sr-RS` |
| Prancis | `fr-FR` | Sindhi (skrip Arab) | `sd-Arab-IN` |
| Galisia | `gl-ES` | Slovakia | `sk-SK` |
| Georgia | `ka-GE` | Slovenia | `sl-SI` |
| Jerman | `de-DE` | Spanyol (Amerika Latin) | `es-419` |
| Yunani | `el-GR` | Spanyol (Amerika Serikat) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausa | `ha-NG` | Swedia | `sv-SE` |
| Ibrani | `he-IL` | Tajik | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Hungaria | `hu-HU` | Thai | `th-TH` |
| Islandia | `is-IS` | Turki | `tr-TR` |
| Inggris - India | `en-IN` | Ukraina | `uk-UA` |
| Indonesia | `id-ID` | Uzbek | `uz-UZ` |
| Italia | `it-IT` | Vietnam | `vi-VN` |

## Format audio yang didukung

Transcribe Gemini 3.5 mendukung jenis MIME format audio berikut:

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

Untuk mengetahui daftar lengkap jenis MIME dan skema parameter yang didukung, lihat [referensi Interactions API](https://ai.google.dev/api/interactions-api?hl=id#Resource:Content).

## Referensi parameter

Konfigurasi transkripsi dengan menyetel kolom dalam objek `audio_transcription_config` di `GenerateContentConfig`:

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `language_codes` | Array string | Kode bahasa BCP-47 (misalnya, `["en-US"]`). Jika tidak ada atau kosong (`[]`), model akan otomatis mendeteksi bahasa dan menangani pengalihan kode. |
| `custom_vocabulary` | Array string | Hingga 1.000 istilah kustom, akronim, atau nama diri untuk memengaruhi pengenalan ucapan. Tidak kompatibel dengan diarisasi pembicara dan stempel waktu tingkat kata. |
| `word_timestamp` | Boolean | Setel ke `True` untuk menyertakan offset awal dan akhir kata. Jika dihilangkan atau `False`, tidak ada stempel waktu kata yang ditampilkan. Tidak kompatibel dengan kosakata kustom. |
| `diarization` | Boolean | Setel ke `True` untuk mengidentifikasi dan melabeli pembicara yang berbeda. Tidak kompatibel dengan kosakata kustom. |
| `mode` | String | Mode transkripsi. Nilai yang didukung: `"VERBATIM"` (default) dan `"SMART"`. Tidak kompatibel dengan stempel waktu dan diarisasi. |

## Praktik terbaik

- **Berikan audio yang jernih:** Pastikan rekaman audio memiliki pemisahan suara yang jelas dan hindari pemangkasan yang parah.
- **Berikan petunjuk bahasa jika diketahui:** Jika Anda mengetahui bahasa audio sebelumnya, tentukan `language_codes` untuk memaksimalkan akurasi.
- **Targetkan kosakata kustom:** Hanya sertakan istilah domain, nama merek, atau kata benda yang berbeda dalam `custom_vocabulary`, bukan kata-kata umum sehari-hari.
- **Gunakan Files API untuk rekaman berdurasi panjang:** Untuk file yang berdurasi lebih dari beberapa detik, upload file menggunakan `client.files.upload` dan teruskan file yang ditampilkan ke konten model.

## Batasan

- **Durasi audio:** Permintaan unary standar mendukung file audio hingga 1 jam. Pemrosesan audio dibatasi hingga 30 menit jika fitur seperti diarisasi speaker atau stempel waktu tingkat kata diaktifkan.
- **Stempel waktu tingkat kata:** Mengaktifkan stempel waktu tingkat kata dapat menurunkan akurasi transkripsi secara keseluruhan.
- **Diarisasi pembicara:** Diarisasi pembicara mendukung hingga 8 pembicara. Atribusi speaker untuk 3 speaker atau lebih bersifat eksperimental.
- **Kosakata kustom:** Anda dapat memberikan hingga 1.000 istilah dalam `custom_vocabulary`, tetapi hasil terbaik biasanya dicapai dengan hingga 100 istilah. Anda tidak dapat menggabungkan `custom_vocabulary` dengan diarisasi pembicara atau stempel waktu tingkat kata; API menolak permintaan yang menentukan `custom_vocabulary` bersama dengan salah satu fitur tersebut.
- **Kompatibilitas mode:** Transkripsi smart (`mode: "SMART"`) tidak dapat digabungkan dengan `word_timestamp` atau `diarization`.

## Langkah berikutnya

- Streaming audio real-time dengan [Panduan transkripsi langsung](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=id) menggunakan Live API.
- Jelajahi [Pemahaman audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=id) untuk menganalisis, meringkas, atau membuat kueri konten audio.
- Pelajari cara menyintesis audio dari teks menggunakan [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id).
- Periksa [halaman Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-3.5-transcribe) untuk mengetahui harga model dan batas token.
- Lihat panduan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id) untuk mengetahui detail tentang cara mengupload dan mengelola file media.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-23 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-23 UTC."],[],[]]
