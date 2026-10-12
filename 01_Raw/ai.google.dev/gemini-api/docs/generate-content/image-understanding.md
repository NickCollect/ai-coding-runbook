---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=bn
fetched_at: 2026-10-12T06:53:32.327998+00:00
title: "\u099b\u09ac\u09bf \u09ac\u09cb\u099d\u09be \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

জেমিনি ৩.৮ ফ্ল্যাশ এখন পাওয়া যাচ্ছে। [ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=bn) ।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# ছবি বোঝা

Gemini মডেলকে একেবারে গোড়া থেকে মাল্টিমোডাল হিসেবে তৈরি করা হয়েছে, এর ফলে ছবি প্রসেসিং ও কম্পিউটার ভিশন সংক্রান্ত বিভিন্ন ধরনের টাস্ক আনলক করা যায়। এর মধ্যে রয়েছে, তবে এগুলিই শেষ নয়, বিশেষ ML মডেলকে ট্রেনিং না দিয়েই
ছবি ক্যাপশন করা, শ্রেণীবদ্ধ করা এবং ভিজ্যুয়াল প্রশ্নের উত্তর দেওয়া।

সাধারণ মাল্টিমোডাল ক্ষমতা ছাড়াও, Gemini মডেল অতিরিক্ত ট্রেনিংয়ের মাধ্যমে
[অবজেক্ট শনাক্তকরণ](#object-detection)-এর মতো নির্দিষ্ট ব্যবহারের ক্ষেত্রে
**উন্নত নির্ভুলতা** প্রদান করে।

## Gemini-তে ছবি পাস করা

দুটি পদ্ধতি ব্যবহার করে আপনি Gemini-তে ইনপুট হিসেবে ছবি দিতে পারবেন:

- [ইনলাইন ইমেজ ডেটা পাস করা](#inline-image): ছোট ফাইলের জন্য আদর্শ (মোট অনুরোধ
  সাইজ ২০ এমবির কম, প্রম্পট সহ)।
- [File API ব্যবহার করে ছবি আপলোড করা](#upload-image): বড় ফাইল বা একাধিক অনুরোধ জুড়ে ছবি
  পুনর্ব্যবহার করার জন্য সাজেস্ট করা হয়।

### ইনলাইন ছবির ডেটা পাস করা

আপনি `generateContent`-এ
অনুরোধে ইনলাইন ইমেজ ডেটা পাস করতে পারবেন। আপনি Base64 এনকোড করা
স্ট্রিং হিসেবে অথবা সরাসরি লোকাল ফাইল রিড করার মাধ্যমে (ভাষার উপর নির্ভর করে) ইমেজ ডেটা প্রদান করতে পারেন।

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে লোকাল ফাইল থেকে কোনও ছবি পড়তে হয় এবং প্রসেসিংয়ের জন্য
`generateContent` API-তে পাঠাতে হয়।

### Python

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3.8-flash',
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

### জাভাস্ক্রিপ্ট

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
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### খুলুন

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
  "gemini-3.8-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

এছাড়াও, আপনি কোনও URL থেকে ছবি আনতে, এটিকে বাইটে কনভার্ট করতে এবং নিম্নলিখিত উদাহরণে দেখানো
`generateContent` হিসেবে পাস করতে পারবেন।

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
    model="gemini-3.8-flash",
    contents=["What is this image?", image],
)

print(response.text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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

### খুলুন

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
    "gemini-3.8-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

### File API ব্যবহার করে ছবি আপলোড করা

বড় ফাইল বা একই ইমেজ ফাইল বারবার ব্যবহার করার জন্য, Files API ব্যবহার করুন। নিচে দেওয়া কোডটি একটি ছবির ফাইল আপলোড করে এবং তারপরে `generateContent`-এ কল করার জন্য ফাইলটি ব্যবহার করে।
আরও তথ্য ও উদাহরণ পেতে, [Files API গাইড](https://ai.google.dev/gemini-api/docs/files?hl=bn) দেখুন।

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

### জাভাস্ক্রিপ্ট

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
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Caption this image.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### খুলুন

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
      "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## একাধিক ছবি সহ প্রম্পট করা

আপনি `contents` অ্যারেতে একাধিক ছবি
`Part` অবজেক্ট যোগ করে একটি প্রম্পটে একাধিক ছবি প্রদান করতে পারেন। এগুলি ইনলাইন ডেটা
(স্থানীয় ফাইল বা URL) ও ফাইল API রেফারেন্সের মিশ্রণ হতে পারে।

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

    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

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

    model: "gemini-3.8-flash",
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

### খুলুন

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
  "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## অবজেক্ট ডিটেকশন

কোনও
ছবির মধ্যে থাকা অবজেক্ট শনাক্ত করতে এবং সেটির বাউন্ডিং বক্স কোঅর্ডিনেট পেতে মডেলগুলিকে প্রশিক্ষণ দেওয়া হয়। ছবির
ডাইমেনশনের সাপেক্ষে কোঅর্ডিনেট, [০, ১০০০] স্কেলে থাকে। আপনার আসল ছবির সাইজের উপর ভিত্তি করে
এইসব কোঅর্ডিনেটকে ডিস্কেল করতে হবে।

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

response = client.models.generate_content(model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("/path/to/image.png", {
  encoding: "base64",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
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

### খুলুন

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
    "gemini-3.8-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

আরও উদাহরণের জন্য, [Gemini Cookbook](https://github.com/google-gemini/cookbook)-এ নিম্নলিখিত নোটবুক দেখুন:

- [2D স্পেশিয়াল আন্ডারস্ট্যান্ডিং নোটবুক](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=bn)
- [পরীক্ষামূলক 3D পয়েন্টিং নোটবুক](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=bn)

## কাজ করে এমন ছবির ফর্ম্যাট

Gemini-তে নিম্নলিখিত ছবির ফর্ম্যাট MIME ধরন কাজ করে:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

অন্যান্য ফাইল ইনপুট পদ্ধতি সম্পর্কে জানতে, [ফাইল ইনপুট পদ্ধতি](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=bn) নির্দেশিকা দেখুন।

## কেপেবিলিটি

Gemini মডেলের সব ভার্সনই মাল্টিমোডাল এবং এগুলি ছবি প্রসেসিং ও কম্পিউটার ভিশন সংক্রান্ত বিভিন্ন ধরনের টাস্কে ব্যবহার করা যেতে পারে। এর মধ্যে রয়েছে, ছবি ক্যাপশন করা, ভিজ্যুয়াল প্রশ্ন ও উত্তর, ছবি শ্রেণীবদ্ধ করা এবং অবজেক্ট শনাক্ত করা।

আপনার কোয়ালিটি ও পারফর্ম্যান্স সংক্রান্ত প্রয়োজনীয়তার উপর নির্ভর করে Gemini বিশেষ ML মডেল ব্যবহারের প্রয়োজনীয়তা কমাতে পারে।

লেটেস্ট মডেল ভার্সনগুলি সাধারণ ক্ষমতা ছাড়াও বিশেষ বিশেষ টাস্কের নির্ভুলতা উন্নত করার জন্য বিশেষভাবে ট্রেনিংপ্রাপ্ত, যেমন উন্নত
[অবজেক্ট শনাক্তকরণ](#object-detection)।

## সীমাবদ্ধতা ও মূল টেকনিক্যাল তথ্য

### ফাইলের সীমা

Gemini মডেল,প্রতিটি অনুরোধে সর্বাধিক ৩৬০০টি ইমেজ ফাইল সাপোর্ট করে।

### টোকেন গণনা

- দুটি ডাইমেনশনই <= ৩৮৪ পিক্সেল হলে ২৫৮টি টোকেন।
  বড় ছবিগুলিকে ৭৬৮x৭৬৮ পিক্সেল টাইলসে ভাগ করা হয়, প্রতিটি টাইলসের জন্য ২৫৮টি টোকেন খরচ হয়।

টাইলের সংখ্যা গণনা করার জন্য একটি মোটামুটি ফর্মুলা নিচে দেওয়া হল:

- ক্রপ ইউনিট সাইজ গণনা করুন, যা মোটামুটি এইরকম হয়: floor(min(width, height) / 1.5).
- প্রতিটি ডাইমেনশনকে ক্রপ ইউনিট সাইজ দিয়ে ভাগ করুন এবং একসাথে গুণ করে টাইলের
  সংখ্যা পান।

যেমন, ৯৬০x৫৪০ ডাইমেনশনের ছবির জন্য ক্রপ ইউনিট সাইজ
৩৬০ হবে। প্রতিটি ডাইমেনশনকে ৩৬০ দিয়ে ভাগ করুন এবং টাইলের সংখ্যা হল ৩ \* ২ = ৬।

### মিডিয়ার রেজোলিউশন

Gemini 3,
`media_resolution` প্যারামিটারের মাধ্যমে মাল্টিমোডাল ভিশন প্রসেসিংয়ের উপর গ্র্যানুলার কন্ট্রোল প্রদান করে। `media_resolution` প্যারামিটার
**প্রতিটি ইনপুট ছবি বা ভিডিও ফ্রেমে বরাদ্দ করা টোকেনের সর্বাধিক সংখ্যা** নির্ধারণ করে।
আরও বেশি রেজোলিউশন থাকলে, মডেলের
ছোট টেক্সট পড়া বা ছোট ছোট বিবরণ শনাক্ত করার ক্ষমতা উন্নত হয়, তবে টোকেন ব্যবহার ও লেটেন্সি বেড়ে যায়।

প্যারামিটার ও টোকেন গণনার উপর এর প্রভাব সম্পর্কে আরও জানতে,
[মিডিয়া রেজোলিউশন](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=bn) নির্দেশিকা দেখুন।

## পরামর্শ ও পেশাদার পদ্ধতি

- ছবিগুলি সঠিকভাবে রোটেট করা হয়েছে কিনা তা যাচাই করুন।
- স্পষ্ট, অস্পষ্ট নয় এমন ছবি ব্যবহার করুন।
- টেক্সট সহ একটি ছবি ব্যবহার করার সময়, `contents` অ্যারের মধ্যে ছবির অংশের *পরে* টেক্সট প্রম্পটটি রাখুন।

## এর পরে কী করতে হবে

এই গাইড আপনাকে দেখায় কীভাবে ইমেজ ফাইল আপলোড করতে হয় এবং ইমেজ
ইনপুট থেকে টেক্সট আউটপুট জেনারেট করতে হয়। আরও জানতে, নিম্নলিখিত রিসোর্স দেখুন:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn): Gemini-তে ব্যবহারের জন্য ফাইল আপলোড ও ম্যানেজ করা সম্পর্কে আরও জানুন।
- [সিস্টেম নির্দেশাবলী](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn#system-instructions):
  সিস্টেম নির্দেশাবলী আপনাকে নিজের
  নির্দিষ্ট প্রয়োজন ও ব্যবহারের ক্ষেত্রে মডেলের আচরণ নিয়ন্ত্রণ করতে দেয়।
- [ফাইল প্রম্পটিং স্ট্র্যাটেজি](https://ai.google.dev/gemini-api/docs/files?hl=bn#prompt-guide): Gemini API
  টেক্সট, ছবি, অডিও ও ভিডিও ডেটা সহ প্রম্পটিং কাজ করে। এটি
  মাল্টিমোডাল প্রম্পটিং নামেও পরিচিত।
- [নিরাপত্তা সংক্রান্ত নির্দেশিকা](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=bn): কখনও কখনও জেনারেটিভ
  AI মডেল অপ্রত্যাশিত আউটপুট তৈরি করে, যেমন ভুল,
  পক্ষপাতদুষ্ট বা আপত্তিকর আউটপুট। এই ধরনের আউটপুট থেকে ক্ষতির ঝুঁকি কমাতে
  পোস্ট-প্রসেসিং ও হিউম্যান রিভিউ অপরিহার্য।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
