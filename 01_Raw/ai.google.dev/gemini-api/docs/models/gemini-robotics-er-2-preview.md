---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-preview?hl=id
fetched_at: 2026-08-03T04:34:43.416360+00:00
title: "Pratinjau Gemini Robotics ER 2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pratinjau Gemini Robotics ER 2

Gemini Robotics ER 2 adalah model bahasa-penglihatan (VLM) untuk robotik yang menerima input teks, gambar, video, dan audio. Gemini 1.5 Pro mendukung penalaran spasial, pemahaman video, eksekusi kode agentic, orkestrasi alat multi-langkah, dan koordinasi multi-robot.

[Coba di Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=id)

## Dokumentasi

Buka halaman [Robotika](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id) untuk mengetahui cakupan lengkap fitur dan kemampuan.

## gemini-robotics-er-2-preview

### Pratinjau Gemini Robotics ER 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-2-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Tidak didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-2-preview` |
| calendar\_monthPembaruan terbaru | Juli 2026 |
| Kartu model id\_card | [Kartu model](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=id) |

### Pratinjau Streaming Gemini Robotics ER 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Tidak didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Tidak didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Tidak didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Tidak didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Tidak didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Tidak didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Tidak didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Tidak didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthPembaruan terbaru | Juli 2026 |
| Kartu model id\_card | [Kartu model](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=id) |

### Pratinjau Gemini Robotics ER 1.6

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-1.6-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Tidak didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-1.6-preview` |
| calendar\_monthPembaruan terbaru | Desember 2025 |
| cognition\_2Batas informasi | Januari 2025 |

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
