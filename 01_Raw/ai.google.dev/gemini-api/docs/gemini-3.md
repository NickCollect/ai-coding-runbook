---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=vi
fetched_at: 2026-07-06T05:22:08.371774+00:00
title: "H\u01b0\u1edbng d\u1eabn cho nh\u00e0 ph\u00e1t tri\u1ec3n Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn cho nhà phát triển Gemini 3

Gemini 3 là dòng mô hình thông minh nhất của chúng tôi cho đến nay, được xây dựng dựa trên nền tảng suy luận tiên tiến. Gemini Pro được thiết kế để biến mọi ý tưởng thành hiện thực bằng cách thành thạo quy trình làm việc dựa trên tác nhân, lập trình tự động và các tác vụ đa phương thức phức tạp.
Hướng dẫn này trình bày các tính năng chính của nhóm mô hình Gemini 3 và cách khai thác tối đa nhóm mô hình này.

Khám phá [bộ sưu tập các ứng dụng Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=vi) để xem cách mô hình này xử lý khả năng suy luận nâng cao, lập trình tự động và các nhiệm vụ phức tạp có nhiều phương thức.

Bắt đầu bằng một vài dòng mã:

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

## Làm quen với dòng Gemini 3

Gemini 3.1 Pro phù hợp nhất với những nhiệm vụ phức tạp đòi hỏi kiến thức rộng lớn về thế giới và khả năng suy luận nâng cao trên nhiều phương thức.

Gemini 3 Flash là mô hình mới nhất thuộc dòng 3, có trí thông minh cấp Pro với tốc độ và mức giá của Flash.

Nano Banana Pro (còn gọi là Gemini 3 Pro Image) là mô hình tạo hình ảnh có chất lượng cao nhất của chúng tôi, còn Nano Banana 2 (còn gọi là Gemini 3.1 Flash Image) là mô hình tương đương có hiệu suất cao, số lượng lớn và mức giá thấp hơn.

Gemini 3.1 Flash-Lite là mô hình hiệu suất cao được thiết kế để mang lại hiệu quả về chi phí và xử lý các nhiệm vụ với khối lượng lớn.

Tất cả các mô hình Gemini 3 hiện đang ở giai đoạn dùng thử.

| Mã kiểu máy | Cửa sổ ngữ cảnh (Vào / Ra) | Điểm cắt kiến thức | Giá (Đầu vào / Đầu ra)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Tháng 1 năm 2025 | 0,25 USD (văn bản, hình ảnh, video), 0,5 USD (âm thanh) / 1,5 USD |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Tháng 1 năm 2025 | 0,25 USD (Đầu vào là văn bản) / 0,067 USD (Đầu ra là hình ảnh)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Tháng 1 năm 2025 | 2 USD / 12 USD (<200.000 token)   4 USD / 18 USD (>200.000 token) |
| **gemini-3-flash-preview** | 1M / 64k | Tháng 1 năm 2025 | 0,5 USD / 3 USD |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Tháng 1 năm 2025 | 2 USD (Nhập văn bản) / 0,134 USD (Xuất hình ảnh)\*\* |

*\* Giá tính trên 1 triệu mã thông báo, trừ phi có quy định khác.*
*\*\* Giá hình ảnh thay đổi theo độ phân giải. Hãy xem [trang giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) để biết thông tin chi tiết.*

Để biết các giới hạn, mức giá và thông tin bổ sung chi tiết, hãy xem [trang mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi).

## Các tính năng mới của API trong Gemini 3

Gemini 3 giới thiệu các tham số mới được thiết kế để giúp nhà phát triển kiểm soát độ trễ, chi phí và độ trung thực của nhiều phương thức hiệu quả hơn.

### Cấp độ tư duy

Các mô hình Gemini 3 sử dụng tư duy linh hoạt theo mặc định để suy luận thông qua các câu lệnh. Bạn có thể sử dụng tham số `thinking_level` để kiểm soát độ sâu **tối đa** của quy trình suy luận nội bộ của mô hình trước khi mô hình tạo ra một câu trả lời. Gemini 3 coi những cấp độ này là mức cho phép tương đối để suy nghĩ thay vì đảm bảo nghiêm ngặt về số lượng mã thông báo.

Nếu bạn không chỉ định `thinking_level`, Gemini 3 sẽ mặc định là `high`. Để có câu trả lời nhanh hơn và có độ trễ thấp hơn khi không cần suy luận phức tạp, bạn có thể giới hạn mức độ suy nghĩ của mô hình ở `low`.

