---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi
fetched_at: 2026-11-02T07:18:31.915442+00:00
title: "Hi\u1ec3u h\u00ecnh \u1ea3nh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hiểu hình ảnh

Các mô hình Gemini được xây dựng từ đầu theo hướng đa phương thức, mở ra nhiều nhiệm vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc tạo chú thích cho hình ảnh, phân loại và trả lời câu hỏi bằng hình ảnh mà không cần phải huấn luyện các mô hình học máy chuyên biệt.

Ngoài các khả năng đa phương thức chung, các mô hình Gemini còn mang đến **độ chính xác cao hơn** cho các trường hợp sử dụng cụ thể như [phát hiện đối tượng](#object-detection) và [phân đoạn](#segmentation) thông qua quá trình huấn luyện bổ sung.

## Truyền hình ảnh cho Gemini

Bạn có thể cung cấp hình ảnh làm dữ liệu đầu vào cho Gemini bằng một số phương thức:

- [Truyền hình ảnh bằng URL](#url-image): Phù hợp với những hình ảnh có thể truy cập công khai.
- [Truyền dữ liệu hình ảnh cùng dòng](#inline-image): Đối với dữ liệu hình ảnh được mã hoá base64.
- [Tải hình ảnh lên bằng File API](#upload-image): Nên dùng cho các tệp lớn hơn hoặc để dùng lại hình ảnh trong nhiều yêu cầu.

### Truyền hình ảnh bằng URL

Bạn có thể tải hình ảnh lên bằng [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi) và truyền hình ảnh đó trong yêu cầu:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/organ.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

Content textContent = TextContent.builder().text("Caption this image.").build();
Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/organ.jpg", &genai.UploadFileConfig{
        MIMEType: "image/jpeg",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Caption this image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
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
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/small-sample.jpg"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Client client = new Client();

Content textContent = TextContent.builder().text("Caption this image.").build();
Content imageContent =
    ImageContent.builder()
        .data(base64Image)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    imageBytes, err := os.ReadFile("path/to/small-sample.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Caption this image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
    "model": "gemini-3.8-flash",
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

Đối với các tệp lớn hoặc để có thể sử dụng cùng một tệp hình ảnh nhiều lần, hãy sử dụng Files API. Hãy xem [hướng dẫn về Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
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
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

Content textContent = TextContent.builder().text("Caption this image.").build();
Content imageContent =
    ImageContent.builder()
        .uri(myFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(myFile.mimeType().orElse("image/jpeg")))
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", &genai.UploadFileConfig{
        MIMEType: "image/jpeg",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Caption this image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(myFile.URI),
                    MimeType: interactions.ImageContentMimeType(myFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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
    model="gemini-3.8-flash",
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
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
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
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("What is different between these two images?").build();
Content image1 =
    ImageContent.builder()
        .uri("https://example.com/image1.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();
Content image2 =
    ImageContent.builder()
        .uri("https://example.com/image2.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, image1, image2);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "What is different between these two images?",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr("https://example.com/image1.jpg"),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr("https://example.com/image2.jpg"),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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

## Phát hiện đối tượng

Các mô hình được huấn luyện để phát hiện các đối tượng trong một hình ảnh và lấy toạ độ hộp giới hạn của các đối tượng đó. Toạ độ, tương ứng với kích thước hình ảnh, tỷ lệ thành [0, 1000]. Bạn cần giảm tỷ lệ các toạ độ này dựa trên kích thước hình ảnh gốc.

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
    model="gemini-3.8-flash",
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

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
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
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

Client client = new Client();
String prompt =
    "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

Map<String, Object> boundingBoxSchema =
    Map.of(
        "type", "object",
        "properties",
            Map.of(
                "box_2d",
                    Map.of(
                        "type", "array",
                        "items", Map.of("type", "integer"),
                        "description",
                            "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000."),
                "mask",
                    Map.of(
                        "type", "array",
                        "items", Map.of("type", "array", "items", Map.of("type", "integer")),
                        "description",
                            "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000."),
                "label",
                    Map.of("type", "string", "description", "A descriptive label for the item.")),
        "required", List.of("box_2d", "mask", "label"));

Map<String, Object> boundingBoxesSchema =
    Map.of(
        "type", "object",
        "properties", Map.of("boxes", Map.of("type", "array", "items", boundingBoxSchema)),
        "required", List.of("boxes"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(boundingBoxesSchema)
                .build()));

Content textContent = TextContent.builder().text(prompt).build();
Content imageContent =
    ImageContent.builder()
        .uri("https://example.com/image.png")
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(Arrays.asList(textContent, imageContent)))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    prompt := "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

    boundingBoxSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "box_2d": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "integer"},
                "description": "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.",
            },
            "mask": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "array", "items": map[string]any{"type": "integer"}},
                "description": "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.",
            },
            "label": map[string]any{
                "type":        "string",
                "description": "A descriptive label for the item.",
            },
        },
        "required": []string{"box_2d", "mask", "label"},
    }

    boundingBoxesSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "boxes": map[string]any{
                "type":  "array",
                "items": boundingBoxSchema,
            },
        },
        "required": []string{"boxes"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   boundingBoxesSchema,
        }),
    )

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr("https://example.com/image.png"),
                    MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
                }),
            }),
            ResponseFormat: genai.Ptr(format),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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

