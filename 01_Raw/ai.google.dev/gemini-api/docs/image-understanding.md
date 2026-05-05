---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar
fetched_at: 2026-05-05T20:44:04.672650+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0635\u0648\u0631 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الصور

تم تصميم نماذج Gemini لتكون متعددة الوسائط منذ البداية، ما يتيح تنفيذ مجموعة واسعة من مهام معالجة الصور ورؤية الكمبيوتر، بما في ذلك على سبيل المثال لا الحصر، إضافة تعليقات توضيحية إلى الصور وتصنيفها والإجابة عن الأسئلة المرئية بدون الحاجة إلى تدريب نماذج مخصّصة للتعلم الآلي.

بالإضافة إلى الإمكانات العامة المتعدّدة الوسائط، توفّر نماذج Gemini **دقة محسّنة** لحالات استخدام معيّنة، مثل [اكتشاف العناصر](#object-detection)، وذلك من خلال تدريب إضافي.

## تمرير الصور إلى Gemini

يمكنك تقديم صور كمدخلات إلى Gemini باستخدام طريقتَين:

- [تمرير بيانات الصور المضمّنة](#inline-image): هذه الطريقة مثالية للملفات الأصغر حجمًا (إجمالي حجم الطلب أقل من 20 ميغابايت، بما في ذلك الطلبات).
- [تحميل الصور باستخدام File API](#upload-image): ننصح بهذه الطريقة للملفات الأكبر حجمًا أو لإعادة استخدام الصور في طلبات متعدّدة.

### تمرير بيانات الصور المضمّنة

يمكنك تمرير بيانات الصور المضمّنة في الطلب إلى `generateContent`. يمكنك تقديم بيانات الصور كسلاسل مرمّزة بتنسيق Base64 أو من خلال قراءة الملفات المحلية مباشرةً (حسب اللغة).

يوضّح المثال التالي كيفية قراءة صورة من ملف محلي وتمريرها إلى واجهة برمجة التطبيقات `generateContent` لمعالجتها.

### Python

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
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
  "gemini-3-flash-preview",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

يمكنك أيضًا جلب صورة من عنوان URL وتحويلها إلى وحدات بايت وتمريرها إلى
`generateContent` كما هو موضّح في الأمثلة التالية.

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
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
    "gemini-3-flash-preview",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

### تحميل الصور باستخدام File API

بالنسبة إلى الملفات الكبيرة أو لاستخدام ملف الصورة نفسه بشكل متكرر، استخدِم Files API. يحمّل الرمز التالي ملف صورة ثم يستخدم الملف في استدعاء `generateContent`. يمكنك الاطّلاع على [دليل Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) للحصول على مزيد من المعلومات والأمثلة.

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
      "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## تقديم طلب باستخدام صور متعددة

يمكنك تقديم صور متعددة في طلب واحد من خلال تضمين عناصر صورة
`Part` متعددة في مصفوفة `contents`. يمكن أن تكون هذه المراجع مزيجًا من البيانات المضمّنة (الملفات المحلية أو عناوين URL) ومراجع File API.

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

    model="gemini-3-flash-preview",
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

    model: "gemini-3-flash-preview",
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
  "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## رصد الأجسام

يتم تدريب النماذج على رصد العناصر في صورة والحصول على إحداثيات المربّع المحيط بها. يتم تغيير حجم الإحداثيات، بالنسبة إلى أبعاد الصورة، إلى النطاق [0, 1000]. عليك إعادة ضبط مقياس هذه الإحداثيات استنادًا إلى حجم الصورة الأصلي.

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

response = client.models.generate_content(model="gemini-3-flash-preview",
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

للاطّلاع على المزيد من الأمثلة، راجِع دفاتر الملاحظات التالية في [كتاب وصفات Gemini](https://github.com/google-gemini/cookbook):

- [دفتر ملاحظات لفهم المساحات الثنائية الأبعاد](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=ar)
- [دفتر ملاحظات تجريبي للإشارة ثلاثية الأبعاد](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=ar)

## تنسيقات الصور المسموح بها

يتوافق Gemini مع أنواع MIME التالية لتنسيقات الصور:

- ‫PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

للتعرّف على طرق إدخال الملفات الأخرى، يُرجى الاطّلاع على دليل [طرق إدخال الملفات](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar).

## الإمكانات

جميع إصدارات نموذج Gemini متعدّدة الوسائط ويمكن استخدامها في مجموعة واسعة من مهام معالجة الصور ورؤية الكمبيوتر، بما في ذلك على سبيل المثال لا الحصر، إضافة تعليقات توضيحية إلى الصور، والإجابة عن الأسئلة المرئية، وتصنيف الصور، ورصد العناصر.

يمكن أن يقلّل Gemini من الحاجة إلى استخدام نماذج تعلُّم آلي متخصّصة استنادًا إلى متطلبات الجودة والأداء.

تم تدريب أحدث إصدارات النماذج خصيصًا لتحسين دقة
المهام المتخصصة بالإضافة إلى الإمكانات العامة، مثل
[رصد الأجسام](#object-detection) المحسّن.

## القيود والمعلومات الفنية الأساسية

### الحد الأقصى لعدد الملفات

تتيح نماذج Gemini تحميل 3,600 ملف صورة كحد أقصى لكل طلب.

### احتساب الرموز المميزة

- ‫258 رمزًا مميزًا إذا كان كلا البُعدَين <= 384 بكسل
  يتم تقسيم الصور الأكبر حجمًا إلى مربّعات بحجم 768 × 768 بكسل، وتكلّف كل مربّع 258 رمزًا مميزًا.

في ما يلي صيغة تقريبية لاحتساب عدد المربّعات:

- احسب حجم وحدة الاقتصاص الذي يبلغ تقريبًا: floor(min(width, height) / 1.5).
- قسِّم كل بُعد على حجم وحدة الاقتصاص واضرب النتيجة في بعضها للحصول على عدد المربّعات.

على سبيل المثال، إذا كانت أبعاد الصورة 960x540، سيكون حجم وحدة الاقتصاص 360. قسِّم كل بُعد على 360، وسيكون عدد المربّعات 3 × 2 = 6.

### درجة دقة الوسائط

يقدّم Gemini 3 إمكانية التحكّم الدقيق في معالجة الصور المتعددة الوسائط باستخدام المَعلمة
`media_resolution`. تحدّد المَعلمة `media_resolution`
**الحد الأقصى لعدد الرموز المميزة المخصّصة لكل صورة إدخال أو إطار فيديو.**
تساهم الدقة الأعلى في تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميزة ووقت الاستجابة.

لمزيد من التفاصيل حول المَعلمة وكيفية تأثيرها في احتساب الرموز المميّزة، راجِع دليل [دقة الوسائط](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ar).

## النصائح وأفضل الممارسات

- تأكَّد من أنّ الصور تم تدويرها بشكل صحيح.
- استخدِم صورًا واضحة وغير معتمة.
- عند استخدام صورة واحدة مع نص، ضَع الطلب النصي *بعد* جزء الصورة في مصفوفة `contents`.

## الخطوات التالية

يوضّح لك هذا الدليل كيفية تحميل ملفات الصور وإنشاء نواتج نصية من مدخلات الصور. لمزيد من المعلومات، يُرجى الاطّلاع على المراجع التالية:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar): مزيد من المعلومات حول تحميل الملفات وإدارتها لاستخدامها مع Gemini
- [تعليمات النظام](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#system-instructions):
  تتيح لك تعليمات النظام توجيه سلوك النموذج استنادًا إلى احتياجاتك وحالات الاستخدام المحدّدة.
- [استراتيجيات إنشاء الطلبات](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide): تتيح واجهة Gemini API إمكانية إنشاء الطلبات باستخدام بيانات نصية وصور وملفات صوتية وفيديوهات، ويُعرف ذلك أيضًا باسم إنشاء الطلبات المتعددة الوسائط.
- [إرشادات الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar): في بعض الأحيان، تقدّم نماذج الذكاء الاصطناعي التوليدي نتائج غير متوقعة، مثل نتائج غير دقيقة أو متحيزة أو مسيئة. تُعدّ المعالجة اللاحقة والتقييم البشري أساسيَّين للحدّ من خطر الأضرار الناجمة عن هذه النتائج.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
