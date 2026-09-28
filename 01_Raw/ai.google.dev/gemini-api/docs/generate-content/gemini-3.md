---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=id
fetched_at: 2026-09-28T06:19:33.343936+00:00
title: "Panduan developer Gemini 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)

Kirim masukan

# Panduan developer Gemini 3

Gemini 3 adalah rangkaian model tercerdas kami hingga saat ini, yang dibangun berdasarkan penalaran canggih. Model ini dirancang untuk mewujudkan ide apa pun dengan menguasai alur kerja agentic, coding otonom, dan tugas multimodal yang kompleks.
Panduan ini membahas fitur utama rangkaian model Gemini 3 dan cara mengoptimalkan penggunaannya.

[Coba Pratinjau Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=id)
[Coba Pratinjau Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=id)
[Coba Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=id)
[Coba Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=id)

Jelajahi [koleksi aplikasi Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=id) kami untuk melihat cara model menangani penalaran tingkat lanjut, coding otonom, dan tugas multimodal yang kompleks.

Mulai dengan beberapa baris kode:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Memperkenalkan seri Gemini 3

Gemini 3.1 Pro paling cocok untuk tugas kompleks yang memerlukan pengetahuan umum yang luas dan penalaran canggih di berbagai modalitas.

Gemini 3 Flash adalah model seri 3 terbaru kami, dengan kecerdasan tingkat Pro pada kecepatan dan harga Flash.

Nano Banana Pro (juga dikenal sebagai Gemini 3 Pro Image) adalah model pembuatan gambar berkualitas tertinggi kami, dan Nano Banana 2 (juga dikenal sebagai Gemini 3.1 Flash Image) adalah model yang setara dengan volume tinggi, efisiensi tinggi, dan titik harga lebih rendah.

Gemini 3.1 Flash-Lite adalah model andalan kami yang dibuat untuk model hemat biaya dan tugas bervolume tinggi.

| ID Model | Jendela Konteks (Masuk / Keluar) | Batas Informasi | Harga (Input / Output)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Jan 2025 | $0,25 (teks, gambar, video), $0,50 (audio) / $1,50 |
| **gemini-3.1-flash-image-preview** | 128 ribu / 32 ribu | Jan 2025 | $0,25 (Input Teks) / $0,067 (Output Gambar)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Jan 2025 | $2 / $12 (<200 ribu token)   $4 / $18 (>200 ribu token) |
| **gemini-3-flash-preview** | 1M / 64k | Jan 2025 | $0,50 / $3 |
| **gemini-3-pro-image-preview** | 65 ribu / 32 ribu | Jan 2025 | $2 (Input Teks) / $0,134 (Output Gambar)\*\* |

*\* Harga adalah per 1 juta token, kecuali dinyatakan lain.*
*\*\* Harga gambar bervariasi menurut resolusi. Lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detailnya.*

Untuk mengetahui batas, harga, dan informasi tambahan yang mendetail, lihat [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id).

## Fitur API baru di Gemini 3

Gemini 3 memperkenalkan parameter baru yang dirancang untuk memberi developer kontrol lebih besar atas latensi, biaya, dan kualitas multimodal.

### Tingkat penalaran

Model seri Gemini 3 menggunakan penalaran dinamis secara default untuk memproses perintah. Anda dapat menggunakan parameter `thinking_level`, yang mengontrol
kedalaman **maksimum** dari proses penalaran internal model sebelum menghasilkan
respons. Gemini 3 memperlakukan level ini sebagai alokasi relatif untuk berpikir, bukan jaminan token yang ketat.

Jika `thinking_level` tidak ditentukan, Gemini 3 akan ditetapkan secara default ke `high`. Untuk respons yang lebih cepat dan latensi yang lebih rendah saat penalaran yang kompleks tidak diperlukan, Anda dapat membatasi tingkat pemikiran model ke `low`.

