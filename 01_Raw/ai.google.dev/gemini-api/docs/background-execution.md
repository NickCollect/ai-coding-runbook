---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=id
fetched_at: 2026-06-29T05:33:22.140695+00:00
title: "Eksekusi latar belakang \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Eksekusi latar belakang

Untuk tugas yang berjalan lama seperti riset mendalam, penalaran kompleks, atau eksekusi agen multi-langkah, waktu tunggu koneksi dapat mengganggu permintaan HTTP standar (yang biasanya ditutup setelah 60 detik). [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) menyediakan **eksekusi latar belakang** untuk menjalankan tugas ini secara asinkron.

Agar interaksi berjalan hingga menyelesaikan tugas di server, tetapkan `"background": true` saat membuat interaksi. API akan segera menampilkan ID interaksi, yang dapat digunakan aplikasi klien untuk melakukan polling status, memproses streaming, atau menghubungkan kembali ke streaming yang terputus.

Eksekusi di latar belakang didukung untuk model Gemini standar (seperti `gemini-3.5-flash` dan `gemini-3.1-pro-preview`) dan Agen Terkelola (seperti `antigravity-preview-05-2026`).

## Membuat interaksi latar belakang

Untuk memulai interaksi latar belakang, tetapkan parameter `background` ke `true` saat membuat resource.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Cara kerja eksekusi latar belakang

Saat Anda membuat interaksi latar belakang, tugas akan berjalan secara asinkron di server. Interaksi bertransisi melalui berbagai status eksekusi:

- `in_progress`: Server sedang aktif menjalankan interaksi (seperti menjalankan kode atau melakukan riset).
- `requires_action`: Interaksi telah dijeda dan menunggu input klien (seperti mengonfirmasi eksekusi alat atau menjawab pertanyaan).
- `completed`: Interaksi berhasil diselesaikan dan output tersedia.
- `failed`: Terjadi error selama eksekusi (seperti kegagalan alat atau batas kecepatan).
- `cancelled`: Permintaan klien menghentikan eksekusi.

### Kasus penggunaan

Gunakan eksekusi latar belakang untuk:

- **Eksekusi agen:** Tugas yang memerlukan eksekusi kode, penjelajahan web, atau orkestrasi sub-agen (seperti `antigravity-preview-05-2026`).
- **Deep Research:** Berjalan menggunakan `deep-research-preview-04-2026` atau `deep-research-max-preview-04-2026` yang memerlukan waktu beberapa menit.
- **Penalaran panjang:** Tugas yang langkah-langkah pemikiran modelnya melampaui batas koneksi HTTP standar.

## Mengambil hasil

Dapatkan hasil interaksi latar belakang menggunakan **polling** atau **streaming**.

### Pola polling (tidak memblokir)

Polling memeriksa status interaksi secara berkala menggunakan permintaan GET non-blocking hingga mencapai status terminal.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

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

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Pola streaming

Jika gangguan jaringan menghentikan streaming, streaming dapat dilanjutkan dari peristiwa terakhir yang diterima. Setiap delta berisi `event_id` unik dalam payload-nya. Meneruskan ID ini sebagai `last_event_id` akan melanjutkan streaming dari peristiwa tersebut.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Percakapan multi-giliran

Interaksi berikutnya dapat dirangkai ke percakapan latar belakang menggunakan `previous_interaction_id`, dengan tunduk pada batasan berikut:

1. **Eksekusi aktif diblokir:** Merangkai interaksi berikutnya dengan interaksi yang berstatus `in_progress` akan menampilkan error `400 Bad Request`. Tunggu hingga interaksi mencapai status `completed` sebelum memulai interaksi berikutnya.
2. **Parameter Lingkungan untuk Agen Terkelola:** Saat merangkai interaksi untuk Agen Terkelola (seperti `antigravity-preview-05-2026`), permintaan harus menyertakan `previous_interaction_id` dan `environment`.

Contoh berikut menunjukkan cara merangkai interaksi:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Pembatalan dan penghapusan

Mengontrol eksekusi yang sedang berjalan dan mengelola penyimpanan menggunakan permintaan pembatalan dan penghapusan:

- **Batalkan (`POST /interactions/{id}/cancel`):** Menghentikan tugas yang sedang berjalan. Status akan berubah menjadi `cancelled`. Tindakan pembersihan di server dapat menyebabkan sedikit penundaan sebelum status diperbarui dalam permintaan GET.
- **Hapus (`DELETE /interactions/{id}`):** Menghapus catatan interaksi dari server. Permintaan GET berikutnya akan menampilkan error `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Langkah berikutnya

- Baca [Ringkasan Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) untuk memahami pengelolaan sesi dan status.
- Lihat panduan [Interaksi streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=id) untuk mengetahui detail tentang update peristiwa real-time.
- Pelajari [Panduan memulai agen terkelola](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id) untuk membangun agen multi-turn stateful.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-26 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-26 UTC."],[],[]]
