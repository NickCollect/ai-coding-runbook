---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=tr
fetched_at: 2026-08-31T06:33:16.495731+00:00
title: "Gemini Omni Flash ile video \u00fcretme ve d\u00fczenleme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Omni Flash ile video üretme ve düzenleme

Gemini Omni Flash (`gemini-omni-1.1-flash`), yüksek hızlı video üretimi, düzenleme ve sinematik kontrol için tasarlanmış yüksek performanslı bir çok formatlı modeldir.
Gemini Omni, önceki video modellerinden ayıran aşağıdaki temel özellikler üzerine kurulmuştur:

- **Doğal çok formatlılık:** Metin, resim, ses ve videoyu aynı anda işleyerek daha tutarlı, tutarlı ve kontrol edilebilir bir çıkış sağlar.
- **Sohbet ederek düzenleme:** [Etkileşimler API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) ile etkinleştirilen bu özellik, doğal dil sohbeti aracılığıyla videolarınızı yinelemeli olarak iyileştirmenize ve düzenlemenize olanak tanır. Değiştirmek istediğiniz şeyi açıklayın. Model, düzenlemeyi uygularken videonun korumak istediğiniz kısımlarını da korur.
- **Dünya bilgisi:** Gemini Omni, fizik anlayışını Gemini'ın tarih, bilim ve kültürel bağlam bilgisiyle birleştirerek fotorealizmden anlamlı hikaye anlatımına geçişi sağlar.

## Metinden video üretme

Metin isteminden video oluşturma Model, metin açıklamanıza göre sesli bir video oluşturur. En iyi sonuçları almak için sahne açıklaması, kamera hareketi, ışıklandırma ve atmosfer gibi ayrıntıları içeren istemler yazın.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### REST yanıt şeması

Kolaylık alanı `interaction.output_video` **yalnızca SDK**'dır.
REST API'yi doğrudan kullanırken `steps` dizisinden video çıkışını alın.

**Ham REST JSON yapısı:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

### En boy oranını kontrol etme

Dikey videolar oluşturmak için `aspect_ratio` simgesini `"9:16"` olarak ayarlayın. Varsayılan yön Yatay (16:9)'dur.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Çıkış çözünürlüğü

`response_format` uygulamasında `resolution` parametresini kullanarak oluşturulan videonuzun çıkış çözünürlüğünü kontrol edin. Varsayılan çözünürlük 720p'dir.

