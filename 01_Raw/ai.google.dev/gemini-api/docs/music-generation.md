---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-CN
fetched_at: 2026-10-05T06:43:14.502397+00:00
title: "\u4f7f\u7528 Lyria 3.5 \u751f\u6210\u97f3\u4e50 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Lyria 3.5 生成音乐

Lyria 3.5 是 Google 的音乐创作模型系列，现已可通过 Gemini API 调用。借助 Lyria 3.5，您可以根据文本提示或图片生成高质量的 44.1 kHz 立体声音频。这些模型可提供结构连贯的音乐，包括人声、同步歌词和完整的器乐编排。

Lyria 系列包含以下模型：

| 模型 | 模型 ID | 适用场景 | 时长 | 输出 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短片、循环播放的短视频、预览 | 30 秒 | MP3 |
| **Lyria 3.5** | `lyria-3.5` | 包含主歌、副歌和桥段的完整歌曲 | 几分钟（可通过提示词控制） | MP3 |

这两种模型均可通过新的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 使用，支持多模态输入（文本和图片），并生成 **44.1 kHz 高保真立体声**音频。

## 生成音乐片段

Lyria 3 Clip 模型始终会生成 **30 秒**的片段。如需生成剪辑，请使用文本提示调用 `interactions.create` 方法。响应始终包含生成的歌词和歌曲结构，以及 `steps` 架构中的音频。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### Java

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
        .model(Model.of("lyria-3-clip-preview"))
        .input(InteractionsInput.of("A short instrumental acoustic guitar piece."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("music.mp3"), audioBytes);
}

