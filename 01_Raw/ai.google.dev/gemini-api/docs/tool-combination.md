---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=id
fetched_at: 2026-08-10T03:12:00.711161+00:00
title: "Menggabungkan alat bawaan dan panggilan fungsi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggabungkan alat bawaan dan panggilan fungsi

Gemini memungkinkan kombinasi [alat bawaan](https://ai.google.dev/gemini-api/docs/tools?hl=id), seperti `google_search`, dan [panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) (juga dikenal sebagai *alat kustom*) dalam satu interaksi dengan mempertahankan dan mengekspos histori konteks panggilan alat. Kombinasi alat bawaan dan kustom memungkinkan alur kerja yang kompleks dan seperti agen, misalnya, model dapat mendasarkan dirinya pada data web real-time sebelum memanggil logika bisnis spesifik Anda.

Berikut adalah contoh yang memungkinkan kombinasi alat bawaan dan kustom dengan
`google_search` dan fungsi kustom `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.6-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Cara kerjanya

Model Gemini 3 menggunakan *sirkulasi konteks alat* untuk mengaktifkan kombinasi alat bawaan dan kustom. Sirkulasi konteks alat memungkinkan untuk mempertahankan dan
mengekspos konteks alat bawaan serta membagikannya dengan alat kustom dalam interaksi yang sama.

### Mengaktifkan kombinasi alat

- Sertakan [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#function-declarations), beserta alat bawaan yang ingin Anda gunakan, untuk memicu perilaku kombinasi.

### Langkah-langkah pengembalian API

Dalam respons interaksi, API menampilkan langkah-langkah terpisah untuk panggilan alat bawaan dan panggilan fungsi (alat kustom):

- **Langkah-langkah alat bawaan**: API mengelola langkah-langkah ini secara otomatis, dengan mempertahankan konteks di seluruh giliran.
- **Langkah-langkah panggilan fungsi**: API menampilkan `function_call` langkah untuk fungsi kustom Anda. Anda menjalankan fungsi dan memberikan hasilnya kembali.

### Kolom penting dalam langkah yang ditampilkan

Kolom tertentu dalam langkah yang ditampilkan sangat penting untuk mempertahankan konteks alat dan memungkinkan kombinasi alat:

- **`id`**: Ditemukan pada langkah `function_call` dan `function_response`. ID unik yang memetakan panggilan ke responsnya.
- **`signature`**: Ditemukan di langkah `thought`, serta semua langkah panggilan alat (misalnya, `function_call`) dan hasil (misalnya, `function_response`) untuk model Gemini 3+. Konteks terenkripsi ini memungkinkan **sirkulasi konteks alat** di seluruh interaksi.

**Mengelola kolom ini:**

- **Mode Stateful (Direkomendasikan)**: Saat Anda menggunakan `previous_interaction_id`, server akan otomatis menangani kolom `id` dan `signature`.
- **Mode Tanpa Status**: Saat mengelola histori percakapan secara manual, Anda harus memastikan bahwa Anda meneruskan kembali kolom `id` dan `signature` ke model dalam permintaan berikutnya untuk memvalidasi keaslian dan mempertahankan konteks. SDK resmi menanganinya secara otomatis jika Anda meneruskan kembali objek respons lengkap ke histori.

### Data khusus alat

Beberapa alat bawaan menampilkan argumen data yang terlihat oleh pengguna dan khusus untuk jenis alat.

| Alat | Argumen pemanggilan alat yang terlihat oleh pengguna (jika ada) | Respons alat yang dapat dilihat pengguna (jika ada) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL yang akan dijelajahi | `status`: Status penjelajahan `retrieved_url`: URL yang dijelajahi |
| **file\_search** | Tidak ada | Tidak ada |

## Token dan harga

Perhatikan bahwa bagian panggilan alat bawaan dalam permintaan dihitung dalam
`prompt_token_count`. Karena langkah-langkah alat perantara ini kini terlihat dan dikembalikan kepada Anda, langkah-langkah tersebut menjadi bagian dari histori percakapan. Hal ini hanya berlaku untuk *permintaan*, bukan *respons*.

Alat Google Penelusuran dikecualikan dari aturan ini. Google Penelusuran sudah menerapkan model harganya sendiri di tingkat kueri, sehingga token tidak ditagih dua kali (lihat halaman [Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id)).

Baca halaman [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=id) untuk mengetahui informasi selengkapnya.

## Batasan

- Secara default menggunakan mode `validated` (mode `auto` tidak didukung) jika sirkulasi konteks alat diaktifkan.
- Alat bawaan seperti `google_search` mengandalkan informasi lokasi dan waktu saat ini, jadi jika `system_instruction` atau `function_declaration.description` Anda memiliki informasi lokasi dan waktu yang bertentangan, fitur kombinasi alat mungkin tidak berfungsi dengan baik.

## Alat yang didukung

Sirkulasi konteks alat standar berlaku untuk alat sisi server (bawaan).
Eksekusi Kode juga merupakan alat sisi server, tetapi memiliki solusi bawaan sendiri untuk
sirkulasi konteks. Penggunaan Komputer dan panggilan fungsi adalah alat sisi klien,
dan juga memiliki solusi bawaan untuk sirkulasi konteks.

| Alat | Sisi eksekusi | Dukungan Sirkulasi Konteks |
| --- | --- | --- |
| [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) | Sisi server | Didukung |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) | Sisi server | Didukung |
| [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) | Sisi server | Didukung |
| [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id) | Sisi server | Didukung |
| [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) | Sisi server | Didukung (bawaan, menggunakan langkah-langkah `code_execution` dan `code_execution_result`) |
| [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id) | Sisi klien | Didukung (bawaan, menggunakan langkah-langkah `function_call` dan `function_response`) |
| [Fungsi kustom](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) | Sisi klien | Didukung (bawaan, menggunakan langkah-langkah `function_call` dan `function_response`) |

## Langkah berikutnya

- Pelajari lebih lanjut [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) di Gemini API.
- Jelajahi alat yang didukung:
  - [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)
  - [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)
  - [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
