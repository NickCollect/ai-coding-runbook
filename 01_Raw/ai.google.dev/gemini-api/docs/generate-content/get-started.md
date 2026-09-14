---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id
fetched_at: 2026-09-14T05:52:07.228992+00:00
title: "Memulai \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Memulai

Panduan ini akan membantu Anda memulai penggunaan **generateContent** API lama. Untuk project dan aplikasi baru, sebaiknya gunakan **Interactions API** baru, yang merupakan cara terbaik dan paling sederhana untuk membangun dengan model dan agen Gemini.

Panduan memulai ini menunjukkan cara menginstal
[library](https://ai.google.dev/gemini-api/docs/libraries?hl=id) kami dan membuat permintaan pertama, melakukan streaming
respons, membuat percakapan multi-giliran, dan menggunakan alat menggunakan metode standar
`generateContent`.

## Mendapatkan kunci API

Untuk menggunakan Gemini API, Anda harus memiliki kunci API untuk mengautentikasi permintaan, menerapkan batas keamanan, dan melacak penggunaan ke akun Anda.

- Google AI Studio otomatis membuat project dan kunci API untuk pengguna baru.
  Anda dapat menyalinnya dari halaman kunci [API](https://aistudio.google.com/api-keys?hl=id).
- Jika memerlukan kunci baru, klik **Create API key** di AI Studio dan ikuti dialog untuk menambahkan pasangan kunci-project baru.

[Membuat Kunci Gemini API](https://aistudio.google.com/apikey?hl=id)

Tetapkan kunci Anda sebagai variabel lingkungan:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Mengupgrade ke paket berbayar

Mengupgrade ke paket berbayar akan meningkatkan batas frekuensi Anda dan mengharuskan Anda menyiapkan Penagihan Cloud.

- Klik **Set up billing** di halaman kunci [API](https://aistudio.google.com/api-keys?hl=id) atau [Project](https://aistudio.google.com/projects?hl=id) AI Studio.
- Ikuti dialog Penagihan Cloud untuk membuat atau menautkan akun penagihan, menambahkan metode pembayaran, dan membayar di muka minimal $10 (atau nilai mata uang yang setara) dalam kredit berbayar.
- Lihat penggunaan API Anda di [Google AI Studio](https://aistudio.google.com/usage?hl=id)
  di bagian **Dashboard** > **Usage**.

Lihat halaman [Penagihan](https://ai.google.dev/gemini-api/docs/billing?hl=id) untuk mengetahui informasi selengkapnya.

## Menginstal Google GenAI SDK

### Python

Dengan menggunakan [Python 3.9+](https://www.python.org/downloads/), instal paket
[`google-genai` menggunakan](https://pypi.org/project/google-genai/)
perintah
[pip berikut](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Dengan menggunakan [Node.js v18+](https://nodejs.org/en/download/package-manager),
instal
[Google Gen AI SDK untuk TypeScript dan JavaScript](https://www.npmjs.com/package/@google/genai)
menggunakan
[perintah npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) berikut:

```
npm install @google/genai
```

## Membuat teks

Gunakan metode `models.generate_content` untuk
[membuat respons teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Mengaktifkan respons bertahap

Secara default, model hanya menampilkan respons setelah seluruh proses pembuatan selesai. Untuk pengalaman yang lebih cepat dan interaktif, Anda dapat
[melakukan streaming potongan respons](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#stream) saat
dibuat.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Percakapan multi-giliran

Untuk percakapan multi-giliran, SDK menyediakan helper `chats` stateful untuk
membangun pengalaman [chat multi-giliran](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#chat)
yang otomatis mengelola histori percakapan.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Menggunakan alat

Perluas kemampuan model dengan
[melakukan grounding respons dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)
untuk mengakses konten web real-time. Model akan otomatis menentukan kapan harus menelusuri, menjalankan kueri, dan membuat respons.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Gemini API juga mendukung alat bawaan lainnya:

- **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**:
  Memungkinkan model menulis dan menjalankan kode Python untuk memecahkan masalah matematika yang kompleks.
- **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**: Memungkinkan Anda
  melakukan grounding respons di URL halaman web tertentu yang Anda berikan.
- **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**: Memungkinkan Anda
  mengupload file dan melakukan grounding respons dalam kontennya menggunakan penelusuran semantik.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**: Memungkinkan Anda
  melakukan grounding respons dalam data lokasi dan menelusuri tempat, rute, dan
  peta.
- **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**: Memungkinkan
  model berinteraksi dengan layar, keyboard, dan mouse komputer virtual untuk
  melakukan tugas.

## Memanggil fungsi kustom

Gunakan **[panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)** untuk menghubungkan
model ke alat dan API kustom Anda. Model akan menentukan kapan harus memanggil fungsi Anda dan menampilkan `functionCall` dalam respons agar aplikasi Anda dapat dieksekusi.

Contoh ini mendeklarasikan fungsi suhu tiruan dan memeriksa apakah model ingin memanggilnya.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Langkah berikutnya

Setelah Anda mulai menggunakan Gemini API, pelajari panduan berikut untuk membuat aplikasi yang lebih canggih:

- [Pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id)
- [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)
- [Pemahaman gambar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=id)
- [Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)
- [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
- [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=id)
- [Konteks panjang](https://ai.google.dev/gemini-api/docs/long-context?hl=id)
- [Embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-12 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-12 UTC."],[],[]]
