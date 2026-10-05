---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=ar
fetched_at: 2026-10-05T06:37:25.918668+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0627\u0644\u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a \u0648\u062a\u0639\u062f\u064a\u0644\u0647\u0627 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء الفيديوهات وتعديلها باستخدام Gemini Omni Flash

‫Gemini Omni Flash (`gemini-omni-1.1-flash`) هو نموذج متعدد الوسائط عالي الأداء مصمّم لإنشاء الفيديوهات وتعديلها والتحكّم بها سينمائيًا بسرعة عالية.
يستند Gemini Omni إلى الإمكانات الأساسية التالية التي تميّزه عن نماذج الفيديوهات السابقة:

- **تعدُّد الوسائط:** يعالج النصوص والصور والمقاطع الصوتية والفيديوهات في الوقت نفسه، ما يمنحك نتائج أكثر تماسكًا واتساقًا وقابلية للتحكّم.
- **التعديل الحواري:** يتيح لك هذا الخيار، الذي توفّره [واجهة برمجة التطبيقات Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar)، تحسين فيديوهاتك وتعديلها بشكل متكرّر من خلال محادثة باللغة الطبيعية. صِف التغييرات التي تريد إجراءها، وسيُطبّق النموذج التعديل مع الحفاظ على أجزاء الفيديو التي تريد الاحتفاظ بها.
- **المعرفة بالعالم:** يجمع Gemini Omni بين فهم الفيزياء ومعرفة Gemini بالتاريخ والعلوم والسياق الثقافي، ما يتيح الانتقال من الواقعية الفوتوغرافية إلى السرد القصصي الهادف.

## إنشاء فيديو من نص

