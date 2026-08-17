---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=zh-CN
fetched_at: 2026-08-17T02:18:02.758430+00:00
title: "\u56fe\u7247\u7406\u89e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 图片理解

Gemini 模型从一开始就具有多模态特性，可解锁各种图片处理和计算机视觉任务，包括但不限于图片配文、分类和视觉问答，而无需训练专门的机器学习模型。

除了通用的多模态功能外，Gemini 模型还通过额外训练，针对特定使用场景（例如[对象检测](#object-detection)）提供
**更高的准确率**。

## 将图片传递给 Gemini

您可以使用以下两种方法将图片作为输入提供给 Gemini：

- [传递内嵌图片数据](#inline-image)：非常适合较小的文件（总请求
  大小小于 20MB，包括提示）。
- [使用 File API 上传图片](#upload-image)：建议用于较大的文件，或在
  多个请求中重复使用图片。

### 传递内嵌图片数据

您可以在对 `generateContent` 的请求中传递内嵌图片数据。您可以提供 Base64 编码的字符串形式的图片数据，也可以直接读取本地文件（具体取决于语言）。

以下示例展示了如何从本地文件读取图片并将其传递给 `generateContent` API 进行处理。

### Python

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )

  print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile,
    },
  },
  { text: "Caption this image." },
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
bytes, _ := os.ReadFile("path/to/small-sample.jpg")

parts := []*genai.Part{
  genai.NewPartFromBytes(bytes, "image/jpeg"),
  genai.NewPartFromText("Caption this image."),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3.6-flash",
  contents,
  nil,
)

fmt.Println(result.Text())
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
B64FLAGS="--input"
else
B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{
    "parts":[
        {
            "inline_data": {
            "mime_type":"image/jpeg",
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
            }
        },
        {"text": "Caption this image."},
    ]
    }]
}' 2> /dev/null
```

您还可以从网址提取图片，将其转换为字节，然后将其传递给 `generateContent`，如以下示例所示。

### Python

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=["What is this image?", image],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
    {
      inlineData: {
        mimeType: 'image/jpeg',
        data: base64ImageData,
      },
    },
    { text: "Caption this image." }
  ],
  });
  console.log(result.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "io"
  "net/http"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Download the image.
  imageResp, _ := http.Get("https://goo.gle/instrument-img")

  imageBytes, _ := io.ReadAll(imageResp.Body)

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    genai.NewPartFromText("Caption this image."),
  }

  contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.6-flash",
    contents,
    nil,
  )

  fmt.Println(result.Text())
}
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Caption this image."}
        ]
      }]
    }' 2> /dev/null
```

### 使用 File API 上传图片

对于较大的文件，或者为了能够重复使用同一图片文件，请使用 Files API。以下代码会上传图片文件，然后在对 `generateContent` 的调用中使用该文件。如需了解
更多信息和示例，请参阅[Files API 指南](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)。

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Caption this image.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

  parts := []*genai.Part{
      genai.NewPartFromText("Caption this image."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
IMAGE_PATH="path/to/sample.jpg"
MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
DISPLAY_NAME=IMAGE

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Caption this image."}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## 使用多张图片进行提示

您可以在单个提示中提供多张图片，方法是在 `contents` 数组中添加多个图片 `Part` 对象。这些对象可以是内嵌数据（本地文件或网址）和 File API 引用的组合。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-3.6-flash",
    contents=[
        "What is different between these two images?",
        uploaded_file,  # Use the uploaded file reference
        types.Part.from_bytes(
            data=img2_bytes,
            mime_type='image/png'
        )
    ]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  // Upload the first image
  const image1_path = "path/to/image1.jpg";
  const uploadedFile = await ai.files.upload({
    file: image1_path,
    config: { mimeType: "image/jpeg" },
  });

  // Prepare the second image as inline data
  const image2_path = "path/to/image2.png";
  const base64Image2File = fs.readFileSync(image2_path, {
    encoding: "base64",
  });

  // Create the prompt with text and multiple images

  const response = await ai.models.generateContent({

    model: "gemini-3.6-flash",
    contents: createUserContent([
      "What is different between these two images?",
      createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),
      {
        inlineData: {
          mimeType: "image/png",
          data: base64Image2File,
        },
      },
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
// Upload the first image
image1Path := "path/to/image1.jpg"
uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

// Prepare the second image as inline data
image2Path := "path/to/image2.jpeg"
imgBytes, _ := os.ReadFile(image2Path)

parts := []*genai.Part{
  genai.NewPartFromText("What is different between these two images?"),
  genai.NewPartFromBytes(imgBytes, "image/jpeg"),
  genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3.6-flash",
  contents,
  nil,
)

fmt.Println(result.Text())
```

### REST

```
# Upload the first image
IMAGE1_PATH="path/to/image1.jpg"
MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
DISPLAY_NAME1=IMAGE1

tmp_header_file1=upload-header1.tmp

curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header1.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file1}"

curl "${upload_url1}" \
  -H "Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

file1_uri=$(jq ".file.uri" file_info1.json)
echo file1_uri=$file1_uri

# Prepare the second image (inline)
IMAGE2_PATH="path/to/image2.png"
MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi
IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

# Now generate content using both images
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "What is different between these two images?"},
          {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},
          {
            "inline_data": {
              "mime_type":"'"${MIME2_TYPE}"'",
              "data": "'"$IMAGE2_BASE64"'"
            }
          }
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## 对象检测

模型经过训练，可以检测图片中的对象并获取其边界框坐标。相对于图片尺寸的坐标会缩放为 [0, 1000]。您需要根据原始图片大小对这些坐标进行反缩放。

### Python

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3.6-flash",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("/path/to/image.png", {
  encoding: "base64",
});

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: [
    {
      inlineData: {
        mimeType: "image/png",
        data: base64ImageFile,
      },
    },
    "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."
  ],
  config: {
    responseMimeType: "application/json",
  },
});

