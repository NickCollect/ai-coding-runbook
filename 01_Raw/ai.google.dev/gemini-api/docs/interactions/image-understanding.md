---
source_url: https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=vi
fetched_at: 2026-05-11T05:08:01.875965+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hiểu hình ảnh

Các mô hình Gemini được xây dựng từ đầu theo hướng đa phương thức, mở ra nhiều nhiệm vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc chú thích hình ảnh, phân loại và trả lời câu hỏi bằng hình ảnh mà không cần phải huấn luyện các mô hình học máy chuyên biệt.

Ngoài các khả năng đa phương thức chung, các mô hình Gemini còn mang đến **độ chính xác cao hơn** cho các trường hợp sử dụng cụ thể như [phát hiện đối tượng](#object-detection) và [phân đoạn](#segmentation), thông qua quá trình huấn luyện bổ sung.

## Truyền hình ảnh cho Gemini

Bạn có thể cung cấp hình ảnh làm dữ liệu đầu vào cho Gemini bằng một số phương thức:

- [Truyền hình ảnh bằng URL](#url-image): Phù hợp với những hình ảnh có thể truy cập công khai.
- [Truyền dữ liệu hình ảnh cùng dòng](#inline-image): Đối với dữ liệu hình ảnh được mã hoá base64.
- [Tải hình ảnh lên bằng File API](#upload-image): Nên dùng cho các tệp lớn hơn hoặc để dùng lại hình ảnh trong nhiều yêu cầu.

### Truyền hình ảnh bằng URL

Bạn có thể tải hình ảnh lên bằng [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi) và truyền hình ảnh đó trong yêu cầu:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mime_type: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Truyền dữ liệu hình ảnh cùng dòng

Bạn có thể cung cấp dữ liệu hình ảnh dưới dạng chuỗi được mã hoá base64:

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Tải hình ảnh lên bằng File API

Đối với các tệp lớn hoặc để có thể sử dụng cùng một tệp hình ảnh nhiều lần, hãy sử dụng Files API. Hãy xem [hướng dẫn về Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Đưa ra câu lệnh bằng nhiều hình ảnh

Bạn có thể cung cấp nhiều hình ảnh trong một câu lệnh bằng cách đưa nhiều đối tượng hình ảnh vào mảng `input`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Phát hiện vật thể

Các mô hình được huấn luyện để phát hiện các đối tượng trong một hình ảnh và lấy toạ độ hộp giới hạn của các đối tượng đó. Toạ độ, so với kích thước hình ảnh, tỷ lệ thành [0, 1000]. Bạn cần giảm tỷ lệ các toạ độ này dựa trên kích thước hình ảnh gốc.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.steps[-1].content[0].text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesJsonSchema = {
  type: "object",
  properties: {
    boxes: {
      type: "array",
      items: {
        type: "object",
        properties: {
          box_2d: { type: "array", items: { type: "integer" }, description: "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000." },
          mask: { type: "array", items: { type: "array", items: { type: "integer" } }, description: "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000." },
          label: { type: "string", description: "A descriptive label for the item." }
        },
        required: ["box_2d", "mask", "label"]
      }
    }
  },
  required: ["boxes"]
};

const boundingBoxesSchema = z.fromJSONSchema(boundingBoxesJsonSchema);

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: boundingBoxesJsonSchema
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

Để xem thêm ví dụ, hãy xem các sổ ghi chú sau trong [Gemini Cookbook](https://github.com/google-gemini/cookbook):

## Phân đoạn

Bắt đầu từ Gemini 2.5, các mô hình không chỉ phát hiện mà còn phân đoạn các mục và cung cấp mặt nạ đường viền của các mục đó.

Mô hình này dự đoán một danh sách JSON, trong đó mỗi mục đại diện cho một mặt nạ phân đoạn.
Mỗi mục đều có một khung hình chữ nhật ("`box_2d`") ở định dạng `[y0, x0, y1, x1]` với các toạ độ được chuẩn hoá từ 0 đến 1000, một nhãn ("`label`") xác định đối tượng và cuối cùng là mặt nạ phân đoạn bên trong khung hình chữ nhật, dưới dạng png được mã hoá base64 là bản đồ xác suất có giá trị từ 0 đến 255.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"  # Minimize thinking for better detection results
    }
)

items = BoundingBoxes.model_validate_json(interaction.steps[-1].content[0].text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesJsonSchema = {
  type: "object",
  properties: {
    boxes: {
      type: "array",
      items: {
        type: "object",
        properties: {
          box_2d: { type: "array", items: { type: "integer" }, description: "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000." },
          mask: { type: "array", items: { type: "array", items: { type: "integer" } }, description: "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000." },
          label: { type: "string", description: "A descriptive label for the item." }
        },
        required: ["box_2d", "mask", "label"]
      }
    }
  },
  required: ["boxes"]
};

const boundingBoxesSchema = z.fromJSONSchema(boundingBoxesJsonSchema);

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: boundingBoxesJsonSchema
  },
  generationConfig: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "config": {
      "thinking_level": "minimal"
    }
  }'
```

![Một chiếc bàn có bánh cupcake, trong đó các vật dụng bằng gỗ và thuỷ tinh được làm nổi bật](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=vi)

Ví dụ về kết quả phân đoạn có các đối tượng và mặt nạ phân đoạn

## Định dạng hình ảnh được hỗ trợ

Gemini hỗ trợ các loại MIME sau đây cho định dạng hình ảnh:

- PNG – `image/png`
- JPEG – `image/jpeg`
- WEBP – `image/webp`
- HEIC – `image/heic`
- HEIF – `image/heif`

Để tìm hiểu về các phương thức nhập tệp khác, hãy xem hướng dẫn [Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=vi).

## Tính năng

Tất cả các phiên bản mô hình Gemini đều là mô hình đa phương thức và có thể được sử dụng trong nhiều tác vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc chú thích hình ảnh, trả lời câu hỏi bằng hình ảnh, phân loại hình ảnh, phát hiện và phân đoạn đối tượng.

Gemini có thể giảm nhu cầu sử dụng các mô hình học máy chuyên biệt, tuỳ thuộc vào yêu cầu về chất lượng và hiệu suất của bạn.

Các phiên bản mô hình mới nhất được huấn luyện đặc biệt để cải thiện độ chính xác của các tác vụ chuyên biệt ngoài các chức năng chung, chẳng hạn như tính năng [phát hiện đối tượng](#object-detection) và [phân đoạn](#segmentation) nâng cao.

## Hạn chế và thông tin kỹ thuật chính

### Giới hạn về tệp

Các mô hình Gemini hỗ trợ tối đa 3.600 tệp hình ảnh cho mỗi yêu cầu.

### Cách tính toán mã thông báo

- 258 mã thông báo nếu cả hai chiều đều <= 384 pixel.
  Các hình ảnh lớn hơn được chia thành các ô có kích thước 768x768 pixel, mỗi ô có giá 258 mã thông báo.

Công thức sơ bộ để tính số lượng ô như sau:

- Tính kích thước đơn vị cắt, xấp xỉ bằng: `floor(min(width, height)` / 1,5).
- Chia từng chiều cho kích thước đơn vị cắt và nhân với nhau để có số lượng ô.

Ví dụ: đối với hình ảnh có kích thước 960x540, kích thước đơn vị cắt sẽ là 360. Chia mỗi chiều cho 360 và số lượng ô là 3 \* 2 = 6.

### Độ phân giải của nội dung nghe nhìn

Gemini 3 giới thiệu chế độ kiểm soát chi tiết đối với quy trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.**
Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

## Mẹo và phương pháp hay nhất

- Xác minh rằng hình ảnh được xoay đúng cách.
- Sử dụng hình ảnh rõ ràng, không bị mờ.
- Khi dùng một hình ảnh có văn bản, hãy đặt câu lệnh dạng văn bản *trước* hình ảnh trong mảng `input`.

## Bước tiếp theo

Hướng dẫn này cho bạn biết cách tải tệp hình ảnh lên và tạo đầu ra văn bản từ đầu vào hình ảnh. Để tìm hiểu thêm, hãy xem các tài nguyên sau:

- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý tệp để sử dụng với Gemini.
- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi#system-instructions): Hướng dẫn hệ thống giúp bạn điều hướng hành vi của mô hình dựa trên nhu cầu và trường hợp sử dụng cụ thể của bạn.
- [Chiến lược đặt câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi#prompt-guide): Gemini API hỗ trợ đặt câu lệnh bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là đặt câu lệnh đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Hậu xử lý và đánh giá của con người là những bước cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-09 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-09 UTC."],[],[]]
