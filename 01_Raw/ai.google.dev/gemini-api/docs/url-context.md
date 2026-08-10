---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=id
fetched_at: 2026-08-10T03:12:24.233211+00:00
title: "Konteks URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Konteks URL

Alat konteks URL memungkinkan Anda memberikan konteks tambahan ke model dalam bentuk URL. Dengan menyertakan URL dalam permintaan Anda, model akan mengakses konten dari halaman tersebut (selama tidak termasuk jenis URL yang tercantum di [bagian batasan](#limitations)) untuk menginformasikan dan meningkatkan kualitas responsnya.

Alat konteks URL berguna untuk tugas seperti berikut:

- **Mengekstrak Data**: Menarik informasi tertentu seperti harga, nama, atau temuan utama dari beberapa URL.
- **Membandingkan Dokumen**: Menganalisis beberapa laporan, artikel, atau PDF untuk
  mengidentifikasi perbedaan dan melacak tren.
- **Menyintesis & Membuat Konten**: Menggabungkan informasi dari beberapa URL sumber untuk membuat ringkasan, postingan blog, atau laporan yang akurat.
- **Analisis Kode & Dokumen**: Merujuk repositori GitHub atau dokumentasi teknis untuk menjelaskan kode, membuat petunjuk penyiapan, atau menjawab pertanyaan.

Contoh berikut menunjukkan cara membandingkan dua resep dari situs yang berbeda.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Cara kerjanya

Alat Konteks URL menggunakan proses pengambilan dua langkah untuk menyeimbangkan kecepatan, biaya, dan akses ke data baru. Saat Anda memberikan URL, alat ini
pertama-tama akan mencoba mengambil konten dari cache indeks internal. Cache ini berfungsi sebagai cache yang sangat dioptimalkan. Jika URL tidak tersedia di indeks (misalnya, jika
URL tersebut adalah halaman yang sangat baru), alat otomatis akan melakukan pengambilan langsung.
Alat ini mengakses URL secara langsung untuk mengambil kontennya secara real time.

## Menggabungkan dengan alat lain

Anda dapat menggabungkan alat konteks URL dengan alat lain untuk membuat alur kerja yang lebih canggih.

[Model Gemini 3](#supported-models) mendukung penggabungan alat bawaan
(seperti Konteks URL) dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

### Grounding dengan penelusuran

Jika konteks URL dan
[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id) diaktifkan,
model dapat menggunakan kemampuan penelusurannya untuk menemukan
informasi yang relevan secara online, lalu menggunakan alat konteks URL untuk mendapatkan pemahaman yang lebih
mendalam tentang halaman yang ditemukannya. Pendekatan ini sangat efektif untuk perintah yang memerlukan penelusuran luas dan analisis mendalam halaman tertentu.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Memahami respons

Saat model menggunakan alat konteks URL, respons teksnya akan menyertakan anotasi `url_citation` inline pada blok konten teks. Setiap anotasi menautkan segmen teks respons (melalui `start_index` dan `end_index`) ke URL sumber yang digunakan untuk membuat teks tersebut. Ini adalah cara utama untuk menampilkan kutipan di aplikasi
Anda. Lihat [contoh utama di atas](#get-started) untuk mengetahui cara mengekstraknya.

Respons tersebut juga mencakup langkah `url_context_result` dengan metadata tentang setiap upaya pengambilan URL (status, URL yang diambil). Hal ini terutama berguna untuk proses debug.

### Pemeriksaan keamanan

Sistem melakukan pemeriksaan moderasi konten pada URL untuk mengonfirmasi bahwa URL tersebut memenuhi standar keamanan. Jika URL gagal dalam pemeriksaan ini, langkah yang sesuai
`url_context_result` akan menampilkan `status` `"unsafe"`.

### Jumlah token

Konten yang diambil dari URL yang Anda tentukan dalam perintah akan dihitung sebagai bagian dari token input. Anda dapat melihat jumlah token di objek `usage` interaksi. Berikut adalah contohnya:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Harga per token bergantung pada model yang digunakan. Lihat halaman
[harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detailnya.

## Model yang didukung

| Model | Konteks URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
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

- Batas permintaan: Alat ini dapat memproses hingga 20 URL per permintaan.
- Ukuran konten URL: Ukuran maksimum untuk konten yang diambil dari satu URL adalah 34 MB.
- Aksesibilitas publik: URL harus dapat diakses secara publik di web.
  Alamat localhost (misalnya, localhost, 127.0.0.1), jaringan pribadi, dan layanan tunneling (misalnya, ngrok, pinggy) tidak didukung.

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

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-31 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-31 UTC."],[],[]]
