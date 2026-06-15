---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=id
fetched_at: 2026-06-15T06:32:11.026639+00:00
title: "Integrasi partner dan library \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Integrasi partner dan library

Panduan ini menguraikan strategi arsitektur untuk membangun library, platform, dan gateway di atas Gemini API. Dokumen ini menjelaskan secara mendetail pertimbangan teknis
antara penggunaan SDK GenAI resmi, Direct API (REST/gRPC), dan
lapisan kompatibilitas OpenAI.

Gunakan panduan ini jika Anda membuat alat untuk developer lain, seperti
framework open source, gateway perusahaan, atau agregator SaaS, dan perlu
mengoptimalkan kebersihan dependensi, ukuran paket, atau paritas fitur.

## Apa itu integrasi partner?

Partner adalah siapa saja yang membangun integrasi antara Gemini API dan developer pengguna akhir. Kami mengategorikan partner ke dalam empat arketipe. Mengidentifikasi mana yang paling cocok dengan Anda akan membantu Anda memilih jalur integrasi yang tepat.

#### Framework ekosistem

- **Siapa Anda:** Pengelola framework open source (misalnya, LangChain, LlamaIndex, Spring AI) atau klien khusus bahasa.
- **Sasaran Anda:** Kompatibilitas luas. Anda ingin pustaka Anda berfungsi di lingkungan apa pun yang dipilih pengguna tanpa memaksakan konflik.

#### Platform runtime dan edge

- **Siapa Anda:** Platform SaaS, Gateway AI, atau penyedia infrastruktur cloud (misalnya, Vercel, Cloudflare, Zapier) tempat eksekusi kode terjadi di lingkungan yang dibatasi.
- **Sasaran Anda:** Performa. Anda memerlukan latensi rendah, ukuran paket minimal, dan
  cold start yang cepat.

#### Agregator

- **Siapa Anda:** Platform, proxy, atau "Taman Model" internal yang menormalisasi akses di berbagai penyedia LLM (misalnya, OpenAI, Anthropic, Google) ke dalam satu antarmuka.
- **Sasaran Anda:** Portabilitas dan keseragaman.

#### Gateway perusahaan

- **Siapa Anda:** Tim Engineering Platform internal di perusahaan besar yang membangun "Jalur Ideal" untuk ratusan developer internal.
- **Sasaran Anda:** Standardisasi, tata kelola, dan autentikasi terpadu.

## Perbandingan sekilas