| Tingkat Penalaran | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Deskripsi |
| --- | --- | --- | --- | --- |
| **`minimal`** | Tidak didukung | Didukung (Default) | Didukung | Cocok dengan setelan "tanpa penalaran" untuk sebagian besar kueri. Model mungkin berpikir sangat minimal untuk tugas coding yang kompleks. Meminimalkan latensi untuk aplikasi chat atau throughput tinggi. Perhatikan, `minimal` tidak menjamin bahwa pemikiran tidak berfungsi. |
| **`low`** | Didukung | Didukung | Didukung | Meminimalkan latensi dan biaya. Paling cocok untuk mengikuti petunjuk sederhana, chat, atau aplikasi dengan throughput tinggi. |
| **`medium`** | Didukung | Didukung | Didukung | Pemikiran yang seimbang untuk sebagian besar tugas. |
| **`high`** | Didukung (Default, Dinamis) | Didukung (Dinamis) | Didukung (Default, Dinamis) | Memaksimalkan kedalaman penalaran. Model mungkin memerlukan waktu yang jauh lebih lama untuk mencapai token output pertama (non-pemikiran), tetapi outputnya akan lebih beralasan. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Resolusi media

Gemini 3 memperkenalkan kontrol terperinci atas pemrosesan visi multimodal menggunakan parameter
`media_resolution`. Resolusi yang lebih tinggi meningkatkan kemampuan model untuk membaca teks kecil atau mengidentifikasi detail kecil, tetapi meningkatkan penggunaan token dan latensi.
Parameter `media_resolution` menentukan **jumlah maksimum token
yang dialokasikan per gambar input atau frame video.**

Anda kini dapat menyetel resolusi ke `media_resolution_low`,
`media_resolution_medium`, `media_resolution_high`, atau
`media_resolution_ultra_high` per bagian media individual atau secara global (melalui
`generation_config`, global tidak tersedia untuk ultra tinggi). Jika tidak ditentukan, model akan menggunakan default optimal berdasarkan jenis media.

**Setelan yang direkomendasikan**

| Jenis Media | Setelan yang Direkomendasikan | Token Maksimum | Panduan Penggunaan |
| --- | --- | --- | --- |
| **Gambar** | `media_resolution_high` | 1120 | Direkomendasikan untuk sebagian besar tugas analisis gambar guna memastikan kualitas maksimum. |
| **PDF** | `media_resolution_medium` | 560 | Optimal untuk pemahaman dokumen; kualitas biasanya mencapai titik jenuh pada `medium`. Meningkatkan ke `high` jarang meningkatkan hasil OCR untuk dokumen standar. |
| **Video** (Umum) | `media_resolution_low` (atau `media_resolution_medium`) | 70 (per frame) | **Catatan:** Untuk video, setelan `low` dan `medium` diperlakukan sama (70 token) untuk mengoptimalkan penggunaan konteks. Langkah ini cukup untuk sebagian besar tugas pengenalan dan deskripsi tindakan. |
| **Video** (Banyak teks) | `media_resolution_high` | 280 (per frame) | Diperlukan hanya jika kasus penggunaan melibatkan pembacaan teks padat (OCR) atau detail kecil dalam frame video. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Suhu

Untuk semua model Gemini 3, sebaiknya pertahankan parameter temperatur pada nilai defaultnya, yaitu `1.0`.

Meskipun model sebelumnya sering kali diuntungkan dengan menyesuaikan temperatur untuk mengontrol kreativitas versus determinisme, kemampuan penalaran Gemini 3 dioptimalkan untuk setelan default. Mengubah suhu (menyetelnya di bawah 1.0) dapat menyebabkan perilaku yang tidak terduga, seperti perulangan atau penurunan performa, terutama dalam tugas matematika atau penalaran yang kompleks.

### Tanda tangan penalaran

Gemini 3 menggunakan [Tanda tangan pemikiran](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id) untuk
mempertahankan konteks penalaran di seluruh panggilan API. Tanda tangan ini adalah representasi terenkripsi dari proses pemikiran internal model. Untuk memastikan model
mempertahankan kemampuan penalaran, Anda harus menampilkan kembali tanda tangan ini ke
model dalam permintaan Anda persis seperti yang diterima:

