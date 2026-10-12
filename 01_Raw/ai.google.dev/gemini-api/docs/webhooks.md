---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=th
fetched_at: 2026-10-12T07:03:09.191694+00:00
title: "\u0e40\u0e27\u0e47\u0e1a\u0e2e\u0e38\u0e04 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เว็บฮุค

Webhook ช่วยให้ Gemini API สามารถส่งการแจ้งเตือนแบบเรียลไทม์ไปยังเซิร์ฟเวอร์ของคุณ
เมื่อการดำเนินการแบบไม่พร้อมกันหรือการดำเนินการที่ใช้เวลานาน (LRO) เสร็จสมบูรณ์ ซึ่งมาแทนที่
ความจำเป็นในการสำรวจ API เพื่อดูการอัปเดตสถานะ ซึ่งจะช่วยลดเวลาในการตอบสนองและค่าใช้จ่าย

Webhook พร้อมใช้งานสำหรับการดำเนินการต่างๆ เช่น งาน[กลุ่ม](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)
[การโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) และ[การสร้างวิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)

## วิธีการทำงาน

แทนที่จะทำการสำรวจ`GET /operations`ซ้ำๆ เพื่อตรวจสอบว่างานเสร็จสิ้นแล้วหรือไม่
คุณสามารถกำหนดค่าเว็บฮุคของ Gemini API ให้ส่งคำขอ HTTP POST ไปยัง
URL ของ Listener ทันทีเมื่อมีการทริกเกอร์เหตุการณ์

Gemini API รองรับการกำหนดค่า Webhook 2 วิธี ดังนี้

