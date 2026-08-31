---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=id
fetched_at: 2026-08-31T06:39:27.738599+00:00
title: "Grounding dengan Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Grounding dengan Google Maps

Grounding with Google Maps menghubungkan kemampuan generatif Gemini dengan data Google Maps yang kaya, faktual, dan terbaru. Fitur ini memungkinkan developer dengan mudah menyertakan fungsi yang mengetahui lokasi ke dalam aplikasi mereka. Saat kueri pengguna memiliki konteks yang terkait dengan data Maps, model Gemini memanfaatkan Google Maps untuk memberikan jawaban yang akurat secara faktual dan terbaru yang relevan dengan lokasi atau area umum yang ditentukan pengguna.

- **Respons yang akurat dan mengetahui lokasi:** Manfaatkan data Google Maps yang luas dan terbaru untuk kueri yang spesifik secara geografis.
- **Personalisasi yang ditingkatkan:** Sesuaikan rekomendasi dan informasi berdasarkan lokasi yang diberikan pengguna.

## Mulai

Contoh ini menunjukkan cara mengintegrasikan Grounding with Google Maps ke dalam aplikasi Anda untuk memberikan respons yang akurat dan mengetahui lokasi terhadap kueri pengguna. Perintah meminta rekomendasi lokal dengan lokasi pengguna opsional, sehingga model Gemini dapat menggunakan data Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Cara kerja Grounding with Google Maps

Grounding with Google Maps mengintegrasikan Gemini API dengan ekosistem Google Geo menggunakan Maps API sebagai sumber grounding. Saat kueri pengguna berisi konteks geografis, model Gemini dapat memanggil alat Grounding with Google Maps. Model ini kemudian dapat menghasilkan respons yang didasarkan pada data Google Maps yang relevan dengan lokasi yang diberikan.

Proses ini biasanya melibatkan:

1. **Kueri pengguna:** Pengguna mengirimkan kueri ke aplikasi Anda, yang mungkin menyertakan konteks geografis (misalnya, "kafe di dekat saya", "museum di San Francisco").
2. **Pemanggilan alat:** Model Gemini, yang mengenali maksud geografis, memanggil alat Grounding with Google Maps. Alat ini dapat secara opsional diberikan `latitude` dan `longitude` pengguna. Alat ini adalah alat penelusuran teks dan berperilaku mirip dengan penelusuran di Maps, yang mana kueri lokal ("di dekat saya") akan menggunakan koordinat, sedangkan kueri spesifik atau non-lokal kemungkinan tidak akan terpengaruh oleh lokasi eksplisit.
3. **Pengambilan data:** Layanan Grounding with Google Maps meminta informasi yang relevan dari Google Maps (misalnya, tempat, ulasan, foto, alamat, jam buka).
4. **Generasi yang didasarkan:** Data Maps yang diambil digunakan untuk menginformasikan respons model Gemini, sehingga memastikan akurasi dan relevansi faktual.
5. **Respons:** Model menampilkan respons teks, yang menyertakan kutipan ke sumber Google Maps.

## Alasan dan waktu penggunaan Grounding with Google Maps

Grounding with Google Maps sangat ideal untuk aplikasi yang memerlukan informasi yang akurat, terbaru, dan spesifik lokasi. Fitur ini meningkatkan pengalaman pengguna dengan menyediakan konten yang relevan dan dipersonalisasi yang didukung oleh database Google Maps yang luas dengan lebih dari 250 juta tempat di seluruh dunia.

Anda harus menggunakan Grounding with Google Maps jika aplikasi Anda perlu:

- Memberikan respons yang lengkap dan akurat terhadap pertanyaan spesifik geografis.
- Membuat perencana perjalanan percakapan dan panduan lokal.
- Merekomendasikan tempat menarik berdasarkan lokasi dan preferensi pengguna seperti restoran atau toko.
- Membuat pengalaman yang mengetahui lokasi untuk layanan sosial, retail, atau pengiriman makanan.

Grounding with Google Maps unggul dalam kasus penggunaan yang mengutamakan kedekatan dan data faktual saat ini, seperti menemukan "kafe terbaik di dekat saya" atau mendapatkan rute.

## Metode dan parameter API