إنشاء فيديو من طلب نصي ينشئ النموذج فيديو مع محتوى صوتي
استنادًا إلى الوصف النصي الذي تقدّمه. اكتب طلبات تتضمّن تفاصيل مثل وصف المشهد وحركة الكاميرا والإضاءة والمزاج للحصول على أفضل النتائج.

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(
            InteractionsInput.of(
                "A marble rolling fast on a chain reaction style track, continuous smooth shot."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("marble.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(
                "A marble rolling fast on a chain reaction style track, continuous smooth shot.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("marble.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

### مخطط استجابة REST

حقل الراحة `interaction.output_video` هو **حقل خاص بحزمة تطوير البرامج (SDK) فقط**.
احصل على ناتج الفيديو من مصفوفة `steps` عند استخدام REST API مباشرةً.

**بنية JSON REST غير المُعالَجة:**

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

### التحكّم في نسبة العرض إلى الارتفاع

اضبطوا `aspect_ratio` على `"9:16"` لإنشاء فيديوهات باتجاه عمودي. يكون الوضع الأفقي (16:9) هو الوضع التلقائي.

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormatAspectRatio;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .aspectRatio(VideoResponseFormatAspectRatio.of("9:16"))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(
            InteractionsInput.of(
                "A futuristic city with neon lights and flying cars, cyberpunk style"))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    videoFormat := interactions.VideoResponseFormat{
        AspectRatio: interactions.VideoResponseFormatAspectRatioNineHundredAndSixteen.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(
                "A futuristic city with neon lights and flying cars, cyberpunk style",
            ),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

### دقة عرض الفيديو

يمكنك التحكّم في درجة دقة الفيديو الذي تم إنشاؤه باستخدام المَعلمة `resolution`
في `response_format`. درجة الدقة التلقائية هي 720p.

| القيمة | الوصف |
| --- | --- |
| `360p` | درجة دقة العرض 360p |
| `720p` | دقة عرض الفيديو 720p (الإعداد التلقائي) |
| `1080p` | إخراج بدقة 1080p (محسَّنة) |
| `4k` | إخراج بدقة 4K (محسّنة) |

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Resolution;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .resolution(Resolution.of("1080p"))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A drone shot of a mountain landscape at sunrise."))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("hires.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    videoFormat := interactions.VideoResponseFormat{
        Resolution: interactions.ResolutionOneThousandAndEightyp.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A drone shot of a mountain landscape at sunrise."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("hires.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

[

لا يدعم متصفّحك علامة الفيديو.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_misty_mountains_1080p.mp4)

## إنشاء فيديو من صورة

يمكنك تقديم صورة مرجعية مع طلبك النصي. استنادًا إلى طلبك، سيقرّر النموذج كيفية استخدام الصورة. هذه الميزة مفيدة لتحويل لقطات المنتجات أو الرسوم التوضيحية أو الصور الفوتوغرافية إلى فيديوهات.

يوضّح المثال التالي كيفية استخدام الصورة المرجعية لرسم سمكة تقفز من الماء:

![رسم لسمكة تقفز خارج الماء](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=ar)

باستخدام الطلب التالي:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

لإنشاء فيديو واقعي للرسمة

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

### جافا

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

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("drawing.jpg"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Content imageContent =
    ImageContent.builder()
        .data(base64Image)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content textContent =
    TextContent.builder()
        .text(
            "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video")
        .build();

List<Content> contents = Arrays.asList(imageContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("clownfish.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    imageBytes, err := os.ReadFile("drawing.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(base64Image),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("clownfish.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

### تضمين إطارات بين الإطارين الأول والأخير

يتيح Gemini Omni Flash إنشاء فيديوهات تتضمّن استيفاءً للفواصل الزمنية بين اللقطات، ما يسمح لك بإنشاء فيديو ينتقل بسلاسة بين صورة البداية (الإطار الأول) وصورة النهاية (الإطار الأخير).

قدِّم صورتَين في قائمة `input` واشرح الانتقال المطلوب في طلبك. سيحرّك النموذج المشهد من الإطار الأول إلى الإطار الأخير.

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

### جافا

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

Client client = new Client();

String firstFrameB64 =
    Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("first_frame.jpg")));
String lastFrameB64 =
    Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("last_frame.jpg")));

Content firstFrame =
    ImageContent.builder()
        .data(firstFrameB64)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content lastFrame =
    ImageContent.builder()
        .data(lastFrameB64)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content prompt =
    TextContent.builder()
        .text(
            "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.")
        .build();

List<Content> contents = Arrays.asList(firstFrame, lastFrame, prompt);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("interpolation.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    firstBytes, err := os.ReadFile("first_frame.jpg")
    if err != nil {
        log.Fatal(err)
    }
    lastBytes, err := os.ReadFile("last_frame.jpg")
    if err != nil {
        log.Fatal(err)
    }

    firstFrameB64 := base64.StdEncoding.EncodeToString(firstBytes)
    lastFrameB64 := base64.StdEncoding.EncodeToString(lastBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(firstFrameB64),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(lastFrameB64),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("interpolation.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

[

لا يدعم متصفّحك علامة الفيديو.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_keyframe_interpolation.mp4)

### معرّف الموضوع

يمكنك إنشاء فيديو يتضمّن مواضيع محدّدة مقدَّمة كصور مرجعية.
على سبيل المثال، يوضّح الرمز التالي كيفية تقديم صورتَين لقطة وخيط
لإنشاء فيديو للقطة وهي تلعب بالخيط.

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

### جافا

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

Client client = new Client();

String catB64 = Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("cat.png")));
String yarnB64 = Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("yarn.png")));

Content catImage =
    ImageContent.builder()
        .data(catB64)
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

Content yarnImage =
    ImageContent.builder()
        .data(yarnB64)
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

Content textContent =
    TextContent.builder()
        .text("A cat playfully batting at a ball of yarn.")
        .build();

List<Content> contents = Arrays.asList(catImage, yarnImage, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("cat.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    catBytes, err := os.ReadFile("cat.png")
    if err != nil {
        log.Fatal(err)
    }
    yarnBytes, err := os.ReadFile("yarn.png")
    if err != nil {
        log.Fatal(err)
    }

    catB64 := base64.StdEncoding.EncodeToString(catBytes)
    yarnB64 := base64.StdEncoding.EncodeToString(yarnBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(catB64),
            MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
        }),
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(yarnB64),
            MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "A cat playfully batting at a ball of yarn.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("cat.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

### مَعلمة المهام

استخدِم المَعلمة `task` في `video_config` لتحديد السلوك المطلوب بشكل صريح، مثلاً إذا أردت أن ينشئ النموذج فيديو من صورة، يمكنك ضبط المَعلمة على `image_to_video`. إذا لم يتم ضبط هذه السمة، سيستنتج النموذج ما تريده من الطلب.

في ما يلي القيم المسموح بها:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

يوضّح المثال التالي كيفية ضبط ذلك على المثال السابق الذي يعرض صورة
إلى فيديو.

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Task;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoConfig;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("drawing.jpg"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Content imageContent =
    ImageContent.builder()
        .data(base64Image)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content textContent =
    TextContent.builder()
        .text(
            "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video")
        .build();

List<Content> contents = Arrays.asList(imageContent, textContent);

GenerationConfig generationConfig =
    GenerationConfig.builder()
        .videoConfig(VideoConfig.builder().task(Task.IMAGE_TO_VIDEO).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .generationConfig(generationConfig)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    imageBytes, err := os.ReadFile("drawing.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(base64Image),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video",
        }),
    }

    generationConfig := &interactions.GenerationConfig{
        VideoConfig: &interactions.VideoConfig{
            Task: interactions.TaskImageToVideo.ToPointer(),
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:            interactions.Model("gemini-omni-1.1-flash"),
            Input:            interactions.NewInteractionsInput(contents),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

## تعديل الفيديوهات مع الحفاظ على السياق

إنشاء فيديو وتعديله بشكل متكرّر باستخدام طلبات متابعة يستند كل رد إلى النتيجة السابقة. يتذكّر النموذج سياق الفيديو، ويطبّق التغييرات التي أجريتها مع الحفاظ على العناصر التي لم تذكرها. استخدِم
`previous_interaction_id` لتتبُّع سجلّ المحادثات وحالة الفيديو الذي تم إنشاؤه بدون إعادة تحميل الفيديو السابق.

يوضّح المثال التالي كيفية إنشاء فيديو أولاً ثم تعديله:

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

// Turn 1: Generate initial video
CreateModelInteraction turn1Params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A woman playing violin outdoors."))
        .build();

Interaction res1 =
    client.interactions.create(CreateInteractionRequestBody.of(turn1Params)).interaction().get();

// Turn 2: Edit the previous video
CreateModelInteraction turn2Params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .previousInteractionId(res1.id().get())
        .input(InteractionsInput.of("Make the violin invisible."))
        .build();

Interaction res2 =
    client.interactions.create(CreateInteractionRequestBody.of(turn2Params)).interaction().get();

if (res2.outputVideo().isPresent() && res2.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(res2.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    // Turn 1: Generate initial video
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A woman playing violin outdoors."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Edit the previous video
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-omni-1.1-flash"),
            PreviousInteractionID: res1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Make the violin invisible."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res2.Interaction.OutputVideo != nil && res2.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res2.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

مثال على فيديو أولي:

مثال على فيديو معدَّل:

يؤدي كل رد في المحادثة إلى إنشاء فيديو جديد. يفهم النموذج السياق من المحادثات السابقة، ما يتيح لك إجراء تغييرات تدريجية، مثل تعديل الإضاءة وتبديل الخلفيات، بدون إعادة وصف المشهد بأكمله.

### تعديل فيديوهاتك

حمِّل فيديوهاتك باستخدام [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) لتعديلها
باستخدام Gemini Omni Flash.

يوضّح المثال التالي كيفية تعديل الفيديو الأصلي التالي:

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
        {"type": "video", "uri": video_file.uri},
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
    { type: 'video', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload video using the file API
File videoFile =
    client.files.upload("Video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (videoFile.state().isPresent()
    && videoFile.state().get().knownEnum() == FileState.Known.PROCESSING) {
  System.out.println("Waiting for video to be processed.");
  Thread.sleep(10000);
  videoFile = client.files.get(videoFile.name().get(), null);
}

if (videoFile.state().isPresent()
    && videoFile.state().get().knownEnum() == FileState.Known.FAILED) {
  throw new IllegalStateException("Video processing failed: " + videoFile.state().get());
}
System.out.println("Video processing complete: " + videoFile.uri().orElse(""));

// Edit your video
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content textContent =
    TextContent.builder()
        .text(
            "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
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
    "time"

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

    // Upload video using the file API
    videoFile, err := client.Files.UploadFromPath(ctx, "Video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for videoFile.State == genai.FileStateProcessing {
        fmt.Println("Waiting for video to be processed.")
        time.Sleep(10 * time.Second)
        videoFile, err = client.Files.Get(ctx, videoFile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    if videoFile.State == genai.FileStateFailed {
        log.Fatalf("Video processing failed: %s", videoFile.State)
    }
    fmt.Printf("Video processing complete: %s\n", videoFile.URI)

    // Edit your video
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
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

مثال على فيديو معدَّل:

## استرداد الفيديوهات باستخدام معرّف موارد منتظم (URI)

استخدِم المَعلمة `delivery="uri"` في
`response_format` لاسترداد الفيديوهات التي تم إنشاؤها والتي يزيد حجمها عن 4 ميغابايت.
تعرض هذه الطريقة معرّف موارد منتظم (URI) مستضافًا على Google يمكنك استخدامه للاستقصاء إلى أن يصبح الفيديو `ACTIVE` قبل تنزيله.

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

// 1. Request video using URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract filename and poll for ACTIVE state
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormatDelivery;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;

Client client = new Client();

// 1. Request video using URI delivery
VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .delivery(VideoResponseFormatDelivery.URI)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A beautiful sunset."))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// 2. Extract filename and poll for ACTIVE state
VideoContent videoOutput = interaction.outputVideo().get();
String uri = videoOutput.uri().get();
String[] parts = uri.split("/");
String fileName = parts[parts.length - 1];

System.out.println("Waiting for video processing...");
while (true) {
  File fileInfo = client.files.get("files/" + fileName, null);
  if (fileInfo.state().isPresent()
      && fileInfo.state().get().knownEnum() == FileState.Known.ACTIVE) {
    break;
  } else if (fileInfo.state().isPresent()
      && fileInfo.state().get().knownEnum() == FileState.Known.FAILED) {
    throw new RuntimeException("Generation failed.");
  }
  Thread.sleep(5000);
}

// 3. Download the final video
client.files.download(uri, "output.mp4", null);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"
    "strings"
    "time"

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

    // 1. Request video using URI delivery
    videoFormat := interactions.VideoResponseFormat{
        Delivery: interactions.VideoResponseFormatDeliveryURI.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A beautiful sunset."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Extract filename and poll for ACTIVE state
    uri := *res.Interaction.OutputVideo.URI
    parts := strings.Split(uri, "/")
    fileName := parts[len(parts)-1]

    fmt.Println("Waiting for video processing...")
    var fileInfo *genai.File
    for {
        fileInfo, err = client.Files.Get(ctx, "files/"+fileName, nil)
        if err != nil {
            log.Fatal(err)
        }
        if fileInfo.State == genai.FileStateActive {
            break
        } else if fileInfo.State == genai.FileStateFailed {
            log.Fatal("Generation failed.")
        }
        time.Sleep(5 * time.Second)
    }

    // 3. Download the final video
    videoBytes, err := client.Files.Download(ctx, genai.NewDownloadURIFromFile(fileInfo), nil)
    if err != nil {
        log.Fatal(err)
    }
    if err := os.WriteFile("output.mp4", videoBytes, 0644); err != nil {
        log.Fatal(err)
    }
}
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

**بنية JSON غير مُعالَجة لخدمة REST (معرّف الموارد المنتظم):**

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

## إضافة الفيديو

توسيع فيديو حالي من خلال إنشاء تكملة سلسة في نهاية المقطع اكتب في طلبك وصفًا لكيفية استكمال أحداث الفيديو، مثلاً
`"Extend this video"` أو `"Continue the scene: the camera pans across the mountains"`.
يحلّل النموذج الفيديو المُدخَل لإنشاء فيديو مدّته من 3 إلى 10 ثوانٍ يكمّل أحداث الفيديو الأصلي.

يمكنك تمديد:

- **الفيديوهات التي ينشئها النموذج (محادثة مترابطة)**: يمكنك توسيع فيديو تم إنشاؤه سابقًا من خلال الإشارة إلى `previous_interaction_id`.
- **الفيديوهات التي تم تحميلها**: قدِّم ملف فيديو تم تحميله (عبر Files API) مع طلب الإضافة.

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
        {"type": "video", "uri": video_file.uri},
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
    { type: 'video', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload your video using the Files API
File videoFile =
    client.files.upload(
        "my_video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

// Extend the video using prompt-based extension
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content textContent = TextContent.builder().text("Continue the scene.").build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("extended.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    // Upload your video using the Files API
    videoFile, err := client.Files.UploadFromPath(ctx, "my_video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    // Extend the video using prompt-based extension
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Continue the scene.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("extended.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "video", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

[

لا يدعم متصفّحك علامة الفيديو.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_base.mp4)

[

لا يدعم متصفّحك علامة الفيديو.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_extended.mp4)

### التوسّع باستخدام الوسائط المرجعية

يمكنك تقديم صور مرجعية في مصفوفة `input` مع الطلب الخاص بك لتقديم شخصيات أو عناصر جديدة في الفيديو الموسّع:

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
        {"type": "video", "uri": video_file.uri},
        {"type": "image", "uri": character_img.uri},
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
    { type: 'video', uri: videoFile.uri },
    { type: 'image', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload base video and reference image using the Files API
File videoFile =
    client.files.upload(
        "my_video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());
File characterImg =
    client.files.upload(
        "character.png", UploadFileConfig.builder().mimeType("image/png").build());

// Extend the video while introducing the reference character
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content imageContent = ImageContent.builder().uri(characterImg.uri().get()).build();
Content textContent =
    TextContent.builder()
        .text(
            "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.")
        .build();

List<Content> contents = Arrays.asList(videoContent, imageContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("extended_with_character.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    // Upload base video and reference image using the Files API
    videoFile, err := client.Files.UploadFromPath(ctx, "my_video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }
    characterImg, err := client.Files.UploadFromPath(ctx, "character.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    // Extend the video while introducing the reference character
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.ImageContent{
            URI: genai.Ptr(characterImg.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("extended_with_character.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
  "input": [
    {"type": "video", "uri": "'$VIDEO_URI'"},
    {"type": "image", "uri": "'$CHARACTER_IMG_URI'"},
    {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
  ]
}'
```

[

لا يدعم متصفّحك علامة الفيديو.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_traveler_extension.mp4)

### القيود والإرشادات المتعلّقة بالإضافات

يُرجى مراعاة القواعد والقيود التالية عند تمديد الفيديوهات:

- **المحادثات المنطوقة في الفيديوهات المحمّلة**: لا يمكنك حاليًا إضافة محادثات إضافية إلى فيديو محمّل يتضمّن محادثة منطوقة (يمكنك إجراء ذلك إذا لم يتضمّن الفيديو أي محادثة منطوقة أو إذا لم يضف الطلب محادثة منطوقة).
- **إضافة صوتية للمحادثة المترابطة**: يمكن إنشاء حوار أو كلام منطوق عند إضافة محتوى إلى فيديوهات تم إنشاؤها سابقًا من خلال محادثة مترابطة (`previous_interaction_id`).
- **نهاية المقطع فقط**: تقتصر الإضافة على إلحاقها بنهاية الفيديو.
  لا يمكنك إضافة محتوى في بداية المقطع أو توسيع وسطه.
- **حدّ المدة**: يجب أن تكون مدة الفيديوهات التي يتم إدخالها لإنشاء الإضافة 10 ثوانٍ أو أقل عند التحميل (إلا إذا كنت تستخدم المحادثة المترابطة).
- **التوفّر حسب المنطقة**: لا تتوفّر حاليًا ميزة تمديد الفيديوهات التي تم تحميلها للمستخدمين في المنطقة الاقتصادية الأوروبية وسويسرا والمملكة المتحدة (تتوفّر ميزة تمديد الفيديوهات التي أنشأها النموذج في جميع المناطق التي تتوفّر فيها).

## أفضل الممارسات

- **استخدام عرض المحتوى عبر معرّف الموارد الموحّد (URI) للفيديوهات الكبيرة:** بالنسبة إلى الفيديوهات التي يزيد حجمها عن 4 ميغابايت (أكبر من 720p عند توفّرها)، استخدِم `delivery="uri"` في `response_format` لتجنُّب حدود حجم الحمولة.
- **الأداء المحسّن:** اضبط `background=false` و`store=false` و`stream=false` لإنشاء رموز أحادية أسرع ومتزامنة. يُرجى العِلم أنّ ضبط
  `store=false` يعني أنّه لن يكون بالإمكان تعديل الفيديو الذي تم إنشاؤه في المحادثات اللاحقة باستخدام `previous_interaction_id`.
- **دقة الطلب:** يُرجى الاطّلاع على قسم [إرشادات الطلب](#prompt-guide) للحصول على التفاصيل.

## القيود

- لا تتوفّر إمكانية تحميل وتعديل الصور التي تتضمّن قاصرين في المنطقة الاقتصادية الأوروبية وسويسرا والمملكة المتحدة.
- لا يمكن تحميل وتعديل الصور التي تحتوي على أشخاص معيّنين يمكن التعرّف عليهم.
- لا تتوفّر حاليًا إمكانية تعديل الفيديوهات التي تم تحميلها أو تمديدها للمستخدمين في المنطقة الاقتصادية الأوروبية وسويسرا والمملكة المتحدة (تتوفّر إمكانية تعديل الفيديوهات التي أنشأها النموذج أو تمديدها).
- يجب أن تكون مدة الفيديوهات التي يتم إدخالها لتعديلها وتوسيعها 10 ثوانٍ أو أقل عند تحميلها (ما لم يتم توسيع الفيديوهات التي أنشأها النموذج في محادثة مترابطة).
- يقتصر امتداد الفيديو على الإضافة إلى نهاية الفيديو، ولا يمكن إضافة مقطع في بداية الفيديو أو في منتصفه.
- لا يمكنك تمديد فيديو تم تحميله يتضمّن شخصًا يتحدث لإضافة حوار إضافي (يمكن أن تبقى الشخصيات صامتة، أو يمكن استخدام ميزة التمديد المتعدد مع `previous_interaction_id`).
- لا يمكن إجراء تعديل صوتي.
- لا يتيح الإصدار الحالي من واجهة برمجة التطبيقات تحميل المراجع الصوتية.
- تعمل المراجع المرئية بشكل أفضل مع الصور المشابهة، ويتم تجاهل أي محتوى صوتي في المرجع المرئي. يمكن أن تتضمّن مراجع الفيديو 3 مقاطع كحدّ أقصى، تصل مدة كل منها إلى 3 ثوانٍ.
- لا يمكن الإشارة إلى محتوى في فيديوهات متعددة أو تقديم أسباب استنادًا إلى محتوى في فيديوهات متعددة. قد تؤدي محاولة استخدام طلبات متعددة الفيديوهات إلى تدهور أداء النموذج أو ظهور نتائج غير متوقعة.
- لا تتوفّر ميزة "معدل النقل المحدّد".
- لا تتوفّر تعليمات النظام ودرجة الحرارة و`top_p` وتسلسلات الإيقاف والطلبات السلبية (يمكنك وضع الطلبات السلبية في الطلب العادي، مثلاً "لا تفعل X").
- لا يمكن استخدام فيديوهات YouTube كمصدر للوسائط.

## التفاصيل الفنية

- تتضمّن جميع الفيديوهات التي يتم إنشاؤها علامات مائية من SynthID، وهي غير مرئية للمشاهدين ولكن يمكن رصدها آليًا للتحقّق من مصدرها.
- تختلف أوقات إنشاء الفيديوهات استنادًا إلى المدة ودرجة الدقة وحِمل واجهة برمجة التطبيقات الحالي. يستغرق إنشاء الفيديوهات الأطول والأعلى دقة وقتًا أطول.
- تطبّق Omni فلاتر أمان المحتوى على طلبات الإدخال والفيديوهات التي يتم إنشاؤها (تختلف حسب المنطقة). يتم حظر الطلبات التي تنتهك سياسات الاستخدام.
- اللغة الإنجليزية (EN) متوافقة تمامًا، ولكن لم يتم تقييم اللغات الأخرى، لذا قد تعمل ولكن قد تختلف النتائج.

## دليل كتابة الطلبات المُوجَّهة إلى Gemini Omni Flash

يتضمّن هذا القسم نصائح وأمثلة حول كيفية توجيه الطلبات إلى Gemini Omni Flash بفعالية.

### مشهد واحد

سيحاول Omni Flash تلقائيًا إنشاء فيديو يتضمّن بعض اللقطات المختلفة.
سيحاول إنشاء سرد مثير للاهتمام استنادًا إلى الطلب.

إذا كنت تريد أن يحتوي الفيديو الناتج على مشهد واحد، عليك تقديم طلب بذلك:

- في مشهد واحد متواصل
- في لقطة واحدة متواصلة
- لا تتوفّر إمكانية قطع المشهد

على سبيل المثال:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### إزالة العناصر غير المرغوب فيها

إذا كان الفيديو الذي تم إنشاؤه يتضمّن عناصر لا تريدها، أضِف طلبات سلبية بسيطة لتجنُّبها:

- ما مِن حوار
- بدون تحسينات
- ما مِن تأثيرات صوتية إضافية

### طلبات التعديل

تعمل الطلبات البسيطة بشكل أفضل عند تعديل الفيديوهات. يمكن أن تؤدي الطلبات الوصفية المفرطة إلى تغييرات غير مقصودة.

في ما يلي المزيد من الأمثلة على طلبات التعديل البسيطة:

- حوِّل هذا الفيديو إلى أنمي
- ضَع قبعة عصرية على هذا الشخص
- غيِّر الإضاءة لتكون أكثر درامية
- تغيير النص على اللافتة إلى "Omni Flash"

عند تعديل جانب معيّن من الفيديو، أدرِج `"Keep everything else the same"` للحفاظ على التناسق المرئي.

في ما يلي بعض الأمثلة لتوضيح كيفية تطبيق هذه التقنية:

- **تجنَّب ما يلي:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **التبسيط:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **تجنَّب ما يلي:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **التبسيط:** `Make the phone invisible. Keep everything else the
    same.`

### طلب المحتوى الصوتي

سيحاول النموذج تلقائيًا إنشاء مقطع صوتي مناسب لفيديو. قد لا يكون هذا هو ما تريده دائمًا. يمكنك استخدام الطلب لوصف نوع المحتوى الصوتي الذي تريده. هذا مهم بشكل خاص إذا أردت تضمين موسيقى في الفيديو:

- تضمين موسيقى هادئة في الخلفية
- يتضمّن الفيديو موسيقى تكنو صاخبة
- المقطع الصوتي هو بث إذاعي منخفض الجودة في الخلفية، ويتم فيه تشغيل أغنية

### أحداث التوقيت

يمكنك طلب تنفيذ إجراءات في أوقات معيّنة من الفيديو، ولا حاجة إلى استخدام بنية دقيقة، بل يمكنك استخدام اللغة الطبيعية. ويفيد ذلك بشكل خاص في إنشاء مقاطع المشاهد الخاصة بك أو الإيقاع أو التسلسلات السريعة.
اطّلِع على ما يلي للاطّلاع على أمثلة:

- بعد 3 ثوانٍ، تدخل امرأة إلى المشهد.
- في الثانية 5، تبدأ اللازمة الموسيقية في الصوت في الخلفية.
- يتم الانتقال إلى إطار جديد كل ثانيتَين.
- في تسلسل سريع، غيِّر المشهد إلى موقع جديد كل نصف ثانية (12 لقطة بمعدل 24 لقطة في الثانية).

يمكنك أيضًا استخدام بنية رمز الوقت:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta prompting

يمكنك أن تطلب من Gemini Omni Flash الانتباه إلى الصفات العامة أو المبادئ العامة لإنشاء الفيديوهات:

- يجب مراعاة التفاصيل الدقيقة والتعبير والتوقيت لإنشاء مشهد غني بالتفاصيل
  وطبيعي تمامًا.
- يجب أن تكون تفاصيل الأوصاف الخاصة بالشخصيات والبيئات دقيقة للغاية.
  تطبيق مبادئ تصميم الأزياء على الشخصيات يجب أن تكون دقيقًا جدًا بشأن الأشخاص والأشياء والعناصر في المشهد.
- أضِف الكثير من التفاصيل المناسبة في عناصر الخلفية لجعل المشهد يبدو واقعيًا وطبيعيًا.
- أنشئ فيديو سريعًا يعرض `[thing]` مختلفًا نادرًا كل ثانية واحدة، مع موسيقى حماسية، وأدرِج نصًا لتسمية الشيء.

### النص في الفيديوهات

يمكنك تقديم طلب يتضمّن نصًا في الفيديو، وسيعرضه Gemini Omni بطريقة صحيحة وقابلة للقراءة. إذا كان الفيديو سيتضمّن نصًا يظهر بشكل طبيعي، حتى في عناصر الخلفية، من المفيد تحديد ما يجب أن يقوله.

- كلمة واحدة على الشاشة في كل مرة: "هل، تعلم، أنّ، Omni، يمكنه، إنشاء، نصوص، رائعة؟" تظهر كل كلمة لمدة ثانية واحدة بأسلوب متحرك مختلف. لا يوجد حوار.
- هناك لوحة إرشادية في الشارع مكتوب عليها: "هذا المحتوى من إنشاء الذكاء الاصطناعي في Omni"، وهناك واجهة متجر مكتوب عليها: "الذكاء الاصطناعي هو كل ما تحتاجه"، وهناك سيارة تحمل لوحة أرقام مكتوب عليها: "OMNI1.1"

### طلبات لإطالة مدة فيديو

باستخدام Gemini Omni 1.1 Flash، يمكنك توسيع الفيديوهات باستخدام طلبات مثل `"Extend this video"` أو `"The scene continues"`. يمكنك تمديد الفيديوهات بمقدار 10 ثوانٍ، وبإجمالي مدة يصل إلى 40 ثانية.

ينشئ Omni إضافة تحافظ على اتّساق الفيديو والحركة والشخصيات والصوت من خلال استخدام آخر 10 ثوانٍ من الفيديو الأصلي كسياق. سيتم تعديل بعض اللقطات الأخيرة في الفيديو المصدر لجعل الانتقال سلسًا.

عند التوسيع، تظل جميع نصائح Omni التالية سارية:

- قدِّم وصفًا للمحتوى الصوتي في المشهد الموسّع، خاصةً إذا كنت بحاجة إلى تغييره: `"The music continues into the chorus"`
- يجب توضيح ما إذا كان المشهد مستمرًا، أو ما إذا تم الانتقال إلى مشهد جديد (ربما مع الشخصيات نفسها): `"Show the same characters in the next scene"`
- يمكنك تضمين صور وفيديوهات كمراجع عند توسيع المحادثة للمساعدة في الحفاظ على دقة النتائج أو لتقديم شخصيات جديدة: `"The person shown in the reference image enters the scene"`، `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- في حال استخدام الطوابع الزمنية أو بنية رمز الوقت، يشير 0s إلى بداية الجزء الموسّع من الفيديو. في حال تمديد فيديو مدته 10 ثوانٍ، سيتم قطع المشهد في هذا الطلب بعد 12 ثانية: `"After 2s cut to a new scene with the same characters"`

### استخدام العلامات في الطلبات لضبط أدوار الصور والفيديوهات

يمكنك استخدام العلامات لربط الوسائط التي تم تحميلها بأدوار إنشاء محتوى معيّنة. يتيح لك ذلك تحديد ما إذا كانت كل صورة أو فيديو عبارة عن إطار بداية أو إطار نهاية أو مرجع.

#### 1. علامات بسيطة (يُوصى بها)

في الحالات البسيطة التي تكون فيها أدوار الوسائط واضحة من الطلب، يمكنك ربط الصور والفيديوهات بالأدوار مباشرةً:

- استخدِم **`<FIRST_FRAME>`**: لاستخدام الصورة كإطار بدء للفيديو، مثلاً: `<FIRST_FRAME> a woman is walking`
- ‫**`<LAST_FRAME>`**: استخدام الصورة كإطار نهائي للفيديو للانتقال إليه يجب استخدامها مع `<FIRST_FRAME>`، مثلاً: `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: استخدام الصورة كمرجع، على سبيل المثال: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (يجمع بين مرجع النمط من الصورة الأولى ومرجع العنصر من الصورة الثانية).
  تبدأ مراجع الصور من 0.
- **`<VIDEO_REF_N>`**: استخدام الفيديو كمرجع لشخصية أو كائن، مثلاً:
  `the person in <VIDEO_REF_0> is playing the violin` تبدأ مراجع الفيديو أيضًا من 0.

في ما يلي مثال على 6 صور مرجعية:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. تحديد المصادر والمراجع

في الحالات الأكثر تعقيدًا التي تتضمّن وسائط متعددة وأدوارًا متعددة، يمكنك استخدام علامات بادئة صريحة مع تعليمات باللغة الطبيعية. يجب الإفصاح عن هذه المصادر والمراجع في بداية الطلب.

- `[# Sources <FIRST_FRAME>@Image1]` سيتم استخدام الصورة الأولى كإطار البداية.
- ستستخدم `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` الصورة الأولى كإطار بدء والصورة الثانية كإطار نهائي.
- ستستخدم أداة `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` الصورة الأولى كإطار أول وإطار أخير، ما يؤدي إلى إنشاء فيديو يتكرّر.
- ستستخدم `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` الصورة الأولى كإطار البداية والصورة الثانية كمرجع.
- سيتم استخدام الفيديو `[# Sources <VIDEO_0>@Video1]` كمصدر أساسي لتعديله أو تغييره.
- سيستخدم `[# Sources <PREVIOUS_VIDEO>@Video1]` الفيديو من الجولة السابقة لتمديدها.
- `[# References <IMAGE_REF_0>@Image1]` سيتم استخدام الصورة الأولى كمرجع.
- سيستخدم `[# References <IMAGE_REF_1>@Image2]` الصورة الثانية كمرجع.
- سيستخدم `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` كلتا الصورتين كمرجع.
- `[# References <VIDEO_REF_0>@Video1]` سيتم استخدام الفيديو الأول كمرجع.
- ستستخدم `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` صورة وفيديو كمرجع.

أضِف تعليمات توجيهية في نهاية طلبك:

- بالنسبة إلى إطار البدء: `"Use this image as the starting frame."`
- لإنشاء فيديو متكرّر باستخدام إطارات البدء والانتهاء: `"Use this image as the first frame and the last frame."`
- بالنسبة إلى الصور المرجعية: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- بالنسبة إلى الفيديوهات المرجعية: `"Use the given video(s) as references. Do not use them as a source for video editing."`

في ما يلي بعض الأمثلة على الطلبات التي تتضمّن إقرارات بالمصدر والمرجع:

**الإطار الأوّل مع صورة مرجعية:**

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**فيديو مرجعي للشخصية مع صورة مرجعية للكائن:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## الخطوات التالية

- ابدأ رحلتك مع Gemini Omni Flash من خلال تجربة [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=ar).
- تعرَّف على كيفية كتابة طلبات أفضل من خلال [مقدمة حول تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
