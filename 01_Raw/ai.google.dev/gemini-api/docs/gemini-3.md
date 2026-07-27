---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=vi
fetched_at: 2026-07-27T04:49:12.106274+00:00
title: "H\u01b0\u1edbng d\u1eabn cho nh\u00e0 ph\u00e1t tri\u1ec3n Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn cho nhà phát triển Gemini 3

Gemini 3 là mô hình thông minh nhất của chúng tôi cho đến nay, được xây dựng dựa trên nền tảng suy luận tiên tiến. Mô hình này được thiết kế để hiện thực hoá mọi ý tưởng bằng cách thành thạo quy trình công việc của tác nhân, lập trình tự động và các nhiệm vụ đa phương thức phức tạp.
Hướng dẫn này đề cập đến các tính năng chính của mô hình Gemini 3 và cách tận dụng tối đa mô hình này.

Khám phá [bộ sưu tập ứng dụng Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=vi) của chúng tôi để
xem cách mô hình này xử lý khả năng suy luận nâng cao, lập trình tự động và các nhiệm vụ đa phương thức
phức tạp.

Bắt đầu với một vài dòng mã:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Giới thiệu về dòng Gemini 3

Gemini 3.1 Pro phù hợp nhất cho các nhiệm vụ phức tạp đòi hỏi kiến thức rộng về thế giới và khả năng suy luận nâng cao trên nhiều phương thức.

Gemini 3 Flash là mô hình mới nhất thuộc dòng 3, có trí thông minh ở cấp độ Pro với tốc độ và mức giá của Flash.

Nano Banana Pro (còn gọi là Gemini 3 Pro Image) là mô hình tạo hình ảnh chất lượng cao nhất của chúng tôi, còn Nano Banana 2 (còn gọi là Gemini 3.1 Flash Image) là mô hình tương đương có số lượng lớn, hiệu suất cao và mức giá thấp hơn.

Gemini 3.1 Flash-Lite là mô hình hiệu suất cao được xây dựng để mang lại hiệu quả về chi phí và xử lý các nhiệm vụ có số lượng lớn.

Tất cả các mô hình Gemini 3 hiện đều ở chế độ xem trước.

| Mã kiểu máy | Cửa sổ ngữ cảnh (Đầu vào / Đầu ra) | Điểm cắt kiến thức | Mức giá (Đầu vào / Đầu ra)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 triệu / 64.000 | Tháng 1 năm 2025 | 0,25 USD (văn bản, hình ảnh, video), 0,50 USD (âm thanh) / 1,50 USD |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Tháng 1 năm 2025 | 0,25 USD (Đầu vào dạng văn bản) / 0,067 USD (Đầu ra dạng hình ảnh)\*\* |
| **gemini-3.1-pro-preview** | 1 triệu / 64.000 | Tháng 1 năm 2025 | 2 USD / 12 USD (<200.000 token)   4 USD / 18 USD (>200.000 token) |
| **gemini-3-flash-preview** | 1 triệu / 64.000 | Tháng 1 năm 2025 | 0,50 USD / 3 USD |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Tháng 1 năm 2025 | 2 USD (Đầu vào dạng văn bản) / 0,134 USD (Đầu ra dạng hình ảnh)\*\* |

*\* Mức giá tính cho 1 triệu token, trừ phi có ghi chú khác.*
*\*\* Mức giá cho hình ảnh thay đổi theo độ phân giải. Hãy xem [trang giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) để biết thông tin chi tiết.*

Để biết thông tin chi tiết về hạn mức, mức giá và thông tin bổ sung, hãy xem trang về các
[mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi).

## Các tính năng mới của API trong Gemini 3

Gemini 3 giới thiệu các tham số mới được thiết kế để giúp nhà phát triển kiểm soát tốt hơn độ trễ, chi phí và độ trung thực đa phương thức.

### Cấp độ tư duy

Các mô hình thuộc dòng Gemini 3 sử dụng chế độ tư duy động theo mặc định để suy luận thông qua các câu lệnh. Bạn có thể sử dụng tham số `thinking_level`, tham số này kiểm soát độ sâu **tối đa** của quy trình suy luận nội bộ của mô hình trước khi mô hình tạo ra câu trả lời. Gemini 3 coi các cấp độ này là hạn mức tương đối cho việc tư duy thay vì đảm bảo nghiêm ngặt về token.

Nếu bạn không chỉ định `thinking_level`, Gemini 3 sẽ mặc định là `high`. Để có câu trả lời nhanh hơn và độ trễ thấp hơn khi không cần suy luận phức tạp, bạn có thể giới hạn cấp độ tư duy của mô hình thành `low`.