interaction.outputText().ifPresent(lyrics -> System.out.println("Lyrics:\n" + lyrics));
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput("A short instrumental acoustic guitar piece."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("music.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

您可以使用 `interaction.output_audio` 属性检索生成的音乐数据，该属性会返回上次生成的音频块。您还可以使用 `interaction.output_text` 属性检索歌曲的歌词和结构。如需详细了解便捷属性，请参阅[互动概览](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn#convenience-properties)。

## 生成完整歌曲

使用 `lyria-3.5` 模型生成时长为几分钟的完整歌曲。Pro 模型能理解音乐结构，并能创作出具有鲜明主歌、副歌和桥段的乐曲。您可以在提示中指定时长（例如“创作一首 2 分钟的歌曲”），也可以使用[时间戳](#timing)来定义结构，从而影响时长。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## 选择输出格式

默认情况下，Lyria 3.5 模型会生成 **MP3** 格式的音频。对于 Lyria 3.5，您还可以通过设置 `response_format` 来请求 **WAV** 格式的输出。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A beautiful piano melody."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A beautiful piano melody."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## 解析响应

Lyria 3.5 的回答包含 `steps` 架构中的多个内容块。
互动会返回一系列步骤，其中 `model_output` 步骤包含生成的内容。文本内容块包含生成的歌词或歌曲结构的 JSON 说明。
类型为 `audio` 的内容块包含 base64 编码的音频数据。

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### Java

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
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("output.mp3"), audioBytes);
}

if (interaction.outputText().isPresent()) {
  System.out.println("Lyrics:\n" + interaction.outputText().get());
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
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("output.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### 交错显示歌词和音乐

由于 Lyria 3.5 的输出较为复杂，包含生成歌词（文本）和歌曲本身（音频）的单独步骤和代码块，因此便利属性可提供快速且推荐的快捷方式。

不过，如果您想以程序化方式完全控制服务器返回的原始步数时间轴（例如在收到各个内容块时记录它们），可以改为手动迭代 `steps`：

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof AudioContent) {
            AudioContent audioBlock = (AudioContent) contentBlock;
            if (audioBlock.data().isPresent()) {
              audioData = Base64.getDecoder().decode(audioBlock.data().get());
            }
          } else if (contentBlock instanceof TextContent) {
            TextContent textBlock = (TextContent) contentBlock;
            textBlock.text().ifPresent(lyrics::add);
          }
        }
      }
    }
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
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
    "strings"

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
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var lyrics []string
    var audioData []byte

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.AudioContent != nil && contentBlock.AudioContent.Data != nil {
                    decoded, err := base64.StdEncoding.DecodeString(*contentBlock.AudioContent.Data)
                    if err != nil {
                        log.Fatal(err)
                    }
                    audioData = decoded
                } else if contentBlock.TextContent != nil {
                    lyrics = append(lyrics, contentBlock.TextContent.Text)
                }
            }
        }
    }

    if len(lyrics) > 0 {
        fmt.Printf("Lyrics:\n%s\n", strings.Join(lyrics, "\n"))
    }

    if audioData != nil {
        if err := os.WriteFile("output.mp3", audioData, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

## 根据图片生成音乐

Lyria 3.5 支持多模态输入，您可以在 `input` 列表中提供最多 **10 张图片**以及文本提示，模型将根据视觉内容创作音乐。

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
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

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("desert_sunset.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

Content textContent =
    TextContent.builder()
        .text("An atmospheric ambient track inspired by the mood and colors in this image.")
        .build();
Content imageContent =
    ImageContent.builder()
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .data(imageB64)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    imageBytes, err := os.ReadFile("desert_sunset.jpg")
    if err != nil {
        log.Fatal(err)
    }
    imageB64 := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        }),
        interactions.NewContent(interactions.ImageContent{
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
            Data:     genai.Ptr(imageB64),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## 提供自定义歌词

您可以自行撰写歌词，并将其添加到提示中。使用 `[Verse]`、`[Chorus]` 和 `[Bridge]` 等部分标记来帮助模型了解歌曲结构：

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Create a dreamy indie pop song with the following lyrics:\n\n"
        + "[Verse 1]\n"
        + "Walking through the neon glow,\n"
        + "city lights reflect below,\n"
        + "every shadow tells a story,\n"
        + "every corner, fading glory.\n\n"
        + "[Chorus]\n"
        + "We are the echoes in the night,\n"
        + "burning brighter than the light,\n"
        + "hold on tight, don't let me go,\n"
        + "we are the echoes down below.\n\n"
        + "[Verse 2]\n"
        + "Footsteps lost on empty streets,\n"
        + "rhythms sync to heartbeats,\n"
        + "whispers carried by the breeze,\n"
        + "dancing through the autumn leaves.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    prompt := "Create a dreamy indie pop song with the following lyrics:\n\n" +
        "[Verse 1]\n" +
        "Walking through the neon glow,\n" +
        "city lights reflect below,\n" +
        "every shadow tells a story,\n" +
        "every corner, fading glory.\n\n" +
        "[Chorus]\n" +
        "We are the echoes in the night,\n" +
        "burning brighter than the light,\n" +
        "hold on tight, don't let me go,\n" +
        "we are the echoes down below.\n\n" +
        "[Verse 2]\n" +
        "Footsteps lost on empty streets,\n" +
        "rhythms sync to heartbeats,\n" +
        "whispers carried by the breeze,\n" +
        "dancing through the autumn leaves."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## 控制时间和结构

您可以使用时间戳精确指定歌曲中特定时刻发生的情况。这对于控制乐器何时进入、歌词何时出现以及歌曲如何推进非常有用：

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n"
        + "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n"
        + "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n"
        + "[0:50 - 1:00] Outro: Fade out with the piano melody alone.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    prompt := "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n" +
        "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n" +
        "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n" +
        "[0:50 - 1:00] Outro: Fade out with the piano melody alone."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## 生成乐器演奏曲目

对于背景音乐、游戏配乐或不需要人声的任何应用场景，您可以提示模型生成纯乐器曲目：

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(
            InteractionsInput.of(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## 生成不同语言的音乐

Lyria 3.5 会以提示所用的语言生成歌词。如需生成带有法语歌词的歌曲，请使用法语撰写提示。模型会调整其发音风格和发音，以匹配相应语言。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## 模型智能

Lyria 3.5 会分析您的提示流程，其中模型会根据您的提示，通过音乐结构（前奏、主歌、副歌、桥段等）进行推理。
此过程发生在生成音频之前，可确保结构连贯性和音乐性。

## 提示指南

如需了解如何针对音乐流派、乐器、歌曲结构、自定义歌词和演唱风格编写有效的提示，请参阅 [Lyria 提示指南](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=zh-cn)。

## 最佳做法

- **先使用 Clip 进行迭代。**使用速度更快的 `lyria-3-clip-preview` 模型来测试提示，然后再使用 `lyria-3.5` 生成完整内容。
- **内容要具体。**模糊的提示会产生泛化的结果。提及乐器、BPM、调、基调和结构，以获得最佳输出。
- **使用与您相同的语言。**以您想要的歌词语言输入提示。
- **使用部分标记。**`[Verse]`、`[Chorus]`、`[Bridge]` 标记为模型提供了清晰的结构，以便模型遵循。
- **将歌词与说明分开。**提供自定义歌词时，请务必将其与音乐指导指令明确分开。

## 限制

- **安全**：所有提示都会经过安全过滤器的检查。触发过滤条件的提示将被屏蔽。这包括要求使用特定艺术家的声音或生成受版权保护的歌词的提示。
- **水印**：所有生成的音频都包含 [SynthID 音频水印](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-cn)，以便进行识别。这种水印人耳无法察觉，不会影响聆听体验。
- **多轮编辑**：音乐创作是一个单轮过程。当前版本的 Lyria 3.5 不支持通过多个提示迭代修改或优化生成的剪辑。
- **时长**：Clip 模型始终生成 30 秒的片段。Pro 模型生成的歌曲时长为几分钟；确切时长会受到提示的影响。
- **确定性**：即使使用相同的提示，每次调用得到的结果也可能有所不同。

## 后续步骤

- 查看 Lyria 3.5 模型的价格。
- 试试使用 Lyria RealTime 进行[实时流式音乐生成](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-cn)。
- 使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)生成多说话人对话。
- 了解如何生成[图片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)或[视频](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)。
- 了解 Gemini 如何[理解音频文件](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)。
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn) 与 Gemini 进行实时对话。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-01。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-01。"],[],[]]
