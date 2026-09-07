---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id
fetched_at: 2026-09-07T05:48:30.826924+00:00
title: "Log dan set data \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Log dan set data

Dalam panduan ini, Anda akan mempelajari cara
melihat log dari penggunaan Gemini API di dasbor Google AI Studio
untuk lebih memahami perilaku model dan cara pengguna berinteraksi dengan
aplikasi Anda. Gunakan logging untuk mengamati, men-debug, dan *secara opsional membagikan masukan penggunaan
kepada Google untuk membantu meningkatkan kualitas Gemini di berbagai kasus penggunaan developer*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=id)

Semua panggilan API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent`, dan panggilan API [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=id), kecuali Agen Terkelola, didukung. Hal ini mencakup panggilan yang dilakukan melalui endpoint [kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id).

## Mengonfigurasi logging project

Secara default, API menyimpan semua objek interaksi (`store=true`) untuk
menyederhanakan penggunaan fitur pengelolaan status sisi server. Sebaliknya, Generate Content API tidak menyimpan permintaan secara default, dan memerlukan penyimpanan diaktifkan per permintaan atau di tingkat project dari AI Studio.

Di [AI Studio](https://aistudio.google.com/logs?hl=id) Google, Anda dapat mengaktifkan atau menonaktifkan logging untuk semua project atau untuk project tertentu dan mengubah preferensi ini kapan saja melalui panel **Setelan** di halaman [Log dan Kumpulan Data](https://aistudio.google.com/logs?hl=id). Logging dapat diaktifkan atau dinonaktifkan secara terpisah untuk `generateContent` API dan [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=id) API untuk mengubah perilaku penyimpanan default untuk project.

### Logging tingkat permintaan

Perilaku penyimpanan dan logging berbeda menurut API:

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id):** Menyimpan permintaan secara default (`store=true`) untuk menyederhanakan pengelolaan status sisi server.
- **Generate Content API (`generateContent`):** Tidak menyimpan permintaan secara default (`store=false`).

Berikut cara menetapkan properti `store`:

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Melihat log project di AI Studio

1. Buka halaman Logs di [AI Studio](https://aistudio.google.com/logs?hl=id).
2. Pilih project dari menu drop-down.
3. Log akan muncul dalam tabel dalam urutan kronologis terbalik untuk Interactions API, jika ada.
4. Untuk mengamati log project untuk Generate Content API, aktifkan terlebih dahulu di [panel setelan](#configure-logging).

Klik entri untuk melihat pratinjau payload. Anda dapat memeriksa perintah dan respons lengkap dari Gemini, serta konteks dari pernyataan sebelumnya. Untuk permintaan **Interactions API**, log juga menyertakan link
langsung ke `previous_interaction_id`.

## Mengonfigurasi retensi penyimpanan project

Log akan berakhir dan ditandai untuk dihapus setelah periode retensi default selama 55 hari (kecuali jika [disimpan ke set data](#create), yang tidak akan berakhir).
Anda dapat mengonfigurasi periode retensi log project hingga maksimum 7, 14, 28, atau 55 hari.

## Membuat dan membagikan set data

Anda dapat menyimpan log ke set data untuk mengelola dan mengekspornya secara lebih efektif.

- Dari [halaman Log](https://aistudio.google.com/logs?hl=id), temukan panel filter di bagian atas untuk memilih properti yang akan difilter.
- Dari tampilan yang difilter, gunakan kotak centang untuk memilih semua atau masing-masing log.
- Klik tombol **Buat set data** yang muncul di bagian atas daftar.
- Beri nama dan deskripsi opsional untuk set data baru Anda.
- Anda akan melihat set data yang baru saja dibuat dengan kumpulan log yang telah dikurasi.
- Ekspor set data Anda untuk analisis lebih lanjut sebagai file CSV, JSONL, atau ke Google Spreadsheet.

Set data dapat berguna untuk sejumlah kasus penggunaan yang berbeda.

- **Susun set tantangan:** Dorong peningkatan di masa mendatang yang menargetkan area tempat Anda ingin AI ditingkatkan.
- **Menyusun set sampel:** Misalnya, sampel dari penggunaan nyata untuk menghasilkan respons dari model lain, atau kumpulan kasus ekstrem untuk pemeriksaan rutin sebelum deployment.
- **Set evaluasi:** Set yang mewakili penggunaan nyata di seluruh kemampuan penting, untuk perbandingan di seluruh model atau iterasi petunjuk sistem lainnya.

Anda dapat berkontribusi pada riset dan pengembangan Gemini dengan memilih untuk membagikan set data Anda kepada Google sebagai contoh demonstrasi.

## Batasan

Pencatatan saat ini tidak didukung untuk hal berikut:

- Model Imagen dan Veo
- Model embedding Gemini
- Model Gemini Robotics
- Input yang berisi video, GIF, atau PDF
- Agen Pratinjau Publik di Gemini API

## Langkah berikutnya

- **Membuat prototipe dengan histori sesi:** Gunakan [Build AI Studio](https://aistudio.google.com/apps?hl=id) untuk melakukan vibe coding aplikasi dan menambahkan kunci API Anda untuk mengaktifkan histori log Gemini API untuk fitur AI.
- **Menjalankan ulang log dengan Gemini Batch API:** Gunakan set data untuk pengambilan sampel respons dan evaluasi model atau logika aplikasi dengan menjalankan ulang log menggunakan [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-22 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-22 UTC."],[],[]]
