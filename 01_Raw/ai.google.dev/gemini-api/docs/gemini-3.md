---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=id
fetched_at: 2026-09-07T05:42:10.463200+00:00
title: "Panduan developer Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)

Kirim masukan

# Panduan developer Gemini 3

Gemini 3 adalah rangkaian model tercerdas kami hingga saat ini, yang dibangun berdasarkan penalaran canggih. Model ini dirancang untuk mewujudkan ide apa pun dengan menguasai alur kerja agentic, coding otonom, dan tugas multimodal yang kompleks.
Panduan ini membahas fitur utama rangkaian model Gemini 3 dan cara mengoptimalkan penggunaannya.

Jelajahi [koleksi aplikasi Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=id) kami untuk melihat cara model menangani penalaran tingkat lanjut, coding otonom, dan tugas multimodal yang kompleks.

Mulai dengan beberapa baris kode:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Memperkenalkan seri Gemini 3

Gemini 3.1 Pro paling cocok untuk tugas kompleks yang memerlukan pengetahuan umum yang luas dan penalaran canggih di berbagai modalitas.

Gemini 3 Flash adalah model seri 3 terbaru kami, dengan kecerdasan tingkat Pro pada kecepatan dan harga Flash.

Nano Banana Pro (juga dikenal sebagai Gemini 3 Pro Image) adalah model pembuatan gambar berkualitas tertinggi kami, dan Nano Banana 2 (juga dikenal sebagai Gemini 3.1 Flash Image) adalah model yang setara dengan volume tinggi, efisiensi tinggi, dan titik harga lebih rendah.

Gemini 3.1 Flash-Lite adalah model andalan kami yang dibuat untuk model hemat biaya dan tugas bervolume tinggi.

Semua model Gemini 3 saat ini dalam versi pratinjau.

| ID Model | Jendela Konteks (Masuk / Keluar) | Batas Informasi | Harga (Input / Output)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Jan 2025 | $0,25 (teks, gambar, video), $0,50 (audio) / $1,50 |
| **gemini-3.1-flash-image-preview** | 128 ribu / 32 ribu | Jan 2025 | $0,25 (Input Teks) / $0,067 (Output Gambar)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Jan 2025 | $2 / $12 (<200 ribu token)   $4 / $18 (>200 ribu token) |
| **gemini-3-flash-preview** | 1M / 64k | Jan 2025 | $0,50 / $3 |
| **gemini-3-pro-image-preview** | 65 ribu / 32 ribu | Jan 2025 | $2 (Input Teks) / $0,134 (Output Gambar)\*\* |

*\* Harga adalah per 1 juta token, kecuali dinyatakan lain.*
*\*\* Harga gambar bervariasi menurut resolusi. Lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detailnya.*

Untuk mengetahui batas, harga, dan informasi tambahan yang mendetail, lihat [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id).

## Fitur API baru di Gemini 3

Gemini 3 memperkenalkan parameter baru yang dirancang untuk memberi developer kontrol lebih besar atas latensi, biaya, dan kualitas multimodal.

### Tingkat pemikiran

Model seri Gemini 3 menggunakan penalaran dinamis secara default untuk memproses perintah. Anda dapat menggunakan parameter `thinking_level`, yang mengontrol
kedalaman **maksimum** dari proses penalaran internal model sebelum menghasilkan
respons. Gemini 3 memperlakukan level ini sebagai alokasi relatif untuk berpikir, bukan jaminan token yang ketat.

Jika `thinking_level` tidak ditentukan, Gemini 3 akan ditetapkan secara default ke `high`. Untuk respons yang lebih cepat dan latensi yang lebih rendah saat penalaran yang kompleks tidak diperlukan, Anda dapat membatasi tingkat pemikiran model ke `low`.

