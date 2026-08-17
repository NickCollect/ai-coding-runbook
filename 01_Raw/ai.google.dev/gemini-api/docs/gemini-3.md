---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=tr
fetched_at: 2026-08-17T02:18:10.695204+00:00
title: "Gemini 3 Geli\u015ftirici K\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)

Geri bildirim gönderin

# Gemini 3 Geliştirici Kılavuzu

Gemini 3, gelişmiş mantık yürütme altyapısıyla geliştirilmiş, bugüne kadarki en akıllı model ailemizdir. Asenkron iş akışlarında, bağımsız kodlamada ve karmaşık çok formatlı görevlerde uzmanlaşarak her fikri hayata geçirmek için tasarlanmıştır.
Bu rehberde, Gemini 3 model ailesinin temel özellikleri ve bu özelliklerden en iyi şekilde nasıl yararlanabileceğiniz açıklanmaktadır.

Modelin gelişmiş akıl yürütme, bağımsız kodlama ve karmaşık çok formatlı görevleri nasıl ele aldığını görmek için [Gemini 3 uygulamaları koleksiyonumuzu](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=tr) inceleyin.

Birkaç satır kodla başlayın:

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

## Gemini 3 serisiyle tanışın

Gemini 3.1 Pro, geniş dünya bilgisi ve farklı formatlarda gelişmiş mantık yürütme gerektiren karmaşık görevler için en iyi seçenektir.

Gemini 3 Flash, 3 serisinin en yeni modelidir. Pro düzeyinde zekaya sahip olan bu model, Flash'in hızı ve fiyatıyla sunulur.

Nano Banana Pro (Gemini 3 Pro Image olarak da bilinir) en yüksek kaliteli görüntü üretme modelimizdir. Nano Banana 2 (Gemini 3.1 Flash Image olarak da bilinir) ise yüksek hacimli, yüksek verimli ve daha düşük fiyatlı bir alternatiftir.

Gemini 3.1 Flash-Lite, maliyet verimliliği ve yüksek hacimli görevler için tasarlanmış modelimizdir.

Tüm Gemini 3 modelleri şu anda önizleme sürümündedir.

| Model Kimliği | Bağlam penceresi (içinde / dışında) | Son Güncel Bilgi Tarihi | Fiyatlandırma (Giriş / Çıkış)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Ocak 2025 | 0,25 ABD doları (metin, resim, video), 0,50 ABD doları (ses) / 1,50 ABD doları |
| **gemini-3.1-flash-image-preview** | 128 bin / 32 bin | Ocak 2025 | 0,25 ABD doları (Metin Girişi) / 0,067 ABD doları (Resim Çıkışı)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Ocak 2025 | 2 ABD doları / 12 ABD doları (<200 bin parça)   4 ABD doları / 18 ABD doları (>200 bin parça) |
| **gemini-3-flash-preview** | 1M / 64k | Ocak 2025 | 0,50 ABD doları / 3 ABD doları |
| **gemini-3-pro-image-preview** | 65 bin / 32 bin | Ocak 2025 | 2 ABD doları (Metin Girişi) / 0,134 ABD doları (Resim Çıkışı)\*\* |

*\* Aksi belirtilmedikçe fiyatlandırma 1 milyon jeton başına yapılır.*
*\*\* Resim fiyatlandırması çözünürlüğe göre değişir. Ayrıntılar için [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) göz atın.*

Ayrıntılı sınırlar, fiyatlandırma ve ek bilgiler için [modeller sayfasına](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) bakın.

## Gemini 3'teki yeni API özellikleri

Gemini 3, geliştiricilere gecikme, maliyet ve çok formatlı doğruluk üzerinde daha fazla kontrol imkanı sunmak için tasarlanmış yeni parametreler sunar.

### Düşünme düzeyi

Gemini 3 serisi modeller, istemleri değerlendirmek için varsayılan olarak dinamik düşünme özelliğini kullanır. Yanıt oluşturmadan önce modelin dahili muhakeme sürecinin **maksimum** derinliğini kontrol eden `thinking_level` parametresini kullanabilirsiniz. Gemini 3, bu seviyeleri katı jeton garantileri yerine düşünme için göreceli izinler olarak değerlendirir.

`thinking_level` belirtilmezse Gemini 3 varsayılan olarak `high` değerini kullanır. Karmaşık akıl yürütme gerekmeyen durumlarda daha hızlı ve daha düşük gecikmeli yanıtlar için modelin düşünce düzeyini `low` ile sınırlayabilirsiniz.

