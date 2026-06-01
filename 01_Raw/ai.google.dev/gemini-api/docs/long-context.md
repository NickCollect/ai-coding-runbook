---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=id
fetched_at: 2026-06-01T06:02:15.669827+00:00
title: "Konteks panjang \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Konteks panjang

Banyak model Gemini dilengkapi dengan jendela konteks besar sebesar 1 juta token atau lebih.
Sebelumnya, model bahasa besar (LLM) sangat dibatasi oleh
jumlah teks (atau token) yang dapat diteruskan ke model dalam satu waktu.
Jendela konteks panjang Gemini memungkinkan banyak kasus penggunaan baru dan paradigma developer.

Kode yang sudah Anda gunakan untuk kasus seperti [pembuatan
teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id) atau [input multimodal](https://ai.google.dev/gemini-api/docs/vision?hl=id) akan berfungsi tanpa perubahan apa pun dengan konteks panjang.

Dokumen ini memberi Anda ringkasan tentang apa yang dapat Anda capai menggunakan model dengan jendela konteks 1 juta token dan lebih banyak lagi. Halaman ini memberikan ringkasan singkat tentang jendela konteks, dan mempelajari cara developer harus memikirkan konteks panjang, berbagai kasus penggunaan dunia nyata untuk konteks panjang, dan cara mengoptimalkan penggunaan konteks panjang.

Untuk ukuran jendela konteks model tertentu, lihat halaman [Model](https://ai.google.dev/gemini-api/docs/models?hl=id).

## Apa itu jendela konteks?

Cara dasar Anda menggunakan model Gemini adalah dengan meneruskan informasi (konteks) ke model, yang selanjutnya akan menghasilkan respons. Analogi untuk jendela konteks adalah memori jangka pendek. Jumlah informasi yang dapat disimpan dalam memori jangka pendek seseorang terbatas, dan hal yang sama berlaku untuk model generatif.

Anda dapat membaca lebih lanjut cara kerja model di balik layar dalam [panduan model generatif](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id#under-the-hood) kami.

## Mulai menggunakan konteks panjang

Versi model generatif sebelumnya hanya dapat memproses 8.000 token sekaligus. Model yang lebih baru mendorong batas ini lebih jauh dengan menerima 32.000 atau bahkan 128.000 token. Gemini adalah model pertama yang mampu menerima 1 juta token.

Dalam praktiknya, 1 juta token akan terlihat seperti:

- 50.000 baris kode (dengan 80 karakter per baris standar)
- Semua pesan teks yang telah Anda kirim dalam 5 tahun terakhir
- 8 novel berbahasa Inggris dengan panjang rata-rata
- Transkrip lebih dari 200 episode podcast dengan durasi rata-rata

Jendela konteks yang lebih terbatas yang umum di banyak model lain sering kali memerlukan
strategi seperti menghapus pesan lama secara acak, meringkas konten, menggunakan
RAG dengan database vektor, atau memfilter perintah untuk menghemat token.

Meskipun teknik ini tetap berharga dalam skenario tertentu, jendela konteks Gemini yang luas mendorong pendekatan yang lebih langsung: memberikan semua informasi yang relevan di awal. Karena model Gemini dibuat khusus dengan kemampuan konteks yang sangat besar, model ini menunjukkan pembelajaran dalam konteks yang efektif. Misalnya, hanya dengan menggunakan materi pengajaran dalam konteks (tata bahasa referensi 500 halaman, kamus, dan ≈400 kalimat paralel), Gemini [belajar menerjemahkan](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf) dari bahasa Inggris ke Kalamang—bahasa Papua dengan kurang dari 200 penutur—dengan kualitas yang serupa dengan kualitas pelajar manusia yang menggunakan materi yang sama. Hal ini menggambarkan perubahan paradigma yang dimungkinkan oleh konteks panjang Gemini, yang membuka kemungkinan baru melalui pembelajaran dalam konteks yang andal.

## Kasus penggunaan konteks panjang

Meskipun kasus penggunaan standar untuk sebagian besar model generatif masih berupa input teks, serangkaian model Gemini memungkinkan paradigma baru kasus penggunaan multimodal. Model ini dapat memahami teks, video, audio, dan gambar secara native. File tersebut
disertai dengan [Gemini API yang menerima jenis file multi-modal](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=id) untuk
memudahkan.

### Teks panjang

Teks telah terbukti menjadi lapisan kecerdasan yang mendasari sebagian besar momentum seputar LLM. Seperti yang disebutkan sebelumnya, sebagian besar batasan praktis LLM disebabkan oleh tidak adanya jendela konteks yang cukup besar untuk melakukan tugas tertentu. Hal ini menyebabkan adopsi cepat retrieval augmented generation (RAG) dan teknik lainnya yang secara dinamis memberikan informasi kontekstual yang relevan kepada model. Sekarang, dengan jendela konteks yang semakin besar, ada teknik baru yang tersedia dan memungkinkan kasus penggunaan baru.

Beberapa kasus penggunaan baru dan standar untuk konteks panjang berbasis teks meliputi:

- Meringkas korpus teks besar
  - Opsi ringkasan sebelumnya dengan model konteks yang lebih kecil akan memerlukan
    jendela geser atau teknik lain untuk mempertahankan status bagian sebelumnya
    saat token baru diteruskan ke model
- Tanya jawab
  - Sebelumnya, hal ini hanya dapat dilakukan dengan RAG mengingat jumlah konteks yang terbatas dan ingatan faktual model yang rendah
- Alur kerja agentic
  - Teks adalah dasar dari cara agen mempertahankan status tindakan yang telah dilakukan dan yang perlu dilakukan; tidak memiliki informasi yang cukup tentang dunia dan tujuan agen adalah batasan pada keandalan agen

[Pembelajaran dalam konteks banyak contoh](https://arxiv.org/pdf/2404.11018) adalah salah satu kemampuan paling unik yang dihadirkan oleh model konteks panjang. Riset telah menunjukkan
bahwa mengambil paradigma contoh "sekali coba" atau "beberapa kali coba" yang umum, di mana
model disajikan dengan satu atau beberapa contoh tugas, dan menskalakannya hingga
ratusan, ribuan, atau bahkan ratusan ribu contoh, dapat menghasilkan
kemampuan model baru. Pendekatan multi-shot ini juga terbukti berperforma
serupa dengan model yang disesuaikan untuk tugas tertentu. Untuk kasus penggunaan yang performa model Gemini-nya belum cukup untuk peluncuran produksi, Anda dapat mencoba pendekatan banyak contoh. Seperti yang mungkin Anda pelajari nanti di bagian pengoptimalan konteks panjang, penyiapan cache konteks membuat jenis workload token input tinggi ini jauh lebih layak secara ekonomis dan bahkan memiliki latensi yang lebih rendah dalam beberapa kasus.

### Video panjang

Kegunaan konten video telah lama dibatasi oleh kurangnya aksesibilitas media itu sendiri. Konten sulit dibaca sekilas, transkrip sering gagal
menangkap nuansa video, dan sebagian besar alat tidak memproses gambar, teks, dan
audio secara bersamaan. Dengan Gemini, kemampuan teks panjang konteks diterjemahkan menjadi
kemampuan untuk memahami dan menjawab pertanyaan tentang input multimodal dengan
performa yang berkelanjutan.

Beberapa kasus penggunaan baru dan standar untuk konteks panjang video mencakup:

- Pertanyaan dan jawaban video
- Memori video, seperti yang ditunjukkan dengan [Project Astra Google](https://deepmind.google/technologies/gemini/project-astra/?hl=id)
- Teks video
- Sistem rekomendasi video, dengan memperkaya metadata yang ada menggunakan pemahaman multimodal baru
- Penyesuaian video, dengan melihat kumpulan data dan metadata video terkait, lalu menghapus bagian video yang tidak relevan bagi penonton
- Moderasi konten video
- Pemrosesan video real-time

Saat bekerja dengan video, penting untuk mempertimbangkan cara [video diproses menjadi token](https://ai.google.dev/gemini-api/docs/tokens?hl=id#media-token), yang memengaruhi penagihan dan batas penggunaan. Anda dapat mempelajari lebih lanjut cara membuat perintah dengan file video di
[panduan
Perintah](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=id#prompting-with-videos).

### Audio panjang

Model Gemini adalah model bahasa besar multimodal pertama yang secara native dapat memahami audio. Sebelumnya, alur kerja developer yang umum akan melibatkan penggabungan beberapa model khusus domain, seperti model speech-to-text dan model text-to-text, untuk memproses audio. Hal ini menyebabkan latensi tambahan yang diperlukan dengan melakukan beberapa permintaan pulang-pergi dan penurunan performa yang biasanya disebabkan oleh arsitektur yang terputus dari penyiapan beberapa model.

Beberapa kasus penggunaan baru dan standar untuk konteks audio mencakup:

- Transkripsi dan terjemahan real-time
- Tanya jawab podcast / video
- Transkripsi dan peringkasan rapat
- Asisten suara

Anda dapat mempelajari lebih lanjut cara membuat perintah dengan file audio di [panduan
Perintah](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=id#prompting-with-videos).

## Pengoptimalan konteks panjang

Pengoptimalan utama saat bekerja dengan konteks panjang dan model Gemini adalah menggunakan [penyimpanan cache konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id). Selain tidak mungkinnya memproses banyak token dalam satu permintaan, batasan utama lainnya adalah biaya. Jika Anda memiliki aplikasi "chat dengan data Anda" tempat pengguna mengupload 10 PDF, satu video, dan beberapa dokumen kerja, Anda harus menggunakan alat/framework pembuatan dengan pengoptimalan pengambilan (RAG) yang lebih kompleks untuk memproses permintaan ini dan membayar sejumlah besar token yang dipindahkan ke jendela konteks. Sekarang, Anda dapat menyimpan dalam cache file yang diupload pengguna dan membayar untuk menyimpannya per jam. Biaya input / output per permintaan dengan Gemini Flash, misalnya, ~4x lebih rendah daripada biaya input / output standar. Jadi, jika pengguna cukup sering melakukan percakapan dengan datanya, Anda sebagai developer akan menghemat biaya yang sangat besar.

## Batasan konteks panjang

Di berbagai bagian panduan ini, kami membahas cara model Gemini mencapai performa tinggi di berbagai evaluasi pengambilan informasi dalam tugas mencari jarum dalam tumpukan jerami. Pengujian
ini mempertimbangkan penyiapan paling dasar, yaitu Anda memiliki satu jarum yang
Anda cari. Dalam kasus di mana Anda mungkin memiliki beberapa "jarum" atau informasi spesifik yang Anda cari, model tidak akan berperforma dengan akurasi yang sama. Performa dapat sangat bervariasi, bergantung pada konteksnya. Hal ini
penting untuk dipertimbangkan karena ada pertukaran yang melekat antara mendapatkan
informasi yang tepat yang diambil dan biaya. Anda bisa mendapatkan akurasi ~99% pada satu kueri, tetapi Anda harus membayar biaya token input setiap kali Anda mengirim kueri tersebut. Jadi, untuk mengambil 100 informasi, jika Anda memerlukan performa 99%, Anda mungkin perlu mengirim 100 permintaan. Ini adalah contoh yang baik tentang tempat penyimpanan cache konteks dapat secara signifikan mengurangi biaya yang terkait dengan penggunaan model Gemini sekaligus menjaga performa tetap tinggi.

## FAQ

### Di mana tempat terbaik untuk menempatkan kueri saya di jendela konteks?

Dalam sebagian besar kasus, terutama jika total konteksnya panjang, performa model akan lebih baik jika Anda menempatkan kueri / pertanyaan di akhir perintah (setelah semua konteks lainnya).

### Apakah performa model menurun saat saya menambahkan lebih banyak token ke kueri?

Secara umum, jika Anda tidak memerlukan token untuk diteruskan ke model, sebaiknya
hindari meneruskannya. Namun, jika Anda memiliki sejumlah besar token dengan beberapa
informasi dan ingin mengajukan pertanyaan tentang informasi tersebut, model ini
sangat mampu mengekstrak informasi tersebut (dengan akurasi hingga 99% dalam banyak
kasus).

### Bagaimana cara menurunkan biaya dengan kueri konteks panjang?

Jika Anda memiliki kumpulan token / konteks serupa yang ingin digunakan kembali berkali-kali, [penyimpanan cache konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id) dapat membantu mengurangi biaya yang terkait dengan mengajukan pertanyaan tentang informasi tersebut.

### Apakah panjang konteks memengaruhi latensi model?

Ada sejumlah latensi tetap dalam setiap permintaan tertentu, terlepas dari
ukurannya, tetapi umumnya kueri yang lebih panjang akan memiliki latensi yang lebih tinggi (waktu untuk token pertama).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
