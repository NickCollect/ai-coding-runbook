---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=id
fetched_at: 2026-05-05T19:42:38.470462+00:00
title: "Menyiapkan asisten coding Anda dengan Gemini MCP dan Keterampilan \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menyiapkan asisten coding Anda dengan Gemini MCP dan Keterampilan

Asisten coding AI sangat canggih, tetapi memiliki batasan—data pelatihan terhenti pada tanggal tertentu, sehingga tidak ada fitur dan perubahan API baru. Tanpa akses ke dokumentasi khusus Gemini, agen mungkin menyarankan pola umum, bukan pendekatan yang dioptimalkan.

Untuk memastikan asisten coding Anda selalu menggunakan Gemini API yang terus berkembang dan penggunaan yang direkomendasikan, sebaiknya siapkan **Gemini Docs MCP** dan tingkatkan lingkungan Anda dengan **Gemini API Skills**. Meskipun alat ini dapat digunakan secara independen, alat ini dirancang untuk bekerja sama guna memberikan cakupan lengkap.

## Menghubungkan Gemini Docs MCP

Gemini menghosting server Model Context Protocol (MCP) publik di `https://gemini-api-docs-mcp.dev`. Menghubungkan agen coding Anda ke server ini akan memastikan bahwa semua kueri memiliki akses ke API terbaru, update kode, dan contoh konfigurasi optimal.

Jalankan perintah berikut di terminal agen atau root project untuk menginstal server:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Server ini menambahkan fungsi `search_documentation` yang dapat digunakan agen Anda untuk mengambil definisi API real-time dan pola integrasi dari file dokumentasi Gemini resmi.

## Menambahkan Keterampilan Pengembangan API

Keterampilan ini menyediakan **aturan dan praktik terbaik bawaan** (seperti menerapkan SDK yang benar dan versi model saat ini) langsung dalam konteks asisten Anda. Keterampilan ini berfungsi bersama dengan layanan Gemini Docs MCP: Jika Anda menginstal keduanya, keterampilan ini akan menggunakan layanan MCP untuk dokumentasi, tetapi meskipun tanpa MCP terinstal, keterampilan ini akan mengambil `llms.txt` dari `ai.google.dev` sebagai penggantian.

Untuk menginstal keterampilan ini, Anda dapat menggunakan salah satu alat yang didukung berikut. Petunjuk penginstalan untuk keduanya disediakan di bawah setiap modul keterampilan:

- **[skills.sh](https://skills.sh)**: Direkomendasikan. Standar terbuka untuk perilaku agen portabel.
- **[Context7](https://context7.com)**

### gemini-api-dev

Keterampilan dasar untuk pengembangan Gemini tujuan umum. Keterampilan ini menyediakan dokumentasi dan praktik terbaik untuk:

- Perutean perintah ke model saat ini (misalnya, Gemini 3.1 Pro/Flash) dan menghindari model yang tidak digunakan lagi
- Perintah multimodal, panggilan fungsi, output terstruktur, dan pola integrasi umum

#### Menginstal dengan skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Menginstal dengan Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Keterampilan untuk membangun aplikasi AI percakapan real-time dengan Gemini Live API. Keterampilan ini menyediakan dokumentasi dan praktik terbaik untuk:

- Koneksi WebSocket untuk streaming latensi rendah
- Streaming audio, video, dan teks
- Deteksi aktivitas suara dan dukungan barge-in

#### Menginstal dengan skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Menginstal dengan Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Keterampilan untuk membangun aplikasi dengan
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id). Interactions API adalah antarmuka terpadu untuk berinteraksi dengan model dan agen Gemini, yang dirancang untuk aplikasi agentic. Keterampilan ini mencakup:

- Pembuatan teks, chat multi-giliran, dan streaming
- Panggilan fungsi, output terstruktur, dan pembuatan gambar
- Eksekusi latar belakang dan agen Deep Research
- Pengelolaan status percakapan sisi server
- Pola Python dan TypeScript SDK

#### Menginstal dengan skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Menginstal dengan Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Memverifikasi penginstalan

Setelah menginstal, pastikan asisten coding Anda dapat terhubung ke server Gemini Docs MCP dan menggunakan keterampilan yang telah diinstal.

### 1. Memverifikasi perilaku agen

Cara paling andal untuk memverifikasi adalah dengan mengajukan pertanyaan teknis tentang Gemini API kepada agen Anda.

**Perintah:** "How do I use context caching with the Gemini API?"

Penyiapan yang berhasil akan:

- **Menyediakan kode yang akurat**: Merujuk metode Gemini tertentu seperti `cacheContent` atau `cachedContents.create` dari endpoint terbaru.
- **Menggunakan Alat MCP**: Menunjukkan bahwa alat ini terhubung ke **Server Gemini Docs MCP** atau menggunakan alat `search_documentation` untuk mengambil data.
- **Memanggil keterampilan yang dimuat**: Menampilkan indikator bahwa keterampilan ini "Using skill: gemini-api-dev" (jika mengandalkan wrapper sekunder).

### 2. Memverifikasi manifestasi &alat

Jika agen memberikan jawaban umum, gunakan perintah Discovery atau Status tertentu untuk lingkungan Anda guna memverifikasi bahwa Docs MCP atau keterampilan dimuat ke dalam memori.

| Lingkungan | Verifikasi MCP | Verifikasi Keterampilan |
| --- | --- | --- |
| **Claude Code** | Ketik `/mcp` di terminal untuk melihat server aktif dan alat `search_documentation`. | Ketik `/skills` di terminal untuk mencantumkan semua manifes aktif. |
| **Cursor** | Buka **Settings > Features > MCP**. Pastikan server "Connected". | Buka **Settings > Rules**. Pastikan keterampilan muncul di bagian "Agent Decides". |
| **Antigravity** | Periksa sidebar **Customizations > Connections** untuk mengetahui status MCP. | Ketik `/skills list` atau periksa sidebar **Customizations > Rules**. |
| **Gemini CLI** | Jalankan `gemini mcp list` atau gunakan `/mcp list`. | Jalankan `gemini skills list` atau gunakan perintah garis miring `/skills` dalam sesi. |
| **Copilot** | Ketik `@gemini /mcp` untuk mencantumkan konektor data aktif. | Ketik `@gemini /skills` (atau `/skills`) untuk melihat ekstensi aktif. |

## Pemecahan masalah

Jika agen Anda hanya memberikan informasi umum atau gagal mengenali metode khusus Gemini, periksa hal berikut:

### Agen tidak menemukan keterampilan

Sebagian besar agen mengindeks keterampilan hanya saat startup.

**Perbaikan:** Mulai ulang IDE (Cursor/VS Code) sepenuhnya atau keluar dan buka kembali agen berbasis terminal (Claude Code).

### Konflik global vs. lokal

Jika Anda menginstal dengan flag `--global`, agen Anda mungkin mengabaikannya dan lebih memilih aturan khusus project.

**Perbaikan:** Coba instal keterampilan langsung ke root project Anda tanpa flag global:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Resource

- [Keterampilan Gemini API di GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id)
- [Panduan memulai](https://ai.google.dev/gemini-api/docs/quickstart?hl=id)
- [Perpustakaan](https://ai.google.dev/gemini-api/docs/libraries?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
