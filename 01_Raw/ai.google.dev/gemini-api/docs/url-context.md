---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=id
fetched_at: 2026-05-18T05:09:48.568681+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Konteks URL

[Alat konteks URL memungkinkan Anda memberikan konteks tambahan ke model dalam bentuk URL. Dengan menyertakan URL dalam permintaan Anda, model akan mengakses konten dari halaman tersebut (selama tidak termasuk jenis URL yang tercantum di bagian batasan) untuk menginformasikan dan meningkatkan kualitas responsnya.](#limitations)

Alat konteks URL berguna untuk tugas seperti berikut:

- **Mengekstrak Data**: Menarik informasi tertentu seperti harga, nama, atau temuan utama dari beberapa URL.
- **Membandingkan Dokumen**: Menganalisis beberapa laporan, artikel, atau PDF untuk
  mengidentifikasi perbedaan dan melacak tren.
- **Menyintesis & Membuat Konten**: Menggabungkan informasi dari beberapa URL sumber untuk membuat ringkasan, postingan blog, atau laporan yang akurat.
- **Analisis Kode & Dokumen**: Merujuk repositori GitHub atau dokumentasi teknis untuk menjelaskan kode, membuat petunjuk penyiapan, atau menjawab pertanyaan.

Contoh berikut menunjukkan cara membandingkan dua resep dari situs yang berbeda.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Cara kerjanya

Alat Konteks URL menggunakan proses pengambilan dua langkah untuk menyeimbangkan kecepatan, biaya, dan akses ke data baru. Saat Anda memberikan URL, alat ini
pertama-tama akan mencoba mengambil konten dari cache indeks internal. Cache ini berfungsi sebagai cache yang sangat dioptimalkan. Jika URL tidak tersedia di indeks (misalnya, jika
URL tersebut adalah halaman yang sangat baru), alat otomatis akan melakukan pengambilan langsung.
Alat ini mengakses URL secara langsung untuk mengambil kontennya secara real time.

## Menggabungkan dengan alat lain

Anda dapat menggabungkan alat konteks URL dengan alat lain untuk membuat alur kerja yang lebih canggih.

[Model Gemini 3](#supported-models) mendukung penggabungan alat bawaan
(seperti Konteks URL) dengan alat kustom (pemanggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

### Grounding dengan penelusuran

Jika konteks URL dan
[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id) diaktifkan,
model dapat menggunakan kemampuan penelusurannya untuk menemukan
informasi yang relevan secara online, lalu menggunakan alat konteks URL untuk mendapatkan pemahaman yang lebih
mendalam tentang halaman yang ditemukannya. Pendekatan ini sangat berguna untuk perintah yang memerlukan penelusuran luas dan analisis mendalam halaman tertentu.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Memahami respons

Saat model menggunakan alat konteks URL, respons akan menyertakan objek `url_context_metadata`. Objek ini mencantumkan URL tempat model mengambil konten dan status setiap upaya pengambilan, yang berguna untuk verifikasi dan proses debug.

Berikut adalah contoh bagian respons tersebut (bagian respons telah dihilangkan untuk mempersingkat):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Untuk mengetahui detail lengkap tentang objek ini , lihat referensi API
[`UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=id#UrlContextMetadata).

### Pemeriksaan keamanan

Sistem melakukan pemeriksaan moderasi konten pada URL untuk mengonfirmasi bahwa URL tersebut memenuhi standar keamanan. Jika URL yang Anda berikan gagal dalam pemeriksaan ini, Anda akan mendapatkan `url_retrieval_status` dengan nilai `URL_RETRIEVAL_STATUS_UNSAFE`.

### Jumlah token

Konten yang diambil dari URL yang Anda tentukan dalam perintah Anda dihitung sebagai bagian dari token input. Anda dapat melihat jumlah token untuk penggunaan perintah dan
alat di objek [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=id#UsageMetadata)
dari output model. Berikut adalah contoh output:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Harga per token bergantung pada model yang digunakan. Lihat halaman
[harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detailnya.

## Model yang didukung

| Model | Konteks URL |
| --- | --- |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Praktik Terbaik

- **Berikan URL spesifik**: Untuk mendapatkan hasil terbaik, berikan URL langsung ke
  konten yang Anda ingin untuk dianalisis oleh model. Model hanya akan mengambil konten
  dari URL yang Anda berikan, bukan konten dari link bertingkat.
- **Periksa aksesibilitas**: Pastikan URL yang Anda berikan tidak mengarah ke
  halaman yang memerlukan login atau berada di balik paywall.
- **Gunakan URL lengkap**: Berikan URL lengkap, termasuk protokol
  (misalnya, https://www.google.com, bukan hanya google.com).

## Batasan

- Pemanggilan fungsi: Penggunaan alat (Konteks URL, Grounding dengan Google Penelusuran, dll.) dengan pemanggilan fungsi saat ini tidak didukung.
- Batas permintaan: Alat ini dapat memproses hingga 20 URL per permintaan.
- Ukuran konten URL: Ukuran maksimum untuk konten yang diambil dari satu URL adalah 34 MB.
- Aksesibilitas publik: URL harus dapat diakses secara publik di web.
  Alamat localhost (misalnya, localhost, 127.0.0.1), jaringan pribadi, dan layanan tunneling (misalnya, ngrok, pinggy) tidak didukung.
- Hanya Gemini API: Konteks URL hanya tersedia di Gemini API, bukan melalui Gemini Enterprise Agent Platform.

### Jenis konten yang didukung dan tidak didukung

Alat ini dapat mengekstrak konten dari URL dengan jenis konten berikut:

- Teks (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Gambar (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Jenis konten berikut **tidak** didukung:

- Konten berbayar berpenghalang
- Video YouTube (Lihat
  [pemahaman video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id#youtube) untuk mempelajari
  cara memproses URL YouTube)
- File Google Workspace seperti dokumen atau spreadsheet Google
- File video dan audio

## Langkah berikutnya

- Pelajari [cookbook konteks URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=id#url-context)
  untuk contoh lainnya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-13 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-13 UTC."],[],[]]
