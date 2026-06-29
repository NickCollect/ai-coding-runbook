---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id
fetched_at: 2026-06-29T05:37:28.167348+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Interactions API

Interactions API adalah antarmuka baru kami dan cara paling mudah untuk membangun dengan model dan agen Gemini. Mulai Juni 2026, API ini Tersedia Secara Umum dan merupakan antarmuka yang direkomendasikan untuk semua project baru.

Meskipun kini dianggap sebagai API lama, API [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=id) asli tetap didukung sepenuhnya.

## Mengapa menggunakan Interactions API?

- **Kemampuan baru langsung digunakan**: Status percakapan sisi server opsional menggunakan `previous_interaction_id`, langkah-langkah eksekusi yang dapat diamati untuk proses debug dan rendering UI, serta [eksekusi di latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) untuk tugas yang berjalan lama menggunakan `background=true`.
- **Biaya lebih rendah dengan rasio hit cache yang lebih tinggi**: Pengelolaan status sisi server memungkinkan penyimpanan cache konteks yang lebih efisien di seluruh giliran, sehingga mengurangi biaya token untuk percakapan multi-giliran.
- **Dibuat untuk model dan agen canggih**: Dibuat khusus untuk model pemikiran, penggunaan alat multi-langkah, dan alur penalaran yang kompleks — menyederhanakan proses pembuatan, proses debug, dan orkestrasi aplikasi agentik.
- **Satu API untuk model dan agen**: Satu antarmuka terpadu untuk memanggil model dan agen Gemini secara langsung seperti Deep Research dan agen yang dikelola kustom — tidak ada endpoint atau pola terpisah yang perlu dipelajari.
- **Tempat peluncuran fitur baru**: Ke depannya, model dan kemampuan baru di luar keluarga utama, beserta kemampuan dan alat agentik baru, akan diluncurkan di Interactions API.

