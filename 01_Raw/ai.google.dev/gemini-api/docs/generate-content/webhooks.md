---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/webhooks?hl=ko
fetched_at: 2026-08-24T02:24:31.079541+00:00
title: "\uc6f9\ud6c5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 웹훅

웹훅을 사용하면 비동기식 또는 장기 실행 작업 (LRO)이 완료될 때 Gemini API가 서버에 실시간 알림을 푸시할 수 있습니다. 이렇게 하면 상태 업데이트를 위해 API를 폴링할 필요가 없어 지연 시간과 오버헤드가 줄어듭니다.

웹훅은 [일괄](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 작업,
[상호작용](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko) 및 [동영상 생성](https://ai.google.dev/gemini-api/docs/video?hl=ko)과 같은 작업에 사용할 수 있습니다.

## 작동 방식

작업이 완료되었는지 확인하기 위해 `GET /operations`를 반복적으로 폴링하는 대신 Gemini API 웹훅을 구성하여 이벤트 트리거 시 리스너 URL에 HTTP POST 요청을 즉시 전송할 수 있습니다.

Gemini API는 웹훅을 구성하는 두 가지 방법을 지원합니다.

- [**정적 웹훅**](#static-webhooks): Gemini [WebhookService API](https://ai.google.dev/api?hl=ko)로 구성된 프로젝트 수준 엔드포인트입니다. 전역 통합 (예: Slack에 알림, 데이터베이스 동기화 등)에 적합합니다.
- [**동적 웹훅**](#dynamic-webhooks): 특정 작업 호출의 구성 페이로드에서
  웹훅 URL을 전달하는 요청 수준 재정의입니다. 특정 작업을 전용 엔드포인트로 라우팅하는 데 적합합니다.

## 정적 웹훅

정적 웹훅은 전체 [프로젝트](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects)에 등록되며 일치하는
이벤트에 대해 트리거됩니다.

### 웹훅 만들기

SDK 또는 REST API를 사용하여 엔드포인트를 만들 수 있습니다.

**중요**: 웹훅을 만들 때 API는 **서명 보안 비밀**
**한 번만** 반환합니다. 나중에 서명을 확인하려면 이 보안 비밀을 안전하게 저장해야 합니다 (예: 환경 변수에 저장). 서명 보안 비밀을 분실하면
[순환](#rotate-signing-secret)해야 합니다.

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

데이터를 수신하도록 서버를 설정하는 방법에 관한 자세한 내용은
[웹훅 요청 처리](#handle-webhook-requests) 섹션을 참고하세요.

### 웹훅 가져오기

리소스 이름으로 특정 웹훅에 관한 세부정보를 가져옵니다.

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

### 웹훅 나열

현재 프로젝트에 대해 구성된 모든 웹훅을 나열합니다(선택적 페이지 나누기 포함).

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

### 웹훅 업데이트

표시 이름, 타겟 URI, 구독된 이벤트와 같은 기존 웹훅의 속성을 업데이트합니다.

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

### 웹훅 삭제

프로젝트에서 웹훅 엔드포인트를 삭제합니다. 이렇게 하면 향후 해당 엔드포인트로의 이벤트 전달이 중지됩니다.

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

### 서명 보안 비밀 순환

웹훅의 서명 보안 비밀을 순환합니다. 이전에 활성 상태였던 보안 비밀을 즉시 취소할지 아니면 24시간의 유예 기간 후에 취소할지 구성할 수 있습니다.

**중요**: 새 서명 보안 비밀은 순환
시 **한 번만** 반환됩니다. 확인 로직을 업데이트하기 전에 안전하게 저장하세요.

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

### 서버에서 웹훅 요청 처리

구독한 이벤트가 발생하면 웹훅 URL이 HTTP POST 요청을 수신합니다. 재시도를 방지하려면 엔드포인트가 몇 초 이내에 2xx 상태 코드로 응답해야 합니다. 전달을 보장하기 위해 Gemini API는 지수 백오프를 사용하여 실패한 요청을 24시간 동안 자동으로 재시도합니다.

Gemini는 보안 헤더에 관한 [표준 웹훅](https://github.com/standard-webhooks/standard-webhooks) 사양을
엄격하게 준수합니다. 서명된 헤더 서명과 저장된 정적 서명 보안 비밀을 사용하여 서버에서 페이로드를 확인합니다. 페이로드 정보는 [웹훅 봉투](#webhook-envelope) 섹션을 참고하세요.

다음은 HTTP 리스너에 Flask를 사용하는 예입니다.

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

## 동적 웹훅

동적 웹훅을 사용하면 웹훅 엔드포인트를 **특정 요청
구성**에 바인딩할 수 있습니다. 이는 에이전트 오케스트레이션 큐에 적합합니다. 동적 웹훅은 대칭 보안 비밀 대신 비대칭 공개 키 JWKS 서명을 활용합니다.

### 동적 요청 제출

비동기식 작업 (예: 일괄 작업 만들기)을 트리거할 때 `webhook_config`를 추가합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.6-flash:batchCreate" \
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

### 동적 서명 (JWKS) 확인

동적 웹훅 요청은 JSON 웹 토큰 (JWT) 서명을 내보냅니다. [리스너는 서명을 추출하고 Google의 공개 인증서 엔드포인트를 사용하여 서명을 확인해야 합니다.](https://www.googleapis.com/oauth2/v3/certs)

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

## 웹훅 봉투

대역폭 정체를 방지하기 위해 Gemini 웹훅은 **얇은 페이로드** 모델을 사용하여 데이터를 전달합니다. 전달은 원시 출력 파일 자체가 아닌 상태 세부정보와 결과 포인터가 포함된 스냅샷을 전송합니다.

다음은 페이로드 형식의 예입니다.

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

## 이벤트 카탈로그 참조

지원 작업에 대해 다음 이벤트가 트리거됩니다.

| 이벤트 유형 | 트리거 | 페이로드 항목 (`data`) |
| --- | --- | --- |
| `batch.succeeded` | 처리가 완료되었습니다. | `id`, `output_file_uri` |
| `batch.cancelled` | 사용자가 요청을 취소했습니다. | `id` |
| `batch.expired` | 일괄 작업이 24시간 이내에 처리 (완료)되지 않았습니다. | `id` |
| `batch.failed` | 일괄 작업이 실패했습니다 (시스템 또는 유효성 검사 오류). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | 함수 호출, 사용자가 작업을 해야 함 | `id` |
| `interaction.completed` | 상호작용 API의 LRO가 성공했습니다. | `id` |
| `interaction.failed` | 상호작용 API의 LRO가 실패했습니다 (시스템 또는 유효성 검사 오류). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | 상호작용 API의 LRO가 취소되었습니다. | `id` |
| `video.generated` | 동영상 생성 LRO가 완료되었습니다. | `id`, `output_file_uri`, `file_name` |

## 권장사항

신뢰할 수 있고 확장 가능한 운영을 보장하려면 다음 안내를 따르세요.

- **엄격한 재생 보호 확인**: 모든 요청에는 `webhook-timestamp`
  헤더가 포함됩니다. 재생 공격을 완화하기 위해 **5분** 보다 오래된 페이로드를 거부하도록 서버 구성 레이어에서 이 타임스탬프를 항상 확인하세요.
- **비동기식으로 처리**: 유효한
  서명이 감지되면 즉시 `2xx OK`로 응답하고 내부적으로 파싱 작업을 대기열에 추가합니다. 리스너 대기 시간이 길어지면 전달 재시도 주기가 트리거됩니다.
- **중복 삭제 처리**: 표준 웹훅은 "최소 한 번" 전달합니다. 일관된 `webhook-id` 헤더를 사용하여 혼잡도가 높은 흐름에서 발생할 수 있는 중복을 처리합니다.

## 다음 단계

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=ko): 웹훅을 활용하여 대용량 엔드포인트를 자동화합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