| Cấp độ tư duy | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Mô tả |
| --- | --- | --- | --- | --- |
| **`minimal`** | Không được hỗ trợ | Được hỗ trợ (Mặc định) | Được hỗ trợ | Khớp với chế độ cài đặt "không tư duy" cho hầu hết các truy vấn. Mô hình có thể tư duy rất ít cho các nhiệm vụ lập trình phức tạp. Giảm thiểu độ trễ cho các ứng dụng trò chuyện hoặc có thông lượng cao. Xin lưu ý rằng `minimal` không đảm bảo rằng chế độ tư duy đã tắt. |
| **`low`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Giảm thiểu độ trễ và chi phí. Phù hợp nhất cho các ứng dụng tuân theo hướng dẫn đơn giản, trò chuyện hoặc có thông lượng cao. |
| **`medium`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Tư duy cân bằng cho hầu hết các nhiệm vụ. |
| **`high`** | Được hỗ trợ (Mặc định, Động) | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Tối đa hoá độ sâu suy luận. Mô hình có thể mất nhiều thời gian hơn đáng kể để đạt được token đầu ra đầu tiên (không tư duy), nhưng đầu ra sẽ được suy luận cẩn thận hơn. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Nhiệt độ

Đối với tất cả các mô hình Gemini 3, bạn nên giữ tham số nhiệt độ ở giá trị mặc định là `1.0`.

Mặc dù các mô hình trước đây thường được hưởng lợi từ việc điều chỉnh nhiệt độ để kiểm soát khả năng sáng tạo so với tính xác định, nhưng khả năng suy luận của Gemini 3 được tối ưu hoá cho chế độ cài đặt mặc định. Việc thay đổi nhiệt độ (đặt nhiệt độ dưới 1.0) có thể dẫn đến hành vi không mong muốn, chẳng hạn như lặp lại hoặc giảm hiệu suất, đặc biệt là trong các nhiệm vụ phức tạp về toán học hoặc suy luận.

### Chữ ký tư duy

Các mô hình Gemini 3 sử dụng chữ ký tư duy để duy trì ngữ cảnh suy luận trên các lệnh gọi API. Các chữ ký này là biểu diễn được mã hoá của quy trình tư duy nội bộ của mô hình.

- **Chế độ có trạng thái (Đề xuất)**: Khi sử dụng API Tương tác ở chế độ có trạng thái (cung cấp `previous_interaction_id`), máy chủ sẽ tự động quản lý nhật ký cuộc trò chuyện và chữ ký tư duy.
- **Chế độ không trạng thái**: Nếu bạn đang quản lý nhật sử cuộc trò chuyện theo cách thủ công, bạn phải đưa các khối tư duy có chữ ký vào các yêu cầu tiếp theo để xác thực tính xác thực.

Để biết thông tin chi tiết, hãy xem trang [Chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).

### Đầu ra có cấu trúc bằng các công cụ

