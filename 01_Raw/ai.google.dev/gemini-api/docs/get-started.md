---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=pl
fetched_at: 2026-11-02T07:24:27.445808+00:00
title: "Pierwsze kroki \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Pierwsze kroki

Z tego przewodnika dowiesz się, jak zacząć korzystać z interfejsu Gemini API za pomocą [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl). Pierwsze wywołanie interfejsu API wykonasz w mniej niż minutę. Poznasz generowanie tekstu, rozpoznawanie multimodalne, generowanie obrazów, dane wyjściowe strukturalne, narzędzia, wywoływanie funkcji, agenty i wykonywanie w tle.

Interfejs Interactions API jest dostępny w pakietach SDK w językach [Python](https://github.com/googleapis/python-genai) i [JavaScript](https://github.com/googleapis/js-genai), a także w ramach interfejsu REST.

## 1. Uzyskiwanie klucza interfejsu API

Aby korzystać z interfejsu Gemini API, musisz mieć klucz interfejsu API, który umożliwia uwierzytelnianie żądań, egzekwowanie limitów bezpieczeństwa i śledzenie wykorzystania na koncie.

- Google AI Studio automatycznie tworzy projekt i klucz interfejsu API dla nowych użytkowników.
  Możesz go skopiować ze [strony kluczy interfejsów API](https://aistudio.google.com/api-keys?hl=pl).
- Jeśli potrzebujesz nowego klucza, w AI Studio kliknij **Utwórz klucz interfejsu API** i postępuj zgodnie z instrukcjami w oknie, aby dodać nową parę klucz-projekt.

[Tworzenie klucza interfejsu Gemini API](https://aistudio.google.com/apikey?hl=pl)

Ustaw klucz jako zmienną środowiskową:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Przejście na poziom płatny

Przejście na poziom płatny zwiększa limity ograniczania liczby żądań i wymaga skonfigurowania Rozliczeń usługi Google Cloud.

- Na stronie AI Studio – [Klucze interfejsu API](https://aistudio.google.com/api-keys?hl=pl) lub [Projekty](https://aistudio.google.com/projects?hl=pl) kliknij **Skonfiguruj płatności**.
- Postępuj zgodnie z instrukcjami w oknie dialogowym Rozliczenia usługi Google Cloud, aby utworzyć lub połączyć konto rozliczeniowe, dodać formę płatności i wpłacić przedpłatę w wysokości co najmniej 5 USD (lub równowartości w innej walucie) w postaci środków.
- Wykorzystanie interfejsu API możesz sprawdzić w [Google AI Studio](https://aistudio.google.com/usage?hl=pl) w sekcji **Panel** > **Wykorzystanie**.

Więcej informacji znajdziesz na [stronie Płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

## 2. Instalowanie pakietu SDK i wykonywanie pierwszego wywołania

Zainstaluj pakiet SDK i generuj tekst za pomocą jednego wywołania interfejsu API.

### Python

Zainstaluj pakiet SDK:

```
pip install -U google-genai
```

Zainicjuj klienta i wyślij żądanie:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

Zainstaluj pakiet SDK:

```
npm install @google/genai
```

Zainicjuj klienta i wyślij żądanie:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
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
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few words."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**Odpowiedź:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

W przypadku korzystania z interfejsu REST API zwraca pełny zasób `Interaction` zawierający metadane, statystyki wykorzystania i szczegółową historię tury.

Pakiety SDK udostępniają pełną odpowiedź, ale też wygodne właściwości, takie jak `interaction.output_text` i `interaction.output_image`, które umożliwiają bezpośredni dostęp do ostatecznych wyników. Więcej informacji o strukturze odpowiedzi znajdziesz w [omówieniu interakcji](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl). Szczegółowe informacje o instrukcjach systemowych i konfiguracji generowania znajdziesz w [przewodniku po generowaniu tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl).

## 3. Wyświetlaj odpowiedź stopniowo

Aby interakcje były płynniejsze, przesyłaj strumieniowo generowaną odpowiedź. Każde zdarzenie `step.delta` dostarcza fragment tekstu, który możesz od razu wyświetlić.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works"))
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent event : stream) {
    System.out.println(event);
  }
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Write a haiku about coding."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

Podczas strumieniowania serwer odpowiada strumieniem zdarzeń wysyłanych przez serwer (SSE). Każde zdarzenie zawiera typ i dane JSON.

**Odpowiedź:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

Szczegółowe informacje o obsłudze zdarzeń przesyłanych strumieniowo i typów delta znajdziesz w [przewodniku po interakcjach przesyłanych strumieniowo](https://ai.google.dev/gemini-api/docs/streaming?hl=pl).

## 4. Rozmowy wieloetapowe

Interfejs Interactions API obsługuje wieloetapowe rozmowy na 2 sposoby:

- **Stanowe (zalecane):** kontynuuj rozmowę na serwerze za pomocą `previous_interaction_id`. Idealny do większości procesów czatu i procesów agentowych, w których chcesz, aby serwer zarządzał historią i optymalizował buforowanie.
- **Bezstanowy:** zarządzaj historią rozmowy na urządzeniu klienta, przekazując w każdym żądaniu wszystkie poprzednie etapy (w tym pośrednie etapy myślenia modelu i narzędzia).

### Stanowy (zalecany)

Łącz interakcje, przekazując `previous_interaction_id`. Serwer zarządza za Ciebie pełną historią rozmowy.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
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

// Server-side state (recommended)
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("I have 2 dogs in my house."))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("How many paws are in my house?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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
            Input:  interactions.NewInteractionsInput("Explain quantum computing in simple terms."),
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
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### Bezstanowy

Ustaw `store=false` i zarządzaj historią rozmów po stronie klienta. Musisz zachować i ponownie przesłać wszystkie kroki wygenerowane przez model (w tym kroki `thought` i `function_call`) w dokładnie takiej samej formie, w jakiej zostały otrzymane.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("I have 2 dogs in my house.").build()))
        .build());

CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

interaction1.steps().ifPresent(history::addAll);

history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("How many paws are in my house?").build()))
        .build());

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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

    // 1. First turn
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Alex."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res1.Interaction.OutputText != nil {
        fmt.Println(*res1.Interaction.OutputText)
    }

    // 2. Second turn (passing PreviousInteractionID)
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What's my name?"),
            PreviousInteractionID: res1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**Odpowiedź:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

