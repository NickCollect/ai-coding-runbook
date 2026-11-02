---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=id
fetched_at: 2026-11-02T07:22:47.504012+00:00
title: "Inferensi prioritas \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Inferensi prioritas

Deskripsi: Pelajari cara mengoptimalkan latensi dengan tingkat inferensi Prioritas

Gemini Priority API adalah paket inferensi premium yang dirancang untuk
workload penting bisnis yang memerlukan latensi lebih rendah dan keandalan
tertinggi dengan harga premium. Traffic paket prioritas diprioritaskan di atas traffic API standar dan paket Flex.

Inferensi prioritas tersedia untuk pengguna [Paket 2 & Paket 3](https://ai.google.dev/gemini-api/docs/billing?hl=id#about-billing) di seluruh endpoint GenerateContent API
dan Interactions API.

## Cara menggunakan Prioritas

Untuk menggunakan tingkat Prioritas, tetapkan kolom `service_tier` di isi permintaan ke
`priority`. Paket default adalah standar jika kolom tidak diisi.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
          model: "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cara kerja Inferensi prioritas

Inferensi prioritas merutekan permintaan ke antrean komputasi dengan tingkat kekritisan tinggi, sehingga menawarkan performa yang cepat dan dapat diprediksi untuk aplikasi yang ditampilkan kepada pengguna. Mekanisme utamanya adalah downgrade sisi server yang lancar ke pemrosesan standar untuk traffic yang melebihi batas dinamis, sehingga memastikan stabilitas aplikasi, bukan membuat permintaan gagal.

| Fitur | Prioritas | Standar | Lipat | Batch |
| --- | --- | --- | --- | --- |
| **Harga** | 75-100% lebih banyak daripada Standard | Harga penuh | Diskon 50% | Diskon 50% |
| **Latensi** | Detik | Detik ke menit | Menit (target 1–15 menit) | Hingga 24 jam |
| **Keandalan** | Tinggi (Tidak dapat dilepas) | Tinggi / Sedang-tinggi | Upaya terbaik (Dapat dihentikan) | Tinggi (untuk throughput) |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron |

### Manfaat utama

- **Latensi rendah**: Dirancang untuk waktu respons dalam hitungan detik untuk alat AI interaktif yang ditampilkan kepada pengguna.
- **Keandalan tinggi**: Traffic diperlakukan dengan tingkat kritikalitas tertinggi dan
  sangat tidak dapat dibatalkan.
- **Degradasi halus**: Lonjakan traffic yang melebihi batas dinamis akan otomatis diturunkan ke paket Standard untuk diproses, bukan gagal, sehingga mencegah pemadaman layanan.
- **Friksi rendah**: Menggunakan metode `generateContent` sinkron yang sama dengan
  tingkat standar dan Flex.

### Kasus penggunaan

Pemrosesan prioritas ideal untuk alur kerja yang penting bagi bisnis, yang mengutamakan performa dan keandalan.

- **Aplikasi AI interaktif**: Chatbot dan copilot layanan pelanggan tempat
  pengguna membayar harga premium dan mengharapkan respons yang cepat dan konsisten.
- **Mesin keputusan real-time**: Sistem yang memerlukan hasil yang sangat andal dan berlatensi rendah, seperti triase tiket langsung atau deteksi penipuan.
- **Fitur pelanggan premium**: Developer yang perlu menjamin tujuan tingkat layanan (SLO) yang lebih tinggi untuk pelanggan yang membayar.

### Batas kapasitas

Konsumsi prioritas memiliki batas kapasitasnya sendiri meskipun konsumsi
dihitung terhadap [batas kapasitas traffic interaktif keseluruhan](https://aistudio.google.com/rate-limit?hl=id). Batas frekuensi default
untuk Inferensi prioritas adalah **batas frekuensi standar 0,3x untuk Model / Tingkatan**

### Logika downgrade yang lancar

Jika batas Prioritas terlampaui karena kemacetan, permintaan tambahan akan
**otomatis dan lancar** diturunkan ke pemrosesan Standar, bukan
gagal dengan error 503 atau 429. Permintaan yang di-downgrade ditagih dengan tarif standar, bukan tarif premium Prioritas.

### Tanggung jawab klien

- **Pemantauan respons**: Developer harus memantau header `x-gemini-service-tier`
  dalam respons API untuk mendeteksi apakah permintaan sering didowngrade ke
  `standard`.
- **Percobaan ulang**: Klien harus menerapkan logika percobaan ulang/backoff eksponensial untuk
  error standar, seperti `DEADLINE_EXCEEDED`.

## Harga

Inferensi prioritas dikenai harga 75-100% lebih tinggi daripada [API standar](https://ai.google.dev/gemini-api/docs/pricing?hl=id) dan ditagih per token.

## Model yang didukung

Model berikut mendukung Inferensi prioritas:

| Model | Inferensi prioritas |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=id) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=id) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Image Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Langkah berikutnya

Baca opsi [inferensi dan pengoptimalan](https://ai.google.dev/gemini-api/docs/optimization?hl=id) Gemini lainnya:

- [Inferensi Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id) untuk pengurangan biaya sebesar 50%.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id) untuk pemrosesan asinkron dalam waktu 24 jam.
- [Caching konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id) untuk mengurangi biaya token input.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-13 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-13 UTC."],[],[]]
