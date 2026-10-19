---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=pl
fetched_at: 2026-10-19T05:49:54.836038+00:00
title: "Generowanie muzyki za pomoc\u0105 Lyrii\u00a03.5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie muzyki za pomocą Lyrii 3.5

Lyria 3.5 to rodzina modeli generowania muzyki od Google, dostępna w ramach Gemini API. Lyria 3.5 umożliwia generowanie wysokiej jakości dźwięku stereo o częstotliwości próbkowania 44,1 kHz na podstawie promptów tekstowych lub obrazów. Te modele zapewniają spójność strukturalną, w tym wokal, zsynchronizowany tekst i pełne aranżacje instrumentalne.

Rodzina Lyria obejmuje modele:

| Model | Identyfikator modelu | Urządzenia | Czas trwania | Wyniki |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Krótkie klipy, pętle, zapowiedzi | 30 sekund | MP3 |
| **Lyria 3.5** | `lyria-3.5` | pełne utwory z wersami, refrenami i przejściami; | Kilka minut (można kontrolować za pomocą prompta) | MP3 |

Oba modele można używać za pomocą nowego [interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl), który obsługuje dane wejściowe w różnych formatach (tekst i obrazy) i generuje dźwięk stereo o wysokiej jakości (**44,1 kHz**).

## Generowanie klipu muzycznego

Model Lyria 3 Clip zawsze generuje **30-sekundowy** klip. Aby wygenerować klip, wywołaj metodę `interactions.create` z promptem tekstowym. Odpowiedź zawsze zawiera wygenerowane słowa i strukturę utworu wraz z dźwiękiem w schemacie `steps`.

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

