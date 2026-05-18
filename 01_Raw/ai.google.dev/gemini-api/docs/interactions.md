---
source_url: https://ai.google.dev/gemini-api/docs/interactions?hl=id
fetched_at: 2026-05-18T05:14:00.226299+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Interactions API

Interactions API adalah primitif standar baru untuk membangun dengan Gemini, yang direkomendasikan untuk semua project baru. Framework ini dioptimalkan untuk alur kerja agentik, pengelolaan status sisi server, dan percakapan multi-modal dan multi-giliran yang kompleks. API [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id) asli tetap didukung sepenuhnya.

## Mengapa menggunakan Interactions API?

- **Pengelolaan histori sisi server**: Alur multi-turn yang disederhanakan melalui `previous_interaction_id`. Server mengaktifkan status secara default (`store=true`), tetapi Anda dapat memilih perilaku tanpa status dengan menyetel `store=false`.
- **Langkah-langkah eksekusi yang dapat diamati**: Langkah-langkah yang diketik memudahkan proses debug alur yang kompleks dan merender UI untuk peristiwa perantara (seperti pemikiran atau widget penelusuran).
- **Dibuat untuk alur kerja agentic**: Dukungan native untuk penggunaan alat multilangkah, orkestrasi, dan alur penalaran kompleks melalui langkah-langkah eksekusi yang diketik.
- **Tugas latar belakang dan berjalan lama**: Mendukung operasi yang memakan waktu seperti [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=id) dan [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=id) ke proses latar belakang menggunakan `background=true`.
- **Akses ke model dan kemampuan baru**: Ke depannya, model baru di luar keluarga mainline inti, beserta kemampuan dan alat agentic baru, akan diluncurkan secara eksklusif di Interactions API.