| Tingkat Penalaran | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Deskripsi |
| --- | --- | --- | --- | --- |
| **`minimal`** | Tidak didukung | Didukung (Default) | Didukung | Cocok dengan setelan "tanpa penalaran" untuk sebagian besar kueri. Model mungkin berpikir sangat minimal untuk tugas coding yang kompleks. Meminimalkan latensi untuk aplikasi chat atau throughput tinggi. Perhatikan, `minimal` tidak menjamin bahwa pemikiran tidak berfungsi. |
| **`low`** | Didukung | Didukung | Didukung | Meminimalkan latensi dan biaya. Paling cocok untuk mengikuti petunjuk sederhana, chat, atau aplikasi dengan throughput tinggi. |
| **`medium`** | Didukung | Didukung | Didukung | Pemikiran yang seimbang untuk sebagian besar tugas. |
| **`high`** | Didukung (Default, Dinamis) | Didukung (Dinamis) | Didukung (Default, Dinamis) | Memaksimalkan kedalaman penalaran. Model mungkin memerlukan waktu yang jauh lebih lama untuk mencapai token output pertama (non-pemikiran), tetapi outputnya akan lebih beralasan. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Suhu

Untuk semua model Gemini 3, sebaiknya pertahankan parameter temperatur pada nilai defaultnya, yaitu `1.0`.

Meskipun model sebelumnya sering kali diuntungkan dengan menyesuaikan temperatur untuk mengontrol kreativitas versus determinisme, kemampuan penalaran Gemini 3 dioptimalkan untuk setelan default. Mengubah suhu (menyetelnya di bawah 1.0) dapat menyebabkan perilaku yang tidak terduga, seperti perulangan atau penurunan performa, terutama dalam tugas matematika atau penalaran yang kompleks.

### Tanda tangan penalaran

Model Gemini 3 menggunakan tanda tangan pemikiran untuk mempertahankan konteks penalaran di seluruh panggilan API. Tanda tangan ini adalah representasi terenkripsi dari proses pemikiran internal model.

- **Mode Stateful (Direkomendasikan)**: Saat menggunakan Interactions API dalam mode stateful (menyediakan `previous_interaction_id`), server akan otomatis mengelola histori percakapan dan tanda tangan pemikiran.
- **Mode Tanpa Status**: Jika Anda mengelola histori percakapan secara manual, Anda harus menyertakan blok pemikiran dengan tanda tangannya dalam permintaan berikutnya untuk memvalidasi keaslian.

