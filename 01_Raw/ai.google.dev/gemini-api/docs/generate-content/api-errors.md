---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=id
fetched_at: 2026-09-21T05:53:05.508334+00:00
title: "Error API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Error API

Halaman ini memberikan referensi untuk kode error backend yang ditampilkan oleh `GenerateContent` API, menjelaskan format respons error gRPC, dan memberikan langkah-langkah pemecahan masalah.

## Kode error HTTP

Tabel berikut mencantumkan kode error backend umum, penjelasan penyebabnya, dan solusi yang direkomendasikan:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kode HTTP** | **Status** | **Deskripsi** | **Contoh** | **Solusi** |
| 400 | INVALID\_ARGUMENT | Isi permintaan salah format. | Ada kesalahan ketik, atau kolom wajib diisi yang tidak ada dalam permintaan Anda. | Lihat [referensi API](https://ai.google.dev/api?hl=id) untuk mengetahui format permintaan, contoh, dan versi yang didukung. Menggunakan fitur dari versi API yang lebih baru dengan endpoint yang lebih lama dapat menyebabkan error. |
| 400 | FAILED\_PRECONDITION | Paket gratis Gemini API tidak tersedia di negara Anda. Aktifkan penagihan di project Anda di Google AI Studio. | Anda membuat permintaan di wilayah yang tidak mendukung paket gratis, dan Anda belum mengaktifkan penagihan di project Anda di Google AI Studio. | Untuk menggunakan Gemini API, Anda harus menyiapkan paket berbayar menggunakan [Google AI Studio](https://aistudio.google.com/apikey?hl=id). |
| 402 | RESOURCE\_EXHAUSTED | Saldo kredit Prabayar Anda habis. | Akun penagihan Anda telah kehabisan kredit Prabayar, sehingga setiap kunci API yang ditautkan ke akun penagihan tersebut akan berhenti berfungsi. | [Tambahkan kredit](https://ai.google.dev/gemini-api/docs/billing?hl=id#buy-credits) ke akun penagihan Anda, atau aktifkan [isi ulang otomatis](https://ai.google.dev/gemini-api/docs/billing?hl=id#auto-reload). Jangan coba lagi permintaan ini: permintaan tidak akan berhasil hingga kredit ditambahkan. |
| 403 | PERMISSION\_DENIED | Kunci API Anda tidak memiliki izin yang diperlukan. | Anda menggunakan kunci API yang salah; Anda mencoba menggunakan model yang di-tune tanpa melalui [autentikasi yang tepat](https://ai.google.dev/gemini-api/docs/model-tuning?hl=id). | Pastikan kunci API Anda ditetapkan dan memiliki akses yang tepat. Selain itu, pastikan untuk melakukan autentikasi yang tepat untuk menggunakan model yang di-tuning. |
| 404 | NOT\_FOUND | Resource yang diminta tidak ditemukan. | File gambar, audio, atau video yang dirujuk dalam permintaan Anda tidak ditemukan. | Periksa apakah semua parameter dalam permintaan Anda valid untuk versi API Anda. |
| 429 | RESOURCE\_EXHAUSTED | Anda telah melampaui salah satu batas frekuensi API (RPM, TPM, RPD, pembelanjaan, dll.). | Anda mengirim terlalu banyak permintaan, menggunakan terlalu banyak token, atau melampaui batas berbasis pembelanjaan untuk histori penagihan dan tingkat akun Anda. | Pastikan Anda berada dalam [batas kecepatan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id) model. Tunggu dan coba lagi setelah beberapa saat. Kurangi frekuensi atau ukuran permintaan Anda. [Minta peningkatan batas frekuensi panggilan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id#request-rate-limit-increase) jika diperlukan. |
| 499 | DIBATALKAN | Operasi dibatalkan, biasanya oleh pemanggil. | Klien menutup koneksi sebelum API dapat menyelesaikan respons. | Periksa apakah klien atau infrastruktur jaringan Anda menutup koneksi sebelum waktunya (misalnya, karena waktu tunggu di sisi klien). |
| 500 | INTERNAL | Terjadi error yang tidak terduga di pihak Google. | Konteks input Anda terlalu panjang. | Periksa [halaman status Gemini API](https://aistudio.google.com/status?hl=id) untuk mengetahui insiden yang sedang berlangsung. Kurangi konteks input Anda atau beralihlah ke model lain untuk sementara (misalnya, dari Gemini 2.5 Pro ke Gemini 2.5 Flash) dan lihat apakah berhasil. Atau, tunggu sebentar dan coba lagi permintaan Anda. Jika masalah berlanjut setelah mencoba lagi, laporkan masalah tersebut menggunakan tombol **Kirim masukan** di Google AI Studio. |
| 503 | UNAVAILABLE | Layanan mungkin mengalami kelebihan beban atau gangguan sementara. | Layanan ini untuk sementara kehabisan kapasitas. | Periksa [halaman status Gemini API](https://aistudio.google.com/status?hl=id) untuk mengetahui insiden yang sedang berlangsung. Beralihlah sementara ke model lain (misalnya, dari Gemini 2.5 Pro ke Gemini 2.5 Flash) dan lihat apakah model tersebut berfungsi. Atau, tunggu sebentar dan coba lagi permintaan Anda. Jika masalah berlanjut setelah mencoba lagi, laporkan masalah tersebut menggunakan tombol **Kirim masukan** di Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Layanan tidak dapat menyelesaikan pemrosesan dalam batas waktu. | Perintah (atau konteks) Anda terlalu besar untuk diproses tepat waktu. | Tetapkan 'timeout' yang lebih besar dalam permintaan klien Anda untuk menghindari error ini. |

## Format respons error

Jika permintaan `GenerateContent` gagal, API akan menetapkan kode status HTTP (seperti `400 Bad Request`, `403 Forbidden`, atau `429 Too Many Requests`) dan menampilkan isi respons JSON yang berisi detail status gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `code` | bilangan bulat | Kode status HTTP. |
| `message` | string | Deskripsi error yang dapat dibaca manusia. |
| `status` | string | Kode status gRPC di `SCREAMING_CASE`. |
| `details` | array | Konteks error tambahan, seperti `ErrorInfo` atau `LocalizedMessage`. |

## Langkah berikutnya

- [Pemecahan masalah API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id): Atasi masalah dan skenario error umum.
- [Batas kecepatan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id): Pelajari batas permintaan dan penanganan kuota.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-20 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-20 UTC."],[],[]]