Druga interakcja zwraca pełny obiekt odpowiedzi, który zawiera tylko nowe kroki, ale jest oparty na kontekście poprzedniej tury. Więcej informacji o utrzymywaniu stanu znajdziesz w [przewodniku po rozmowach wieloetapowych](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#multi-turn-conversations). Możesz też zapoznać się z [trybem bezstanowym](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#stateless-conversations), który umożliwia zarządzanie historią po stronie klienta.

## 5. Rozpoznawanie multimodalne

Modele Gemini natywnie rozumieją obrazy, dźwięk, filmy i dokumenty. Przesyłaj multimedia wraz z tekstem w ramach jednego żądania.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

// Load a local image
byte[] imageBytes = Files.readAllBytes(Path.of("sample.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder()
                        .text("Compare this local image and this remote audio file.")
                        .build(),
                    ImageContent.builder()
                        .data(imageB64)
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .build(),
                    AudioContent.builder()
                        .uri("https://storage.googleapis.com/generativeai-downloads/data/sample.mp3")
                        .mimeType(AudioContentMimeType.AUDIO_MP3)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    imageBytes, err := os.ReadFile("path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "What is in this image?",
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

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**Odpowiedź:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

Dowiedz się, jak przekazywać obrazy, filmy i pliki audio, z [przewodnika po rozpoznawaniu obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl).

[hearing

Rozpoznawanie dźwięku

transkrybować pliki audio, podsumowywać je i odpowiadać na dotyczące ich pytania;](https://ai.google.dev/gemini-api/docs/audio?hl=pl)
[videocam

Rozpoznawanie filmów

analizować treści wideo, lokalizować zdarzenia i opisywać działania;](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl)
[description

Przetwarzanie dokumentów

wyodrębniać informacje z plików PDF i innych formatów dokumentów;](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl)

## 6. Generowanie multimodalne

Gemini może generować obrazy natywnie za pomocą modeli graficznych [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-image"))
        .input(InteractionsInput.of("Generate an image of a futuristic city skyline at sunset"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputImage().isPresent()) {
  ImageContent generatedImage = interaction.outputImage().get();
  if (generatedImage.data().isPresent()) {
    byte[] imageBytes = Base64.getDecoder().decode(generatedImage.data().get());
    Files.write(Path.of("generated_image.png"), imageBytes);
  }
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

    weatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_current_weather"),
        Description: genai.Ptr("Gets the current weather for a given location."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": []string{"location"},
        },
    })

    // 1. Send prompt with tool declaration
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like in Boston?"),
            Tools: []interactions.Tool{weatherTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Check if the model requested a function call
    for _, step := range res.Interaction.Steps {
        if call := step.FunctionCallStep; call != nil {
            fmt.Printf("Function to call: %s\n", call.Name)
            fmt.Printf("Arguments: %v\n", call.Arguments)

            // 3. Execute your local function and send the result back
            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3.8-flash"),
                    PreviousInteractionID: res.Interaction.ID,
                    Input: interactions.NewInteractionsInput([]interactions.Step{
                        interactions.NewStep(interactions.FunctionResultStep{
                            Name:   genai.Ptr(call.Name),
                            CallID: call.ID,
                            Result: interactions.NewFunctionResultStepResultUnion(`{"temperature": "72F", "condition": "Sunny"}`),
                        }),
                    }),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }

            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
        }
    }
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**Odpowiedź:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

Gdy model wygeneruje obraz, zwraca dane obrazu zakodowane w formacie base64 w kroku w tablicy `steps`, a także za pomocą właściwości `output_image`. Zapoznaj się z [przewodnikiem po generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl), aby dowiedzieć się więcej o współczynnikach proporcji, edytowaniu obrazów i odniesieniach.

[record\_voice\_over

Generowanie mowy

Generuj ekspresywną mowę wielu osób za pomocą Gemini 3.1 Flash TTS.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)
[music\_note

Generowanie muzyki

Twórz klipy i pełne utwory za pomocą Lyrii 3.5.](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl)

## 7. Korzystanie z uporządkowanych danych wyjściowych

Skonfiguruj model tak, aby zwracał kod JSON zgodny ze zdefiniowanym przez Ciebie schematem. Uporządkowane dane wyjściowe działają z bibliotekami [Pydantic](https://docs.pydantic.dev/latest/) (Python) i [Zod](https://zod.dev/) (JavaScript).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> recipeNameProp = new HashMap<>();
recipeNameProp.put("type", "string");
recipeNameProp.put("description", "Name of the recipe.");

Map<String, Object> itemsProp = new HashMap<>();
itemsProp.put("type", "string");

Map<String, Object> ingredientsProp = new HashMap<>();
ingredientsProp.put("type", "array");
ingredientsProp.put("items", itemsProp);
ingredientsProp.put("description", "List of ingredients.");

Map<String, Object> prepTimeProp = new HashMap<>();
prepTimeProp.put("type", "integer");
prepTimeProp.put("description", "Prep time in minutes.");

Map<String, Object> properties = new HashMap<>();
properties.put("recipe_name", recipeNameProp);
properties.put("ingredients", ingredientsProp);
properties.put("prep_time_minutes", prepTimeProp);

Map<String, Object> recipeJsonSchema = new HashMap<>();
recipeJsonSchema.put("type", "object");
recipeJsonSchema.put("properties", properties);
recipeJsonSchema.put("required", Arrays.asList("recipe_name", "ingredients"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(recipeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Give me a recipe for banana bread"))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Who won the latest Super Bowl and what was the score?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }

    // Optional: Inspect search queries and citations
    for _, step := range res.Interaction.Steps {
        if searchCall := step.GoogleSearchCallStep; searchCall != nil {
            fmt.Printf("Search queries: %v\n", searchCall.Arguments.Queries)
        } else if modelOut := step.ModelOutputStep; modelOut != nil {
            for _, part := range modelOut.Content {
                if textPart := part.TextContent; textPart != nil {
                    for _, annotation := range textPart.Annotations {
                        if citation := annotation.URLCitation; citation != nil {
                            var title, url string
                            if citation.Title != nil {
                                title = *citation.Title
                            }
                            if citation.URL != nil {
                                url = *citation.URL
                            }
                            fmt.Printf("Source: %s (%s)\n", title, url)
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**Odpowiedź:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

Blok tekstu wyjściowego zawiera prawidłowy ciąg znaków JSON, który jest zgodny z wymaganym schematem. Aby dowiedzieć się, jak definiować bardziej złożone struktury i rekurencyjne schematy, zapoznaj się z [przewodnikiem po uporządkowanych danych wyjściowych](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl).

## 8. Korzystanie z narzędzi

Opieraj odpowiedzi modelu na informacjach uzyskiwanych w czasie rzeczywistym za pomocą wyszukiwarki Google. Interfejs API automatycznie wyszukuje i przetwarza wyniki oraz zwraca cytowania.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));

// Print citations
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent && textContent.annotations().isPresent()) {
        System.out.println("\nCitations:");
        for (Annotation annotation : textContent.annotations().get()) {
          if (annotation instanceof URLCitation citation) {
            System.out.printf("  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
          }
        }
      }
    }
  }
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Calculate the 20th Fibonacci number and verify if it is prime."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if codeCall := step.CodeExecutionCallStep; codeCall != nil {
            fmt.Printf("Generated Code:\n%s\n", codeCall.Arguments.Code)
        } else if codeRes := step.CodeExecutionResultStep; codeRes != nil {
            fmt.Printf("Execution Output:\n%s\n", codeRes.Result)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**Odpowiedź:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

Szczegółowe informacje o krokach wyszukiwania znajdziesz w historii interakcji, a wynik końcowy zawiera przypisy w tekście wskazujące źródła internetowe.

Więcej informacji o wyodrębnianiu cytatów z wyszukiwarki znajdziesz w [przewodniku po ugruntowaniu w wyszukiwarce Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl). Z kolei w [przewodniku po łączeniu narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl) dowiesz się, jak łączyć ze sobą różne narzędzia.

[code

Wykonanie kodu

Uruchamiaj kod Pythona w bezpiecznym środowisku piaskownicy Borg.](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)
[link

Kontekst adresu URL

Przekazuj publiczne adresy URL bezpośrednio do odpowiedzi podstawowych w treści strony internetowej.](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)
[search

Wyszukiwanie plików

Indeksowanie i wyszukiwanie przesłanych dokumentów i plików multimedialnych.](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)
[map

Mapy Google

Uzasadniaj odpowiedzi danymi geoprzestrzennymi i danymi o lokalizacji z rzeczywistego świata.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)
[computer

Korzystanie z komputera

Automatyzacja przeglądarki i interakcja z ekranem.](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)

## 9. Wywoływanie własnych funkcji

Wywoływanie funkcji umożliwia połączenie modelu z kodem. Deklarujesz nazwę i parametry funkcji, model decyduje, kiedy ją wywołać, i zwraca argumenty strukturalne, a Ty wykonujesz ją lokalnie i odsyłasz wynik.

### Stanowy (zalecany)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

InteractionsInput userInput = InteractionsInput.of("What is the temperature in London?");
String previousId = null;
Interaction interaction = null;

while (true) {
  CreateModelInteraction.Builder paramsBuilder =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(userInput)
          .tools(Arrays.asList(weatherTool));
  if (previousId != null) {
    paramsBuilder.previousInteractionId(previousId);
  }

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(paramsBuilder.build())).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      functionResults.add(
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build());
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }

  userInput = InteractionsInput.ofStep(functionResults);
  previousId = interaction.id().orElse(null);
}

System.out.println(interaction.outputText().orElse(""));
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

    // Turn 1: Create a CSV file in the sandbox
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Write a Python script to save a CSV file 'sales.csv' with 5 rows of sample data."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var env *interactions.CreateModelInteractionEnvironment
    if turn1.Interaction.EnvironmentID != nil {
        env = genai.Ptr(interactions.NewCreateModelInteractionEnvironment(*turn1.Interaction.EnvironmentID))
    }

    // Turn 2: Reuse the sandbox environment to analyze the file created in Turn 1
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            PreviousInteractionID: turn1.Interaction.ID,
            Environment:           env,
            Input:                 interactions.NewInteractionsInput("Now read 'sales.csv' and compute the total revenue."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Bezstanowy

Możesz też używać wywoływania funkcji w trybie bezstanowym, zarządzając historią rozmowy po stronie klienta i ustawiając wartość `store=false`. W trybie bezstanowym musisz przekazywać pełną historię rozmowy w polu `input` każdej kolejnej prośby. Historia musi zawierać:

1. Początkowy krok `user_input`.
2. Wszystkie kroki wygenerowane przez model zwrócone w turze 1 (w tym kroki `thought` i `function_call`) w dokładnie takiej postaci, w jakiej zostały otrzymane.
3. Krok `function_result` zawierający dane wyjściowe wykonanej funkcji.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("What is the temperature in London?").build()))
        .build());

Interaction interaction = null;

while (true) {
  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .store(false)
          .input(InteractionsInput.ofStep(history))
          .tools(Arrays.asList(weatherTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    history.add(step);
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      FunctionResultStep fnResult =
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build();
      functionResults.add(fnResult);
      history.add(fnResult);
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }
}

System.out.println(interaction.outputText().orElse(""));
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

    recipeSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "recipe_name":       map[string]any{"type": "string"},
            "prep_time_minutes": map[string]any{"type": "integer"},
            "ingredients": map[string]any{
                "type":  "array",
                "items": map[string]any{"type": "string"},
            },
        },
        "required": []string{"recipe_name", "prep_time_minutes", "ingredients"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me a quick recipe for chocolate chip cookies."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
                    Schema:   recipeSchema,
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**Odpowiedź:**

W turze 1 model zwraca odpowiedź ze stanem `requires_action` i krokiem `function_call`:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

Po uruchomieniu funkcji lokalnie i przesłaniu wyniku (tura 2) otrzymasz ostateczną, ukończoną interakcję:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

Więcej informacji o funkcjach zaawansowanych, takich jak równoległe wywoływanie funkcji czy tryby wyboru funkcji, znajdziesz w [przewodniku po wywoływaniu funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl).

## 10. Uruchamianie agenta zarządzanego

Zarządzane agenty działają w zdalnej piaskownicy z dostępem do narzędzi takich jak wykonywanie kodu i zarządzanie plikami. Przekaż `agent` zamiast `model` i ustaw `environment="remote"`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("antigravity-preview-09-2026")
        .input(
            InteractionsInput.of(
                "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment: " + interaction.environmentId().orElse(""));
System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Solve this logic puzzle: Three gods A, B, and C are called True, False, and Random..."),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print thought summaries if returned
    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought Summary: %s\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer: %s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

Możesz też definiować i zapisywać [agenty niestandardowe](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl) z własnymi instrukcjami, umiejętnościami i źródłami danych.

[rocket\_launch

Krótkie wprowadzenie

Wykonaj pierwsze połączenie z agentem, przesyłaj strumieniowo odpowiedzi i utwórz niestandardowego agenta.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl)
[smart\_toy

Agent Antigravity

Możliwości, narzędzia, dane wejściowe multimodalne i ceny domyślnego agenta.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl)
[experiment

Agenty w AI Studio

Wizualne środowisko do tworzenia prototypów agentów bez pisania kodu.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl)

## 11. Uruchamianie zadań w tle

Skonfiguruj `background=True` tak, aby długotrwałe zadania były wykonywane asynchronicznie. Sprawdź wyniki z `interactions.get()`. Więcej informacji znajdziesz w [przewodniku po wykonywaniu w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Write a detailed analysis of the impact of artificial intelligence on modern healthcare."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");
System.out.println("Started background task: " + interactionId);
System.out.println("Status: " + interaction.status().map(InteractionStatus::value).orElse(""));

// Poll for completion
while (true) {
  Interaction result =
      client.interactions.get(new GetInteractionByIdRequest(interactionId)).interaction().get();
  String status = result.status().map(InteractionStatus::value).orElse("");
  System.out.println("Status: " + status);
  if ("completed".equals(status)) {
    System.out.println("\nResult:\n" + result.outputText().orElse(""));
    break;
  } else if ("failed".equals(status)) {
    System.out.println("Failed: " + result.errors().orElse(null));
    break;
  }
  Thread.sleep(5000);
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
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

    // Start a Deep Research agent in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:      interactions.AgentOption("deep-research-pro-preview-12-2025"),
            Input:      interactions.NewInteractionsInput("Research the competitive landscape of solid-state EV batteries in 2026."),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Started research job: %s\n", *interaction.ID)

    // Poll until completion
    for interaction.Status != interactions.InteractionStatusCompleted && interaction.Status != interactions.InteractionStatusFailed {
        time.Sleep(10 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        fmt.Printf("Current status: %s\n", interaction.Status)
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Research failed: %v\n", interaction.Errors)
    }
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**Odpowiedź:**

Początkowa odpowiedź jest zwracana natychmiast ze stanem `in_progress`:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

Po pełnym wykonaniu zadania w tle sprawdzenie stanu interakcji zwraca:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

Więcej informacji o asynchronicznym uruchamianiu modeli i agentów znajdziesz w [przewodniku po wykonywaniu w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl).

## Co dalej?

- [Wykonywanie w tle:](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) asynchroniczne wykonywanie długotrwałych zadań i zarządzanie stanem.
- [Generowanie tekstu:](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl) instrukcje systemowe, konfiguracja generowania i zaawansowane wzorce tekstu.
- [Generowanie obrazów:](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) formaty obrazu, edytowanie obrazów i odnośniki do stylu.
- [Rozpoznawanie obrazów:](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl) klasyfikacja, wykrywanie obiektów oraz pytania i odpowiedzi dotyczące obrazów.
- [Myślenie:](https://ai.google.dev/gemini-api/docs/thinking?hl=pl) używaj rozumowania opartego na łańcuchu myśli w przypadku złożonych zadań.
- [Wywoływanie funkcji:](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) tryby równoległy, kompozycyjny i ograniczony.
- [Wyszukiwarka Google:](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) grounding, cytaty i sugestie wyszukiwania.
- [Zarządzane agenty:](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl) gotowe agenty z funkcjami wykonywania kodu i zarządzania plikami.
- [Deep Research:](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) autonomiczne, wieloetapowe badania z planowaniem i syntezą.
- [Uporządkowane dane wyjściowe:](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) schematy JSON, wyliczenia i rekurencyjne definicje typów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-05 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-05 UTC."],[],[]]
