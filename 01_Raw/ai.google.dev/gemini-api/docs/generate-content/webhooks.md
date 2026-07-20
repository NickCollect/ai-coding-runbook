---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/webhooks?hl=id
fetched_at: 2026-07-20T04:46:09.878161+00:00
title: "Webhook \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Webhook

Webhook memungkinkan Gemini API mengirimkan notifikasi real-time ke server Anda
saat Operasi Asinkron atau Operasi yang Berjalan Lama (LRO) selesai. Hal ini menggantikan
kebutuhan untuk melakukan polling API untuk mendapatkan update status, sehingga mengurangi latensi dan overhead.

Webhook tersedia untuk operasi seperti tugas [Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=id),
[Interaksi](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id), dan [pembuatan video](https://ai.google.dev/gemini-api/docs/video?hl=id).

## Cara kerjanya

Daripada melakukan polling `GET /operations` berulang kali untuk memeriksa apakah tugas telah selesai, Anda dapat mengonfigurasi Webhook Gemini API untuk mengirim permintaan HTTP POST ke URL
pendengar Anda segera setelah pemicu peristiwa.

Gemini API mendukung dua cara untuk mengonfigurasi webhook:

- [**Webhook statis**](#static-webhooks): Endpoint tingkat project yang dikonfigurasi dengan [WebhookService API](https://ai.google.dev/api?hl=id) Gemini. Cocok untuk integrasi global (misalnya, memberi tahu Slack, menyinkronkan database, dll.).
- [**Webhook dinamis**](#dynamic-webhooks): Penggantian tingkat permintaan yang meneruskan
  URL webhook dalam payload konfigurasi panggilan tugas tertentu. Ideal untuk
  merutekan tugas tertentu ke endpoint khusus.

## Webhook statis

Webhook statis didaftarkan untuk seluruh [project](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) dan dipicu untuk setiap peristiwa yang cocok.

### Membuat webhook

Anda dapat membuat endpoint menggunakan SDK atau REST API.

**PENTING**: Saat membuat webhook, API akan menampilkan **secret penandatanganan**
**hanya sekali**. Anda harus menyimpannya dengan aman (misalnya, di variabel lingkungan Anda)
untuk memverifikasi tanda tangan nanti. Jika Anda kehilangan rahasia penandatanganan, Anda harus
[merotasinya](#rotate-signing-secret).

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

# Store webhook.new_signing_secret securely
webhook_secret = webhook.new_signing_secret
print(f"Created webhook: {webhook.name}, {webhook.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  // Store webhook.signingSecret securely
  const webhookSecret = webhook.new_signing_secret;
  console.log(`Created webhook: ${webhook.name}, ${webhook.id}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "name": "MyBatchWebhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

Untuk mengetahui detail tentang cara menyiapkan server Anda untuk menerima data, lihat bagian [Menangani permintaan webhook](#handle-webhook-requests).

### Mendapatkan webhook

Mengambil detail tentang webhook tertentu berdasarkan nama resource-nya.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.get(id="<your_webhook_id>")

print(f"Webhook: {webhook.name}")
print(f"URI: {webhook.uri}")
print(f"Events: {webhook.subscribed_events}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI(); // Assumes process.env.GEMINI_API_KEY is set

async function getWebhook() {
  const webhook = await client.webhooks.get("<your_webhook_id>");

  console.log(`Webhook: ${webhook.name}`);
  console.log(`URI: ${webhook.uri}`);
  console.log(`Events: ${webhook.subscribed_events}`);
}

getWebhook();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Mencantumkan webhook

Mencantumkan semua webhook yang dikonfigurasi untuk project saat ini, dengan penomoran halaman opsional.

### Python

```
from google import genai

client = genai.Client()

webhooks = client.webhooks.list()

for wh in webhooks:
    print(f"{wh.id}: {wh.name} -> {wh.uri}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function listWebhooks() {
  const webhooks = await client.webhooks.list();

  for (const wh of webhooks) {
    console.log(`${wh.id}: ${wh.name} -> ${wh.uri}`);
  }
}

listWebhooks();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Memperbarui webhook

Memperbarui properti webhook yang ada seperti nama tampilan, target URI, atau
peristiwa yang disubscribe.

### Python

```
from google import genai

client = genai.Client()

updated_webhook = client.webhooks.update(
    id="<your_webhook_id>",
    subscribed_events=["batch.succeeded", "batch.failed", "batch.cancelled"],
)

print(f"Updated webhook: {updated_webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function updateWebhook() {
  const updatedWebhook = await client.webhooks.update(
    "<your_webhook_id>",
    {
      subscribed_events: ["batch.succeeded", "batch.failed", "batch.cancelled"],
    }
  );

  console.log(`Updated webhook: ${updatedWebhook.name}`);
}

updateWebhook();
```

### REST

```
curl -X PATCH \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "subscribed_events": ["batch.succeeded", "batch.failed", "batch.cancelled"]
  }'
```

### Menghapus webhook

Menghapus endpoint webhook dari project. Tindakan ini akan menghentikan pengiriman acara mendatang ke endpoint tersebut.

### Python

```
from google import genai

client = genai.Client()

client.webhooks.delete(id="<your_webhook_id>")

print("Webhook deleted.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function deleteWebhook() {
  await client.webhooks.delete("<your_webhook_id>");

  console.log("Webhook deleted.");
}

deleteWebhook();
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Merotasi secret penandatanganan

Merotasi rahasia penandatanganan untuk webhook. Anda dapat mengonfigurasi apakah secret yang sebelumnya aktif dicabut segera atau setelah masa tenggang 24 jam.

**PENTING**: Secret penandatanganan baru hanya ditampilkan **sekali** pada waktu rotasi. Simpan dengan aman sebelum memperbarui logika verifikasi Anda.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.webhooks.rotate_signing_secret(
    id="<your_webhook_id>",
    revocation_behavior="REVOKE_PREVIOUS_SECRETS_AFTER_H24",
)

# Store response.secret securely, then update your server's verification config
print("New signing secret generated. Update your server configuration.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function rotateSigningSecret() {
  const response = await client.webhooks.rotateSigningSecret(
    "<your_webhook_id>",
    {
      revocation_behavior: "REVOKE_PREVIOUS_SECRETS_AFTER_H24",
    }
  );

  // Store response.secret securely, then update your server's verification config
  console.log("New signing secret generated. Update your server configuration.");
}

rotateSigningSecret();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>/rotate_secret" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "revocation_behavior": "REVOKE_PREVIOUS_SECRETS_AFTER_H24"
  }'
```

### Menangani permintaan webhook di server

Saat peristiwa yang Anda ikuti terjadi, URL webhook Anda akan menerima
permintaan POST HTTP. Endpoint Anda harus merespons dengan kode status 2xx dalam beberapa detik untuk menghindari percobaan ulang. Untuk memastikan pengiriman, Gemini API
akan otomatis mencoba ulang permintaan yang gagal selama 24 jam menggunakan backoff eksponensial.

Gemini secara ketat mengikuti spesifikasi [Webhook Standar](https://github.com/standard-webhooks/standard-webhooks) untuk
header keamanan. Verifikasi payload di server Anda menggunakan tanda tangan header yang ditandatangani dan rahasia penandatanganan statis yang disimpan. Lihat bagian [Webhook envelope](#webhook-envelope) untuk mengetahui informasi payload.

Berikut adalah contoh penggunaan Flask untuk pemroses HTTP:

### Python

```
# pip install flask standardwebhooks
import os
from flask import Flask, request, jsonify
# Standard verification wrapper for Standard Webhook Headers
from standardwebhooks.webhooks import Webhook, WebhookVerificationError

app = Flask(__name__)

SIGNING_SECRET = os.environ.get('WEBHOOK_SIGNING_SECRET')

@app.route('/gemini-callback', methods=['POST'])
def gemini_callback():
    payload = request.get_data(as_text=True)
    headers = request.headers

    try:
        wh = Webhook(SIGNING_SECRET)
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return jsonify({"error": "Signature invalid"}), 400

    # Process thin payload contents
    if event.get("type") == "batch.succeeded":
        print(f"Batch completed! ID: {event["data"]["id"]}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event["data"]["output_file_uri"]}")
    elif (event.type == "video.generated"):
        print(f"Video generated! URI: {event["data"]["output_file_uri"]}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=8000)
```

### JavaScript

```
// npm install standardwebhooks
import { Webhook } from "standardwebhooks";
import express from "express";

const app = express();
const client = new GoogleGenAI({ webhookSecret: process.env.WEBHOOK_SIGNING_SECRET });

// Don't use express.json() because signature verification needs the raw text body
app.use(express.text({ type: "application/json" }));

app.post("/gemini-callback", async (req, res) => {
  const payload = await req.text();
        const headers: Record<string, string> = {};
        req.headers.forEach((value, key) => {
            headers[key] = value;
        });

        try {
            const wh = new Webhook(process.env.WEBHOOK_SIGNING_SECRET);
            const event = wh.verify(payload, headers) as Record<string, any>;
    console.log(`Event type: ${event.type}, data: ${JSON.stringify(event.data)}`);

            // Process thin payload contents
            if (event.type === "batch.succeeded") {
                console.log(`Batch completed! ID: ${event.data.id}`);
                if (event.data.output_file_uri) {
                    // For batch jobs with input file
                    console.log(`Batch file: ${event.data.output_file_uri}`);
                }
            } else if (event.type === "video.generated") {
                console.log(`Video generated! URI: ${event.data.output_file_uri}`);
            }

            res.status(200).json({ status: "received" });
        } catch (e) {
            console.error("Webhook verification failed:", e);
            res.status(400).send("Invalid signature");
        }
});

app.listen(8000, () => {
  console.log("Webhook server is running on port 8000");
});
```

## Webhook dinamis

Webhook dinamis memungkinkan Anda mengikat endpoint webhook ke **konfigurasi
permintaan tertentu**, yang ideal untuk antrean orkestrasi agen. Webhook dinamis memanfaatkan tanda tangan JWKS kunci publik asimetris, bukan secret simetris.

### Mengirim permintaan dinamis

Tambahkan `webhook_config` saat memicu tugas asinkron (misalnya, membuat Batch).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src="files/uploaded_file_id",
    config={
        "display_name": "My Setup",
        "webhook_config": {
            "uris": ["https://my-api.com/gemini-webhook-dynamic"],
            "user_metadata":{"job_group": "nightly-eval", "priority": "high"}
        }
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createBatchWithWebhook() {
  const fileBatchJob = await client.batches.create({
    model: "gemini-3.5-flash",
    src: "files/uploaded_file_id",
    config: {
      displayName: "My Setup",
      webhookConfig: {
        uris: ["https://my-api.com/gemini-webhook-dynamic"],
        user_metadata: {"job_group": "nightly-eval", "priority": "high"}
      },
    },
  });
}
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.5-flash:batchCreate" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "src": "files/uploaded_file_id",
    "config": {
      "display_name": "My Setup",
      "webhook_config": {
        "uris": ["https://my-api.com/gemini-webhook-dynamic"],
        "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
      }
    }
  }'
```

### Memverifikasi tanda tangan dinamis (JWKS)

Permintaan webhook dinamis memancarkan tanda tangan Token Web JSON (JWT). Pendengar Anda
harus mengekstrak tanda tangan dan memverifikasinya menggunakan [endpoint sertifikat publik Google](https://www.googleapis.com/oauth2/v3/certs).

### Python

```
import jwt
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Google public cert list endpoint
JWKS_URI = "https://generativelanguage.googleapis.com/.well-known/jwks.json"

def load_google_public_key(kid):
    response = requests.get(JWKS_URI).json()
    for key_item in response.get('keys', []):
        if key_item.get('kid') == kid:
            # Convert JWK to Cert wrapper
            return jwt.algorithms.RSAAlgorithm.from_jwk(key_item)
    return None

@app.route('/gemini-webhook-dynamic', methods=['POST'])
def dynamic_handler():
    payload = request.get_data(as_text=True)
    headers = request.headers

    token = headers.get('Webhook-Signature')
    if not token:
        return jsonify({"error": "No signature header"}), 400

    try:
        # Extract kid from JWT header
        unverified_headers = jwt.get_unverified_header(token)
        pub_key = load_google_public_key(unverified_headers.get('kid'))

        if not pub_key:
            return jsonify({"error": "Key cert not found"}), 400

        # Verify Signature against expected audience (e.g., your project client ID)
        event = jwt.decode(
            token,
            pub_key,
            algorithms=["RS256"],
            audience="your-configured-audience"
        )
    except Exception as e:
        return jsonify({"error": "Invalid Dynamic signature", "details": str(e)}), 400

    print("Verified Dynamic payload success.")
    return jsonify({"status": "received"}), 200
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import express from "express";
import jwt from "jsonwebtoken";
import jwksClient from "jwks-rsa";

const app = express();
app.use(express.text({ type: 'application/json' }));

const client = jwksClient({
  jwksUri: "https://generativelanguage.googleapis.com/.well-known/jwks.json"
});

function getKey(header, callback) {
  client.getSigningKey(header.kid, (err, key) => {
    const signingKey = key.getPublicKey();
    callback(null, signingKey);
  });
}

app.post('/gemini-webhook-dynamic', (req, res) => {
  const token = req.headers['webhook-signature'];

  if (!token) {
    return res.status(400).json({ error: "No signature header" });
  }

  jwt.verify(
    token,
    getKey,
    {
      algorithms: ["RS256"],
      audience: "your-configured-audience"
    },
    (err, decoded) => {
      if (err) {
        return res.status(400).json({ error: "Invalid Dynamic signature", details: err.message });
      }

      console.log("Verified Dynamic payload success.");
      res.status(200).json({ status: "received" });
    }
  );
});
```

## Amplop webhook

Untuk menghindari kemacetan bandwidth, webhook Gemini menggunakan model **payload tipis** untuk
mengirimkan data.
Pengiriman mengirimkan snapshot yang berisi detail status dan pointer ke hasil,
bukan file output mentah itu sendiri.

Berikut adalah contoh format payload:

```
{
  "type": "batch.succeeded",
  "version": "v1",
  "timestamp": "2026-01-22T12:00:00Z",
  "data": {
    "id": "batch_123456",
    "output_file_uri": "gs://my-bucket/results.jsonl"
  }
}
```

## Referensi katalog acara

Peristiwa berikut dipicu untuk tugas pendukung:

| Jenis peristiwa | Pemicu | Item payload (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Pemrosesan berhasil diselesaikan. | `id`, `output_file_uri` |
| `batch.cancelled` | Pengguna membatalkan permintaan | `id` |
| `batch.expired` | Batch belum diproses (selesai) dalam jangka waktu 24 jam | `id` |
| `batch.failed` | Tugas batch gagal (error sistem atau validasi). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Panggilan fungsi, pengguna perlu melakukan sesuatu | `id` |
| `interaction.completed` | LRO di API interaksi berhasil | `id` |
| `interaction.failed` | LRO di API interaksi gagal (error sistem atau validasi). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO di API interaksi dibatalkan | `id` |
| `video.generated` | LRO pembuatan video selesai. | `id`, `output_file_uri`, `file_name` |

## Praktik terbaik

Untuk memastikan operasi yang andal dan skalabel:

- **Pemeriksaan perlindungan pemutaran ulang ketat**: Semua permintaan membawa header `webhook-timestamp`. Selalu validasi stempel waktu ini di lapisan konfigurasi server Anda untuk menolak payload yang lebih lama dari **5 menit** (untuk memitigasi serangan replay).
- **Memproses secara asinkron**: Merespons dengan `2xx OK` segera setelah deteksi tanda tangan yang valid, dan mengantrekan operasi parsing secara internal. Waktu penahanan
  pendengar yang lama akan memicu siklus coba ulang pengiriman.
- **Penanganan penghapusan duplikat**: Webhook standar mengirimkan "Minimal sekali". Gunakan header `webhook-id` yang konsisten untuk menangani potensi duplikat dalam alur kemacetan yang lebih tinggi.

## Apa langkah selanjutnya?

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=id): Manfaatkan webhook untuk mengotomatiskan endpoint bervolume tinggi.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-24 UTC."],[],[]]
