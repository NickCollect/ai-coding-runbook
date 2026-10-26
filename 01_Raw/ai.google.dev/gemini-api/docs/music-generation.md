---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=tr
fetched_at: 2026-10-26T05:58:29.911864+00:00
title: "Lyria 3.5 ile m\u00fczik \u00fcretme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Lyria 3.5 ile müzik üretme

Lyria 3.5, Gemini API üzerinden kullanılabilen Google'ın müzik üretme modeli ailesidir. Lyria 3.5 ile metin istemlerinden veya resimlerden yüksek kaliteli, 44, 1 kHz stereo ses üretebilirsiniz. Bu modeller, vokaller, zamanlanmış şarkı sözleri ve tam enstrümantal düzenlemeler dahil olmak üzere yapısal tutarlılık sağlar.

Lyria ailesinde şu modeller bulunur:

| Model | Model Kimliği | En uygun olduğu durumlar | Süre | Çıkış |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Kısa klipler, döngüler, önizlemeler | 30 saniye | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Dizeler, nakaratlar ve köprüler içeren tam uzunlukta şarkılar | Birkaç dakika (istem kullanılarak kontrol edilebilir) | MP3 |

Her iki model de çok formatlı girişleri (metin ve resim) destekleyen yeni [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) kullanılarak kullanılabilir ve **44,1 kHz yüksek kaliteli stereo** ses üretir.

## Müzik klibi oluşturma

Lyria 3 Clip modeli her zaman **30 saniyelik** bir klip oluşturur. Klip oluşturmak için `interactions.create` yöntemini metin istemiyle çağırın. Yanıtta, `steps` şemasındaki sesin yanı sıra her zaman oluşturulan şarkı sözleri ve şarkı yapısı yer alır.

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