| Düşünme Düzeyi | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Açıklama |
| --- | --- | --- | --- | --- |
| **`minimal`** | Desteklenmiyor | Destekleniyor (Varsayılan) | Destekleniyor | Çoğu sorgu için "düşünme yok" ayarıyla eşleşir. Model, karmaşık kodlama görevleri için çok az düşünebilir. Sohbet veya yüksek gönderim hacmi uygulamalarında gecikmeyi en aza indirir. `minimal`'nın düşünme özelliğinin kapalı olduğunu garanti etmediğini unutmayın. |
| **`low`** | Destekleniyor | Destekleniyor | Destekleniyor | Gecikmeyi ve maliyeti en aza indirir. Basit talimatları uygulamak, sohbet etmek veya yüksek işleme hızlı uygulamalar için en iyisidir. |
| **`medium`** | Destekleniyor | Destekleniyor | Destekleniyor | Çoğu görev için dengeli düşünme |
| **`high`** | Destekleniyor (Varsayılan, Dinamik) | Desteklenir (Dinamik) | Destekleniyor (Varsayılan, Dinamik) | Akıl yürütme derinliğini en üst düzeye çıkarır. Modelin ilk (düşünme içermeyen) çıkış jetonuna ulaşması önemli ölçüde daha uzun sürebilir ancak çıkış daha dikkatli bir şekilde gerekçelendirilir. |

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

### Sıcaklık

Tüm Gemini 3 modellerinde, sıcaklık parametresini `1.0` varsayılan değerinde tutmanızı önemle tavsiye ederiz.

Önceki modellerde yaratıcılık ile determinizm arasındaki dengeyi kontrol etmek için genellikle sıcaklık ayarından yararlanılırdı. Ancak Gemini 3'ün akıl yürütme özellikleri varsayılan ayar için optimize edilmiştir. Sıcaklığı değiştirmek (1, 0'ın altına ayarlamak), özellikle karmaşık matematiksel veya muhakeme görevlerinde döngüye girme ya da performansın düşmesi gibi beklenmedik davranışlara yol açabilir.

### Düşünce imzaları

Gemini 3 modelleri, API çağrıları arasında akıl yürütme bağlamını korumak için düşünce imzalarını kullanır. Bu imzalar, modelin içsel düşünce sürecinin şifrelenmiş gösterimleridir.

- **Durumlu Mod (Önerilen)**: Interactions API'yi durumlu modda (`previous_interaction_id` sağlanarak) kullanırken sunucu, görüşme geçmişini ve düşünce imzalarını otomatik olarak yönetir.
- **Durumsuz Mod**: Konuşma geçmişini manuel olarak yönetiyorsanız sonraki isteklerde orijinalliği doğrulamak için düşünce bloklarını imzalarıyla birlikte eklemeniz gerekir.

Ayrıntılı bilgi için [Düşünce İmzaları](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) sayfasına bakın.

### Araçlarla yapılandırılmış çıkışlar

Gemini 3 modelleri, [Yapılandırılmış Çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)'ı [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr), [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) gibi yerleşik araçlarla birleştirmenize olanak tanır.

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

### Görüntü üretme

Gemini 3.1 Flash Image ve Gemini 3 Pro Image, metin istemlerinden görseller oluşturup düzenlemenize olanak tanır. Bir istemi "düşünmek" için akıl yürütme özelliğini kullanır ve yüksek kaliteli görüntüler oluşturmadan önce [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)'yı temel alarak hava durumu tahminleri veya borsa grafikleri gibi gerçek zamanlı verileri alabilir.

**Yeni ve iyileştirilmiş özellikler:**

- **4K ve metin oluşturma:** 2K ve 4K çözünürlüklerde net ve okunaklı metinler ve diyagramlar oluşturun.
- **Temellendirilmiş üretim:** Gerçek dünyadaki bilgilere dayalı görüntüler oluşturmak ve bilgileri doğrulamak için `google_search` aracını kullanın. Google *Görsel* Arama ile temellendirme, Gemini 3.1 Flash Image için kullanılabilir.
- **Sohbete dayalı düzenleme:** Değişiklikleri (ör. "Arka planı gün batımı yap") isteyerek çok aşamalı etkileşimli görüntü düzenleme. Bu iş akışında, dönüşler arasındaki görsel bağlamı korumak için **Thought Signatures** (Düşünce İmzaları) kullanılır.

En-boy oranları, düzenleme iş akışları ve yapılandırma seçenekleriyle ilgili tüm ayrıntılar için [Görüntü Üretme Kılavuzu](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)'na bakın.

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

