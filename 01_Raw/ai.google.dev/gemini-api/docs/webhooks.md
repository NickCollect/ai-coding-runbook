---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-CN
fetched_at: 2026-11-02T07:05:50.038684+00:00
title: "Webhook \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Webhook

借助 Webhook，当异步操作或长时间运行的操作 (LRO) 完成时，Gemini API 可以向您的服务器推送实时通知。这样一来，就不再需要轮询 API 以获取状态更新，从而缩短延迟时间并减少开销。

Webhook 可用于[批量](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)作业、[互动](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn)和[视频生成](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)等操作。

## 运作方式

您可以配置 Gemini API Webhook，使其在事件触发后立即向您的监听器网址发送 HTTP POST 请求，而无需反复轮询 `GET /operations` 来检查作业是否已完成。

Gemini API 支持两种配置 Webhook 的方式：

- [**静态 Webhook**](#static-webhooks)：使用 Gemini [WebhookService API](https://ai.google.dev/api?hl=zh-cn) 配置的项目级端点。适用于全局集成（例如，通知 Slack、同步数据库等）。
- [**动态网络钩子**](#dynamic-webhooks)：请求级替换，在特定作业调用的配置载荷中传递网络钩子网址。非常适合将特定作业路由到专用端点。

## 静态 Webhook

静态 webhook 是针对整个[项目](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)注册的，并且会针对任何匹配的事件触发。

### 创建网络钩子

您可以使用 SDK 或 REST API 创建端点。

**重要提示**：创建 Webhook 时，API **仅返回一次签名密钥**。您必须安全地存储此密钥（例如，存储在环境变量中），以便日后验证签名。如果您丢失了签名密钥，则必须[轮换](#rotate-signing-secret)该密钥。

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

如需详细了解如何设置服务器以接收数据，请参阅[处理 Webhook 请求](#handle-webhook-requests)部分。

### 获取网络钩子

按资源名称检索特定 Webhook 的详细信息。

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

### 列出网络钩子

列出当前项目的所有已配置的 Webhook，并提供可选的分页功能。

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

### 更新 webhook

更新现有 Webhook 的属性，例如显示名称、目标 URI 或订阅的事件。

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

### 删除网络钩子

从项目中移除 webhook 端点。这会停止向相应端点传送未来的事件。

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

### 轮替签名密钥

轮替网络钩子的签名密钥。您可以配置是立即撤消之前有效的密钥，还是在 24 小时的宽限期后撤消。

**重要提示**：新的签名密钥仅在轮换时返回一次。在更新验证逻辑之前，请务必妥善保存该密钥。

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

### 在服务器上处理网络钩子请求

当发生您订阅的事件时，您的网络钩子网址会收到 HTTP POST 请求。您的端点必须在几秒钟内以 2xx 状态代码进行响应，以避免重试。为确保交付，Gemini API 会使用指数退避算法自动重试失败的请求，重试时间长达 24 小时。

Gemini 严格遵循[标准 Webhook](https://github.com/standard-webhooks/standard-webhooks) 规范来设置安全标头。使用签名标头签名和您存储的静态签名密钥，在服务器上验证载荷。如需了解载荷信息，请参阅 [Webhook 信封](#webhook-envelope)部分。

以下是使用 Flask 实现 HTTP 监听器的示例：

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

## 动态 webhook

借助动态 webhook，您可以将 webhook 端点绑定到**特定请求配置**，非常适合代理编排队列。动态 Webhook 利用非对称公钥 JWKS 签名（而非对称密钥）。

### 提交动态请求

在触发异步作业（例如创建批处理）时添加 `webhook_config`。

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

### 验证动态签名 (JWKS)

动态 Webhook 请求会发出 JSON Web 令牌 (JWT) 签名。您的监听器必须提取签名并使用 [Google 的公共证书端点](https://www.googleapis.com/oauth2/v3/certs)对其进行验证。

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

## 网络钩子信封

为避免带宽拥塞，Gemini webhook 使用**精简载荷**模型来传送数据。传送内容会发送包含状态详细信息和结果指针的快照，而不是原始输出文件本身。

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

## 活动目录参考

系统会针对支持的作业触发以下事件：

| 事件类型 | 触发器 | 载荷项 (`data`) |
| --- | --- | --- |
| `batch.succeeded` | 处理已成功完成。 | `id`、`output_file_uri` |
| `batch.cancelled` | 用户取消了请求 | `id` |
| `batch.expired` | 批次在 24 小时内未处理（完成） | `id` |
| `batch.failed` | 批量作业失败（系统或验证错误）。 | `id`、`error_code`、`error_message` |
| `interaction.requires_action` | 函数调用，用户需要执行某些操作 | `id` |
| `interaction.completed` | 互动 API 中的 LRO 成功 | `id` |
| `interaction.failed` | 互动 API 中的 LRO 失败（系统或验证错误）。 | `id`、`error_code`、`error_message` |
| `interaction.cancelled` | 取消了 interactions API 中的 LRO | `id` |
| `video.generated` | 视频生成 LRO 已完成。 | `id`、`output_file_uri`、`file_name` |

## 最佳做法

为确保运行可靠且可扩缩，请执行以下操作：

- **严格的重放保护检查**：所有请求都带有 `webhook-timestamp` 标头。始终在服务器配置层验证此时间戳，以拒绝超过 **5 分钟**的载荷（以缓解重放攻击）。
- **异步处理**：在检测到有效签名后立即使用 `2xx OK` 进行响应，并在内部将解析操作排入队列。如果监听器保持时间过长，则会触发传送重试周期。
- **重复数据处理**：标准 Webhook 提供“至少一次”的交付保证。使用一致的 `webhook-id` 标头来处理高拥塞流量中可能出现的重复项。

## 接下来怎么做？

- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)：利用 Webhook 自动执行高流量端点。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-24。"],[],[]]
