---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl
fetched_at: 2026-11-02T07:16:29.667775+00:00
title: "Logi i zbiory danych \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Logi i zbiory danych

Z tego przewodnika dowiesz się, jak wyświetlać logi z użycia interfejsu Gemini API w panelu Google AI Studio, aby lepiej zrozumieć zachowanie modelu i sposób, w jaki użytkownicy mogą wchodzić w interakcje z Twoimi aplikacjami. Wykorzystaj logowanie, aby obserwować i debugować, a także *opcjonalnie udostępniać Google opinie na temat użytkowania, aby pomóc ulepszać Gemini w różnych przypadkach użycia przez deweloperów*[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pl).

Obsługiwane są wszystkie wywołania interfejsów API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` i [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) z wyjątkiem agentów zarządzanych. Obejmuje to wywołania wykonywane przez punkty końcowe [zgodne z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

## Konfigurowanie logowania projektu

Domyślnie zarówno interfejs [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) API, jak i Generate Content API przechowują żądania (`store=true`). W przypadku interfejsu Interactions API umożliwia to też korzystanie z funkcji zarządzania stanem po stronie serwera.

W Google [AI Studio](https://aistudio.google.com/logs?hl=pl) możesz włączyć lub wyłączyć przechowywanie danych w przypadku poszczególnych projektów i w każdej chwili zmienić te ustawienia w panelu **Ustawienia** w [panelu logów interfejsu Gemini API](https://aistudio.google.com/logs?hl=pl). Możesz włączać i wyłączać logowanie niezależnie dla interfejsu `generateContent` API i [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) API, aby zmienić domyślne zachowanie przechowywania w projekcie.

### Logowanie na poziomie żądania

Oba interfejsy API domyślnie przechowują żądania (`store=true`):

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl):** domyślnie przechowuje żądania, aby uprościć zarządzanie stanem po stronie serwera.
- **Generate Content API (`generateContent`, `streamGenerateContent` i `batchGenerateContent`):** domyślnie przechowuje żądania w przypadku projektów utworzonych 26 października 2026 r. lub później. Projekty utworzone przed tą datą domyślnie nie przechowują żądań (`store=false`), chyba że w AI Studio włączono logowanie.

Właściwość `store` na poziomie żądania ma pierwszeństwo przed ustawieniem na poziomie projektu. Ustawienie `store` w żądaniach do interfejsu Generate Content API wymaga `google-genai` w wersji 2.33.0 lub nowszej w przypadku Pythona, `@google/genai` w wersji 2.31.0 lub nowszej w przypadku JavaScriptu, `google-genai` w wersji 1.79.0 lub nowszej w przypadku Javy oraz `google.golang.org/genai` w wersji 1.76.0 lub nowszej w przypadku Go. Oto jak możesz ustawić właściwość `store`:

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': True} # Set to False to disable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: true // Set to false to disable logging of this request
    }
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder()
            .store(true) // Set to false to disable logging of this request
            .build());

System.out.println(response.text());
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{
            Store: genai.Ptr(true), // Set to false to disable logging of this request
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
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
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
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
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
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

## Wyświetlanie logów projektu w AI Studio

1. Otwórz stronę Logi w [AI Studio](https://aistudio.google.com/logs?hl=pl).
2. Wybierz projekt z menu.
3. Dzienniki będą wyświetlane w tabeli w odwrotnej kolejności chronologicznej, jeśli istnieją.
4. W przypadku projektów utworzonych przed 26 października 2026 r. najpierw włącz logowanie interfejsu Generate Content API w [panelu ustawień](#configure-logging), aby obserwować logi projektu dotyczące interfejsu Generate Content API.

Kliknij wpis, aby wyświetlić podgląd ładunku. Możesz sprawdzić pełny prompt i odpowiedź Gemini oraz kontekst z poprzednich etapów. W przypadku żądań do **Interactions API** logi zawierają też bezpośredni link do `previous_interaction_id`.

## Konfigurowanie przechowywania danych w projekcie

Logi wygasają i są oznaczane do usunięcia po domyślnym okresie przechowywania wynoszącym 55 dni (chyba że są [zapisane w zbiorze danych](#create), który nie wygasa).
Okno przechowywania logów projektu możesz skonfigurować na maksymalnie 7, 14, 28 lub 55 dni.

## Tworzenie i udostępnianie zbiorów danych

Możesz zapisywać logi w zbiorach danych, aby skuteczniej je porządkować i eksportować.

- Na [stronie Logi](https://aistudio.google.com/logs?hl=pl) znajdź pasek filtrowania u góry, aby wybrać właściwość, według której chcesz filtrować.
- W widoku przefiltrowanym użyj pól wyboru, aby wybrać wszystkie lub poszczególne logi.
- Kliknij przycisk **Utwórz zbiór danych**, który pojawi się u góry listy.
- Nadaj nowemu zbiorowi danych nazwę i opcjonalnie dodaj opis.
- Zobaczysz utworzony właśnie zbiór danych z wybranym zestawem logów.
- Wyeksportuj zbiór danych do dalszej analizy jako pliki CSV, JSONL lub do Arkuszy Google.

Zbiory danych mogą być przydatne w wielu różnych przypadkach użycia.

- **Tworzenie zestawów wyzwań:** wprowadzaj ulepszenia w obszarach, w których chcesz poprawić działanie AI.
- **Tworzenie zestawów próbek:** na przykład próbka z rzeczywistego użycia do generowania odpowiedzi z innego modelu lub zbiór przypadków brzegowych do rutynowych kontroli przed wdrożeniem.
- **Zbiory ewaluacyjne:** zbiory, które odzwierciedlają rzeczywiste wykorzystanie ważnych funkcji, do porównania z innymi modelami lub iteracjami instrukcji systemowych.

Możesz przyczynić się do badań i rozwoju Gemini, udostępniając Google swoje zbiory danych jako przykłady demonstracyjne.

## Ograniczenia

Logowanie nie jest obecnie obsługiwane w przypadku:

- Modele Imagen i Veo
- Modele wektorów dystrybucyjnych Gemini
- Model Gemini Robotics
- Dane wejściowe zawierające filmy, GIF-y lub pliki PDF
- Agenty w publicznej wersji przedpremierowej w Gemini API

## Co dalej?

- **Prototyp z historią sesji:** użyj [AI Studio Build](https://aistudio.google.com/apps?hl=pl), aby tworzyć aplikacje za pomocą vibe codingu i dodać klucz interfejsu API, który umożliwi zapisywanie historii logów Gemini API na potrzeby funkcji opartych na AI.
- **Ponowne uruchamianie logów za pomocą interfejsu Gemini Batch API:** używaj zbiorów danych do próbkowania odpowiedzi i oceny modeli lub logiki aplikacji, ponownie uruchamiając logi za pomocą [interfejsu Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-26 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-26 UTC."],[],[]]