**Örnek Yanıt**

![Weather Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=tr)

### Görüntülerle kod yürütme

Gemini 3 Flash, görme eylemini yalnızca statik bir bakış olarak değil, aktif bir araştırma olarak ele alabilir. Model, akıl yürütmeyi [kod yürütmeyle](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) birleştirerek bir plan oluşturur. Ardından, cevaplarını görsel olarak temellendirmek için görüntüleri adım adım yakınlaştırmak, kırpmak, açıklama eklemek veya başka bir şekilde değiştirmek üzere Python kodu yazar ve yürütür.

**Kullanım alanları:**

- **Yakınlaştırma ve inceleme:** Model, ayrıntıların çok küçük olduğunu (ör. uzaktaki bir ölçüm cihazını veya seri numarasını okuma) algıladığında alanı kırpıp daha yüksek çözünürlükte yeniden incelemek için kodu otomatik olarak yazar.
- **Görsel matematik ve grafik oluşturma:** Model, kod kullanarak çok adımlı hesaplamalar yapabilir (ör. bir makbuzdaki satır öğelerini toplama veya çıkarılan verilerden Matplotlib grafiği oluşturma).
- **Resim açıklaması:** Model, "Bu öğe nereye yerleştirilmeli?" gibi konumsal soruları yanıtlamak için doğrudan resimlerin üzerine oklar, sınırlayıcı kutular veya başka açıklamalar çizebilir.

Görsel düşünmeyi etkinleştirmek için [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)'yi araç olarak yapılandırın. Model, gerektiğinde resimleri değiştirmek için otomatik olarak kod kullanır.

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

