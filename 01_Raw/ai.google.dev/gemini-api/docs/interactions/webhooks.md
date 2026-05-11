---
source_url: https://ai.google.dev/gemini-api/docs/interactions/webhooks?hl=th
fetched_at: 2026-05-11T04:58:02.058821+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เว็บฮุค

Webhook ช่วยให้ Gemini API สามารถส่งการแจ้งเตือนแบบเรียลไทม์ไปยังเซิร์ฟเวอร์ของคุณ
เมื่อการดำเนินการแบบไม่พร้อมกันหรือการดำเนินการที่ใช้เวลานาน (LRO) เสร็จสมบูรณ์ ซึ่งจะมาแทนที่
ความจำเป็นในการสำรวจ API เพื่อดูการอัปเดตสถานะ ซึ่งจะช่วยลดเวลาในการตอบสนองและค่าใช้จ่าย

Webhook พร้อมใช้งานสำหรับการดำเนินการต่างๆ เช่น งาน[เป็นกลุ่ม](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)
[การโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions?hl=th) และ[การสร้างวิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)

## วิธีการทำงาน

แทนที่จะสำรวจ`GET /operations`ซ้ำๆ เพื่อตรวจสอบว่างานเสร็จสิ้นแล้วหรือไม่
คุณสามารถกำหนดค่าเว็บฮุคของ Gemini API เพื่อส่งคำขอ HTTP POST ไปยัง
URL ของ Listener ทันทีเมื่อมีการทริกเกอร์เหตุการณ์

Gemini API รองรับการกำหนดค่าเว็บฮุก 2 วิธี ได้แก่

