---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=pl
fetched_at: 2026-08-10T03:23:35.617003+00:00
title: "Zrozumienie i liczenie token\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Zrozumienie i liczenie tokenów

Gemini i inne modele generatywnej AI przetwarzają dane wejściowe i wyjściowe z dokładnością do *tokena*.

**W przypadku modeli Gemini token odpowiada około 4 znakom.
100 tokenów to około 60–80 słów w języku angielskim.**

## Informacje o tokenach

Tokeny mogą być pojedynczymi znakami, np. `z`, lub całymi słowami, np. `cat`. Długie słowa są dzielone na kilka tokenów. Zbiór wszystkich tokenów używanych przez model nazywa się słownikiem, a proces dzielenia tekstu na tokeny – *tokenizacją*.

Gdy płatności są włączone, [koszt wywołania Gemini API](https://ai.google.dev/pricing?hl=pl) jest
częściowo określany przez liczbę tokenów wejściowych i wyjściowych, dlatego warto wiedzieć, jak je
zliczać.

## Zliczanie tokenów

Wszystkie dane wejściowe i wyjściowe z Gemini API są tokenizowane, w tym tekst, pliki graficzne i inne formaty nietekstowe.

Tokeny możesz zliczać na te sposoby:

- **Wywołaj funkcję `count_tokens` z danymi wejściowymi żądania.** Zwraca łączną liczbę tokenów *tylko w danych wejściowych*. Wykonaj to wywołanie przed wysłaniem danych wejściowych, aby sprawdzić rozmiar żądań.
- **Użyj parametru `usage` w odpowiedzi na interakcję.** Zwraca liczbę tokenów dla danych wejściowych (`total_input_tokens`), wyjściowych (`total_output_tokens`), myślenia (`total_thought_tokens`), treści z pamięci podręcznej (`total_cached_tokens`), użycia narzędzia (`total_tool_use_tokens`) i łączną liczbę tokenów (`total_tokens`).

### Zliczanie tokenów tekstowych

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Zliczanie tokenów wieloetapowych

Zliczaj tokeny w historii rozmów za pomocą parametru `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Zliczanie tokenów multimodalnych

Wszystkie dane wejściowe do Gemini API są tokenizowane, w tym obrazy, filmy i dźwięk.
Najważniejsze informacje o tokenizacji:

- **Obrazy**: obrazy o wymiarach ≤384 pikseli w obu wymiarach są liczone jako 258 tokenów. Większe obrazy są dzielone na kafelki o wymiarach 768 x 768 pikseli, z których każdy jest liczony jako 258 tokenów.
- **Film**: 263 tokeny na sekundę
- **Dźwięk**: 32 tokeny na sekundę

#### Tokeny obrazów

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**Przykład danych wbudowanych:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

#### Tokeny filmów

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Tokeny dźwięku

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Zliczanie tokenów instrukcji systemowych

Instrukcje systemowe są liczone jako część tokenów wejściowych:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Zliczanie tokenów narzędzi

Narzędzia (funkcje, wykonywanie kodu, wyszukiwarka Google) są również zliczane:

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
    model="gemini-3.6-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Okno kontekstu

Każdy model Gemini ma maksymalną liczbę tokenów, które może przetworzyć. Okno kontekstu określa łączny limit tokenów wejściowych i wyjściowych.

### Programowe pobieranie rozmiaru okna kontekstu

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.6-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.6-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

Rozmiary okien kontekstu znajdziesz na stronie [modeli](https://ai.google.dev/gemini-api/docs/models?hl=pl).

## Co dalej?

- [Generowanie tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl): podstawy generowania
- [Pamięć podręczna](https://ai.google.dev/gemini-api/docs/caching?hl=pl): zmniejszanie kosztów dzięki pamięci podręcznej
- [Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl): informacje o kosztach

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
