---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl
fetched_at: 2026-09-07T05:33:38.194222+00:00
title: "Pierwsze kroki \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Pierwsze kroki

Z tego przewodnika dowiesz się, jak zacząć korzystać z starszego interfejsu **generateContent** API.
W przypadku nowych projektów i aplikacji zdecydowanie zalecamy korzystanie z nowego **interfejsu Interactions API** , który jest najprostszym i najlepszym sposobem na tworzenie aplikacji z wykorzystaniem modeli i agentów Gemini.

Z tego przewodnika dowiesz się, jak zainstalować nasze
[biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl) i wysłać pierwsze żądanie, przesyłać strumieniowo
odpowiedzi, tworzyć rozmowy wieloetapowe i korzystać z narzędzi za pomocą standardowej
`generateContent` metody.

## Uzyskiwanie klucza interfejsu API

Aby korzystać z Gemini API, musisz mieć klucz interfejsu API, który umożliwi uwierzytelnianie żądań, egzekwowanie limitów bezpieczeństwa i śledzenie wykorzystania na koncie.

- Google AI Studio automatycznie tworzy projekt i klucz interfejsu API dla nowych użytkowników.
  Możesz go skopiować ze strony [kluczy interfejsów API](https://aistudio.google.com/api-keys?hl=pl).
- Jeśli potrzebujesz nowego klucza, w AI Studio kliknij **Utwórz klucz interfejsu API** i postępuj zgodnie z instrukcjami w oknie, aby dodać nową parę klucz-projekt.

[Utwórz klucz Gemini API](https://aistudio.google.com/apikey?hl=pl)

Ustaw klucz jako zmienną środowiskową:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Przejście na płatny poziom

Przejście na płatny poziom zwiększa limity szybkości i wymaga skonfigurowania Rozliczeń usługi Google Cloud.

- [[Na stronach kluczy interfejsów API lub projektów w AI Studio kliknij **Skonfiguruj rozliczenia**.](https://aistudio.google.com/api-keys?hl=pl)](https://aistudio.google.com/projects?hl=pl)
- Postępuj zgodnie z instrukcjami w oknie Cloud Billing, aby utworzyć lub połączyć konto rozliczeniowe, dodać formę płatności i zapłacić z góry co najmniej 10 USD (lub równowartość w innej walucie) w postaci płatnych środków.
- Wykorzystanie interfejsu API możesz sprawdzić w [Google AI Studio](https://aistudio.google.com/usage?hl=pl)
  w sekcji **Panel** > **Wykorzystanie**.

Więcej informacji znajdziesz na stronie [Rozliczenia](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

## Instalowanie pakietu Google GenAI SDK

### Python

W [Pythonie 3.9 lub nowszym](https://www.python.org/downloads/) zainstaluj pakiet
[`google-genai`](https://pypi.org/project/google-genai/)
za pomocą tego
[polecenia pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

W [Node.js w wersji 18 lub nowszej](https://nodejs.org/en/download/package-manager),
zainstaluj
[pakiet Google Gen AI SDK dla TypeScript i JavaScript](https://www.npmjs.com/package/@google/genai)
za pomocą tego
[polecenia npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Generowanie tekstu

Aby wygenerować odpowiedź tekstową, użyj metody `models.generate_content`
.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Odpowiadanie na bieżąco

Domyślnie model zwraca odpowiedź dopiero po zakończeniu całego procesu generowania. Aby przyspieszyć działanie i zwiększyć interaktywność, możesz
[przesyłać strumieniowo fragmenty odpowiedzi](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#stream) w miarę ich
generowania.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Rozmowy wieloetapowe

W przypadku rozmów wieloetapowych pakiety SDK udostępniają pomocniczą funkcję `chats` z informacjami o stanie, która
umożliwia tworzenie [czatu wieloetapowego](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#chat)
automatycznie zarządzającego historią rozmów.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Korzystanie z narzędzi

[Rozszerz możliwości modelu, powiązując odpowiedzi z wyszukiwarką Google, aby uzyskać dostęp do treści z internetu w czasie rzeczywistości.](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) Model automatycznie decyduje, kiedy wyszukiwać, wykonuje zapytania i syntetyzuje odpowiedź.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API obsługuje też inne wbudowane narzędzia:

- **[Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**:
  umożliwia modelowi pisanie i uruchamianie kodu Pythona w celu rozwiązywania złożonych problemów matematycznych.
- **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**: umożliwia powiązanie odpowiedzi z określonymi adresami URL stron internetowych.
- **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**: umożliwia
  przesyłanie plików i powiązanie odpowiedzi z ich treścią za pomocą wyszukiwania semantycznego.
- **[Mapy Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**: umożliwiają
  powiązanie odpowiedzi z danymi o lokalizacji oraz wyszukiwanie miejsc, tras i
  map.
- **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**: umożliwia
  modelowi interakcję z wirtualnym ekranem komputera, klawiaturą i myszą w celu
  wykonywania zadań.

## Wywoływanie funkcji niestandardowych

Użyj **[wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)** , aby połączyć
modele z niestandardowymi narzędziami i interfejsami API. Model określa, kiedy wywołać funkcję, i zwraca w odpowiedzi `functionCall`, którą aplikacja ma wykonać.

Ten przykład deklaruje funkcję symulującą temperaturę i sprawdza, czy model chce ją wywołać.

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Co dalej?

Teraz, gdy masz już podstawy korzystania z Gemini API, zapoznaj się z tymi przewodnikami, aby tworzyć bardziej zaawansowane aplikacje:

- [Generowanie tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl)
- [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)
- [Rozpoznawanie obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl)
- [Myślę](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)
- [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
- [Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)
- [Długi kontekst](https://ai.google.dev/gemini-api/docs/long-context?hl=pl)
- [Osadzanie](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
