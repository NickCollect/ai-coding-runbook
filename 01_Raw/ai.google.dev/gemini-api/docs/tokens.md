---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=pl
fetched_at: 2026-10-05T06:36:39.757691+00:00
title: "Zrozumienie i liczenie token\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Zrozumienie i liczenie tokenów

Gemini i inne modele generatywnej AI przetwarzają dane wejściowe i wyjściowe w jednostkach zwanych *tokenami*.

**W przypadku modeli Gemini token odpowiada około 4 znakom.
100 tokenów to około 60–80 słów w języku angielskim.**

## Informacje o tokenach

Tokeny mogą być pojedynczymi znakami, np. `z`, lub całymi słowami, np. `cat`. Długie słowa
są dzielone na kilka tokenów. Zbiór wszystkich tokenów używanych przez model nazywa się słownikiem, a proces dzielenia tekstu na tokeny to *tokenizacja*.

Gdy płatności są włączone, [koszt wywołania interfejsu Gemini API](https://ai.google.dev/pricing?hl=pl) jest częściowo określany przez liczbę tokenów wejściowych i wyjściowych, więc wiedza o tym, jak je zliczać, może być przydatna.

## Liczba tokenów

Wszystkie dane wejściowe i wyjściowe interfejsu Gemini API są tokenizowane, w tym tekst, pliki obrazów i inne formaty nietekstowe.

Tokeny możesz zliczać na te sposoby:

- **Wywołaj funkcję `count_tokens` z danymi wejściowymi żądania.** Zwraca łączną liczbę tokenów *tylko w danych wejściowych*. Zanim wyślesz dane wejściowe, wywołaj tę funkcję, aby sprawdzić rozmiar żądań.
- **Użyj `usage` w odpowiedzi na interakcję.** Zwraca liczbę tokenów dla danych wejściowych (`total_input_tokens`), wyjściowych (`total_output_tokens`), myślenia (`total_thought_tokens`), treści w pamięci podręcznej (`total_cached_tokens`), korzystania z narzędzi (`total_tool_use_tokens`) i łączną (`total_tokens`).

### Zliczanie tokenów tekstowych

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CountTokensResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
CountTokensResponse countResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println("total_tokens: " + countResponse.totalTokens().orElse(0));

// Get usage from interaction
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    modelInfo, err := client.Models.Get(ctx, "gemini-3.8-flash", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Input token limit: %d\n", modelInfo.InputTokenLimit)
    fmt.Printf("Output token limit: %d\n", modelInfo.OutputTokenLimit)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Zliczanie tokenów w przypadku wieloetapowych rozmów

Zlicz tokeny w historii rozmów za pomocą funkcji `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// First interaction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Bob"))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Second interaction continues the conversation
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's my name?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Usage includes tokens from both turns
if (interaction2.usage().isPresent()) {
  Usage usage = interaction2.usage().get();
  System.out.println("Input tokens: " + usage.totalInputTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
  System.out.println("Total tokens: " + usage.totalTokens().orElse(0));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    prompt := "The quick brown fox jumps over the lazy dog."

    // Count input tokens before sending
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", genai.Text(prompt), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("total_tokens: %d\n", totalTokens.TotalTokens)

    // Create the interaction and inspect the returned usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil {
        if interaction.Usage.TotalInputTokens != nil {
            fmt.Printf("Input tokens: %d\n", *interaction.Usage.TotalInputTokens)
        }
        if interaction.Usage.TotalOutputTokens != nil {
            fmt.Printf("Output tokens: %d\n", *interaction.Usage.TotalOutputTokens)
        }
        if interaction.Usage.TotalThoughtTokens != nil {
            fmt.Printf("Thought tokens: %d\n", *interaction.Usage.TotalThoughtTokens)
        }
        if interaction.Usage.TotalTokens != nil {
            fmt.Printf("Total tokens: %d\n", *interaction.Usage.TotalTokens)
        }
    }
}
```

### Liczba tokenów multimodalnych

Wszystkie dane wejściowe do interfejsu Gemini API są tokenizowane, w tym obrazy, filmy i dźwięk.
Najważniejsze informacje o tokenizacji:

- **Obrazy:** obrazy o wymiarach ≤384 pikseli w każdym z wymiarów liczą się jako 258 tokenów. Większe obrazy są dzielone na kafelki o rozmiarze 768 x 768 pikseli, z których każdy jest liczony jako 258 tokenów.
- **Wideo:** 263 tokeny na sekundę (dotyczy przetwarzania statycznego). W przypadku przetwarzania z użyciem agenta wykorzystanie tokenów jest różne. Zobacz [wykorzystanie tokenów wideo według trybu przetwarzania](#video-token-usage).
- **Dźwięk:** 32 tokeny na sekundę

#### Tokeny obrazów

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/image.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

// Count tokens for image + text
CountTokensResponse countResponse =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromText("Tell me about this image"),
                Part.fromUri(
                    uploadedFile.uri().orElse(""), uploadedFile.mimeType().orElse("image/jpeg")))),
        null);