| Cấp độ tư duy | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Mô tả |
| --- | --- | --- | --- | --- |
| **`minimal`** | Không được hỗ trợ | Được hỗ trợ (Mặc định) | Được hỗ trợ | Phù hợp với chế độ cài đặt "không suy nghĩ" cho hầu hết các cụm từ tìm kiếm. Mô hình có thể suy nghĩ rất ít cho các nhiệm vụ lập trình phức tạp. Giảm thiểu độ trễ cho các ứng dụng trò chuyện hoặc ứng dụng có thông lượng cao. Xin lưu ý rằng `minimal` không đảm bảo rằng tính năng suy nghĩ đã tắt. |
| **`low`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Giảm thiểu độ trễ và chi phí. Phù hợp nhất với các ứng dụng tuân theo hướng dẫn đơn giản, trò chuyện hoặc có thông lượng cao. |
| **`medium`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Tư duy cân bằng cho hầu hết các nhiệm vụ. |
| **`high`** | Được hỗ trợ (Mặc định, Động) | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Tối đa hoá độ sâu suy luận. Mô hình có thể mất nhiều thời gian hơn đáng kể để đạt được mã thông báo đầu ra đầu tiên (không phải mã thông báo tư duy), nhưng đầu ra sẽ được suy luận cẩn thận hơn. |

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

Mặc dù các mô hình trước đây thường được hưởng lợi từ việc điều chỉnh nhiệt độ để kiểm soát khả năng sáng tạo so với tính xác định, nhưng khả năng suy luận của Gemini 3 được tối ưu hoá cho chế độ cài đặt mặc định. Việc thay đổi nhiệt độ (đặt nhiệt độ dưới 1.0) có thể dẫn đến hành vi không mong muốn, chẳng hạn như lặp lại hoặc giảm hiệu suất, đặc biệt là trong các nhiệm vụ phức tạp về toán học hoặc lý luận.

### Chữ ký của suy nghĩ

Các mô hình Gemini 3 sử dụng chữ ký suy luận để duy trì ngữ cảnh suy luận trong các lệnh gọi API. Các chữ ký này là biểu thị được mã hoá của quy trình suy nghĩ nội bộ của mô hình.

- **Chế độ có trạng thái (Nên dùng)**: Khi sử dụng Interactions API ở chế độ có trạng thái (cung cấp `previous_interaction_id`), máy chủ sẽ tự động quản lý nhật ký cuộc trò chuyện và chữ ký suy nghĩ.
- **Chế độ không trạng thái**: Nếu đang quản lý nhật ký cuộc trò chuyện theo cách thủ công, bạn phải đưa các khối suy nghĩ cùng với chữ ký của chúng vào các yêu cầu tiếp theo để xác thực tính chân thực.

Để biết thông tin chi tiết, hãy xem trang [Chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).

### Đầu ra có cấu trúc bằng các công cụ

