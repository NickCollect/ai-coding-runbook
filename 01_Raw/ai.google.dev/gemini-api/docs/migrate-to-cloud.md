---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=id
fetched_at: 2026-09-28T06:35:21.614503+00:00
title: "Gemini Developer API vs. Platform Agen Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Gemini Developer API vs. Platform Agen Gemini Enterprise

Saat mengembangkan solusi AI generatif dengan Gemini, Google menawarkan dua produk API:
yang [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=id) dan [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=id).

Gemini Developer API menyediakan jalur tercepat untuk membangun, memproduksi, dan menskalakan aplikasi yang didukung Gemini. Sebagian besar developer harus menggunakan Gemini Developer API kecuali jika ada kebutuhan untuk kontrol perusahaan tertentu.

Gemini Enterprise Agent Platform menawarkan ekosistem komprehensif berisi fitur dan layanan siap pakai untuk perusahaan guna membangun dan men-deploy aplikasi AI generatif yang didukung oleh Google Cloud Platform.

Baru-baru ini kami menyederhanakan migrasi antar-layanan ini. Gemini
Developer API dan Gemini Enterprise Agent Platform API kini dapat diakses melalui
[Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=id) terpadu.

## Perbandingan kode

Halaman ini berisi perbandingan kode berdampingan antara Gemini Developer API dan Gemini Enterprise Agent Platform quickstart untuk pembuatan teks.

### Python

Anda dapat mengakses layanan Gemini Developer API dan Gemini Enterprise Agent Platform melalui library `google-genai`. Lihat halaman [library](https://ai.google.dev/gemini-api/docs/libraries?hl=id)
untuk mengetahui petunjuk cara menginstal `google-genai`.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript dan TypeScript

Anda dapat mengakses layanan Gemini Developer API dan Gemini Enterprise Agent Platform melalui library `@google/genai`. Lihat halaman [library](https://ai.google.dev/gemini-api/docs/libraries?hl=id) untuk mengetahui petunjuk cara
menginstal `@google/genai`.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Anda dapat mengakses layanan Gemini Developer API dan Gemini Enterprise Agent Platform melalui library `google.golang.org/genai`. Lihat halaman [library](https://ai.google.dev/gemini-api/docs/libraries?hl=id) untuk mengetahui petunjuk cara
menginstal `google.golang.org/genai`.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Platform dan kasus penggunaan lainnya

Lihat panduan khusus kasus penggunaan di [Dokumentasi Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=id)
dan [dokumentasi Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=id)
untuk platform dan kasus penggunaan lainnya.

## Pertimbangan migrasi

Saat Anda bermigrasi:

- Anda harus menggunakan akun layanan Google Cloud untuk melakukan autentikasi. Lihat [dokumentasi Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=id)
  untuk mengetahui informasi selengkapnya.
- Anda dapat menggunakan project Google Cloud yang ada
  (project yang sama yang Anda gunakan untuk membuat kunci API) atau Anda dapat
  [membuat project Google Cloud baru](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=id).
- Region yang didukung mungkin berbeda antara Gemini Developer API dan Gemini Enterprise Agent Platform API. Lihat daftar
  [region yang didukung untuk AI generatif di Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=id).
- Model apa pun yang Anda buat di Google AI Studio harus dilatih ulang di Gemini Enterprise Agent Platform.

Jika Anda tidak perlu lagi menggunakan kunci Gemini API untuk Gemini Developer API, ikuti praktik terbaik keamanan dan hapus kunci tersebut.

Cara menghapus kunci API:

1. Buka halaman
   [Kredensial API Google Cloud](https://console.cloud.google.com/apis/credentials?hl=id).
2. Temukan kunci API yang ingin Anda hapus, lalu klik ikon **Tindakan**.
3. Pilih **Hapus kunci API**.
4. Di modal **Hapus kredensial**, pilih **Hapus**.

   Penghapusan kunci API memerlukan waktu beberapa menit untuk diterapkan. Setelah
   propagasi selesai, traffic yang menggunakan kunci API yang dihapus akan ditolak.

## Langkah berikutnya

- Lihat
  [ringkasan AI Generatif di Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=id)
  untuk mempelajari lebih lanjut solusi AI generatif di Gemini Enterprise Agent Platform.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-12 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-12 UTC."],[],[]]
