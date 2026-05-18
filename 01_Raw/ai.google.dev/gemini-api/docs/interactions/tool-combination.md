---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=id
fetched_at: 2026-05-18T05:16:28.432566+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggabungkan alat bawaan dan panggilan fungsi

Gemini memungkinkan kombinasi [alat bawaan](https://ai.google.dev/gemini-api/docs/tools?hl=id), seperti
`google_search`, dan [panggilan fungsi](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id)
(juga dikenal sebagai *alat kustom*) dalam satu interaksi dengan mempertahankan dan mengekspos
histori konteks panggilan alat. Kombinasi alat bawaan dan kustom memungkinkan alur kerja agentik yang kompleks, yang modelnya dapat mendasarkan diri pada data web real-time sebelum memanggil logika bisnis spesifik Anda.

Berikut adalah contoh yang mengaktifkan kombinasi alat bawaan dan kustom dengan `google_search` dan fungsi kustom `getWeather`:

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
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3-flash-preview",
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

Model Gemini 3 menggunakan *sirkulasi konteks alat* untuk mengaktifkan kombinasi alat bawaan dan kustom. Sirkulasi konteks alat memungkinkan konteks alat bawaan dipertahankan dan diekspos, serta dibagikan dengan alat kustom dalam interaksi yang sama.

### Mengaktifkan kombinasi alat

- Sertakan [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id#function-declarations), beserta
  alat bawaan yang ingin Anda gunakan, untuk memicu perilaku kombinasi.

### Langkah-langkah yang ditampilkan API

Dalam respons interaksi, API menampilkan langkah-langkah terpisah untuk panggilan alat bawaan dan panggilan fungsi (alat kustom):

- **Langkah-langkah alat bawaan**: API mengelola langkah-langkah ini secara otomatis, dengan mempertahankan
  konteks di seluruh giliran.
- **Langkah-langkah panggilan fungsi**: API menampilkan langkah-langkah `function_call` untuk fungsi kustom Anda. Anda menjalankan fungsi dan memberikan hasilnya kembali.

### Kolom penting dalam langkah-langkah yang ditampilkan

Kolom tertentu dalam langkah-langkah yang ditampilkan sangat penting untuk mempertahankan konteks alat dan mengaktifkan kombinasi alat:

- **`id`**: Ditemukan di langkah-langkah `function_call` dan `function_response`. ID unik yang memetakan panggilan ke responsnya.
- **`signature`**: Ditemukan di langkah-langkah `thought`, serta semua langkah panggilan alat (misalnya, `function_call`) dan hasil (misalnya, `function_response`) untuk model Gemini 3+. Konteks terenkripsi ini memungkinkan **sirkulasi konteks alat** di seluruh interaksi.

**Mengelola kolom ini:**

- **Mode Stateful (Direkomendasikan)**: Saat Anda menggunakan `previous_interaction_id`, server akan otomatis menangani kolom `id` dan `signature`.
- **Mode Stateless**: Saat mengelola histori percakapan secara manual, Anda harus memastikan bahwa Anda meneruskan kolom `id` dan `signature` kembali ke model dalam permintaan berikutnya untuk memvalidasi keaslian dan mempertahankan konteks. SDK resmi menangani hal ini secara otomatis jika Anda meneruskan objek respons lengkap kembali ke histori.

### Data khusus alat

Beberapa alat bawaan menampilkan argumen data yang terlihat oleh pengguna dan khusus untuk jenis alat.

| Alat | Argumen panggilan alat yang terlihat oleh pengguna (jika ada) | Respons alat yang terlihat oleh pengguna (jika ada) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL yang akan dijelajahi | `status`: Status penjelajahan `retrieved_url`: URL yang dijelajahi |
| **file\_search** | Tidak ada | Tidak ada |

## Token dan harga

Perhatikan bahwa bagian panggilan alat bawaan dalam permintaan dihitung ke dalam `prompt_token_count`. Karena langkah-langkah alat perantara ini kini terlihat dan ditampilkan kepada Anda, langkah-langkah tersebut merupakan bagian dari histori percakapan. Hal ini hanya berlaku untuk
kasus untuk *permintaan*, bukan *respons*.

Alat Google Penelusuran adalah pengecualian untuk aturan ini. Google Penelusuran sudah
menerapkan model harganya sendiri di tingkat kueri, sehingga token tidak
dikenai biaya dua kali (lihat halaman [Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id)).

Baca halaman [Token](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=id) untuk mengetahui informasi selengkapnya.

## Batasan

- Secara default, gunakan mode `validated` (mode `auto` tidak didukung) saat sirkulasi konteks alat diaktifkan.
- Alat bawaan seperti `google_search` mengandalkan informasi lokasi dan waktu saat ini. Jadi, jika `system_instruction` atau `function_declaration.description` Anda memiliki informasi lokasi dan waktu yang bertentangan, fitur kombinasi alat mungkin tidak berfungsi dengan baik.

## Alat yang didukung

Sirkulasi konteks alat standar berlaku untuk alat sisi server (bawaan).
Eksekusi Kode juga merupakan alat sisi server, tetapi memiliki solusi bawaannya sendiri untuk sirkulasi konteks. Penggunaan Komputer dan panggilan fungsi adalah alat sisi klien, dan juga memiliki solusi bawaan untuk sirkulasi konteks.

| Alat | Sisi eksekusi | Dukungan Sirkulasi Konteks |
| --- | --- | --- |
| [Google Penelusuran](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=id) | Sisi server | Didukung |
| [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=id) | Sisi server | Didukung |
| [Konteks URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=id) | Sisi server | Didukung |
| [Penelusuran File](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=id) | Sisi server | Didukung |
| [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=id) | Sisi server | Didukung (bawaan, menggunakan langkah-langkah `code_execution` dan `code_execution_result`) |
| [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=id) | Sisi klien | Didukung (bawaan, menggunakan langkah-langkah `function_call` dan `function_response`) |
| [Fungsi kustom](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id) | Sisi klien | Didukung (bawaan, menggunakan langkah-langkah `function_call` dan `function_response`) |

## Langkah berikutnya

- Pelajari lebih lanjut [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id) di Gemini API.
- Pelajari alat yang didukung:
  - [Google Penelusuran](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=id)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=id)
  - [Konteks URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=id)
  - [Penelusuran File](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-16 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-16 UTC."],[],[]]
