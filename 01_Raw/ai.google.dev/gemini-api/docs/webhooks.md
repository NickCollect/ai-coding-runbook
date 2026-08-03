---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=ar
fetched_at: 2026-08-03T04:34:26.638362+00:00
title: "\u0627\u0644\u0631\u062f\u0651 \u0627\u0644\u062a\u0644\u0642\u0627\u0626\u064a \u0639\u0644\u0649 \u0627\u0644\u0648\u064a\u0628 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الردّ التلقائي على الويب

تتيح الويب هوك لواجهة Gemini API إرسال إشعارات في الوقت الفعلي إلى الخادم عند اكتمال العمليات غير المتزامنة أو العمليات الطويلة الأمد. يحلّ ذلك محل الحاجة إلى طلب البيانات من واجهة برمجة التطبيقات بشكل متكرر للحصول على آخر المعلومات، ما يقلّل من وقت الاستجابة والحِمل الزائد.

تتوفّر خطافات الويب لعمليات مثل مهام [المعالجة المجمّعة](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) و[التفاعلات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) و[إنشاء الفيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar).

## آلية العمل

بدلاً من إجراء استطلاع متكرّر `GET /operations` لمعرفة ما إذا كانت مهمة قد اكتملت،
يمكنك ضبط Webhooks في Gemini API لإرسال طلب HTTP POST إلى
عنوان URL الخاص بالبرنامج المستمع فور تشغيل حدث.

تتيح Gemini API طريقتَين لإعداد خطافات الويب:

- [**عمليات ربط ثابتة**](#static-webhooks): نقاط نهاية على مستوى المشروع تم إعدادها باستخدام [WebhookService API](https://ai.google.dev/api?hl=ar) في Gemini. مناسبة لعمليات الدمج العالمية (مثل إرسال إشعارات إلى Slack ومزامنة قاعدة بيانات وما إلى ذلك).
- [**روابط الويب هوك الديناميكية**](#dynamic-webhooks): عمليات إلغاء على مستوى الطلب يتم فيها تمرير عنوان URL لويب هوك في حمولة الإعدادات لطلب وظائف معيّن. وهي مثالية لتوجيه مهام معيّنة إلى نقاط نهاية مخصّصة.

## الويب هوك الثابتة

يتم تسجيل خطافات الويب الثابتة [لمشروع](https://ai.google.dev/gemini-api/docs/api-key?hl=ar#google-cloud-projects) بأكمله ويتم تشغيلها لأي حدث مطابق.

### إنشاء ويب هوك

يمكنك إنشاء نقاط نهاية باستخدام حزمة تطوير البرامج أو واجهة REST API.

**ملاحظة مهمة**: عند إنشاء خطاف ويب، تعرض واجهة برمجة التطبيقات **مفتاح توقيع**
**مرة واحدة فقط**. يجب تخزين هذا المفتاح بشكل آمن (مثلاً في متغيّرات البيئة) للتحقّق من التواقيع لاحقًا. في حال فقدان سر التوقيع، عليك [تغييره](#rotate-signing-secret).

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

للحصول على تفاصيل حول إعداد الخادم لتلقّي البيانات، يُرجى الاطّلاع على قسم [التعامل مع طلبات Webhook](#handle-webhook-requests).

### الحصول على ويب هوك

استرداد تفاصيل حول خطاف ويب معيّن من خلال اسم المورد الخاص به

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

### عرض قائمة بالويب هوك

تعرض هذه الطريقة جميع خطافات الويب التي تم ضبط إعداداتها للمشروع الحالي، مع إمكانية تقسيم النتائج إلى صفحات.

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

### تعديل ويب هوك

تعديل خصائص خطاف ويب حالي، مثل الاسم المعروض أو معرّف الموارد الموحّد المستهدف أو الأحداث التي تم الاشتراك فيها

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

### حذف ويب هوك

إزالة نقطة نهاية لـ Webhook من المشروع سيؤدي ذلك إلى إيقاف عمليات تسليم الأحداث المستقبلية إلى نقطة النهاية هذه.

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

### تغيير سر توقيع

تغيير واجهة برمجة التطبيقات السرّية للتوقيع الخاصة بخطاف ويب يمكنك ضبط ما إذا كان سيتم إبطال الرموز السرية النشطة سابقًا على الفور أو بعد فترة سماح مدتها 24 ساعة.

**ملاحظة مهمة**: يتم عرض سر التوقيع الجديد **مرة واحدة فقط** عند تدويره. يجب تخزينها بشكل آمن قبل تعديل منطق إثبات الملكية.

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

### التعامل مع طلبات الويب هوك على خادم

عند وقوع حدث اشتركت فيه، سيتلقّى رابط ويب هوك طلب HTTP POST. يجب أن يستجيب نقطة النهاية برمز حالة 2xx في غضون بضع ثوانٍ لتجنُّب إعادة المحاولة. لضمان تسليم الردود، تعيد Gemini API تلقائيًا معالجة الطلبات التي فشلت لمدة 24 ساعة باستخدام التراجع الدليلي.

يتّبع Gemini مواصفات [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) بدقة في ما يتعلق بعناوين الأمان. تحقَّق من الحمولة على الخادم باستخدام توقيعات العنوان الموقَّع وسر التوقيع الثابت المحفوظ. راجِع قسم [حزمة Webhook](#webhook-envelope) للحصول على معلومات الحمولة.

في ما يلي مثال على استخدام Flask لمستمع HTTP:

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

## خطافات الويب الديناميكية

تتيح لك خطافات الويب الديناميكية ربط نقطة نهاية خطاف الويب **بإعداد طلب معيّن**، ما يجعلها مثالية لقوائم انتظار تنسيق الوكلاء. تستفيد خطافات الويب الديناميكية من توقيعات JWKS غير المتماثلة بالمفتاح العام بدلاً من الأسرار المتماثلة.

### إرسال طلب ديناميكي

أضِف `webhook_config` عند تشغيل مهمة غير متزامنة (مثل إنشاء Batch).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3.6-flash',
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
    model: "gemini-3.6-flash",
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### التحقّق من صحة التواقيع الديناميكية (JWKS)

تُصدر طلبات Webhook الديناميكية توقيع JSON Web Token (JWT). على المستمع استخراج التوقيع والتحقّق منه باستخدام [نقاط نهاية شهادة Google العامة](https://www.googleapis.com/oauth2/v3/certs).

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

## حزمة ويب هوك

لتجنُّب الازدحام في نطاق ترددي، تستخدم خطافات الويب في Gemini نموذج **حمولة رقيقة** لتقديم البيانات. وترسل عمليات التسليم لقطة تحتوي على تفاصيل الحالة ومؤشرات إلى النتائج، بدلاً من ملف الإخراج الأولي نفسه.

في ما يلي مثال على تنسيق الحمولة:

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

## مرجع كتالوج الأحداث

يتم تشغيل الأحداث التالية للوظائف المتوافقة:

| نوع الحدث | Trigger | عنصر الحمولة (`data`) |
| --- | --- | --- |
| `batch.succeeded` | اكتملت المعالجة بنجاح. | ‫`id`، `output_file_uri` |
| `batch.cancelled` | ألغى المستخدم الطلب | `id` |
| `batch.expired` | لم تتم معالجة الدفعة (انتهت) خلال فترة 24 ساعة | `id` |
| `batch.failed` | تعذّر تنفيذ مهمة الدفعات (خطأ في النظام أو خطأ في التحقّق). | ‫`id`، `error_code`، `error_message` |
| `interaction.requires_action` | طلب تنفيذ دالة، يجب أن يتّخذ المستخدم إجراءً | `id` |
| `interaction.completed` | نجاح عملية LRO في واجهة برمجة التطبيقات الخاصة بالتفاعلات | `id` |
| `interaction.failed` | تعذّر تنفيذ عملية LRO في واجهة برمجة التطبيقات الخاصة بالتفاعلات (حدث خطأ في النظام أو التحقّق من الصحة). | ‫`id`، `error_code`، `error_message` |
| `interaction.cancelled` | تم إلغاء LRO في واجهة برمجة التطبيقات الخاصة بالتفاعلات | `id` |
| `video.generated` | اكتملت عملية إنشاء الفيديو الطويلة الأمد. | ‫`id`، `output_file_uri`، `file_name` |

## أفضل الممارسات

لضمان التشغيل الموثوق والقابل للتوسّع، اتّبِع ما يلي:

- **التحقّق من الحماية الصارمة من إعادة التشغيل**: تتضمّن جميع الطلبات عنوان `webhook-timestamp`. يجب دائمًا التحقّق من صحة هذا الطابع الزمني في طبقة إعدادات الخادم لرفض الحِزم التي مرّ عليها أكثر من **5 دقائق** (للحدّ من هجمات إعادة الإرسال).
- **المعالجة بشكل غير متزامن**: الردّ باستخدام `2xx OK` فور رصد توقيع صالح، ووضع عمليات التحليل في قائمة الانتظار داخليًا. سيؤدي طول مدة انتظار المستمع إلى بدء دورة إعادة محاولة التسليم.
- **التعامل مع إزالة التكرار**: تقدّم خطافات الويب العادية خدمة "مرة واحدة على الأقل". استخدِم العنوان `webhook-id` المتسق للتعامل مع النسخ المكرّرة المحتملة في تدفقات الازدحام الأعلى.

## ما هي الخطوات التالية؟

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=ar): استخدِم خطافات الويب لأتمتة نقاط النهاية ذات الحجم الكبير.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
