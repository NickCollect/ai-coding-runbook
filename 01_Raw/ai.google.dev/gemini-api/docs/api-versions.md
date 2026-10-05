---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=pl
fetched_at: 2026-10-05T06:32:32.452559+00:00
title: "Om\u00f3wienie wersji interfejsu API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumentacja API](https://ai.google.dev/api?hl=pl)

Prześlij opinię

# Omówienie wersji interfejsu API

Ten dokument zawiera ogólne omówienie różnic między wersjami `v1` i `v1beta` interfejsu Gemini API.

- **v1**: stabilna wersja interfejsu API. Funkcje w wersji stabilnej są w pełni obsługiwane przez cały okres istnienia wersji głównej. Jeśli zostaną wprowadzone zmiany powodujące niezgodność wsteczną, utworzymy nową wersję główną interfejsu API, a dotychczasowa wersja zostanie wycofana po upływie odpowiedniego czasu.
  W interfejsie API mogą być wprowadzane zmiany, które nie powodują błędów, bez zmiany wersji głównej. **Interfejs API interakcji** i jego podstawowe funkcje są ogólnie dostępne w `v1`.
- **v1beta** ta wersja zawiera wczesne funkcje i możliwości, które są aktywnie rozwijane. Funkcje w `v1beta` mogą ulec zmianom, ponieważ dopracowujemy je na podstawie opinii. Dzięki temu możesz wypróbować nowe funkcje, zanim zostaną one udostępnione w wersji stabilnej.

## Obsługa funkcji i możliwości

W tabeli poniżej znajdziesz informacje o dostępności funkcji w wersji `v1` (ogólnodostępnej) i `v1beta` (beta). Podstawowe możliwości interfejsu API i narzędzia dotyczą zarówno interfejsu Interactions API, jak i `generateContent`, chyba że podano inaczej:

| Funkcja | v1 | v1beta |
| --- | --- | --- |
| **Podstawowe możliwości interfejsu API** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=pl) |  |  |
| [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) |  |  |
| [Uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) |  |  |
| [Myślenie / rozumowanie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl) |  |  |
| [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/system-instructions?hl=pl) |  |  |
| [Wyjście audio (konfiguracja mowy)](https://ai.google.dev/gemini-api/docs/audio?hl=pl) |  |  |
| [Typ usługi (Priority / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) |  |  |
| **Narzędzia** |  |  |
| [Narzędzie do wykonywania kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) |  |  |
| [Grounding w wyszukiwarce Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) |  |  |
| [Grounding w Mapach Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl) |  |  |
| [Narzędzie kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) |  |  |
| [Narzędzie do wyszukiwania plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl) |  |  |
| [Narzędzie do korzystania z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl) |  |  |
| [Narzędzie Serwery MCP](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#mcp) |  |  |
| **Interfejsy API w czasie rzeczywistym** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=pl) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pl) |  |  |
| [Tokeny tymczasowe (interfejs API na żywo)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pl) |  |  |
| **Interfejsy API platformy** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=pl) |  |  |
| [Trasa usługi plików](https://ai.google.dev/gemini-api/docs/files?hl=pl) |  |  |
| [File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search?hl=pl) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=pl) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=pl) |  |  |
| [Zapisywanie kontekstu w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl) |  |  |

- – obsługiwane

## Konfigurowanie wersji interfejsu API w pakiecie SDK

Pakiety SDK interfejsu Gemini API domyślnie używają wersji `v1beta`, ale możesz wyraźnie określić wersje, ustawiając wersję interfejsu API, jak pokazano w tym przykładowym kodzie:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
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
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-24 UTC."],[],[]]
