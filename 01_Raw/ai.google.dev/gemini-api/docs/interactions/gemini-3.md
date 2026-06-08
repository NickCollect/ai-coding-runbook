---
source_url: https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=pl
fetched_at: 2026-06-08T05:30:49.728396+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pl)

Prześlij opinię

# Przewodnik dla programistów Gemini 3

Gemini 3 to nasza najbardziej inteligentna rodzina modeli, która opiera się na najnowocześniejszym rozumowaniu. Została zaprojektowana tak, aby realizować każdy pomysł dzięki opanowaniu przepływów pracy agentów, autonomicznego kodowania i złożonych zadań multimodalnych.
Z tego przewodnika dowiesz się, jakie są najważniejsze funkcje rodziny modeli Gemini 3 i jak je wykorzystać.

Zapoznaj się z naszą [kolekcją aplikacji Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pl), aby zobaczyć, jak model radzi sobie z zaawansowanym wnioskowaniem, autonomicznym kodowaniem i złożonymi zadaniami multimodalnymi.

Zacznij od kilku wierszy kodu:

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Poznaj serię Gemini 3

Gemini 3.1 Pro najlepiej sprawdza się w przypadku złożonych zadań, które wymagają szerokiej wiedzy o świecie i zaawansowanego wnioskowania w różnych modalnościach.

Gemini 3 Flash to nasz najnowszy model z serii 3, który oferuje inteligencję na poziomie Pro z szybkością i ceną Flash.

Nano Banana Pro (znany też jako Gemini 3 Pro Image) to nasz model generowania obrazów o najwyższej jakości, a Nano Banana 2 (znany też jako Gemini 3.1 Flash Image) to odpowiednik o dużej wydajności i niższej cenie.

Gemini 3.1 Flash-Lite to nasz model do pracy, który został stworzony z myślą o oszczędności i zadaniach o dużej skali.

Wszystkie modele Gemini 3 są obecnie dostępne w wersji testowej.

| Identyfikator modelu | Okno kontekstu (wejście / wyjście) | Granica wiedzy | Ceny (wejście / wyjście)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 mln / 64 tys. | Styczeń 2025 r. | 0,25 USD (tekst, obraz, film), 0,50 USD (dźwięk) / 1,50 USD |
| **gemini-3.1-flash-image-preview** | 128 tys. / 32 tys. | Styczeń 2025 r. | 0,25 USD (wejście tekstowe) / 0,067 USD (wyjście obrazowe)\*\* |
| **gemini-3.1-pro-preview** | 1 mln / 64 tys. | Styczeń 2025 r. | 2 USD / 12 USD (< 200 tys. tokenów)   4 USD / 18 USD (> 200 tys. tokenów) |
| **gemini-3-flash-preview** | 1 mln / 64 tys. | Styczeń 2025 r. | 0,50 USD / 3 USD |
| **gemini-3-pro-image-preview** | 65 tys. / 32 tys. | Styczeń 2025 r. | 2 USD (wejście tekstowe) / 0,134 USD (wyjście obrazowe)\*\* |

*\* Ceny dotyczą 1 miliona tokenów, o ile nie wskazano inaczej.*
*\*\* Ceny obrazów zależą od rozdzielczości. Szczegółowe informacje znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).*

