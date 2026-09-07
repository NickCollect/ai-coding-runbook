---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=id
fetched_at: 2026-09-07T05:49:36.553575+00:00
title: "Pengoptimalan dan inferensi Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pengoptimalan dan inferensi Gemini API

Gemini API menawarkan berbagai mekanisme pengoptimalan untuk membantu Anda menyeimbangkan kecepatan, biaya, dan keandalan berdasarkan kebutuhan workload tertentu.
Baik Anda membuat bot percakapan real-time atau menjalankan pipeline pemrosesan data offline yang berat, memilih paradigma yang tepat dapat mengurangi biaya atau meningkatkan performa secara signifikan.

| Fitur | Standar | Fleksibel | Prioritas | Batch | Menyimpan ke cache |
| --- | --- | --- | --- | --- | --- |
| **Harga** | Harga Penuh | Diskon 50% | 75% hingga 100% lebih mahal dari standar | Diskon 50% | Diskon 90% + Penyimpanan token prorata |
| **Latensi** | Detik hingga menit | Menit (target 1–15 menit) | Detik | Hingga 24 jam | Waktu-hingga-token-pertama (TTFT) lebih cepat |
| **Keandalan** | Tinggi / Sedang-tinggi | Upaya terbaik (Dapat dihentikan) | Tinggi (Tidak dapat dihentikan) | Tinggi (untuk throughput) | T/A |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron | Status tersimpan |
| **Kasus penggunaan terbaik** | Alur kerja aplikasi umum | Rantai berurutan yang tidak mendesak | Aplikasi produksi yang ditampilkan kepada pengguna | Set data besar, evaluasi offline | Kueri berulang pada file yang sama |

## Tingkat layanan inferensi (Sinkron)

Anda dapat beralih antara traffic sinkron yang dioptimalkan untuk keandalan dan yang dioptimalkan untuk biaya dengan meneruskan parameter `service_tier` dalam panggilan pembuatan standar.

### Inferensi standar (Default)

Tingkat standar adalah opsi default untuk pembuatan konten berurutan.
Tingkat ini memberikan waktu respons normal tanpa premi tambahan atau antrean yang berat.

- **Keandalan:** Tingkat keparahan standar
- **Harga:** Harga standar.
- **Terbaik Untuk:** Sebagian besar aplikasi interaktif sehari-hari.

### Inferensi prioritas (Dioptimalkan untuk latensi)

[Pemrosesan](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)prioritas merutekan permintaan Anda
ke antrean komputasi dengan tingkat keparahan tinggi.
Traffic ini bersifat tidak dapat dihentikan (tidak pernah didahulukan oleh tingkat lainnya) dan menawarkan keandalan tertinggi. Jika Anda melebihi batas Prioritas dinamis, sistem akan menurunkan permintaan ke pemrosesan Standar, bukan gagal dengan error.

- **Keandalan:** Tingkat keparahan tertinggi
- **Harga:** 75% hingga 100% di atas tarif Standar.
- **Terbaik untuk:** Chatbot pelanggan, deteksi penipuan real-time, dan kopilot penting untuk bisnis.

### Inferensi fleksibel (Dioptimalkan untuk biaya)

[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id) menawarkan diskon 50% dibandingkan tarif standar dengan memanfaatkan
kapasitas komputasi di luar jam sibuk yang oportunistik. Permintaan diproses secara sinkron, yang berarti Anda tidak perlu menulis ulang kode untuk mengelola objek batch.
Karena merupakan traffic yang "dapat dihentikan", permintaan dapat didahulukan jika sistem mengalami lonjakan traffic standar.

- **Keandalan:** Tingkat keparahan yang tidak dijamin dan dapat dihentikan
- **Harga:** 50% dari Harga Standar (ditagih per token).
- **Terbaik untuk:** Alur kerja agen multi-langkah yang bergantung pada output panggilan N, update CRM latar belakang, dan evaluasi offline.

## Batch API (Massal, asinkron)

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id) dirancang untuk memproses permintaan dalam jumlah besar
secara asinkron dengan
biaya 50% dari biaya standar. Anda dapat mengirimkan permintaan sebagai kamus inline atau menggunakan file input JSONL (hingga 2 GB). API ini memproses permintaan menggunakan antrean throughput latar belakang dengan waktu penyelesaian target 24 jam.

- **Keandalan:** Dapat dihentikan, tetapi dengan sistem antrean dan percobaan ulang otomatis 24 jam
- **Harga:** 50% dari harga Standar.
- **Terbaik untuk:** Pra-pemrosesan set data besar, menjalankan rangkaian pengujian regresi berkala, dan pembuatan gambar atau embedding dalam volume tinggi.

## Context caching (Penghematan input)

[Context caching](https://ai.google.dev/gemini-api/docs/caching?hl=id) digunakan saat konteks awal yang substansial
dirujuk berulang kali oleh permintaan yang lebih singkat.

- **Caching implisit:** Diaktifkan secara otomatis pada model Gemini 2.5 dan yang lebih baru.
  Sistem akan memberikan penghematan biaya jika permintaan Anda cocok dengan cache yang ada berdasarkan awalan prompt umum.
- **Caching Eksplisit:** Anda dapat membuat objek cache secara manual dengan Time-To-Live (TTL) tertentu. Setelah dibuat, Anda dapat merujuk ke token yang di-cache untuk permintaan berikutnya agar tidak perlu meneruskan payload korpus yang sama berulang kali.
- **Harga:** Ditagih berdasarkan jumlah token cache dan durasi penyimpanan (TTL).
- **Terbaik Untuk:** Chatbot dengan petunjuk sistem yang ekstensif, analisis berulang pada file video yang panjang, atau kueri terhadap kumpulan dokumen besar.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
