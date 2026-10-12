---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=id
fetched_at: 2026-10-12T06:54:34.896011+00:00
title: "Agen di playground AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen di playground AI Studio

Google AI Studio Playground menyediakan antarmuka visual untuk membuat prototipe dan mempelajari cara membuat agen terkelola tanpa harus membuat dan menulis panggilan API.

Untuk memulai, buka tab **Playground** di panel navigasi Google AI Studio, dan alihkan tombol ke **Agents**.

## Template bawaan

Tab **Agents** memiliki serangkaian template yang telah mengonfigurasi Agen Antigravity dasar dengan menetapkan konfigurasi alat dan lingkungan. Semua template bersifat open source dan dipublikasikan di
repositori [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Mempelajari template ini adalah cara yang bagus untuk mempelajari cara membuat dan menyusun agen terkelola Anda sendiri.

Misalnya, saat Anda memilih template AI Radio, semua alat yang diizinkan akan diaktifkan, dan file `AGENTS.md` serta keterampilan khusus untuk produksi acara radio akan ditautkan. Anda dapat melihat setelan ini di UI Playground di bagian **Environment**, dengan mengklik tombol **Sources**.

## Konfigurasi alat

Di bagian Agent settings di Playground, Anda dapat mengalihkan akses ke alat bawaan berikut:

- **Google Search:** Mengakses web terbuka untuk grounding informasi real-time.
- **URL Context:** Mengambil dan mengurai konten teks URL halaman web tertentu.
- **Code Execution:** Menjalankan perintah Bash dan Python langsung dalam lingkungan sandbox terisolasi.
- **Filesystem Tools:** Membaca, menulis, mencantumkan, dan menghapus file di dalam ruang kerja.

## Konfigurasi Lingkungan

Agen terkelola berjalan dalam sandbox Linux efemeral yang aman (lingkungan) yang menyediakan ruang kerja dan alat yang diperlukan untuk beroperasi. Untuk mempelajari lebih lanjut, lihat panduan [lingkungan agen terkelola](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id).

### Mengontrol perilaku agen

Perilaku, persona, dan kemampuan agen sebagian besar ditentukan oleh file yang ada di lingkungannya. Agen akan otomatis mendeteksi dan memuat konfigurasi dari folder `.agents` khusus:

- **`AGENTS.md`**: Dimuat sebelumnya ke dalam konteks agen untuk menentukan persona dan petunjuk sistem.
- **`SKILL.md`**: Terletak di folder keterampilan masing-masing (misalnya, `.agents/skills/my-skill/SKILL.md`) untuk menentukan kemampuan dan alur kerja tertentu.

### Menyediakan Lingkungan

Anda dapat mengonfigurasi lingkungan yang akan digunakan oleh agen dengan memasang file ke lingkungan sebelum memulai sesi. Anda dapat membuat lingkungan baru dengan memasang sumber, atau memulihkan lingkungan sebelumnya:

- **Untuk membuat lingkungan baru**, klik **Add Sources** di panel Environment settings dan pilih dari jenis sumber berikut:

| Jenis sumber | Deskripsi | Jalur pemasangan |
| --- | --- | --- |
| **File Sebaris** | Menulis atau menempel file konfigurasi, set data tiruan, atau skrip utilitas (hingga 100 KB) langsung ke UI Playground. | Jalur tujuan yang ditentukan pengguna (misalnya, `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Memasang bucket Cloud Storage publik atau pribadi.  Bucket pribadi memerlukan token Bearer OAuth 2.0 standar. Untuk mengetahui informasi selengkapnya, lihat [Sumber pribadi](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#private-sources). | Memetakan jalur bucket GCS (misalnya, `gs://your-bucket-name/data/`) ke direktori ruang kerja (misalnya, `/workspace/data/`). |
| **Repositori GitHub** | Meng-clone codebase publik atau pribadi.  Repositori pribadi memerlukan Autentikasi dasar dengan Token Akses Pribadi (PAT) GitHub Anda. Untuk mengetahui informasi selengkapnya, lihat [Sumber pribadi](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#private-sources). | Di-clone langsung ke `/workspace/` (biasanya di bagian `/workspace/<repo-name>`). |

- **Untuk memulihkan lingkungan sebelumnya**, Anda dapat [menggunakan kembali ID lingkungan yang ada](#reusing-an-existing-environment-id) untuk meng-clone dan membuat fork statusnya yang sama persis.

### Menggunakan kembali ID lingkungan yang ada

Jika sudah menghabiskan waktu untuk menyiapkan lingkungan sandbox, Anda tidak perlu memulai dari awal. Untuk menggunakan lingkungan yang ada:

1. Buka panel Environments di AI Studio dan alihkan **Type** ke **Existing**
2. Masukkan **Environment ID** (misalnya, `env_abc123`)

Untuk mengetahui informasi selengkapnya, lihat [Mengonfigurasi lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#configure-an-environment). Anda juga dapat mengambil Environment ID sesi saat ini dari tab Environment di UI.

Setelah Anda mengirim pesan pertama ke agen, konfigurasi lingkungan akan ditetapkan untuk sesi tersebut. Anda tidak dapat memasang sumber baru atau mengubah daftar yang diizinkan jaringan saat interaksi sedang berjalan aktif.

## Mendownload lingkungan

Setelah lingkungan dibuat, Anda dapat mendownload snapshot lingkungan kapan saja menggunakan tombol **Download** di Environment settings AI Studio Playground untuk mengambil file lingkungan sebagai tarball.

## Pengelolaan Keamanan dan Biaya

### Mengelola Penggunaan Token

Tidak seperti permintaan chat standar yang menghasilkan satu output, Agen Antigravity menjalankan alur kerja otonom. Agen ini merencanakan, menjalankan kode, mengamati hasil, dan melakukan iterasi. Artinya, satu perintah dapat menghasilkan penggunaan token tanpa batas.

Untuk mengelola biaya, **berikan kriteria penghentian yang jelas dalam perintah Anda dan batasi tugas untuk agen**. Contoh yang baik adalah perintah seperti *Tinjau permintaan pull dan berhenti setelah Anda membuat ringkasan markdown.
Jangan mencoba menulis perbaikan sendiri*.

### Biaya Tambahan

Secara default, semua template agen di Playground memiliki akses ke layanan Gemini API dan dapat melakukan panggilan API dari lingkungan untuk memenuhi permintaan. Hal ini dapat dikenai biaya tambahan yang tidak akan tercermin dalam penggunaan token.

Demikian pula, jika Anda menambahkan layanan eksternal lainnya, agen dapat dikenai biaya tambahan dengan memanggil layanan ini atas nama Anda.

### Daftar yang Diizinkan Jaringan

Secara default, di AI Studio, semua permintaan jaringan keluar dari dalam lingkungan sandbox agen Anda dikontrol dan dibatasi secara ketat untuk memastikan keamanan. Untuk memberikan kemampuan kepada agen Anda untuk menjangkau API eksternal, layanan web, atau pengelola paket, Anda harus mendeklarasikannya secara eksplisit:

1. Buka panel Environments di AI Studio.
2. Pilih tombol **rules** di samping **Network**.
3. Di panel **Network configuration**, klik **Add to allowlist** dan isi detail yang relevan:
   - **Domain Restriction:** Hanya domain atau pola karakter pengganti tertentu yang ditambahkan ke daftar yang dapat diakses oleh mesin virtual agen. Misalnya, Anda dapat memasukkan domain yang sama persis seperti `api.github.com` atau pola luas seperti `*.googleapis.com`.
   - **Add HTTP Header and Token Injection:** Gunakan opsi **Add HTTP header** untuk menyuntikkan kredensial yang diperlukan (seperti token API) secara aman untuk domain tertentu. Kredensial ini diteruskan dengan aman melalui proxy keluar dan tidak pernah diekspos secara langsung sebagai teks mentah di dalam sandbox agen.

Selalu berhati-hatilah saat menambahkan domain ke daftar yang diizinkan. Memberikan akses agen ke layanan yang diautentikasi berarti agen dapat bertindak atas nama Anda, yang dapat menyebabkan tindakan yang tidak diinginkan jika tidak dipantau dengan cermat.

### Praktik terbaik kredensial

Jika alur kerja Anda mengharuskan agen untuk melakukan autentikasi dengan layanan eksternal, Anda bertanggung jawab untuk menyediakan dan menentukan cakupan kredensial tersebut. Ikuti panduan ini untuk mengurangi risiko:

- **Gunakan kredensial hak istimewa terendah:** Buat akun layanan atau kunci API hanya dengan izin yang diperlukan agen Anda. Hindari meneruskan kredensial dengan akses administratif atau luas.
- **Pilih token yang memiliki masa aktif singkat:** Jika memungkinkan, gunakan kredensial atau token yang memiliki batas waktu yang akan berakhir masa berlakunya, bukan kunci API yang memiliki masa aktif lama.
- **Asumsikan akses penuh:** Agen dapat menggunakan kredensial apa pun yang dapat diaksesnya untuk menyelesaikan tugas yang telah Anda berikan. Hanya berikan kredensial yang cakupan aksesnya sepenuhnya ingin Anda berikan.
- **Rotasi kredensial secara rutin:** Perlakukan kredensial yang dibagikan dengan agen dengan cara yang sama seperti Anda memperlakukan kredensial terprogram; rotasi secara rutin.

### Menghubungkan alat dan API eksternal

Anda dapat menghubungkan alat dan API eksternal (seperti server Model Context Protocol / MCP) untuk memperluas kemampuan agen. Saat melakukannya:

- Hanya hubungkan alat dari sumber yang Anda percaya. Alat yang berbahaya atau ditulis dengan buruk dapat mengekspos data atau melakukan tindakan yang tidak diinginkan.
- Konfigurasi alat dengan izin minimum yang diperlukan untuk kasus penggunaan Anda. Jika alat mendukung mode hanya baca, sebaiknya gunakan mode tersebut kecuali jika penulisan benar-benar diperlukan.
- Sebelum menghubungkan alat ke sumber data produksi, uji alat tersebut terhadap data sampel atau sintetis untuk memverifikasi bahwa agen menggunakannya seperti yang diharapkan.

### Pengawasan manusia

Agen dapat melakukan penalaran, perencanaan, dan menjalankan alur kerja multi-langkah dengan tingkat otonomi yang tinggi. Meskipun efektif, hal ini juga berarti Anda harus menerapkan pengawasan yang sesuai, terutama untuk tugas yang mengubah data atau berinteraksi dengan sistem eksternal.

Selalu verifikasi output penting seperti kode yang dihasilkan, transformasi data, atau perubahan konfigurasi sebelum Anda men-deploy-nya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-08-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-08-19 UTC."],[],[]]