System.out.println("Total tokens: " + countResponse.totalTokens().orElse(0));

// Generate with image
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("Tell me about this image").build(),
                    ImageContent.builder()
                        .uri(uploadedFile.uri().orElse(""))
                        .mimeType(
                            ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
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
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Explain the history of the internet in 3 paragraphs."),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
        if completed := event.GetDataInteractionCompleted(); completed != nil {
            usage := completed.Interaction.Usage
            if usage != nil && usage.TotalTokens != nil {
                fmt.Printf("\nTotal tokens: %d\n", *usage.TotalTokens)
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

**Przykład danych wbudowanych:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### Tokeny wideo

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 100 * 60 = 6,000 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Wykorzystanie tokenów wideo według trybu przetwarzania

Wykorzystanie tokenów w przypadku filmu zależy od trybu przetwarzania:

| **Tryb przetwarzania** | **Obliczanie tokenów** | **Typowe użycie** |
| --- | --- | --- |
| **Statyczny** (domyślnie) | Domyślnie ok. 100 tokenów na sekundę (niska rozdzielczość) lub ok. 300 tokenów na sekundę (wysoka rozdzielczość). Wszystkie klatki próbkowane z częstotliwością 1 klatki na sekundę. | Przewidywalne, proporcjonalne do czasu trwania filmu. |
| **Agentic** | Zależy od złożoności treści. Model wczytuje tylko transkrypcję, klatki lub dźwięk potrzebne do udzielenia odpowiedzi na prompta. | Do 88% mniej tokenów w przypadku długich treści. |

W przypadku przetwarzania z użyciem agentów 1-godzinny wykład, który w trybie statycznym wykorzystuje około 1,08 mln tokenów, może wykorzystać około 108 tys.tokenów w zależności od promptu i treści.

Aby sprawdzić rzeczywiste wykorzystanie tokenów w przypadku żądania, sprawdź `interaction.usage`. Tokeny wideo agenta są raportowane w tych polach:

- **Prompt początkowy** (odniesienie do filmu + prompt użytkownika): `total_input_tokens`
- **Myślenie nawigacyjne:** `total_thought_tokens`
- **Transkrypcja, klatki i dźwięk wczytywane na żądanie:** `total_tool_use_tokens`
- **Odpowiedź:** `total_output_tokens`

#### Tokeny audio

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Zliczanie tokenów instrukcji systemowych

Instrukcje systemowe są liczone jako tokeny wejściowe:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Zliczanie tokenów narzędzia

Narzędzia (funkcje, wykonywanie kodu, wyszukiwarka Google) są również uwzględniane:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Okno kontekstu

Każdy model Gemini ma maksymalną liczbę tokenów, które może przetworzyć. Okno kontekstu określa łączny limit tokenów wejściowych i wyjściowych.

### Programowe uzyskiwanie rozmiaru okna kontekstu

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.8-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.8-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Model;

Client client = new Client();

Model modelInfo = client.models.get("gemini-3.8-flash", null);
System.out.println("Input token limit: " + modelInfo.inputTokenLimit().orElse(0));
System.out.println("Output token limit: " + modelInfo.outputTokenLimit().orElse(0));
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

    prompt := "Tell me about this instrument"
    imageBytes, err := os.ReadFile("/path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    // Count tokens before creating the interaction
    parts := []*genai.Part{
        genai.NewPartFromText(prompt),
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    }
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Estimated input tokens: %d\n", totalTokens.TotalTokens)

    // Create the multimodal interaction and inspect the usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Total tokens billed: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

Rozmiary okien kontekstu znajdziesz na stronie [modele](https://ai.google.dev/gemini-api/docs/models?hl=pl).

## Co dalej?

- [Generowanie tekstu:](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl) podstawy generowania
- [Pamięć podręczna:](https://ai.google.dev/gemini-api/docs/caching?hl=pl) zmniejszanie kosztów dzięki pamięci podręcznej
- [Ceny:](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) informacje o kosztach

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-24 UTC."],[],[]]
