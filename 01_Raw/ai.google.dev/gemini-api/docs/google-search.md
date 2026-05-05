---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=id
fetched_at: 2026-05-05T13:13:07.080783+00:00
title: "Perujukan dengan Google Penelusuran \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/Deep Research Gemini) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

- [Beranda](https://ai.google.dev/gemini-api/docs/Beranda)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumen](https://ai.google.dev/gemini-api/docs/Dokumen)

Kirim masukan

# Perujukan dengan Google Penelusuran

Grounding dengan Google Penelusuran menghubungkan model Gemini ke konten web real-time dan berfungsi dengan semua bahasa yang tersedia. Hal ini memungkinkan Gemini memberikan jawaban yang lebih akurat dan mengutip sumber yang dapat diverifikasi di luar batas pengetahuannya.

Perujukan membantu Anda membangun aplikasi yang dapat:

- **Meningkatkan akurasi faktual:** Mengurangi halusinasi model dengan mendasarkan respons pada informasi dunia nyata.
- **Mengakses informasi real-time:** Menjawab pertanyaan tentang peristiwa dan topik terbaru.
- **Memberikan kutipan:** Bangun kepercayaan pengguna dengan menunjukkan sumber klaim model.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Anda dapat mempelajari lebih lanjut dengan mencoba [notebook alat Penelusuran](https://ai.google.dev/gemini-api/docs/notebook alat Penelusuran).

## Cara kerja perujukan dengan Google Penelusuran

Saat Anda mengaktifkan alat `google_search`, model akan menangani seluruh alur kerja
untuk menelusuri, memproses, dan mengutip informasi secara otomatis.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=id)

1. **Perintah Pengguna:** Aplikasi Anda mengirimkan perintah pengguna ke Gemini API
   dengan mengaktifkan alat `google_search`.
2. **Analisis Perintah:** Model menganalisis perintah dan menentukan apakah Google Penelusuran dapat meningkatkan kualitas jawaban.
3. **Google Penelusuran:** Jika diperlukan, model akan otomatis membuat satu atau beberapa kueri penelusuran dan mengeksekusinya.
4. **Pemrosesan Hasil Penelusuran:** Model memproses hasil penelusuran, menyintesis informasi, dan merumuskan respons.
5. **Respons yang Di-grounding:** API menampilkan respons akhir yang mudah digunakan dan
   didasarkan pada hasil penelusuran. Respons ini mencakup jawaban teks model
   dan `groundingMetadata` dengan kueri penelusuran, hasil web, dan
   kutipan.

## Memahami respons perujukan

Jika respons berhasil didasarkan, respons akan menyertakan kolom
`groundingMetadata`. Data terstruktur ini penting untuk memverifikasi klaim dan membangun pengalaman kutipan yang kaya di aplikasi Anda.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API menampilkan informasi berikut dengan `groundingMetadata`:

- `webSearchQueries` : Array kueri penelusuran yang digunakan. Hal ini berguna untuk
  men-debug dan memahami proses penalaran model.
- `searchEntryPoint` : Berisi HTML dan CSS untuk merender Saran
  Penelusuran yang diperlukan. Persyaratan penggunaan lengkap dijelaskan dalam [Persyaratan Layanan](https://ai.google.dev/gemini-api/docs/Persyaratan Layanan).
- `groundingChunks` : Array objek yang berisi sumber web (`uri` dan
  `title`).
- `groundingSupports` : Array potongan untuk menghubungkan respons model `text` ke sumber di `groundingChunks`. Setiap bagian menautkan teks `segment` (ditentukan
  oleh `startIndex` dan `endIndex`) ke satu atau beberapa `groundingChunkIndices`. Langkah ini
  adalah kunci untuk membuat kutipan inline.

Pen-grounding dengan Google Penelusuran juga dapat digunakan bersama dengan [alat konteks URL](https://ai.google.dev/gemini-api/docs/alat konteks URL) untuk men-grounding respons dalam data web publik dan URL tertentu yang Anda berikan.

## Mengatribusikan sumber dengan kutipan di dalam teks

API menampilkan data kutipan terstruktur, sehingga Anda memiliki kontrol penuh atas cara Anda menampilkan sumber di antarmuka pengguna. Anda dapat menggunakan kolom `groundingSupports`
dan `groundingChunks` untuk menautkan pernyataan model secara langsung ke sumbernya. Berikut adalah pola umum untuk memproses metadata guna membuat respons dengan kutipan inline yang dapat diklik.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](https://ai.google.dev/gemini-api/docs/1)[2](https://ai.google.dev/gemini-api/docs/2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}](https://ai.google.dev/gemini-api/docs/{i + 1})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](https://ai.google.dev/gemini-api/docs/${i + 1})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

Respons baru dengan kutipan inline akan terlihat seperti ini:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https://ai.google.dev/gemini-api/docs/1), [2](https://ai.google.dev/gemini-api/docs/2), [4](https://ai.google.dev/gemini-api/docs/4), [5](https://ai.google.dev/gemini-api/docs/5) This victory marks Spain's record-breaking fourth European Championship title.[5](https://ai.google.dev/gemini-api/docs/5), [2](https://ai.google.dev/gemini-api/docs/2), [3](https://ai.google.dev/gemini-api/docs/3), [4](https://ai.google.dev/gemini-api/docs/4)
```

## Harga

Saat Anda menggunakan Grounding dengan Google Penelusuran dengan Gemini 3, project Anda akan ditagih
untuk setiap kueri penelusuran yang diputuskan untuk dijalankan oleh model. Jika model memutuskan untuk
menjalankan beberapa kueri penelusuran untuk menjawab satu perintah (misalnya,
menelusuri `"UEFA Euro 2024 winner"` dan `"Spain vs England Euro 2024 final
score"` dalam panggilan API yang sama), hal ini dihitung sebagai dua penggunaan alat yang dapat ditagih
untuk permintaan tersebut. Untuk tujuan penagihan, kami mengabaikan kueri penelusuran web yang kosong saat menghitung kueri unik. Model penagihan ini hanya berlaku untuk model Gemini 3; saat Anda menggunakan perujukan penelusuran dengan model Gemini 2.5 atau yang lebih lama, project Anda akan ditagih per perintah.

Untuk mengetahui informasi harga selengkapnya, lihat [halaman harga Gemini API](https://ai.google.dev/gemini-api/docs/halaman harga Gemini API).

## Model yang didukung

Anda dapat menemukan kemampuan lengkap di halaman [ringkasan
model](https://ai.google.dev/gemini-api/docs/ringkasanmodel).

| Model | Grounding dengan Google Penelusuran |
| --- | --- |
| Pratinjau Gambar Gemini 3.1 Flash | ✔️ |
| Pratinjau Gemini 3.1 Pro | ✔️ |
| Pratinjau Gambar Gemini 3 Pro | ✔️ |
| Pratinjau Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Kombinasi alat yang didukung

Anda dapat menggunakan Grounding dengan Google Penelusuran bersama alat lain seperti
[eksekusi kode](https://ai.google.dev/gemini-api/docs/eksekusi kode) dan
[konteks URL](https://ai.google.dev/gemini-api/docs/konteks URL) untuk mendukung kasus penggunaan yang lebih kompleks.

Model Gemini 3 mendukung penggabungan alat bawaan (seperti Perujukan dengan Google Penelusuran) dengan alat kustom (pemanggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/kombinasi alat).

## Langkah berikutnya

- Coba [Grounding dengan Google Penelusuran di Cookbook Gemini API](https://ai.google.dev/gemini-api/docs/Grounding dengan Google Penelusuran di Cookbook Gemini API).
- Pelajari alat lain yang tersedia, seperti [Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/Panggilan Fungsi).
- Pelajari cara memperkaya perintah dengan URL tertentu menggunakan [alat konteks URL](https://ai.google.dev/gemini-api/docs/alat konteks URL).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Lisensi Creative Commons Attribution 4.0), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://ai.google.dev/gemini-api/docs/Lisensi Apache 2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://ai.google.dev/gemini-api/docs/Kebijakan Situs Google Developers). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?