Resimlerle kod yürütme hakkında daha fazla bilgi için [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#images) başlıklı makaleyi inceleyin.

### Çok formatlı işlev yanıtları

[Çok formatlı işlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#multimodal), kullanıcıların çok formatlı nesneler içeren işlev yanıtları almasına olanak tanıyarak modelin işlev çağırma özelliklerinin daha iyi kullanılmasını sağlar. Standart işlev çağrısı yalnızca metin tabanlı işlev yanıtlarını destekler:

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

### Yerleşik araçları ve işlev çağrılarını birleştirme

Gemini 3, aynı API çağrısında yerleşik araçların (ör. Google Arama, URL bağlamı ve [daha fazlası](https://ai.google.dev/gemini-api/docs/tools?hl=tr)) ve özel [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) araçlarının kullanılmasına olanak tanıyarak daha karmaşık iş akışları oluşturulmasını sağlar.

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

## Gemini 2.5'ten taşıma

Gemini 3, bugüne kadarki en yetenekli model ailemizdir ve Gemini 2.5'e kıyasla kademeli bir iyileşme sunar. Taşıma işlemi yaparken aşağıdakileri göz önünde bulundurun:

- **Düşünen:** Gemini 2.5'i mantık yürütmeye zorlamak için daha önce karmaşık istem mühendisliği (ör. düşünce zinciri) kullanıyorsanız `thinking_level: "high"` ile Gemini 3'ü ve basitleştirilmiş istemleri deneyin.
- **Sıcaklık ayarları:** Mevcut kodunuz sıcaklığı açıkça ayarlıyorsa (özellikle de deterministik çıkışlar için düşük değerlere ayarlıyorsa) olası döngü sorunlarını veya karmaşık görevlerde performans düşüşünü önlemek için bu parametreyi kaldırmanızı ve Gemini 3'ün varsayılan değeri olan 1.0'ı kullanmanızı öneririz.
- **PDF ve belge anlama:**
  Yoğun belge ayrıştırma için belirli bir davranışa güveniyorsanız doğruluğun devamlılığını sağlamak amacıyla yeni `media_resolution_high` ayarını test edin.
- **Jeton tüketimi:** Varsayılan olarak Gemini 3'e geçiş, PDF'ler için jeton kullanımını **artırabilir** ancak videolar için jeton kullanımını **azaltabilir**. Varsayılan çözünürlüklerin yükselmesi nedeniyle istekler artık bağlam penceresini aşıyorsa medya çözünürlüğünü açıkça düşürmenizi öneririz.
- **Görüntü segmentasyonu:** Görüntü segmentasyonu özellikleri (nesneler için piksel düzeyinde maskeler döndürme) Gemini 3 Pro veya Gemini 3 Flash'te desteklenmez. Yerleşik görüntü segmentasyonu gerektiren iş yükleri için düşünme özelliği devre dışı bırakılmış Gemini 2.5 Flash'i kullanmaya devam etmenizi öneririz.
- **Bilgisayar Kullanımı:** Gemini 3 Pro ve Gemini 3 Flash, [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)'nı destekler. 2.5 serisinin aksine, Bilgisayar Kullanımı aracına erişmek için ayrı bir model kullanmanız gerekmez.
- **Araç desteği**: [Yerleşik araçları işlev çağrısıyla birleştirme](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) artık Gemini 3 modellerinde destekleniyor. [Haritalar
  temellendirmesi](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) artık Gemini 3
  modellerinde de destekleniyor.

## OpenAI uyumluluğu

[OpenAI uyumluluk katmanını](https://ai.google.dev/gemini-api/docs/openai?hl=tr) kullananlar için standart parametreler (OpenAI'ın `reasoning_effort`) otomatik olarak Gemini (`thinking_level`) eşdeğerleriyle eşlenir.

## İstemlerle ilgili en iyi uygulamalar

Gemini 3, istem oluşturma şeklinizi değiştiren bir akıl yürütme modelidir.

- **Net talimatlar:** Giriş istemlerinizde kısa ve öz olun. Gemini 3, doğrudan ve net talimatlara en iyi şekilde yanıt verir. Eski modeller için kullanılan ayrıntılı veya aşırı karmaşık istem mühendisliği tekniklerini aşırı analiz edebilir.
- **Çıkış ayrıntı düzeyi:** Gemini 3 varsayılan olarak daha az ayrıntılıdır ve doğrudan, etkili yanıtlar vermeyi tercih eder. Kullanım alanınız daha sohbet odaklı veya "konuşkan" bir karakter gerektiriyorsa istemde modeli açıkça yönlendirmeniz gerekir (ör. "Bunu arkadaş canlısı, konuşkan bir asistan gibi açıkla").
- **Bağlam yönetimi:** Büyük veri kümeleriyle (ör. kitapların tamamı, kod tabanları veya uzun videolar) çalışırken özel talimatlarınızı ya da sorularınızı istemin sonuna, veri bağlamından sonra ekleyin. Sorunuza "Önceki bilgilere göre..." gibi bir ifadeyle başlayarak modelin muhakemesini sağlanan verilere dayandırın.

İstem tasarımı stratejileri hakkında daha fazla bilgiyi [istem mühendisliği kılavuzunda](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) bulabilirsiniz.

## SSS

1. **Gemini 3'ün son güncel bilgi tarihi nedir?** Gemini 3 modellerinin son güncel bilgi tarihi Ocak 2025'tir. Daha güncel bilgiler için [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) aracını kullanın.
2. **Bağlam penceresi sınırları nelerdir?** Gemini 3 modelleri, 1 milyon parçalık giriş bağlam penceresini ve 64 bin parçaya kadar çıkışı destekler.
3. **Gemini 3 için ücretsiz katman var mı?** Gemini 3 Flash
   `gemini-3-flash-preview`, Gemini API'de ücretsiz katmana sahiptir. Google AI Studio'da Gemini 3.1 Pro ve 3 Flash'ı ücretsiz olarak deneyebilirsiniz ancak Gemini API'de `gemini-3.1-pro-preview` için ücretsiz katman bulunmamaktadır.
4. **Eski `thinking_budget` kodum çalışmaya devam eder mi?** Evet, `thinking_budget` geriye dönük uyumluluk için hâlâ desteklenmektedir ancak daha öngörülebilir bir performans için `thinking_level`'ye geçmenizi öneririz. Aynı istekte ikisini birden kullanmayın.
5. **Gemini 3, Batch API'yi destekliyor mu?** Evet, Gemini 3, [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)'yi destekler.
6. **Bağlamı önbelleğe alma özelliği destekleniyor mu?** Evet, Gemini 3'te [Context Caching](https://ai.google.dev/gemini-api/docs/caching?hl=tr) (Bağlam Önbelleğe Alma) desteklenir.
7. **Gemini 3'te hangi araçlar desteklenir?** Gemini 3; [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), [Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr), [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr), [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)'nı destekler. Ayrıca, kendi özel araçlarınız için ve [yerleşik araçlarla birlikte](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) standart [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)'i de destekler.
8. **`gemini-3.1-pro-preview-customtools` nedir?** `gemini-3.1-pro-preview` kullanıyorsanız ve model, bash komutları yerine özel araçlarınızı yoksayıyorsa bunun yerine `gemini-3.1-pro-preview-customtools` modelini deneyin.
   Daha fazla bilgiye [buradan][customtools-model] ulaşabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
