---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=id
fetched_at: 2026-07-20T04:37:17.954670+00:00
title: "Inferensi prioritas \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Inferensi prioritas

Deskripsi: Pelajari cara mengoptimalkan latensi dengan tingkat inferensi Prioritas

Gemini Priority API adalah tingkat inferensi premium yang dirancang untuk beban kerja penting bisnis yang memerlukan latensi lebih rendah dan keandalan tertinggi dengan harga premium. Traffic tingkat prioritas diprioritaskan di atas traffic API standar dan tingkat Flex.

Inferensi prioritas tersedia untuk [pengguna Tingkat 2 & Tingkat 3](https://ai.google.dev/gemini-api/docs/billing?hl=id#about-billing) di seluruh endpoint GenerateContent API
dan Interactions API.

## Cara menggunakan Prioritas

Untuk menggunakan tingkat Prioritas, tetapkan kolom `service_tier` di isi permintaan ke `priority`. Tingkat default adalah standar jika kolom dihilangkan.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.5-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cara kerja inferensi Prioritas

Inferensi prioritas merutekan permintaan ke antrean komputasi dengan tingkat kekritisan tinggi, yang menawarkan performa cepat dan dapat diprediksi untuk aplikasi yang berinteraksi dengan pengguna. Mekanisme utamanya adalah downgrade sisi server yang lancar ke pemrosesan standar untuk traffic yang melebihi batas dinamis, sehingga memastikan stabilitas aplikasi, bukan membuat permintaan gagal.

| Fitur | Prioritas | Standar | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Harga** | 75-100% lebih mahal dari Standar | Harga penuh | Diskon 50% | Diskon 50% |
| **Latensi** | Detik | Detik hingga menit | Menit (target 1–15 menit) | Hingga 24 jam |
| **Keandalan** | Tinggi (Tidak dapat dihentikan) | Tinggi / Sedang-tinggi | Upaya terbaik (Dapat dihentikan) | Tinggi (untuk throughput) |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron |

### Manfaat utama

- **Latensi rendah**: Dirancang untuk waktu respons kedua untuk alat AI interaktif,
  yang berinteraksi dengan pengguna.
- **Keandalan tinggi**: Traffic diperlakukan dengan tingkat kekritisan tertinggi dan
  tidak dapat dihentikan.
- **Degradasi halus**: Lonjakan traffic yang melebihi batas dinamis secara otomatis di-downgrade ke tingkat Standar untuk diproses, bukan gagal, sehingga mencegah gangguan layanan.
- **Gesekan rendah**: Menggunakan metode sinkron `generateContent` yang sama dengan tingkat
  standar dan Flex.

### Kasus penggunaan

Pemrosesan prioritas ideal untuk alur kerja penting bisnis yang mengutamakan performa dan keandalan.

- **Aplikasi AI interaktif**: Chatbot dan kopilot layanan pelanggan yang
  pengguna membayar premium dan mengharapkan respons yang cepat dan konsisten.
- **Mesin keputusan real-time**: Sistem yang memerlukan hasil yang sangat andal dan berlatensi rendah
  seperti triase tiket langsung atau deteksi penipuan.
- **Fitur pelanggan premium**: Developer yang perlu menjamin tujuan tingkat layanan
  yang lebih tinggi untuk pelanggan berbayar.

### Batas kapasitas

Konsumsi prioritas memiliki batas kapasitasnya sendiri meskipun konsumsi dihitung terhadap [batas kapasitas traffic interaktif secara keseluruhan](https://aistudio.google.com/rate-limit?hl=id). Batas kapasitas default untuk inferensi Prioritas adalah **0,3x batas kapasitas standar untuk Model / Tingkat**

### Logika downgrade lancar

Jika batas Prioritas terlampaui karena kemacetan, permintaan overflow akan **otomatis dan lancar** di-downgrade ke pemrosesan Standar, bukan gagal dengan error 503 atau 429. Permintaan yang di-downgrade ditagih dengan tarif standar, bukan tarif premium Prioritas.

### Tanggung jawab klien

- **Pemantauan respons**: Developer harus memantau `x-gemini-service-tier`
  header dalam respons API untuk mendeteksi apakah permintaan sering di-downgrade ke
  `standard`.
- **Percobaan ulang**: Klien harus menerapkan logika percobaan ulang/backoff eksponensial untuk
  error standar, seperti `DEADLINE_EXCEEDED`.

## Harga

Inferensi prioritas dihargai 75-100% lebih mahal daripada [API standar](https://ai.google.dev/gemini-api/docs/pricing?hl=id) dan ditagih per token.

## Model yang didukung

Model berikut mendukung inferensi Prioritas:

| Model | Inferensi prioritas |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Langkah berikutnya

Baca opsi [inferensi dan pengoptimalan](https://ai.google.dev/gemini-api/docs/optimization?hl=id) Gemini lainnya:

- [Inferensi Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id) untuk pengurangan biaya 50%.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id) untuk pemrosesan asinkron dalam waktu 24 jam.
- [Context caching](https://ai.google.dev/gemini-api/docs/caching?hl=id) untuk mengurangi biaya token input.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-23 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-23 UTC."],[],[]]