Để xem thêm ví dụ, hãy truy cập vào [Gemini Cookbook](https://github.com/google-gemini/cookbook).

## Phân đoạn

Các mô hình Gemini không chỉ phát hiện mà còn phân đoạn các mục và cung cấp mặt nạ đường viền của các mục đó.

Mô hình này dự đoán một danh sách JSON, trong đó mỗi mục đại diện cho một mặt nạ phân đoạn. Mỗi mục đều có một khung hình chữ nhật ("`box_2d`") ở định dạng `[ymin, xmin, ymax, xmax]` với các toạ độ được chuẩn hoá từ 0 đến 1000, một nhãn ("`label`") xác định đối tượng và cuối cùng là mặt nạ phân đoạn bên trong khung hình chữ nhật dưới dạng một đa giác gồm các toạ độ `[x, y]` được chuẩn hoá thành 0-1000.

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
    model="gemini-3.8-flash",
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
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
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

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
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
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

Client client = new Client();

String prompt =
    "Give the segmentation masks for the wooden and glass items.\n"
        + "Output a JSON list of segmentation masks where each entry contains the 2D\n"
        + "bounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\n"
        + "the text label in the key \"label\". Use descriptive labels.";

Map<String, Object> boundingBoxSchema =
    Map.of(
        "type", "object",
        "properties",
            Map.of(
                "box_2d",
                    Map.of(
                        "type", "array",
                        "items", Map.of("type", "integer"),
                        "description",
                            "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000."),
                "mask",
                    Map.of(
                        "type", "array",
                        "items", Map.of("type", "array", "items", Map.of("type", "integer")),
                        "description",
                            "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000."),
                "label",
                    Map.of("type", "string", "description", "A descriptive label for the item.")),
        "required", List.of("box_2d", "mask", "label"));

Map<String, Object> boundingBoxesSchema =
    Map.of(
        "type", "object",
        "properties", Map.of("boxes", Map.of("type", "array", "items", boundingBoxSchema)),
        "required", List.of("boxes"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(boundingBoxesSchema)
                .build()));

Content textContent = TextContent.builder().text(prompt).build();
Content imageContent =
    ImageContent.builder()
        .uri("https://example.com/image.png")
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(Arrays.asList(textContent, imageContent)))
        .responseFormat(format)
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.MINIMAL).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Segmentation results: " + interaction.outputText().orElse(""));
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

    prompt := "Give the segmentation masks for the wooden and glass items.\n" +
        "Output a JSON list of segmentation masks where each entry contains the 2D\n" +
        "bounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\n" +
        "the text label in the key \"label\". Use descriptive labels."

    boundingBoxSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "box_2d": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "integer"},
                "description": "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.",
            },
            "mask": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "array", "items": map[string]any{"type": "integer"}},
                "description": "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.",
            },
            "label": map[string]any{
                "type":        "string",
                "description": "A descriptive label for the item.",
            },
        },
        "required": []string{"box_2d", "mask", "label"},
    }

    boundingBoxesSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "boxes": map[string]any{
                "type":  "array",
                "items": boundingBoxSchema,
            },
        },
        "required": []string{"boxes"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   boundingBoxesSchema,
        }),
    )

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr("https://example.com/image.png"),
                    MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
                }),
            }),
            ResponseFormat: genai.Ptr(format),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelMinimal.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println("Segmentation results: " + *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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
    "generation_config": {
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

Để tìm hiểu về các phương thức nhập tệp khác, hãy xem hướng dẫn [Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

## Tính năng

Tất cả các phiên bản mô hình Gemini đều là mô hình đa phương thức và có thể được sử dụng trong nhiều nhiệm vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc tạo chú thích cho hình ảnh, trả lời câu hỏi bằng hình ảnh, phân loại hình ảnh, phát hiện đối tượng và phân đoạn đối tượng.

Gemini có thể giảm nhu cầu sử dụng các mô hình học máy chuyên biệt, tuỳ thuộc vào yêu cầu về chất lượng và hiệu suất của bạn.

Các phiên bản mô hình mới nhất được huấn luyện đặc biệt để cải thiện độ chính xác của các tác vụ chuyên biệt ngoài các chức năng chung, chẳng hạn như tính năng [phát hiện đối tượng](#object-detection) và [phân đoạn](#segmentation) nâng cao.

## Các hạn chế và thông tin kỹ thuật chính

### Giới hạn về tệp

Các mô hình Gemini hỗ trợ tối đa 3.600 tệp hình ảnh cho mỗi yêu cầu.

### Cách tính mã thông báo

- 258 mã thông báo nếu cả hai chiều đều <= 384 pixel.
  Các hình ảnh lớn hơn được chia thành các ô có kích thước 768x768 pixel, mỗi ô có giá 258 mã thông báo.

Công thức sơ bộ để tính số lượng ô như sau:

- Tính kích thước đơn vị cắt xén, xấp xỉ bằng: `floor(min(width, height)` / 1,5).
- Chia từng phương diện cho kích thước đơn vị cắt và nhân với nhau để có số lượng ô.

Ví dụ: đối với hình ảnh có kích thước 960x540, kích thước đơn vị cắt sẽ là 360. Chia mỗi chiều cho 360 và số lượng ô là 3 \* 2 = 6.

### Độ phân giải của nội dung nghe nhìn

Gemini 3 giới thiệu khả năng kiểm soát chi tiết đối với quy trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.**
Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

## Mẹo và phương pháp hay nhất

- Xác minh rằng hình ảnh được xoay đúng cách.
- Sử dụng hình ảnh rõ ràng, không bị mờ.
- Khi sử dụng một hình ảnh có văn bản, hãy đặt câu lệnh dạng văn bản *trước* hình ảnh trong mảng `input`.

## Bước tiếp theo

Hướng dẫn này cho bạn biết cách tải tệp hình ảnh lên và tạo đầu ra văn bản từ đầu vào hình ảnh. Để tìm hiểu thêm, hãy xem các tài nguyên sau:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý tệp để sử dụng với Gemini.
- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions): Hướng dẫn hệ thống giúp bạn điều hướng hành vi của mô hình dựa trên nhu cầu và trường hợp sử dụng cụ thể của bạn.
- [Chiến lược đặt câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide): Gemini API hỗ trợ đặt câu lệnh bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là đặt câu lệnh đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Việc xử lý hậu kỳ và đánh giá của con người là rất cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-24 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-24 UTC."],[],[]]
