---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=tr
fetched_at: 2026-06-08T05:27:37.338022+00:00
title: "Webhook'lar \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Webhook'lar

Webhook'lar, eşzamansız veya uzun süren işlemler (LRO) tamamlandığında Gemini API'nin sunucunuza gerçek zamanlı bildirimler göndermesine olanak tanır. Bu, durum güncellemeleri için API'ye yoklama yapma ihtiyacını ortadan kaldırarak gecikmeyi ve ek yükü azaltır.

Web kancaları, [toplu](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr) işler, [etkileşimler](https://ai.google.dev/gemini-api/docs/interactions?hl=tr) ve [video oluşturma](https://ai.google.dev/gemini-api/docs/video?hl=tr) gibi işlemler için kullanılabilir.

## İşleyiş şekli

Bir işin tamamlanıp tamamlanmadığını kontrol etmek için `GET /operations`'i tekrar tekrar yoklamak yerine, bir etkinlik tetiklendiğinde Gemini API Web kancalarını dinleyici URL'nize hemen bir HTTP POST isteği gönderecek şekilde yapılandırabilirsiniz.

Gemini API, webhook'ları yapılandırmak için iki yöntemi destekler:

- [**Statik webhook'lar**](#static-webhooks): Gemini [WebhookService API](https://ai.google.dev/api?hl=tr) ile yapılandırılmış proje düzeyinde uç noktalar. Küresel entegrasyonlar için uygundur (ör. Slack'e bildirim gönderme, veritabanı senkronize etme vb.).
- [**Dinamik webhook'lar**](#dynamic-webhooks): Belirli bir iş çağrısının yapılandırma yükünde webhook URL'si ileten istek düzeyinde geçersiz kılmalar. Belirli işleri özel uç noktalara yönlendirmek için idealdir.

## Statik web kancaları

Statik webhook'lar, tüm [proje](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#google-cloud-projects) için kaydedilir ve eşleşen tüm etkinlikler için tetiklenir.

### Webhook oluşturma

SDK veya REST API'yi kullanarak uç noktalar oluşturabilirsiniz.

**ÖNEMLİ**: API, webhook oluştururken **imza gizli anahtarını**
**yalnızca bir kez** döndürür. İmzaları daha sonra doğrulamak için bunu güvenli bir şekilde (ör. ortam değişkenlerinizde) saklamanız gerekir. İmzalama gizli anahtarını kaybederseniz [döndürmeniz](#rotate-signing-secret) gerekir.

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

Sunucunuzu veri alacak şekilde ayarlama hakkında ayrıntılı bilgi için [Webhook isteklerini işleme](#handle-webhook-requests) bölümüne bakın.

### Webhook alma

Kaynak adına göre belirli bir webhook hakkında ayrıntıları alın.

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

### Webhook'ları listeleme

Geçerli proje için yapılandırılmış tüm webhook'ları isteğe bağlı sayfalama ile listeleyin.

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

### Webhook'u güncelleme

Mevcut bir webhook'un görünen ad, hedef URI veya abone olunan etkinlikler gibi özelliklerini güncelleyin.

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

### Webhook silme

Projeden bir webhook uç noktasını kaldırma. Bu işlem, gelecekteki etkinliklerin ilgili uç noktaya teslim edilmesini durdurur.

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

### İmzalama gizli anahtarını döndürme

Bir webhook için imzalama gizli anahtarını değiştirin. Daha önce etkin olan sırların hemen mi yoksa 24 saatlik ek süre sonunda mı iptal edileceğini yapılandırabilirsiniz.

**ÖNEMLİ**: Yeni imzalama gizli anahtarı, döndürme sırasında **yalnızca bir kez** döndürülür. Doğrulama mantığınızı güncellemeden önce güvenli bir şekilde saklayın.

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

### Webhook isteklerini sunucuda işleme

Abone olduğunuz bir etkinlik gerçekleştiğinde webhook URL'niz bir HTTP POST isteği alır. Yeniden denemeyi önlemek için uç noktanız birkaç saniye içinde 2xx durum koduyla yanıt vermelidir. Teslimatı sağlamak için Gemini API, başarısız olan istekleri eksponansiyel geri yükleme kullanarak 24 saat boyunca otomatik olarak yeniden dener.

Gemini, güvenlik başlıkları için [Standart Web Kancaları](https://github.com/standard-webhooks/standard-webhooks) spesifikasyonuna sıkı sıkıya uyar. İmzalanmış başlık imzalarını ve depolanan statik imzalama gizli anahtarınızı kullanarak sunucunuzdaki yükü doğrulayın. Yük bilgileri için [Webhook zarfı](#webhook-envelope) bölümüne bakın.

HTTP dinleyicisi için Flask'i kullanan bir örneği aşağıda bulabilirsiniz:

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

## Dinamik webhook'lar

Dinamik webhook'lar, bir webhook uç noktasını **belirli bir istek yapılandırmasına** bağlamanıza olanak tanır. Bu özellik, aracı düzenleme kuyrukları için idealdir. Dinamik webhook'lar, simetrik gizli diziler yerine asimetrik ortak anahtar JWKS imzalarından yararlanır.

### Dinamik istek gönderme

Eşzamansız bir işi (ör. toplu iş oluşturma) tetiklerken `webhook_config` ekleyin.

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

### Dinamik imzaları (JWKS) doğrulama

Dinamik webhook istekleri, JSON Web Token (JWT) imzası yayar. Dinleyiciniz, imzayı ayıklamalı ve [Google'ın ortak sertifika uç noktalarını](https://www.googleapis.com/oauth2/v3/certs) kullanarak doğrulamalıdır.

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

## Webhook zarfı

Gemini webhook'ları, bant genişliği tıkanıklığını önlemek için veri iletmek üzere **ince yük** modeli kullanır. Teslimatlar, ham çıkış dosyasının kendisi yerine durum ayrıntılarını ve sonuçlara yönelik işaretçileri içeren bir anlık görüntü gönderir.

Aşağıda örnek bir yük biçimi verilmiştir:

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

## Etkinlik kataloğu referansı

Destekleyici işler için aşağıdaki etkinlikler tetiklenir:

| Etkinlik türü | Tetikleyici | Yük öğesi (`data`) |
| --- | --- | --- |
| `batch.succeeded` | İşlem başarıyla tamamlandı. | `id`, `output_file_uri` |
| `batch.cancelled` | Kullanıcı isteği iptal etti | `id` |
| `batch.expired` | Toplu işlem 24 saat içinde işlenmedi (tamamlanmadı) | `id` |
| `batch.failed` | Toplu iş başarısız oldu (sistem veya doğrulama hatası). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | İşlev çağrısı, kullanıcının bir işlem yapması gerekiyor | `id` |
| `interaction.completed` | Etkileşimler API'sindeki LRO başarılı oldu | `id` |
| `interaction.failed` | Etkileşimler API'sindeki LRO başarısız oldu (sistem veya doğrulama hatası). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | Etkileşimler API'sindeki LRO iptal edildi | `id` |
| `video.generated` | Video üretme LRO'su tamamlandı. | `id`, `output_file_uri`, `file_name` |

## En iyi uygulamalar

Güvenilir ve ölçeklenebilir bir işlem sağlamak için:

- **Sıkı yeniden oynatma koruması kontrolü**: Tüm istekler `webhook-timestamp`
  başlığı taşır. Yeniden oynatma saldırılarını azaltmak için **5 dakikadan** eski yükleri reddetmek üzere bu zaman damgasını her zaman sunucu yapılandırma katmanınızda doğrulayın.
- **İşlemi eşzamansız olarak yapın**: Geçerli imza algılandığında hemen `2xx OK` ile yanıt verin ve ayrıştırma işlemlerini dahili olarak sıraya alın. Dinleyicinin uzun süre beklemesi, teslimatın yeniden denenmesi döngüsünü tetikler.
- **Yinelenen öğeleri işleme**: Standart webhook'lar "en az bir kez" teslimat yapar. Daha yüksek trafik akışlarında olası yinelenenleri işlemek için tutarlı `webhook-id` üstbilgisini kullanın.

## Sırada ne var?

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=tr): Yüksek hacimli uç noktaları otomatikleştirmek için webhook'ları kullanın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