- [**Webhook แบบคงที่**](#static-webhooks): ปลายทางระดับโปรเจ็กต์ที่กำหนดค่า
  ด้วย [WebhookService API](https://ai.google.dev/api?hl=th) ของ Gemini เหมาะสำหรับการผสานรวมทั่วโลก (เช่น การแจ้งเตือน Slack, การซิงค์ฐานข้อมูล ฯลฯ)
- [**เว็บฮุคแบบไดนามิก**](#dynamic-webhooks): การลบล้างระดับคำขอที่ส่ง URL ของเว็บฮุคในเพย์โหลดการกำหนดค่าของการเรียกงานที่เฉพาะเจาะจง เหมาะสำหรับ
  การกำหนดเส้นทางงานที่เฉพาะเจาะจงไปยังปลายทางเฉพาะ

## เว็บฮุคแบบคงที่

ระบบจะลงทะเบียนเว็บบุ๊กแบบคงที่สำหรับ[โปรเจ็กต์](https://ai.google.dev/gemini-api/docs/api-key?hl=th#google-cloud-projects)ทั้งหมดและทริกเกอร์สำหรับเหตุการณ์ที่ตรงกัน

### สร้างเว็บฮุค

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookInput;
import com.google.genai.gaos.models.webhooks.WebhookSubscribedEvent;
import java.util.Arrays;

Client client = new Client();

WebhookInput input =
    WebhookInput.builder()
        .name("MyBatchWebhook")
        .subscribedEvents(
            Arrays.asList(
                WebhookSubscribedEvent.BATCH_SUCCEEDED, WebhookSubscribedEvent.BATCH_FAILED))
        .uri("https://my-api.com/gemini-callback")
        .build();

Webhook webhook = client.webhooks.create(input).webhook().get();

// Store webhook.newSigningSecret() securely
String webhookSecret = webhook.newSigningSecret().orElse("");
System.out.println(
    "Created webhook: " + webhook.name().orElse("") + ", " + webhook.id().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/webhooks"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Webhooks.Create(ctx, operations.CreateWebhookRequest{
        Body: webhooks.WebhookInput{
            Name: genai.Ptr("MyBatchWebhook"),
            SubscribedEvents: []webhooks.WebhookSubscribedEvent{
                webhooks.WebhookSubscribedEventBatchSucceeded,
                webhooks.WebhookSubscribedEventBatchFailed,
            },
            URI: "https://my-api.com/gemini-callback",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    webhook := res.Webhook
    // Store webhook.GetNewSigningSecret() securely
    _ = webhook.GetNewSigningSecret()
    fmt.Printf("Created webhook: %v, %v\n", webhook.GetName(), webhook.GetID())
}
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

ดึงรายละเอียดเกี่ยวกับ Webhook ที่เฉพาะเจาะจงตามชื่อทรัพยากร

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import java.util.Collections;

Client client = new Client();

Webhook webhook = client.webhooks.get("<your_webhook_id>").webhook().get();

System.out.println("Webhook: " + webhook.name().orElse(""));
System.out.println("URI: " + webhook.uri().orElse(""));
System.out.println("Events: " + webhook.subscribedEvents().orElse(Collections.emptyList()));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Webhooks.Get(ctx, operations.GetWebhookRequest{
        ID: "<your_webhook_id>",
    })
    if err != nil {
        log.Fatal(err)
    }

    webhook := res.Webhook
    if webhook.Name != nil {
        fmt.Printf("Webhook: %s\n", *webhook.Name)
    }
    fmt.Printf("URI: %s\n", webhook.URI)
    fmt.Printf("Events: %v\n", webhook.SubscribedEvents)
}
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### แสดงรายการเว็บฮุค

แสดงรายการ Webhook ทั้งหมดที่กำหนดค่าไว้สำหรับโปรเจ็กต์ปัจจุบัน โดยมีการแบ่งหน้าเป็นตัวเลือก

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookListResponse;
import java.util.Collections;

Client client = new Client();

WebhookListResponse response =
    client.webhooks.listDirect().webhookListResponse().orElse(new WebhookListResponse());

for (Webhook wh : response.webhooks().orElse(Collections.emptyList())) {
  System.out.println(
      wh.id().orElse("") + ": " + wh.name().orElse("") + " -> " + wh.uri().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Webhooks.List(ctx, operations.ListWebhooksRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.WebhookListResponse != nil {
        for _, wh := range res.WebhookListResponse.Webhooks {
            fmt.Printf("%v: %v -> %s\n", wh.GetID(), wh.GetName(), wh.URI)
        }
    }
}
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### อัปเดตเว็บฮุค

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookUpdate;
import com.google.genai.gaos.models.webhooks.WebhookUpdateSubscribedEvent;
import java.util.Arrays;

Client client = new Client();

WebhookUpdate updateBody =
    WebhookUpdate.builder()
        .subscribedEvents(
            Arrays.asList(
                WebhookUpdateSubscribedEvent.BATCH_SUCCEEDED,
                WebhookUpdateSubscribedEvent.BATCH_FAILED,
                WebhookUpdateSubscribedEvent.of("batch.cancelled")))
        .build();

Webhook updatedWebhook =
    client.webhooks
        .update()
        .id("<your_webhook_id>")
        .updateMask("subscribed_events")
        .body(updateBody)
        .call()
        .webhook()
        .get();

System.out.println("Updated webhook: " + updatedWebhook.name().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/webhooks"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Webhooks.Update(ctx, operations.UpdateWebhookRequest{
        ID:         "<your_webhook_id>",
        UpdateMask: genai.Ptr("subscribed_events"),
        Body: &webhooks.WebhookUpdate{
            SubscribedEvents: []webhooks.WebhookUpdateSubscribedEvent{
                webhooks.WebhookUpdateSubscribedEventBatchSucceeded,
                webhooks.WebhookUpdateSubscribedEventBatchFailed,
                webhooks.WebhookUpdateSubscribedEvent("batch.cancelled"),
            },
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Webhook.Name != nil {
        fmt.Printf("Updated webhook: %s\n", *res.Webhook.Name)
    }
}
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

นำปลายทางของเว็บฮุคออกจากโปรเจ็กต์ ซึ่งจะเป็นการหยุดการนำส่งเหตุการณ์ในอนาคต
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

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.webhooks.delete("<your_webhook_id>");

System.out.println("Webhook deleted.");
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Webhooks.Delete(ctx, operations.DeleteWebhookRequest{
        ID: "<your_webhook_id>",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Webhook deleted.")
}
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### หมุนเวียนข้อมูลลับในการลงนาม

หมุนเวียนข้อมูลลับในการลงนามสำหรับ Webhook คุณสามารถกำหนดค่าว่าจะเพิกถอนข้อมูลลับที่เคย
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.RevocationBehavior;
import com.google.genai.gaos.models.webhooks.RotateSigningSecretRequest;
import com.google.genai.gaos.models.webhooks.WebhookRotateSigningSecretResponse;

Client client = new Client();

RotateSigningSecretRequest requestBody =
    RotateSigningSecretRequest.builder()
        .revocationBehavior(RevocationBehavior.REVOKE_PREVIOUS_SECRETS_AFTER_H24)
        .build();

WebhookRotateSigningSecretResponse response =
    client.webhooks
        .rotateSigningSecret()
        .id("<your_webhook_id>")
        .body(requestBody)
        .call()
        .webhookRotateSigningSecretResponse()
        .get();

// Store response.secret() securely, then update your server's verification config
String newSecret = response.secret().orElse("");
System.out.println("New signing secret generated. Update your server configuration.");
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/webhooks"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Webhooks.RotateSigningSecret(ctx, operations.RotateSigningSecretRequest{
        ID: "<your_webhook_id>",
        Body: &webhooks.RotateSigningSecretRequest{
            RevocationBehavior: webhooks.RevocationBehaviorRevokePreviousSecretsAfterH24.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    // Store res.WebhookRotateSigningSecretResponse.GetSecret() securely, then update your server's verification config
    _ = res.WebhookRotateSigningSecretResponse.GetSecret()
    fmt.Println("New signing secret generated. Update your server configuration.")
}
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

เมื่อเกิดเหตุการณ์ที่คุณติดตาม URL ของเว็บฮุคจะได้รับคำขอ HTTP POST ปลายทางต้องตอบกลับด้วยรหัสสถานะ 2xx
ภายในไม่กี่วินาทีเพื่อหลีกเลี่ยงการลองใหม่ Gemini API จะลองส่งคำขอที่ไม่สำเร็จซ้ำโดยอัตโนมัติเป็นเวลา 24 ชั่วโมงโดยใช้ Exponential Backoff เพื่อให้มั่นใจว่าคำขอจะได้รับการนำส่ง

Gemini ปฏิบัติตามข้อกำหนดเฉพาะของ [Webhooks มาตรฐาน](https://github.com/standard-webhooks/standard-webhooks)อย่างเคร่งครัดสำหรับ
ส่วนหัวด้านความปลอดภัย ยืนยันเพย์โหลดในเซิร์ฟเวอร์โดยใช้ส่วนหัวที่ลงชื่อ
signatures และรหัสลับการลงชื่อแบบคงที่ที่จัดเก็บไว้ ดูข้อมูลเพย์โหลดได้ที่ส่วน[ซองจดหมายของ Webhook](#webhook-envelope)

ตัวอย่างการใช้ Flask สำหรับเครื่องมือฟัง HTTP มีดังนี้

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

### Java

```
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

String signingSecret = System.getenv("WEBHOOK_SIGNING_SECRET");

HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
server.createContext(
    "/gemini-callback",
    exchange -> {
      String payload =
          new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
      String msgId = exchange.getRequestHeaders().getFirst("webhook-id");
      String msgTimestamp = exchange.getRequestHeaders().getFirst("webhook-timestamp");
      String msgSignature = exchange.getRequestHeaders().getFirst("webhook-signature");

      try {
        String toSign = msgId + "." + msgTimestamp + "." + payload;
        Mac mac = Mac.getInstance("HmacSHA256");
        byte[] secretBytes =
            Base64.getDecoder().decode(signingSecret.replaceFirst("^whsec_", ""));
        mac.init(new SecretKeySpec(secretBytes, "HmacSHA256"));
        String expectedSig =
            "v1,"
                + Base64.getEncoder()
                    .encodeToString(mac.doFinal(toSign.getBytes(StandardCharsets.UTF_8)));

        if (msgSignature == null || !msgSignature.contains(expectedSig)) {
          byte[] resp = "{\"error\": \"Signature invalid\"}".getBytes(StandardCharsets.UTF_8);
          exchange.sendResponseHeaders(400, resp.length);
          try (OutputStream os = exchange.getResponseBody()) {
            os.write(resp);
          }
          return;
        }

        Matcher typeMatcher = Pattern.compile("\"type\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String type = typeMatcher.find() ? typeMatcher.group(1) : "";

        Matcher idMatcher = Pattern.compile("\"id\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String id = idMatcher.find() ? idMatcher.group(1) : "";

        Matcher uriMatcher =
            Pattern.compile("\"output_file_uri\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String outputFileUri = uriMatcher.find() ? uriMatcher.group(1) : "";

        if ("batch.succeeded".equals(type)) {
          System.out.println("Batch completed! ID: " + id);
          if (!outputFileUri.isEmpty()) {
            System.out.println("Batch file: " + outputFileUri);
          }
        } else if ("interaction.completed".equals(type)) {
          System.out.println("Interaction completed! ID: " + id);
        } else if ("video.generated".equals(type)) {
          System.out.println("Video generated! URI: " + outputFileUri);
        }

        byte[] resp = "{\"status\": \"received\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(200, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      } catch (Exception e) {
        exchange.sendResponseHeaders(400, -1);
      }
    });
server.start();
```

### Go

```
package main

import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io"
    "log"
    "net/http"
    "os"
    "strings"

)

func main() {
    signingSecret := os.Getenv("WEBHOOK_SIGNING_SECRET")

    http.HandleFunc("/gemini-callback", func(w http.ResponseWriter, r *http.Request) {
        payloadBytes, err := io.ReadAll(r.Body)
        if err != nil {
            http.Error(w, `{"error": "Failed to read body"}`, http.StatusBadRequest)
            return
        }
        payload := string(payloadBytes)
        msgID := r.Header.Get("webhook-id")
        msgTimestamp := r.Header.Get("webhook-timestamp")
        msgSignature := r.Header.Get("webhook-signature")

        secretBytes, err := base64.StdEncoding.DecodeString(strings.TrimPrefix(signingSecret, "whsec_"))
        if err != nil {
            http.Error(w, `{"error": "Invalid secret"}`, http.StatusBadRequest)
            return
        }

        toSign := fmt.Sprintf("%s.%s.%s", msgID, msgTimestamp, payload)
        mac := hmac.New(sha256.New, secretBytes)
        mac.Write([]byte(toSign))
        expectedSig := "v1," + base64.StdEncoding.EncodeToString(mac.Sum(nil))

        if msgSignature == "" || !strings.Contains(msgSignature, expectedSig) {
            http.Error(w, `{"error": "Signature invalid"}`, http.StatusBadRequest)
            return
        }

        var event struct {
            Type string `json:"type"`
            Data struct {
                ID            string `json:"id"`
                OutputFileURI string `json:"output_file_uri"`
            } `json:"data"`
        }
        _ = json.Unmarshal(payloadBytes, &event)

        switch event.Type {
        case "batch.succeeded":
            fmt.Printf("Batch completed! ID: %s\n", event.Data.ID)
            if event.Data.OutputFileURI != "" {
                fmt.Printf("Batch file: %s\n", event.Data.OutputFileURI)
            }
        case "interaction.completed":
            fmt.Printf("Interaction completed! ID: %s\n", event.Data.ID)
        case "video.generated":
            fmt.Printf("Video generated! URI: %s\n", event.Data.OutputFileURI)
        }

        w.Header().Set("Content-Type", "application/json")
        w.WriteHeader(http.StatusOK)
        _, _ = w.Write([]byte(`{"status": "received"}`))
    })

    log.Fatal(http.ListenAndServe(":8000", nil))
}
```

## เว็บฮุกแบบไดนามิก

Webhook แบบไดนามิกช่วยให้คุณเชื่อมโยงปลายทางของ Webhook กับ**การกำหนดค่าคำขอที่เฉพาะเจาะจง** ซึ่งเหมาะสำหรับคิวการจัดคิวของตัวแทน Webhook แบบไดนามิกใช้ประโยชน์จากลายเซ็น JWKS คีย์สาธารณะแบบอสมมาตรแทนที่จะใช้ลับแบบสมมาตร

### ส่งคำขอแบบไดนามิก

เพิ่ม `webhook_config` เมื่อทริกเกอร์งานแบบไม่พร้อมกัน (เช่น การสร้าง
Batch)

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3.8-flash',
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
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createInteractionWithWebhook() {
  const response = await client.interactions.create({
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.WebhookConfig;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> userMetadata = new HashMap<>();
userMetadata.put("job_group", "nightly-eval");
userMetadata.put("priority", "high");

WebhookConfig webhookConfig =
    WebhookConfig.builder()
        .uris(Arrays.asList("https://my-api.com/gemini-webhook-dynamic"))
        .userMetadata(userMetadata)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Tell me a short joke about programming."))
        .background(true) // Required when webhookConfig is specified
        .webhookConfig(webhookConfig)
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Interaction created! ID: " + response.id().orElse(""));
System.out.println(
    "Status: " + response.status().map(InteractionStatus::value).orElse(""));
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
            Model:      interactions.Model("gemini-3.8-flash"),
            Input:      interactions.NewInteractionsInput("Tell me a short joke about programming."),
            Background: genai.Ptr(true), // Required when WebhookConfig is specified
            WebhookConfig: &interactions.WebhookConfig{
                Uris: []string{"https://my-api.com/gemini-webhook-dynamic"},
                UserMetadata: map[string]any{
                    "job_group": "nightly-eval",
                    "priority":  "high",
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.ID != nil {
        fmt.Printf("Interaction created! ID: %s\n", *res.Interaction.ID)
    }
    fmt.Printf("Status: %s\n", res.Interaction.Status)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### ยืนยันลายเซ็นแบบไดนามิก (JWKS)

คำขอเว็บฮุกแบบไดนามิกจะปล่อยลายเซ็นโทเค็นเว็บ JSON (JWT) ผู้ฟัง
ต้องแยกข้อมูลลายเซ็นและยืนยันโดยใช้[ปลายทางใบรับรองสาธารณะของ Google](https://www.googleapis.com/oauth2/v3/certs)

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

### Java

```
import com.sun.net.httpserver.HttpServer;
import java.io.InputStream;
import java.io.OutputStream;
import java.math.BigInteger;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.RSAPublicKeySpec;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

String jwksUri = "https://generativelanguage.googleapis.com/.well-known/jwks.json";

HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
server.createContext(
    "/gemini-webhook-dynamic",
    exchange -> {
      String token = exchange.getRequestHeaders().getFirst("Webhook-Signature");
      if (token == null || token.split("\\.").length != 3) {
        byte[] resp = "{\"error\": \"No signature header\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(400, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
        return;
      }

      try {
        String[] parts = token.split("\\.");
        String headerJson =
            new String(Base64.getUrlDecoder().decode(parts[0]), StandardCharsets.UTF_8);
        Matcher kidMatcher = Pattern.compile("\"kid\"\\s*:\\s*\"([^\"]+)\"").matcher(headerJson);
        String kid = kidMatcher.find() ? kidMatcher.group(1) : "";

        PublicKey pubKey = null;
        try (InputStream in = URI.create(jwksUri).toURL().openStream()) {
          String jwksJson = new String(in.readAllBytes(), StandardCharsets.UTF_8);
          Matcher keyBlockMatcher =
              Pattern.compile(
                      "\\{[^}]*\"kid\"\\s*:\\s*\"" + Pattern.quote(kid) + "\"[^}]*\\}")
                  .matcher(jwksJson);
          if (keyBlockMatcher.find()) {
            String keyBlock = keyBlockMatcher.group(0);
            Matcher nMatcher = Pattern.compile("\"n\"\\s*:\\s*\"([^\"]+)\"").matcher(keyBlock);
            Matcher eMatcher = Pattern.compile("\"e\"\\s*:\\s*\"([^\"]+)\"").matcher(keyBlock);
            if (nMatcher.find() && eMatcher.find()) {
              BigInteger n =
                  new BigInteger(1, Base64.getUrlDecoder().decode(nMatcher.group(1)));
              BigInteger e =
                  new BigInteger(1, Base64.getUrlDecoder().decode(eMatcher.group(1)));
              pubKey =
                  KeyFactory.getInstance("RSA").generatePublic(new RSAPublicKeySpec(n, e));
            }
          }
        }

        Signature sig = Signature.getInstance("SHA256withRSA");
        sig.initVerify(pubKey);
        sig.update((parts[0] + "." + parts[1]).getBytes(StandardCharsets.UTF_8));
        boolean verified = sig.verify(Base64.getUrlDecoder().decode(parts[2]));

        if (!verified) {
          throw new SecurityException("Signature verification failed");
        }

        System.out.println("Verified Dynamic payload success.");
        byte[] resp = "{\"status\": \"received\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(200, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      } catch (Exception e) {
        byte[] resp =
            ("{\"error\": \"Invalid Dynamic signature\", \"details\": \""
                    + e.getMessage()
                    + "\"}")
                .getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(400, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      }
    });
server.start();
```

### Go

```
package main

import (
    "crypto"
    "crypto/rsa"
    "crypto/sha256"
    "encoding/base64"
    "encoding/json"
    "fmt"
    "io"
    "log"
    "math/big"
    "net/http"
    "strings"

)

func main() {
    jwksURI := "https://generativelanguage.googleapis.com/.well-known/jwks.json"

    http.HandleFunc("/gemini-webhook-dynamic", func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Webhook-Signature")
        parts := strings.Split(token, ".")
        if len(parts) != 3 {
            http.Error(w, `{"error": "No signature header"}`, http.StatusBadRequest)
            return
        }

        headerBytes, err := base64.RawURLEncoding.DecodeString(parts[0])
        if err != nil {
            http.Error(w, `{"error": "Invalid header"}`, http.StatusBadRequest)
            return
        }
        var header struct {
            Kid string `json:"kid"`
        }
        _ = json.Unmarshal(headerBytes, &header)

        resp, err := http.Get(jwksURI)
        if err != nil {
            http.Error(w, `{"error": "Failed to fetch JWKS"}`, http.StatusBadRequest)
            return
        }
        defer resp.Body.Close()
        jwksBytes, _ := io.ReadAll(resp.Body)

        var jwks struct {
            Keys []struct {
                Kid string `json:"kid"`
                N   string `json:"n"`
                E   string `json:"e"`
            } `json:"keys"`
        }
        _ = json.Unmarshal(jwksBytes, &jwks)

        var pubKey *rsa.PublicKey
        for _, k := range jwks.Keys {
            if k.Kid == header.Kid {
                nBytes, _ := base64.RawURLEncoding.DecodeString(k.N)
                eBytes, _ := base64.RawURLEncoding.DecodeString(k.E)
                pubKey = &rsa.PublicKey{
                    N: new(big.Int).SetBytes(nBytes),
                    E: int(new(big.Int).SetBytes(eBytes).Int64()),
                }
                break
            }
        }
        if pubKey == nil {
            http.Error(w, `{"error": "Matching key not found"}`, http.StatusBadRequest)
            return
        }

        sigBytes, _ := base64.RawURLEncoding.DecodeString(parts[2])
        hashed := sha256.Sum256([]byte(parts[0] + "." + parts[1]))
        if err := rsa.VerifyPKCS1v15(pubKey, crypto.SHA256, hashed[:], sigBytes); err != nil {
            http.Error(w, `{"error": "Invalid Dynamic signature"}`, http.StatusBadRequest)
            return
        }

        fmt.Println("Verified Dynamic payload success.")
        w.Header().Set("Content-Type", "application/json")
        w.WriteHeader(http.StatusOK)
        _, _ = w.Write([]byte(`{"status": "received"}`))
    })

    log.Fatal(http.ListenAndServe(":8000", nil))
}
```

## ซองจดหมายของเว็บฮุค

Webhook ของ Gemini ใช้โมเดล**เพย์โหลดแบบบาง**เพื่อส่งข้อมูล
การนำส่งจะส่งสแนปชอตที่มีรายละเอียดสถานะและตัวชี้ไปยังผลลัพธ์
แทนที่จะเป็นไฟล์เอาต์พุตดิบ

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
| `interaction.completed` | LRO ใน Interactions API สำเร็จแล้ว | `id` |
| `interaction.failed` | LRO ใน Interactions API ล้มเหลว (ข้อผิดพลาดของระบบหรือการตรวจสอบ) | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | ยกเลิก LRO ใน Interactions API แล้ว | `id` |
| `video.generated` | LRO การสร้างวิดีโอเสร็จสมบูรณ์แล้ว | `id`, `output_file_uri`, `file_name` |

## แนวทางปฏิบัติแนะนำ

เพื่อให้การดำเนินงานมีความน่าเชื่อถือและรองรับการปรับขนาด ให้ทำดังนี้

- **การตรวจสอบการป้องกันการเล่นซ้ำอย่างเข้มงวด**: คำขอทั้งหมดมี`webhook-timestamp`
  ส่วนหัว ตรวจสอบการประทับเวลาในเลเยอร์การกำหนดค่าเซิร์ฟเวอร์เสมอเพื่อปฏิเสธเพย์โหลดที่เก่ากว่า**5 นาที** (เพื่อลดการโจมตีแบบรีเพลย์)
- **ประมวลผลแบบไม่พร้อมกัน**: ตอบกลับด้วย `2xx OK` ทันทีที่ตรวจพบ
  ลายเซ็นที่ถูกต้อง และจัดคิวการแยกวิเคราะห์ภายใน ระยะเวลาการรอสายที่นานเกินไปจะทริกเกอร์รอบการลองนำส่งอีกครั้ง
- **การจัดการการกรองข้อมูลที่ซ้ำกันออก**: เว็บฮุกมาตรฐานจะส่ง "อย่างน้อย 1 ครั้ง" ใช้ส่วนหัว
  ที่สอดคล้องกัน`webhook-id`เพื่อจัดการรายการที่อาจซ้ำกันในโฟลว์ที่มีความหนาแน่น
  สูงกว่า

## ต้องทำอะไรต่อ

- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th): ใช้ Webhook เพื่อทำให้ปลายทางที่มีปริมาณสูงเป็นแบบอัตโนมัติ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
