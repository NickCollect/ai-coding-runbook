---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=pl
fetched_at: 2026-06-08T05:37:20.732774+00:00
title: "Interfejs Gemini Developer API a\u00a0platforma agent\u00f3w Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interfejs Gemini Developer API a platforma agentów Gemini Enterprise

Podczas tworzenia rozwiązań generatywnej AI za pomocą Gemini Google oferuje 2 interfejsy API:
[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=pl) i [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=pl).

Gemini Developer API to najszybsza droga do tworzenia, wdrażania i skalowania aplikacji opartych na Gemini. Większość programistów powinna korzystać z Gemini Developer API, chyba że potrzebuje określonych kontroli dla przedsiębiorstw.

Gemini Enterprise Agent Platform oferuje kompleksowy ekosystem funkcji i usług gotowych do użycia w przedsiębiorstwie, które umożliwiają tworzenie i wdrażanie aplikacji generatywnej AI opartych na Google Cloud Platform.

Niedawno uprościliśmy migrację między tymi usługami. Zarówno Gemini
Developer API, jak i Gemini Enterprise Agent Platform API są teraz dostępne za pomocą ujednoliconego
[pakietu Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

## Porównanie kodu

Na tej stronie znajdziesz porównanie kodu w przewodnikach Szybki start dotyczących Gemini Developer API i Gemini Enterprise Agent Platform w przypadku generowania tekstu.

### Python

Dostęp do usług Gemini Developer API i Gemini Enterprise Agent Platform możesz uzyskać za pomocą biblioteki `google-genai`. Instrukcje instalacji `google-genai` znajdziesz na stronie [bibliotek](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript i TypeScript

Dostęp do usług Gemini Developer API i Gemini Enterprise Agent Platform możesz uzyskać za pomocą biblioteki `@google/genai`. Instrukcje instalacji `@google/genai` znajdziesz na stronie [bibliotek](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Dostęp do usług Gemini Developer API i Gemini Enterprise Agent Platform możesz uzyskać za pomocą biblioteki `google.golang.org/genai`. Instrukcje instalacji `google.golang.org/genai` znajdziesz na stronie [bibliotek](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Inne przypadki użycia i platformy

Więcej informacji o innych platformach i przypadkach użycia znajdziesz w przewodnikach dotyczących konkretnych przypadków użycia w dokumentacji [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=pl)
i dokumentacji [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=pl).

## Wskazówki dotyczące migracji

Podczas migracji:

- Do uwierzytelniania musisz używać kont usługi Google Cloud. Więcej informacji znajdziesz w [dokumentacji Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=pl).
- Możesz użyć dotychczasowego projektu Google Cloud
  (tego samego, którego używasz do generowania klucza interfejsu API) lub możesz
  [utworzyć nowy projekt Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pl).
- Obsługiwane regiony mogą się różnić w zależności od tego, czy używasz Gemini Developer API czy Gemini Enterprise Agent Platform API. Zapoznaj się z listą
  [obsługiwanych regionów w przypadku generatywnej AI w Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=pl).
- Wszystkie modele utworzone w Google AI Studio trzeba ponownie wytrenować w Gemini Enterprise Agent Platform.

Jeśli nie musisz już używać klucza Gemini API w Gemini Developer API, postępuj zgodnie ze sprawdzonymi metodami zapewniania bezpieczeństwa i usuń go.

Aby usunąć klucz interfejsu API:

1. Otwórz stronę
   [danych logowania do interfejsu Google Cloud API](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Znajdź klucz interfejsu API, który chcesz usunąć, i kliknij ikonę **Działania**.
3. Kliknij **Usuń klucz interfejsu API**.
4. W oknie **Usuń dane logowania** kliknij **Usuń**.

   Rozpowszechnienie usunięcia klucza interfejsu API zajmuje kilka minut. Po zakończeniu rozpowszechniania cały ruch korzystający z usuniętego klucza interfejsu API jest odrzucany.

## Dalsze kroki

- Więcej informacji o rozwiązaniach generatywnej AI w Gemini Enterprise Agent Platform znajdziesz w artykule
  [Generatywna AI w Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
