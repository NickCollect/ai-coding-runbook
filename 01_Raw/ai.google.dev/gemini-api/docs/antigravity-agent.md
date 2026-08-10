---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id
fetched_at: 2026-08-10T03:15:02.514641+00:00
title: "Agen Antigravitasi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen Antigravitasi

Agen Antigravity adalah agen terkelola tujuan umum di Gemini API. Satu panggilan API memberi Anda agen yang dapat melakukan penalaran, mengeksekusi kode, mengelola file, dan menjelajahi web di dalam sandbox Linux aman Anda sendiri, yang dihosting oleh Google.

Gemini Code Assist didukung oleh Gemini 3.6 Flash dan menggunakan harness yang sama dengan Antigravity IDE. Anda dapat mengonfigurasi model Gemini yang mendasarinya menggunakan `agent_config`. Tersedia melalui [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) dan [Google AI Studio](https://aistudio.google.com?hl=id).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Kemampuan

Setiap panggilan dapat menyediakan sandbox Linux dan memulai loop penggunaan alat. Agen merencanakan, bertindak, mengamati hasil, dan mengulangi hingga tugas selesai.

- **Eksekusi kode:** Jalankan perintah Bash, Python, dan Node.js. Menginstal paket, menjalankan pengujian, membangun aplikasi.
- **Pengelolaan file:** Membaca, menulis, mengedit, menelusuri, dan mencantumkan file di sandbox. File tetap ada di seluruh interaksi.
- **Akses web:** Google Penelusuran dan pengambilan URL untuk data.
- **Pemadatan konteks:** Pemadatan konteks otomatis (dipicu pada ~135 ribu token) untuk mendukung sesi multi-turn yang berjalan lama tanpa kehilangan konteks atau mencapai batas token.

Lihat [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id) untuk penggunaan dan streaming multi-giliran.

## Alat yang didukung

Secara default, agen memiliki akses ke `code_execution`, `google_search`, dan `url_context`. Alat sistem file diaktifkan secara otomatis saat Anda menentukan parameter `environment`. Anda juga dapat menentukan **fungsi kustom** untuk menghubungkan agen ke API dan alat Anda sendiri. Anda hanya perlu menentukan parameter `tools` saat menyesuaikan atau membatasi set default, atau saat menambahkan fungsi kustom.

| Alat | Nilai jenis | Deskripsi |
| --- | --- | --- |
| Eksekusi Kode | `code_execution` | Jalankan perintah shell (bash, Python, Node) dengan pengambilan stdout/stderr. |
| Google Penelusuran | `google_search` | Telusuri web publik. |
| Konteks URL | `url_context` | Mengambil dan membaca halaman web. |
| Filesystem | *(diaktifkan melalui `environment`)* | Membaca, menulis, mengedit, menelusuri, dan mencantumkan file di sandbox. Sistem mengaktifkan alat ini secara otomatis saat Anda menyetel `environment`. |
| Fungsi Kustom | `function` | Tentukan fungsi kustom yang dapat diminta agen untuk dieksekusi. Lihat [Pemanggilan fungsi](#function-calling). |
| Server MCP Jarak Jauh | `mcp_server` | Mendaftarkan server Model Context Protocol (MCP) eksternal sebagai alat. Lihat [server MCP](#mcp-servers). |

Anda dapat mencegat dan memvalidasi eksekusi alat `code_execution` dan `filesystem` langsung di dalam sandbox jarak jauh menggunakan [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=id) sinkron.

Untuk membatasi agen ke alat tertentu, teruskan hanya alat yang Anda butuhkan:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Input Multimodal

Agen Antigravity mendukung input multimodal. Saat ini, hanya input `text` dan `image` yang didukung. Gambar harus diberikan sebagai string berenkode base64 inline (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Panggilan fungsi

Panggilan fungsi memungkinkan Anda menghubungkan agen Antigravity ke API dan database eksternal dengan menentukan alat kustom yang dapat dipanggil agen. Untuk mengetahui konsep umumnya, lihat [Panggilan fungsi dengan Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id).

Contoh berikut menunjukkan interaksi 2 putaran. Agen pertama-tama meminta panggilan fungsi `get_weather` kustom, dan klien mengeksekusinya serta menampilkan hasilnya pada giliran kedua.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Server MCP

Anda dapat menghubungkan agen Antigravity ke alat eksternal dengan mendaftarkan server Model Context Protocol (MCP) jarak jauh. Agen mendukung server MCP jarak jauh melalui HTTP yang dapat di-streaming.

Saat mendaftarkan server MCP, Anda harus menentukan kolom berikut dalam array `tools`:

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `type` | string | Ya | Harus berupa `"mcp_server"`. |
| `name` | string | Ya | ID unik untuk server. Harus huruf kecil dan alfanumerik (cocok dengan `^[a-z0-9_-]+$`). |
| `url` | string | Ya | URL endpoint server MCP jarak jauh. |
| `headers` | objek | Tidak | Header kustom (misalnya, autentikasi) yang dikirim dengan permintaan. |
| `allowed_tools` | array | Tidak | Daftar nama alat yang diizinkan untuk dieksekusi. Jika tidak disertakan, semua alat diizinkan. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Pemilihan model

Untuk `antigravity-preview-05-2026`, model defaultnya adalah **Gemini 3.6 Flash** (`gemini-3.6-flash`). Jika Anda tidak menyertakan `agent_config`, agen akan menggunakan `gemini-3.6-flash` sebagai default.

Anda dapat mengonfigurasi model Gemini yang mendasarinya menggunakan `agent_config` untuk mengoptimalkan kecepatan, biaya, atau kemampuan penalaran.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

Nilai yang didukung untuk `agent_config.model` adalah:

| Model | Nilai dalam `agent_config.model` | Deskripsi |
| --- | --- | --- |
| **Gemini 3.6 Flash** (default) | `gemini-3.6-flash` | Model seimbang default untuk penalaran, coding, dan penggunaan alat. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Model Flash generasi sebelumnya untuk alur kerja agentic umum. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Model ringan yang dioptimalkan untuk tugas-tugas yang sensitif terhadap biaya dan latensi rendah. |

Saat membuat agen terkelola dengan `agents.create`, Anda mengonfigurasi model dengan cara yang sama persis dengan meneruskan `base_agent` dan `agent_config`. Perhatikan bahwa Anda tidak dapat mengganti model pada waktu interaksi untuk agen terkelola yang dibuat dengan `agents.create`. Model dikunci ke setelan yang ditetapkan saat agen dibuat. Hal ini memastikan perilaku panggilan alat yang dapat diprediksi, proses debug yang konsisten, dan kepatuhan terhadap batas keamanan.

## Menyesuaikan agen

Anda dapat memperluas agen Antigravity dengan menyesuaikan petunjuk, alat, dan lingkungannya. Agen mendukung pendekatan native sistem file untuk penyesuaian: Anda dapat memuat file seperti `AGENTS.md` untuk petunjuk dan kemampuan di `.agents/skills/` langsung ke sandbox, atau meneruskan konfigurasi inline pada waktu interaksi. Anda dapat melakukan iterasi pada konfigurasi secara inline, lalu menyimpannya sebagai agen terkelola saat sudah siap.

Untuk mengetahui detail lengkap tentang cara membuat agen kustom, lihat [Membangun Agen Terkelola](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id).

## Eksekusi latar belakang

Tugas agen yang melibatkan penalaran multi-langkah, eksekusi kode, atau operasi file dapat memerlukan waktu beberapa menit untuk diselesaikan. Gunakan `background=True` untuk menjalankan interaksi secara asinkron. API akan langsung menampilkan ID interaksi yang Anda polling hingga statusnya `completed` atau `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

Eksekusi latar belakang memerlukan `store=True`, yang merupakan setelan default. Untuk update progres real-time selama eksekusi latar belakang, lihat [Streaming interaksi latar belakang](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=id#streaming-background).

Anda dapat membatalkan interaksi latar belakang yang sedang berjalan menggunakan metode `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Multi-turn dengan eksekusi latar belakang**

Jika interaksi latar belakang melibatkan alat stateful (seperti eksekusi kode di sandbox), gunakan `environment_id` dari interaksi yang telah selesai untuk melanjutkan di lingkungan yang sama. Tindakan ini memastikan agen melanjutkan dari tempat terakhir kali berhenti dengan semua file dan status tetap utuh.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Lingkungan

Setiap panggilan membuat atau menggunakan kembali sandbox Linux. Parameter `environment` memiliki tiga bentuk:

| Formulir | Deskripsi |
| --- | --- |
| `"remote"` | Sediakan sandbox baru dengan setelan default. |
| `"env_abc123"` | Menggunakan kembali lingkungan yang ada berdasarkan ID, dengan mempertahankan semua file dan status. |
| `{...}` | Penuh `EnvironmentConfig` dengan sumber dan aturan jaringan kustom. |

Lihat [Environments](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id) untuk mengetahui detail tentang sumber (Git, GCS, inline), jaringan, siklus proses, dan batas resource.

## Pemicu

Pemicu memungkinkan Anda menjadwalkan agen untuk berjalan secara otomatis sesuai jadwal cron. Pemicu mengikat agen, lingkungan, perintah, dan jadwal ke dalam resource persisten yang diaktifkan tanpa intervensi manual. Setiap eksekusi menggunakan kembali lingkungan yang sama, sehingga file yang dibuat dalam satu eksekusi akan tetap ada dan terlihat oleh eksekusi berikutnya.

### Buat pemicu

Buat pemicu dengan menentukan jadwal cron, zona waktu, dan konfigurasi interaksi. Pemicu dimulai dalam status `active` dan akan diaktifkan pada waktu cron yang cocok berikutnya. Simpan `id` yang ditampilkan untuk mengelola pemicu dalam panggilan berikutnya.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

Permintaan `CreateTrigger` menerima kolom berikut:

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `schedule` | string | Ya | Ekspresi cron (misalnya, `0 * * * *` untuk setiap jam, `0 9 * * 1-5` untuk pagi hari pada hari kerja). |
| `time_zone` | string | Ya | Zona waktu IANA (misalnya, `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | string | Tidak | Nama pemicu yang dapat dibaca manusia. |
| `max_consecutive_failures` | bilangan bulat | Tidak | Jumlah kegagalan maksimum sebelum pemicu dijeda secara otomatis. Default: 5. |
| `execution_timeout_seconds` | bilangan bulat | Tidak | Waktu tunggu per eksekusi dalam detik. Default: 600. |
| `interaction` | objek | Ya | `CreateInteractionRequest` yang menentukan agen, input, alat, dan lingkungan. |

Respons mencakup kolom kunci berikut:

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `id` | string | ID unik untuk pemicu. Gunakan ini di semua operasi berikutnya. |
| `status` | string | Status saat ini: `active`, `paused`, atau `disabled`. |
| `next_run_time` | string | Stempel waktu ISO 8601 untuk eksekusi terjadwal berikutnya. |
| `consecutive_failure_count` | bilangan bulat | Jumlah eksekusi gagal berturut-turut sejak keberhasilan terakhir. |

### Mencantumkan pemicu

Mengambil semua pemicu yang terkait dengan project Anda.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Mendapatkan pemicu

Mengambil konfigurasi lengkap dan status saat ini dari satu pemicu.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Jeda dan lanjutkan

Anda dapat menjeda pemicu untuk menghentikan eksekusi terjadwal, dan melanjutkannya untuk mengaktifkan kembali jadwal. Menjeda tidak memengaruhi eksekusi manual.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Menghapus pemicu

Menghapus pemicu secara permanen. Histori eksekusi sebelumnya tidak dihapus.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Menjalankan pemicu secara langsung

Aktifkan pemicu sesuai permintaan tanpa menunggu waktu yang dijadwalkan berikutnya. Hal ini berfungsi meskipun pemicu dijeda.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Mencantumkan eksekusi

Melihat histori eksekusi untuk pemicu. Setiap eksekusi mencakup `status`, stempel waktu, `interaction_id` yang dapat Anda gunakan untuk mengambil output interaksi lengkap, dan `environment_id` yang mengonfirmasi bahwa semua proses berbagi sandbox yang sama.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Ketersediaan dan harga

Agen Antigravity tersedia dalam pratinjau melalui
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) di Google AI Studio
dan Gemini API untuk project paket gratis dan paket berbayar.

Harga mengikuti [model bayar sesuai penggunaan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing-for-agents)
berdasarkan token model Gemini yang mendasarinya dan alat yang digunakan agen. Tidak seperti permintaan chat standar yang menghasilkan satu output, interaksi Antigravity adalah alur kerja berbasis agen. Satu permintaan memicu loop penalaran, eksekusi alat, menjalankan kode, dan pengelolaan file yang otonom. Project tingkat gratis mencakup batas frekuensi dan kuota penggunaan gratis.

Interaksi antigravitasi menjalankan loop otonom multi-turn dan dapat menggunakan token dalam jumlah besar. Tetapkan [kontrol anggaran](#budget-controls) pada permintaan Anda untuk membatasi penggunaan token. Anda juga dapat memantau progres secara real time dengan
[streaming SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=id), atau membatalkan permintaan yang sedang berjalan.

### Kontrol anggaran

Selain [pemilihan model](#model-selection), tetapkan `max_total_tokens` di dalam `agent_config` (dengan `"type": "antigravity"`) untuk membatasi
total jumlah token (input + output + penalaran) yang dapat digunakan oleh interaksi.
Token yang di-cache tidak diperhitungkan dalam batas ini. Saat agen mencapai batas, interaksi akan berhenti dan kembali dengan `status: "incomplete"`. Batas ini adalah upaya terbaik:
penggunaan sebenarnya mungkin sedikit melebihi batas tersebut, bergantung pada waktu saat agen memeriksa anggaran
di antara langkah-langkah.

Tetapkan anggaran pada permintaan interaksi di `agent_config` bersama dengan `agent` dan `input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Melanjutkan interaksi yang belum selesai

Saat interaksi menampilkan `status: "incomplete"`, tugas dan konteks agen
dipertahankan. Kirim interaksi baru yang mereferensikan interaksi asli `id` dan
`environment_id` untuk melanjutkan dari tempat terakhir. Interaksi baru mendapatkan anggaran
`max_total_tokens` sendiri.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Perkiraan biaya

Biaya bervariasi berdasarkan kompleksitas tugas. Agen secara mandiri menentukan jumlah panggilan alat, eksekusi kode, dan operasi file yang diperlukan. Estimasi berikut didasarkan pada proses.

| Kategori tugas | Token input | Token output | Biaya standar |
| --- | --- | --- | --- |
| **Riset & sintesis informasi** | 100 ribu–500 ribu | 10.000–40.000 | Rp4.500–Rp15.000 |
| **Pembuatan dokumen & konten** | 100 ribu–500 ribu | 15 ribu–50 ribu | Rp4.500–Rp19.500 |
| **Desain proses & sistem** | 100 ribu–400 ribu | 10.000–30.000 | Rp3.500–Rp11.000 |
| **Pemrosesan & analisis data** | 300 ribu–3 juta | 30.000–150.000 | Rp10.000–Rp45.000 |

50–70% token input biasanya di-cache. Alur kerja kompleks dengan banyak panggilan alat dapat mengakumulasi 3–5 juta token dalam satu interaksi, dengan biaya hingga sekitar$5.

**Komputasi lingkungan** (CPU, memori, eksekusi sandbox) **tidak ditagih** selama periode pratinjau.

## Batasan

- **Status pratinjau:** Agen Antigravity dan Interactions API. Fitur dan skema dapat berubah.
- **Konfigurasi pembuatan yang tidak didukung:** Parameter berikut tidak didukung dan menampilkan error 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Output terstruktur:** Agen Antigravity tidak mendukung output terstruktur.
- **Alat yang tidak tersedia:** `file_search`, `computer_use`, dan `google_maps` belum didukung.
- **Batasan MCP jarak jauh:** Transpor Peristiwa yang Dikirim Server (SSE) tidak didukung (gunakan HTTP yang Dapat Di-stream). Selain itu, server `name` harus berupa huruf kecil dan alfanumerik (menggunakan huruf besar akan memicu error `400 Bad Request` umum).
- **Alat sistem file:** Saat ini tidak ada alat sistem file. Ini adalah bagian dari `environment`.
- **Persyaratan penyimpanan:** Eksekusi agen menggunakan `background=True` memerlukan `store=True`.
- **Panggilan fungsi hanya stateful:** Panggilan fungsi hanya didukung dalam mode stateful. Anda harus menggunakan `previous_interaction_id` untuk melanjutkan giliran; merekonstruksi histori secara manual (mode stateless) tidak didukung.
- **Jenis multimodal yang tidak didukung.** Input audio, video, dan dokumen saat ini tidak didukung. Hanya teks dan gambar yang diizinkan.

## Langkah berikutnya

- [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id): percakapan multi-turn dan streaming.
- [Membangun Agen Kustom](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id): petunjuk kustom, keterampilan, dan menyimpan agen.
- [Lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id): konfigurasi sandbox, sumber, jaringan.
- [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=id): menerapkan gerbang keamanan dan validasi efek samping di dalam sandbox.
- [Agen Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id): tugas riset panjang.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id): API yang mendasarinya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
