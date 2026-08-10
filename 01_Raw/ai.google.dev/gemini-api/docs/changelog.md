---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=id
fetched_at: 2026-08-10T03:21:23.008291+00:00
title: "Catatan rilis \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Catatan rilis

Halaman ini mendokumentasikan update pada Gemini API.

## 21 Juli 2026

- **Gemini 3.6 Flash dan Gemini 3.5 Flash-Lite tersedia secara umum (GA)**:
  Merilis versi stabil dan siap produksi dari model Flash 3.x terbaru kami:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): Menampilkan peningkatan efisiensi token dan kemampuan perencanaan kode/agen dengan harga yang lebih rendah daripada 3.5 Flash, sehingga menyelesaikan masukan developer terkait kelebihan output.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): Menawarkan opsi sub-agen dengan latensi rendah dan sangat hemat biaya yang dirancang untuk otomatisasi bervolume tinggi.

  Untuk mempelajari lebih lanjut, lihat panduan [Model Gemini terbaru](https://ai.google.dev/gemini-api/docs/latest-model?hl=id).
- **Parameter yang tidak digunakan lagi**: Parameter sampling `temperature`, `top_p`
  dan `top_k` kini tidak digunakan lagi. Lihat
  [Model Gemini Terbaru](https://ai.google.dev/gemini-api/docs/latest-model?hl=id#sampling-parameter-deprecation)
  untuk mengetahui detailnya.

## 6 Juli 2026

- Dukungan [log developer](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id) untuk
  Interactions API: log untuk panggilan Interactions API yang didukung kini dapat dilihat
  di [dasbor AI Studio](https://aistudio.google.com/logs?hl=id).

## 30 Juni 2026

- **Gemini Omni Flash dalam pratinjau publik**: Dirilis `gemini-omni-flash-preview`,
  model multimodal berperforma tinggi yang dirancang untuk pembuatan video berkecepatan tinggi
  dan pengeditan video percakapan. Dengan [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id), Anda dapat membuat video berdurasi 3–10 detik dalam kualitas 720p dari deskripsi teks atau menganimasikan gambar diam, lalu mengedit dan menyempurnakan output secara percakapan. Untuk memulai, lihat panduan
  [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=id) dan kartu model
  [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=id).
- Merilis `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) untuk ketersediaan umum (GA), model multimodal bawaan kami yang dioptimalkan untuk latensi sangat rendah serta pembuatan dan pengeditan gambar yang hemat biaya. Lihat kartu model [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=id) dan panduan [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id).

## 24 Juni 2026

- **Penggunaan Komputer**: Meluncurkan dukungan pratinjau publik untuk alat
  [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id) di Gemini 3.5 Flash. Rilis
  ini mencakup tindakan yang disederhanakan dengan maksud, dukungan bawaan untuk
  lingkungan browser, seluler, dan desktop, kebijakan keamanan yang dapat dikonfigurasi, dan
  deteksi serangan injeksi perintah tingkat lanjut.

## 17 Juni 2026

- **Dukungan streaming untuk pembuatan ucapan**: Streaming melalui `streamGenerateContent`
  (dan `stream: true` di Interactions API) kini didukung untuk model
  `gemini-3.1-flash-tts-preview`. Untuk mempelajari lebih lanjut, lihat panduan [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id#streaming).

## 15 Juni 2026

- **Pengumuman penghentian**: Model pembuatan gambar berikut akan dihentikan dan [ditutup](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada **17 Agustus 2026**:

  - **Model Imagen 4 dan Gemini 3 Image**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    Untuk memigrasikan kode Anda ke endpoint pratinjau atau stabil yang lebih baru, lihat halaman
    [Penghentian penggunaan Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=id#imagen-models).
- **Pengumuman penghentian**: Model pembuatan video berikut akan dihentikan dan [ditutup](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada **30 Juni 2026**:

  - **Model Veo**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    Perbarui integrasi Anda untuk menggunakan ID model pratinjau Veo 3.1 (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) atau model GA 3.1 yang tersedia melalui [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=id) untuk menghindari gangguan layanan.
- **Pengumuman penghentian**: Alat eksperimental GMP Contextual View (antarmuka tetap untuk output Perujukan dengan Google Maps) akan [ditutup](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada **15 Juni 2026**:

## 1 Juni 2026

- Model Gemini 2.0 berikut kini [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Sebagai gantinya, gunakan [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) atau
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id).

## 28 Mei 2026

- Dirilis `gemini-3.1-flash-image` (Nano Banana 2) dan `gemini-3-pro-image`
  (Nano Banana Pro), versi yang tersedia secara umum (GA) dari model visual
  asli kami, [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=id)
  dan [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=id).
- **Dukungan pembuatan gambar dari video**: Anda kini dapat meneruskan file video (melalui upload langsung atau sebagai URL YouTube publik) sebagai konteks multimodal bersama dengan perintah teks untuk membuat thumbnail berkualitas tinggi, poster film sinematik, atau infografis ringkasan. Fitur ini hanya didukung di model
  `gemini-3.1-flash-image`. Untuk mempelajari lebih lanjut, lihat panduan
  [Pembuatan video ke gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id#video-to-image).
- Pengumuman penghentian: Model `gemini-3.1-flash-image-preview` dan
  `gemini-3-pro-image-preview` tidak digunakan lagi
  dan akan [dihentikan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 25 Juni 2026.

## 25 Mei 2026

- Model `gemini-3.1-flash-lite-preview` telah
  [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id). Sebagai gantinya, gunakan
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id).

## 19 Mei 2026

- Dirilis `gemini-3.5-flash`, versi yang tersedia secara umum (GA) dari
  [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id),
  model tercerdas kami untuk performa terdepan yang berkelanjutan dalam
  tugas agentic dan coding. Sekarang, model di balik `gemini-flash-latest` adalah model ini.
- Meluncurkan **Agen Terkelola di Gemini API** dalam pratinjau publik. Hal ini memungkinkan developer membangun dan men-deploy agen otonom dan stateful yang berjalan di lingkungan sandbox Linux yang aman dan terisolasi yang dihosting oleh Google. Untuk mempelajari lebih lanjut,
  lihat halaman [Ringkasan agen](https://ai.google.dev/gemini-api/docs/agents?hl=id) dan
  [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id).
- Merilis agen terkelola **Antigravity Agent** tujuan umum,
  [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=id), dalam pratinjau publik.
  Agen Antigravity dapat secara mandiri merencanakan, melakukan penalaran, menulis dan mengeksekusi kode,
  mengelola file, dan menjelajahi web di dalam container sandbox-nya. Lihat panduan
  [Agen Antigravitasi](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id) untuk mengetahui contoh
  kode dan spesifikasi.

## 7 Mei 2026

- Dirilis `gemini-3.1-flash-lite`, versi yang tersedia secara umum (GA) dari
  [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id),
  dioptimalkan untuk kecepatan, skala, dan efisiensi biaya.
- Pengumuman penghentian: Model `gemini-3.1-flash-lite-preview` akan dihentikan pada 11/5/26 dan akan [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 25 Mei 2026.

## 6 Mei 2026

- **Perubahan yang dapat menyebabkan gangguan mendatang**: Skema permintaan dan respons [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) (`outputs` → `steps`) serta konfigurasi format output (`response_format`) akan berubah. Skema baru akan menjadi
  default pada **26 Mei** dan skema lama akan dihapus pada **8 Juni**.
  Lihat
  [panduan migrasi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=id)
  untuk mengetahui detailnya.

## 5 Mei 2026

- Memperbarui **Penelusuran File** untuk mendukung penelusuran multimodal. Anda kini dapat menyematkan dan menelusuri gambar secara native menggunakan model `gemini-embedding-2`.
  Metadata perujukan kini mencakup `media_id` untuk kutipan visual dan
  `page_numbers` yang menunjukkan tempat informasi ditemukan. Untuk mempelajari lebih lanjut, lihat panduan [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id).

## 4 Mei 2026

- Meluncurkan dukungan [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=id) berbasis peristiwa di Gemini API untuk menggantikan alur kerja polling untuk Batch API dan operasi yang berjalan lama.

## 30 April 2026

- Model `gemini-robotics-er-1.5-preview` telah
  [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id). Sebagai gantinya, gunakan
  [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=id).

## 22 April 2026

- Merilis `gemini-embedding-2` sebagai layanan yang tersedia secara umum (GA). Untuk mempelajari lebih lanjut, lihat halaman [Embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id).

## 21 April 2026

- Merilis versi baru agen [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) dengan perencanaan kolaboratif, dukungan visualisasi, integrasi server MCP, dan Penelusuran File:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=id): Didesain untuk
    kecepatan dan efisiensi, ideal untuk di-streaming kembali ke UI klien.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=id): Komprehensifitas
    maksimum untuk pengumpulan dan sintesis konteks otomatis.

## 15 April 2026

- Meluncurkan [Pratinjau Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=id), model text-to-speech kami yang hemat biaya, ekspresif, dan dapat dikontrol. Baca dokumentasi
  [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id) untuk mempelajari lebih lanjut.

## 14 April 2026

- Merilis `gemini-robotics-er-1.6-preview`, model robotik kami yang telah diupdate.
  Sekarang Gemini memiliki kemampuan baru seperti membaca instrumen, kemampuan penalaran spasial dan fisik yang lebih baik. Untuk mempelajari lebih lanjut, lihat halaman [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id) dan [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=id).
- Pengumuman penghentian: Model `gemini-robotics-er-1.5-preview`
  akan [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 30 April 2026 pukul 09.00
  PST.

## 2 April 2026

- Dirilis `gemma-4-26b-a4b-it` dan `gemma-4-31b-it`, tersedia di
  [AI Studio](https://aistudio.google.com?hl=id) dan melalui Gemini API,
  sebagai bagian dari peluncuran [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=id).

## April 1, 2026

- Memperkenalkan tingkat inferensi [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id) dan [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id) baru, yang menawarkan lebih banyak opsi untuk mengoptimalkan biaya atau latensi.

## 31 Maret 2026

- Meluncurkan Pratinjau Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=id), model [pembuatan video](https://ai.google.dev/gemini-api/docs/video?hl=id) kami yang paling hemat biaya, yang dirancang untuk iterasi cepat dan membangun aplikasi bervolume tinggi.
- Model `gemini-2.5-flash-lite-preview-09-2025` telah dinonaktifkan. Sebagai gantinya, gunakan
  [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=id).

## 26 Maret 2026

- Dirilis [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=id), model audio-ke-audio (A2A) terbaru yang dirancang untuk dialog real-time dan aplikasi AI yang mengutamakan suara. Baca dokumen [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id) untuk mulai menggunakan API ini.

## 25 Maret 2025

- Meluncurkan model pembuatan musik [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=id): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=id)
  (klip 30 detik) dan [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=id)
  (lagu lengkap). Kedua model menerima input teks dan gambar serta menghasilkan audio stereo 48 kHz berkualitas tinggi. Lihat panduan
  [Pembuatan musik](https://ai.google.dev/gemini-api/docs/music-generation?hl=id) untuk mengetahui detail dan
  contoh kode.

## 23 Maret 2026

- Meluncurkan [paket penagihan Prabayar dan Pascabayar](https://ai.google.dev/gemini-api/docs/billing?hl=id) di AI Studio. Akun yang ada mungkin terpengaruh; baca dokumentasi [Penagihan](https://ai.google.dev/gemini-api/docs/billing?hl=id) untuk mengetahui informasi selengkapnya.

## 18 Maret 2026

- Merilis fitur [Kombinasi Alat Bawaan dan Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) baru, sehingga memungkinkan
  penggunaan alat bawaan Gemini bersama alat panggilan fungsi kustom
  dalam satu panggilan API.
- [Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id#supported_models)
  kini didukung untuk model Gemini 3 ke depannya.

## 16 Maret 2026

- Memperkenalkan [Tingkatan Penggunaan](https://ai.google.dev/gemini-api/docs/billing?hl=id#about-billing) yang diubah dan [batas pembelanjaan Akun Penagihan](https://ai.google.dev/gemini-api/docs/billing?hl=id#tier-spend-caps) untuk pengalaman penagihan pengguna yang lebih baik.

## 12 Maret 2026

- Memperkenalkan [batas pembelanjaan tingkat project](https://ai.google.dev/gemini-api/docs/billing?hl=id#project-spend-caps) untuk penagihan di AI Studio.

## 10 Maret 2026

- Merilis `gemini-embedding-2-preview`, model embedding multimodal pertama kami.
  Model ini mendukung input teks, gambar, video, audio, dan PDF,
  memetakan semua modalitas ke dalam ruang penyematan terpadu. Untuk mempelajari lebih lanjut, lihat
  [Embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id).
- Pengumuman penghentian: Model `gemini-2.5-flash-lite-preview-09-2025`
  akan [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 31 Maret 2026.

## 9 Maret 2026

- Model Pratinjau Gemini 3 Pro telah [ditutup](https://ai.google.dev/gemini-api/docs/deprecations?hl=id). `gemini-3-pro-preview` kini mengarah ke
  [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id).

## 3 Maret 2026

- Meluncurkan Pratinjau Gemini 3.1 Flash-Lite, model Flash-Lite pertama dalam seri Gemini 3. Baca [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=id) untuk mengetahui spesifikasi, update khusus, dan panduan developer.

## 26 Februari 2026

- Meluncurkan Nano Banana 2, [Pratinjau Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=id), model berefisiensi tinggi yang dioptimalkan untuk kecepatan dan kasus penggunaan bervolume tinggi.
- Pengumuman penghentian penggunaan: Pratinjau Gemini 3 Pro (`gemini-3-pro-preview`) akan [ditutup](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 9 Maret 2026.

## 19 Februari 2026

- Merilis [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id), iterasi terbaru kami dalam keluarga seri Gemini 3 baru.
- Meluncurkan endpoint terpisah `gemini-3.1-pro-preview-customtools`, yang lebih baik dalam memprioritaskan alat kustom, bagi pengguna yang membangun dengan campuran bash dan alat.

## 18 Februari 2026

- Pengumuman penghentian: Model berikut akan [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 1 Juni 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 Februari 2026

- Model berikut akan [dimatikan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 Januari 2026

- Meluncurkan dukungan untuk alat Penggunaan Komputer di `gemini-3-pro-preview` dan
  `gemini-3-flash-preview`.

## 21 Januari 2026

- Mengubah alias `latest`:

  - `gemini-pro-latest` beralih ke `gemini-3-pro-preview`
  - `gemini-flash-latest` beralih ke `gemini-3-flash-preview`

## 15 Januari 2026

- Pengumuman penghentian: Model berikut akan [dihentikan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) pada 17 Februari 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Model `gemini-2.5-flash-image-preview` telah dinonaktifkan.

## 14 Januari 2026

- Model `text-embedding-004` telah [dinonaktifkan](https://ai.google.dev/gemini-api/docs/deprecations?hl=id).

## 13 Januari 2026

- Menambahkan resolusi output 4K untuk [Veo](https://ai.google.dev/gemini-api/docs/video?hl=id) dan dukungan yang lebih luas untuk video potret dalam semua resolusi.

## 12 Januari 2026

- Meluncurkan fitur siklus proses model. Beberapa model kini akan menentukan tahap siklus proses dan linimasa penghentian. Lihat dokumentasi berikut untuk mengetahui informasi selengkapnya:

  - [Tahapan model](https://ai.google.dev/api/generate-content?hl=id#ModelStatus)

## 8 Januari 2026

- Meluncurkan dukungan untuk bucket Cloud Storage dan URL yang telah ditandatangani sebelumnya untuk DB publik dan pribadi sebagai sumber input data untuk Gemini API. Batas ukuran file juga telah ditingkatkan dari 20 MB menjadi 100 MB. Untuk mengetahui detailnya, lihat [Panduan metode input file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id).

## 19 Desember 2025

- Memperkenalkan perubahan yang dapat menyebabkan gangguan pada Interactions API di
  v1beta. Kolom `total_reasoning_tokens` telah diganti namanya menjadi
  `total_thought_tokens` agar lebih selaras dengan konsep "pemikiran" dalam
  model pemikiran.

## 17 Desember 2025

- Meluncurkan Pratinjau Gemini 3 Flash, `gemini-3-flash-preview`, yang memberikan performa cepat kelas terdepan yang menyaingi model yang lebih besar dengan sebagian kecil biaya. Dengan peningkatan penalaran visual dan spasial, serta kemampuan coding agentic. Baca dokumentasi tentang beberapa fitur baru, termasuk:

  - [Respons fungsi multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#multimodal)
  - [Eksekusi kode dengan gambar](https://ai.google.dev/gemini-api/docs/code-execution?hl=id#images)

## 12 Desember 2025

- Merilis `gemini-2.5-flash-native-audio-preview-12-2025`,
  model audio native baru untuk Live API. Update ini meningkatkan kemampuan model dalam menangani alur kerja yang kompleks. Untuk mempelajari lebih lanjut, lihat
  [panduan Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=id) dan
  [Audio Native Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=id).

## 11 Desember 2025

- Meluncurkan Interactions API. API ini menyediakan antarmuka terpadu untuk berinteraksi dengan model dan agen Gemini. Untuk mempelajari lebih lanjut, lihat panduan
  [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id).
- Meluncurkan Agen Deep Research Gemini dalam pratinjau. Deep Research dapat merencanakan, menjalankan, dan menyintesis hasil untuk tugas riset multilangkah secara mandiri. Lihat panduan [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) untuk
  mengetahui detailnya.

## 10 Desember 2025

- Meluncurkan peningkatan pada [model text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id) kami, pratinjau Gemini 2.5 Flash TTS (dioptimalkan untuk latensi rendah) dan pratinjau Gemini 2.5 Pro TTS (dioptimalkan untuk kualitas), termasuk ekspresivitas yang ditingkatkan, pengaturan kecepatan yang presisi, dan dialog yang lancar.

## 9 Desember 2025

- Model Gemini Live API berikut kini dinonaktifkan:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 Desember 2025

- Penagihan Gemini 3 untuk [Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) akan dimulai pada 5 Januari 2026.

## 4 Desember 2025

- Pengumuman penghentian: Model `gemini-2.5-flash-image-preview` akan dihentikan pada 15 Januari 2026.

## 3 Desember 2025

- Pengumuman penghentian penggunaan: Model `text-embedding-004` akan dinonaktifkan pada 14 Januari 2026.

## 20 November 2025

- Merilis Pratinjau Gambar Gemini 3 Pro, `gemini-3-pro-image-preview`, iterasi berikutnya untuk model Nano Banana. Baca halaman [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) untuk mengetahui detail selengkapnya.

## 18 November 2025

- Meluncurkan model seri Gemini 3 pertama, `gemini-3-pro-preview`, model penalaran dan pemahaman multimodal canggih kami dengan kemampuan agen dan coding yang canggih.

  Selain peningkatan kecerdasan dan performa, Pratinjau Gemini 3 Pro memperkenalkan perilaku baru terkait:

  - [Resolusi media](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id)
  - [Tanda tangan penalaran](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id)
  - [Tingkat penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#thinking-levels)

  Baca [Panduan Developer Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=id) untuk mengetahui migrasi, fitur baru, dan spesifikasi.

## 11 November 2025

- Pengumuman penghentian: Model berikut akan dihentikan:

  - 12 November:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 November:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 November 2025

- Model berikut akan dimatikan:

  - `imagen-3.0-generate-002`

  Gunakan [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=id#imagen-4). Lihat
  [tabel penghentian penggunaan Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=id) untuk mengetahui detail selengkapnya.

## 6 November 2025

- Meluncurkan File Search API ke pratinjau publik, sehingga pengembang dapat
  melakukan grounding respons dalam data mereka sendiri. Baca halaman [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id) baru untuk mengetahui info selengkapnya.

## 4 November 2025

- Untuk [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=id), jumlah token input untuk gambar telah dikurangi dari 1.290 menjadi 258, sehingga menurunkan biaya pengeditan gambar.
- Pengumuman penghentian: Model berikut akan dihentikan:

  - 18 November:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 Desember:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 Desember:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 Oktober 2025

- Meluncurkan alat [logging dan set data](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id) baru untuk Gemini API.

## 20 Oktober 2025

- Model Gemini Live API berikut kini dihentikan:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Sebagai gantinya, Anda dapat menggunakan `gemini-2.5-flash-native-audio-preview-09-2025`.
- Pengumuman penghentian: Penutupan untuk `gemini-2.0-flash-live-001` dan
  `gemini-live-2.5-flash-preview` akan dilakukan pada 9 Desember 2025.

## 17 Oktober 2025

- **Grounding with Google Maps** kini tersedia secara umum. Untuk mengetahui informasi selengkapnya, lihat dokumentasi [Merujuk dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id).

## 15 Oktober 2025

- Merilis model [Veo 3.1 dan 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=id#veo-3.1) dalam pratinjau publik, dengan fitur baru termasuk:

  - Memperpanjang video buatan Veo.
  - Mereferensikan hingga tiga gambar untuk membuat video.
  - Menyediakan gambar bingkai pertama dan terakhir untuk membuat video.

  Peluncuran ini juga menambahkan opsi durasi video output Veo 3: 4, 6, dan 8 detik.
- Pengumuman penghentian: Penutupan untuk `veo-3.0-generate-preview` dan
  `veo-3.0-fast-generate-preview` akan dilakukan pada 12 November 2025.

## 7 Oktober 2025

- Meluncurkan [Pratinjau Penggunaan Komputer Gemini 2.5](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)

## 2 Oktober 2025

- Meluncurkan GA Gemini 2.5 Flash Image: [Pembuatan Gambar dengan Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)

## 29 September 2025

- Model Gemini 1.5 berikut kini dinonaktifkan:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 September 2025

- Merilis model Gemini Robotics-ER 1.5 dalam pratinjau. Lihat
  [Ringkasan robotik](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id)
  untuk mempelajari cara menggunakan model untuk aplikasi robotik Anda.
- Meluncurkan model pratinjau berikut:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Lihat halaman [Model](https://ai.google.dev/gemini-api/docs/models?hl=id) untuk mengetahui detailnya.

## 23 September 2025

- Merilis `gemini-2.5-flash-native-audio-preview-09-2025`,
  model audio native baru untuk Live API dengan panggilan fungsi yang ditingkatkan
  dan penanganan pemotongan ucapan. Untuk mempelajari lebih lanjut, lihat
  [panduan Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=id) dan
  [Audio Native Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-native-audio).

## 16 September 2025

- Pengumuman penghentian: Model berikut akan dimatikan pada Oktober 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Lihat halaman [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=id) untuk mengetahui detail tentang model embedding terbaru.

## 10 September 2025

- Merilis dukungan untuk
  [model Sematan di Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id#batch-embedding),
  dan menambahkan Batch API ke
  [library kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id#batch) untuk cara yang lebih
  mudah dalam memulai kueri batch.

## 9 September 2025

- Meluncurkan GA Veo 3 dan Veo 3 Fast, dengan harga yang lebih rendah dan opsi baru untuk rasio aspek, resolusi, dan inisialisasi. Baca
  [dokumentasi Veo](https://ai.google.dev/gemini-api/docs/video?hl=id#model-features) untuk mengetahui informasi selengkapnya.

## 26 Agustus 2025

- Meluncurkan [Pratinjau Gambar Gemini 2.5](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-image-preview),
  model pembuatan gambar native terbaru kami.

## 18 Agustus 2025

- Merilis [alat konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) untuk ketersediaan umum (GA), alat untuk menyediakan URL sebagai konteks tambahan pada perintah. Dukungan untuk menggunakan konteks URL dengan model `gemini-2.0-flash`
  (tersedia selama rilis eksperimental) akan dihentikan dalam satu minggu.

## 14 Agustus 2025

- Merilis model Imagen 4 Ultra, Standard, dan Fast sebagai model yang tersedia secara umum (GA). Untuk mempelajari lebih lanjut, lihat halaman [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=id).

## 7 Agustus 2025

- `allow_adult` dalam pembuatan Image to Video kini tersedia di wilayah yang dibatasi. Lihat halaman
  [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=id#veo-model-parameters)
  untuk mengetahui detailnya.

## 31 Juli 2025

- Meluncurkan pembuatan video dari gambar untuk model Pratinjau Veo 3.
- Merilis model Pratinjau Veo 3 Fast.
- Untuk mempelajari Veo 3 lebih lanjut, buka halaman [Veo](https://ai.google.dev/gemini-api/docs/video?hl=id).

## 22 Juli 2025

- Merilis `gemini-2.5-flash-lite`, model Gemini 2.5 kami yang cepat, berbiaya rendah, dan berperforma tinggi. Untuk mempelajari lebih lanjut, lihat [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-lite).

## Juli 17, 2025

- Meluncurkan `veo-3.0-generate-preview`, update terbaru untuk Veo yang memperkenalkan pembuatan video dengan audio. Untuk mempelajari Veo 3 lebih lanjut, buka halaman [Veo](https://ai.google.dev/gemini-api/docs/video?hl=id).
- Peningkatan batas kecepatan untuk Imagen 4 Standard dan Ultra. Buka halaman
  [Batas kecepatan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id) untuk mengetahui detail selengkapnya.

## 14 Juli 2025

- Merilis `gemini-embedding-001`, versi stabil dari model penyematan teks kami. Untuk mempelajari lebih lanjut, lihat
  [embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id). Model `gemini-embedding-exp-03-07`
  tidak akan digunakan lagi mulai 14 Agustus 2025.

## 7 Juli 2025

- Meluncurkan Mode Batch Gemini API. Gabungkan permintaan dan kirimkan untuk diproses secara asinkron. Untuk mempelajari lebih lanjut, lihat [Mode Batch](https://ai.google.dev/gemini-api/docs/batch-mode?hl=id).

## 26 Juni 2025

- Model pratinjau `gemini-2.5-pro-preview-05-06` dan
  `gemini-2.5-pro-preview-03-25` kini dialihkan ke
  versi stabil terbaru `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` dimatikan.

## 24 Juni 2025

- Merilis model Pratinjau Ultra dan Standar Imagen 4. Untuk mempelajari lebih lanjut, lihat halaman
  [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id).

## 17 Juni 2025

- Merilis `gemini-2.5-pro`, versi stabil dari model tercanggih kami, kini dengan kemampuan berpikir adaptif. Untuk mempelajari lebih lanjut, lihat
  [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-pro)
  dan [Berpikir](https://ai.google.dev/gemini-api/docs/thinking?hl=id). `gemini-2.5-pro-preview-05-06`
  akan dialihkan ke `gemini-2.5-pro` pada 26 Juni 2025.
- Merilis `gemini-2.5-flash`, model 2.5 Flash stabil pertama kami. Untuk mempelajari lebih lanjut, lihat [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` tidak akan digunakan lagi pada 15 Juli 2025.
- Merilis `gemini-2.5-flash-lite-preview-06-17`, model Gemini 2.5 berperforma tinggi dan berbiaya rendah. Untuk mempelajari lebih lanjut, lihat [Pratinjau Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-lite).

## 5 Juni 2025

- Merilis `gemini-2.5-pro-preview-06-05`, versi baru model tercanggih kami, yang kini dilengkapi kemampuan berpikir adaptif. Untuk mempelajari lebih lanjut, lihat
  [Pratinjau Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-pro-preview-06-05)
  dan [Berpikir](https://ai.google.dev/gemini-api/docs/thinking?hl=id).
  `gemini-2.5-pro-preview-05-06` akan dialihkan ke `gemini-2.5-pro` pada
  26 Juni 2025.

## 27 Mei 2025

- Model penyesuaian terakhir yang tersedia, Gemini 1.5 Flash 001, telah dihentikan.
  Penyesuaian tidak lagi didukung di model apa pun.
  Lihat [Penyesuaian dengan Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=id).

## 20 Mei 2025

**Update API:**

- Meluncurkan dukungan untuk
  [pra-pemrosesan video kustom](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id#customize-video-processing)
  menggunakan interval kliping dan pengambilan sampel kecepatan frame yang dapat dikonfigurasi.
- Meluncurkan penggunaan multi-alat, yang mendukung konfigurasi
  [eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) dan
  [Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id) pada permintaan
  `generateContent` yang sama.
- Meluncurkan dukungan untuk
  [panggilan fungsi asinkron](https://ai.google.dev/gemini-api/docs/live-tools?hl=id#async-function-calling)
  di Live API.
- Meluncurkan [alat konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) eksperimental
  untuk memberikan URL sebagai konteks tambahan pada perintah.

**Update model:**

- Merilis `gemini-2.5-flash-preview-05-20`, model pratinjau
  [Gemini](https://ai.google.dev/gemini-api/docs/models?hl=id#model-versions) yang dioptimalkan untuk
  performa harga dan pemikiran adaptif. Untuk mempelajari lebih lanjut, lihat
  [Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-preview)
  dan [Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id).
- Merilis model
  [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-pro-preview-tts)
  dan
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-preview-tts), yang mampu
  [membuat ucapan](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id) dengan satu atau dua
  pembicara.
- Merilis model `lyria-realtime-exp`, yang
  [membuat musik](https://ai.google.dev/gemini-api/docs/music-generation?hl=id) secara real time.
- Merilis `gemini-2.5-flash-preview-native-audio-dialog` dan
  `gemini-2.5-flash-exp-native-audio-thinking-dialog`,
  model Gemini baru untuk Live API dengan kemampuan output audio native. Untuk mempelajari lebih lanjut, lihat [panduan Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#native-audio-output) dan [Audio Native Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-native-audio).
- Dirilis dalam pratinjau `gemma-3n-e4b-it`, tersedia di
  [AI Studio](https://aistudio.google.com?hl=id) dan melalui Gemini API,
  sebagai bagian dari peluncuran [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=id).

## 7 Mei 2025

- Merilis `gemini-2.0-flash-preview-image-generation`, model pratinjau untuk membuat dan mengedit gambar. Untuk mempelajari lebih lanjut, lihat [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) dan [Pembuatan Gambar Pratinjau Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.0-flash-preview-image-generation).

## 6 Mei 2025

- Merilis `gemini-2.5-pro-preview-05-06`, versi baru model kami yang paling canggih, dengan peningkatan pada panggilan fungsi dan kode. `gemini-2.5-pro-preview-03-25`
  akan otomatis mengarah ke versi baru model.

## 17 April 2025

- Merilis `gemini-2.5-flash-preview-04-17`, model pratinjau
  [Gemini](https://ai.google.dev/gemini-api/docs/models?hl=id#model-versions) yang dioptimalkan untuk
  performa harga dan pemikiran adaptif. Untuk mempelajari lebih lanjut, lihat
  [Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-flash-preview)
  dan [Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id).

## 16 April 2025

- Meluncurkan penyimpanan cache konteks untuk
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.0-flash).

## 9 April 2025

**Update model:**

- Merilis `veo-2.0-generate-001`, model text- dan image-to-video yang tersedia secara umum (GA), yang mampu menghasilkan video yang mendetail dan bernuansa artistik. Untuk mempelajari lebih lanjut, lihat [dokumentasi Veo](https://ai.google.dev/gemini-api/docs/video?hl=id).
- Merilis `gemini-2.0-flash-live-001`, versi pratinjau publik model
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) dengan penagihan diaktifkan.

  - **Peningkatan Pengelolaan Sesi dan Keandalan**

    - **Lanjutan Sesi:** Menjaga sesi tetap aktif saat terjadi gangguan jaringan sementara. API kini mendukung penyimpanan status sesi sisi server (hingga 24 jam) dan menyediakan handle (session\_resumption) untuk terhubung kembali dan melanjutkan dari tempat Anda berhenti.
    - **Sesi yang Lebih Panjang melalui Kompresi Konteks:** Memungkinkan interaksi yang lebih panjang dari batas waktu sebelumnya. Konfigurasi kompresi jendela konteks dengan mekanisme jendela geser untuk mengelola panjang konteks secara otomatis, sehingga mencegah penghentian mendadak karena batas konteks.
    - **Notifikasi Pemutusan Koneksi yang Baik:** Menerima pesan server `GoAway` yang menunjukkan kapan koneksi akan ditutup, sehingga memungkinkan penanganan yang baik sebelum penghentian.
  - **Kontrol Lebih Besar atas Dinamika Interaksi**
  - **Deteksi Aktivitas Suara (VAD) yang Dapat Dikonfigurasi:** Pilih tingkat sensitivitas atau nonaktifkan VAD otomatis sepenuhnya dan gunakan peristiwa klien baru (`activityStart`, `activityEnd`) untuk kontrol pergantian manual.
  - **Penanganan Interupsi yang Dapat Dikonfigurasi:** Tentukan apakah input pengguna
    harus menginterupsi respons model.
  - **Cakupan Putaran yang Dapat Dikonfigurasi:** Pilih apakah API memproses semua input audio dan video secara terus-menerus atau hanya merekamnya saat pengguna akhir terdeteksi sedang berbicara.
  - **Resolusi Media yang Dapat Dikonfigurasi:** Optimalkan kualitas atau penggunaan token
    dengan memilih resolusi untuk media input.
  - **Output dan Fitur yang Lebih Kaya**
  - **Opsi Suara & Bahasa yang Lebih Banyak:** Pilih dari dua suara baru dan 30 bahasa baru untuk output audio. Bahasa output kini dapat dikonfigurasi dalam `speechConfig`.
  - **Streaming Teks:** Menerima respons teks secara bertahap saat respons tersebut dibuat, sehingga memungkinkan tampilan yang lebih cepat kepada pengguna.
  - **Pelaporan Penggunaan Token:** Dapatkan insight tentang penggunaan dengan jumlah token mendetail yang diberikan di kolom `usageMetadata` pesan server, yang dikelompokkan menurut fase perintah dan respons serta modalitas.

## 4 April 2025

- Merilis `gemini-2.5-pro-preview-03-25`, versi pratinjau publik Gemini 2.5 Pro
  dengan penagihan diaktifkan. Anda dapat terus menggunakan `gemini-2.5-pro-exp-03-25` di tingkat gratis.

## 25 Maret 2025

- Merilis `gemini-2.5-pro-exp-03-25`, model Gemini eksperimental publik
  dengan mode penalaran selalu aktif secara default.
  Untuk mempelajari lebih lanjut, lihat
  [Gemini 2.5 Pro Eksperimental](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-2.5-pro-preview-03-25).

## 12 Maret 2025

**Update model:**

- Meluncurkan model eksperimental [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=id#gemini) yang mampu membuat dan mengedit gambar.
- Dirilis `gemma-3-27b-it`, tersedia di
  [AI Studio](https://aistudio.google.com?hl=id) dan melalui Gemini API,
  sebagai bagian dari peluncuran [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=id).

**Update API:**

- Menambahkan dukungan untuk
  [URL YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=id#youtube) sebagai sumber media.
- Menambahkan dukungan untuk menyertakan
  [video inline](https://ai.google.dev/gemini-api/docs/vision?hl=id#inline-video) yang berukuran kurang dari 20 MB.

## 11 Maret 2025

**Update SDK:**

- Merilis
  [Google Gen AI SDK for TypeScript and JavaScript](https://googleapis.github.io/js-genai)
  untuk pratinjau publik.

## 7 Maret 2025

**Update model:**

- Merilis `gemini-embedding-exp-03-07`, model embedding berbasis Gemini [eksperimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=id) dalam pratinjau publik.

## 28 Februari 2025

**Update API:**

- Dukungan untuk [Penelusuran sebagai alat](https://ai.google.dev/gemini-api/docs/grounding?hl=id)
  ditambahkan ke `gemini-2.0-pro-exp-02-05`, model eksperimental berdasarkan
  Gemini 2.0 Pro.

## 25 Februari 2025

**Update model:**

- Merilis `gemini-2.0-flash-lite`, versi yang tersedia secara umum (GA) dari
  [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-2.0-flash-lite),
  yang dioptimalkan untuk kecepatan, skala, dan efisiensi biaya.

## 19 Februari 2025

**Info terbaru AI Studio:**

- Dukungan untuk
  [wilayah tambahan](https://ai.google.dev/gemini-api/docs/available-regions?hl=id)
  (Kosovo, Greenland, dan Kepulauan Faroe).

**Update API:**

- Dukungan untuk
  [wilayah tambahan](https://ai.google.dev/gemini-api/docs/available-regions?hl=id)
  (Kosovo, Greenland, dan Kepulauan Faroe).

## 18 Februari 2025

**Update model:**

- Gemini 1.0 Pro tidak lagi didukung. Untuk mengetahui daftar model yang didukung, lihat
  [Model Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id).

## 11 Februari 2025

**Update API:**

- Update tentang
  [kompatibilitas library OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id).

## 6 Februari 2025

**Update model:**

- Merilis `imagen-3.0-generate-002`, versi yang tersedia secara umum (GA) dari
  [Imagen 3 di Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=id).

**Update SDK:**

- Merilis [Google Gen AI SDK untuk Java](https://github.com/googleapis/java-genai)
  untuk pratinjau publik.

## 5 Februari 2025

**Update model:**

- Merilis `gemini-2.0-flash-001`, versi yang tersedia secara umum (GA) dari
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-2.0-flash) yang
  mendukung output khusus teks.
- Merilis `gemini-2.0-pro-exp-02-05`,
  versi pratinjau publik [eksperimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=id) Gemini 2.0 Pro.
- Merilis `gemini-2.0-flash-lite-preview-02-05`, pratinjau publik eksperimental [model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-2.0-flash-lite) yang dioptimalkan untuk efisiensi biaya.

**Update API:**

- Menambahkan dukungan
  [input file dan output grafik](https://ai.google.dev/gemini-api/docs/code-execution?hl=id#input-output)
  untuk eksekusi kode.

**Update SDK:**

- Merilis
  [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/)
  dengan ketersediaan umum (GA).

## 21 Januari 2025

**Update model:**

- Dirilis `gemini-2.0-flash-thinking-exp-01-21`, versi pratinjau terbaru dari model yang mendukung [Gemini 2.0 Flash Thinking Model](https://ai.google.dev/gemini-api/docs/thinking?hl=id).

## 19 Desember 2024

**Update model:**

- Merilis Mode Penalaran Flash Gemini 2.0 untuk pratinjau publik. Mode Berpikir adalah
  model komputasi waktu pengujian yang memungkinkan Anda melihat proses berpikir model
  saat model menghasilkan respons, dan menghasilkan respons dengan kemampuan
  penalaran yang lebih kuat.

  Baca selengkapnya tentang Mode Flash Thinking Gemini 2.0 di [halaman ringkasan
  kami](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=id).

## 11 Desember 2024

**Update model:**

- Merilis [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-2.0-flash)
  untuk pratinjau publik. Daftar sebagian fitur Gemini 2.0 Flash Experimental mencakup:
  - Dua kali lebih cepat dari Gemini 1.5 Pro
  - Streaming dua arah dengan Live API kami
  - Pembuatan respons multimodal dalam bentuk teks, gambar, dan ucapan
  - Penggunaan alat bawaan dengan penalaran multi-giliran untuk menggunakan fitur seperti eksekusi kode, Penelusuran, pemanggilan fungsi, dan lainnya

Baca selengkapnya tentang Gemini 2.0 Flash di [halaman ringkasan
kami](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=id).

## 21 November 2024

**Update model:**

- Merilis `gemini-exp-1121`, model Gemini API eksperimental yang lebih canggih.

**Update model:**

- Memperbarui alias model `gemini-1.5-flash-latest` dan `gemini-1.5-flash`
  untuk menggunakan `gemini-1.5-flash-002`.
  - Perubahan pada parameter `top_k`: Model `gemini-1.5-flash-002`
    mendukung nilai `top_k` antara 1 dan 41 (eksklusif).
    Nilai yang lebih besar dari 40 akan diubah menjadi 40.

## 14 November 2024

**Update model:**

- Merilis `gemini-exp-1114`, model Gemini API eksperimental yang canggih.

## 8 November 2024

**Update API:**

- Menambahkan [dukungan untuk Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=id) di library OpenAI / REST API.

## 31 Oktober 2024

**Update API:**

- Menambahkan [dukungan untuk Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id).

## 3 Oktober 2024

**Update model:**

- Merilis `gemini-1.5-flash-8b-001`, versi stabil dari model Gemini API terkecil kami.

## 24 September 2024

**Update model:**

- Merilis `gemini-1.5-pro-002` dan `gemini-1.5-flash-002`, dua versi stabil baru
  Gemini 1.5 Pro dan 1.5 Flash, untuk ketersediaan umum.
- Memperbarui kode model `gemini-1.5-pro-latest` untuk menggunakan `gemini-1.5-pro-002`
  dan kode model `gemini-1.5-flash-latest` untuk menggunakan `gemini-1.5-flash-002`.
- Merilis `gemini-1.5-flash-8b-exp-0924` untuk menggantikan `gemini-1.5-flash-8b-exp-0827`.
- Merilis [filter keamanan integritas sipil](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id#safety-filters)
  untuk Gemini API dan AI Studio.
- Merilis dukungan untuk dua parameter baru untuk Gemini 1.5 Pro dan 1.5 Flash di Python dan NodeJS:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=id#FIELDS.frequency_penalty) dan
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=id#FIELDS.presence_penalty).

## 19 September 2024

**Info terbaru AI Studio:**

- Menambahkan tombol suka dan tidak suka ke respons model, agar pengguna dapat memberikan masukan tentang kualitas respons.

**Update API:**

- Menambahkan dukungan untuk kredit Google Cloud, yang kini dapat digunakan untuk penggunaan Gemini API.

## 17 September 2024

**Info terbaru AI Studio:**

- Menambahkan tombol **Buka di Colab** yang mengekspor perintah – dan kode untuk menjalankannya – ke notebook Colab. Fitur ini belum mendukung perintah dengan alat (mode JSON, panggilan fungsi, atau eksekusi kode).

## 13 September 2024

**Info terbaru AI Studio:**

- Menambahkan dukungan untuk mode perbandingan, yang memungkinkan Anda membandingkan respons di berbagai model dan perintah untuk menemukan yang paling sesuai dengan kasus penggunaan Anda.

## 30 Agustus 2024

**Update model:**

- Gemini 1.5 Flash mendukung
  [penyediaan skema JSON melalui konfigurasi model](https://ai.google.dev/gemini-api/docs/json-mode?hl=id#supply-schema-in-config).

## 27 Agustus 2024

**Update model:**

- Merilis [model eksperimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=id) berikut:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 Agustus 2024

**Update API:**

- Menambahkan dukungan untuk [pemrosesan PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=id).

## 5 Agustus 2024

**Update model:**

- Dukungan penyesuaian yang dirilis untuk Gemini 1.5 Flash.

## 1 Agustus 2024

**Update model:**

- Merilis `gemini-1.5-pro-exp-0801`, versi eksperimental baru dari
  [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-1.5-pro).

## 12 Juli 2024

**Update model:**

- Dukungan untuk Gemini 1.0 Pro Vision dihapus dari layanan dan alat AI Google.

## 27 Juni 2024

**Update model:**

- Rilis ketersediaan umum untuk jendela konteks 2 juta token Gemini 1.5 Pro.

**Update API:**

- Menambahkan dukungan untuk [eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id).

## 18 Juni 2024

**Update API:**

- Menambahkan dukungan untuk [penyimpanan cache konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id).

## 12 Juni 2024

**Update model:**

- Penghentian penggunaan Gemini 1.0 Pro Vision.

## 23 Mei 2024

**Update model:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) kini tersedia secara umum (GA).
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) tersedia secara umum (GA).

## 14 Mei 2024

**Update API:**

- Memperkenalkan jendela konteks 2 juta untuk Gemini 1.5 Pro (daftar tunggu).
- Memperkenalkan [penagihan](https://ai.google.dev/gemini-api/docs/billing?hl=id) bayar sesuai penggunaan untuk Gemini 1.0 Pro, dengan penagihan Gemini 1.5 Pro dan Gemini 1.5 Flash yang akan segera hadir.
- Memperkenalkan batas kapasitas yang lebih tinggi untuk paket berbayar Gemini 1.5 Pro yang akan datang.
- Menambahkan dukungan video bawaan ke [File API](https://ai.google.dev/api/rest/v1beta/files?hl=id).
- Menambahkan dukungan teks biasa ke [File API](https://ai.google.dev/api/rest/v1beta/files?hl=id).
- Menambahkan dukungan untuk panggilan fungsi paralel, yang menampilkan lebih dari satu
  panggilan sekaligus.

## 10 Mei 2024

**Update model:**

- Merilis [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) dalam pratinjau.

## 9 April 2024

**Update model:**

- Merilis [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) dalam pratinjau.
- Merilis model embedding teks baru, `text-embeddings-004`, yang mendukung ukuran
  [elastic embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id#elastic-embedding)
  di bawah 768.

**Update API:**

- Merilis [File API](https://ai.google.dev/api/rest/v1beta/files?hl=id) untuk menyimpan file media sementara untuk digunakan dalam perintah.
- Menambahkan dukungan untuk perintah dengan data teks, gambar, dan audio, yang juga dikenal sebagai perintah *multimodal*. Untuk mempelajari lebih lanjut, lihat
  [Membuat perintah dengan media](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=id).
- Merilis [Petunjuk sistem](https://ai.google.dev/gemini-api/docs/system-instructions?hl=id) dalam versi beta.
- Menambahkan
  [Mode panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#function_calling_mode),
  yang menentukan perilaku eksekusi untuk panggilan fungsi.
- Menambahkan dukungan untuk opsi konfigurasi `response_mime_type`, yang memungkinkan
  Anda meminta respons dalam
  [format JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=id#json).

## 19 Maret 2024

**Update model:**

- Menambahkan dukungan untuk
  [menyesuaikan Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  di Google AI Studio atau dengan Gemini API.

## 13 Desember 2023

**Update model:**

- gemini-pro: Model teks baru untuk berbagai tugas. Menyeimbangkan kemampuan dan efisiensi.
- gemini-pro-vision: Model multimodal baru untuk berbagai tugas.
  Menyeimbangkan kapabilitas dan efisiensi.
- embedding-001: Model embedding baru.
- aqa: Model baru yang disesuaikan secara khusus dan dilatih untuk menjawab pertanyaan
  menggunakan bagian teks untuk merujuk jawaban yang dihasilkan.

Lihat [Model Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id) untuk mengetahui detail selengkapnya.

**Update versi API:**

- v1: Saluran API stabil.
- v1beta: Saluran beta. Channel ini memiliki fitur yang mungkin masih dalam pengembangan.

Lihat [topik versi API](https://ai.google.dev/gemini-api/docs/api-versions?hl=id) untuk mengetahui detail selengkapnya.

**Update API:**

- `GenerateContent` adalah endpoint terpadu tunggal untuk chat dan teks.
- Streaming tersedia melalui metode `StreamGenerateContent`.
- Kemampuan multimodal: Gambar adalah modalitas baru yang didukung
- Fitur beta baru:
  - [Pemanggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=id)
  - Question Answering dengan Atribusi (AQA)
- Jumlah kandidat yang diperbarui: Model Gemini hanya menampilkan 1 kandidat.
- Kategori Setelan Keamanan dan SafetyRating yang berbeda. Lihat
  [setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id) untuk mengetahui detail selengkapnya.
- Penyetelan model belum didukung untuk model Gemini (Masih dalam proses).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
