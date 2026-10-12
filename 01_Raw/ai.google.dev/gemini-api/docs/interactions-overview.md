---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id
fetched_at: 2026-10-12T06:52:33.281875+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Interactions API

Interactions API adalah cara terbaik untuk membangun dengan model dan agen Gemini. Mulai Juni 2026, fitur ini Tersedia Secara Umum dan direkomendasikan untuk semua project baru. Meskipun kini dianggap sebagai API lama, API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=id) asli
tetap didukung sepenuhnya.

## Mengapa menggunakan Interactions API?

- **Antarmuka universal untuk semua aplikasi**: Dirancang sebagai antarmuka standar untuk setiap kasus penggunaan, termasuk pembuatan teks satu giliran, pemahaman multimodal, output terstruktur, orkestrasi alat, dan Agentic Workflows.
- **Satu API untuk model dan agen**: Satu endpoint dan pola terpadu untuk memanggil model Gemini standar serta agen khusus secara langsung (seperti Deep Research dan agen yang dikelola kustom).
- **Kemampuan baru siap pakai**: Fitur seperti status percakapan sisi server opsional menggunakan `previous_interaction_id`, langkah-langkah eksekusi yang dapat diamati untuk proses debug dan rendering UI, serta [eksekusi di latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) untuk tugas yang berjalan lama menggunakan `background=true`.
- **Biaya lebih rendah dengan rasio hit cache yang lebih tinggi**: Saat menggunakan percakapan multi-giliran, pengelolaan status sisi server opsional memungkinkan penyiapan cache konteks yang lebih efisien di seluruh giliran, sehingga mengurangi biaya token.
- **Tempat peluncuran fitur baru**: Ke depannya, semua model baru, kemampuan multimodal, alat, dan fitur berbasis agen akan diluncurkan di Interactions API.