- [**Webhook แบบคงที่**](#static-webhooks): จุดสิ้นสุดระดับโปรเจ็กต์ที่กำหนดค่าด้วย [WebhookService API](https://ai.google.dev/api?hl=th) ของ Gemini เหมาะสำหรับการผสานรวมทั่วโลก (เช่น การแจ้งเตือน Slack, การซิงค์ฐานข้อมูล ฯลฯ)
- [**เว็บฮุคแบบไดนามิก**](#dynamic-webhooks): การลบล้างระดับคำขอที่ส่ง URL ของเว็บฮุคในเพย์โหลดการกำหนดค่าของการเรียกงานที่เฉพาะเจาะจง เหมาะสำหรับ
  การกำหนดเส้นทางงานที่เฉพาะเจาะจงไปยังปลายทางเฉพาะ

## เว็บฮุคแบบคงที่

ระบบจะลงทะเบียนเว็บบุ๊กแบบคงที่สำหรับทั้ง[โปรเจ็กต์](https://ai.google.dev/gemini-api/docs/api-key?hl=th#google-cloud-projects)และทริกเกอร์สำหรับเหตุการณ์ที่ตรงกัน

### สร้างเว็บฮุก

คุณสร้างปลายทางได้โดยใช้ SDK หรือ REST API

**สำคัญ**: เมื่อสร้าง Webhook แล้ว API จะแสดง**ข้อมูลลับในการลงนาม**
**เพียงครั้งเดียว** คุณต้องจัดเก็บข้อมูลนี้อย่างปลอดภัย (เช่น ในตัวแปรสภาพแวดล้อม) เพื่อยืนยันลายเซ็นในภายหลัง
หากทำคีย์ลับสำหรับการลงนามหาย คุณจะต้อง[หมุนเวียน](#rotate-signing-secret)คีย์ลับ

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

ดูรายละเอียดเกี่ยวกับการตั้งค่าเซิร์ฟเวอร์เพื่อรับข้อมูลได้ที่ส่วน[จัดการคำขอ Webhook](#handle-webhook-requests)

### รับเว็บฮุค

ดึงรายละเอียดเกี่ยวกับเว็บบุ๊กที่เฉพาะเจาะจงตามชื่อทรัพยากร

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

### แสดงรายการเว็บฮุค

แสดงรายการเว็บฮุกทั้งหมดที่กำหนดค่าไว้สำหรับโปรเจ็กต์ปัจจุบัน โดยมีการแบ่งหน้าเป็นตัวเลือก

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

### อัปเดตเว็บฮุก

อัปเดตพร็อพเพอร์ตี้ของ Webhook ที่มีอยู่ เช่น ชื่อที่แสดง, URI เป้าหมาย หรือ
เหตุการณ์ที่สมัครรับข้อมูล

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

### ลบเว็บฮุค

นำปลายทางของเว็บฮุกออกจากโปรเจ็กต์ ซึ่งจะเป็นการหยุดการนำส่งเหตุการณ์ในอนาคต
ไปยังปลายทางนั้น

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

### หมุนเวียนข้อมูลลับในการลงนาม

หมุนเวียนรหัสลับการลงนามสำหรับเว็บฮุก คุณสามารถกำหนดค่าว่าจะเพิกถอนข้อมูลลับที่เคย
ใช้งานอยู่ทันทีหรือหลังจากระยะเวลาผ่อนผัน 24 ชั่วโมง

**สำคัญ**: ระบบจะแสดงข้อมูลลับในการลงนามใหม่**เพียงครั้งเดียว**เมื่อถึงเวลาหมุนเวียน
โปรดจัดเก็บอย่างปลอดภัยก่อนอัปเดตตรรกะการยืนยัน

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

### จัดการคำขอเว็บฮุคในเซิร์ฟเวอร์

เมื่อเกิดเหตุการณ์ที่คุณติดตาม URL ของเว็บฮุคจะได้รับคำขอ HTTP POST
ปลายทางต้องตอบกลับด้วยรหัสสถานะ 2xx ภายในไม่กี่วินาทีเพื่อหลีกเลี่ยงการลองใหม่ Gemini API จะลองส่งคำขอที่ไม่สำเร็จอีกครั้งโดยอัตโนมัติเป็นเวลา 24 ชั่วโมงโดยใช้ Exponential Backoff เพื่อให้มั่นใจว่าคำขอจะได้รับการนำส่ง

Gemini ปฏิบัติตามข้อกำหนดของ [Webhooks มาตรฐาน](https://github.com/standard-webhooks/standard-webhooks)อย่างเคร่งครัดสำหรับ
ส่วนหัวด้านความปลอดภัย ยืนยันเพย์โหลดในเซิร์ฟเวอร์โดยใช้ส่วนหัวที่ลงชื่อ
signatures และรหัสลับการลงชื่อแบบคงที่ที่จัดเก็บไว้ ดูข้อมูลเพย์โหลดได้ที่ส่วน[ซองจดหมายของ Webhook](#webhook-envelope)

ตัวอย่างการใช้ Flask สำหรับ Listener HTTP มีดังนี้

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
        print(f"Batch completed! ID: {event['data']['id']}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event['data']['output_file_uri']}")
    elif event.get("type") == "interaction.completed":
        print(f"Interaction completed! ID: {event['data']['id']}")
    elif event.get("type") == "video.generated":
        print(f"Video generated! URI: {event['data']['output_file_uri']}")

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
            } else if (event.type === "interaction.completed") {
                console.log(`Interaction completed! ID: ${event.data.id}`);
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

## เว็บฮุคแบบไดนามิก

Webhook แบบไดนามิกช่วยให้คุณเชื่อมโยงปลายทางของ Webhook กับ**การกำหนดค่าคำขอที่เฉพาะเจาะจง** ซึ่งเหมาะสำหรับคิวการจัดการเป็นกลุ่มของตัวแทน Webhook แบบไดนามิกใช้ประโยชน์จากลายเซ็น JWKS คีย์สาธารณะแบบอสมมาตรแทนที่จะใช้ลับแบบสมมาตร

### ส่งคำขอแบบไดนามิก

เพิ่ม `webhook_config` เมื่อทริกเกอร์งานแบบไม่พร้อมกัน (เช่น การสร้าง
Batch)

### Python

```
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3-flash-preview',
    input='Tell me a short joke about programming.',
    background=True, # Required when webhook_config is specified
    webhook_config={
        'uris': ["https://my-api.com/gemini-webhook-dynamic"],
        'user_metadata': {"job_group": "nightly-eval", "priority": "high"}
    }
)

print(f"Interaction created! ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createInteractionWithWebhook() {
  const response = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Tell me a short joke about programming.",
    background: true, // Required when webhook_config is specified
    webhook_config: {
      uris: ["https://my-api.com/gemini-webhook-dynamic"],
      user_metadata: { job_group: "nightly-eval", priority: "high" },
    },
  });

  console.log(`Interaction created! ID: ${response.id}`);
  console.log(`Status: ${response.status}`);
}

createInteractionWithWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### ยืนยันลายเซ็นแบบไดนามิก (JWKS)

คำขอเว็บบุ๊กแบบไดนามิกจะปล่อยลายเซ็นโทเค็นเว็บ JSON (JWT) ผู้ฟังต้องแยกข้อมูลลายเซ็นและยืนยันโดยใช้[ปลายทางใบรับรองสาธารณะของ Google](https://www.googleapis.com/oauth2/v3/certs)

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

## ซองจดหมายของเว็บฮุค

Webhook ของ Gemini ใช้โมเดล**เพย์โหลดขนาดเล็ก**เพื่อส่งข้อมูล
เพื่อหลีกเลี่ยงการใช้งานแบนด์วิดท์มากเกินไป
การนำส่งจะส่งสแนปชอตที่มีรายละเอียดสถานะและตัวชี้ไปยังผลลัพธ์
แทนที่จะส่งไฟล์เอาต์พุตดิบเอง

ตัวอย่างรูปแบบเพย์โหลดมีดังนี้

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

## ข้อมูลอ้างอิงแคตตาล็อกกิจกรรม

ระบบจะทริกเกอร์เหตุการณ์ต่อไปนี้สำหรับงานที่รองรับ

| ประเภทของกิจกรรม | ทริกเกอร์ | รายการเพย์โหลด (`data`) |
| --- | --- | --- |
| `batch.succeeded` | การประมวลผลเสร็จสมบูรณ์แล้ว | `id`, `output_file_uri` |
| `batch.cancelled` | ผู้ใช้ยกเลิกคำขอ | `id` |
| `batch.expired` | ระบบยังไม่ได้ประมวลผล (เสร็จสิ้น) แบตช์ภายในกรอบเวลา 24 ชั่วโมง | `id` |
| `batch.failed` | งานแบบกลุ่มล้มเหลว (ข้อผิดพลาดของระบบหรือการตรวจสอบ) | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | การเรียกใช้ฟังก์ชัน ผู้ใช้ต้องดำเนินการบางอย่าง | `id` |
| `interaction.completed` | LRO ในการโต้ตอบ API สำเร็จแล้ว | `id` |
| `interaction.failed` | LRO ใน Interactions API ล้มเหลว (ข้อผิดพลาดของระบบหรือการตรวจสอบ) | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | ยกเลิก LRO ใน Interactions API แล้ว | `id` |
| `video.generated` | LRO การสร้างวิดีโอเสร็จสมบูรณ์แล้ว | `id`, `output_file_uri`, `file_name` |

## แนวทางปฏิบัติแนะนำ

เพื่อให้การดำเนินงานมีความน่าเชื่อถือและรองรับการปรับขนาด

- **การตรวจสอบการป้องกันการเล่นซ้ำอย่างเข้มงวด**: คำขอทั้งหมดมี`webhook-timestamp`
  ส่วนหัว ตรวจสอบการประทับเวลาในเลเยอร์การกำหนดค่าเซิร์ฟเวอร์เสมอเพื่อปฏิเสธเพย์โหลดที่เก่ากว่า**5 นาที** (เพื่อลดการโจมตีแบบเล่นซ้ำ)
- **ประมวลผลแบบไม่พร้อมกัน**: ตอบกลับด้วย `2xx OK` ทันทีเมื่อตรวจพบ
  ลายเซ็นที่ถูกต้อง และจัดคิวการแยกวิเคราะห์ภายใน ระยะเวลาที่ผู้ฟังถือสายเป็นเวลานานจะทริกเกอร์รอบการลองนำส่งอีกครั้ง
- **การจัดการการขจัดข้อมูลที่ซ้ำกัน**: เว็บฮุกมาตรฐานจะส่ง "อย่างน้อย 1 ครั้ง" ใช้ ส่วนหัวที่สอดคล้องกัน`webhook-id`เพื่อจัดการรายการที่อาจซ้ำกันในโฟลว์ที่มีความ หนาแน่นสูงกว่า

## ขั้นตอนต่อไปคืออะไร

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=th): ใช้ Webhook เพื่อทำให้ปลายทางที่มีปริมาณสูงเป็นแบบอัตโนมัติ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-08 UTC"],[],[]]