Szczegółowe limity, ceny i dodatkowe informacje znajdziesz na
[stronie modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

## Nowe funkcje interfejsu API w Gemini 3

W Gemini 3 wprowadzamy nowe parametry, które zapewniają programistom większą kontrolę nad opóźnieniem, kosztami i wiernością multimodalną.

### Poziom myślenia

Modele z serii Gemini 3 domyślnie używają myślenia dynamicznego do analizowania promptów. Możesz użyć parametru `thinking_level`, który określa **maksymalną** głębokość wewnętrznego procesu rozumowania modelu przed wygenerowaniem odpowiedzi. Gemini 3 traktuje te poziomy jako względne limity myślenia, a nie ścisłe gwarancje tokenów.

Jeśli parametr `thinking_level` nie zostanie określony, Gemini 3 domyślnie ustawi wartość `high`. Aby uzyskać szybsze odpowiedzi z mniejszym opóźnieniem, gdy nie jest wymagane złożone rozumowanie, możesz ograniczyć poziom myślenia modelu do `low`.

| Poziom myślenia | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Opis |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nieobsługiwane | Obsługiwane (domyślnie) | Obsługiwane | W przypadku większości zapytań odpowiada ustawieniu „bez myślenia”. W przypadku złożonych zadań związanych z kodowaniem model może myśleć bardzo minimalnie. Minimalizuje opóźnienie w przypadku aplikacji do czatowania lub aplikacji o wysokiej przepustowości. Pamiętaj, że `minimal` nie gwarantuje, że myślenie jest wyłączone. |
| **`low`** | Obsługiwane | Obsługiwane | Obsługiwane | Minimalizuje opóźnienie i koszty. Najlepsze rozwiązanie w przypadku prostych instrukcji, czatów lub aplikacji o wysokiej przepustowości. |
| **`medium`** | Obsługiwane | Obsługiwane | Obsługiwane | Zrównoważone myślenie w przypadku większości zadań. |
| **`high`** | Obsługiwane (domyślnie, dynamiczne) | Obsługiwane (dynamiczne) | Obsługiwane (domyślnie, dynamiczne) | Maksymalizuje głębokość rozumowania. Model może znacznie dłużej generować pierwszy token wyjściowy (bez myślenia), ale wynik będzie bardziej przemyślany. |

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

W przypadku wszystkich modeli Gemini 3 zdecydowanie zalecamy pozostawienie parametru temperatury na jego domyślnej wartości `1.0`.

W przypadku poprzednich modeli często warto było dostosować temperaturę, aby kontrolować kreatywność i determinizm, ale możliwości rozumowania Gemini 3 są zoptymalizowane pod kątem ustawienia domyślnego. Zmiana temperatury (ustawienie jej poniżej 1.0) może prowadzić do nieoczekiwanych zachowań, takich jak pętle lub pogorszenie wydajności, szczególnie w przypadku złożonych zadań matematycznych lub związanych z rozumowaniem.

### Podpisy myśli

Modele Gemini 3 używają podpisów myśli, aby zachować kontekst rozumowania w wywołaniach interfejsu API. Te podpisy to zaszyfrowane reprezentacje wewnętrznego procesu myślowego modelu.

- **Tryb stanowy (zalecany)**: gdy używasz interfejsu Interactions API w trybie stanowym (podając `previous_interaction_id`), serwer automatycznie zarządza historią rozmów i podpisami myśli.
- **Tryb bezstanowy**: jeśli zarządzasz historią rozmów ręcznie, musisz uwzględnić bloki myśli z ich podpisami w kolejnych żądaniach, aby zweryfikować autentyczność.

Szczegółowe informacje znajdziesz na stronie [Podpisy myśli](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pl).

### Uporządkowane dane wyjściowe z narzędziami

Modele Gemini 3 umożliwiają łączenie [uporządkowanych danych wyjściowych](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pl) z wbudowanymi narzędziami, takimi jak
[powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pl), [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pl), [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pl) i [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl).

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
  -H "Api-Revision: 2026-05-20" \
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

### Generowanie obrazów

Gemini 3.1 Flash Image i Gemini 3 Pro Image umożliwiają generowanie i edytowanie obrazów na podstawie promptów tekstowych. Model używa
rozumowania do "przemyślenia" prompta i może pobierać dane w czasie rzeczywistym, takie jak
prognozy pogody czy wykresy giełdowe, zanim użyje [Grounding z wyszukiwarką Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pl) do wygenerowania obrazów o wysokiej wierności.

**Nowe i ulepszone możliwości:**

- **Renderowanie tekstu i obrazów w rozdzielczości 4K:** generuj wyraźny, czytelny tekst i diagramy w rozdzielczości do 2K i 4K.
- **Generowanie z Grounding:** użyj narzędzia `google_search`, aby weryfikować fakty i generować obrazy na podstawie informacji z rzeczywistego świata. Grounding z wyszukiwarką *grafiki* Google jest dostępny w Gemini 3.1 Flash Image.
- **Edytowanie w trybie konwersacyjnym:** wieloetapowa edycja obrazów przez proste poproszenie o zmiany (np. „Zmień tło na zachód słońca”). Ten przepływ pracy opiera się na **podpisach myśli** , aby zachować kontekst wizualny między etapami.

Szczegółowe informacje o proporcjach, przepływach pracy związanych z edycją i opcjach konfiguracji
znajdziesz w przewodniku [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=pl).

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
  -H "Api-Revision: 2026-05-20" \
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

**Przykładowa odpowiedź**

![Pogoda w Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=pl)

### Wykonywanie kodu z obrazami

Gemini 3 Flash może traktować widzenie jako aktywne badanie, a nie tylko statyczne spojrzenie. Łącząc rozumowanie z [wykonywaniem kodu](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pl), model formułuje plan, a następnie pisze i
wykonuje kod w Pythonie, aby powiększać, przycinać, dodawać adnotacje lub w inny sposób manipulować obrazami
krok po kroku, aby wizualnie uzasadnić swoje odpowiedzi.

**Możesz na przykład:**

- **Powiększanie i sprawdzanie:** model niejawnie wykrywa, kiedy szczegóły są zbyt małe (np. odczytywanie odległego wskaźnika lub numeru seryjnego), i pisze kod, aby przyciąć i ponownie sprawdzić obszar w wyższej rozdzielczości.
- **Matematyka wizualna i wykresy:** model może wykonywać wieloetapowe obliczenia za pomocą kodu (np. sumowanie pozycji na paragonie lub generowanie wykresu Matplotlib na podstawie wyodrębnionych danych).
- **Dodawanie adnotacji do obrazów:** model może rysować strzałki, ramki ograniczające lub inne adnotacje bezpośrednio na obrazach, aby odpowiadać na pytania przestrzenne, takie jak „Gdzie powinien znajdować się ten element?”.

Aby włączyć myślenie wizualne, skonfiguruj [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pl) jako narzędzie. W razie potrzeby model automatycznie użyje kodu do manipulowania obrazami.

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
    -H "Api-Revision: 2026-05-20" \
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

Więcej informacji o wykonywaniu kodu z obrazami znajdziesz w artykule [Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pl#images).

### Odpowiedzi funkcji multimodalnych

[Wywoływanie funkcji multimodalnych](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl#multimodal)
umożliwia użytkownikom uzyskiwanie odpowiedzi funkcji zawierających
obiekty multimodalne, co pozwala na lepsze wykorzystanie możliwości wywoływania funkcji
przez model. Standardowe wywoływanie funkcji obsługuje tylko odpowiedzi funkcji tekstowych:

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
#   -H "Api-Revision: 2026-05-20" \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

### Łączenie wbudowanych narzędzi i wywoływania funkcji

Gemini 3 umożliwia używanie wbudowanych narzędzi (takich jak wyszukiwarka Google, kontekst adresu URL
i [inne](https://ai.google.dev/gemini-api/docs/tools?hl=pl)) oraz niestandardowych narzędzi do [wywoływania funkcji](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl) w tym samym wywołaniu interfejsu API, co pozwala na
bardziej złożone przepływy pracy.

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

## Migracja z Gemini 2.5

Gemini 3 to nasza najbardziej zaawansowana rodzina modeli, która oferuje stopniowe ulepszenia w porównaniu z Gemini 2.5. Podczas migracji weź pod uwagę te kwestie:

- **Myślenie:** jeśli wcześniej używałeś złożonego inżynierii promptów (np.
  łańcucha myśli), aby zmusić Gemini 2.5 do rozumowania, wypróbuj Gemini 3 z
  `thinking_level: "high"` i uproszczonymi promptami.
- **Ustawienia temperatury:** jeśli Twój dotychczasowy kod wyraźnie ustawia temperaturę (szczególnie na niskie wartości w przypadku deterministycznych danych wyjściowych), zalecamy usunięcie tego parametru i użycie domyślnej wartości 1.0 w Gemini 3, aby uniknąć potencjalnych problemów z pętlami lub pogorszenia wydajności w przypadku złożonych zadań.
- **Rozumienie plików PDF i dokumentów:** jeśli polegasz na określonym zachowaniu podczas analizowania gęstych dokumentów, przetestuj nowe ustawienie `media_resolution_high`, aby zapewnić dalszą dokładność.
- **Zużycie tokenów:** migracja do domyślnych ustawień Gemini 3 może **zwiększyć** zużycie tokenów w przypadku plików PDF, ale **zmniejszyć** zużycie tokenów w przypadku filmów. Jeśli żądania przekraczają teraz okno kontekstu ze względu na wyższe domyślne rozdzielczości, zalecamy wyraźne zmniejszenie rozdzielczości multimediów.
- **Segmentacja obrazów:** możliwości segmentacji obrazów (zwracanie masek obiektów na poziomie pikseli) nie są obsługiwane w Gemini 3 Pro ani Gemini 3 Flash. W przypadku
  zadań wymagających wbudowanej segmentacji obrazów zalecamy dalsze korzystanie z
  Gemini 2.5 Flash z wyłączonym myśleniem lub [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl).
- **Korzystanie z komputera:** Gemini 3 Pro i Gemini 3 Flash obsługują [korzystanie
  z komputera](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=pl). W przeciwieństwie do serii 2.5 nie musisz używać osobnego modelu, aby uzyskać dostęp do narzędzia Korzystanie z komputera.
- **Obsługa narzędzi**: [łączenie wbudowanych narzędzi z wywoływaniem funkcji](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pl) jest teraz obsługiwane w przypadku modeli Gemini 3. [Grounding z Mapami Google
  jest też teraz obsługiwany w przypadku modeli Gemini 3
  .](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pl)

## Zgodność z OpenAI

W przypadku użytkowników korzystających z [warstwy zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl),
standardowe parametry (parametr `reasoning_effort` OpenAI) są automatycznie mapowane na
odpowiedniki w Gemini (`thinking_level`).

## Sprawdzone metody tworzenia promptów

Gemini 3 to model rozumowania, który zmienia sposób tworzenia promptów.

- **Precyzyjne instrukcje:** w promptach wejściowych używaj zwięzłych instrukcji. Gemini 3 najlepiej reaguje na bezpośrednie, jasne instrukcje. Może nadmiernie analizować rozbudowane lub zbyt złożone techniki inżynierii promptów używane w przypadku starszych modeli.
- **Szczegółowość danych wyjściowych:** Gemini 3 jest domyślnie mniej szczegółowy i woli podawać bezpośrednie, skuteczne odpowiedzi. Jeśli Twój przypadek użycia wymaga bardziej konwersacyjnej lub „gadatliwej” osobowości, musisz wyraźnie nakierować model w prompcie (np. „Wyjaśnij to jako przyjazny, rozmowny asystent”).
- **Zarządzanie kontekstem:** podczas pracy z dużymi zbiorami danych (np. całymi książkami,
  bazami kodu lub długimi filmami) umieść konkretne instrukcje lub pytania na
  końcu prompta, po kontekście danych. Aby zakotwiczyć rozumowanie modelu w podanych danych, zacznij pytanie od frazy takiej jak „Na podstawie powyższych informacji...”.

Więcej informacji o strategiach projektowania promptów znajdziesz w przewodniku [Inżynieria promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl).

## Najczęstsze pytania

1. **Jaka jest granica wiedzy w przypadku Gemini 3?** Modele Gemini 3 mają granicę wiedzy w styczniu 2025 r. Aby uzyskać najnowsze informacje, użyj narzędzia
   [Grounding z wyszukiwarką](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pl).
2. **Jakie są limity okna kontekstu?** Modele Gemini 3 obsługują okno kontekstu wejściowego o wielkości 1 miliona tokenów i do 64 tys. tokenów wyjściowych.
3. **Czy w przypadku Gemini 3 jest dostępny bezpłatny poziom?** Gemini 3 Flash `gemini-3-flash-preview` ma bezpłatny poziom w interfejsie Gemini API. Możesz bezpłatnie wypróbować Gemini 3.1 Pro i 3 Flash w Google AI Studio, ale w interfejsie Gemini API nie jest dostępny bezpłatny poziom dla `gemini-3.1-pro-preview`.
4. **Czy mój stary kod `thinking_budget` będzie nadal działać?** Tak, `thinking_budget` jest nadal obsługiwany w celu zapewnienia zgodności wstecznej, ale zalecamy migrację do `thinking_level`, aby uzyskać bardziej przewidywalną wydajność. Nie używaj obu tych parametrów w tym samym żądaniu.
5. **Czy Gemini 3 obsługuje interfejs Batch API?** Tak, Gemini 3 obsługuje interfejs
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl).
6. **Czy buforowanie kontekstu jest obsługiwane?** Tak, [buforowanie kontekstu](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=pl) jest obsługiwane w przypadku Gemini 3.
7. **Które narzędzia są obsługiwane w Gemini 3?** Gemini 3 obsługuje
   [wyszukiwarkę Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pl),
   [powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pl),
   [wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pl),
   [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pl) i
   [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pl). Obsługuje też
   standardowe [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl) w
   przypadku własnych narzędzi niestandardowych oraz w
   [połączeniu z wbudowanymi narzędziami](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pl).
8. **Co to jest `gemini-3.1-pro-preview-customtools`?** Jeśli używasz
   `gemini-3.1-pro-preview` a model ignoruje Twoje narzędzia niestandardowe na rzecz
   poleceń bash, wypróbuj model `gemini-3.1-pro-preview-customtools` zamiast.
   Więcej informacji [tutaj][customtools-model].

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-29 UTC."],[],[]]