Các mô hình Gemini 3 cho phép bạn kết hợp [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) với các công cụ tích hợp, bao gồm
[Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi), [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi), [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Tạo hình ảnh

Gemini 3.1 Flash Image và Gemini 3 Pro Image cho phép bạn tạo và chỉnh sửa hình ảnh từ câu lệnh dạng văn bản. Mô hình này sử dụng
khả năng suy luận để "tư duy" thông qua một câu lệnh và có thể truy xuất dữ liệu theo thời gian thực (chẳng hạn như
dự báo thời tiết hoặc biểu đồ chứng khoán) trước khi sử dụng [tính năng bám sát nguồn của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) để tạo hình ảnh có độ trung thực cao.

**Các tính năng mới và cải tiến:**

- **Kết xuất văn bản và 4K:** Tạo văn bản và sơ đồ sắc nét, dễ đọc với độ phân giải lên đến 2K và 4K.
- **Tạo hình ảnh bám sát nguồn:** Sử dụng công cụ `google_search` để xác minh thông tin và tạo hình ảnh dựa trên thông tin thực tế. Tính năng bám sát nguồn bằng Google Tìm kiếm *Hình ảnh* có sẵn cho Gemini 3.1 Flash Image.
- **Chỉnh sửa trong cuộc trò chuyện:** Chỉnh sửa hình ảnh nhiều lượt bằng cách yêu cầu thay đổi (ví dụ: "Thay đổi nền thành cảnh hoàng hôn"). Quy trình này dựa vào **Chữ ký tư duy** để giữ nguyên ngữ cảnh hình ảnh giữa các lượt.

Để biết thông tin chi tiết đầy đủ về tỷ lệ khung hình, quy trình chỉnh sửa và các lựa chọn cấu hình
, hãy xem [hướng dẫn Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Ví dụ về câu trả lời**

![Thời tiết ở Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=vi)

### Thực thi mã bằng hình ảnh

Gemini 3 Flash có thể coi hình ảnh là một cuộc điều tra chủ động, chứ không chỉ là một cái nhìn thoáng qua. Bằng cách kết hợp khả năng suy luận với [việc thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi), mô hình sẽ xây dựng một kế hoạch, sau đó viết và
thực thi mã Python để phóng to, cắt, chú thích hoặc thao tác với hình ảnh
từng bước để bám sát nguồn câu trả lời bằng hình ảnh.

**Trường hợp sử dụng:**

- **Phóng to và kiểm tra:** Mô hình này ngầm phát hiện khi các chi tiết quá nhỏ (ví dụ: đọc một đồng hồ đo hoặc số sê-ri ở xa) và viết mã để cắt và kiểm tra lại khu vực đó ở độ phân giải cao hơn.
- **Toán học và vẽ đồ thị bằng hình ảnh:** Mô hình này có thể chạy các phép tính nhiều bước bằng mã (ví dụ: tính tổng các mục hàng trên biên nhận hoặc tạo biểu đồ Matplotlib từ dữ liệu đã trích xuất).
- **Chú thích hình ảnh:** Mô hình này có thể vẽ mũi tên, hộp giới hạn hoặc các chú thích khác trực tiếp lên hình ảnh để trả lời các câu hỏi về không gian như "Mục này nên đặt ở đâu?".

Để bật tính năng tư duy bằng hình ảnh, hãy định cấu hình [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) như một công cụ. Mô hình này sẽ tự động sử dụng mã để thao tác với hình ảnh khi cần.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Để biết thêm thông tin chi tiết về việc thực thi mã bằng hình ảnh, hãy xem bài viết [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi#images).

### Câu trả lời đa phương thức của hàm

[Tính năng gọi hàm đa phương thức](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#multimodal)
cho phép người dùng có câu trả lời của hàm chứa các đối tượng đa phương thức, giúp cải thiện việc sử dụng các chức năng gọi hàm
của mô hình. Tính năng gọi hàm tiêu chuẩn chỉ hỗ trợ câu trả lời của hàm dựa trên văn bản:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Kết hợp các công cụ tích hợp và tính năng gọi hàm

Gemini 3 cho phép sử dụng các công cụ tích hợp (như Google Tìm kiếm, ngữ cảnh URL
và [nhiều công cụ khác](https://ai.google.dev/gemini-api/docs/tools?hl=vi)) và các công cụ [gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) tuỳ chỉnh trong cùng một lệnh gọi API, cho phép các quy trình công việc phức tạp hơn.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Di chuyển từ Gemini 2.5

Gemini 3 là mô hình mạnh mẽ nhất của chúng tôi cho đến nay và cải thiện từng bước so với Gemini 2.5. Khi di chuyển, hãy cân nhắc những yếu tố sau:

- **Tư duy:** Nếu trước đây bạn đang sử dụng kỹ thuật tạo câu lệnh phức tạp (chẳng hạn như
  chuỗi tư duy) để buộc Gemini 2.5 suy luận, hãy thử Gemini 3 với
  `thinking_level: "high"` và các câu lệnh đơn giản.
- **Chế độ cài đặt nhiệt độ:** Nếu mã hiện có của bạn đặt nhiệt độ một cách rõ ràng (đặc biệt là các giá trị thấp cho đầu ra xác định), bạn nên xoá tham số này và sử dụng giá trị mặc định là 1.0 của Gemini 3 để tránh các vấn đề tiềm ẩn về vòng lặp hoặc giảm hiệu suất đối với các nhiệm vụ phức tạp.
- **Hiểu tài liệu và tệp PDF:** Nếu bạn dựa vào hành vi cụ thể để phân tích cú pháp tài liệu dày đặc, hãy kiểm thử chế độ cài đặt `media_resolution_high` mới để đảm bảo độ chính xác liên tục.
- **Mức tiêu thụ token:** Việc di chuyển sang các giá trị mặc định của Gemini 3 có thể **tăng** mức sử dụng token cho tệp PDF nhưng **giảm** mức sử dụng token cho video. Nếu các yêu cầu hiện vượt quá cửa sổ ngữ cảnh do độ phân giải mặc định cao hơn, bạn nên giảm rõ ràng độ phân giải của nội dung nghe nhìn.
- **Phân đoạn hình ảnh:** Các tính năng phân đoạn hình ảnh (trả về mặt nạ ở cấp độ pixel cho các đối tượng) không được hỗ trợ trong Gemini 3 Pro hoặc Gemini 3 Flash. Đối với
  các khối lượng công việc yêu cầu tính năng phân đoạn hình ảnh tích hợp, bạn nên tiếp tục
  sử dụng Gemini 2.5 Flash khi tắt chế độ tư duy hoặc [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi).
- **Sử dụng máy tính:** Gemini 3 Pro và Gemini 3 Flash hỗ trợ tính năng [Sử dụng
  máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi). Không giống như dòng 2.5, bạn không cần sử dụng một mô hình riêng để truy cập vào công cụ Sử dụng máy tính.
- **Hỗ trợ công cụ**: [Các mô hình Gemini 3 hiện hỗ trợ việc kết hợp các công cụ tích hợp với tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi). [Các mô hình Gemini 3
  hiện cũng hỗ trợ tính năng bám sát nguồn trên
  Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi).

## Khả năng tương thích với OpenAI

Đối với những người dùng sử dụng [lớp tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi),
các tham số tiêu chuẩn (tham số `reasoning_effort` của OpenAI) sẽ tự động được liên kết với các tham số tương đương của
Gemini (`thinking_level`).

## Các phương pháp hay nhất khi đưa ra câu lệnh

Gemini 3 là một mô hình suy luận, thay đổi cách bạn nên đưa ra câu lệnh.

- **Hướng dẫn chính xác:** Hãy đưa ra câu lệnh đầu vào một cách ngắn gọn. Gemini 3 phản hồi tốt nhất với các hướng dẫn trực tiếp và rõ ràng. Mô hình này có thể phân tích quá mức các kỹ thuật tạo câu lệnh dài dòng hoặc quá phức tạp được sử dụng cho các mô hình cũ.
- **Độ chi tiết của đầu ra:** Theo mặc định, Gemini 3 ít chi tiết hơn và thích cung cấp câu trả lời trực tiếp và hiệu quả. Nếu trường hợp sử dụng của bạn yêu cầu một nhân vật trò chuyện nhiều hơn hoặc "thân thiện", bạn phải hướng mô hình một cách rõ ràng trong câu lệnh (ví dụ: "Giải thích điều này như một trợ lý thân thiện và hay nói").
- **Quản lý ngữ cảnh:** Khi làm việc với các tập dữ liệu lớn (ví dụ: toàn bộ sách, cơ sở mã hoặc video dài), hãy đặt các hướng dẫn hoặc câu hỏi cụ thể ở cuối câu lệnh, sau ngữ cảnh dữ liệu. Liên kết khả năng suy luận của mô hình với dữ liệu được cung cấp bằng cách bắt đầu câu hỏi bằng một cụm từ như "Dựa trên thông tin trước đó...".

Tìm hiểu thêm về các chiến lược thiết kế câu lệnh trong [hướng dẫn về kỹ thuật tạo câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi).

## Câu hỏi thường gặp

1. **Điểm cắt kiến thức của Gemini 3 là gì?** Các mô hình Gemini 3 có điểm cắt kiến thức là tháng 1 năm 2025. Để biết thông tin mới nhất, hãy sử dụng công cụ
   [Bám sát nguồn trên Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi).
2. **Hạn mức của cửa sổ ngữ cảnh là gì?** Các mô hình Gemini 3 hỗ trợ cửa sổ ngữ cảnh đầu vào 1 triệu token và tối đa 64.000 token đầu ra.
3. **Gemini 3 có gói miễn phí không?** Gemini 3 Flash `gemini-3-flash-preview` có gói miễn phí trong Gemini API. Bạn có thể dùng thử Gemini 3.1 Pro và 3 Flash miễn phí trong Google AI Studio, nhưng không có gói miễn phí cho `gemini-3.1-pro-preview` trong Gemini API.
4. **Mã `thinking_budget` cũ của tôi có còn hoạt động không?** Có, `thinking_budget` vẫn được hỗ trợ để tương thích ngược, nhưng bạn nên di chuyển sang `thinking_level` để có hiệu suất dễ dự đoán hơn. Đừng sử dụng cả hai trong cùng một yêu cầu.
5. **Gemini 3 có hỗ trợ Batch API không?** Có, Gemini 3 hỗ trợ
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi).
6. **Có hỗ trợ tính năng lưu vào bộ nhớ đệm theo ngữ cảnh không?** Có, Gemini 3 hỗ trợ tính năng [lưu vào bộ nhớ đệm theo ngữ cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi).
7. **Gemini 3 hỗ trợ những công cụ nào?** Gemini 3 hỗ trợ
   [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi),
   [Bám sát nguồn bằng Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi),
   [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi),
   [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi), và
   [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi). Mô hình này cũng hỗ trợ
   tính năng [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) tiêu chuẩn cho
   các công cụ tuỳ chỉnh của riêng bạn và kết hợp
   [với các công cụ tích hợp](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).
8. **`gemini-3.1-pro-preview-customtools` là gì?** Nếu bạn đang sử dụng
   `gemini-3.1-pro-preview` và mô hình này bỏ qua các công cụ tuỳ chỉnh của bạn để ưu tiên
   các lệnh bash, hãy thử mô hình `gemini-3.1-pro-preview-customtools` thay thế.
   Xem thêm thông tin [tại đây][customtools-model].

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-08 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-08 UTC."],[],[]]
