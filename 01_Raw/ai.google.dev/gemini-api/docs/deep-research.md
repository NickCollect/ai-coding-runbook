---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=vi
fetched_at: 2026-05-05T19:50:58.957639+00:00
title: "T\u00e1c nh\u00e2n Deep Research c\u1ee7a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân Deep Research của Gemini

Tác nhân Deep Research của Gemini tự động lập kế hoạch, thực hiện và tổng hợp các nhiệm vụ nghiên cứu nhiều bước. Được hỗ trợ bởi Gemini, công cụ này điều hướng các mảng thông tin phức tạp để tạo ra các báo cáo chi tiết có trích dẫn. Các chức năng mới cho phép bạn lập kế hoạch cộng tác với tác nhân, kết nối với các công cụ bên ngoài bằng máy chủ MCP, bao gồm cả hình ảnh trực quan (chẳng hạn như biểu đồ và đồ thị) và cung cấp trực tiếp tài liệu làm dữ liệu đầu vào.

Các tác vụ nghiên cứu bao gồm tìm kiếm và đọc lặp đi lặp lại và có thể mất vài phút để hoàn thành. Bạn phải sử dụng tính năng thực thi ở chế độ nền (đặt `background=true`) để chạy tác nhân một cách không đồng bộ và thăm dò kết quả hoặc truyền trực tuyến thông tin cập nhật. Hãy xem phần [Xử lý các tác vụ chạy trong thời gian dài](#long-running-tasks) để biết thêm thông tin chi tiết.

Ví dụ sau đây cho thấy cách bắt đầu một tác vụ nghiên cứu ở chế độ nền và thăm dò kết quả.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Các phiên bản được hỗ trợ

Nhân viên hỗ trợ Deep Research có 2 phiên bản:

- **Deep Research** (`deep-research-preview-04-2026`): Được thiết kế để đạt tốc độ và hiệu quả cao, lý tưởng để truyền trực tiếp về giao diện người dùng của một ứng dụng.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Mức độ toàn diện tối đa để tự động thu thập và tổng hợp bối cảnh.

## Lập kế hoạch cộng tác

Lập kế hoạch cộng tác giúp bạn kiểm soát hướng nghiên cứu trước khi tác nhân bắt đầu công việc. Khi được bật, tác nhân sẽ trả về một kế hoạch nghiên cứu đề xuất thay vì thực thi ngay lập tức. Sau đó, bạn có thể xem xét, sửa đổi hoặc phê duyệt kế hoạch thông qua các lượt tương tác nhiều lượt.

### Bước 1: Yêu cầu tạo kế hoạch

Đặt `collaborative_planning=True` trong lượt tương tác đầu tiên. Thay vì trả về một báo cáo đầy đủ, tác nhân sẽ trả về một kế hoạch nghiên cứu.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Bước 2: Tinh chỉnh kế hoạch (không bắt buộc)

Sử dụng `previous_interaction_id` để tiếp tục cuộc trò chuyện và lặp lại kế hoạch. Giữ `collaborative_planning=True` để tiếp tục ở chế độ lập kế hoạch.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Bước 3: Phê duyệt và thực hiện

Đặt `collaborative_planning=False` (hoặc bỏ qua) để phê duyệt kế hoạch và bắt đầu nghiên cứu.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Hình ảnh trực quan

Khi `visualization` được đặt thành `"auto"`, tác nhân có thể tạo biểu đồ, đồ thị và các phần tử trực quan khác để hỗ trợ các kết quả nghiên cứu của mình.
Hình ảnh được tạo sẽ có trong đầu ra phản hồi và được truyền dưới dạng các delta `image`. Để có kết quả tốt nhất, hãy yêu cầu rõ ràng về hình ảnh trong câu hỏi của bạn, ví dụ: "Đưa biểu đồ cho thấy xu hướng theo thời gian" hoặc "Tạo hình ảnh so sánh thị phần". Việc đặt `visualization` thành `"auto"` sẽ bật tính năng này, nhưng tác nhân chỉ tạo hình ảnh khi câu lệnh yêu cầu.

### Python

```
import base64
from IPython.display import Image, display

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for output in result.outputs:
    if output.type == "text":
        print(output.text)
    elif output.type == "image" and output.data:
        image_bytes = base64.b64decode(output.data)
        print(f"Received image: {len(image_bytes)} bytes")
        # To display in a Jupyter notebook:
        # from IPython.display import display, Image
        # display(Image(data=image_bytes))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const output of result.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    } else if (output.type === 'image' && output.data) {
        console.log(`[Image Output: ${output.data.substring(0, 20)}...]`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Các công cụ được hỗ trợ

Deep Research hỗ trợ nhiều công cụ tích hợp và công cụ bên ngoài. Theo mặc định (khi không có tham số `tools` nào được cung cấp), tác nhân có quyền truy cập vào Google Tìm kiếm, Bối cảnh URL và Thực thi mã. Bạn có thể chỉ định rõ ràng các công cụ để hạn chế hoặc mở rộng khả năng của tác nhân.

| Công cụ | Giá trị loại | Mô tả |
| --- | --- | --- |
| Google Tìm kiếm | `google_search` | Tìm kiếm trên web công khai. Bật theo mặc định. |
| Ngữ cảnh URL | `url_context` | Đọc và tóm tắt nội dung trang web. Bật theo mặc định. |
| Thực thi mã | `code_execution` | Thực thi mã để thực hiện các phép tính và phân tích dữ liệu. Bật theo mặc định. |
| Máy chủ MCP | `mcp_server` | Kết nối với các máy chủ MCP từ xa để truy cập vào công cụ bên ngoài. |
| Tìm kiếm tệp | `file_search` | Tìm kiếm tập hợp tài liệu bạn đã tải lên. |

### Google Tìm kiếm

Bật Google Tìm kiếm một cách rõ ràng làm công cụ duy nhất:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Bối cảnh URL

Cho phép tác nhân đọc và tóm tắt các trang web cụ thể:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Thực thi mã

Cho phép tác nhân thực thi mã để tính toán và phân tích dữ liệu:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Máy chủ MCP

Cung cấp `name` và `url` của máy chủ trong cấu hình công cụ. Bạn cũng có thể truyền thông tin xác thực và hạn chế những công cụ mà tác nhân có thể gọi.

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `type` | `string` | Có | Phải là `"mcp_server"`. |
| `name` | `string` | Không | Tên hiển thị của máy chủ MCP. |
| `url` | `string` | Không | URL đầy đủ cho điểm cuối của máy chủ MCP. |
| `headers` | `object` | Không | Các cặp khoá-giá trị được gửi dưới dạng tiêu đề HTTP trong mỗi yêu cầu đến máy chủ (ví dụ: mã thông báo xác thực). |
| `allowed_tools` | `array` | Không | Hạn chế những công cụ mà tác nhân có thể gọi từ máy chủ. |

#### Cách sử dụng cơ bản

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Tìm kiếm tệp

Cấp cho tác nhân quyền truy cập vào dữ liệu của riêng bạn bằng cách sử dụng công cụ [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Khả năng điều hướng và định dạng

Bạn có thể điều hướng đầu ra của tác nhân bằng cách cung cấp hướng dẫn định dạng cụ thể trong câu lệnh. Nhờ đó, bạn có thể sắp xếp báo cáo thành các phần và tiểu mục cụ thể, thêm bảng dữ liệu hoặc điều chỉnh giọng điệu cho các đối tượng khác nhau (ví dụ: "chuyên môn", "điều hành", "thông thường").

Xác định rõ định dạng đầu ra mong muốn trong văn bản đầu vào.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Thông tin đầu vào đa phương thức

Tính năng Deep Research hỗ trợ nhiều phương thức nhập, bao gồm cả hình ảnh và tài liệu (tệp PDF), cho phép tác nhân phân tích nội dung trực quan và tiến hành nghiên cứu dựa trên nền tảng web theo bối cảnh của thông tin đầu vào được cung cấp.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Hiểu tài liệu

Truyền trực tiếp tài liệu dưới dạng dữ liệu đầu vào đa phương thức. Trợ lý sẽ phân tích các tài liệu được cung cấp và tiến hành nghiên cứu dựa trên nội dung của các tài liệu đó.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Xử lý các tác vụ chạy trong thời gian dài

Deep Research là một quy trình gồm nhiều bước, bao gồm lập kế hoạch, tìm kiếm, đọc và viết. Chu kỳ này thường vượt quá giới hạn thời gian chờ tiêu chuẩn của các lệnh gọi API đồng bộ.

Nhân viên hỗ trợ bắt buộc phải sử dụng `background=True`. API này sẽ trả về ngay một đối tượng `Interaction` một phần. Bạn có thể dùng thuộc tính `id` để truy xuất một lượt tương tác cho hoạt động bỏ phiếu. Trạng thái tương tác sẽ chuyển từ `in_progress` sang `completed` hoặc `failed`.

### Phát trực tiếp

Tính năng Deep Research hỗ trợ truyền trực tuyến để nhận thông tin cập nhật theo thời gian thực về tiến trình nghiên cứu, bao gồm cả bản tóm tắt ý tưởng, đầu ra văn bản và hình ảnh được tạo.
Bạn phải đặt `stream=True` và `background=True`.

Để nhận các bước suy luận trung gian (tư duy) và thông tin cập nhật về tiến trình, bạn phải bật **bản tóm tắt tư duy** bằng cách đặt `thinking_summaries` thành `"auto"` trong `agent_config`. Nếu không có tham số này, luồng có thể chỉ cung cấp kết quả cuối cùng.

#### Loại sự kiện phát trực tuyến

| Loại sự kiện | Loại delta | Mô tả |
| --- | --- | --- |
| `content.delta` | `thought_summary` | Bước suy luận trung gian của tác nhân. |
| `content.delta` | `text` | Một phần của văn bản đầu ra cuối cùng. |
| `content.delta` | `image` | Một hình ảnh được tạo (được mã hoá bằng base64). |

Ví dụ sau đây bắt đầu một tác vụ nghiên cứu và xử lý luồng bằng tính năng tự động kết nối lại. Thao tác này theo dõi `interaction_id` và `last_event_id` để nếu kết nối bị gián đoạn (ví dụ: sau khi hết thời gian chờ 600 giây), thao tác này có thể tiếp tục từ nơi bị gián đoạn.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for chunk in stream:
        if chunk.event_type == "interaction.start":
            interaction_id = chunk.interaction.id
        if chunk.event_id:
            last_event_id = chunk.event_id
        if chunk.event_type == "content.delta":
            if chunk.delta.type == "text":
                print(chunk.delta.text, end="", flush=True)
            elif chunk.delta.type == "thought_summary":
                print(f"Thought: {chunk.delta.content.text}", flush=True)
        elif chunk.event_type in ("interaction.complete", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const chunk of stream) {
        if (chunk.event_type === 'interaction.start') {
            interactionId = chunk.interaction.id;
        }
        if (chunk.event_id) lastEventId = chunk.event_id;
        if (chunk.event_type === 'content.delta') {
            if (chunk.delta.type === 'text') {
                process.stdout.write(chunk.delta.text);
            } else if (chunk.delta.type === 'thought_summary') {
                console.log(`Thought: ${chunk.delta.content.text}`);
            }
        } else if (['interaction.complete', 'error'].includes(chunk.event_type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Câu hỏi nối tiếp và lượt tương tác

Bạn có thể tiếp tục cuộc trò chuyện sau khi nhân viên hỗ trợ gửi báo cáo cuối cùng bằng cách sử dụng `previous_interaction_id`. Nhờ đó, bạn có thể yêu cầu làm rõ, tóm tắt hoặc giải thích chi tiết về các phần cụ thể của nghiên cứu mà không cần bắt đầu lại toàn bộ nhiệm vụ.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Trường hợp nên dùng Tác nhân Deep Research của Gemini

Deep Research là một **tác nhân**, chứ không chỉ là một mô hình. Công cụ này phù hợp nhất với những khối lượng công việc yêu cầu phương pháp "nhà phân tích trong hộp" thay vì trò chuyện có độ trễ thấp.

| Tính năng | Các mô hình Gemini tiêu chuẩn | Tác nhân Deep Research của Gemini |
| --- | --- | --- |
| **Độ trễ** | Giây | Phút (Không đồng bộ/Nền) |
| **Quy trình** | Tạo -> Đầu ra | Lập kế hoạch -> Tìm kiếm -> Đọc -> Lặp lại -> Đầu ra |
| **Đầu ra** | Cuộc trò chuyện, viết mã, bản tóm tắt ngắn | Báo cáo chi tiết, phân tích dài, bảng so sánh |
| **Phù hợp nhất cho** | Chatbot, trích xuất, viết sáng tạo | Phân tích thị trường, thẩm định, đánh giá tài liệu, bối cảnh cạnh tranh |

## Cấu hình tác nhân

Deep Research sử dụng tham số `agent_config` để kiểm soát hành vi.
Truyền nó dưới dạng một từ điển có các trường sau:

| Trường | Loại | Mặc định | Mô tả |
| --- | --- | --- | --- |
| `type` | `string` | Bắt buộc | Phải là `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Đặt thành `"auto"` để nhận các bước suy luận trung gian trong quá trình truyền trực tuyến. Đặt thành `"none"` để tắt. |
| `visualization` | `string` | `"auto"` | Đặt thành `"auto"` để cho phép biểu đồ và hình ảnh do tác nhân tạo. Đặt thành `"off"` để tắt. |
| `collaborative_planning` | `boolean` | `false` | Đặt thành `true` để bật tính năng xem xét kế hoạch nhiều lượt trước khi bắt đầu nghiên cứu. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Tình trạng còn hàng và giá

Bạn có thể truy cập vào Gemini Deep Research Agent bằng Interactions API trong Google AI Studio và Gemini API.

Giá tuân theo [mô hình trả tiền theo mức dùng](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#pricing-for-agents) dựa trên các mô hình Gemini cơ bản và các công cụ cụ thể mà tác nhân sử dụng. Không giống như các yêu cầu trò chuyện thông thường (một yêu cầu dẫn đến một kết quả đầu ra), tác vụ Deep Research là một quy trình làm việc dựa trên tác nhân. Một yêu cầu duy nhất sẽ kích hoạt một vòng lặp tự động gồm lập kế hoạch, tìm kiếm, đọc và suy luận.

### Chi phí ước tính

Chi phí sẽ khác nhau tuỳ thuộc vào mức độ nghiên cứu cần thiết. Trợ lý tự động xác định mức độ cần thiết của việc đọc và tìm kiếm để trả lời câu lệnh của bạn.

- **Deep Research** (`deep-research-preview-04-2026`): Đối với một cụm từ tìm kiếm thông thường đòi hỏi mức độ phân tích vừa phải, tác nhân có thể sử dụng khoảng 80 cụm từ tìm kiếm, khoảng 250.000 mã thông báo đầu vào (khoảng 50-70% được lưu vào bộ nhớ đệm) và khoảng 60.000 mã thông báo đầu ra.
  - **Tổng ước tính:** Khoảng 10.000 VND – 30.000 VND cho mỗi nhiệm vụ
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Để phân tích sâu về môi trường cạnh tranh hoặc thẩm định kỹ lưỡng, tác nhân có thể sử dụng tối đa khoảng 160 cụm từ tìm kiếm, khoảng 900.000 mã thông báo đầu vào (khoảng 50-70% được lưu vào bộ nhớ đệm) và khoảng 80.000 mã thông báo đầu ra.
  - **Tổng ước tính:** Khoảng 30.000 VND – 70.000 VND cho mỗi nhiệm vụ

## Lưu ý về an toàn

Việc cấp cho một đặc vụ quyền truy cập vào web và các tệp riêng tư của bạn đòi hỏi bạn phải cân nhắc kỹ lưỡng các rủi ro về an toàn.

- **Tiêm câu lệnh (prompt injection) sử dụng tệp:** Trợ lý sẽ đọc nội dung của các tệp mà bạn cung cấp. Đảm bảo rằng các tài liệu đã tải lên (tệp PDF, tệp văn bản) đến từ các nguồn đáng tin cậy. Một tệp độc hại có thể chứa văn bản ẩn được thiết kế để thao túng đầu ra của tác nhân.
- **Rủi ro về nội dung trên web:** Đặc vụ tìm kiếm trên web công khai. Mặc dù chúng tôi triển khai các bộ lọc an toàn mạnh mẽ, nhưng vẫn có nguy cơ là tác nhân có thể gặp phải và xử lý các trang web độc hại. Bạn nên xem xét `citations` được cung cấp trong câu trả lời để xác minh các nguồn.
- **Trích xuất:** Hãy thận trọng khi yêu cầu tác nhân tóm tắt dữ liệu nội bộ nhạy cảm nếu bạn cũng cho phép tác nhân duyệt web.

## Các phương pháp hay nhất

- **Nhắc về những thông tin chưa biết:** Hướng dẫn nhân viên cách xử lý dữ liệu bị thiếu.
  Ví dụ: hãy thêm *"Nếu không có số liệu cụ thể cho năm 2025, hãy nêu rõ rằng đó là số liệu dự đoán hoặc không có sẵn thay vì ước tính"* vào câu lệnh của bạn.
- **Cung cấp bối cảnh:** Hỗ trợ hoạt động nghiên cứu của tác nhân bằng cách cung cấp thông tin cơ bản hoặc các ràng buộc ngay trong câu lệnh đầu vào.
- **Sử dụng tính năng lập kế hoạch cộng tác:** Đối với các câu hỏi phức tạp, hãy bật tính năng lập kế hoạch cộng tác để xem xét và tinh chỉnh kế hoạch nghiên cứu trước khi thực hiện.
- **Thông tin đầu vào đa phương thức:** Deep Research Agent hỗ trợ thông tin đầu vào đa phương thức.
  Hãy sử dụng một cách thận trọng vì điều này sẽ làm tăng chi phí và nguy cơ tràn cửa sổ ngữ cảnh.

## Các điểm hạn chế

- **Trạng thái thử nghiệm**: Interactions API đang ở giai đoạn thử nghiệm công khai. Các tính năng và lược đồ có thể thay đổi.
- **Công cụ tuỳ chỉnh:** Hiện tại, bạn không thể cung cấp công cụ Gọi hàm tuỳ chỉnh nhưng có thể sử dụng các máy chủ MCP (Giao thức ngữ cảnh mô hình) từ xa với tác nhân Deep Research.
- **Đầu ra có cấu trúc:** Deep Research Agent hiện không hỗ trợ đầu ra có cấu trúc.
- **Thời gian nghiên cứu tối đa:** Trợ lý Deep Research có thời gian nghiên cứu tối đa là 60 phút. Hầu hết các nhiệm vụ sẽ hoàn tất trong vòng 20 phút.
- **Yêu cầu về cửa hàng:** Việc thực thi tác nhân bằng `background=True` yêu cầu `store=True`.
- **Google Tìm kiếm:** [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) được bật theo mặc định và [các hạn chế cụ thể](https://ai.google.dev/gemini-api/terms?hl=vi#use-restrictions2) áp dụng cho kết quả có căn cứ.

## Bước tiếp theo

- Tìm hiểu thêm về [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi).
- Hãy dùng thử [Deep Research trong Sổ tay về Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Deep_Research.ipynb?hl=vi).
- Tìm hiểu cách sử dụng dữ liệu của riêng bạn bằng công cụ [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
