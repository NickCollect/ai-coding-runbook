---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=id
fetched_at: 2026-05-11T05:04:24.636607+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)

# Mempercepat penemuan dengan Gemini for Research

[Mendapatkan Kunci Gemini API](https://aistudio.google.com/apikey?hl=id)

Model Gemini dapat digunakan untuk memajukan riset dasar di berbagai disiplin ilmu.
Berikut adalah cara Anda dapat menjelajahi Gemini untuk riset Anda:

- **Menganalisis dan mengontrol output model**: Untuk analisis lebih lanjut, Anda dapat memeriksa
  kandidat respons yang dihasilkan oleh model menggunakan alat seperti
  `CitationMetadata`. Anda juga dapat mengonfigurasi opsi untuk pembuatan dan output model, seperti `responseSchema`, `topP`, dan `topK`. [Pelajari lebih lanjut](https://ai.google.dev/api/generate-content?hl=id).
- **Input multimodal**: Gemini dapat memproses gambar, audio, dan video, sehingga memungkinkan a
  berbagai arah riset yang menarik. [Pelajari lebih lanjut](https://ai.google.dev/gemini-api/docs/vision?hl=id).
- **Kemampuan konteks panjang**: Gemini 3.0 Flash dan Pro dilengkapi dengan jendela konteks 1 juta token. [Pelajari lebih lanjut](https://ai.google.dev/gemini-api/docs/long-context?hl=id).
- **Grow with Google**: Akses model Gemini dengan cepat melalui API dan Google AI
  Studio untuk kasus penggunaan produksi. Jika Anda mencari platform berbasis Google Cloud, Platform Agen Gemini Enterprise dapat menyediakan infrastruktur pendukung tambahan.

Untuk mendukung riset akademis dan mendorong riset mutakhir, Google menyediakan
akses ke kredit Gemini API untuk ilmuwan dan peneliti akademis melalui
[Program Akademis Gemini](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=id#gemini-academic-program).

## Panduan awal menggunakan Gemini

Gemini API dan Google AI Studio membantu Anda mulai menggunakan model terbaru Google dan mengubah ide Anda menjadi aplikasi yang dapat diskalakan.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Akademisi unggulan

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=id)

"Riset kami menyelidiki Gemini sebagai model bahasa visual (VLM) dan perilaku agentiknya di berbagai lingkungan dari perspektif ketahanan dan keamanan. Sejauh ini, kami telah mengevaluasi ketahanan Gemini terhadap gangguan seperti jendela pop-up saat agen VLM melakukan tugas komputer, dan telah memanfaatkan Gemini untuk menganalisis interaksi sosial, peristiwa temporal, serta faktor risiko berdasarkan input video."

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=id)

"Gemini Pro dan Flash, dengan jendela konteks panjangnya, telah membantu kami dalam OK-Robot, project manipulasi seluler kosakata terbuka kami. Gemini memungkinkan kueri dan perintah bahasa alami yang kompleks atas "memori" robot: dalam hal ini, pengamatan sebelumnya yang dilakukan oleh robot selama durasi operasi yang panjang. Mahi Shafiullah dan saya juga menggunakan Gemini untuk menguraikan tugas menjadi kode yang dapat dijalankan robot di dunia nyata."

## Program Akademis Gemini

Peneliti akademis yang memenuhi syarat (seperti pengajar, staf, dan mahasiswa PhD) di [negara
yang didukung](https://ai.google.dev/gemini-api/docs/available-regions?hl=id) dapat mengajukan permohonan untuk menerima kredit Gemini API
dan batas frekuensi yang lebih tinggi untuk project riset. Dukungan ini memungkinkan throughput yang lebih tinggi untuk eksperimen ilmiah dan memajukan riset.

Kami sangat tertarik dengan area riset di bagian berikut, tetapi kami menerima permohonan dari berbagai disiplin ilmu:

- **Evaluasi dan tolok ukur**: Metode evaluasi yang didukung komunitas yang
  dapat memberikan sinyal performa yang kuat di area seperti faktualitas, keamanan,
  kepatuhan terhadap petunjuk, penalaran, dan perencanaan.
- **Mempercepat penemuan ilmiah untuk memberi manfaat bagi umat manusia**: Potensi
  aplikasi AI dalam riset ilmiah interdisipliner, termasuk area
  seperti penyakit langka dan terabaikan, biologi eksperimental, ilmu material,
  dan keberlanjutan.
- **Perwujudan dan interaksi**: Memanfaatkan model bahasa besar untuk
  menyelidiki interaksi baru dalam bidang AI terwujud, interaksi sekitar, robotika, dan interaksi manusia-komputer.
- **Kemampuan yang muncul**: Menjelajahi kemampuan agentik baru yang diperlukan untuk
  meningkatkan penalaran dan perencanaan, serta cara kemampuan dapat diperluas selama
  inferensi (misalnya, dengan memanfaatkan Gemini Flash).
- **Interaksi dan pemahaman multimodal**: Mengidentifikasi kesenjangan dan
  peluang untuk model dasar multimodal untuk analisis, penalaran,
  dan perencanaan di berbagai tugas.

Kelayakan: Hanya individu (anggota pengajar, peneliti, atau yang setara) yang berafiliasi dengan institusi akademis yang valid, atau organisasi riset akademis yang dapat mengajukan permohonan. Perhatikan bahwa akses dan kredit API akan diberikan dan dihapus atas pertimbangan Google. Kami meninjau permohonan setiap bulan.

### Mulai riset dengan Gemini API

[Daftar sekarang](https://forms.gle/HMviQstU8PxC5iCt5)

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
