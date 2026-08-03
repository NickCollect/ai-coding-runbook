---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=id
fetched_at: 2026-08-03T04:27:57.080768+00:00
title: "Retensi data nol di Gemini Developer API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Retensi data nol di Gemini Developer API

Halaman ini menguraikan detail tentang apa yang biasanya disebut sebagai "retensi data nol" di Gemini Developer API.

## Batasan pelatihan

Seperti yang diuraikan dalam [Persyaratan Layanan Gemini API](https://ai.google.dev/gemini-api/terms?hl=id), saat Anda
menggunakan Layanan Berbayar, Google tidak menggunakan perintah Anda (termasuk petunjuk sistem
terkait, konten yang di-cache, dan file seperti gambar, video, atau dokumen) atau
respons untuk meningkatkan kualitas produk kami. Layanan Berbayar didefinisikan
[di sini](https://ai.google.dev/gemini-api/terms?hl=id#paid-services).

## Retensi data pelanggan dan pencapaian retensi data nol

Data pelanggan biasanya disimpan untuk jangka waktu terbatas dalam skenario dan kondisi berikut. Untuk mencapai retensi data nol, pelanggan harus mengambil tindakan tertentu atau menghindari fitur tertentu dalam setiap area berikut:

- **Pencatatan log perintah untuk pemantauan penyalahgunaan**: Seperti yang diuraikan dalam [Persyaratan Layanan Tambahan](https://ai.google.dev/gemini-api/terms?hl=id)
  Gemini API, untuk Layanan Berbayar, Google
  mencatat log perintah dan respons selama jangka waktu terbatas hanya untuk mendeteksi
  pelanggaran [Kebijakan Penggunaan Terlarang](https://policies.google.com/terms/generative-ai/use-policy?hl=id). Saat permintaan Anda untuk ZDR untuk project tertentu disetujui, semua konten pengguna (perintah dan respons) serta metadata yang dapat diidentifikasi (seperti alamat IP dan ID Akun Google) akan dihapus sebelum dicatat ke dalam log. Catatan yang dihasilkan ditandai sebagai data yang disanitasi dan tidak berisi data pengguna yang dapat diidentifikasi, sehingga memastikan kesetaraan dengan Retensi Data Nol Platform Agen Gemini Enterprise.
- **Grounding dengan Google Penelusuran**: Seperti yang diuraikan dalam [Persyaratan Layanan Tambahan Gemini API](https://ai.google.dev/gemini-api/terms?hl=id#grounding-with-google-search), Google menyimpan perintah, informasi kontekstual, dan output yang dihasilkan selama tiga puluh (30) hari untuk membuat hasil yang di-grounding dan saran penelusuran.
  Informasi yang disimpan ini dapat digunakan untuk proses debug dan pengujian sistem yang mendukung grounding. **Tidak ada cara untuk menonaktifkan penyimpanan informasi ini jika Anda menggunakan Grounding dengan Google Penelusuran.**
- **Grounding dengan Google Maps**: Seperti yang diuraikan dalam [Persyaratan Layanan Tambahan
  Gemini API](https://ai.google.dev/gemini-api/terms?hl=id), Google menyimpan perintah, informasi kontekstual, dan output yang dihasilkan selama tiga puluh (30) hari untuk membuat hasil yang di-grounding. Informasi yang disimpan ini hanya dapat digunakan untuk rekayasa keandalan, seperti proses debug jika terjadi masalah layanan.
  **Tidak ada cara untuk menonaktifkan penyimpanan informasi ini jika Anda menggunakan Grounding dengan Google Maps.**
- **Interactions API**: Interactions API mengelola status aktif
  percakapan untuk mengaktifkan percakapan multi-turn. **Secara default, Interactions API mengaktifkan penyimpanan status**. Untuk memastikan jejak data nol, Anda harus menetapkan parameter `store` ke `false` secara eksplisit dalam permintaan API untuk menonaktifkan retensi status default.
- **Live API**: API stateful ini memungkinkan koneksi ulang real-time dengan menyimpan
  status percakapan. Untuk mencapai retensi data nol, **jangan konfigurasi SessionResumptionConfig**. Jika handle sesi dibuat, status percakapan (termasuk teks, audio, dan video) akan disimpan hingga 24 jam.
- **Penyimpanan File API**: File API memungkinkan pengguna mengupload aset berukuran besar.
  File disimpan saat tidak digunakan hingga dihapus oleh pengguna atau hingga masa berlakunya berakhir.
  Penggunaan File API tidak bergantung pada pencatatan log ZDR; pengguna harus menghapus file secara manual untuk memastikan jejak data nol.
- **Caching Konteks Eksplisit**: Pengguna dapat melakukan cache dataset besar secara manual (misalnya,
  video panjang atau library dokumen) menggunakan kolom `cached_content`. Meskipun log permintaan ini mengikuti kebijakan penghapusan ZDR, konteks yang di-cache itu sendiri disimpan dengan `ttl` atau `expire_time` yang ditentukan pengguna. Untuk mencapai jejak data nol absolut, jangan gunakan fitur cached\_content.
- **Caching Dalam Memori Implisit**: Secara default, model Gemini melakukan cache data
  dalam memori untuk mengurangi latensi dan biaya bagi developer. Data ini sepenuhnya berada di RAM (tidak saat tidak digunakan), diisolasi di tingkat project, dan memiliki TTL 24 jam.
  **Hal ini tidak melanggar Retensi Data Nol.**

## Langkah berikutnya

- Pelajari [Kebijakan Penggunaan Terlarang untuk AI Generatif
  Policy](https://policies.google.com/terms/generative-ai/use-policy?hl=id).
- Tinjau [Persyaratan Layanan Tambahan Gemini API](https://ai.google.dev/gemini-api/terms?hl=id).
- Jika Anda memerlukan kontrol ZDR mandiri tingkat perusahaan, lihat panduan [Platform Agen Gemini Enterprise
  Retensi Data Nol](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-28 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-28 UTC."],[],[]]