Secara default, Interactions API menyimpan permintaan sehingga Anda dapat memanfaatkan fitur pengelolaan status sisi server menggunakan `previous_interaction_id`. Anda dapat memilih untuk menggunakan perilaku tanpa status dengan menyetel
`store=false`. Lihat bagian [retensi data](#data-storage-retention) untuk mengetahui detailnya.

## Mulai

- **Siapkan agen coding Anda**: Hubungkan ke **MCP Dokumen Gemini** dan instal
  keterampilan `gemini-api-dev` untuk memberi asisten Anda akses langsung ke
  dokumentasi developer dan praktik terbaik terbaru. Untuk mengetahui langkah-langkah mendetail, lihat
  [panduan Menyiapkan agen coding Anda](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)
- **Bermigrasi dari `generateContent`**: Jika Anda memiliki integrasi yang sudah ada, ikuti [Panduan migrasi](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=id) untuk beralih ke Interactions API.
- **Mulai**: Ikuti langkah-langkah dalam panduan [Mulai menggunakan Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=id).

### Panduan fitur

Jelajahi kemampuan spesifik Interactions API melalui panduan ini. Anda dapat menggunakan tombol di halaman ini untuk beralih antara generateContent dan Interactions API:

- [Pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id)
- [Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)
- [Pemahaman gambar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=id)
- [Pemahaman audio](https://ai.google.dev/gemini-api/docs/audio?hl=id)
- [Pemahaman video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id)
- [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id)
- [Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
- [Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)
- [Agen Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id)
- [Inferensi Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)
- [Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)

## Cara kerja Interactions API

Interactions API berpusat pada resource inti: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=id#Resource:Interaction). `Interaction` mewakili giliran yang lengkap dalam percakapan atau tugas. Objek ini berfungsi sebagai catatan sesi, yang berisi seluruh histori interaksi sebagai urutan **langkah eksekusi** secara kronologis. Langkah-langkah ini mencakup pemikiran model, panggilan dan hasil alat sisi server atau sisi klien (seperti `function_call` dan `function_result`), serta `model_output` akhir. Resource yang disimpan (diambil melalui `interactions.get`) juga mencakup langkah-langkah `user_input` untuk konteks lengkap, meskipun respons `interactions.create` hanya menampilkan langkah-langkah yang dihasilkan model.

Saat melakukan panggilan ke
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=id#CreateInteraction), Anda
membuat resource `Interaction` baru:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Pengelolaan status sisi server

Anda dapat menggunakan `id` interaksi yang telah selesai dalam panggilan berikutnya menggunakan parameter `previous_interaction_id` untuk melanjutkan percakapan. Server menggunakan ID ini untuk mengambil histori percakapan, sehingga Anda tidak perlu mengirim ulang seluruh histori chat:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

Parameter `previous_interaction_id` hanya mempertahankan histori percakapan (input dan output) menggunakan `previous_interaction_id`. Parameter lainnya adalah **cakupan interaksi**
dan hanya berlaku untuk interaksi tertentu yang saat ini Anda buat:

- `tools`
- `system_instruction`
- `generation_config` (termasuk `thinking_level`, `temperature`, dll.)

Artinya, Anda harus menentukan ulang parameter ini di setiap interaksi baru jika ingin menerapkannya. Pengelolaan status sisi server ini bersifat opsional; Anda juga dapat
beroperasi dalam mode stateless dengan mengirimkan histori percakapan lengkap di setiap
permintaan.

### Penyimpanan dan retensi data

Secara default, API menyimpan semua objek Interaksi (`store=true`) untuk
menyederhanakan penggunaan fitur pengelolaan status sisi server (dengan
`previous_interaction_id`), [eksekusi latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) (menggunakan `background=true`), dan
tujuan observasi.

- **Paket berbayar**: Sistem menyimpan interaksi selama **55 hari**.
- **Paket gratis**: Sistem menyimpan interaksi selama **1 hari**.

Jika tidak menginginkannya, Anda dapat
menetapkan `store=false` dalam permintaan Anda. Kontrol ini terpisah dari pengelolaan status
; Anda dapat menonaktifkan penyimpanan untuk interaksi apa pun. Namun, perhatikan bahwa
`store=false` tidak kompatibel dengan [eksekusi di latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id) dan mencegah penggunaan
`previous_interaction_id` untuk giliran berikutnya.

Untuk project Tingkat Berbayar, Anda dapat mengonfigurasi periode retensi di
[AI Studio](https://aistudio.google.com/logs?hl=id) untuk otomatis menandai log agar
dihapus dari penyimpanan project setelah 7, 14, 28, atau 55 hari. Periode retensi yang lebih singkat dapat memengaruhi pengambilan percakapan sebelumnya.

Anda dapat menghapus interaksi tersimpan kapan saja menggunakan metode
[`delete`](https://ai.google.dev/api/interactions-api?hl=id#deleteInteraction) secara terprogram,
yang memerlukan ID interaksi. Anda juga dapat melihat dan mengelola log interaksi tersimpan, termasuk penghapusan dari penyimpanan project, di [AI Studio](https://aistudio.google.com/logs?hl=id).

Setelah periode retensi berakhir, data Anda akan dihapus secara otomatis.

Objek interaksi diproses sesuai dengan [persyaratan](https://ai.google.dev/gemini-api/terms?hl=id).

### Melihat interaksi di AI Studio

API menyimpan permintaan Interactions API yang dieksekusi dengan `store=true` untuk
project di Tingkat Berbayar. Anda dapat melihatnya langsung dari
[halaman Log di Google AI Studio](https://aistudio.google.com/logs?hl=id). Lihat
[Panduan log](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id) untuk mengetahui informasi selengkapnya.

## Praktik terbaik

- **Rasio hit cache**: Peng-cache-an implisit didukung dalam mode stateful dan stateless (lihat [Panduan memulai](https://ai.google.dev/gemini-api/docs/get-started?hl=id#4_multi-turn_conversations)). Penggunaan
  `previous_interaction_id` (berstatus) untuk melanjutkan percakapan memungkinkan
  sistem lebih mudah memanfaatkan caching implisit untuk histori
  percakapan, yang meningkatkan performa dan mengurangi biaya.
- **Mencampur interaksi**: Anda memiliki fleksibilitas untuk mencampur dan mencocokkan interaksi Agen dan Model dalam percakapan. Misalnya, Anda dapat menggunakan agen khusus, seperti agen Deep Research, untuk pengumpulan data awal, lalu menggunakan model Gemini standar untuk tugas lanjutan seperti meringkas atau memformat ulang, dengan menautkan langkah-langkah ini dengan `previous_interaction_id`.

## Model & agen yang didukung

| Nama Model | Jenis | ID Model |
| --- | --- | --- |
| Gemini 3.8 Flash | Model | `gemini-3.8-flash` |
| Gemini 3.6 Flash | Model | `gemini-3.6-flash` |
| Pratinjau Gemini 3.1 Pro | Model | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Model | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Pratinjau Gemini 3 Flash | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Model | `gemini-3-pro-image` |
| Gambar Gemini 3.1 Flash | Model | `gemini-3.1-flash-image` |
| Pratinjau Gemini 3.1 Flash TTS | Model | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Model | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Model | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Model | `lyria-3.5` |
| Pratinjau Klip Lyria 3 | Model | `lyria-3-clip-preview` |
| Pratinjau Lyria 3 Pro | Model | `lyria-3-pro-preview` |
| Pratinjau Deep Research | Agen | `deep-research-preview-04-2026` |
| Pratinjau Deep Research | Agen | `deep-research-max-preview-04-2026` |
| Pratinjau Antigravity | Agen | `antigravity-preview-09-2026` |

## SDK

Anda dapat menggunakan Google GenAI SDK versi terbaru untuk mengakses
Interactions API.

- Di Python, ini adalah paket `google-genai` dari versi `2.3.0` dan seterusnya.
- Di JavaScript, ini adalah paket `@google/genai` dari versi `2.3.0` dan yang lebih baru.
- Di Go, ini adalah paket `google.golang.org/genai`.
- Di Java, ini adalah paket `com.google.genai:google-genai`.

Anda dapat mempelajari lebih lanjut cara menginstal SDK di halaman
[Libraries](https://ai.google.dev/gemini-api/docs/libraries?hl=id).

## Batasan

- **MCP Jarak Jauh**: Gemini 3 tidak mendukung MCP jarak jauh, fitur ini akan segera hadir.
- **Kompatibilitas model multi-giliran**: Saat menggabungkan model yang berbeda dalam percakapan (baik yang memiliki status maupun tidak), model berikutnya harus mendukung modalitas output model sebelumnya sebagai input. Misalnya, jika Anda membuat gambar menggunakan `gemini-3.1-flash-image`, Anda tidak dapat melanjutkan percakapan tersebut dengan model yang tidak menerima input gambar (seperti model khusus teks atau model pembuatan musik seperti Lyria).

Fitur berikut didukung oleh API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=id), tetapi **belum
tersedia** di Interactions API:

- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**
- **[Pemanggilan fungsi otomatis (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=id#automatic_function_calling_python_only)**
- **[Penyimpanan dalam cache eksplisit](https://ai.google.dev/gemini-api/docs/caching?hl=id)**: Perhatikan bahwa penyimpanan dalam cache implisit sisi server tersedia di Interactions API
  melalui `previous_interaction_id`.
- **[Setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id)**: Setelan keamanan kustom tidak didukung di Interactions API.

## Masukan

Masukan Anda sangat penting untuk pengembangan Interactions API.
Sampaikan pendapat Anda, laporkan bug, atau minta fitur di
[Forum Komunitas Developer AI Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=id) kami.

## Langkah berikutnya

- Coba [notebook panduan memulai Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=id).
- Pelajari lebih lanjut [agen Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
