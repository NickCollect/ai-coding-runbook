---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=id
fetched_at: 2026-07-20T04:33:22.271647+00:00
title: "Batas kapasitas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Batas kapasitas

Batas laju mengatur jumlah permintaan yang dapat Anda ajukan ke Gemini API dalam jangka waktu tertentu. Batasan ini membantu mempertahankan penggunaan yang adil, melindungi dari penyalahgunaan, dan membantu mempertahankan performa sistem untuk semua pengguna.

[Melihat batas frekuensi aktif di AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=id)

## Cara kerja batas laju

Batas laju biasanya diukur di tiga dimensi:

- Permintaan per menit (**RPM**)
- Token per menit (input) (**TPM**)
- Permintaan per hari (**RPD**)

Penggunaan Anda dievaluasi terhadap setiap batas, dan jika salah satu batas terlampaui, error batas kecepatan akan dipicu. Misalnya, jika batas RPM Anda adalah 20, membuat 21
permintaan dalam satu menit akan menghasilkan error, meskipun Anda belum melampaui
TPM atau batas lainnya.

Batas laju diterapkan per project, bukan per kunci API. Kuota permintaan per hari (**RPD**) direset pada tengah malam waktu Pasifik.

Batas bervariasi bergantung pada model spesifik yang digunakan, dan beberapa batas hanya berlaku untuk model tertentu. Misalnya, Gambar per menit (IPM) hanya dihitung untuk model yang mampu membuat gambar (Nano Banana), tetapi secara konseptual mirip dengan TPM. Model lain mungkin memiliki batas token per hari (TPD).

Batas kapasitas lebih terbatas untuk model eksperimental dan pratinjau.

### Batas frekuensi berbasis pembelanjaan