| Değer | Açıklama |
| --- | --- |
| `360p` | 360p çıkış çözünürlüğü |
| `720p` | 720p çıkış çözünürlüğü (varsayılan) |
| `1080p` | 1080p çıkış (çözünürlüğü artırılmış) |
| `4k` | 4K çıkış (yukarı ölçeklenmiş) |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A drone shot of a mountain landscape at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",
    },
)
with open("hires.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A drone shot of a mountain landscape at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p',
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('hires.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A drone shot of a mountain landscape at sunrise.",
 "response_format": {
   "type": "video",
   "resolution": "1080p"
 }
}'
```

## Görüntüden video üretme

Metin isteminizle birlikte bir referans görsel sağlayabilirsiniz. Modele verdiğiniz isteme bağlı olarak, model görüntüyü nasıl kullanacağına karar verir. Bu özellik, ürün çekimlerini, çizimleri veya fotoğrafları canlandırmak için kullanışlıdır.

Aşağıdaki örnekte, sudan çıkan bir balık çiziminin referans görselinin nasıl kullanılacağı gösterilmektedir:

![Sudan zıplayan balık çizimi](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=tr)

Aşağıdaki istemle:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Çizimin gerçekçi bir videosunu oluşturmak için.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### İlk ve son kare interpolasyonu

Gemini Omni Flash, video ara karesi oluşturmayı destekler. Bu sayede, başlangıç resmi (ilk kare) ile bitiş resmi (son kare) arasında sorunsuz geçiş yapan videolar oluşturabilirsiniz.

`input` listesinde iki resim sağlayın ve isteminizde istediğiniz geçişi açıklayın. Model, sahneyi ilk kareden son kareye kadar animasyon haline getirir.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": first_frame_b64, "mime_type": "image/jpeg"},
        {"type": "image", "data": last_frame_b64, "mime_type": "image/jpeg"},
        {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
    ],
)
with open("interpolation.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: firstFrameB64, mime_type: 'image/jpeg' },
    { type: 'image', data: lastFrameB64, mime_type: 'image/jpeg' },
    { type: 'text', text: 'A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolation.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$FIRST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "image", "data": "'"$LAST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
 ]
}'
```

### Konu referansı

Referans resim olarak sağlanan belirli konuları içeren bir video oluşturabilirsiniz.
Örneğin, aşağıdaki kodda, kedinin iple oynadığı bir video oluşturmak için kedi ve ipin 2 resminin nasıl sağlanacağı gösterilmektedir.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Görevler parametresi

`video_config` composable'ında `task` parametresini kullanarak amaçlanan davranışı açıkça belirtebilirsiniz. Örneğin, modelin bir resimden video oluşturmasını istiyorsanız parametreyi `image_to_video` olarak ayarlayabilirsiniz. Bu ayar yapılmazsa model, istemden ne istediğinizi çıkarır.

İzin verilen değerler şunlardır:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

Aşağıdaki örnekte, daha önce gösterilen resimden videoya örneği için bu ayarın nasıl yapılacağı gösterilmektedir.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-flash",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## Durumlu video düzenleme

Video oluşturun ve takip istemlerini kullanarak videoyu yinelemeli olarak düzenleyin. Her dönüş, önceki sonucun üzerine kurulur. Model, video bağlamını hatırlar ve değişikliklerinizi uygularken bahsetmediğiniz öğeleri korur. Önceki videoyu yeniden yüklemeden sohbet geçmişini ve oluşturulan video durumunu izlemek için `previous_interaction_id` simgesini kullanın.

Aşağıdaki örnekte, ilk videonun nasıl oluşturulacağı ve düzenleneceği gösterilmektedir:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-flash", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

İlk video örneği:

Düzenlenmiş video örneği:

Sohbetteki her dönüş yeni bir video oluşturur. Model, önceki dönüşlerdeki bağlamı anlar. Bu sayede, sahnenin tamamını yeniden tanımlamadan ışığı ayarlama ve arka planları değiştirme gibi artımlı değişiklikler yapabilirsiniz.

### Kendi videolarınızı düzenleme

Videolarınızı [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr)'yi kullanarak yükleyip Gemini Omni Flash ile düzenleyin.

Aşağıdaki örnekte, orijinal videonun nasıl düzenleneceği gösterilmektedir:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-1.1-flash",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

Düzenlenmiş video örneği:

## URI ile video alma

Oluşturulan 4 MB'tan büyük videoları almak için `delivery="uri"` parametresini `response_format` içinde kullanın.
Bu işlem, indirmeden önce video `ACTIVE` olana kadar yoklayabileceğiniz Google tarafından barındırılan bir URI döndürür.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
client.files.download(file=video_output.uri, destination="output.mp4")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Ham REST JSON yapısı (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

## Video uzantısı

Klipin sonuna sorunsuz bir devam niteliğinde içerik oluşturarak mevcut bir videoyu uzatın. İsteminizde videonun nasıl devam etmesini istediğinizi açıklayın. Örneğin, `"Extend this video"` veya `"Continue the scene: the camera pans across the mountains"`.
Model, 3-10 saniyelik bir devam niteliğinde video oluşturmak için giriş videosunu analiz eder.

Şunları uzatabilirsiniz:

- **Model tarafından oluşturulan videolar (çok aşamalı etkileşim)**: Daha önce oluşturulmuş bir videoyu `previous_interaction_id` referans alarak genişletin.
- **Yüklenen videolar**: Uzantı isteminizle birlikte yüklenen bir video dosyası (Files API aracılığıyla) sağlayın.

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload your video using the Files API
video_file = client.files.upload(file="my_video.mp4")

# Extend the video using prompt-based extension
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "Continue the scene."}
    ],
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload your video using the Files API
let videoFile = await ai.files.upload({
  file: 'my_video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Extend the video using prompt-based extension
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

### Referans medyayla genişletme

Genişletilmiş videoya yeni karakterler veya öğeler eklemek için isteminizle birlikte `input` dizisinde referans görseller sağlayabilirsiniz:

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload base video and reference image using the Files API
video_file = client.files.upload(file="my_video.mp4")
character_img = client.files.upload(file="character.png")

# Extend the video while introducing the reference character
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "document", "uri": character_img.uri},
        {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
    ],
)
with open("extended_with_character.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload base video and reference image using the Files API
let videoFile = await ai.files.upload({ file: 'my_video.mp4' });
let characterImg = await ai.files.upload({ file: 'character.png' });

while (videoFile.state === 'PROCESSING' || characterImg.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
  characterImg = await ai.files.get({ name: characterImg.name });
}

// Extend the video while introducing the reference character
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'document', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'$VIDEO_URI'"},
   {"type": "document", "uri": "'$CHARACTER_IMG_URI'"},
   {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
 ]
}'
```

### Uzantılarla ilgili kısıtlamalar ve yönergeler

Videoları uzatırken aşağıdaki kuralları ve kısıtlamaları göz önünde bulundurun:

- **Yüklenen videolardaki konuşma diyalogları**: Şu anda, konuşan birinin yer aldığı yüklenmiş bir videoyu ek diyalog eklemek için uzatamazsınız (karakter sessiz kalırsa veya istem diyalog eklemezse bu işlem desteklenir).
- **Çok aşamalı etkileşimli ses uzantısı**: Daha önce oluşturulan videoları çok aşamalı etkileşimli (`previous_interaction_id`) olarak genişletirken konuşma diyaloğu veya konuşma oluşturma desteklenir.
- **Yalnızca klibin sonu**: Uzantı, yalnızca videonun sonuna ekleme yapmakla sınırlıdır.
  İçerik ekleyemez veya klibin ortasını uzatamazsınız.
- **Süre sınırı**: Uzantı için giriş videoları, yüklenirken (çok aşamalı etkileşim kullanılmadığı sürece) 10 saniye veya daha kısa olmalıdır.
- **Bölgesel kullanılabilirlik**: Yüklenen videoları uzatma özelliği şu anda Avrupa Ekonomik Alanı (AEA), İsviçre ve Birleşik Krallık'taki kullanıcılar tarafından kullanılamamaktadır (model tarafından oluşturulan videoları uzatma özelliği, kullanılabilir olan tüm bölgelerde desteklenir).

## En iyi uygulamalar

- **Büyük videolar için URI teslimini kullanın:** 4 MB'tan büyük videolar için (varsa >720p) yük boyutu sınırlarını aşmamak amacıyla `response_format` içinde `delivery="uri"` kullanın.
- **Optimize edilmiş performans:** Daha hızlı ve senkron tekli oluşturma için `background=false`, `store=false` ve `stream=false` değerlerini ayarlayın. `store=false` ayarının, oluşturulan videonun sonraki dönüşlerde `previous_interaction_id` kullanılarak düzenlenemeyeceği anlamına geldiğini unutmayın.
- **İstem hassasiyeti:** Ayrıntılar için [istem rehberliği](#prompt-guide) bölümüne bakın.

## Sınırlamalar

- Küçüklerin yer aldığı resimleri yükleme ve düzenleme özelliği Avrupa Ekonomik Alanı, İsviçre ve Birleşik Krallık'ta desteklenmez.
- Tanınabilir kişilerin yer aldığı resimlerin yüklenmesi ve düzenlenmesi desteklenmez.
- Yüklenen videoları düzenleme veya uzatma özelliği şu anda Avrupa Ekonomik Alanı (AEA), İsviçre ve Birleşik Krallık'taki kullanıcılar tarafından kullanılamamaktadır (model tarafından oluşturulan videoları düzenleme veya uzatma özelliği desteklenir).
- Düzenleme ve uzatma için giriş videoları, yüklenirken 10 saniye veya daha kısa olmalıdır (çok aşamalı etkileşim model tarafından oluşturulan videolar uzatılmadığı sürece).
- Video uzatma, yalnızca videonun sonuna ekleme ile sınırlıdır. Klibin başına ekleme veya ortasını uzatma desteklenmez.
- Yüklenen ve birinin konuştuğu videolara ek diyalog eklemek için videoyu uzatamazsınız (karakterler sessiz kalabilir veya `previous_interaction_id` ile çok aşamalı etkileşim uzatma kullanılabilir).
- Sesle düzenleme desteklenmez.
- Ses referanslarının yüklenmesi, API'nin mevcut sürümünde desteklenmemektedir.
- Video referansları, benzerliklerle en iyi şekilde çalışır. Video referansındaki sesler dikkate alınmaz. Video referansları, her biri en fazla 3 saniye uzunluğunda olmak üzere en fazla 3 klip destekler.
- Birden fazla videoda referans verme veya akıl yürütme desteklenmez. Çok videolu istem denemek, model performansının düşmesine veya beklenmedik çıktılara neden olabilir.
- Sağlanan işleme hızı desteklenmez.
- Sistem talimatları, sıcaklık, `top_p`, durdurma dizileri ve olumsuz istemler desteklenmez (olumsuz istemlerinizi normal isteme ekleyebilirsiniz: ör. "X yapma").
- YouTube videolarının medya kaynağı olarak kullanılması desteklenmez.

## Teknik ayrıntılar

- Üretilen tüm videolarda, izleyiciler tarafından görünmeyen ancak kaynağın doğrulanması için programatik olarak algılanabilen SynthID filigranı bulunur.
- Video oluşturma süreleri; süreye, çözünürlüğe ve mevcut API yüküne göre değişir. Daha uzun ve daha yüksek çözünürlüklü videoların oluşturulması daha uzun sürer.
- Omni, hem giriş istemlerine hem de oluşturulan videoya (bölgeye göre değişir) içerik güvenliği filtreleri uygular. Kullanım politikalarını ihlal eden istemler engellenir.
- İngilizce (EN) tam olarak desteklenir ancak diğer diller değerlendirilmediğinden çalışabilir ancak sonuçlar değişebilir.

## Gemini Omni Flash istem rehberi

Bu bölümde, Gemini Omni Flash'e etkili istemler yazmayla ilgili ipuçları ve örnekler yer almaktadır.

### Tek sahne

Omni Flash, varsayılan olarak birkaç farklı çekimden oluşan bir video oluşturmaya çalışır.
İstemden yola çıkarak ilgi çekici bir anlatı oluşturmaya çalışır.

Çıkış videosunun tek bir sahne içermesini istiyorsanız bunu istemde belirtmeniz gerekir:

- Tek bir kesintisiz sahnede
- Tek kesintisiz çekimde
- Sahne kesintisi yok

Örneğin:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### İstenmeyen öğeleri kaldırma

Oluşturulan videoda istemediğiniz şeyler varsa bunları önlemek için basit olumsuz istemler ekleyin:

- Diyalog yok
- Süsleme yok
- Ek ses efektleri yok

### Düzenleme istemleri

Video düzenleme için en iyi sonucu basit istemler verir. Aşırı açıklayıcı istemler, istenmeyen değişikliklere yol açabilir.

Aşağıda, basit düzenleme istemlerine dair daha fazla örnek verilmiştir:

- Bu videoyu animeye dönüştür
- Bu kişiye şık bir şapka tak
- Işıklandırmayı daha dramatik hale getirme
- Tabeladaki metni "Omni Flash" olarak değiştirin.

Videonun belirli bir yönünü düzenlerken görsel tutarlılığı korumak için `"Keep everything else the same"` simgesini ekleyin.

Bu tekniğin nasıl uygulanacağını gösteren bazı örnekleri aşağıda bulabilirsiniz:

- **Kaçınılması gerekenler:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Basitleştirin:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Kaçınılması gerekenler:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Basitleştirin:** `Make the phone invisible. Keep everything else the
    same.`

### Ses istemi

Model, varsayılan olarak bir video için uygun bir ses parçası oluşturmaya çalışır. Bu her zaman istediğiniz sonuç olmayabilir. İsteminizi kullanarak istediğiniz ses türünü açıklayabilirsiniz. Bu durum, özellikle videonuzda müzik kullanmak istiyorsanız önemlidir:

- Sakinleştirici arka plan müziği ekleyin
- Videoda yüksek enerjili bir tekno ritmi var.
- Arka planda, şarkı çalan düşük kaliteli bir radyo yayını duyuluyor.

### Zamanlama etkinlikleri

Videoda belirli zamanlarda gerçekleşmesini istediğiniz olayları istemek için doğal dil kullanabilirsiniz. Bu özellik, özellikle kendi sahne kesimlerinizi, ritminizi veya hızlı çekim dizilerinizi oluştururken kullanışlıdır.
Örnekler için aşağıdakilere bakın:

- 3 saniye sonra bir kadın sahneye giriyor.
- 5. saniyede arka plan sesinde koro başlıyor.
- Her 2 saniyede bir yeni kareye geçiş yapın.
- Hızlı çekim dizisinde, her yarım saniyede (24 kare/sn hızında 12 kare) sahneyi yeni bir konuma değiştirin.

Ayrıca bir zaman kodu söz dizimi de kullanabilirsiniz:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta istem

Gemini Omni Flash'ten video oluşturmayla ilgili genel niteliklere veya ilkelere dikkat etmesini isteyebilirsiniz:

- Çok zengin ve ayrıntılı ancak tamamen doğal bir sahne oluşturmak için mikro ayrıntıları, ifadeyi ve zamanlamayı göz önünde bulundurun.
- Karakter ve ortam açıklamalarınızda son derece ayrıntılı olun.
  Karakterlere kostüm tasarım ilkelerini uygulayın. Sahnedeki kişiler, öğeler ve nesneler hakkında çok net olun.
- Sahnenin gerçekçi ve doğal görünmesi için arka plan öğelerine uygun ayrıntılar ekleyin.
- Her saniyede farklı bir nadir `[thing]` gösteren, hızlı tempolu müzik içeren ve öğeleri etiketlemek için metin eklenmiş bir video oluştur.

### Videolardaki metinler

Videonuzda metin olmasını isteyebilirsiniz. Gemini Omni, metni doğru ve okunabilir şekilde oluşturur. Videonuzda arka plan öğelerinde bile doğal olarak oluşan metinler varsa ne söylemesi gerektiğini tanımlamak faydalı olabilir.

- Ekranda tek seferde bir kelime: "did, you, know, that, Omni, can, do,
  awesome, text?" ("Omni'nin, harika, metinler, oluşturabildiğini, biliyor, muydunuz?") Her kelime, farklı bir animasyon stiliyle 1 saniye boyunca görünür. Diyalog yok.
- "Bu, Omni tarafından üretilen bir yapay zeka görüntüsüdür" yazan bir sokak tabelası, "İhtiyacınız olan tüm yapay zeka" yazan bir vitrin ve "OMNI1.1" plakalı bir araba var.

### Videoları uzatmaya yönelik istemler

Gemini Omni 1.1 Flash ile `"Extend this video"` veya `"The scene continues"` gibi istemlerle videoları uzatabilirsiniz. Videoları 10 saniye uzatarak toplam uzunluğu 40 saniyeye çıkarabilirsiniz.

Omni, orijinal videonuzun son 10 saniyesini bağlam olarak kullanarak video, hareket, karakter ve sesin tutarlı olmasını sağlayan bir uzantı oluşturur. Giriş videonuzdaki son karelerden bazıları, geçişin sorunsuz olması için düzenlenir.

Uzatma işlemi yaparken bu kılavuzdaki tüm Omni istemi ipuçları geçerliliğini korur:

- Genişletilmiş sahnenizdeki sesi açıklayın. Özellikle değiştirilmesi gerekiyorsa bu açıklamayı yapın: `"The music continues into the chorus"`
- Sahnenin devam edip etmediğini veya yeni bir sahneye geçiş yapılıp yapılmadığını (belki aynı karakterlerle) açıklayın: `"Show the same characters in the next scene"`
- Çıkışlarınızın doğru olmasını sağlamak veya yeni karakterler tanıtmak için genişletme yaparken referans olarak resim ve video ekleyin: `"The person shown in the reference image enters the scene"`, `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- Zaman damgaları veya zaman kodu söz dizimi kullanılıyorsa 0s, videonun uzatılmış kısmının başlangıcını ifade eder. 10 saniyelik bir videoyu uzatıyorsanız bu istemdeki sahne kesimi 12 saniye sonra gerçekleşir: `"After 2s cut to a new scene with the same characters"`

