---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=ja
fetched_at: 2026-06-01T06:03:22.854906+00:00
title: "Webhook \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Webhook

Webhook を使用すると、非同期オペレーションまたは長時間実行オペレーション（LRO）が完了したときに、Gemini API
からサーバーにリアルタイム通知をプッシュできます。これにより、API
にステータス更新をポーリングする必要がなくなり、レイテンシとオーバーヘッドが削減されます。

Webhook は、[バッチ](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)ジョブ、
[インタラクション](https://ai.google.dev/gemini-api/docs/interactions?hl=ja)、[動画生成](https://ai.google.dev/gemini-api/docs/video?hl=ja)などのオペレーションで使用できます。

## 仕組み

ジョブが完了したかどうかを確認するために `GET /operations` を繰り返しポーリングする代わりに、イベント トリガーが発生するとすぐに HTTP POST リクエストをリスナー URL に送信するように Gemini API Webhook を構成できます。

Gemini API では、Webhook を構成する次の 2 つの方法がサポートされています。

- [**静的 Webhook**](#static-webhooks): Gemini [WebhookService API](https://ai.google.dev/api?hl=ja) で構成されたプロジェクト レベルのエンドポイント。グローバル統合（Slack への通知、データベースの同期など）に適しています。
- [**動的 Webhook**](#dynamic-webhooks): 特定のジョブ呼び出しの構成ペイロードで
  Webhook URL を渡すリクエストレベルのオーバーライド。特定のジョブを専用のエンドポイントにルーティングする場合に最適です。

## 静的 Webhook

[静的 Webhook はプロジェクト全体に登録され、一致するイベントが発生するとトリガーされます。](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)

### Webhook を作成する

エンドポイントは、SDK または REST API を使用して作成できます。

**重要**: Webhook を作成すると、API は**署名シークレット**
**一度だけ**返します。後で署名を確認するために、この情報を安全に保存する必要があります（環境変数など）。署名シークレットを紛失した場合は、
[ローテーション](#rotate-signing-secret)する必要があります。

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

データを受信するようにサーバーを設定する方法については、
[Webhook リクエストを処理する](#handle-webhook-requests)をご覧ください。

### Webhook を取得する

リソース名で特定の Webhook の詳細を取得します。

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

### Webhook を一覧表示する

現在のプロジェクトで構成されているすべての Webhook を一覧表示します。ページ分割は省略可能です。

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

### Webhook を更新する

表示名、ターゲット URI、登録済みイベントなど、既存の Webhook のプロパティを更新します。

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

### Webhook を削除する

プロジェクトから Webhook エンドポイントを削除します。これにより、そのエンドポイントへの今後のイベント配信が停止します。

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

### 署名シークレットをローテーションする

Webhook の署名シークレットをローテーションします。以前に有効だったシークレットをすぐに取り消すか、24 時間の猶予期間後に取り消すかを構成できます。

**重要**: ローテーション時に新しい署名シークレットが**一度だけ**返されます。検証ロジックを更新する前に、安全に保存してください。

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

### サーバーで Webhook リクエストを処理する

登録しているイベントが発生すると、Webhook URL は HTTP POST リクエストを受信します。再試行を回避するには、エンドポイントが数秒以内に 2xx ステータス コードで応答する必要があります。配信を確実に行うため、Gemini API は指数バックオフを使用して、失敗したリクエストを 24 時間自動的に再試行します。

Gemini は、セキュリティ ヘッダーの
[標準 Webhook](https://github.com/standard-webhooks/standard-webhooks) 仕様に厳密に準拠しています。署名付きヘッダーの署名と保存されている静的署名シークレットを使用して、サーバー上のペイロードを確認します。ペイロード情報については、[Webhook エンベロープ](#webhook-envelope)をご覧ください。

HTTP リスナーに Flask を使用する例を次に示します。

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

## 動的 Webhook

動的 Webhook を使用すると、Webhook エンドポイントを **特定のリクエスト
構成**にバインドできます。これは、エージェント オーケストレーション キューに最適です。動的 Webhook は、対称シークレットではなく、非対称公開鍵
JWKS 署名を利用します。

### 動的リクエストを送信する

非同期ジョブ（バッチの作成など）をトリガーするときに `webhook_config` を追加します。

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

### 動的署名（JWKS）を確認する

動的 Webhook リクエストは、JSON ウェブトークン（JWT）署名を発行します。リスナーは署名を抽出し、[Google の公開証明書エンドポイントを使用して検証する必要があります。](https://www.googleapis.com/oauth2/v3/certs)

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

## Webhook エンベロープ

帯域幅の輻輳を回避するため、Gemini Webhook は**シン ペイロード** モデルを使用してデータを配信します。配信では、元の出力ファイルではなく、ステータスの詳細と結果へのポインタを含むスナップショットが送信されます。

ペイロード形式の例を次に示します。

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

## イベント カタログのリファレンス

サポートされているジョブでは、次のイベントがトリガーされます。

| イベントの種類 | トリガー | ペイロード アイテム（`data`） |
| --- | --- | --- |
| `batch.succeeded` | 処理が正常に完了しました。 | `id`、`output_file_uri` |
| `batch.cancelled` | ユーザーがリクエストをキャンセルしました | `id` |
| `batch.expired` | バッチが 24 時間以内に処理（完了）されませんでした | `id` |
| `batch.failed` | バッチジョブが失敗しました（システム エラーまたは検証エラー）。 | `id`、`error_code`、`error_message` |
| `interaction.requires_action` | 関数呼び出し。ユーザーが操作する必要があります | `id` |
| `interaction.completed` | インタラクション API の LRO が成功しました | `id` |
| `interaction.failed` | インタラクション API の LRO が失敗しました（システム エラーまたは検証エラー）。 | `id`、`error_code`、`error_message` |
| `interaction.cancelled` | インタラクション API の LRO がキャンセルされました | `id` |
| `video.generated` | 動画生成 LRO が完了しました。 | `id`、`output_file_uri`、`file_name` |

## ベスト プラクティス

信頼性が高くスケーラブルなオペレーションを確保するには:

- **厳格なリプレイ保護チェック**: すべてのリクエストに `webhook-timestamp`
  ヘッダーが含まれます。サーバー構成レイヤでこのタイムスタンプを常に検証し、**5 分** より古いペイロードを拒否します（リプレイ攻撃を軽減するため）。
- **非同期で処理する**: 有効な
  署名が検出されたらすぐに `2xx OK` で応答し、解析オペレーションを内部でキューに登録します。リスナーの保持時間が長すぎると、配信の再試行サイクルがトリガーされます。
- **重複排除処理**: 標準の Webhook は「少なくとも 1 回」配信します。一貫した `webhook-id` ヘッダーを使用して、輻輳の多いフローで発生する可能性のある重複を処理します。

## 次のステップ

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=ja): Webhook を使用して、大量のエンドポイントを自動化します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-19 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-19 UTC。"],[],[]]