Selain batas permintaan per menit (RPM) dan token per menit (TPM), Gemini API menerapkan batas kapasitas berbasis pembelanjaan untuk melindungi dari biaya yang tidak terduga. Apakah batas ini berlaku untuk akun Anda atau tidak bergantung pada histori penagihan dan [tingkat penggunaan](#usage-tiers) Anda.

Tabel berikut menunjukkan batas frekuensi berbasis pembelanjaan untuk setiap
[tingkat penggunaan](#usage-tiers). Batas ini dievaluasi dalam jangka waktu 10 menit yang terus berlanjut. Apakah batas ini berlaku untuk akun Anda bergantung pada histori penagihan dan reputasi akun Anda.

| Tingkat penggunaan | Batas laju pembelanjaan (per 10 menit) |
| --- | --- |
| **Gratis** | T/A |
| **Tingkat 1** | $10 |
| **Tingkat 2** | $200 |
| **Tingkat 3** | $200 |

Jika Anda mencapai batas tarif berbasis pembelanjaan, API akan menampilkan error `429 RESOURCE_EXHAUSTED`. Untuk mengatasi hal ini:

- **Tunggu dan coba lagi** setelah beberapa saat.
- **Kurangi frekuensi permintaan yang mahal**, misalnya dengan menggunakan jendela konteks yang lebih kecil atau output yang lebih pendek.
- Jika Anda terus-menerus mencapai batas ini selama penggunaan normal,
  [minta peningkatan batas kecepatan](#request-rate-limit-increase).

## Tingkat penggunaan

Pembatasan kapasitas terikat dengan tingkat penggunaan project. Seiring meningkatnya penggunaan dan pembelanjaan API, Anda akan otomatis diupgrade ke tingkat yang lebih tinggi dengan batas tarif yang lebih tinggi.

Kualifikasi untuk Tingkat 2 dan 3 didasarkan pada total pembelanjaan kumulatif
untuk layanan Google Cloud (termasuk, tetapi tidak terbatas pada, Gemini API) untuk
akun penagihan yang ditautkan ke project Anda.

| Tingkat penggunaan | Kualifikasi | [Batas tingkat penagihan](https://ai.google.dev/gemini-api/docs/billing?hl=id#tier-spend-caps) |
| --- | --- | --- |
| **Gratis** | [Project aktif](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) atau uji coba gratis | T/A |
| **Tingkat 1** | [Menyiapkan dan menautkan akun penagihan yang aktif](https://ai.google.dev/gemini-api/docs/billing?hl=id#setup-billing) | $250 |
| **Tingkat 2** | Dibayar $100 + 3 hari sejak pembayaran pertama yang berhasil | $2.000 |
| **Tingkat 3** | Membayar $1.000 + 30 hari sejak pembayaran pertama yang berhasil | $20.000 - $100.000+ |

Meskipun memenuhi kriteria kelayakan yang dinyatakan umumnya sudah cukup untuk mendapatkan persetujuan, dalam kasus yang jarang terjadi, permintaan upgrade dapat ditolak berdasarkan faktor lain yang diidentifikasi selama proses peninjauan.

Sistem ini membantu menjaga keamanan dan integritas platform Gemini API bagi semua pengguna.

## Batas kapasitas Gemini API

Batas frekuensi bergantung pada berbagai faktor (seperti tingkat penggunaan Anda) dan dapat dilihat di Google AI Studio. Seiring perubahan tingkat dan status akun Anda dari waktu ke waktu, batas laju Anda akan diperbarui secara otomatis.

[Melihat batas frekuensi aktif di AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=id)

Batas frekuensi yang ditentukan tidak dijamin dan kapasitas sebenarnya dapat bervariasi.

## Batas frekuensi inferensi prioritas

Penggunaan [Prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id) memiliki batas laju sendiri meskipun penggunaan dihitung dalam batas laju traffic interaktif keseluruhan. **Batas frekuensi default adalah: 0,3x [batas frekuensi standar](https://aistudio.google.com/rate-limit?hl=id) untuk setiap model dan tingkat**

## Batas kapasitas API batch

Permintaan [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id) tunduk pada batas kapasitasnya sendiri, terpisah dari panggilan API non-batch.

- **Permintaan batch serentak:** 100
- **Batas ukuran file input:** 2 GB
- **Batas penyimpanan file:** 20 GB
- **Token dalam antrean per model:** Tabel **Token dalam antrean batch** mencantumkan jumlah maksimum token yang dapat dimasukkan dalam antrean untuk pemrosesan batch di semua tugas batch aktif Anda untuk model tertentu.

### Tingkat 1

| Model | Token yang dimasukkan dalam antrean batch |
| --- | --- |
| Model teks keluar | | | | |
| --- | --- | --- | --- | --- |
| Pratinjau Gemini 3.1 Pro | 5.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Pratinjau Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Pratinjau Gemini 2.5 Flash | 3.000.000 |
| Pratinjau Gambar Gemini 2.5 Flash | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 10.000.000 |
| Pratinjau Gemini 2.5 Flash Lite | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Gambar Gemini 2.0 Flash | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Model pembuatan multi-modal | | | | |
| Pratinjau Gambar Flash Gemini 3.1 🍌 | 1.000.000 |
| Gambar Gemini 3.1 Flash Lite 🍌 | 2.000.000 |
| Pratinjau Gambar Gemini 3 Pro 🍌 | 2.000.000 |
| Model embedding | | | | |
| Penyematan Gemini | 500.000 |

### Tingkat 2

| Model | Token yang dimasukkan dalam antrean batch |
| --- | --- |
| Model teks keluar | | | | |
| --- | --- | --- | --- | --- |
| Pratinjau Gemini 3.1 Pro | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Pratinjau Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Pratinjau Gemini 2.5 Flash | 400.000.000 |
| Pratinjau Gambar Gemini 2.5 Flash | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 500.000.000 |
| Pratinjau Gemini 2.5 Flash Lite | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Gambar Gemini 2.0 Flash | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Model pembuatan multi-modal | | | | |
| Pratinjau Gambar Flash Gemini 3.1 🍌 | 250.000.000 |
| Gambar Gemini 3.1 Flash Lite 🍌 | 270.000.000 |
| Pratinjau Gambar Gemini 3 Pro 🍌 | 270.000.000 |
| Model embedding | | | | |
| Penyematan Gemini | 5.000.000 |

### Tingkat 3

| Model | Token yang dimasukkan dalam antrean batch |
| --- | --- |
| Model teks keluar | | | | |
| --- | --- | --- | --- | --- |
| Pratinjau Gemini 3.1 Pro | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Pratinjau Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Pratinjau Gemini 2.5 Flash | 1.000.000.000 |
| Pratinjau Gambar Gemini 2.5 Flash | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash Lite | 1.000.000.000 |
| Pratinjau Gemini 2.5 Flash Lite | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Gambar Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Model pembuatan multi-modal | | | | |
| Pratinjau Gambar Flash Gemini 3.1 🍌 | 750.000.000 |
| Gambar Gemini 3.1 Flash Lite 🍌 | 1.000.000.000 |
| Pratinjau Gambar Gemini 3 Pro 🍌 | 1.000.000.000 |
| Model embedding | | | | |
| Penyematan Gemini | 10.000.000 |

## Cara mengupgrade ke tingkat berikutnya

Untuk bertransisi dari Paket gratis ke paket berbayar, Anda harus
[menyiapkan penagihan di AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=id) terlebih dahulu.

Setelah proyek Anda memenuhi [kriteria yang ditentukan](#usage-tiers), proyek tersebut akan
diupgrade secara otomatis ke tingkat berikutnya. Upgrade paket dari Gratis ke Paket 1
biasanya akan langsung diterapkan, dan upgrade paket berikutnya akan
diterapkan dalam waktu 10 menit. Buka [halaman Project](https://aistudio.google.com/projects?hl=id) di AI Studio untuk memeriksa tingkat Anda.

## Meminta peningkatan batas laju

Setiap variasi model memiliki batas frekuensi panggilan yang terkait (permintaan per menit, RPM).
Untuk mengetahui detail tentang batas frekuensi tersebut, lihat halaman
[Batas Frekuensi AI Studio](https://aistudio.google.com/rate-limit?hl=id).

[Meminta peningkatan batas frekuensi tingkat berbayar](https://forms.gle/ETzX94k8jf7iSotH9)

Kami tidak memberikan jaminan tentang peningkatan batas kecepatan Anda, tetapi kami akan berupaya sebaik mungkin untuk meninjau permintaan Anda.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-03 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-03 UTC."],[],[]]
