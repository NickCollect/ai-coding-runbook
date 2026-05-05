---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=id
fetched_at: 2026-05-05T19:44:15.407503+00:00
title: "Library Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Library Gemini API

Saat membangun dengan Gemini API, sebaiknya gunakan **Google GenAI SDK**.
Ini adalah library resmi yang siap produksi yang kami kembangkan dan kelola
untuk bahasa yang paling populer. Fitur ini dalam [Ketersediaan Umum](https://ai.google.dev/gemini-api/docs/libraries?hl=id#new-libraries) dan digunakan dalam semua dokumentasi dan contoh resmi kami.

Jika Anda baru menggunakan Gemini API, ikuti [panduan memulai cepat](https://ai.google.dev/gemini-api/docs/quickstart?hl=id) kami untuk memulai.

## Dukungan bahasa dan penginstalan

Google GenAI SDK tersedia untuk bahasa Python, JavaScript/TypeScript, Go, dan Java. Anda dapat menginstal library setiap bahasa menggunakan pengelola paket,
atau mengunjungi repositori GitHub-nya untuk berinteraksi lebih lanjut:

### Python

- Library: [`google-genai`](https://pypi.org/project/google-genai)
- Repositori GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Penginstalan: `pip install google-genai`

### JavaScript

- Library: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Repositori GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Penginstalan: `npm install @google/genai`

### Go

- Library: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Repositori GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Penginstalan: `go get google.golang.org/genai`

### Java

- Library: `google-genai`
- Repositori GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Penginstalan: Jika Anda menggunakan Maven, tambahkan kode berikut ke dependensi Anda:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Library: `Google.GenAI`
- Repositori GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Penginstalan: `dotnet add package Google.GenAI`

## Ketersediaan umum

Mulai Mei 2025, Google GenAI SDK telah mencapai Ketersediaan Umum (GA) di semua platform yang didukung dan merupakan library yang direkomendasikan untuk mengakses Gemini API.
API ini stabil, didukung sepenuhnya untuk penggunaan produksi, dan dikelola secara aktif.
Aplikasi ini memberikan akses ke fitur terbaru, dan menawarkan performa terbaik saat digunakan dengan Gemini.

Jika Anda menggunakan salah satu library lama kami, sebaiknya Anda melakukan migrasi agar dapat mengakses fitur terbaru dan mendapatkan performa terbaik saat menggunakan Gemini. Tinjau bagian [library lama](https://ai.google.dev/gemini-api/docs/libraries?hl=id#previous-sdks) untuk mengetahui informasi selengkapnya.

## Library lama dan migrasi

Jika Anda menggunakan salah satu library lama kami, sebaiknya Anda
[bermigrasi ke library baru](https://ai.google.dev/gemini-api/docs/migrate?hl=id).

Library lama tidak menyediakan akses ke fitur terbaru (seperti
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) dan [Veo](https://ai.google.dev/gemini-api/docs/video?hl=id)) dan
tidak digunakan lagi mulai 30 November 2025.

Status dukungan setiap library lama bervariasi, yang dijelaskan dalam tabel berikut:

| Language | Library lama | Status dukungan | Pustaka yang direkomendasikan |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Tidak dipertahankan secara aktif | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Tidak dipertahankan secara aktif | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Tidak dipertahankan secara aktif | `google.golang.org/genai` |
| **Dart dan Flutter** | `google_generative_ai` | Tidak dipertahankan secara aktif | Gunakan [Genkit Dart](https://genkit.dev/docs/dart/get-started/) atau [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Tidak dipertahankan secara aktif | Menggunakan [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=id) |
| **Android** | `generative-ai-android` | Tidak dipertahankan secara aktif | Menggunakan [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=id) |

**Catatan untuk developer Java:** Tidak ada SDK Java lama yang disediakan Google untuk Gemini API, sehingga tidak diperlukan migrasi dari library Google sebelumnya. Anda
dapat langsung memulai dengan library baru di bagian
[Dukungan bahasa dan penginstalan](#install).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