Wygenerowane dane muzyczne możesz pobrać za pomocą właściwości `interaction.output_audio`, która zwraca ostatni wygenerowany blok audio. Możesz też pobrać tekst i strukturę utworu za pomocą właściwości `interaction.output_text`. Więcej informacji o właściwościach ułatwiających korzystanie z usługi znajdziesz w [omówieniu interakcji](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl#convenience-properties).

## Generowanie pełnych utworów

Użyj modelu `lyria-3.5`, aby wygenerować pełne utwory trwające kilka minut. Model Pro rozumie strukturę muzyczną i może tworzyć kompozycje z wyraźnymi zwrotkami, refrenami i przejściami. Możesz wpłynąć na czas trwania utworu, podając go w prompcie (np. „utwórz 2-minutową piosenkę”) lub używając [sygnatur czasowych](#timing) do zdefiniowania struktury.

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

## Wybierz format wyjściowy

Domyślnie modele Lyria 3.5 generują dźwięk w formacie **MP3**. W przypadku Lyrii 3.5 możesz też poprosić o wygenerowanie danych wyjściowych w formacie **WAV**, ustawiając parametr `response_format`.

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

## Analizowanie odpowiedzi

Odpowiedź z Lyrii 3.5 zawiera wiele bloków treści w schemacie `steps`.
Interakcje zwracają sekwencję kroków, w której kroki `model_output` zawierają wygenerowane treści.
Bloki treści tekstowych zawierają wygenerowane teksty lub opis struktury utworu w formacie JSON.
Bloki treści typu `audio` zawierają dane audio zakodowane w formacie base64.

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

#### Tekst i muzyka przeplatające się ze sobą

Dane wyjściowe modelu Lyria 3.5 są złożone – zawierają osobne etapy i bloki wygenerowanego tekstu i samego utworu (audio). Właściwości wygody oferują szybki i zalecany skrót.

Jeśli jednak chcesz mieć pełną, programową kontrolę nad surową osią czasu kroków zwracanych przez serwer (np. rejestrować poszczególne bloki treści w miarę ich otrzymywania), możesz ręcznie iterować po `steps`:

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

## Generowanie muzyki na podstawie obrazów

Lyria 3.5 obsługuje dane wejściowe w różnych formatach – możesz podać maksymalnie **10 obrazów** w `input` wraz z promptem tekstowym, a model skomponuje muzykę inspirowaną treściami wizualnymi.

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

## Podaj niestandardowy tekst

Możesz napisać własny tekst i dodać go do prompta. Używaj tagów sekcji, takich jak `[Verse]`, `[Chorus]` i `[Bridge]`, aby pomóc modelowi zrozumieć strukturę utworu:

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

## Kontrolowanie czasu i struktury

Za pomocą znaczników czasu możesz określić, co dokładnie ma się wydarzyć w konkretnych momentach utworu. Jest to przydatne do kontrolowania, kiedy wchodzą instrumenty, kiedy pojawiają się słowa i jak rozwija się utwór:

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

## Generowanie ścieżek instrumentalnych

W przypadku muzyki w tle, ścieżek dźwiękowych do gier lub innych zastosowań, w których nie są wymagane wokale, możesz poprosić model o wygenerowanie utworów instrumentalnych:

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

## Generowanie muzyki w różnych językach

Lyria 3.5 generuje tekst w języku prompta. Aby wygenerować utwór z tekstem w języku francuskim, napisz prompta w tym języku. Model dostosowuje styl mówienia i wymowę do języka.

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

## Inteligencja modelu

Lyria 3.5 analizuje proces tworzenia promptów, w którym model wnioskuje na podstawie prompta o strukturze muzycznej (wprowadzenie, zwrotka, refren, mostek itp.).
Dzieje się to przed wygenerowaniem dźwięku i zapewnia spójność strukturalną oraz muzykalność.

## Przewodnik po promptach

Aby dowiedzieć się, jak tworzyć skuteczne prompty dotyczące gatunków muzycznych, instrumentów, struktury utworu, niestandardowych tekstów i stylów wokalnych, zapoznaj się z [przewodnikiem po tworzeniu promptów Lyrii](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=pl).

## Sprawdzone metody

- **Najpierw wypróbuj klip.** Użyj szybszego modelu `lyria-3-clip-preview`, aby eksperymentować z promptami, zanim zdecydujesz się na wygenerowanie pełnej wersji za pomocą `lyria-3.5`.
- **Unikaj ogólników.** Niejasne prompty dają ogólne wyniki. Aby uzyskać najlepszy rezultat, podaj instrumenty, tempo, tonację, nastrój i strukturę.
- **Wybierz język.** Wpisz prompta w języku, w którym chcesz uzyskać tekst.
- **Używaj tagów sekcji.** Tagi `[Verse]`, `[Chorus]`, `[Bridge]` zapewniają modelowi przejrzystą strukturę, której może się trzymać.
- **Oddziel słowa piosenki od instrukcji.** Podczas podawania niestandardowego tekstu wyraźnie oddziel go od instrukcji dotyczących kierunku muzycznego.

## Ograniczenia

- **Bezpieczeństwo:** wszystkie prompty są sprawdzane przez filtry bezpieczeństwa. Prompty, które uruchamiają filtry, zostaną zablokowane. Obejmuje to prompty, które wymagają konkretnych głosów artystów lub generowania tekstów chronionych prawami autorskimi.
- **Znaki wodne:** wszystkie wygenerowane pliki audio zawierają [znak wodny audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pl), który umożliwia identyfikację. Ten znak wodny jest niedostrzegalny dla ludzkiego ucha i nie wpływa na wrażenia słuchowe.
- **Edycja wieloetapowa:** generowanie muzyki to proces jednoetapowy.
  W obecnej wersji Lyrii 3.5 nie jest obsługiwana iteracyjna edycja ani dopracowywanie wygenerowanego klipu za pomocą wielu promptów.
- **Długość:** model Clip zawsze generuje 30-sekundowe klipy. Model Pro generuje utwory trwające kilka minut. Na dokładny czas trwania można wpłynąć za pomocą promptu.
- **Determinism:** wyniki mogą się różnić w zależności od wywołania, nawet w przypadku tego samego prompta.

## Co dalej?

- Sprawdź [ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) modeli Lyria 3.5.
- Wypróbuj [generowanie muzyki w czasie rzeczywistym](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pl) za pomocą Lyrii RealTime.
- Generowanie rozmów z udziałem wielu osób za pomocą [modeli TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).
- Dowiedz się, jak generować [obrazy](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) lub [filmy](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- Dowiedz się, jak Gemini może [rozumieć pliki audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl).
- Prowadź rozmowy w czasie rzeczywistym z Gemini za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-01 UTC."],[],[]]
