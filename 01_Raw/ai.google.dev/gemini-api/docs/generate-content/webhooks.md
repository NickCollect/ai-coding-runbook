---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/webhooks?hl=hi
fetched_at: 2026-07-06T05:12:02.824582+00:00
title: "\u0935\u0947\u092c\u0939\u0941\u0915 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# वेबहुक

वेबहुक की मदद से, Gemini API आपके सर्वर पर रीयल-टाइम में सूचनाएं भेज सकता है. ऐसा तब होता है, जब एसिंक्रोनस या लंबे समय तक चलने वाली कार्रवाइयां (एलआरओ) पूरी हो जाती हैं. इससे, स्टेटस अपडेट के लिए एपीआई को पोल करने की ज़रूरत नहीं पड़ती. साथ ही, इंतज़ार का समय और ओवरहेड कम हो जाता है.

वेबहुक, [बैच](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) जॉब, [इंटरैक्शन](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi), और [वीडियो जनरेट करने](https://ai.google.dev/gemini-api/docs/video?hl=hi) जैसे ऑपरेशनों के लिए उपलब्ध हैं.

## यह कैसे काम करता है

किसी टास्क के पूरा होने की स्थिति की जांच करने के लिए, `GET /operations` को बार-बार पोल करने के बजाय, Gemini API वेबहुक को कॉन्फ़िगर किया जा सकता है. इससे इवेंट ट्रिगर होने पर, आपके लिसनर यूआरएल पर तुरंत एचटीटीपी पोस्ट अनुरोध भेजा जा सकेगा.

Gemini API में, वेबहुक को कॉन्फ़िगर करने के दो तरीके उपलब्ध हैं:

- [**स्टैटिक वेबहुक**](#static-webhooks): प्रोजेक्ट-लेवल के एंडपॉइंट, जिन्हें Gemini [WebhookService API](https://ai.google.dev/api?hl=hi) की मदद से कॉन्फ़िगर किया जाता है. ग्लोबल इंटिग्रेशन के लिए अच्छा है. जैसे, Slack को सूचना देना, डेटाबेस को सिंक करना वगैरह.
- [**डाइनैमिक वेबहुक**](#dynamic-webhooks): अनुरोध के लेवल पर, किसी खास जॉब कॉल के कॉन्फ़िगरेशन पेलोड में वेबहुक यूआरएल पास करने वाले ओवरराइड. यह खास तौर पर, किसी खास काम को डेडीकेटेड एंडपॉइंट पर रूट करने के लिए सही है.

## स्टैटिक वेबहुक

स्टैटिक वेबहुक, पूरे [प्रोजेक्ट](https://ai.google.dev/gemini-api/docs/api-key?hl=hi#google-cloud-projects) के लिए रजिस्टर किए जाते हैं. साथ ही, ये किसी भी मैचिंग इवेंट के लिए ट्रिगर होते हैं.

### वेबबुक बनाना

एसडीके या REST API का इस्तेमाल करके एंडपॉइंट बनाए जा सकते हैं.

**अहम जानकारी**: वेबुक बनाते समय, एपीआई **साइनिंग सीक्रेट** को **सिर्फ़ एक बार** दिखाता है. आपको इसे सुरक्षित तरीके से सेव करना होगा.जैसे, अपने एनवायरमेंट वैरिएबल में. इससे बाद में हस्ताक्षर की पुष्टि की जा सकेगी. साइनिंग सीक्रेट खो जाने पर, आपको उसे [बदलना](#rotate-signing-secret) होगा.

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

डेटा पाने के लिए सर्वर सेट अप करने के बारे में जानने के लिए, [वेबहुक अनुरोधों को मैनेज करना](#handle-webhook-requests) सेक्शन देखें.

### वेबहुक पाना

किसी वेबुक की जानकारी को उसके संसाधन के नाम के हिसाब से फिर से पाएं.

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

### वेबहुक की सूची बनाना

मौजूदा प्रोजेक्ट के लिए कॉन्फ़िगर किए गए सभी वेबुक की सूची बनाएं. इसमें पेज नंबर डालने का विकल्प होता है.

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

### किसी वेबहुक को अपडेट करना

मौजूदा वेबुक की प्रॉपर्टी अपडेट करें. जैसे, डिसप्ले नेम, टारगेट यूआरआई या सदस्यता लिए गए इवेंट.

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

### वेबहुक मिटाना

प्रोजेक्ट से वेबहुक एंडपॉइंट हटाएं. इससे उस एंडपॉइंट पर, आने वाले समय में इवेंट की डिलीवरी बंद हो जाती है.

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

### साइनिंग सीक्रेट को रोटेट करना

किसी वेबहुक के लिए, साइनिंग सीक्रेट बदलना. आपके पास यह कॉन्फ़िगर करने का विकल्प होता है कि पहले से चालू सीक्रेट को तुरंत रद्द किया जाए या 24 घंटे के ग्रेस पीरियड के बाद.

**अहम जानकारी**: रोटेशन के समय, नया हस्ताक्षर करने का सीक्रेट **सिर्फ़ एक बार** दिखाया जाता है. पुष्टि करने के लॉजिक को अपडेट करने से पहले, इसे सुरक्षित तरीके से सेव करें.

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

### सर्वर पर वेबहुक अनुरोधों को मैनेज करना

जिस इवेंट के लिए आपने सदस्यता ली है उसके होने पर, आपके वेबुक यूआरएल को एचटीटीपी पोस्ट अनुरोध मिलेगा. रीट्राई से बचने के लिए, आपके एंडपॉइंट को कुछ ही सेकंड में 2xx स्टेटस कोड के साथ जवाब देना होगा. डिलीवरी पक्का करने के लिए, Gemini API
एक्सपोनेंशियल बैकऑफ़ का इस्तेमाल करके, 24 घंटे तक उन अनुरोधों को अपने-आप फिर से भेजता है जो पूरे नहीं हो सके.

Gemini, सुरक्षा हेडर के लिए [स्टैंडर्ड वेबहुक](https://github.com/standard-webhooks/standard-webhooks) स्पेसिफ़िकेशन का सख्ती से पालन करता है. हस्ताक्षर किए गए हेडर के सिग्नेचर और स्टोर किए गए स्टैटिक साइनिंग सीक्रेट का इस्तेमाल करके, अपने सर्वर पर पेलोड की पुष्टि करें. पेलोड की जानकारी के लिए, [वेबहुक एनवलप](#webhook-envelope) सेक्शन देखें.

यहां एचटीटीपी लिसनर के लिए, Flask का इस्तेमाल करने का एक उदाहरण दिया गया है:

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

## डाइनैमिक वेबहुक

डाइनैमिक वेबहुक की मदद से, वेबहुक एंडपॉइंट को **अनुरोध के किसी खास कॉन्फ़िगरेशन** से बाइंड किया जा सकता है. यह एजेंट-ऑर्केस्ट्रेशन कतारों के लिए सबसे सही है. डाइनैमिक वेबहुक, सिमेट्रिक सीक्रेट के बजाय असिमेट्रिक पब्लिक-की JWKS सिग्नेचर का इस्तेमाल करते हैं.

### डाइनैमिक अनुरोध सबमिट करना

एसिंक्रोनस जॉब (जैसे, बैच बनाना) को ट्रिगर करते समय, `webhook_config` जोड़ें.

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

### डाइनैमिक सिग्नेचर (JWKS) की पुष्टि करना

डाइनैमिक वेबहुक अनुरोध, JSON Web Token (JWT) सिग्नेचर जारी करते हैं. आपके लिसनर को हस्ताक्षर निकालना होगा और [Google के सार्वजनिक सर्टिफ़िकेट एंडपॉइंट](https://www.googleapis.com/oauth2/v3/certs) का इस्तेमाल करके इसकी पुष्टि करनी होगी.

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

## वेबबुक एन्वेलप

बैंडविड्थ की समस्या से बचने के लिए, Gemini के वेबहुक, डेटा डिलीवर करने के लिए **थिन पेलोड** मॉडल का इस्तेमाल करते हैं. डिलीवरी में, स्टेटस की जानकारी और नतीजों के पॉइंटर वाला स्नैपशॉट भेजा जाता है. इसमें रॉ आउटपुट फ़ाइल नहीं भेजी जाती.

यहां पेलोड फ़ॉर्मैट का एक उदाहरण दिया गया है:

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

## इवेंट कैटलॉग का रेफ़रंस

इन इवेंट को ट्रिगर किया जाता है, ताकि नौकरी ढूंढने में मदद मिल सके:

| इवेंट किस तरह का है | ट्रिगर | पेलोड आइटम (`data`) |
| --- | --- | --- |
| `batch.succeeded` | प्रोसेसिंग पूरी हो गई है. | `id`, `output_file_uri` |
| `batch.cancelled` | उपयोगकर्ता ने अनुरोध रद्द किया | `id` |
| `batch.expired` | बैच को 24 घंटे में प्रोसेस नहीं किया गया है (पूरा नहीं किया गया है) | `id` |
| `batch.failed` | बैच जॉब पूरा नहीं हो सका (सिस्टम या पुष्टि करने से जुड़ी गड़बड़ी). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | फ़ंक्शन कॉल, उपयोगकर्ता को कुछ करना होगा | `id` |
| `interaction.completed` | इंटरैक्शन एपीआई में एलआरओ पूरा हुआ | `id` |
| `interaction.failed` | इंटरैक्शन एपीआई में LRO फ़ेल हो गया (सिस्टम या पुष्टि करने से जुड़ी गड़बड़ी). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | Interactions API में LRO रद्द कर दिया गया | `id` |
| `video.generated` | वीडियो जनरेट करने की LRO प्रोसेस पूरी हो गई है. | `id`, `output_file_uri`, `file_name` |

## सबसे सही तरीके

यह पक्का करने के लिए कि यह सुविधा भरोसेमंद तरीके से और बड़े पैमाने पर काम करे:

- **रिप्ले सुरक्षा की सख्त जांच**: सभी अनुरोधों में `webhook-timestamp`
  हेडर होता है. हमेशा अपने सर्वर कॉन्फ़िगरेशन लेयर पर इस टाइमस्टैंप की पुष्टि करें, ताकि **पांच मिनट** से पुराने पेलोड को अस्वीकार किया जा सके. इससे रीप्ले अटैक को कम करने में मदद मिलती है.
- **एसिंक्रोनस तरीके से प्रोसेस करना**: मान्य हस्ताक्षर का पता चलने पर, तुरंत `2xx OK` के साथ जवाब दें. साथ ही, पार्स करने की कार्रवाइयों को इंटरनल तौर पर कतार में लगाएं. अगर श्रोता लंबे समय तक कॉल पर बने रहते हैं, तो डिलीवरी फिर से करने की कोशिश की जाएगी.
- **डुप्लीकेट कॉपी हटाने की सुविधा**: स्टैंडर्ड वेबहुक, "कम से कम एक बार" डिलीवर करते हैं. ज़्यादा भीड़भाड़ वाले फ़्लो में संभावित डुप्लीकेट को मैनेज करने के लिए, एक जैसे `webhook-id` हेडर का इस्तेमाल करें.

## आगे क्या करना है?

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=hi): ज़्यादा वॉल्यूम वाले एंडपॉइंट को अपने-आप प्रोसेस करने के लिए, वेबुक का इस्तेमाल करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया."],[],[]]