Secara default, Interactions API menyimpan permintaan sehingga Anda dapat memanfaatkan fitur pengelolaan status sisi server dengan menggunakan
`previous_interaction_id`. Anda dapat memilih untuk menggunakan perilaku tanpa status dengan menyetel
`store=false`. Lihat bagian [retensi data](#data-storage-retention) untuk
mengetahui detailnya.

## Mulai

- **Siapkan agen coding Anda**: Hubungkan ke **MCP Dokumen Gemini** dan instal
  keterampilan `gemini-interactions-api` untuk memberi asisten Anda akses langsung ke
  praktik terbaik dan dokumen developer terbaru.
  [Menyiapkan agen coding Anda →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)
- **Bermigrasi dari `generateContent`**: Jika Anda memiliki integrasi yang sudah ada,
  ikuti [Panduan Migrasi](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=id) untuk
  beralih ke Interactions API.
- **Mulai**: Mulai di [Panduan Memulai Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=id).

### Panduan Fitur

Pelajari kemampuan spesifik Interactions API melalui panduan ini. Anda dapat menggunakan tombol di halaman ini untuk beralih antara generateContent dan Interactions API:

- [Pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id)
- [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)
- [Pemahaman gambar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=id)
- [Pemahaman audio](https://ai.google.dev/gemini-api/docs/audio?hl=id)
- [Pemahaman video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id)
- [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id)
- [Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
- [Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)
- [Agen Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id)
- [Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)
- [Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)

## Cara kerja Interactions API

Interactions API berpusat pada resource inti: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=id#Resource:Interaction). `Interaction` mewakili giliran yang selesai dalam percakapan atau tugas. Objek ini berfungsi sebagai catatan sesi, yang berisi seluruh histori interaksi sebagai urutan **langkah-langkah eksekusi** secara kronologis. Langkah-langkah ini mencakup pemikiran model, panggilan dan hasil alat sisi server atau sisi klien (seperti `function_call` dan `function_result`), serta `model_output` akhir. Resource yang disimpan (diambil melalui `interactions.get`) juga mencakup langkah-langkah `user_input` untuk konteks lengkap, meskipun respons `interactions.create` hanya menampilkan langkah-langkah yang dibuat model.

Saat melakukan panggilan ke
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=id#CreateInteraction), Anda
membuat resource `Interaction` baru.

### Pengelolaan status sisi server

Anda dapat menggunakan `id` dari interaksi yang telah selesai dalam panggilan berikutnya menggunakan parameter
`previous_interaction_id` untuk melanjutkan percakapan. Server menggunakan ID ini untuk mengambil histori percakapan, sehingga Anda tidak perlu mengirim ulang seluruh histori chat.

Parameter `previous_interaction_id` hanya mempertahankan histori percakapan (input dan output)
menggunakan `previous_interaction_id`. Parameter lainnya adalah **cakupan interaksi**
dan hanya berlaku untuk interaksi tertentu yang sedang Anda buat:

- `tools`
- `system_instruction`
- `generation_config` (termasuk `thinking_level`, `temperature`, dll.)

Artinya, Anda harus menentukan ulang parameter ini di setiap interaksi baru jika ingin menerapkannya. Pengelolaan status sisi server ini bersifat opsional; Anda juga dapat beroperasi dalam mode tanpa status dengan mengirimkan histori percakapan lengkap di setiap permintaan.

### Penyimpanan dan retensi data

Secara default, API menyimpan semua objek Interaksi (`store=true`) untuk menyederhanakan penggunaan fitur pengelolaan status sisi server (dengan `previous_interaction_id`), [eksekusi latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) (menggunakan `background=true`), dan tujuan kemampuan pengamatan.

- **Paket Berbayar**: Sistem menyimpan interaksi selama **55 hari**.
- **Paket Gratis**: Sistem menyimpan interaksi selama **1 hari**.

Jika tidak menginginkannya, Anda dapat
menetapkan `store=false` dalam permintaan Anda. Kontrol ini terpisah dari pengelolaan status
; Anda dapat menonaktifkan penyimpanan untuk interaksi apa pun. Namun, perhatikan bahwa
`store=false` tidak kompatibel dengan [eksekusi di latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) dan mencegah penggunaan
`previous_interaction_id` untuk giliran berikutnya.

Anda dapat menghapus interaksi tersimpan kapan saja menggunakan metode penghapusan yang ada di
[Referensi API](https://ai.google.dev/api/interactions-api?hl=id). Anda hanya dapat menghapus interaksi jika Anda mengetahui ID interaksi.

Setelah periode retensi berakhir, data Anda akan dihapus secara otomatis.

Sistem memproses objek Interaction sesuai dengan [terms](https://ai.google.dev/gemini-api/terms?hl=id).

## Praktik terbaik

- **Rasio hit cache**: Menggunakan `previous_interaction_id` untuk melanjutkan percakapan memungkinkan sistem lebih mudah memanfaatkan penyimpanan dalam cache implisit untuk histori percakapan, yang meningkatkan performa dan mengurangi biaya.
- **Mencampur interaksi**: Anda memiliki fleksibilitas untuk mencampur dan mencocokkan interaksi Agen dan Model dalam percakapan. Misalnya, Anda dapat menggunakan agen khusus, seperti agen Deep Research, untuk pengumpulan data awal, lalu menggunakan model Gemini standar untuk tugas lanjutan seperti meringkas atau memformat ulang, dengan menautkan langkah-langkah ini dengan `previous_interaction_id`.

## Model & agen yang didukung

| Nama Model | Jenis | ID Model |
| --- | --- | --- |
| Gemini 3.5 Flash | Model | `gemini-3.5-flash` |
| Pratinjau Gemini 3.1 Pro | Model | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Pratinjau Gemini 3 Flash | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Model | `gemini-3-pro-image` |
| Gambar Gemini 3.1 Flash | Model | `gemini-3.1-flash-image` |
| Pratinjau Gemini 3.1 Flash TTS | Model | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Model | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Model | `gemma-4-26b-a4b-it` |
| Pratinjau Klip Lyria 3 | Model | `lyria-3-clip-preview` |
| Pratinjau Lyria 3 Pro | Model | `lyria-3-pro-preview` |
| Pratinjau Deep Research | Agen | `deep-research-preview-04-2026` |
| Pratinjau Deep Research | Agen | `deep-research-max-preview-04-2026` |
| Pratinjau Antigravity | Agen | `antigravity-preview-05-2026` |

## SDK

Anda dapat menggunakan Google GenAI SDK versi terbaru untuk mengakses
Interactions API.

- Di Python, ini adalah paket `google-genai` dari versi `2.3.0` dan seterusnya.
- Di JavaScript, ini adalah paket `@google/genai` dari versi `2.3.0` dan seterusnya.

Anda dapat mempelajari lebih lanjut cara menginstal SDK di halaman
[Libraries](https://ai.google.dev/gemini-api/docs/libraries?hl=id).

## Batasan

- **MCP Jarak Jauh**: Gemini 3 tidak mendukung MCP jarak jauh, fitur ini akan segera hadir.

Fitur berikut didukung oleh API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=id), tetapi **belum tersedia** di Interactions API:

- **[Metadata video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id)**: Kolom `video_metadata`, yang digunakan untuk menetapkan interval
  klip dan kecepatan frame kustom untuk pemahaman video.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**
- **[Panggilan fungsi otomatis (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=id#automatic_function_calling_python_only)**
- **[Penyimpanan dalam cache eksplisit](https://ai.google.dev/gemini-api/docs/caching?hl=id)**: Perhatikan bahwa penyimpanan dalam cache implisit sisi server tersedia di Interactions API
  melalui `previous_interaction_id`.

## Masukan

Masukan Anda sangat penting untuk pengembangan Interactions API.
Sampaikan pendapat Anda, laporkan bug, atau minta fitur di
[Forum Komunitas Developer AI Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=id) kami.

## Langkah berikutnya

- Coba [notebook mulai cepat Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=id).
- Pelajari lebih lanjut [Agen Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-26 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-26 UTC."],[],[]]
