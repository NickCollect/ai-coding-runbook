---
source_url: https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=tr
fetched_at: 2026-05-18T05:07:16.195351+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Görüntü anlama

Gemini modelleri baştan aşağı çok formatlı olacak şekilde tasarlandığından, özel makine öğrenimi modelleri eğitmenize gerek kalmadan görüntü açıklaması, sınıflandırma ve görsel soru cevaplama gibi çok çeşitli görüntü işleme ve bilgisayarla görme görevlerini yerine getirebilirsiniz.

Gemini modelleri, genel çok formatlı özelliklerinin yanı sıra ek eğitim sayesinde [nesne algılama](#object-detection) ve [segmentasyon](#segmentation) gibi belirli kullanım alanlarında **daha yüksek doğruluk** sunar.

## Gemini'a görüntü aktarma

Gemini'a giriş olarak resim sağlamak için çeşitli yöntemler kullanabilirsiniz:

- [URL kullanarak resim iletme](#url-image): Herkese açık resimler için idealdir.
- [Satır içi görüntü verilerini iletme](#inline-image): Base64 kodlu görüntü verileri için.
- [File API'yi kullanarak resim yükleme](#upload-image): Daha büyük dosyalar veya resimleri birden çok istekte yeniden kullanmak için önerilir.

### URL kullanarak resim iletme

[Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=tr)'yi kullanarak bir resim yükleyebilir ve isteğe iletebilirsiniz:

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
  -H "Api-Revision: 2026-05-20" \
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

### Satır içi resim verilerini iletme

Görüntü verilerini base64 kodlu dizeler olarak sağlayabilirsiniz:

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
  -H "Api-Revision: 2026-05-20" \
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

### File API'yi kullanarak resim yükleme

Büyük dosyalar için veya aynı resim dosyasını tekrar tekrar kullanabilmek için Files API'yi kullanın. [Files API kılavuzuna](https://ai.google.dev/gemini-api/docs/interactions/files?hl=tr) bakın.

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
  -H "Api-Revision: 2026-05-20" \
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

## Birden fazla resimle istem oluşturma

`input` dizisine birden fazla resim nesnesi ekleyerek tek bir istemde birden fazla resim sağlayabilirsiniz:

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
  -H "Api-Revision: 2026-05-20" \
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

## Nesne algılama

Modeller, bir görüntüdeki nesneleri algılayıp sınırlayıcı kutu koordinatlarını almak için eğitilir. Görüntü boyutlarına göre koordinatlar [0, 1000] aralığında ölçeklendirilir. Bu koordinatları orijinal resim boyutunuza göre ölçeklendirmeniz gerekir.

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

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

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
    schema: z.toJSONSchema(boundingBoxesSchema)
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
  -H "Api-Revision: 2026-05-20" \
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

Daha fazla örnek için [Gemini Cookbook](https://github.com/google-gemini/cookbook)'taki aşağıdaki not defterlerini inceleyin:

## Segmentasyon

Gemini 2.5'ten itibaren modeller yalnızca öğeleri algılamakla kalmaz, aynı zamanda bunları segmentlere ayırır ve kontur maskelerini sağlar.

Model, her öğenin bir segmentasyon maskesini temsil ettiği bir JSON listesi tahmin eder.
Her öğe, 0 ile 1000 arasında normalleştirilmiş koordinatlara sahip `[y0, x0, y1, x1]` biçiminde bir sınırlayıcı kutu ("`box_2d`"), nesneyi tanımlayan bir etiket ("`label`") ve son olarak sınırlayıcı kutunun içindeki segmentasyon maskesini içerir. Bu maske, 0 ile 255 arasında değerlere sahip bir olasılık haritası olan base64 kodlu png biçimindedir.

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

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

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
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
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
  -H "Api-Revision: 2026-05-20" \
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
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![Ahşap ve cam nesnelerin vurgulandığı, keklerin bulunduğu bir masa](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=tr)

Nesneler ve segmentasyon maskeleri içeren örnek bir segmentasyon çıkışı

## Desteklenen görsel biçimleri

Gemini aşağıdaki resim biçimi MIME türlerini destekler:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Diğer dosya giriş yöntemleri hakkında bilgi edinmek için [Dosya giriş yöntemleri](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=tr) kılavuzuna bakın.

## Özellikler

Tüm Gemini modeli sürümleri çok formatlıdır ve görüntü açıklaması, görsel soru ve yanıtlama, görüntü sınıflandırması, nesne algılama ve segmentasyon dahil ancak bunlarla sınırlı olmamak üzere çok çeşitli görüntü işleme ve bilgisayarla görme görevlerinde kullanılabilir.

Gemini, kalite ve performans gereksinimlerinize bağlı olarak özel makine öğrenimi modelleri kullanma ihtiyacını azaltabilir.

En yeni model sürümleri, özellikle geliştirilmiş [nesne algılama](#object-detection) ve [segmentasyon](#segmentation) gibi genel özelliklerin yanı sıra uzmanlık gerektiren görevlerin doğruluğunu artırmak için eğitilmiştir.

## Sınırlamalar ve temel teknik bilgiler

### Dosya sınırı

Gemini modelleri,istek başına en fazla 3.600 resim dosyasını destekler.

### Jeton hesaplama

- Her iki boyut da <= 384 piksel ise 258 jeton.
  Daha büyük resimler, her biri 258 jeton değerinde olan 768x768 piksellik bloklar halinde düzenlenir.

Döşeme sayısını hesaplamak için kullanılan yaklaşık formül şöyledir:

- Yaklaşık olarak `floor(min(width, height)` / 1,5 olan kırpma birimi boyutunu hesaplayın.
- Her boyutu kırpma birimi boyutuna bölün ve döşeme sayısını elde etmek için sonuçları çarpın.

Örneğin, 960x540 boyutlarındaki bir resmin kırpma birimi boyutu 360 olur. Her boyutu 360'a bölün. Döşeme sayısı 3 \* 2 = 6 olur.

### Medya çözünürlüğü

Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sunar. `media_resolution` parametresi, **giriş resim veya video karesi başına ayrılan maksimum jeton sayısını** belirler.
Daha yüksek çözünürlükler, modelin ince metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.

## İpuçları ve en iyi uygulamalar

- Resimlerin doğru şekilde döndürüldüğünü doğrulayın.
- Net ve bulanık olmayan resimler kullanın.
- Metin içeren tek bir resim kullanırken metin istemini `input` dizisinde resmin *önüne* yerleştirin.

## Sırada ne var?

Bu kılavuzda, resim dosyalarını nasıl yükleyeceğiniz ve resim girişlerinden nasıl metin çıkışları oluşturacağınız açıklanmaktadır. Daha fazla bilgi edinmek için aşağıdaki kaynakları inceleyin:

- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=tr): Gemini ile kullanılacak dosyaları yükleme ve yönetme hakkında daha fazla bilgi edinin.
- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr#system-instructions):
  Sistem talimatları, modelin davranışını özel ihtiyaçlarınıza ve kullanım alanlarınıza göre yönlendirmenizi sağlar.
- [Dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/interactions/files?hl=tr#prompt-guide): Gemini API, çok formatlı istem olarak da bilinen metin, resim, ses ve video verileriyle istemi destekler.
- [Güvenlikle ilgili bilgiler](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr): Üretken yapay zeka modelleri bazen yanlış, taraflı veya rahatsız edici gibi beklenmedik çıkışlar üretebilir. Bu tür çıkışlardan kaynaklanan zarar riskini sınırlamak için işleme sonrası ve insan değerlendirmesi gereklidir.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-11 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-11 UTC."],[],[]]
