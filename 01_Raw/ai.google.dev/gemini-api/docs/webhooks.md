---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=vi
fetched_at: 2026-05-05T20:44:30.227434+00:00
title: "Webhook \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Webhook

Webhook cho phép Gemini API gửi thông báo theo thời gian thực đến máy chủ của bạn khi các Thao tác không đồng bộ hoặc Thao tác kéo dài (LRO) hoàn tất. Điều này giúp bạn không cần phải thăm dò API để biết thông tin cập nhật về trạng thái, giảm độ trễ và mức hao tổn.

Webhook có sẵn cho các thao tác như [Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) jobs (Công việc hàng loạt), [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=vi) (Tương tác) và [video generation](https://ai.google.dev/gemini-api/docs/video?hl=vi) (tạo video).

## Cách hoạt động

Thay vì liên tục thăm dò `GET /operations` để kiểm tra xem một công việc đã hoàn tất hay chưa, bạn có thể định cấu hình webhook của Gemini API để gửi yêu cầu POST qua HTTP đến URL của trình nghe ngay khi có sự kiện kích hoạt.

Gemini API hỗ trợ 2 cách định cấu hình webhook:

- [**Webhook tĩnh**](#static-webhooks): Các điểm cuối ở cấp dự án được định cấu hình bằng [Gemini WebhookService API](https://ai.google.dev/api?hl=vi). Phù hợp với các hoạt động tích hợp trên toàn cầu (ví dụ: thông báo cho Slack, đồng bộ hoá cơ sở dữ liệu, v.v.).
- [**Webhook động**](#dynamic-webhooks): Các chế độ ghi đè ở cấp yêu cầu sẽ truyền URL webhook trong tải trọng cấu hình của một lệnh gọi công việc cụ thể. Lý tưởng cho việc định tuyến các công việc cụ thể đến các điểm cuối chuyên dụng.

## Webhook tĩnh

Webhook tĩnh được đăng ký cho toàn bộ [dự án](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) và kích hoạt cho mọi sự kiện trùng khớp.

### Tạo một webhook

Bạn có thể tạo điểm cuối bằng SDK hoặc API REST.

**QUAN TRỌNG**: Khi tạo một webhook, API chỉ trả về **khoá bí mật ký**
**một lần**. Bạn phải lưu trữ khoá này một cách an toàn (ví dụ: trong các biến môi trường) để xác minh chữ ký sau này. Nếu mất khoá bí mật để ký, bạn sẽ phải [xoay vòng](#rotate-signing-secret) khoá đó.

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

Để biết thông tin chi tiết về cách thiết lập máy chủ để nhận dữ liệu, hãy xem phần [Xử lý yêu cầu webhook](#handle-webhook-requests).

### Nhận webhook

Truy xuất thông tin chi tiết về một webhook cụ thể theo tên tài nguyên.

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

### Liệt kê webhook

Liệt kê tất cả webhook đã định cấu hình cho dự án hiện tại, có thể phân trang.

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

### Cập nhật webhook

Cập nhật các thuộc tính của webhook hiện có, chẳng hạn như tên hiển thị, URI mục tiêu hoặc các sự kiện đã đăng ký.

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

### Xoá webhook

Xoá một điểm cuối webhook khỏi dự án. Thao tác này sẽ dừng việc gửi các sự kiện trong tương lai đến điểm cuối đó.

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

### Xoay vòng khoá bí mật ký

Xoay vòng khoá bí mật ký cho webhook. Bạn có thể định cấu hình xem các bí mật đã hoạt động trước đó có bị thu hồi ngay lập tức hay sau thời gian gia hạn 24 giờ.

**QUAN TRỌNG**: Khoá bí mật ký mới chỉ được trả về **một lần** tại thời điểm xoay vòng. Hãy lưu trữ khoá này một cách an toàn trước khi cập nhật logic xác minh.

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

### Xử lý các yêu cầu webhook trên máy chủ

Khi một sự kiện mà bạn đã đăng ký xảy ra, URL webhook của bạn sẽ nhận được một yêu cầu POST trong HTTP. Điểm cuối của bạn phải phản hồi bằng mã trạng thái 2xx trong vòng vài giây để tránh thử lại. Để đảm bảo việc phân phối, Gemini API sẽ tự động thử lại các yêu cầu không thành công trong 24 giờ bằng cách sử dụng thuật toán thời gian đợi luỹ thừa.

Gemini tuân thủ nghiêm ngặt quy cách [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) (Webhook tiêu chuẩn) đối với tiêu đề bảo mật. Xác minh tải trọng trên máy chủ bằng cách sử dụng chữ ký tiêu đề đã ký và khoá bí mật ký tĩnh đã lưu trữ. Hãy xem phần [Gói webhook](#webhook-envelope) để biết thông tin về tải trọng.

Sau đây là ví dụ về cách sử dụng Flask cho trình nghe HTTP:

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

## Webhook động

Webhook động cho phép bạn liên kết một điểm cuối webhook với một **cấu hình yêu cầu cụ thể**, phù hợp với các hàng đợi điều phối tác nhân. Webhook động tận dụng chữ ký JWKS khoá công khai bất đối xứng thay vì các bí mật đối xứng.

### Gửi yêu cầu linh hoạt

Thêm một `webhook_config` khi kích hoạt một công việc không đồng bộ (ví dụ: tạo một Batch).

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

### Xác minh chữ ký động (JWKS)

Các yêu cầu webhook động phát ra chữ ký Mã thông báo web JSON (JWT). Trình nghe của bạn phải trích xuất chữ ký và xác minh chữ ký đó bằng cách sử dụng [các điểm cuối chứng chỉ công khai của Google](https://www.googleapis.com/oauth2/v3/certs).

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

## Phong bì webhook

Để tránh tình trạng tắc nghẽn băng thông, webhook Gemini sử dụng mô hình **tải trọng mỏng** để phân phối dữ liệu. Các lượt phân phối sẽ gửi một ảnh chụp nhanh chứa thông tin chi tiết về trạng thái và con trỏ đến kết quả, thay vì chính tệp đầu ra thô.

Sau đây là ví dụ về định dạng tải trọng:

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

## Tài liệu tham khảo về danh mục sự kiện

Các sự kiện sau đây được kích hoạt cho các công việc hỗ trợ:

| Loại sự kiện | Trigger | Mục tải trọng (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Đã xử lý xong. | `id`, `output_file_uri` |
| `batch.cancelled` | Người dùng đã huỷ yêu cầu | `id` |
| `batch.expired` | Lô chưa được xử lý (hoàn tất) trong khung thời gian 24 giờ | `id` |
| `batch.failed` | Thao tác hàng loạt không thành công (lỗi hệ thống hoặc lỗi xác thực). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Lệnh gọi hàm, người dùng cần làm gì đó | `id` |
| `interaction.completed` | LRO trong API tương tác đã thành công | `id` |
| `interaction.failed` | LRO trong API tương tác không thành công (lỗi hệ thống hoặc lỗi xác thực). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO trong API tương tác bị huỷ | `id` |
| `video.generated` | Đã hoàn tất LRO tạo video. | `id`, `output_file_uri`, `file_name` |

## Các phương pháp hay nhất

Để đảm bảo hoạt động đáng tin cậy và có khả năng mở rộng:

- **Kiểm tra nghiêm ngặt khả năng bảo vệ chống phát lại**: Tất cả các yêu cầu đều có một tiêu đề `webhook-timestamp`. Luôn xác thực dấu thời gian này trên lớp cấu hình máy chủ để từ chối các tải trọng cũ hơn **5 phút** (để giảm thiểu các cuộc tấn công phát lại).
- **Xử lý không đồng bộ**: Phản hồi bằng `2xx OK` ngay khi phát hiện chữ ký hợp lệ và xếp hàng các thao tác phân tích cú pháp nội bộ. Thời gian giữ máy của người nghe quá lâu sẽ kích hoạt một chu kỳ thử lại việc gửi.
- **Xử lý việc loại bỏ dữ liệu trùng lặp**: Webhook tiêu chuẩn sẽ gửi "Ít nhất một lần". Sử dụng tiêu đề `webhook-id` nhất quán để xử lý các bản sao tiềm ẩn trong các luồng tắc nghẽn cao hơn.

## Tiếp theo là gì?

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=vi): Sử dụng webhook để tự động hoá các điểm cuối có số lượng lớn.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-05 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-05 UTC."],[],[]]
