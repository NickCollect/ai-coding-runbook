---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=id
fetched_at: 2026-05-11T04:57:43.043679+00:00
title: "Interactions API: Panduan migrasi perubahan yang dapat menyebabkan gangguan (Mei 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Interactions API: Panduan migrasi perubahan yang dapat menyebabkan gangguan (Mei 2026)

Interactions API `v1beta` memperkenalkan perubahan yang dapat menyebabkan gangguan yang menata ulang bentuk API untuk mendukung kemampuan mendatang seperti pengarahan di tengah penerbangan dan panggilan alat asinkron. Halaman ini menjelaskan apa yang berubah dan memberikan contoh kode sebelum dan sesudah untuk membantu Anda melakukan migrasi. Ada dua kategori perubahan:

1. [**Skema langkah**](#steps-schema): Array `steps` baru menggantikan array
   `outputs`, yang menyediakan linimasa terstruktur dari setiap giliran interaksi.
2. [**Konfigurasi format output**](#output-format-config): `response\_format` polimorfik baru mengonsolidasikan semua kontrol format output dan menghapus `response\_mime\_type`.`response_format``response_mime_type`

Ikuti langkah-langkah di [Cara melakukan migrasi ke skema baru](#how-to-migrate) untuk
memperbarui integrasi Anda.

## Perubahan inti: `outputs` menjadi `steps`

Skema baru menggantikan array `outputs` dengan array `steps`.

- **Lama**: Respons menampilkan array `outputs` datar yang hanya berisi konten yang dibuat model.
- **Skema baru**: Respons menampilkan array `steps` yang berisi langkah-langkah terstruktur dengan diskriminator jenis.

`POST /interactions` hanya menampilkan langkah-langkah output. `GET /interactions/{id}`
menampilkan linimasa langkah lengkap, termasuk langkah `user_input` awal.

### Input/output dasar (unary)

#### Sebelum (lama)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Setelah (skema baru)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.steps[-1].content[0].text)  # CHANGED: steps instead of outputs
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### Panggilan fungsi

Struktur permintaan tetap tidak berubah, tetapi respons menggantikan konten `outputs` datar dengan langkah-langkah terstruktur.

#### Sebelum (lama)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Setelah (skema baru)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Alat sisi server

Alat sisi server (seperti Google Penelusuran atau Eksekusi Kode) kini menghasilkan jenis langkah tertentu dalam array `steps`. Meskipun skema lama menampilkan operasi ini sebagai jenis konten tertentu dalam array `outputs`, skema baru memindahkannya ke array `steps`. Contoh berikut menggunakan Google Penelusuran.

#### Sebelum (lama)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Setelah (skema baru)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Streaming

Streaming menampilkan jenis peristiwa baru:

#### Jenis peristiwa baru

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `interaction.error`
- `step.start`
- `step.delta`
- `step.stop`

#### Jenis peristiwa yang tidak digunakan lagi

Jenis peristiwa lama berikut digantikan oleh peristiwa baru yang tercantum di atas:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `error` → `interaction.error`
- `interaction.status_update` → digantikan oleh `interaction.in_progress`, `interaction.requires_action`, dll.

**Panggilan fungsi streaming**: Saat Anda menggunakan streaming dengan panggilan fungsi,
peristiwa `step.start` akan menampilkan nama fungsi, dan peristiwa `step.delta` akan
melakukan streaming argumen sebagai string JSON parsial (menggunakan `arguments_delta`). Anda
harus mengumpulkan delta ini untuk mendapatkan argumen lengkap. Hal ini berbeda dengan panggilan unary yang memungkinkan Anda menerima objek panggilan fungsi lengkap sekaligus.

#### Contoh

##### Sebelum (Lama)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Setelah (Skema Baru)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3-flash-preview",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3-flash-preview"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Histori Percakapan Tanpa Status

Jika Anda mengelola histori percakapan secara manual di sisi klien (kasus penggunaan tanpa status), Anda harus memperbarui cara Anda menggabungkan giliran sebelumnya.

- **Lama**: Developer sering mengumpulkan array `outputs` dari respons dan mengirimkannya kembali di kolom `input` pada giliran berikutnya.
- **Skema baru**: Sekarang Anda harus mengumpulkan array `steps` dari respons dan meneruskannya di kolom `input` permintaan berikutnya, dengan menambahkan giliran pengguna baru Anda sebagai langkah `user_input`.

## Konfigurasi format output: Perubahan `response_format`

API yang diperbarui mengonsolidasikan semua kontrol format output ke dalam kolom `response_format` polimorfik terpadu. Hal ini memusatkan konfigurasi output di tingkat atas dan membuat `generation_config` berfokus pada perilaku model (seperti temperatur, top\_p, dan pemikiran).

### Perubahan penting

- **API menghapus `response_mime_type`.** Sekarang Anda menentukan jenis MIME per entri format di dalam `response_format`.
- **`response_format` kini merupakan objek (atau array) polimorfik.** Setiap entri memiliki diskriminator `type` (`text`, `audio`, `image`) dan kolom khusus jenis. Untuk meminta beberapa modalitas output, teruskan array entri format.
- **`image_config` dipindahkan dari `generation_config` ke `response_format`.**
  Sekarang Anda menentukan setelan output gambar seperti `aspect_ratio` dan `image_size`
  dalam entri `response_format` dengan `"type": "image"`.

### Output terstruktur (JSON)

Skema baru menghapus kolom `response_mime_type`. Sebagai gantinya, tentukan
jenis MIME dan skema JSON di dalam objek `response_format` dengan
`"type": "text"`.

#### Sebelum (lama)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize this article.',
    responseMimeType: 'application/json',
    responseFormat: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Setelah (skema baru)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize this article.',
    // responseMimeType is removed — specify mimeType inside responseFormat
    responseFormat: {
        type: 'text',
        mimeType: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Konfigurasi gambar

Skema baru menghapus `image_config` dari `generation_config`. Sekarang Anda menentukan
setelan output gambar dalam entri `response_format` dengan `"type": "image"`.

#### Sebelum (lama)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Generate an image of a sunset over the ocean.',
    generationConfig: {
        imageConfig: {
            aspectRatio: '1:1',
            imageSize: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Setelah (skema baru)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "delivery": "inline",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Generate an image of a sunset over the ocean.',
    // imageConfig is removed from generationConfig — use responseFormat
    responseFormat: {
        type: 'image',
        mimeType: 'image/jpeg',
        delivery: 'inline',
        aspectRatio: '1:1',
        imageSize: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "delivery": "inline",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

Untuk meminta beberapa modalitas output (misalnya, teks dan audio bersama-sama), teruskan array entri format ke `response_format`, bukan satu objek.

## Cara melakukan migrasi ke skema baru

### Pengguna SDK

Upgrade ke versi SDK terbaru (Python ≥2.0.0, JavaScript ≥2.0.0). SDK secara otomatis mengikutsertakan Anda ke dalam skema baru — tidak ada perubahan kode yang diperlukan selain memperbarui cara Anda membaca respons (lihat contoh di atas). Perhatikan bahwa hanya skema baru yang didukung dalam versi SDK ini. Versi SDK lama (Python 1.x.x, JavaScript 1.x.x) akan terus berfungsi hingga skema lama dihapus pada **8 Juni 2026**.

### Pengguna REST API

Tambahkan header `Api-Revision: 2026-05-20` ke permintaan Anda untuk ikut serta ke dalam skema baru sekarang. Setelah **26 Mei**, skema baru akan menjadi default untuk semua
permintaan. Anda dapat memilih tidak ikut serta untuk sementara dengan `Api-Revision: 2026-05-07`
hingga **8 Juni**, saat API menghapus skema lama secara permanen.

### Linimasa

| Tanggal | Fase | Pengguna SDK | Pengguna REST API |
| --- | --- | --- | --- |
| **7 Mei** | Ikut serta | Versi SDK baru tersedia (Python ≥2.0.0, JS ≥2.0.0). Upgrade untuk mendapatkan skema baru secara otomatis. | Tambahkan header `Api-Revision: 2026-05-20` untuk ikut serta. Default tetap lama. |
| **26 Mei** | Perubahan default | Tidak ada tindakan yang diperlukan jika sudah diupgrade. SDK lama (Python 1.x.x, JS 1.x.x) masih berfungsi, tetapi menampilkan respons lama. | Skema baru kini menjadi default. Kirim header `Api-Revision: 2026-05-07` untuk memilih tidak ikut serta. |
| **8 Juni** | Senja | Versi SDK Python 1.x.x dan JS 1.x.x akan rusak untuk panggilan Interactions API. | Skema lama dihapus untuk Interactions API. Header `Api-Revision` diabaikan. |

## Checklist Migrasi

### Skema langkah (`steps`)

- Perbarui kode untuk membaca konten respons dari array `steps`, bukan `outputs`. [Lihat contoh](#basic-unary).
- Pastikan kode Anda menangani jenis langkah `user_input` dan `model_output`. [Lihat contoh](#basic-unary).
- (Panggilan Fungsi) Perbarui kode untuk menemukan langkah `function_call` dalam array `steps`. [Lihat contoh](#function-calling).
- (Alat Sisi Server) Perbarui kode untuk menangani langkah-langkah khusus alat (misalnya, `google_search_call`, `google_search_result`). [Lihat contoh](#server-side-tools).
- (Histori Tanpa Status) Perbarui pengelolaan histori untuk meneruskan array `steps` di kolom `input` permintaan berikutnya. [Lihat detail](#stateless-history).
- (Hanya Streaming) Perbarui klien untuk memproses jenis peristiwa SSE baru (`interaction.created`, `step.delta`, dll.). [Lihat contoh](#streaming).

### Konfigurasi format output (`response_format`)

- Ganti `response_mime_type` dengan kolom `mime_type` di dalam `response_format`. [Lihat contoh](#structured-output).
- Gabungkan skema JSON `response_format` yang ada di dalam objek `{"type": "text", "schema": ...}`. [Lihat contoh](#structured-output).
- (Pembuatan Gambar) Pindahkan `image_config` dari `generation_config` ke entri `{"type": "image", ...}` di `response_format`. [Lihat contoh](#image-config).
- (Multimodal) Konversi `response_format` dari satu objek ke array saat meminta beberapa modalitas output.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-08 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-08 UTC."],[],[]]