**Gunakan Interactions API** jika Anda memulai project baru, membangun aplikasi berbasis agen, atau memerlukan pengelolaan percakapan sisi server. **Gunakan [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id)** jika Anda memiliki integrasi yang ada dan berfungsi untuk kebutuhan Anda, atau jika Anda memerlukan fitur yang [belum tersedia](#limitations) di Interactions API, seperti Batch API atau caching eksplisit.

## Mulai

- **Siapkan agen coding Anda**: Hubungkan ke **MCP Gemini Docs** dan instal
  keterampilan `gemini-interactions-api` untuk memberi asisten Anda akses langsung ke
  praktik terbaik dan dokumentasi developer terbaru.
  [Menyiapkan agen coding Anda →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)
- **Bermigrasi dari `generateContent`**: Jika Anda memiliki integrasi yang sudah ada, ikuti [Panduan Migrasi](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=id) untuk beralih ke Interactions API.
- **Coba panduan memulai**: Mulai dengan contoh kerja minimal di
  [Panduan memulai Interactions API](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=id).

### Panduan Fitur

Pelajari kemampuan spesifik Interactions API melalui panduan ini. Anda dapat menggunakan tombol di halaman ini untuk beralih antara generateContent dan Interactions API:

- [Pembuatan teks](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id)
- [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=id)
- [Pemahaman gambar](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=id)
- [Pemahaman audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=id)
- [Pemahaman video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=id)
- [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=id)
- [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id)
- [Output terstruktur](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=id)
- [Agen Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=id)
- [Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=id)
- [Inferensi prioritas](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=id)
- [Streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=id)

## Cara kerja Interactions API

Interactions API berpusat pada resource inti: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=id#Resource:Interaction). `Interaction` mewakili giliran yang selesai dalam percakapan atau tugas. Tindakan ini berfungsi sebagai catatan sesi, yang berisi seluruh histori interaksi sebagai urutan **langkah-langkah eksekusi** secara kronologis. Langkah-langkah ini mencakup pemikiran model, panggilan dan hasil alat sisi server atau sisi klien (seperti `function_call` dan `function_result`), serta `model_output` akhir. Resource yang disimpan (diambil melalui `interactions.get`) juga mencakup langkah-langkah `user_input` untuk konteks lengkap, meskipun respons `interactions.create` hanya menampilkan langkah-langkah yang dibuat model.

Saat melakukan panggilan ke
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=id#CreateInteraction), Anda
membuat resource `Interaction` baru.

### Pengelolaan status sisi server

Anda dapat menggunakan `id` interaksi yang telah selesai dalam panggilan berikutnya menggunakan parameter
`previous_interaction_id` untuk melanjutkan percakapan. Server menggunakan ID ini untuk mengambil histori percakapan, sehingga Anda tidak perlu mengirim ulang seluruh histori chat.

Parameter `previous_interaction_id` hanya mempertahankan histori percakapan (input dan output)
menggunakan `previous_interaction_id`. Parameter lainnya adalah **cakupan interaksi**
dan hanya berlaku untuk interaksi tertentu yang saat ini Anda buat:

- `tools`
- `system_instruction`
- `generation_config` (termasuk `thinking_level`, `temperature`, dll.)

Artinya, Anda harus menentukan ulang parameter ini di setiap interaksi baru jika ingin menerapkannya. Pengelolaan status sisi server ini bersifat opsional; Anda juga dapat
beroperasi dalam mode tanpa status dengan mengirimkan histori percakapan lengkap di setiap
permintaan.

### Penyimpanan dan retensi data

Secara default, API menyimpan semua objek Interaksi (`store=true`) untuk menyederhanakan penggunaan fitur pengelolaan status sisi server (dengan `previous_interaction_id`), eksekusi di latar belakang (menggunakan `background=true`), dan tujuan observasi.

- **Paket Berbayar**: Sistem menyimpan interaksi selama **55 hari**.
- **Paket Gratis**: Sistem menyimpan interaksi selama **1 hari**.

Jika tidak menginginkannya, Anda dapat
menetapkan `store=false` dalam permintaan Anda. Kontrol ini terpisah dari pengelolaan status
; Anda dapat menonaktifkan penyimpanan untuk interaksi apa pun. Namun, perhatikan bahwa
`store=false` tidak kompatibel dengan `background=true` dan mencegah penggunaan
`previous_interaction_id` untuk giliran berikutnya.

Anda dapat menghapus interaksi tersimpan kapan saja menggunakan metode penghapusan yang ada di
[Referensi API](https://ai.google.dev/api/interactions-api?hl=id). Anda hanya dapat menghapus interaksi jika Anda mengetahui ID interaksi.

Setelah periode retensi berakhir, data Anda akan dihapus secara otomatis.

Sistem memproses objek Interaksi sesuai dengan [persyaratan](https://ai.google.dev/gemini-api/terms?hl=id).

## Praktik terbaik

- **Rasio hit cache**: Menggunakan `previous_interaction_id` untuk melanjutkan percakapan memungkinkan sistem lebih mudah memanfaatkan penyimpanan dalam cache implisit untuk histori percakapan, yang meningkatkan performa dan mengurangi biaya.
- **Mencampur interaksi**: Anda memiliki fleksibilitas untuk mencampur dan mencocokkan interaksi Agen dan Model dalam percakapan. Misalnya, Anda dapat menggunakan agen khusus, seperti agen Deep Research, untuk pengumpulan data awal, lalu menggunakan model Gemini standar untuk tugas lanjutan seperti meringkas atau memformat ulang, dengan menautkan langkah-langkah ini dengan `previous_interaction_id`.

## Model & agen yang didukung

| Nama Model | Jenis | ID Model |
| --- | --- | --- |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Pratinjau Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite-preview` |
| Pratinjau Gemini 3.1 Pro | Model | `gemini-3.1-pro-preview` |
| Pratinjau Gemini 3 Flash | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Pratinjau Klip Lyria 3 | Model | `lyria-3-clip-preview` |
| Pratinjau Lyria 3 Pro | Model | `lyria-3-pro-preview` |
| Pratinjau Deep Research | Agen | `deep-research-pro-preview-12-2025` |
| Pratinjau Deep Research | Agen | `deep-research-preview-04-2026` |
| Pratinjau Deep Research | Agen | `deep-research-max-preview-04-2026` |

## SDK

Anda dapat menggunakan Google GenAI SDK versi terbaru untuk mengakses
Interactions API.

- Di Python, ini adalah paket `google-genai` dari versi `1.55.0` dan seterusnya.
- Di JavaScript, ini adalah paket `@google/genai` dari versi `1.33.0`
  dan seterusnya.

Anda dapat mempelajari lebih lanjut cara menginstal SDK di halaman
[Libraries](https://ai.google.dev/gemini-api/docs/libraries?hl=id).

## Batasan

- **Status beta**: Interactions API dalam versi beta/pratinjau. Fitur dan
  skema dapat berubah.
- **MCP jarak jauh**: Gemini 3 tidak mendukung MCP jarak jauh, fitur ini akan segera hadir.

Fitur berikut didukung oleh API
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id), tetapi **belum tersedia** di
Interactions API:

- **[Metadata video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=id)**: Kolom `video_metadata`, yang digunakan untuk menetapkan interval
  klip dan kecepatan frame kustom untuk pemahaman video.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**
- **[Panggilan fungsi otomatis (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=id#automatic_function_calling_python_only)**
- **[Penyimpanan dalam cache eksplisit](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=id)**: Perhatikan bahwa penyimpanan dalam cache implisit sisi server tersedia di Interactions API
  melalui `previous_interaction_id`.

## Perubahan yang dapat menyebabkan gangguan

Interactions API saat ini berada dalam tahap beta awal. Kami secara aktif
mengembangkan dan menyempurnakan kemampuan API, skema resource, dan antarmuka
SDK berdasarkan penggunaan di dunia nyata dan masukan developer. Akibatnya, **perubahan yang menyebabkan gangguan dapat terjadi**.

Perubahan yang dapat menyebabkan gangguan yang ada:

- **Skema langkah**: Array langkah baru menggantikan array output, yang memberikan linimasa terstruktur dari setiap giliran interaksi.

Untuk mempelajari perubahan yang dapat menyebabkan gangguan terbaru dan memahami cara bermigrasi, lihat [Panduan migrasi perubahan yang dapat menyebabkan gangguan (Mei 2026)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=id).

Update potensial lainnya dapat mencakup perubahan pada skema untuk input dan output, tanda tangan metode SDK dan struktur objek, perilaku fitur tertentu.

Untuk workload produksi, Anda harus terus menggunakan API [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id) standar. Cara ini tetap menjadi jalur yang direkomendasikan untuk deployment yang stabil, dan kami akan terus mengembangkannya dan memeliharanya secara aktif.

## Masukan

Masukan Anda sangat penting untuk pengembangan Interactions API.
Sampaikan pendapat Anda, laporkan bug, atau minta fitur di
[Forum Komunitas Developer AI Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=id) kami.

## Langkah berikutnya

- Coba [notebook panduan memulai Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=id).
- Pelajari [Interaksi streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=id) untuk penanganan respons real-time.
- Pelajari lebih lanjut [Agen Deep Research Gemini](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-16 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-16 UTC."],[],[]]