Untuk mengetahui informasi mendetail, lihat halaman [Tanda Tangan Pikiran](https://ai.google.dev/gemini-api/docs/thinking?hl=id).`

### Output Terstruktur dengan alat

Model Gemini 3 memungkinkan Anda menggabungkan [Output Terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) dengan alat bawaan, termasuk
[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id), [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id), [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), dan [Pemanggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Pembuatan gambar

Gemini 3.1 Flash Image dan Gemini 3 Pro Image memungkinkan Anda membuat dan mengedit gambar dari perintah teks. Model ini menggunakan penalaran untuk "memikirkan" perintah dan dapat mengambil data real-time—seperti prakiraan cuaca atau diagram saham—sebelum menggunakan perujukan [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) sebelum membuat gambar dengan fidelitas tinggi.

**Kemampuan baru & yang ditingkatkan:**

- **Rendering teks & 4K:** Buat teks dan diagram yang jelas dan mudah dibaca dengan resolusi hingga 2K dan 4K.
- **Pembuatan dengan perujukan:** Gunakan alat `google_search` untuk memverifikasi fakta dan membuat gambar berdasarkan informasi dunia nyata. Grounding dengan Google *Penelusuran Gambar*
  tersedia untuk Gemini 3.1 Flash Image.
- **Pengeditan via percakapan:** Pengeditan gambar multi-turn hanya dengan meminta perubahan (misalnya, "Buat latar belakangnya menjadi matahari terbenam"). Alur kerja ini mengandalkan
  **Tanda Pikiran** untuk mempertahankan konteks visual di antara giliran.

Untuk mengetahui detail lengkap tentang rasio aspek, alur kerja pengeditan, dan opsi konfigurasi, lihat [panduan Pembuatan Gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Contoh Respons**

![Cuaca Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=id)

### Eksekusi Kode dengan gambar

Gemini 3 Flash dapat memperlakukan penglihatan sebagai investigasi aktif, bukan hanya sekilas
statis. Dengan menggabungkan penalaran dengan [eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), model merumuskan rencana, lalu menulis dan
mengeksekusi kode Python untuk memperbesar, memangkas, memberi anotasi, atau memanipulasi gambar
langkah demi langkah untuk mendasarkan jawabannya secara visual.

**Kasus penggunaan:**

- **Zoom dan periksa:** Model secara implisit mendeteksi saat detail terlalu kecil (misalnya, membaca pengukur atau nomor seri dari jarak jauh) dan menulis kode untuk memangkas dan memeriksa ulang area tersebut pada resolusi yang lebih tinggi.
- **Matematika dan pemetaan visual:** Model dapat menjalankan perhitungan multi-langkah menggunakan
  kode (misalnya, menjumlahkan item baris pada tanda terima, atau membuat diagram Matplotlib
  dari data yang diekstrak).
- **Anotasi gambar:** Model dapat menggambar panah, kotak pembatas, atau anotasi lain langsung pada gambar untuk menjawab pertanyaan spasial seperti "Ke mana item ini harus diletakkan?".

Untuk mengaktifkan pemikiran visual, konfigurasi [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) sebagai alat. Model akan otomatis menggunakan
kode untuk memanipulasi gambar jika diperlukan.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Untuk mengetahui detail selengkapnya tentang eksekusi kode dengan gambar, lihat [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id#images).

### Respons fungsi multimodal

[Panggilan fungsi multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#multimodal)
memungkinkan pengguna mendapatkan respons fungsi yang berisi
objek multimodal sehingga meningkatkan pemanfaatan kemampuan panggilan fungsi model. Panggilan fungsi standar hanya mendukung respons fungsi berbasis teks:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Menggabungkan alat bawaan dan panggilan fungsi

Gemini 3 memungkinkan penggunaan alat bawaan (seperti Google Penelusuran, konteks URL, dan [lainnya](https://ai.google.dev/gemini-api/docs/tools?hl=id)) serta alat [pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) kustom dalam panggilan API yang sama, sehingga memungkinkan alur kerja yang lebih kompleks.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Migrasi dari Gemini 2.5

Gemini 3 adalah rangkaian model tercanggih kami hingga saat ini dan menawarkan peningkatan bertahap dibandingkan Gemini 2.5. Saat melakukan migrasi, pertimbangkan hal berikut:

- **Penalaran:** Jika sebelumnya Anda menggunakan rekayasa perintah yang rumit (seperti
  rantai pemikiran) untuk memaksa Gemini 2.5 melakukan penalaran, coba Gemini 3 dengan
  `thinking_level: "high"` dan perintah yang disederhanakan.
- **Setelan temperatur:** Jika kode yang ada secara eksplisit menetapkan temperatur (terutama ke nilai rendah untuk output determenistik), sebaiknya hapus parameter ini dan gunakan nilai default Gemini 3 sebesar 1.0 untuk menghindari potensi masalah loop atau penurunan performa pada tugas yang kompleks.
- **Pemahaman PDF & dokumen:**
  Jika Anda mengandalkan perilaku tertentu untuk parsing dokumen padat, uji setelan
  `media_resolution_high` baru untuk memastikan akurasi yang berkelanjutan.
- **Penggunaan token:** Bermigrasi ke setelan default Gemini 3 dapat **meningkatkan** penggunaan token untuk PDF, tetapi **menurunkan** penggunaan token untuk video. Jika permintaan kini melebihi
  jendela konteks karena resolusi default yang lebih tinggi, sebaiknya kurangi resolusi media secara eksplisit.
- **Segmentasi gambar:** Kemampuan segmentasi gambar (menampilkan mask tingkat piksel untuk objek) tidak didukung di Gemini 3 Pro atau Gemini 3 Flash. Untuk beban kerja yang memerlukan segmentasi gambar bawaan, sebaiknya terus gunakan Gemini 2.5 Flash dengan fitur berpikir dinonaktifkan.
- **Penggunaan Komputer:** Gemini 3 Pro dan Gemini 3 Flash mendukung [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id). Tidak seperti seri 2.5, Anda tidak perlu menggunakan model terpisah untuk mengakses alat Penggunaan Komputer.
- **Dukungan alat**: [Menggabungkan alat bawaan dengan pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) kini didukung untuk model Gemini 3. [Perujukan Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) kini juga didukung untuk model Gemini 3.

## Kompatibilitas OpenAI

Untuk pengguna yang memanfaatkan [lapisan kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id),
parameter standar (`reasoning_effort` OpenAI) secara otomatis dipetakan ke
padanan Gemini (`thinking_level`).

## Praktik terbaik pembuatan perintah

Gemini 3 adalah model penalaran, yang mengubah cara Anda memberikan perintah.

- **Petunjuk yang presisi:** Berikan perintah input yang ringkas. Gemini 3 merespons
  paling baik terhadap petunjuk yang langsung dan jelas. Model ini mungkin menganalisis secara berlebihan teknik rekayasa perintah yang panjang atau terlalu kompleks yang digunakan untuk model lama.
- **Panjang output:** Secara default, Gemini 3 tidak terlalu panjang dan lebih suka memberikan jawaban yang langsung dan efisien. Jika kasus penggunaan Anda memerlukan persona yang lebih
  percakapan atau "ramah", Anda harus secara eksplisit mengarahkan model dalam
  perintah (misalnya, "Jelaskan ini sebagai asisten yang ramah dan suka berbicara").
- **Pengelolaan konteks:** Saat bekerja dengan set data besar (misalnya, seluruh buku, codebase, atau video panjang), tempatkan petunjuk atau pertanyaan spesifik Anda di akhir perintah, setelah konteks data. Berikan dasar penalaran model pada data yang diberikan dengan memulai pertanyaan Anda dengan frasa seperti, "Berdasarkan informasi sebelumnya...".

Pelajari lebih lanjut strategi desain perintah dalam [panduan rekayasa perintah](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id).

## FAQ

1. **Apa batas waktu pengetahuan untuk Gemini 3?** Model Gemini 3 memiliki batas pengetahuan hingga Januari 2025. Untuk informasi terbaru, gunakan alat
   [Perujukan Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id).
2. **What are the context window limits?** Model Gemini 3 mendukung jendela konteks input 1 juta token dan output hingga 64 ribu token.
3. **Apakah ada paket gratis untuk Gemini 3?** Gemini 3 Flash
   `gemini-3-flash-preview` memiliki paket gratis di Gemini API. Anda dapat mencoba Gemini 3.1 Pro dan 3 Flash tanpa biaya di Google AI Studio, tetapi tidak ada paket gratis yang tersedia untuk `gemini-3.1-pro-preview` di Gemini API.
4. **Apakah kode `thinking_budget` lama saya masih berfungsi?** Ya, `thinking_budget` masih didukung untuk kompatibilitas mundur, tetapi sebaiknya lakukan migrasi ke `thinking_level` untuk performa yang lebih dapat diprediksi. Jangan gunakan keduanya dalam permintaan yang sama.
5. **Apakah Gemini 3 mendukung Batch API?** Ya, Gemini 3 mendukung
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id).
6. **Apakah Context Caching didukung?** Ya, [Penyimpanan Cache Konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id) didukung untuk Gemini 3.
7. **Alat mana yang didukung di Gemini 3?** Gemini 3 mendukung
   [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id),
   [Perujukan dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id),
   [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id),
   [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id), dan
   [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id). Hal ini juga mendukung
   [Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) standar untuk
   alat kustom Anda sendiri, dan
   [dikombinasikan dengan alat bawaan](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).
8. **Apa itu `gemini-3.1-pro-preview-customtools`?** Jika Anda menggunakan
   `gemini-3.1-pro-preview` dan model mengabaikan alat kustom Anda dan lebih memilih
   perintah bash, coba gunakan model `gemini-3.1-pro-preview-customtools`.
   Info selengkapnya [di sini][customtools-model].

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-08-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-08-19 UTC."],[],[]]