Oluşturulan son ses bloğunu döndüren `interaction.output_audio` özelliğini kullanarak oluşturulan müzik verilerini alabilirsiniz. Ayrıca `interaction.output_text` özelliğini kullanarak şarkı sözlerini ve yapısını da alabilirsiniz. Kolaylık özellikleri hakkında ayrıntılı bilgi için [Etkileşime genel bakış](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr#convenience-properties) başlıklı makaleyi inceleyin.

## Tam uzunlukta şarkı oluşturma

Birkaç dakika süren tam uzunlukta şarkılar oluşturmak için `lyria-3.5` modelini kullanın. Pro modeli, müzikal yapıyı anlar ve farklı kıtalar, nakaratlar ve köprüler içeren kompozisyonlar oluşturabilir. İsteminizde süreyi belirterek (ör. "2 dakikalık bir şarkı oluştur") veya yapıyı tanımlamak için [zaman damgalarını](#timing) kullanarak süreyi etkileyebilirsiniz.

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

## Çıkış biçimini seçin

Lyria 3.5 modelleri, varsayılan olarak **MP3** biçiminde ses üretir. Lyria 3.5 için `response_format` değerini ayarlayarak çıktının **WAV** biçiminde olmasını da isteyebilirsiniz.

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

## Yanıtı ayrıştırma

Lyria 3.5'in yanıtı, `steps` şemasında birden fazla içerik bloğu içeriyor.
Etkileşimler, `model_output` adımlarının oluşturulan içeriği içerdiği bir dizi adım döndürür.
Metin içerik bloklarında, oluşturulan şarkı sözleri veya şarkı yapısının JSON açıklaması yer alır.
`audio` türündeki içerik blokları, Base64 kodlu ses verilerini içerir.

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

#### Şarkı sözleri ve müziğin iç içe gösterilmesi

Lyria 3.5'in çıkışı karmaşıktır. Oluşturulan şarkı sözleri (metin) ve şarkının kendisi (ses) için ayrı adımlar ve bloklar içerir. Bu nedenle, kolaylık özellikleri hızlı ve önerilen bir kısayol sunar.

Ancak sunucu tarafından döndürülen adımların ham zaman çizelgesi üzerinde tam ve programatik kontrol sahibi olmak istiyorsanız (ör. tek tek içerik bloklarını alındıkları sırada günlüğe kaydetmek) bunun yerine `steps` üzerinde manuel olarak yineleme yapabilirsiniz:

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

## Resimlerden müzik oluşturma

Lyria 3.5, çok formatlı girişleri destekler. `input` listesinde metin isteminizle birlikte **10 adede kadar resim** sağlayabilirsiniz. Model, görsel içerikten ilham alarak müzik oluşturur.

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

## Özel şarkı sözleri sağlama

Kendi şarkı sözlerinizi yazıp isteme ekleyebilirsiniz. Modelin şarkı yapısını anlamasına yardımcı olmak için `[Verse]`, `[Chorus]` ve `[Bridge]` gibi bölüm etiketlerini kullanın:

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

## Zamanlamayı ve yapıyı kontrol etme

Zaman damgalarını kullanarak şarkının belirli anlarında tam olarak ne olacağını belirleyebilirsiniz. Bu özellik, enstrümanların ne zaman başlayacağını, şarkı sözlerinin ne zaman gösterileceğini ve şarkının nasıl ilerleyeceğini kontrol etmek için kullanışlıdır:

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

## Enstrümantal parçalar oluşturma

Arka plan müziği, oyun müzikleri veya vokallerin gerekli olmadığı tüm kullanım alanlarında, modelden yalnızca enstrümantal parçalar üretmesini isteyebilirsiniz:

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

## Farklı dillerde müzik üretme

Lyria 3.5, isteminizin dilinde şarkı sözleri oluşturur. Fransızca sözler içeren bir şarkı oluşturmak için isteminizi Fransızca yazın. Model, dilin özelliklerine uygun bir vokal tarzı ve telaffuz kullanır.

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

## Model zekası

Lyria 3.5, isteminizi analiz eder. Bu analiz sürecinde model, isteminize göre müzikal yapı (giriş, kıta, nakarat, köprü vb.) üzerinden akıl yürütür.
Bu işlem, ses oluşturulmadan önce gerçekleşir ve yapısal tutarlılık ile müzikalite sağlar.

## İstem yazma kılavuzu

Müzik türleri, enstrümanlar, şarkı yapısı, özel şarkı sözleri ve vokal sunum stilleri için etkili istemler oluşturmayı öğrenmek istiyorsanız [Lyria istem rehberine](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=tr) bakın.

## En iyi uygulamalar

- **Önce Klibi yineleyin.** `lyria-3-clip-preview` ile tam uzunlukta bir üretim yapmadan önce istemlerle deneme yapmak için daha hızlı olan `lyria-3.5` modelini kullanın.
- **Net olun.** Net olmayan istemler genel sonuçlar üretir. En iyi sonucu elde etmek için enstrümanları, tempoyu, anahtarı, ruh halini ve yapıyı belirtin.
- **Dilinizi eşleştirin.** Şarkı sözlerinin hangi dilde olmasını istiyorsanız o dilde istem girin.
- **Bölüm etiketlerini kullanın.** `[Verse]`, `[Chorus]`, `[Bridge]` etiketleri, modele izleyeceği net bir yapı sunar.
- **Şarkı sözlerini talimatlardan ayırın.** Özel şarkı sözleri sağlarken bunları müzikal yönlendirme talimatlarınızdan net bir şekilde ayırın.

## Sınırlamalar

- **Güvenlik**: Tüm istemler güvenlik filtreleriyle kontrol edilir. Filtreleri tetikleyen istemler engellenir. Belirli sanatçıların seslerini veya telif hakkıyla korunan şarkı sözlerinin oluşturulmasını isteyen istemler de bu kapsamdadır.
- **Filigran ekleme**: Üretilen tüm seslerde tanımlama için [SynthID ses filigranı](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=tr) bulunur. Bu filigran, insan kulağıyla fark edilemez ve dinleme deneyimini etkilemez.
- **Çok adımlı düzenleme**: Müzik üretimi tek adımlı bir süreçtir.
  Oluşturulan bir klibin birden fazla istemle yinelenerek düzenlenmesi veya iyileştirilmesi, Lyria 3.5'in mevcut sürümünde desteklenmemektedir.
- **Uzunluk**: Klip modeli her zaman 30 saniyelik klipler oluşturur. Pro modeli, birkaç dakika süren şarkılar oluşturur. Tam süre, isteminizden etkilenebilir.
- **Belirlenimcilik**: Aynı istemle bile olsa sonuçlar çağrılar arasında farklılık gösterebilir.

## Sırada ne var?

- Lyria 3.5 modellerinin [fiyatlandırmasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.
- Lyria RealTime ile [anlık müzik üretme](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr) özelliğini deneyin.
- [TTS modelleri](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) ile birden fazla konuşmacının yer aldığı görüşmeler oluşturun.
- [Resim](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) veya [video](https://ai.google.dev/gemini-api/docs/video?hl=tr) oluşturmayı öğrenin.
- Gemini'ın [ses dosyalarını nasıl anlayabileceğini](https://ai.google.dev/gemini-api/docs/audio?hl=tr) öğrenin.
- [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)'yi kullanarak Gemini ile anlık sohbet edin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-01 UTC."],[],[]]