Grounding with Google Maps diekspos melalui Gemini API sebagai alat dalam
metode [`generateContent`](https://ai.google.dev/api/generate-content?hl=id). Anda dapat mengaktifkan dan mengonfigurasi
Grounding with Google Maps dengan menyertakan
[`googleMaps`](https://ai.google.dev/api/caching?hl=id#GoogleMaps) objek dalam `tools` parameter
permintaan Anda.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Selain itu, alat ini mendukung penerusan lokasi kontekstual sebagai `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Memahami respons grounding

Jika respons berhasil didasarkan pada data Google Maps, respons
akan menyertakan [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=id#GroundingMetadata) kolom.
Data terstruktur ini penting untuk memverifikasi klaim dan membuat pengalaman kutipan yang kaya dalam aplikasi Anda, serta memenuhi persyaratan penggunaan layanan.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API menampilkan informasi berikut dengan
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=id#GroundingMetadata):

- `groundingChunks`: Array objek yang berisi sumber `maps` (`uri`, `placeId`, dan `title`).
- `groundingSupports`: Array potongan untuk menghubungkan teks respons model ke sumber di `groundingChunks`. Setiap potongan menautkan rentang teks (yang ditentukan oleh `startIndex` dan `endIndex`) ke satu atau beberapa `groundingChunkIndices`. Ini adalah kunci untuk membuat kutipan inline.

Untuk mengetahui cuplikan kode yang menunjukkan cara merender kutipan inline dalam teks, lihat [contoh](https://ai.google.dev/gemini-api/docs/google-search?hl=id#attributing_sources_with_inline_citations)
di dokumen Grounding with Google Search.

## Kasus penggunaan

Grounding with Google Maps mendukung berbagai kasus penggunaan yang mengetahui lokasi. Contoh berikut menunjukkan cara berbagai perintah dan parameter dapat memanfaatkan Grounding with Google Maps. Informasi dalam Hasil yang Di-grounding Google Maps mungkin berbeda dengan kondisi sebenarnya.

### Menangani pertanyaan spesifik tempat

Ajukan pertanyaan mendetail tentang tempat tertentu untuk mendapatkan jawaban berdasarkan ulasan pengguna Google dan data Maps lainnya.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Menyediakan personalisasi berbasis lokasi

Dapatkan rekomendasi yang disesuaikan dengan preferensi pengguna dan area geografis tertentu.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Membantu perencanaan perjalanan

Buat rencana multi-hari dengan rute dan informasi tentang berbagai lokasi, yang cocok untuk aplikasi perjalanan.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Persyaratan penggunaan layanan

Bagian ini menjelaskan persyaratan penggunaan layanan untuk Grounding with Google Maps.

### Memberi tahu pengguna tentang penggunaan sumber Google Maps

Dengan setiap hasil yang Di-grounding Google Maps, Anda akan menerima sumber di `groundingChunks` yang mendukung setiap respons. Metadata berikut juga ditampilkan:

- URI sumber
- judul
- ID

Saat menampilkan hasil dari Grounding with Google Maps, Anda harus menentukan sumber Google Maps terkait, dan memberi tahu pengguna Anda tentang hal berikut:

- Sumber Google Maps harus segera mengikuti konten yang dihasilkan yang didukung oleh sumber tersebut. Konten yang dihasilkan ini juga disebut Hasil yang Di-grounding Google Maps.
- Sumber Google Maps harus dapat dilihat dalam satu interaksi pengguna.

### Menampilkan sumber Google Maps dengan link Google Maps

Untuk setiap sumber di `groundingChunks` dan di `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, pratinjau link harus dibuat dengan mengikuti persyaratan berikut:

- Atribusikan setiap sumber ke Google Maps dengan mengikuti panduan atribusi teks Google Maps
  [Google Maps](#maps-attribution-guidelines).
- Tampilkan judul sumber yang diberikan dalam respons.
- Tautkan ke sumber menggunakan `uri` atau `googleMapsUri` dari respons.

Gambar ini menunjukkan persyaratan minimum untuk menampilkan sumber dan link Google Maps.

![Perintah dengan respons yang menampilkan sumber](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=id)

Anda dapat menciutkan tampilan sumber.

![Perintah dengan respons dan sumber diciutkan](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=id)

Opsional: Tingkatkan pratinjau link dengan konten tambahan, seperti:

- Favicon [Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=id)
  disisipkan sebelum atribusi teks Google Maps.
- Foto dari URL sumber (`og:image`).

Untuk mengetahui informasi selengkapnya tentang beberapa penyedia data Google Maps dan persyaratan lisensi mereka, lihat [pemberitahuan hukum Google Maps dan Google Earth](https://www.google.com/help/legalnotices_maps/?hl=id).

### Panduan atribusi teks Google Maps

Saat Anda mengatribusikan sumber ke Google Maps dalam teks, ikuti panduan berikut:

- Jangan ubah teks Google Maps dengan cara apa pun:
  - Jangan ubah kapitalisasi Google Maps.
  - Jangan gabungkan Google Maps ke beberapa baris.
  - Jangan lokalkan Google Maps ke bahasa lain.
  - Cegah browser menerjemahkan Google Maps dengan menggunakan atribut HTML translate="no".
- Gaya teks Google Maps seperti yang dijelaskan dalam tabel berikut:

| Properti | Gaya |
| --- | --- |
| `Font family` | Roboto. Memuat font bersifat opsional. |
| `Fallback font family` | Font isi sans serif apa pun yang sudah digunakan di produk Anda atau "Sans-Serif" untuk memanggil font sistem default |
| `Font style` | Normal |
| `Font weight` | 400 |
| `Font color` | Putih, hitam (#1F1F1F), atau abu-abu (#5E5E5E). Pertahankan kontras yang dapat diakses (4.5:1) dengan latar belakang. |
| `Font size` | - Ukuran font minimum: 12sp - Ukuran font maksimum: 16sp - Untuk mempelajari sp, lihat Unit ukuran font di situs [Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normal |

#### CSS Contoh

CSS berikut merender Google Maps dengan gaya dan warna tipografi yang sesuai di latar belakang putih atau terang.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### ID tempat dan ID ulasan

Data Google Maps mencakup ID tempat dan ID ulasan. Anda dapat menyimpan cache, menyimpan, dan mengekspor data respons berikut:

- `placeId`
- `reviewId`

Pembatasan terhadap penyimpanan cache dalam Persyaratan Grounding with Google Maps tidak berlaku.

### Aktivitas dan wilayah yang dilarang

Grounding with Google Maps memiliki batasan tambahan untuk konten dan aktivitas tertentu guna mempertahankan platform yang aman dan andal. Selain batasan penggunaan
dalam [Persyaratan](https://ai.google.dev/gemini-api/terms?hl=id#grounding-with-google-maps):

- Anda tidak akan menggunakan Grounding with Google Maps untuk aktivitas berisiko tinggi, termasuk layanan tanggap darurat.
- Anda tidak akan mendistribusikan atau memasarkan aplikasi yang menawarkan Grounding with Google Maps di Wilayah yang Dilarang. Untuk mengetahui informasi selengkapnya, lihat
  [Wilayah yang Dilarang Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=id).
  Daftar Wilayah yang Dilarang dapat diperbarui dari waktu ke waktu.

## Praktik terbaik

- **Berikan lokasi pengguna:** Untuk mendapatkan respons yang paling relevan dan dipersonalisasi, selalu sertakan `user_location` (latitude dan longitude) dalam konfigurasi `googleMapsGrounding` Anda jika lokasi pengguna diketahui.
- **Beri Tahu Pengguna Akhir:** Beri tahu pengguna akhir Anda dengan jelas bahwa data Google Maps digunakan untuk menjawab kueri mereka, terutama saat alat ini diaktifkan.
- **Pantau Latensi:** Untuk aplikasi percakapan, pastikan latensi P95 untuk respons yang didasarkan tetap berada dalam batas yang dapat diterima untuk mempertahankan pengalaman pengguna yang lancar.
- **Nonaktifkan Jika Tidak Diperlukan:** Grounding with Google Maps dinonaktifkan secara default. Hanya aktifkan (`"tools": [{"googleMaps": {}}]`) jika kueri memiliki
  konteks geografis yang jelas, untuk mengoptimalkan performa dan biaya.

## Batasan

- **Cakupan Geografis:** Grounding with Google Maps tersedia secara global
- **Dukungan Model:** Lihat bagian [Model yang didukung](#supported-models).
- **Input/Output Multimodal:** Grounding with Google Maps saat ini tidak mendukung input atau output multimodal selain teks.
- **Status Default:** Alat Grounding with Google Maps dinonaktifkan secara default.
  Anda harus mengaktifkannya secara eksplisit dalam permintaan API Anda.

## Harga dan batas kapasitas

Harga Grounding with Google Maps didasarkan pada kueri. Tarif saat ini adalah **$25 / 1K perintah yang didasarkan**. Paket gratis juga memiliki hingga 500 permintaan per hari. Permintaan hanya dihitung terhadap kuota jika perintah berhasil menampilkan setidaknya satu hasil yang didasarkan Google Maps (yaitu, hasil yang berisi setidaknya satu sumber Google Maps). Jika beberapa kueri dikirim ke Google Maps dari satu permintaan, kueri tersebut akan dihitung sebagai satu permintaan terhadap batas kapasitas.

Untuk mengetahui informasi harga mendetail, lihat halaman harga [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Model yang didukung

Model berikut mendukung Grounding with Google Maps:

| Model | Grounding with Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Kombinasi alat yang didukung

Model Gemini 3 mendukung kombinasi alat bawaan (seperti Grounding with Google Maps) dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

## Langkah berikutnya

- Coba [Grounding with Google Search di Gemini API
  Buku Masak](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=id).
- Pelajari alat lain yang [tersedia](https://ai.google.dev/gemini-api/docs/tools?hl=id).
- Untuk mempelajari praktik terbaik AI yang bertanggung jawab dan filter keamanan Gemini API lebih lanjut, lihat [panduan Setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
