---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=id
fetched_at: 2026-06-01T06:08:31.462074+00:00
title: "Membangun aplikasi di Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Membangun aplikasi di Google AI Studio

Halaman ini menjelaskan cara menggunakan Google AI Studio untuk membuat (atau "mengodekan vibe") dan men-deploy aplikasi dengan cepat yang menguji kemampuan terbaru Gemini seperti [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) dan [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id). Google AI Studio mendukung pembuatan **aplikasi web** dengan runtime full-stack dan **aplikasi Android native** dengan Kotlin dan Jetpack Compose — semuanya melalui perintah bahasa alami.

## Mulai

Mulai vibe coding di [Mode build](https://aistudio.google.com/apps?hl=id) Google AI Studio. Anda dapat
mulai membangun dengan beberapa cara:

- **Mulai dengan perintah**: Dalam mode Buat, gunakan kotak input untuk memasukkan deskripsi tentang apa yang ingin Anda buat. Pilih Chip AI untuk menambahkan fitur tertentu seperti pembuatan gambar atau data Google Maps ke perintah Anda. Anda bahkan dapat mengucapkan apa yang Anda inginkan menggunakan tombol speech-to-text.
- **Tombol "Saya Lagi Beruntung"**: Jika Anda membutuhkan ide kreatif, gunakan tombol "Saya Lagi Beruntung", dan Gemini akan membuat perintah dengan ide project untuk membantu Anda memulai.
- **Me-remix project dari galeri**: Buka project dari [Galeri
  Aplikasi](https://aistudio.google.com/apps?source=showcase&hl=id), lalu pilih **Salin Aplikasi**.

Setelah Anda menjalankan perintahnya, Anda akan melihat kode dan file yang diperlukan dibuat,
dengan pratinjau live aplikasi Anda yang muncul di sisi kanan.

## Apa yang dibuat?

Saat Anda menjalankan perintah, AI Studio akan membuat aplikasi lengkap. Anda dapat memilih untuk membuat **aplikasi web** atau **aplikasi Android native** menggunakan pemilih platform.

Untuk **aplikasi web** (default), AI Studio membuat lingkungan full stack yang mencakup:

- **Sisi klien**: frontend web (React adalah default).
- **Sisi server**: runtime Node.js yang memungkinkan panggilan API yang aman, koneksi database, dan penggunaan paket npm.

Untuk **aplikasi Android**, AI Studio membuat project Kotlin dan Jetpack Compose
yang dapat Anda lihat pratinjaunya di emulator berbasis browser, diinstal di perangkat fisik,
dan dipublikasikan ke Play Store untuk pengujian. [Pelajari lebih lanjut cara membuat aplikasi Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=id).

Anda dapat melihat kode yang dibuat dengan memilih tab **Kode** di panel pratinjau sebelah kanan. **Antigravity Agent** secara cerdas mengelola beberapa file di seluruh stack Anda, memastikan perubahan disebarkan dengan benar.

### The Antigravity Agent

**Antigravity Agent** adalah fungsi AI utama dalam [Google Antigravity](https://antigravity.google?hl=id) dan kini komponen inti dari framework agen mendukung pengalaman mode Build di Google AI Studio. Gemini
melampaui pembuatan kode sederhana dengan mempertahankan konteks seluruh project Anda,
mengelola beberapa file, dan memahami petunjuk yang kompleks untuk membangun aplikasi full-stack yang andal.

Kemampuan utama meliputi:

- **Pemahaman konteks**: mempertahankan konteks perintah dan status file sebelumnya.
- **Pengelolaan multi-file**: menangani dependensi di beberapa file.
- **Eksekusi terverifikasi**: memverifikasi update kode untuk mengurangi halusinasi.

## Kemampuan full-stack

Google AI Studio membuka potensi ekosistem web modern, sehingga Anda dapat membangun lebih dari sekadar prototipe sisi klien.

- **Runtime sisi server & npm**: gunakan library paket npm yang luas. Agen
  akan otomatis mengidentifikasi dan menginstal paket sesuai kebutuhan untuk
  aplikasi Anda (misalnya, library tertentu untuk visualisasi data atau klien API). Anda
  juga dapat meminta paket tertentu jika diinginkan.
- **Pengelolaan secret**: menyimpan kunci API dan secret dengan aman di menu
  **Setelan**. Nilai ini dapat diakses dalam kode sisi server Anda, sehingga aman dari eksposur sisi klien.
- **Multiplayer**: bangun pengalaman kolaboratif real-time langsung di dalam AI Studio. Runtime sisi server mengelola status dan koneksi yang diperlukan agar pengguna dapat berinteraksi bersama.
- **Firebase Firestore dan Authentication**: menyediakan dan menyiapkan Firebase secara otomatis, termasuk database Firestore (penyimpanan data persisten) dan Firebase Authentication (alur login, khususnya "Login dengan Google").
  Agen menangani seluruh proses penyiapan dan bahkan menulis kode di aplikasi Anda untuk layanan ini.
- **Integrasi Google Workspace**: Hubungkan aplikasi Anda ke API Google Workspace seperti Gmail, Spreadsheet, Dokumen, Drive, Kalender, dan lainnya. AI Studio menangani
  semua konfigurasi OAuth secara otomatis.

[Pelajari lebih lanjut pengembangan aplikasi full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=id)

### Aplikasi Android

Anda juga dapat membuat aplikasi Android native menggunakan Kotlin dan Jetpack Compose.
Pratinjau aplikasi Anda di emulator Android berbasis browser, instal di perangkat fisik menggunakan ADB di browser, dan publikasikan ke Play Store untuk pengujian internal.

[Pelajari lebih lanjut cara membangun aplikasi Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=id)

## Lanjutkan pembuatan

Setelah Google AI Studio membuat kode awal untuk aplikasi Anda, Anda
dapat terus menyempurnakannya:

### Membangun solusi di Google AI Studio

- **Melakukan iterasi dengan Gemini**: Gunakan panel chat dalam **Mode pembuatan** untuk meminta Gemini
  membuat modifikasi, menambahkan fitur baru, atau mengubah gaya.
- **Mengedit kode secara langsung**: Buka **tab Kode** di panel pratinjau untuk melakukan pengeditan langsung.

### Mengembangkan secara eksternal

Untuk alur kerja yang lebih canggih, Anda dapat mengekspor kode dan bekerja di lingkungan pilihan Anda:

- **Download dan kembangkan secara lokal**: Ekspor kode yang dihasilkan sebagai **file
  ZIP** dan impor ke editor kode Anda.
- **Kirim ke GitHub**: Integrasikan kode dengan proses pengembangan dan
  deployment yang ada dengan mengirimkannya ke **repositori GitHub**.

## Fitur utama

Google AI Studio menyertakan beberapa fitur untuk membuat proses pembangunan menjadi intuitif dan visual:

- **Buat dan lakukan iterasi pada aplikasi full stack**: Buat aplikasi full stack hanya dengan
  perintah dan lakukan iterasi melalui chat atau **mode anotasi**. Mode anotasi
  memungkinkan Anda menandai bagian mana pun dari UI aplikasi dan menjelaskan
  perubahan yang Anda inginkan.
- **Membagikan dan men-deploy aplikasi**: Anda dapat membagikan kreasi Anda kepada orang lain untuk berkolaborasi atau memamerkan hasil karya Anda. Saat berbagi, panggilan API akan mengurangi batas penggunaan Anda. Jika Anda menggunakan model berbayar, biaya mungkin berlaku. Kemudian, saat aplikasi Anda siap, deploy ke Cloud Run.
- **Galeri aplikasi**: Galeri Aplikasi menyediakan library visual ide project.
  Anda dapat menjelajahi berbagai kemungkinan yang dapat dilakukan Gemini, melihat pratinjau aplikasi secara instan, dan mengombinasikannya untuk menjadikannya milik Anda.

## Men-deploy atau mengarsipkan aplikasi

Setelah aplikasi Anda siap, Anda dapat men-deploy-nya:

- **Cloud Run**: men-deploy aplikasi Anda sebagai layanan yang dapat diskalakan.
  Harga untuk [Google Cloud Run](https://cloud.google.com/run?hl=id) dapat berlaku berdasarkan
  penggunaan. Untuk mempelajari deployment lebih lanjut, lihat
  [Men-deploy dari Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=id).
- **GitHub**: mengekspor project Anda ke repositori GitHub.

## Batasan

Bagian ini mencantumkan batasan mode build saat ini di Google AI Studio.

### Pengelolaan Kunci API

Saat Anda membuat aplikasi baru yang menggunakan Gemini API, AI Studio akan otomatis
mengonfigurasi kunci Gemini API Anda sebagai rahasia di lingkungan sisi server aplikasi.
Anda dapat melihat dan mengelola kunci ini di panel **Secrets**.

- **Penyiapan otomatis**: `GEMINI_API_KEY` Anda disiapkan untuk Anda — tidak diperlukan konfigurasi manual untuk mulai membangun.
- **Khusus sisi server**: Kunci API disisipkan ke runtime sisi server dan tidak pernah disertakan dalam kode sisi klien.
- **Aplikasi yang sudah ada**: Untuk aplikasi yang dibuat sebelum 14 Mei 2026, agen akan
  mengupgrade integrasi Gemini API Anda secara otomatis ke pendekatan
  sisi server yang direkomendasikan saat Anda mengubah fitur Gemini aplikasi tersebut pada waktu berikutnya.

### Deployment di luar Google AI Studio

- **Cloud Run**: Saat Anda men-deploy ke Cloud Run dari AI Studio, kunci API Anda disertakan dengan aman di lingkungan sisi server. Aplikasi yang di-deploy akan menggunakan kunci API Anda untuk semua panggilan Gemini API pengguna.
- **Download ZIP**: Jika Anda mendownload aplikasi sebagai file ZIP untuk menjalankannya di tempat lain, Anda harus menyiapkan `GEMINI_API_KEY`variabel lingkungan di lingkungan hosting. Karena panggilan Gemini API aplikasi Anda dilakukan dari
  kode sisi server, kunci tidak diekspos ke pengguna akhir.

### Error saat berbagi aplikasi

Jika Anda membagikan aplikasi dan pengguna akhir Anda mengalami error **403 Akses Dibatasi**
saat menggunakan URL yang dibagikan, hal ini mungkin disebabkan oleh salah satu hal berikut:

- **Ekstensi browser**: ekstensi privasi seperti Privacy Badger dapat memblokir aplikasi. Nonaktifkan ekstensi untuk menghindari error.
- **Masalah build**: mungkin ada masalah dengan kode saat ini. Minta
  agen untuk "memperbaiki masalah build dengan kode saat ini", lalu bagikan ulang
  URL.

## FAQ

### Apa itu Build di AI Studio?

AI Studio Build adalah platform yang dirancang untuk membantu Anda mengubah perintah sederhana menjadi aplikasi berteknologi AI yang siap produksi menggunakan Gemini. Deskripsikan apa yang ingin Anda buat dengan perintah, dan Gemini akan membuat aplikasi untuk Anda. Anda juga dapat menjelajahi galeri kami untuk melihat kemungkinan yang dapat dilakukan dengan Gemini API, dan me-remix aplikasi untuk menjadikannya milik Anda.

### Bagaimana cara Build menangani kunci Gemini API saya?

Saat Anda membuat aplikasi yang menggunakan Gemini API, AI Studio akan otomatis
menyiapkan kunci Gemini API Anda sebagai rahasia sisi server. Panggilan Gemini API aplikasi Anda dilakukan dari kode sisi server menggunakan kunci ini, sehingga kunci ini tidak pernah diekspos di browser. Anda dapat melihat kunci API di panel **Secrets** di
Settings.

### Apakah kunci API saya terekspos saat membagikan aplikasi?

Tidak. Kunci API Anda disimpan sebagai rahasia sisi server dan tidak pernah disertakan dalam kode sisi klien. Saat Anda membagikan aplikasi, pengguna lain dapat menggunakannya, tetapi mereka tidak dapat melihat kunci API Anda.

Saat membagikan aplikasi Anda kepada orang lain, panggilan API dihitung dalam batas penggunaan Anda.
Jika Anda menggunakan model berbayar, biaya mungkin berlaku. AI Studio akan memberi tahu Anda
selama penyiapan dan sebelum Anda membagikan jika aplikasi Anda dapat menimbulkan biaya.

### Siapa yang dapat melihat aplikasi saya?

Secara default, aplikasi Anda bersifat pribadi. Anda dapat membagikan aplikasi Anda kepada pengguna lain agar mereka dapat menggunakannya. Pengguna yang Anda ajak berbagi aplikasi dapat melihat kodenya dan membuat fork untuk tujuan mereka sendiri. Jika Anda membagikan aplikasi dengan izin edit, pengguna lain dapat mengedit kode aplikasi Anda.

### Dapatkah saya menjalankan aplikasi di luar AI Studio?

Ya. Anda dapat men-deploy aplikasi ke
[Cloud Run](https://cloud.google.com/run?hl=id) dari AI Studio, yang
memberi aplikasi Anda URL publik dengan kunci API yang dikonfigurasi secara aman di
lingkungan sisi server. Anda juga dapat mendownload aplikasi sebagai file ZIP dan
menghostingnya di tempat lain — Anda harus menyetel variabel
lingkungan `GEMINI_API_KEY` di lingkungan hosting Anda. Karena panggilan Gemini API dilakukan dari kode sisi server, kunci Anda tetap aman.

Untuk mempelajari opsi deployment lebih lanjut, lihat [Men-deploy dari Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=id).

### Dapatkah saya mengembangkan aplikasi secara lokal dengan alat saya sendiri, lalu membagikannya di sini?

Fungsi ini belum tersedia. Kami senang dapat mendukung lebih banyak kasus penggunaan aplikasi pada masa mendatang. Berikan masukan kepada kami jika Anda memiliki sesuatu yang spesifik.

### Bagaimana cara menggunakan database atau penyimpanan lain dengan aplikasi saya?

Aplikasi AI Studio adalah aplikasi standar yang berjalan dalam container Cloud Run. Anda dapat
menggunakan solusi penyimpanan apa pun yang dapat Anda hubungkan melalui jaringan, selama
tidak ada firewall yang mencegah akses dari rentang IP dinamis.

Kami sedang berupaya menambahkan dukungan langsung untuk penyimpanan pada masa mendatang, yang dapat Anda konfigurasi langsung dalam AI Studio.

### Bagaimana cara mengakses mikrofon, webcam, dan Navigator API lainnya?

Untuk memastikan bahwa penonton mengetahui penggunaan webcam atau perangkat lain oleh aplikasi, kami mewajibkan pengesahan tambahan sebelum aplikasi dapat mengakses [Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) ini.
Pembuat aplikasi dapat menambahkan permintaan izin ini ke file
`metadata.json` aplikasi mereka. Contoh:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Nilai yang didukung untuk `requestFramePermissions` adalah bagian dari
[fitur yang dikontrol kebijakan](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md) standar.

### Bagaimana cara menggunakan GitHub dengan aplikasi saya?

Integrasi GitHub AI Studio memungkinkan Anda membuat repositori untuk pekerjaan Anda dan meng-commit perubahan terbaru. Saat ini kami tidak mendukung penarikan perubahan jarak jauh.

### Dapatkah saya memberikan akses edit ke aplikasi saya kepada pengguna lain?

Fitur ini belum didukung, tetapi akan segera tersedia.

### Mengapa aplikasi saya ditandai karena pelanggaran kebijakan?

Kami memiliki sistem yang secara otomatis meninjau aplikasi untuk memastikan aplikasi tersebut mematuhi kebijakan kami. Jika kami mendapati bahwa suatu aplikasi melanggar kebijakan kami, aplikasi tersebut akan dihapus dari AI Studio. Pelanggaran kebijakan dapat mencakup, tetapi tidak terbatas pada, hal-hal berikut:

- Aplikasi yang berisi malware, phishing, atau peniruan identitas
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan gambar pelecehan seksual terhadap anak-anak
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan pelecehan
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan ujaran kebencian
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan perdagangan manusia
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan konten seksual vulgar
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan kekerasan dan adegan sadis
- Aplikasi yang menampilkan atau mendistribusikan konten yang melanggar kebijakan konten berbahaya atau berbahaya

Jika aplikasi Anda ditandai karena pelanggaran kebijakan, dan Anda yakin hal ini merupakan kekeliruan, Anda dapat mengajukan banding. Pelanggaran berulang terhadap kebijakan kami dapat mengakibatkan penghentian akses Anda ke AI Studio.

### Apa tanggung jawab saya sebagai developer aplikasi?

Sebagai pengingat, sebagai pemilik aplikasi, Anda bertanggung jawab atas
perilakunya dan semua data yang ditanganinya. Hal ini mencakup:

- **Kepatuhan Hukum dan Hak Pihak Ketiga:** Memastikan aplikasi Anda mematuhi semua hukum dan peraturan yang berlaku serta tidak melanggar hak orang lain, termasuk hak atas kekayaan intelektual dan hak privasi.
- **Pemantauan Konten:** Kepatuhan terhadap persyaratan tambahan dapat berlaku untuk
  layanan lain yang digunakan oleh aplikasi Anda. Misalnya,
  [Persyaratan Layanan Google Cloud](https://cloud.google.com/terms?hl=id),
  yang berlaku untuk Firestore, mewajibkan pelanggan yang menghosting konten pihak ketiga untuk
  memublikasikan kebijakan yang menentukan konten apa yang dilarang (misalnya, konten ilegal) dan memantau keberadaan konten ilegal tersebut.
- **Penerapan yang Aman:** Menerapkan alat pengamanan dan moderasi yang diperlukan untuk mencegah penyalahgunaan aplikasi Anda.

Perhatikan [pembatasan penggunaan](https://ai.google.dev/gemini-api/terms?hl=id#use-restrictions)
dalam Persyaratan Layanan.

### Persyaratan apa yang berlaku untuk aplikasi di galeri aplikasi di AI Studio?

[Persyaratan Layanan Tambahan Gemini API](https://ai.google.dev/gemini-api/terms?hl=id) berlaku untuk penggunaan aplikasi yang ditampilkan di galeri aplikasi di AI Studio, kecuali dinyatakan lain.

## Langkah berikutnya

- [Mengembangkan Aplikasi Full-Stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=id) (web)
- [Membangun Aplikasi Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=id)
- Lihat contoh di [Galeri Aplikasi](https://aistudio.google.com/apps?source=showcase&hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
