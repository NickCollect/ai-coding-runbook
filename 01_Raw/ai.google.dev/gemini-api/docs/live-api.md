---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=id
fetched_at: 2026-09-07T05:37:51.592353+00:00
title: "Ringkasan Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Ringkasan Gemini Live API

Live API memungkinkan interaksi suara dan visi real-time dengan latensi rendah bersama Gemini. Fitur ini memproses aliran audio, gambar, dan teks yang berkelanjutan untuk menghasilkan respons lisan yang langsung dan mirip manusia, sehingga menciptakan pengalaman percakapan yang alami bagi pengguna Anda.

![Ringkasan Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=id)

[Coba Live API di Google AI Studiomic](https://aistudio.google.com/live?hl=id)
[Clone aplikasi contoh dari GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Gunakan keterampilan agen pengodeanterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)

## Kasus penggunaan

Live API dapat digunakan untuk membangun agen suara real-time untuk berbagai industri, termasuk:

- **E-commerce dan retail:** Asisten belanja yang menawarkan rekomendasi yang dipersonalisasi dan agen dukungan yang menyelesaikan masalah pelanggan.
- **Game:** Karakter non-pemain (NPC) interaktif, asisten bantuan dalam game, dan terjemahan real-time konten dalam game.
- **Antarmuka generasi berikutnya:** Pengalaman yang mendukung suara dan video dalam robotika, kacamata pintar, dan kendaraan.
- **Layanan kesehatan:** Pendamping kesehatan untuk dukungan dan edukasi pasien.
- **Layanan keuangan:** Penasihat AI untuk manajemen kekayaan dan panduan investasi.
- **Pendidikan:** Mentor AI dan pendamping pelajar yang memberikan instruksi dan masukan yang dipersonalisasi.
- **Terjemahan dan pelokalan:** Terjemahan real-time dan latensi rendah untuk percakapan lisan, sehingga memungkinkan komunikasi multibahasa yang lancar.

## Fitur utama

Live API menawarkan serangkaian fitur komprehensif untuk membangun agen suara yang andal:

- [**Dukungan multibahasa**](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#supported-languages):
  Berkomunikasi dalam 70 bahasa yang didukung.
- [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#interruptions):
  Pengguna dapat mengganggu model kapan saja untuk interaksi responsif.
- [**Penggunaan alat**](https://ai.google.dev/gemini-api/docs/live-tools?hl=id):
  Mengintegrasikan alat seperti panggilan fungsi dan Google Penelusuran untuk interaksi dinamis.
- [**Transkripsi audio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#audio-transcription):
  Menyediakan transkrip teks untuk input pengguna dan output model.
- [**Audio proaktif**](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#proactive-audio):
  Memungkinkan Anda mengontrol kapan model merespons dan dalam konteks apa.
- [**Dialog afektif**](https://ai.google.dev/gemini-api/docs/live-guide?hl=id#affective-dialog):
  Menyesuaikan gaya dan nada respons agar sesuai dengan ekspresi input pengguna.
- [**Terjemahan Langsung**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=id):
  Terjemahan suara-ke-suara real-time dalam lebih dari 70 bahasa.

## Spesifikasi teknis

Tabel berikut menguraikan spesifikasi teknis untuk Live API:

| Kategori | Detail |
| --- | --- |
| Modalitas input | Audio (audio PCM 16-bit mentah, 16 kHz, little-endian), gambar (JPEG <= 1 FPS), teks |
| Modalitas output | Audio (audio PCM 16-bit mentah, 24 kHz, little-endian) |
| Protokol | Koneksi WebSocket stateful (WSS) |

## Memilih pendekatan implementasi

Saat berintegrasi dengan Live API, Anda harus memilih salah satu pendekatan implementasi berikut:

- **Server-ke-server**: Backend Anda terhubung ke Live API menggunakan
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Biasanya, klien Anda mengirim data streaming (audio, video, teks) ke server Anda, yang kemudian meneruskannya ke Live API.
- **Klien-ke-server**: Kode frontend Anda terhubung langsung ke Live API
  menggunakan [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) untuk men-streaming data, sehingga melewati backend Anda.

## Mulai

Pilih panduan yang sesuai dengan lingkungan pengembangan Anda:

Server-ke-server

### [Tutorial GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=id)

Hubungkan ke Gemini Live API menggunakan GenAI SDK untuk membangun aplikasi multimodal real-time dengan backend Python.

Klien-ke-server

### [Tutorial WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=id)

Hubungkan ke Gemini Live API menggunakan WebSockets untuk membangun aplikasi multimodal real-time dengan frontend JavaScript dan token sementara.

Agent Development Kit

### [Tutorial ADK](https://google.github.io/adk-docs/streaming/)

Buat agen dan gunakan Streaming Agent Development Kit (ADK) untuk mengaktifkan komunikasi suara dan video.

## Integrasi partner

Untuk menyederhanakan pengembangan aplikasi audio dan video real-time, Anda dapat menggunakan
integrasi pihak ketiga yang mendukung Gemini Live
API melalui WebRTC atau WebSockets.

[LiveKit

Gunakan Gemini Live API dengan Agen LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat dari Daily

Buat chatbot AI real-time menggunakan Gemini Live dan Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam dari Software Mansion

Buat aplikasi streaming video dan audio live dengan Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Agen Vision dari Stream

Buat aplikasi AI suara dan video real-time dengan Agen Vision.](https://visionagents.ai/integrations/gemini)
[Voximplant

Hubungkan panggilan masuk dan keluar ke Live API dengan Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Buat aplikasi AI percakapan real-time dengan Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Mulai menggunakan Gemini Live API dengan Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-12 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-12 UTC."],[],[]]