Các mô hình Gemini 3 cho phép bạn kết hợp [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) với các công cụ tích hợp sẵn, bao gồm [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi), [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi), [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

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

Gemini 3.1 Flash Image và Gemini 3 Pro Image cho phép bạn tạo và chỉnh sửa hình ảnh từ câu lệnh văn bản. Mô hình này sử dụng khả năng suy luận để "suy nghĩ" về một câu lệnh và có thể truy xuất dữ liệu theo thời gian thực (chẳng hạn như dự báo thời tiết hoặc biểu đồ chứng khoán) trước khi sử dụng tính năng [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) để tạo cơ sở trước khi tạo hình ảnh có độ trung thực cao.

**Các chức năng mới và được cải thiện:**

- **Độ phân giải 4K và kết xuất văn bản:** Tạo văn bản và sơ đồ sắc nét, dễ đọc với độ phân giải lên đến 2K và 4K.
- **Tạo nội dung có căn cứ:** Sử dụng công cụ `google_search` để xác minh dữ kiện và tạo hình ảnh dựa trên thông tin thực tế. Căn cứ vào thông tin từ tính năng Tìm kiếm *Hình ảnh* của Google cho Gemini 3.1 Flash Image.
- **Chỉnh sửa bằng ngôn ngữ tự nhiên:** Chỉnh sửa ảnh nhiều lượt bằng cách chỉ cần yêu cầu thay đổi (ví dụ: "Chỉnh sửa để nền là cảnh hoàng hôn"). Quy trình này dựa vào **Chữ ký tư duy** để duy trì ngữ cảnh trực quan giữa các lượt.

Để biết thông tin chi tiết đầy đủ về tỷ lệ khung hình, quy trình chỉnh sửa và các lựa chọn cấu hình, hãy xem [hướng dẫn Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi).

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

**Ví dụ về phản hồi**

![Thời tiết ở Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=vi)

### Thực thi mã bằng hình ảnh

Gemini 3 Flash có thể coi thị giác là một hoạt động điều tra chủ động, chứ không chỉ là một cái nhìn tĩnh. Bằng cách kết hợp suy luận với [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi), mô hình sẽ xây dựng một kế hoạch, sau đó viết và thực thi mã Python để phóng to, cắt, chú thích hoặc thao tác với hình ảnh theo từng bước nhằm đưa ra câu trả lời bám sát nguồn trực quan.

**Trường hợp sử dụng:**

- **Phóng to và kiểm tra:** Mô hình sẽ tự động phát hiện khi các chi tiết quá nhỏ (ví dụ: đọc một đồng hồ đo hoặc số sê-ri ở xa) và viết mã để cắt và kiểm tra lại khu vực ở độ phân giải cao hơn.
- **Phép toán và biểu đồ trực quan:** Mô hình có thể chạy các phép tính nhiều bước bằng mã (ví dụ: tính tổng các mục hàng trên biên nhận hoặc tạo biểu đồ Matplotlib từ dữ liệu đã trích xuất).
- **Chú thích hình ảnh:** Mô hình có thể vẽ mũi tên, khung viền hoặc các chú thích khác trực tiếp lên hình ảnh để trả lời các câu hỏi về không gian như "Mặt hàng này nên đặt ở đâu?".

Để bật tính năng tư duy trực quan, hãy định cấu hình [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) làm công cụ. Mô hình sẽ tự động dùng mã để thao tác với hình ảnh khi cần.

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

Để biết thêm thông tin về việc thực thi mã bằng hình ảnh, hãy xem phần [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi#images).

### Phản hồi của hàm đa phương thức

[Tính năng gọi hàm đa phương thức](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#multimodal) cho phép người dùng nhận được các phản hồi của hàm có chứa các đối tượng đa phương thức, giúp cải thiện khả năng sử dụng tính năng gọi hàm của mô hình. Tính năng gọi hàm tiêu chuẩn chỉ hỗ trợ các phản hồi hàm dựa trên văn bản:

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

### Kết hợp các công cụ tích hợp và lệnh gọi hàm

Gemini 3 cho phép sử dụng các công cụ tích hợp sẵn (như Google Tìm kiếm, ngữ cảnh URL và [nhiều công cụ khác](https://ai.google.dev/gemini-api/docs/tools?hl=vi)) cũng như các công cụ [gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) tuỳ chỉnh trong cùng một lệnh gọi API, cho phép các quy trình công việc phức tạp hơn.

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

Gemini 3 là nhóm mô hình mạnh mẽ nhất của chúng tôi cho đến nay và có sự cải tiến từng bước so với Gemini 2.5. Khi di chuyển, hãy cân nhắc những điều sau:

- **Tư duy:** Nếu trước đây bạn đang sử dụng kỹ thuật thiết kế câu lệnh phức tạp (chẳng hạn như chuỗi suy luận) để buộc Gemini 2.5 suy luận, hãy thử Gemini 3 với `thinking_level: "high"` và câu lệnh đơn giản.
- **Chế độ cài đặt nhiệt độ:** Nếu mã hiện tại của bạn đặt nhiệt độ một cách rõ ràng (đặc biệt là ở giá trị thấp cho đầu ra xác định), bạn nên xoá thông số này và sử dụng giá trị mặc định là 1.0 của Gemini 3 để tránh các vấn đề tiềm ẩn về vòng lặp hoặc giảm hiệu suất đối với các tác vụ phức tạp.
- **Hiểu PDF và tài liệu:** Nếu bạn dựa vào hành vi cụ thể để phân tích cú pháp tài liệu dày đặc, hãy kiểm thử chế độ cài đặt `media_resolution_high` mới để đảm bảo độ chính xác liên tục.
- **Mức tiêu thụ mã thông báo:** Việc di chuyển sang Gemini 3 mặc định có thể **tăng** mức sử dụng mã thông báo cho tệp PDF nhưng **giảm** mức sử dụng mã thông báo cho video. Nếu các yêu cầu hiện vượt quá cửa sổ ngữ cảnh do độ phân giải mặc định cao hơn, bạn nên giảm rõ ràng độ phân giải của nội dung nghe nhìn.
- **Phân đoạn hình ảnh:** Gemini 3 Pro hoặc Gemini 3 Flash không hỗ trợ các chức năng phân đoạn hình ảnh (trả về mặt nạ ở cấp độ pixel cho các đối tượng). Đối với những khối lượng công việc yêu cầu tính năng phân đoạn hình ảnh tích hợp, bạn nên tiếp tục sử dụng Gemini 2.5 Flash khi tắt chế độ tư duy hoặc [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi).
- **Sử dụng máy tính:** Gemini 3 Pro và Gemini 3 Flash hỗ trợ tính năng [Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi). Không giống như dòng 2.5, bạn không cần sử dụng một mô hình riêng để truy cập vào công cụ Sử dụng máy tính.
- **Hỗ trợ công cụ**: [Các mô hình Gemini 3 hiện hỗ trợ việc kết hợp các công cụ tích hợp với tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi). [Tính năng cơ sở dữ liệu trên Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) hiện cũng được hỗ trợ cho các mô hình Gemini 3.

## Khả năng tương thích với OpenAI

Đối với những người dùng sử dụng [lớp tương thích OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi), các tham số tiêu chuẩn (`reasoning_effort` của OpenAI) sẽ tự động được liên kết với các tham số tương đương của Gemini (`thinking_level`).

## Các phương pháp hay nhất để viết câu lệnh

Gemini 3 là một mô hình suy luận, do đó bạn cần thay đổi cách đưa ra câu lệnh.

- **Hướng dẫn chính xác:** Nhập câu lệnh một cách ngắn gọn. Gemini 3 phản hồi tốt nhất khi nhận được chỉ dẫn trực tiếp và rõ ràng. Có thể phân tích quá mức các kỹ thuật thiết kế câu lệnh dài dòng hoặc quá phức tạp được dùng cho các mô hình cũ.
- **Mức độ chi tiết của kết quả:** Theo mặc định, Gemini 3 ít chi tiết hơn và ưu tiên cung cấp câu trả lời trực tiếp, hiệu quả. Nếu trường hợp sử dụng của bạn yêu cầu một nhân cách trò chuyện hoặc "hay chuyện" hơn, bạn phải hướng dẫn rõ ràng cho mô hình trong câu lệnh (ví dụ: "Giải thích điều này với tư cách là một trợ lý thân thiện, hay chuyện").
- **Quản lý bối cảnh:** Khi làm việc với các tập dữ liệu lớn (ví dụ: toàn bộ sách, cơ sở mã hoặc video dài), hãy đặt hướng dẫn hoặc câu hỏi cụ thể của bạn ở cuối câu lệnh, sau bối cảnh dữ liệu. Gắn suy luận của mô hình vào dữ liệu được cung cấp bằng cách bắt đầu câu hỏi bằng một cụm từ như "Dựa trên thông tin trước đó...".

Tìm hiểu thêm về các chiến lược thiết kế câu lệnh trong [hướng dẫn kỹ thuật về câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi).

## Câu hỏi thường gặp

1. **Điểm cắt kiến thức của Gemini 3 là khi nào?** Các mô hình Gemini 3 có điểm cắt kiến thức là tháng 1 năm 2025. Để biết thông tin mới nhất, hãy sử dụng công cụ [Tìm kiếm thông tin cơ sở](https://ai.google.dev/gemini-api/docs/google-search?hl=vi).
2. **Hạn mức cửa sổ ngữ cảnh là bao nhiêu?** Các mô hình Gemini 3 hỗ trợ cửa sổ ngữ cảnh đầu vào 1 triệu token và đầu ra lên đến 64.000 token.
3. **Gemini 3 có phiên bản miễn phí không?** Gemini 3 Flash
   `gemini-3-flash-preview` có một cấp miễn phí trong Gemini API. Bạn có thể dùng thử Gemini 3.1 Pro và 3 Flash miễn phí trong Google AI Studio, nhưng không có cấp miễn phí cho `gemini-3.1-pro-preview` trong Gemini API.
4. **Mã `thinking_budget` cũ của tôi có còn hoạt động không?** Có, `thinking_budget` vẫn được hỗ trợ để tương thích ngược, nhưng bạn nên di chuyển sang `thinking_level` để có hiệu suất dễ dự đoán hơn. Đừng sử dụng cả hai trong cùng một yêu cầu.
5. **Gemini 3 có hỗ trợ Batch API không?** Có, Gemini 3 hỗ trợ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi).
6. **Context Caching có được hỗ trợ không?** Có, Gemini 3 có hỗ trợ tính năng [Lưu trữ bối cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi).
7. **Gemini 3 hỗ trợ những công cụ nào?** Gemini 3 hỗ trợ [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi), [Kết nối với Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi), [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi), [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi). Công cụ này cũng hỗ trợ [Tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) tiêu chuẩn cho các công cụ tuỳ chỉnh của riêng bạn và [kết hợp với các công cụ tích hợp sẵn](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).
8. **`gemini-3.1-pro-preview-customtools` là gì?** Nếu bạn đang sử dụng `gemini-3.1-pro-preview` và mô hình này bỏ qua các công cụ tuỳ chỉnh của bạn để ưu tiên các lệnh bash, hãy thử mô hình `gemini-3.1-pro-preview-customtools`.
   Xem thêm thông tin [tại đây][customtools-model].

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
