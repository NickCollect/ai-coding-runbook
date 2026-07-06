---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=id
fetched_at: 2026-07-06T05:06:19.479583+00:00
title: "Agen Deep Research Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen Deep Research Gemini

Agen Deep Research Gemini secara mandiri merencanakan, menjalankan, dan menyintesis tugas riset multi-langkah. Didukung oleh Gemini, fitur ini menavigasi lanskap informasi yang kompleks untuk menghasilkan laporan mendetail yang disertai kutipan. Kemampuan baru memungkinkan Anda merencanakan secara kolaboratif dengan agen, terhubung ke alat eksternal menggunakan server MCP, menyertakan visualisasi (seperti diagram dan grafik), dan memberikan dokumen secara langsung sebagai input.

Tugas riset melibatkan penelusuran dan pembacaan iteratif dan dapat memerlukan waktu beberapa menit untuk diselesaikan. Anda harus menggunakan [eksekusi di latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) (tetapkan `background=true`)
untuk menjalankan agen secara asinkron dan melakukan polling untuk hasil atau streaming update. Lihat
[Menangani tugas yang berjalan lama](#long-running-tasks) untuk mengetahui detail selengkapnya.

Contoh berikut menunjukkan cara memulai tugas riset di latar belakang
dan melakukan polling untuk mendapatkan hasil.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Versi yang Didukung

Agen Deep Research hadir dalam dua versi:

- **Deep Research** (`deep-research-preview-04-2026`): Didesain untuk kecepatan dan efisiensi, ideal untuk di-streaming kembali ke UI klien.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Komprehensivitas maksimum untuk pengumpulan dan sintesis konteks otomatis.

## Perencanaan kolaboratif

Perencanaan kolaboratif memberi Anda kontrol atas arah riset
sebelum agen memulai pekerjaannya. Jika diaktifkan, agen akan menampilkan rencana riset yang diusulkan, bukan langsung menjalankannya. Kemudian, Anda dapat meninjau, mengubah, atau menyetujui rencana melalui interaksi multi-giliran.

### Langkah 1: Minta paket

Tetapkan `collaborative_planning=True` dalam interaksi pertama. Agen
mengembalikan rencana riset, bukan laporan lengkap.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Langkah 2: Sempurnakan rencana (opsional)

Gunakan `previous_interaction_id` untuk melanjutkan percakapan dan melakukan iterasi pada rencana. Tetap tekan `collaborative_planning=True` untuk tetap berada dalam mode perencanaan.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Langkah 3: Setujui dan jalankan

Tetapkan `collaborative_planning=False` (atau hapus) untuk menyetujui rencana dan memulai riset.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Visualisasi

Jika `visualization` disetel ke `"auto"`, agen dapat membuat diagram, grafik, dan elemen visual lainnya untuk mendukung temuan risetnya.
Gambar yang dihasilkan disertakan dalam langkah-langkah respons dan di-streaming sebagai delta `image`. Untuk hasil terbaik, minta visual secara eksplisit dalam kueri Anda — misalnya, "Sertakan diagram yang menunjukkan tren dari waktu ke waktu" atau "Buat grafik yang membandingkan pangsa pasar". Menetapkan `visualization` ke
`"auto"` mengaktifkan kemampuan, tetapi agen hanya menghasilkan visual
saat perintah memintanya.

### Python

```
import base64

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Alat yang didukung

Deep Research mendukung beberapa alat bawaan dan eksternal. Secara default
(jika tidak ada parameter `tools`), agen memiliki akses ke Google
Penelusuran, Konteks URL, dan Eksekusi Kode. Anda dapat secara eksplisit
menentukan alat untuk membatasi atau memperluas kemampuan agen.

| Alat | Nilai jenis | Deskripsi |
| --- | --- | --- |
| Google Penelusuran | `google_search` | Telusuri web publik. Diaktifkan secara default. |
| Konteks URL | `url_context` | Membaca dan merangkum konten halaman web. Diaktifkan secara default. |
| Eksekusi Kode | `code_execution` | Jalankan kode untuk melakukan penghitungan dan analisis data. Diaktifkan secara default. |
| Server MCP | `mcp_server` | Terhubung ke server MCP jarak jauh untuk akses alat eksternal. |
| Penelusuran File | `file_search` | Menelusuri korpora dokumen yang Anda upload. |

### Google Penelusuran

Aktifkan Google Penelusuran secara eksplisit sebagai satu-satunya alat:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Konteks URL

Memberi agen kemampuan untuk membaca dan meringkas halaman web tertentu:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Eksekusi Kode

Mengizinkan agen mengeksekusi kode untuk penghitungan dan analisis data:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Server MCP

Berikan `name` dan `url` server dalam konfigurasi alat. Anda juga dapat meneruskan kredensial autentikasi dan membatasi alat yang dapat dipanggil agen.

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `type` | `string` | Ya | Harus berupa `"mcp_server"`. |
| `name` | `string` | Tidak | Nama tampilan untuk server MCP. |
| `url` | `string` | Tidak | URL lengkap untuk endpoint server MCP. |
| `headers` | `object` | Tidak | Pasangan nilai kunci yang dikirim sebagai header HTTP dengan setiap permintaan ke server (misalnya, token autentikasi). |
| `allowed_tools` | `array` | Tidak | Membatasi alat dari server yang dapat dipanggil oleh agen. |

#### Penggunaan dasar

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Penelusuran File

Beri agen akses ke data Anda sendiri menggunakan alat [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Kemampuan pengarahan dan pemformatan

Anda dapat mengarahkan output agen dengan memberikan petunjuk pemformatan tertentu
dalam perintah Anda. Hal ini memungkinkan Anda menyusun laporan ke dalam bagian dan subbagian tertentu, menyertakan tabel data, atau menyesuaikan gaya bahasa untuk audiens yang berbeda (misalnya, "teknis", "eksekutif", "santai").

Tentukan format output yang diinginkan secara eksplisit dalam teks input Anda.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Input multimodal

Deep Research mendukung input multimodal, termasuk gambar dan dokumen (PDF), sehingga memungkinkan agen menganalisis konten visual dan melakukan riset berbasis web yang dikontekstualisasi oleh input yang diberikan.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Pemahaman dokumen

Teruskan dokumen secara langsung sebagai input multimodal. Agen menganalisis dokumen yang diberikan dan melakukan riset berdasarkan kontennya.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Menangani tugas yang berjalan lama

Deep Research adalah proses multi-langkah yang melibatkan perencanaan, penelusuran, pembacaan, dan penulisan. Siklus ini biasanya melampaui batas waktu tunggu standar panggilan API sinkron.

Agen wajib menggunakan `background=True`. API segera menampilkan objek
`Interaction` parsial. Anda dapat menggunakan properti `id` untuk mengambil
interaksi untuk polling. Status interaksi akan bertransisi dari
`in_progress` ke `completed` atau `failed`. Untuk panduan komprehensif tentang mengelola tugas latar belakang, lihat [Eksekusi latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id).

### Streaming

Deep Research mendukung streaming untuk menerima pembaruan real-time tentang progres riset, termasuk ringkasan pemikiran, output teks, dan gambar yang dihasilkan.
Anda harus menetapkan `stream=True` dan `background=True`.

Untuk menerima langkah-langkah penalaran (pemikiran) dan info terbaru progres,
Anda harus mengaktifkan **ringkasan pemikiran** dengan menetapkan `thinking_summaries` ke
`"auto"` di `agent_config`. Tanpa ini, aliran data hanya dapat memberikan hasil akhir.

#### Jenis peristiwa streaming

| Jenis peristiwa | Jenis delta | Deskripsi |
| --- | --- | --- |
| `step.delta` | `thought` | Langkah penalaran perantara dari agen. |
| `step.delta` | `text` | Bagian dari output teks akhir. |
| `step.delta` | `image` | Gambar yang dihasilkan (berenkode base64). |

Contoh berikut memulai tugas riset dan memproses streaming dengan
koneksi ulang otomatis. Objek ini melacak `interaction_id` dan `last_event_id` sehingga
jika koneksi terputus (misalnya, setelah waktu tunggu 600 detik), objek tersebut dapat
melanjutkan dari tempat terakhir.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Pertanyaan dan interaksi lanjutan

Anda dapat melanjutkan percakapan setelah agen menampilkan laporan akhir dengan
menggunakan `previous_interaction_id`. Dengan begitu, Anda dapat meminta klarifikasi, meringkas, atau menguraikan bagian tertentu dari riset tanpa memulai ulang seluruh tugas.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Kapan harus menggunakan Agen Deep Research Gemini

Deep Research adalah **agen**, bukan hanya model. Cara ini paling cocok untuk workload yang memerlukan pendekatan "analis dalam kotak" daripada chat latensi rendah.

| Fitur | Model Gemini Standar | Agen Deep Research Gemini |
| --- | --- | --- |
| **Latensi** | Detik | Menit (Asinkron/Latar Belakang) |
| **Proses** | Buat -> Output | Rencanakan -> Cari -> Baca -> Lakukan iterasi -> Output |
| **Output** | Teks percakapan, kode, ringkasan singkat | Laporan mendetail, analisis panjang, tabel perbandingan |
| **Paling Cocok untuk** | Chatbot, ekstraksi, penulisan kreatif | Analisis pasar, uji tuntas, tinjauan pustaka, lanskap kompetitif |

## Konfigurasi agen

Deep Research menggunakan parameter `agent_config` untuk mengontrol perilaku.
Teruskan sebagai kamus dengan kolom berikut:

| Kolom | Jenis | Default | Deskripsi |
| --- | --- | --- | --- |
| `type` | `string` | Wajib | Harus berupa `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Setel ke `"auto"` untuk menerima langkah-langkah penalaran perantara selama streaming. Setel ke `"none"` untuk menonaktifkan. |
| `visualization` | `string` | `"auto"` | Setel ke `"auto"` untuk mengaktifkan diagram dan gambar yang dibuat agen. Setel ke `"off"` untuk menonaktifkan. |
| `collaborative_planning` | `boolean` | `false` | Setel ke `true` untuk mengaktifkan peninjauan rencana multi-putaran sebelum riset dimulai. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Ketersediaan dan harga

Anda dapat mengakses Agen Riset Mendalam Gemini menggunakan Interactions API di Google AI Studio dan Gemini API.

Harga mengikuti [model bayar sesuai penggunaan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing-for-agents) berdasarkan model Gemini yang mendasarinya dan alat spesifik yang digunakan agen. Tidak seperti permintaan chat standar, yang menghasilkan satu output, tugas Deep Research adalah alur kerja agentic. Satu permintaan memicu loop otonom perencanaan, penelusuran, pembacaan, dan penalaran.

### Perkiraan biaya

Biaya bervariasi berdasarkan kedalaman riset yang diperlukan. Agen secara otonom menentukan seberapa banyak membaca dan penelusuran yang diperlukan untuk menjawab perintah Anda.

- **Deep Research** (`deep-research-preview-04-2026`): Untuk kueri umum yang memerlukan analisis sedang, agen mungkin menggunakan ~80 kueri penelusuran, ~250 ribu token input (~50-70% di-cache), dan ~60 ribu token output.
  - **Estimasi total:** ~$1.00 – $3.00 per tugas
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Untuk analisis lanskap kompetitif yang mendalam atau uji tuntas yang ekstensif, agen dapat menggunakan hingga ~160 kueri penelusuran, ~900 ribu token input (~50-70% di-cache), dan ~80 ribu token output.
  - **Estimasi total:** ~$3.00 – $7.00 per tugas

## Pertimbangan keamanan

Memberi agen akses ke web dan file pribadi Anda memerlukan pertimbangan yang cermat terhadap risiko keamanan.

- **Injeksi perintah menggunakan file:** Agen membaca isi file yang Anda berikan. Pastikan dokumen yang diupload (PDF, file teks) berasal dari sumber tepercaya. File berbahaya dapat berisi teks tersembunyi yang dirancang untuk memanipulasi output agen.
- **Risiko konten web:** Agen menelusuri web publik. Meskipun kami menerapkan filter keamanan yang andal, ada risiko bahwa agen dapat menemukan dan memproses halaman web berbahaya. Sebaiknya tinjau `citations` yang diberikan
  dalam respons untuk memverifikasi sumber.
- **Pencurian data:** Berhati-hatilah saat meminta agen untuk meringkas data internal sensitif jika Anda juga mengizinkannya menjelajahi web.

## Praktik terbaik

- **Perintah untuk nilai yang tidak diketahui:** Beri tahu agen cara menangani data yang tidak ada.
  Misalnya, tambahkan *"Jika angka spesifik untuk tahun 2025 tidak tersedia, nyatakan secara eksplisit bahwa angka tersebut adalah proyeksi atau tidak tersedia, bukan perkiraan"* ke perintah Anda.
- **Berikan konteks:** Mendasari riset agen dengan memberikan informasi atau batasan latar belakang langsung dalam perintah input.
- **Gunakan perencanaan kolaboratif:** Untuk kueri kompleks, aktifkan perencanaan kolaboratif untuk meninjau dan menyempurnakan rencana riset sebelum eksekusi.
- **Input multimodal:** Agen Deep Research mendukung input multimodal.
  Gunakan dengan hati-hati, karena hal ini akan meningkatkan biaya dan risiko meluapnya jendela konteks.

## Batasan

- **Alat kustom:** Saat ini Anda tidak dapat menyediakan alat Pemanggilan Fungsi kustom, tetapi Anda dapat menggunakan server MCP (Model Context Protocol) jarak jauh dengan agen Deep Research.
- **Output terstruktur:** Agen Deep Research saat ini tidak mendukung output terstruktur.
- **Waktu riset maksimum:** Agen Deep Research memiliki waktu riset maksimum 60 menit. Sebagian besar tugas akan selesai dalam waktu 20 menit.
- **Persyaratan penyimpanan:** Eksekusi agen menggunakan `background=True` memerlukan
  `store=True`.
- **Penelusuran Google:** [Google
  Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) diaktifkan secara
  default dan [pembatasan
  tertentu](https://ai.google.dev/gemini-api/terms?hl=id#use-restrictions2)
  berlaku untuk hasil yang di-grounding.

## Langkah berikutnya

- Pelajari lebih lanjut [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id).
- Pelajari cara menggunakan data Anda sendiri menggunakan alat [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-26 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-26 UTC."],[],[]]