- **Panggilan Fungsi (Ketat):** API menerapkan validasi ketat pada
  "Giliran Saat Ini". Tanda tangan yang tidak ada akan menghasilkan error 400.
- **Teks/Chat:** Validasi tidak ditegakkan secara ketat, tetapi menghilangkan tanda tangan akan menurunkan kualitas penalaran dan jawaban model.
- **Pembuatan/pengeditan gambar (Ketat)**: API menerapkan validasi ketat pada semua bagian Model, termasuk `thoughtSignature`. Tanda tangan yang tidak ada akan menghasilkan error 400.

#### Panggilan fungsi (validasi ketat)

Saat menghasilkan `functionCall`, Gemini mengandalkan `thoughtSignature` untuk
memproses output alat dengan benar pada giliran berikutnya. "Giliran Saat Ini"
mencakup semua langkah Model (`functionCall`) dan Pengguna (`functionResponse`) yang
terjadi sejak pesan `text` **Pengguna** standar terakhir.

- **Panggilan Fungsi Tunggal:** Bagian `functionCall` berisi tanda tangan. Anda harus mengembalikannya.
- **Panggilan Fungsi Paralel:** Hanya bagian `functionCall` pertama dalam daftar yang akan berisi tanda tangan. Anda harus mengembalikan suku cadang dalam urutan yang sama persis seperti saat diterima.
- **Multi-Langkah (Berurutan):** Jika model memanggil alat, menerima hasil, dan memanggil alat *lain* (dalam giliran yang sama), **kedua** panggilan fungsi memiliki tanda tangan. Anda harus menampilkan **semua** tanda tangan yang terkumpul dalam histori.

#### Teks dan streaming

Untuk chat standar atau pembuatan teks, kehadiran tanda tangan tidak dijamin.

- **Non-Streaming**: Bagian konten akhir respons dapat berisi
  `thoughtSignature`, meskipun tidak selalu ada. Jika salah satunya dikembalikan, Anda harus mengirimkannya kembali untuk mempertahankan performa terbaik.
- **Streaming**: Jika tanda tangan dibuat, tanda tangan tersebut dapat tiba dalam potongan akhir yang berisi bagian teks kosong. Pastikan parser aliran Anda memeriksa tanda tangan meskipun kolom teks kosong.

#### Pembuatan dan pengeditan gambar

Untuk `gemini-3-pro-image-preview` dan `gemini-3.1-flash-image-preview`, tanda tangan pemikiran sangat penting untuk pengeditan via percakapan. Saat Anda meminta model untuk memodifikasi gambar, model akan mengandalkan
`thoughtSignature` dari giliran sebelumnya untuk memahami komposisi dan
logika gambar asli.

- **Pengeditan:** Tanda tangan dijamin ada di bagian pertama setelah pemikiran respons (`text` atau `inlineData`) dan di setiap bagian `inlineData` berikutnya. Anda harus menampilkan semua tanda tangan ini untuk menghindari error.

#### Contoh kode

#### Pemanggilan Fungsi Multi-Langkah (Berurutan)

Pengguna mengajukan pertanyaan yang memerlukan dua langkah terpisah (Cek Penerbangan -> Pesan Taksi) dalam satu giliran.   
  
