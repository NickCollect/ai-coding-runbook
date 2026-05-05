---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id
fetched_at: 2026-05-05T13:20:58.094593+00:00
title: "Log dan set data \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/Deep Research Gemini) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

- [Beranda](https://ai.google.dev/gemini-api/docs/Beranda)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumen](https://ai.google.dev/gemini-api/docs/Dokumen)

Kirim masukan

# Log dan set data

Panduan ini berisi semua yang Anda perlukan untuk mulai mengaktifkan logging untuk aplikasi Gemini API yang ada. Dalam panduan ini, Anda akan mempelajari cara melihat log dari aplikasi yang ada atau baru di dasbor Google AI Studio untuk lebih memahami perilaku model dan cara pengguna berinteraksi dengan aplikasi Anda. Gunakan logging untuk mengamati, men-debug, dan *secara opsional membagikan masukan penggunaan
kepada Google untuk membantu meningkatkan kualitas Gemini di berbagai kasus penggunaan developer*.[\*](https://ai.google.dev/gemini-api/docs/\*)

Semua panggilan API `GenerateContent` dan `StreamGenerateContent` didukung,
termasuk panggilan yang dilakukan melalui endpoint [kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/kompatibilitas OpenAI).

## 1. Mengaktifkan logging di Google AI Studio

Sebelum memulai, pastikan Anda memiliki project yang mengaktifkan penagihan dan Anda adalah pemiliknya.

1. Buka halaman log di Google [AI Studio](https://ai.google.dev/gemini-api/docs/AI Studio).
2. Pilih project Anda dari menu drop-down dan tekan tombol aktifkan untuk mengaktifkan logging untuk semua permintaan secara default.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=id)

Anda dapat mengaktifkan atau menonaktifkan logging untuk semua project atau untuk project tertentu, dan mengubah preferensi ini kapan saja melalui Google AI Studio.

## 2. Melihat log di AI Studio

1. Buka [AI Studio](https://ai.google.dev/gemini-api/docs/AI Studio).
2. Pilih project yang telah Anda aktifkan logging-nya.
3. Anda akan melihat log muncul di tabel dalam urutan kronologis terbalik.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Klik entri untuk melihat pasangan permintaan dan respons dalam tampilan halaman penuh. Anda dapat memeriksa perintah lengkap, respons lengkap dari Gemini, dan konteks dari giliran sebelumnya. Perhatikan bahwa setiap project memiliki batas penyimpanan default hingga 1.000 log, dan log yang tidak disimpan dalam set data akan berakhir masa berlakunya setelah 55 hari. Jika project Anda mencapai batas penyimpanan, Anda akan diminta untuk menghapus log.

## 3. Menyeleksi dan membagikan set data

- Dari tabel log, temukan panel filter di bagian atas untuk memilih properti yang akan digunakan sebagai filter.
- Dari tampilan log yang difilter, gunakan kotak centang untuk memilih semua atau beberapa log.
- Klik tombol "Buat Set Data" yang muncul di bagian atas daftar.
- Beri nama deskriptif dan deskripsi opsional untuk set data baru Anda.
- Anda akan melihat set data yang baru saja dibuat dengan kumpulan log yang diseleksi.
- Ekspor set data Anda untuk analisis lebih lanjut sebagai file CSV, JSONL, atau ke Google Spreadsheet.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Set data dapat berguna untuk sejumlah kasus penggunaan yang berbeda.

- **Menyeleksi set tantangan:** Mendorong peningkatan di masa mendatang yang menargetkan area yang ingin Anda tingkatkan kualitas AI-nya.
- **Menyeleksi set sampel:** Misalnya, sampel dari penggunaan sebenarnya untuk membuat respons dari model lain, atau kumpulan kasus ekstrem untuk pemeriksaan rutin sebelum deployment.
- **Set evaluasi:** Set yang mewakili penggunaan sebenarnya di seluruh kemampuan penting, untuk perbandingan di seluruh model lain atau iterasi petunjuk sistem.

Anda dapat membantu mendorong kemajuan dalam riset AI, Gemini API, dan Google AI Studio dengan memilih untuk membagikan set data Anda sebagai contoh demonstrasi. Hal ini memungkinkan kami menyempurnakan model kami dalam berbagai konteks dan membuat sistem AI yang tetap berguna bagi developer di berbagai bidang dan aplikasi

## Langkah berikutnya &hal yang akan diuji

Setelah mengaktifkan logging, berikut beberapa hal yang dapat Anda coba:

- **Membuat prototipe dengan histori sesi:** Manfaatkan [Build AI Studio](https://ai.google.dev/gemini-api/docs/Build AI Studio) untuk membuat prototipe aplikasi kode dan menambahkan kunci API Anda untuk mengaktifkan histori log pengguna.
- **Menjalankan kembali log dengan Gemini Batch API:** Gunakan set data untuk pengambilan sampel respons
  dan evaluasi model atau logika aplikasi dengan menjalankan kembali log melalui
  [Gemini Batch API](https://ai.google.dev/gemini-api/docs/Gemini Batch API).

## Kompatibilitas

Logging saat ini tidak didukung untuk hal berikut:

- Model Imagen dan Veo
- Model embedding Gemini
- Input yang berisi video, GIF, atau PDF

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Lisensi Creative Commons Attribution 4.0), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://ai.google.dev/gemini-api/docs/Lisensi Apache 2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://ai.google.dev/gemini-api/docs/Kebijakan Situs Google Developers). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?
