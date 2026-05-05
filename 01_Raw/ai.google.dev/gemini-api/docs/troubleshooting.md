---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id
fetched_at: 2026-05-05T19:46:02.014940+00:00
title: "Panduan pemecahan masalah \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan pemecahan masalah

Gunakan panduan ini untuk membantu Anda mendiagnosis dan menyelesaikan masalah umum yang muncul saat Anda memanggil Gemini API. Anda mungkin mengalami masalah dari
layanan backend Gemini API atau SDK klien. SDK klien kami bersifat open source di repositori berikut:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Jika Anda mengalami masalah kunci API, pastikan Anda telah menyiapkan kunci API dengan benar sesuai dengan [panduan penyiapan kunci API](https://ai.google.dev/gemini-api/docs/api-key?hl=id).

## Kode error layanan backend Gemini API

Tabel berikut mencantumkan kode error backend umum yang mungkin Anda temui, beserta penjelasan penyebab dan langkah-langkah pemecahan masalahnya:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kode HTTP** | **Status** | **Deskripsi** | **Contoh** | **Solusi** |
| 400 | INVALID\_ARGUMENT | Isi permintaan salah format. | Ada salah ketik, atau kolom wajib diisi yang tidak ada dalam permintaan Anda. | Lihat [referensi API](https://ai.google.dev/api?hl=id) untuk mengetahui format permintaan, contoh, dan versi yang didukung. Menggunakan fitur dari versi API yang lebih baru dengan endpoint yang lebih lama dapat menyebabkan error. |
| 400 | FAILED\_PRECONDITION | Paket gratis Gemini API tidak tersedia di negara Anda. Aktifkan penagihan di project Anda di Google AI Studio. | Anda membuat permintaan di wilayah yang tidak mendukung paket gratis, dan Anda belum mengaktifkan penagihan di project Anda di Google AI Studio. | Untuk menggunakan Gemini API, Anda harus menyiapkan paket berbayar menggunakan [Google AI Studio](https://aistudio.google.com/app/apikey?hl=id). |
| 403 | PERMISSION\_DENIED | Kunci API Anda tidak memiliki izin yang diperlukan. | Anda menggunakan kunci API yang salah; Anda mencoba menggunakan model yang di-tuning tanpa melalui [autentikasi yang tepat](https://ai.google.dev/gemini-api/docs/model-tuning?hl=id). | Pastikan kunci API Anda ditetapkan dan memiliki akses yang tepat. Selain itu, pastikan untuk melakukan autentikasi yang tepat untuk menggunakan model yang di-tuning. |
| 404 | NOT\_FOUND | Resource yang diminta tidak ditemukan. | File gambar, audio, atau video yang dirujuk dalam permintaan Anda tidak ditemukan. | Periksa apakah semua [parameter dalam permintaan Anda valid](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id#check-api) untuk versi API Anda. |
| 429 | RESOURCE\_EXHAUSTED | Anda telah melampaui batas kecepatan. | Anda mengirim terlalu banyak permintaan per menit dengan Gemini API tingkat gratis. | Pastikan Anda berada dalam [batas kecepatan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id) model. [Minta penambahan kuota](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id#request-rate-limit-increase) jika diperlukan. |
| 500 | INTERNAL | Terjadi error yang tidak terduga di pihak Google. | Konteks input Anda terlalu panjang. | Periksa [halaman status Gemini API](https://aistudio.google.com/status?hl=id) untuk mengetahui insiden yang sedang berlangsung. Kurangi konteks input Anda atau beralihlah sementara ke model lain (misalnya, dari Gemini 2.5 Pro ke Gemini 2.5 Flash) dan lihat apakah berhasil. Atau, tunggu sebentar dan coba lagi permintaan Anda. Jika masalah berlanjut setelah mencoba lagi, laporkan masalah tersebut menggunakan tombol **Kirim masukan** di Google AI Studio. |
| 503 | UNAVAILABLE | Layanan mungkin mengalami kelebihan beban atau gangguan sementara. | Layanan ini untuk sementara kehabisan kapasitas. | Periksa [halaman status Gemini API](https://aistudio.google.com/status?hl=id) untuk mengetahui insiden yang sedang berlangsung. Beralihlah sementara ke model lain (misalnya, dari Gemini 2.5 Pro ke Gemini 2.5 Flash) dan lihat apakah model tersebut berfungsi. Atau, tunggu sebentar dan coba lagi permintaan Anda. Jika masalah berlanjut setelah mencoba lagi, laporkan masalah tersebut menggunakan tombol **Kirim masukan** di Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Layanan tidak dapat menyelesaikan pemrosesan dalam batas waktu. | Perintah (atau konteks) Anda terlalu besar untuk diproses tepat waktu. | Tetapkan 'timeout' yang lebih besar dalam permintaan klien Anda untuk menghindari error ini. |

## Memeriksa panggilan API untuk mengetahui error parameter model

Pastikan parameter model Anda berada dalam nilai berikut:

|  |  |
| --- | --- |
| **Parameter model** | **Nilai (rentang)** |
| Jumlah kandidat | 1-8 (bilangan bulat) |
| Suhu | 0.0-1.0 |
| Token output maks | Gunakan [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id) untuk menentukan jumlah token maksimum untuk model yang Anda gunakan. |
| TopP | 0.0-1.0 |

Selain memeriksa nilai parameter, pastikan Anda menggunakan [versi API](https://ai.google.dev/gemini-api/docs/api-versions?hl=id) yang benar (misalnya, `/v1` atau `/v1beta`) dan model yang mendukung fitur yang Anda butuhkan. Misalnya, jika fitur dalam rilis Beta, fitur tersebut hanya akan tersedia di versi API `/v1beta`.

## Periksa apakah Anda memiliki model yang tepat

Pastikan Anda menggunakan model yang didukung dan tercantum di [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id) kami.

## Latensi atau penggunaan token yang lebih tinggi dengan model 2.5

Jika Anda mengamati latensi atau penggunaan token yang lebih tinggi dengan model 2.5 Flash dan Pro, hal ini dapat terjadi karena model tersebut dilengkapi dengan **kemampuan berpikir yang diaktifkan secara default** untuk meningkatkan kualitas. Jika Anda memprioritaskan kecepatan atau perlu meminimalkan biaya, Anda dapat menyesuaikan atau menonaktifkan pemikiran.

Lihat [halaman pemikiran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#set-budget) untuk mendapatkan panduan dan contoh kode.

## Masalah keamanan

Jika Anda melihat perintah diblokir karena setelan keamanan dalam panggilan API Anda,
tinjau perintah tersebut sehubungan dengan filter yang Anda tetapkan dalam panggilan API.

Jika Anda melihat `BlockedReason.OTHER`, kueri atau respons mungkin melanggar [persyaratan layanan](https://ai.google.dev/terms?hl=id) atau tidak didukung.

## Masalah bacaan

Jika Anda melihat model berhenti menghasilkan output karena alasan RECITASI, artinya output model mungkin menyerupai data tertentu. Untuk memperbaikinya, coba buat perintah / konteks seunik mungkin dan gunakan nilai temperature yang lebih tinggi.

## Masalah token berulang

Jika Anda melihat token output yang berulang, coba saran berikut untuk membantu mengurangi atau menghilangkannya.

| Deskripsi | Penyebab | Solusi alternatif yang disarankan |
| --- | --- | --- |
| Tanda hubung berulang dalam tabel Markdown | Hal ini dapat terjadi saat isi tabel panjang karena model mencoba membuat tabel Markdown yang selaras secara visual. Namun, perataan di Markdown tidak diperlukan untuk rendering yang benar. | Tambahkan petunjuk dalam perintah Anda untuk memberikan panduan khusus kepada model dalam membuat tabel Markdown. Berikan contoh yang mengikuti pedoman tersebut. Anda juga dapat mencoba menyesuaikan suhu. Untuk membuat kode atau output yang sangat terstruktur seperti tabel Markdown, nilai temperature yang tinggi terbukti berfungsi lebih baik (>= 0,8).  Berikut adalah contoh kumpulan pedoman yang dapat Anda tambahkan ke perintah untuk mencegah masalah ini:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Token berulang dalam tabel Markdown | Mirip dengan tanda hubung berulang, hal ini terjadi saat model mencoba menyelaraskan konten tabel secara visual. Perataan di Markdown tidak diperlukan untuk rendering yang benar. | - Coba tambahkan petunjuk seperti berikut ke perintah sistem Anda:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Coba sesuaikan suhu. Temperatur yang lebih tinggi (>= 0,8)   biasanya membantu menghilangkan pengulangan atau duplikasi dalam   output. |
| Baris baru berulang (`\n`) dalam output terstruktur | Jika input model berisi urutan escape atau unicode seperti `\u` atau `\t`, hal ini dapat menyebabkan baris baru berulang. | - Periksa dan ganti urutan escape yang dilarang dengan karakter UTF-8   dalam perintah Anda. Misalnya, urutan escape `\u`   dalam contoh JSON dapat menyebabkan model menggunakannya   dalam outputnya juga. - Memberi tahu model tentang karakter escape yang diizinkan. Tambahkan petunjuk sistem seperti   ini:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Teks berulang dalam menggunakan output terstruktur | Jika output model memiliki urutan kolom yang berbeda dengan skema terstruktur yang ditentukan, hal ini dapat menyebabkan teks berulang. | - Jangan tentukan urutan kolom dalam perintah Anda. - Menjadikan semua kolom output wajib diisi. |
| Panggilan alat berulang | Hal ini dapat terjadi jika model kehilangan konteks pemikiran sebelumnya dan/atau memanggil endpoint yang tidak tersedia yang harus dipanggil. | Perintahkan model untuk mempertahankan status dalam proses pemikirannya. Tambahkan ini di akhir petunjuk sistem Anda:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Teks berulang yang bukan bagian dari output terstruktur | Hal ini dapat terjadi jika model mengalami masalah pada permintaan yang tidak dapat diselesaikannya. | - Jika pemikiran diaktifkan, hindari memberikan perintah eksplisit tentang cara   memikirkan suatu masalah dalam petunjuk. Cukup minta output   akhir. - Coba suhu yang lebih tinggi >= 0,8. - Tambahkan petunjuk seperti "Singkat", "Jangan mengulangi diri sendiri", atau   "Berikan jawaban sekali saja". |

## Kunci API yang diblokir atau tidak berfungsi

Bagian ini menjelaskan cara memeriksa apakah kunci Gemini API Anda diblokir
dan apa yang harus dilakukan.

### Memahami alasan kunci diblokir

Kami telah mengidentifikasi kerentanan yang menyebabkan beberapa kunci API mungkin terekspos secara publik. Untuk melindungi data Anda dan mencegah akses tidak sah, kami telah
secara proaktif memblokir kunci yang diketahui bocor ini agar tidak dapat mengakses Gemini API.

### Pastikan apakah kunci Anda terpengaruh

Jika kunci Anda diketahui bocor, Anda tidak dapat lagi menggunakan kunci tersebut dengan Gemini API. Anda dapat menggunakan [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=id) untuk melihat apakah ada kunci API Anda yang diblokir agar tidak memanggil Gemini API dan membuat kunci baru. Anda mungkin juga melihat error berikut yang ditampilkan saat mencoba menggunakan
kunci ini:

```
Your API key was reported as leaked. Please use another API key.
```

### Tindakan untuk kunci API yang diblokir

Anda harus membuat kunci API baru untuk integrasi Gemini API menggunakan [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=id). Sebaiknya tinjau praktik pengelolaan kunci API Anda untuk memastikan kunci baru Anda tetap aman dan tidak diekspos secara publik.

### Tagihan tak terduga karena kerentanan

[Kirim kasus dukungan penagihan](https://console.cloud.google.com/support/chat?hl=id).
Tim penagihan kami sedang menanganinya, dan kami akan menyampaikan info terbaru sesegera mungkin.

### Langkah-langkah keamanan Google untuk kunci yang bocor

**Bagaimana cara Google membantu mengamankan akun saya dari kelebihan biaya dan penyalahgunaan jika kunci API saya bocor?**

- Kami akan menerbitkan kunci API saat Anda meminta kunci baru menggunakan
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=id) yang secara default akan
  dibatasi hanya untuk Google AI Studio dan tidak menerima kunci dari layanan lain.
  Tindakan ini akan membantu mencegah penggunaan lintas tombol yang tidak disengaja.
- Secara default, kami memblokir kunci API yang bocor dan digunakan dengan Gemini API, sehingga membantu mencegah penyalahgunaan biaya dan data aplikasi Anda.
- Anda akan dapat menemukan status kunci API Anda dalam [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=id) dan kami akan berupaya berkomunikasi secara proaktif saat kami mengidentifikasi bahwa kunci API Anda bocor untuk segera ditindaklanjuti.

## Meningkatkan kualitas output model

Untuk output model berkualitas lebih tinggi, coba tulis perintah yang lebih terstruktur. Halaman [panduan rekayasa perintah](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id) memperkenalkan beberapa konsep dasar, strategi, dan praktik terbaik untuk membantu Anda memulai.

## Memahami batas token

Baca [Panduan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id) kami untuk lebih memahami cara menghitung token dan batasnya.

## Masalah umum

- API ini hanya mendukung sejumlah bahasa tertentu. Mengirimkan perintah dalam bahasa yang tidak didukung dapat menghasilkan respons yang tidak terduga atau bahkan diblokir. Lihat
  [bahasa yang tersedia](https://ai.google.dev/gemini-api/docs/models?hl=id#supported-languages) untuk mengetahui info terbaru.

## Laporkan bug

Bergabunglah dalam diskusi di
[forum developer AI Google](https://discuss.ai.google.dev?hl=id)
jika ada pertanyaan.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-30 UTC."],[],[]]