### İstemlerde etiket kullanarak resim ve video rollerini ayarlama

Yüklenen medyaları belirli üretim rollerine bağlamak için etiketleri kullanabilirsiniz. Bu sayede her resmin veya videonun başlangıç karesi, son kare ya da referans olup olmadığını belirleyebilirsiniz.

#### 1. Basit etiketler (önerilen)

Medya rollerinin istemden açıkça anlaşıldığı basit durumlarda, resimleri ve videoları doğrudan rollere bağlayabilirsiniz:

- **`<FIRST_FRAME>`**: Örneğin, `<FIRST_FRAME> a woman is walking` gibi durumlarda videonun başlangıç karesi olarak resmi kullanın.
- **`<LAST_FRAME>`**: Geçiş yapılacak videonun son karesi olarak kullanın. `<FIRST_FRAME>` ile birlikte kullanılmalıdır. Örneğin: `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: Resmi referans olarak kullanın. Örneğin: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (ilk resimdeki stil referansını ve ikinci resimdeki özne referansını birleştirir).
  Resim referansları 0'dan başlar.
- **`<VIDEO_REF_N>`**: Videoyu karakter veya nesne referansı olarak kullanma (örneğin:
  `the person in <VIDEO_REF_0> is playing the violin`). Video referansları da 0'dan başlar.

Aşağıda 6 referans resim içeren bir örnek verilmiştir:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Kaynakları ve referansları belirtme

Birden fazla medya girişi ve birden fazla rol içeren daha karmaşık durumlarda, doğal dil talimatlarıyla eşleştirilmiş açık önek etiketlerini kullanabilirsiniz. Bu kaynakları ve referansları isteminizin başında belirtmeniz gerekir.

- `[# Sources <FIRST_FRAME>@Image1]`, başlangıç karesi olarak ilk resmi kullanır.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]`, ilk resmi başlangıç karesi, ikinci resmi ise son kare olarak kullanır.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]`, ilk resmi hem ilk kare hem de son kare olarak kullanarak döngüye giren bir video oluşturur.
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]`, ilk resmi başlangıç karesi, ikinci resmi ise referans olarak kullanır.
- `[# Sources <VIDEO_0>@Video1]`, düzenleme veya değiştirme için videoyu birincil kaynak video olarak kullanır.
- `[# Sources <PREVIOUS_VIDEO>@Video1]`, önceki dönüşteki videoyu uzatmak için kullanacak.
- `[# References <IMAGE_REF_0>@Image1]`, ilk resmi referans olarak kullanır.
- `[# References <IMAGE_REF_1>@Image2]`, ikinci resmi referans olarak kullanır.
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]`, her iki resmi de referans olarak kullanır.
- `[# References <VIDEO_REF_0>@Video1]`, ilk videoyu referans olarak kullanır.
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]`, hem resmi hem de videoyu referans olarak kullanır.

İsteminize yönlendirici talimatlar ekleyin:

- Başlangıç karesi için: `"Use this image as the starting frame."`
- Başlangıç ve bitiş kareleriyle döngüye alınan video için: `"Use this image as the first frame and the last frame."`
- Referans resimler için: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- Referans videolar için: `"Use the given video(s) as references. Do not use them as a source for video editing."`

Kaynak ve referans beyanları içeren istemlere dair bazı örnekler:

**Başlangıç karesi, referans resimle birleştirildi:**

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**Karakter referans videosu ile nesne referans görselinin birleştirilmesi:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## Sırada ne var?

- [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=tr)'de denemeler yaparak Gemini Omni Flash'i kullanmaya başlayın.
- [İstem tasarımına giriş](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=tr) başlıklı makalemizden yararlanarak daha iyi istemler yazmayı öğrenin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-08-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-08-30 UTC."],[],[]]