**Praktik terbaik global:** Semua partner harus mengirim header [`x-goog-api-client`](#client-id)terlepas dari jalur yang dipilih.

| Jika Anda... | Jalur yang direkomendasikan | Manfaat utama | Kompromi utama | Praktik terbaik |
| --- | --- | --- | --- | --- |
| **Gateway perusahaan, framework ekosistem** | **[Google GenAI SDK](#genai-sdk)** | **Paritas & kecepatan Platform Agen Gemini Enterprise.** Penanganan bawaan untuk jenis, autentikasi, dan fitur kompleks (misalnya, upload file). Migrasi yang lancar ke Google Cloud. | **Bobot dependensi.** Ketergantungan transitif bisa jadi kompleks dan di luar kendali Anda. Terbatas untuk bahasa yang didukung (Python/Node/Go/Java). | **Mengunci versi.** Sematkan versi SDK di image dasar internal Anda untuk memastikan stabilitas di seluruh tim. |
| **Framework ekosistem, platform edge, dan agregator** | **[Direct API](#rest)**  *(REST / gRPC)* | **Tanpa dependensi.** Anda mengontrol klien HTTP dan ukuran paket yang tepat. Akses penuh ke semua fitur API dan model. | **Overhead developer yang tinggi.** Struktur JSON dapat memiliki banyak lapisan dan memerlukan validasi manual serta pemeriksaan jenis yang ketat. | **Gunakan spesifikasi OpenAPI.** Mengotomatiskan pembuatan jenis menggunakan spesifikasi resmi kami, bukan menuliskannya secara manual. |
| **Agregator yang menggunakan SDK OpenAI yang hanya memerlukan alur kerja berbasis teks**  *(Mengoptimalkan portabilitas lama)* | **[Kompatibilitas OpenAI](#openai)** | **Portabilitas instan.** Menggunakan kembali kode atau library yang kompatibel dengan OpenAI. | **Batas fitur.** Fitur khusus model (Video native, Pengekasan) mungkin tidak tersedia. | **Rencana migrasi.** Gunakan ini untuk validasi cepat, tetapi rencanakan untuk mengupgrade ke Direct API untuk fitur API lengkap. |

## Integrasi Google GenAI SDK

Untuk framework, penerapan [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=id)
sering kali merupakan cara yang paling sederhana, mengingat jumlah baris kode yang paling sedikit dalam bahasa yang didukung.

Untuk tim platform internal, hasil utama Anda sering kali berupa "jalur emas" yang memungkinkan engineer produk bergerak cepat sekaligus mematuhi kebijakan keamanan.

**Manfaat:**

- **Antarmuka terpadu untuk migrasi Gemini Enterprise Agent Platform:** Developer internal sering kali membuat prototipe menggunakan Kunci API (Gemini API) dan men-deploy ke Gemini Enterprise Agent Platform (IAM) untuk kepatuhan produksi. SDK mengabstraksi perbedaan autentikasi ini.
  Demikian pula untuk framework, Anda dapat menerapkan satu jalur kode dan mendukung dua set pengguna.
- **Helper sisi klien:** SDK menyertakan utilitas idiomatik yang mengurangi
  boilerplate untuk tugas yang kompleks.
  - *Contoh:* Mendukung objek gambar `PIL` secara langsung dalam perintah, panggilan fungsi otomatis, dan jenis yang komprehensif.
- **Akses fitur pada hari peluncuran:** Fitur API baru tersedia pada waktu peluncuran melalui SDK.
- **Dukungan pembuatan kode yang ditingkatkan:** Penginstalan SDK lokal mengekspos definisi jenis dan string dokumen ke asisten coding (misalnya, Cursor, Copilot).
  Konteks ini meningkatkan akurasi pembuatan kode dibandingkan dengan membuat permintaan REST mentah.

**Kompromi:**

- **Bobot & kompleksitas dependensi:** SDK memiliki dependensinya sendiri, yang dapat meningkatkan ukuran bundle dan berpotensi menimbulkan risiko rantai pasokan.
- **Pembuatan Versi:** Fitur API baru sering kali disematkan ke versi SDK minimum.
  Anda mungkin perlu mengirimkan update kepada pengguna untuk mengakses fitur atau model baru, yang dalam beberapa kasus mungkin memerlukan perubahan pada dependensi transitif yang memengaruhi pengguna Anda.
- **Batasan protokol:** SDK hanya mendukung HTTPS untuk API utama dan
  WebSockets (WSS) untuk Live API. gRPC tidak didukung menggunakan
  klien SDK tingkat tinggi.
- **Dukungan bahasa:** SDK mendukung versi bahasa *saat ini*. Jika Anda perlu mendukung versi EOL (misalnya, Python 3.9), Anda harus mempertahankan fork.

**Praktik terbaik:**

- **Mengunci versi:** Sematkan versi SDK di image dasar internal Anda untuk
  memastikan stabilitas di seluruh tim.

## Integrasi API langsung

Jika Anda mendistribusikan library kepada ribuan developer, menjalankan di lingkungan yang terbatas, atau membangun agregator yang memerlukan fitur canggih Gemini, Anda mungkin perlu berintegrasi dengan API secara langsung menggunakan REST atau gRPC.

**Manfaat:**

- **Akses fitur lengkap:** Tidak seperti lapisan kompatibilitas OpenAI, penggunaan
  API secara langsung memungkinkan fitur khusus Gemini, seperti mengupload ke File
  API, membuat caching konten, dan menggunakan Live API dua arah.
- **Dependensi minimal:** Di lingkungan tempat dependensi sensitif karena ukuran atau biaya audit. Menggunakan API secara langsung melalui
  library standar seperti `fetch` atau melalui wrapper seperti `httpx` memastikan library Anda tetap ringan.
- **Agnostik bahasa:** Ini adalah satu-satunya jalur untuk bahasa yang tidak tercakup oleh SDK, seperti Rust, PHP, dan Ruby, karena tidak ada batasan bahasa.
- **Performa:** Direct API memiliki overhead inisialisasi nol, sehingga meminimalkan cold start dalam fungsi serverless.

**Kompromi:**

- **Implementasi Platform Agen Gemini Enterprise secara manual:** Tidak seperti SDK, penggunaan API secara langsung tidak otomatis menangani perbedaan autentikasi antara AI Studio (Kunci API) dan Platform Agen Gemini Enterprise (IAM). Anda harus menerapkan handler autentikasi
  terpisah jika ingin mendukung kedua lingkungan.
- **Tidak ada jenis atau helper bawaan:** Anda tidak akan mendapatkan penyelesaian kode atau pemeriksaan waktu kompilasi untuk objek permintaan kecuali jika Anda menerapkannya sendiri. Tidak ada "pembantu" klien (misalnya, konverter fungsi ke skema), jadi Anda harus menulis logika ini secara manual sendiri.

**Praktik terbaik**

Kami mengekspos spesifikasi yang dapat dibaca mesin yang dapat Anda gunakan untuk membuat definisi jenis untuk library Anda, sehingga Anda tidak perlu menuliskannya secara manual. Download spesifikasi selama proses build, buat jenis, dan kirim kode yang dikompilasi.

- **Endpoint:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integrasi OpenAI SDK

Jika Anda adalah platform yang memprioritaskan skema terpadu (OpenAI Chat Completions) daripada fitur khusus model, ini adalah cara tercepat Anda.

**Manfaat:**

- **Gesekan rendah:** Anda sering kali dapat menambahkan dukungan Gemini dengan mengubah `baseURL`
  dan `apiKey`. Cara ini adalah cara cepat untuk mengintegrasikan penerapan "Bawa Kunci Anda Sendiri", menambahkan dukungan Gemini tanpa menulis kode baru.
- **Batasan:** Jalur ini hanya direkomendasikan jika Anda dibatasi untuk
  OpenAI SDK dan tidak memerlukan fitur Gemini lanjutan seperti File API,
  atau menambahkan dukungan untuk alat seperti Perujukan dengan Penelusuran Google secara manual.

**Kompromi:**

- **Batasan fitur:** Lapisan kompatibilitas memberikan batasan pada kemampuan inti Gemini. Alat sisi server yang tersedia berbeda di setiap platform, dan mungkin memerlukan penanganan manual agar dapat berfungsi dengan alat Gemini API.
- **Overhead terjemahan:** Karena skema OpenAI tidak dipetakan 1:1 ke arsitektur Gemini, mengandalkan lapisan kompatibilitas menimbulkan beberapa kerumitan yang memerlukan pekerjaan penerapan tambahan untuk diselesaikan, seperti memetakan alat "penelusuran" pengguna ke alat platform yang tepat.
  Jika Anda memerlukan banyak sekali penanganan khusus, mungkin lebih baik menggunakan SDK atau API khusus untuk setiap platform.

**Praktik terbaik**

Jika memungkinkan, lakukan integrasi langsung dengan Gemini API. Namun, untuk kompatibilitas maksimum, pertimbangkan untuk menggunakan library yang mengetahui berbagai penyedia dan dapat menangani pemetaan alat dan pesan untuk Anda.

## Praktik terbaik untuk semua partner: identifikasi klien

Saat melakukan panggilan ke Gemini API sebagai platform atau library, Anda harus
mengidentifikasi klien menggunakan header `x-goog-api-client`.

Dengan begitu, Google dapat mengidentifikasi segmen traffic spesifik Anda, dan jika library Anda menghasilkan pola error tertentu, kami dapat menghubungi Anda untuk membantu men-debug.

Gunakan format `company-product/version` (misalnya, `acme-framework/1.2.0`).

### Contoh implementasi

### GenAI SDK

Dengan menyediakan klien API, SDK akan otomatis menambahkan header kustom Anda ke header internalnya.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Langkah berikutnya

- Buka [ringkasan library](https://ai.google.dev/gemini-api/docs/libraries?hl=id) untuk mempelajari
  SDK GenAI
- Jelajahi [referensi API](https://ai.google.dev/api?hl=id)
- Baca [panduan kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
