---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-CN
fetched_at: 2026-05-05T13:19:07.707441+00:00
title: "Webhook \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

- [首页](https://ai.google.dev/gemini-api/docs/首页)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文档](https://ai.google.dev/gemini-api/docs/文档)

发送反馈

# Webhook

借助网络钩子，Gemini API 可以在异步操作或长时间运行的操作 (LRO) 完成时，向您的服务器推送实时通知。这样就无需轮询 API 以获取状态更新，从而减少延迟和开销。

网络钩子适用于[批量](https://ai.google.dev/gemini-api/docs/批量)作业、
[互动](https://ai.google.dev/gemini-api/docs/互动)和[视频生成](https://ai.google.dev/gemini-api/docs/视频生成)等操作。

## 运作方式

您可以配置 Gemini API 网络钩子，使其在事件触发后立即向您的监听器网址发送 HTTP POST 请求，而无需重复轮询 `GET /operations` 以检查作业是否已完成。

Gemini API 支持两种配置网络钩子的方式：

- [**静态网络钩子**](https://ai.google.dev/gemini-api/docs/**静态网络钩子**)：使用 Gemini [WebhookService API](https://ai.google.dev/gemini-api/docs/WebhookService API) 配置的项目级端点。适用于全局集成（例如通知 Slack、同步数据库等）。
- [**动态网络钩子**](https://ai.google.dev/gemini-api/docs/**动态网络钩子**)：请求级替换，在特定作业调用的配置载荷中传递
  网络钩子网址。非常适合将特定作业路由到专用端点。

## 静态网络钩子

静态网络钩子是为整个 [项目](https://ai.google.dev/gemini-api/docs/项目) 注册的，并且会针对任何匹配的
事件触发。

### 创建网络钩子

您可以使用 SDK 或 REST API 创建端点。

**重要提示**：创建网络钩子时，API **只会返回一次签名密钥**
。您必须安全地存储此密钥（例如在环境变量中），以便稍后验证签名。如果您丢失了签名密钥，则必须
[轮替](https://ai.google.dev/gemini-api/docs/轮替)该密钥。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "MyBatchWebhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

如需详细了解如何设置服务器以接收数据，请参阅
[处理网络钩子请求](https://ai.google.dev/gemini-api/docs/处理网络钩子请求)部分。

### 获取网络钩子

按资源名称检索有关特定网络钩子的详细信息。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY"
```

### 列出网络钩子

列出当前项目的所有已配置网络钩子，并提供可选的分页功能。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY"
```

### 更新网络钩子

更新现有网络钩子的属性，例如显示名称、目标 URI 或订阅的事件。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "subscribed_events": ["batch.succeeded", "batch.failed", "batch.cancelled"]
  }'
```

### 删除网络钩子

从项目中移除网络钩子端点。这会停止向该端点传送未来的事件。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY"
```

### 轮替签名密钥

轮替网络钩子的签名密钥。您可以配置是立即撤消之前活跃的密钥，还是在 24 小时的宽限期后撤消。

**重要提示**：系统**只会**在轮替
时返回一次新的签名密钥。请先安全地存储该密钥，然后再更新验证逻辑。

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
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "revocation_behavior": "REVOKE_PREVIOUS_SECRETS_AFTER_H24"
  }'
```

### 在服务器上处理网络钩子请求

当您订阅的事件发生时，您的网络钩子网址将收到 HTTP POST 请求。您的端点必须在几秒钟内返回 2xx 状态代码，以避免重试。为确保传送，Gemini API 会使用指数退避算法自动重试失败的请求 24 小时。

Gemini 严格遵循安全标头的 [标准网络钩子](https://ai.google.dev/gemini-api/docs/标准网络钩子) 规范。使用签名标头签名和您存储的静态签名密钥在服务器上验证载荷。如需了解载荷信息，请参阅[网络钩子信封](https://ai.google.dev/gemini-api/docs/网络钩子信封)部分。

以下是使用 Flask 作为 HTTP 监听器的示例：

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

## 动态网络钩子

借助动态网络钩子，您可以将网络钩子端点绑定到**特定请求
配置**，非常适合代理编排队列。动态网络钩子利用非对称公钥 JWKS 签名，而不是对称密钥。

### 提交动态请求

触发异步作业（例如创建批处理）时，添加 `webhook_config`。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
  "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:batchCreate" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
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

### 验证动态签名 (JWKS)

动态网络钩子请求会发出 JSON Web 令牌 (JWT) 签名。您的监听器
必须提取签名并使用 [Google 的公共证书
端点](https://ai.google.dev/gemini-api/docs/Google 的公共证书端点)对其进行验证。

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

## 网络钩子信封

为避免带宽拥塞，Gemini 网络钩子使用**精简载荷** 模型来传送数据。传送会发送包含状态详细信息和结果指针的快照，而不是原始输出文件本身。

以下是载荷格式示例：

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

## 事件目录参考文档

系统会针对支持的作业触发以下事件：

| 事件类型 | 触发器 | 载荷项 (`data`) |
| --- | --- | --- |
| `batch.succeeded` | 处理成功完成。 | `id`、`output_file_uri` |
| `batch.cancelled` | 用户取消了请求 | `id` |
| `batch.expired` | 批处理在 24 小时内未处理（完成） | `id` |
| `batch.failed` | 批量作业失败（系统错误或验证错误）。 | `id`、`error_code`、`error_message` |
| `interaction.requires_action` | 函数调用，用户需要执行某些操作 | `id` |
| `interaction.completed` | 互动 API 中的 LRO 成功 | `id` |
| `interaction.failed` | 互动 API 中的 LRO 失败（系统错误或验证错误）。 | `id`、`error_code`、`error_message` |
| `interaction.cancelled` | 互动 API 中的 LRO 已取消 | `id` |
| `video.generated` | 视频生成 LRO 已完成。 | `id`、`output_file_uri`、`file_name` |

## 最佳做法

为确保可靠、可扩缩的操作，请执行以下操作：

- **严格的重放保护检查**：所有请求都带有 `webhook-timestamp`
  标头。请务必在服务器配置层验证此时间戳，以拒绝超过 **5 分钟** 的载荷（以缓解重放攻击）。
- **异步处理**：在检测到有效
  签名后立即返回 `2xx OK`，并在内部将解析操作排队。监听器保持时间过长会触发传送重试周期。
- **重复数据消除处理**：标准网络钩子至少传送一次。使用一致的 `webhook-id` 标头来处理较高拥塞流中可能存在的重复项。

## 接下来怎么做？

- [Batch API](https://ai.google.dev/gemini-api/docs/Batch API)：利用网络钩子自动执行大量端点。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://ai.google.dev/gemini-api/docs/知识共享署名 4.0 许可)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://ai.google.dev/gemini-api/docs/Apache 2.0 许可)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://ai.google.dev/gemini-api/docs/Google 开发者网站政策)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-05。

需要向我们提供更多信息？
