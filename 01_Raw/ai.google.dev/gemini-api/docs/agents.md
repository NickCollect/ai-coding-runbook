---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=id
fetched_at: 2026-05-05T20:08:26.473162+00:00
title: "Ringkasan Agen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Ringkasan Agen

Agen adalah sistem yang memanfaatkan model Gemini, serangkaian alat, dan kemampuan penalaran untuk melakukan tugas kompleks multi-langkah dan mencapai sasaran tertentu. Tidak seperti satu panggilan model, agen dapat merencanakan, menjalankan serangkaian tindakan, berinteraksi dengan sistem eksternal, dan mensintesis informasi untuk memenuhi permintaan pengguna.

Dengan Gemini API, Anda dapat membangun agen yang andal dengan memanfaatkan fitur seperti:

- **[Model Gemini](https://ai.google.dev/gemini-api/docs/models?hl=id):** Kecerdasan inti,
  yang menyediakan penalaran dan pemahaman bahasa.
- **[Alat](https://ai.google.dev/gemini-api/docs/tools?hl=id):** Kemampuan yang menghubungkan model ke
  informasi dan tindakan dunia nyata. Alat ini dapat berupa alat bawaan (seperti Google Penelusuran, Maps, Eksekusi Kode) atau alat kustom.
- **[Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id):** Mekanisme untuk
  menentukan dan menghubungkan alat dan API kustom Anda sendiri ke model Gemini.
- **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id):** Fitur yang meningkatkan
  kemampuan model untuk menalar dan merencanakan tugas yang kompleks.
- **[Konteks panjang](https://ai.google.dev/gemini-api/docs/long-context?hl=id):** Memungkinkan agen untuk
  mempertahankan status dan informasi selama interaksi yang diperpanjang.

## Agen yang Tersedia

- **[Agen Riset Mendalam](https://ai.google.dev/gemini-api/docs/deep-research?hl=id):** Agen otonom
  yang merencanakan, menjalankan, dan mensintesis tugas riset multi-langkah untuk
  kasus penggunaan seperti analisis pasar, uji tuntas, dan tinjauan literatur.

## Membangun agen

Agen menggunakan model dan alat untuk menyelesaikan tugas multi-langkah. Meskipun Gemini menyediakan kemampuan penalaran ("otak") dan alat penting ("tangan"), Anda sering kali memerlukan framework orkestrasi untuk mengelola memori agen, loop rencana, dan melakukan chaining alat yang kompleks.

Untuk memaksimalkan keandalan dalam alur kerja multi-langkah, Anda harus membuat petunjuk yang secara eksplisit mengontrol cara model menalar dan merencanakan. Meskipun Gemini menyediakan penalaran umum yang kuat, agen yang kompleks akan mendapatkan manfaat dari perintah yang menerapkan perilaku tertentu seperti persistensi saat menghadapi masalah, penilaian risiko, dan perencanaan proaktif.

Lihat [Alur kerja
Agentic](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id#agentic-workflows) untuk
mengetahui strategi dalam mendesain perintah ini. Berikut adalah contoh [petunjuk
sistem](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id#agentic-si-template) yang
meningkatkan performa pada beberapa tolok ukur agentic sekitar 5%.

## Framework agen

Gemini terintegrasi dengan framework agen open source terkemuka seperti:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=id): Membangun
  alur aplikasi stateful yang kompleks dan sistem multi-agen menggunakan struktur grafik.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=id): Menghubungkan agen Gemini ke
  data pribadi Anda untuk alur kerja yang ditingkatkan RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=id): Mengorkestrasi agen AI otonom yang kolaboratif,
  memainkan peran.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=id): Membangun
  antarmuka dan agen pengguna yang didukung AI di JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Framework open source untuk membangun dan mengorkestrasi agen AI yang dapat beroperasi.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