const boundingBoxes = JSON.parse(response.text);
console.log(boundingBoxes);
// To convert normalized coordinates to absolute pixels:
// const absY1 = (boundingBoxes[0].box_2d[0] / 1000) * imageHeight;
// const absX1 = (boundingBoxes[0].box_2d[1] / 1000) * imageWidth;
```

### Go

```
package main

import (
  "context"
  "encoding/json"
  "fmt"
  "image"
  _ "image/png" // Register PNG decoder
  "log"
  "os"

  "google.golang.org/genai"
)

type BoundingBox struct {
  Box2D []int  `json:"box_2d"`
  Label string `json:"label"`
}

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
    log.Fatal(err)
  }

  imagePath := "/path/to/image.png"

  // Open the image to get dimensions
  file, err := os.Open(imagePath)
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()

  imgConfig, _, err := image.DecodeConfig(file)
  if err != nil {
    log.Fatal(err)
  }
  width := imgConfig.Width
  height := imgConfig.Height

  // Read image bytes
  imageBytes, err := os.ReadFile(imagePath)
  if err != nil {
    log.Fatal(err)
  }

  prompt := "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/png"),
    genai.NewPartFromText(prompt),
  }

  contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
  }

  config := &genai.GenerateContentConfig{
    ResponseMIMEType: "application/json",
  }

  result, err := client.Models.GenerateContent(
    ctx,
    "gemini-3.6-flash",
    contents,
    config,
  )
  if err != nil {
    log.Fatal(err)
  }

  var boundingBoxes []BoundingBox
  err = json.Unmarshal([]byte(result.Text()), &boundingBoxes)
  if err != nil {
    log.Fatal(err)
  }

  fmt.Printf("Image size: %d %d\n", width, height)
  fmt.Println("Bounding boxes:")
  for _, box := range boundingBoxes {
    if len(box.Box2D) == 4 {
      absY1 := int(float64(box.Box2D[0]) / 1000.0 * float64(height))
      absX1 := int(float64(box.Box2D[1]) / 1000.0 * float64(width))
      absY2 := int(float64(box.Box2D[2]) / 1000.0 * float64(height))
      absX2 := int(float64(box.Box2D[3]) / 1000.0 * float64(width))
      fmt.Printf("- %s: [%d, %d, %d, %d]\n", box.Label, absX1, absY1, absX2, absY2)
    }
  }
}
```

### REST

```
IMG_PATH="/path/to/image.png"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts":[
        {
          "inline_data": {
            "mime_type":"image/png",
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
          }
        },
        {"text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."}
      ]
    }],
    "generationConfig": {
      "responseMimeType": "application/json"
    }
  }' 2> /dev/null
```

如需查看更多示例，请查看 [Gemini Cookbook](https://github.com/google-gemini/cookbook) 中的以下笔记本：

- [2D 空间理解笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=zh-cn)
- [实验性 3D 指向笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=zh-cn)

## 支持的图片格式

Gemini 支持以下图片格式 MIME 类型：

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

如需了解其他文件输入方法，请参阅
[文件输入方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn)指南。

## 功能

所有 Gemini 模型版本都是多模态的，可用于各种图片处理和计算机视觉任务，包括但不限于图片配文、视觉问答、图片分类和对象检测。

Gemini 可以减少对专用机器学习模型的需求，具体取决于您的质量和性能要求。

除了通用功能（例如增强的
[对象检测](#object-detection)）之外，最新模型版本还经过专门训练，可提高
专用任务的准确率。

## 限制和关键技术信息

### 文件限制

Gemini 模型每个请求最多支持 3,600 个图片文件。

### token 计算

- 如果两个尺寸均小于或等于 384 像素，则为 258 个 token。
  较大的图片会平铺到 768x768 像素的图块中，每个图块需要 258 个 token。

计算图块数量的粗略公式如下：

- 计算裁剪单元大小，大致为：floor(min(width, height) / 1.5)。
- 将每个尺寸除以裁剪单元大小，然后将结果相乘，即可得到图块数量。

例如，对于尺寸为 960x540 的图片，裁剪单元大小为 360。将每个尺寸除以 360，得到的图块数量为 3 \* 2 = 6。

### 媒体分辨率

Gemini 3 引入了对多模态视觉处理的精细控制，通过 `media_resolution` 参数实现。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限** 。分辨率越高，模型读取精细文本或识别细小细节的能力就越强，但 token 用量和延迟也会增加。

如需详细了解该参数及其对 token 计算的影响，
请参阅[媒体分辨率](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-cn)指南。

## 技巧和最佳做法

- 验证图片是否正确旋转。
- 使用清晰、不模糊的图片。
- 如果使用包含文本的单张图片，请在 `contents` 数组中将文本提示放在图片部分之后。

## 后续步骤

本指南介绍了如何上传图片文件并根据图片输入生成文本输出。如需了解详情，请参阅以下资源：

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)：详细了解如何上传和管理文件以供 Gemini 使用。
- [系统说明](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#system-instructions)：
  系统说明可让您根据
  特定需求和使用情形来控制模型的行为。
- [文件提示策略](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn#prompt-guide)：
  Gemini API 支持使用文本、图片、音频和视频数据进行提示，也
  称为多模态提示。
- [安全指南](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-cn)：生成式
  AI 模型有时会产生意外输出，例如不准确、
  有偏见或令人反感的输出。后处理和人工评估对于限制此类输出造成的危害风险至关重要。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