**Langkah 1: Model memanggil Alat Penerbangan.**  
Model menampilkan tanda tangan `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Langkah 2: Pengguna mengirimkan Hasil Penerbangan**  
Kita harus mengirimkan kembali `<Sig_A>` untuk mempertahankan alur pemikiran model.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Langkah 3: Model memanggil Alat Taksi**  
Model mengingat keterlambatan penerbangan melalui `<Sig_A>` dan sekarang memutuskan untuk memesan taksi. Tindakan ini akan menghasilkan tanda tangan *baru* `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Langkah 4: Pengguna mengirimkan Hasil Taksi**  
Untuk menyelesaikan giliran, Anda harus mengirim kembali seluruh rangkaian: `<Sig_A>` DAN `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Panggilan Fungsi Paralel

Pengguna bertanya: "Cek cuaca di Paris dan London." Model menampilkan dua panggilan fungsi dalam satu respons.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Penalaran Dalam Konteks/Teks (Tanpa Validasi)

Pengguna mengajukan pertanyaan yang memerlukan penalaran dalam konteks tanpa alat eksternal. Meskipun tidak divalidasi secara ketat, menyertakan tanda tangan membantu model mempertahankan rantai penalaran untuk pertanyaan lanjutan.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Pembuatan & Pengeditan Gambar

Untuk pembuatan gambar, tanda tangan divalidasi secara ketat. Iklan muncul di **bagian pertama** (teks atau gambar) dan **semua bagian gambar berikutnya**. Semua harus dikembalikan pada giliran berikutnya.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Bermigrasi dari model lain

Jika Anda mentransfer rekaman aktivitas percakapan dari model lain (misalnya, Gemini 2.5) atau menyisipkan panggilan fungsi kustom yang tidak dibuat oleh Gemini 3, Anda tidak akan memiliki tanda tangan yang valid.

Untuk melewati validasi ketat dalam skenario tertentu ini, isi kolom dengan string dummy khusus ini: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Output Terstruktur dengan alat

Model Gemini 3 memungkinkan Anda menggabungkan [Output Terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) dengan alat bawaan, termasuk
[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id), [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id), [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), dan [Pemanggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Pembuatan gambar

Gemini 3.1 Flash Image dan Gemini 3 Pro Image memungkinkan Anda membuat dan mengedit gambar dari perintah teks. Model ini menggunakan penalaran untuk "memikirkan" perintah dan dapat mengambil data real-time—seperti prakiraan cuaca atau diagram saham—sebelum menggunakan perujukan [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) sebelum membuat gambar dengan fidelitas tinggi.

**Kemampuan baru & yang ditingkatkan:**

- **Rendering teks & 4K:** Buat teks dan diagram yang jelas dan mudah dibaca dengan resolusi hingga 2K dan 4K.
- **Pembuatan dengan perujukan:** Gunakan alat `google_search` untuk memverifikasi fakta dan membuat gambar berdasarkan informasi dunia nyata. Grounding dengan Google *Penelusuran Gambar*
  tersedia untuk Gemini 3.1 Flash Image.
- **Pengeditan via percakapan:** Pengeditan gambar multi-turn hanya dengan meminta perubahan (misalnya, "Buat latar belakangnya menjadi matahari terbenam"). Alur kerja ini mengandalkan
  **Tanda Pikiran** untuk mempertahankan konteks visual di antara giliran.

Untuk mengetahui detail lengkap tentang rasio aspek, alur kerja pengeditan, dan opsi konfigurasi, lihat [panduan Pembuatan Gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Contoh Respons**

![Cuaca Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=id)

### Eksekusi Kode dengan gambar

Gemini 3 Flash dapat memperlakukan penglihatan sebagai investigasi aktif, bukan hanya sekilas
statis. Dengan menggabungkan penalaran dengan [eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), model merumuskan rencana, lalu menulis dan
mengeksekusi kode Python untuk memperbesar, memangkas, memberi anotasi, atau memanipulasi gambar
langkah demi langkah untuk mendasarkan jawabannya secara visual.

**Kasus penggunaan:**

- **Zoom dan periksa:** Model secara implisit mendeteksi saat detail terlalu kecil (misalnya, membaca pengukur atau nomor seri dari jarak jauh) dan menulis kode untuk memangkas dan memeriksa ulang area tersebut pada resolusi yang lebih tinggi.
- **Matematika dan pemetaan visual:** Model dapat menjalankan perhitungan multi-langkah menggunakan
  kode (misalnya, menjumlahkan item baris pada tanda terima, atau membuat diagram Matplotlib
  dari data yang diekstrak).
- **Anotasi gambar:** Model dapat menggambar panah, kotak pembatas, atau anotasi lain langsung pada gambar untuk menjawab pertanyaan spasial seperti "Ke mana item ini harus diletakkan?".

Untuk mengaktifkan pemikiran visual, konfigurasi [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) sebagai alat. Model akan otomatis menggunakan
kode untuk memanipulasi gambar jika diperlukan.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Untuk mengetahui detail selengkapnya tentang eksekusi kode dengan gambar, lihat [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id#images).

### Respons fungsi multimodal

[Panggilan fungsi multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#multimodal)
memungkinkan pengguna mendapatkan respons fungsi yang berisi
objek multimodal sehingga meningkatkan pemanfaatan kemampuan panggilan fungsi model. Panggilan fungsi standar hanya mendukung respons fungsi berbasis teks:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Menggabungkan alat bawaan dan panggilan fungsi

Gemini 3 memungkinkan penggunaan alat bawaan (seperti Google Penelusuran, konteks URL, dan [lainnya](https://ai.google.dev/gemini-api/docs/tools?hl=id)) serta alat [pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) kustom dalam panggilan API yang sama, sehingga memungkinkan alur kerja yang lebih kompleks. Pelajari lebih lanjut di halaman [kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Bermigrasi dari Gemini 2.5

Gemini 3 adalah rangkaian model tercanggih kami hingga saat ini dan menawarkan peningkatan bertahap dibandingkan Gemini 2.5. Saat melakukan migrasi, pertimbangkan hal berikut:

- **Penalaran:** Jika sebelumnya Anda menggunakan rekayasa perintah yang rumit (seperti
  rantai pemikiran) untuk memaksa Gemini 2.5 melakukan penalaran, coba Gemini 3 dengan
  `thinking_level: "high"` dan perintah yang disederhanakan.
- **Setelan temperatur:** Jika kode yang ada secara eksplisit menetapkan temperatur (terutama ke nilai rendah untuk output determenistik), sebaiknya hapus parameter ini dan gunakan nilai default Gemini 3 sebesar 1.0 untuk menghindari potensi masalah loop atau penurunan performa pada tugas yang kompleks.
- **Pemahaman PDF & dokumen:**
  Jika Anda mengandalkan perilaku tertentu untuk parsing dokumen padat, uji setelan
  `media_resolution_high` baru untuk memastikan akurasi yang berkelanjutan.
- **Penggunaan token:** Bermigrasi ke setelan default Gemini 3 dapat **meningkatkan** penggunaan token untuk PDF, tetapi **menurunkan** penggunaan token untuk video. Jika permintaan kini melebihi
  jendela konteks karena resolusi default yang lebih tinggi, sebaiknya kurangi resolusi media secara eksplisit.
- **Segmentasi gambar:** Kemampuan segmentasi gambar (menampilkan mask tingkat piksel untuk objek) tidak didukung di Gemini 3 Pro atau Gemini 3 Flash. Untuk beban kerja yang memerlukan segmentasi gambar native, sebaiknya terus gunakan Gemini 2.5 Flash dengan fitur berpikir dinonaktifkan.
- **Penggunaan Komputer:** Gemini 3 Pro dan Gemini 3 Flash mendukung [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id). Tidak seperti seri 2.5, Anda tidak perlu menggunakan model terpisah untuk mengakses alat Penggunaan Komputer.
- **Dukungan alat**: [Menggabungkan alat bawaan dengan pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) kini didukung untuk model Gemini 3. [Perujukan Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) kini juga didukung untuk model Gemini 3.
- **Jumlah kandidat**: Model Gemini 3 tidak mendukung `candidateCount > 1`.
  Menetapkan parameter ini ke nilai yang lebih besar dari `1` akan menampilkan
  error 400.

## Kompatibilitas OpenAI

Untuk pengguna yang memanfaatkan [lapisan kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id),
parameter standar (`reasoning_effort` OpenAI) secara otomatis dipetakan ke
padanan Gemini (`thinking_level`).

## Praktik terbaik pembuatan perintah

Gemini 3 adalah model penalaran, yang mengubah cara Anda memberikan perintah.

- **Petunjuk yang presisi:** Berikan perintah input yang ringkas. Gemini 3 merespons
  paling baik terhadap petunjuk yang langsung dan jelas. Model ini mungkin menganalisis secara berlebihan teknik rekayasa perintah yang panjang atau terlalu kompleks yang digunakan untuk model lama.
- **Panjang output:** Secara default, Gemini 3 tidak terlalu panjang dan lebih suka memberikan jawaban yang langsung dan efisien. Jika kasus penggunaan Anda memerlukan persona yang lebih
  percakapan atau "ramah", Anda harus secara eksplisit mengarahkan model dalam
  perintah (misalnya, "Jelaskan ini sebagai asisten yang ramah dan suka berbicara").
- **Pengelolaan konteks:** Saat bekerja dengan set data besar (misalnya, seluruh buku, codebase, atau video panjang), tempatkan petunjuk atau pertanyaan spesifik Anda di akhir perintah, setelah konteks data. Berikan alasan model berdasarkan data yang diberikan dengan memulai pertanyaan Anda dengan frasa seperti, "Berdasarkan informasi di atas...".

Pelajari lebih lanjut strategi desain perintah dalam [panduan rekayasa perintah](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id).

## FAQ

1. **Apa batas waktu pengetahuan untuk Gemini 3?** Model Gemini 3 memiliki batas pengetahuan hingga Januari 2025. Untuk informasi terbaru, gunakan alat
   [Perujukan Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id).
2. **What are the context window limits?** Model Gemini 3 mendukung jendela konteks input 1 juta token dan output hingga 64 ribu token.
3. **Apakah ada paket gratis untuk Gemini 3?** Gemini 3 Flash
   `gemini-3-flash-preview` dan 3.1 Flash-Lite `gemini-3.1-flash-lite` memiliki
   paket gratis di Gemini API. Anda dapat mencoba Gemini 3.1 Pro dan 3 Flash secara gratis di Google AI Studio, tetapi tidak ada paket gratis yang tersedia untuk `gemini-3.1-pro-preview` di Gemini API.
4. **Apakah kode `thinking_budget` lama saya masih berfungsi?** Ya, `thinking_budget` masih didukung untuk kompatibilitas mundur, tetapi sebaiknya lakukan migrasi ke `thinking_level` untuk performa yang lebih dapat diprediksi. Jangan gunakan keduanya dalam permintaan yang sama.
5. **Apakah Gemini 3 mendukung Batch API?** Ya, Gemini 3 mendukung
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id).
6. **Apakah Context Caching didukung?** Ya, [Penyimpanan Cache Konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id) didukung untuk Gemini 3.
7. **Alat mana yang didukung di Gemini 3?** Gemini 3 mendukung [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id), [Perujukan dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id), [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id),
   [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), dan [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id). Hal ini juga mendukung [Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) standar untuk alat kustom Anda sendiri,
   dan [kombinasi dengan alat bawaan](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).
8. **Apa itu `gemini-3.1-pro-preview-customtools`?** Jika Anda menggunakan `gemini-3.1-pro-preview` dan model mengabaikan alat kustom Anda dan lebih memilih perintah bash, coba gunakan model `gemini-3.1-pro-preview-customtools`. Info selengkapnya [di sini](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id#gemini-31-pro-preview-customtools).

## Langkah berikutnya

- Mulai menggunakan [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=id#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Lihat panduan Cookbook khusus tentang [tingkat penalaran](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=id#gemini3) dan cara bermigrasi dari anggaran penalaran ke tingkat penalaran.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-07 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-07 UTC."],[],[]]
