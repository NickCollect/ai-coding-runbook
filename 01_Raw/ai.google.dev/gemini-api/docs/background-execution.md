---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=vi
fetched_at: 2026-09-14T05:39:05.201826+00:00
title: "Ch\u1ea1y \u1edf ch\u1ebf \u0111\u1ed9 n\u1ec1n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Chạy ở chế độ nền

Đối với các tác vụ kéo dài như nghiên cứu chuyên sâu, lập luận phức tạp hoặc thực thi tác nhân nhiều bước, thời gian chờ kết nối có thể làm gián đoạn các yêu cầu HTTP tiêu chuẩn (thường đóng sau 60 giây). [API Tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) cung cấp **hoạt động thực thi trong nền** để chạy các tác vụ này một cách không đồng bộ.

Để cho phép hoạt động tương tác chạy cho đến khi hoàn tất tác vụ trên máy chủ, hãy đặt `"background": true` khi tạo hoạt động tương tác. API này sẽ trả về ngay lập tức một mã nhận dạng tương tác mà các ứng dụng khách có thể dùng để thăm dò trạng thái, tiến trình truyền phát hoặc kết nối lại với một luồng bị ngắt kết nối.

Chế độ thực thi trong nền được hỗ trợ cho các mô hình Gemini tiêu chuẩn (chẳng hạn như `gemini-3.6-flash` và `gemini-3.1-pro-preview`) và Tác nhân được quản lý (chẳng hạn như `antigravity-preview-05-2026`).

## Tạo một hoạt động tương tác ở chế độ nền

Để bắt đầu một hoạt động tương tác ở chế độ nền, hãy đặt tham số `background` thành `true` khi tạo tài nguyên.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Cách hoạt động của tính năng thực thi ở chế độ nền

Khi bạn tạo một hoạt động tương tác ở chế độ nền, tác vụ sẽ chạy không đồng bộ trên máy chủ. Tương tác sẽ chuyển đổi qua nhiều trạng thái thực thi:

- `in_progress`: Máy chủ đang tích cực thực hiện hoạt động tương tác (chẳng hạn như chạy mã hoặc nghiên cứu).
- `requires_action`: Hoạt động tương tác đã tạm dừng và đang chờ thông tin đầu vào của ứng dụng (chẳng hạn như xác nhận việc thực thi một công cụ hoặc trả lời một câu hỏi).
- `completed`: Tương tác hoàn tất thành công và có sẵn đầu ra.
- `failed`: Đã xảy ra lỗi trong quá trình thực thi (chẳng hạn như lỗi công cụ hoặc giới hạn về tốc độ).
- `cancelled`: Yêu cầu của ứng dụng khách đã dừng quá trình thực thi.

### Trường hợp sử dụng

Sử dụng chế độ thực thi trong nền cho:

- **Hoạt động của trợ lý ảo:** Các tác vụ yêu cầu thực thi mã, duyệt web hoặc điều phối trợ lý ảo phụ (chẳng hạn như `antigravity-preview-05-2026`).
- **Deep Research:** Chạy bằng `deep-research-preview-04-2026` hoặc `deep-research-max-preview-04-2026` và mất vài phút.
- **Lý luận dài:** Những tác vụ mà các bước suy nghĩ của mô hình vượt quá giới hạn kết nối HTTP tiêu chuẩn.

## Truy xuất kết quả

Nhận kết quả tương tác trong nền bằng cách sử dụng **polling** hoặc **streaming**.

### Mẫu thăm dò (không chặn)

Cơ chế thăm dò định kỳ kiểm tra trạng thái tương tác bằng cách sử dụng các yêu cầu GET không chặn cho đến khi đạt đến trạng thái kết thúc.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Mẫu truyền trực tuyến

Nếu mạng bị gián đoạn và ngắt kết nối một luồng, thì quá trình phát trực tuyến có thể tiếp tục từ sự kiện đã nhận gần đây nhất. Mỗi delta chứa một `event_id` duy nhất trong tải trọng của nó. Việc truyền mã nhận dạng này dưới dạng `last_event_id` sẽ tiếp tục phát trực tuyến từ sự kiện đó.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Cuộc trò chuyện nhiều lượt

Các lượt tương tác tiếp theo có thể liên kết với một cuộc trò chuyện ở chế độ nền bằng cách sử dụng `previous_interaction_id`, tuỳ thuộc vào những ràng buộc sau:

1. **Các lệnh thực thi đang hoạt động bị chặn:** Việc liên kết một lượt tương tác tiếp theo với một lượt tương tác có trạng thái `in_progress` sẽ trả về lỗi `400 Bad Request`. Chờ cho thao tác tương tác đạt đến trạng thái `completed` trước khi bắt đầu thao tác tiếp theo.
2. **Tham số môi trường cho Tác nhân được quản lý:** Khi liên kết các lượt tương tác cho Tác nhân được quản lý (chẳng hạn như `antigravity-preview-05-2026`), các yêu cầu phải bao gồm cả `previous_interaction_id` và `environment`.

Các ví dụ sau đây minh hoạ cách liên kết các hoạt động tương tác:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Huỷ và xoá

Kiểm soát các hoạt động đang chạy và quản lý bộ nhớ bằng cách sử dụng các yêu cầu huỷ và xoá:

- **Huỷ (`POST /interactions/{id}/cancel`):** Dừng việc cần làm đang chạy. Trạng thái chuyển thành `cancelled`. Các thao tác dọn dẹp trên máy chủ có thể gây ra một chút chậm trễ trước khi các bản cập nhật trạng thái trong yêu cầu GET xuất hiện.
- **Xoá (`DELETE /interactions/{id}`):** Xoá các bản ghi tương tác khỏi máy chủ. Các yêu cầu GET tiếp theo sẽ trả về lỗi `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Các bước tiếp theo

- Đọc [Thông tin tổng quan về Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) để hiểu rõ về việc quản lý phiên và trạng thái.
- Hãy xem hướng dẫn về [Tương tác trong quá trình phát trực tiếp](https://ai.google.dev/gemini-api/docs/streaming?hl=vi) để biết thông tin chi tiết về thông tin cập nhật sự kiện theo thời gian thực.
- Khám phá [Hướng dẫn nhanh về tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi) để tạo tác nhân có trạng thái nhiều lượt tương tác.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-12 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-12 UTC."],[],[]]
