---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pl
fetched_at: 2026-10-26T05:57:27.754995+00:00
title: "Projektowanie g\u0142osu \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Projektowanie głosu

Projektowanie głosu umożliwia utworzenie zupełnie nowej, trwałej osobowości głosowej na podstawie opisu w języku naturalnym za pomocą punktu końcowego Gemini API Voices (`POST /v1beta/voices`). Zamiast ograniczać się do gotowych głosów lub nagrywania dźwięku referencyjnego, możesz opisać wiek postaci, barwę głosu, akcent i podstawowy sposób mówienia, a następnie otrzymać identyfikator `voice_...`, który można ponownie wykorzystać i który jest zapisany w Twoim projekcie.

Najszybszym sposobem na projektowanie, testowanie i ulepszanie niestandardowych głosów jest interaktywne studio **Voice Design** w [Google AI Studio](https://aistudio.google.com/generate-speech?hl=pl). Możesz generować niestandardowe persony na podstawie promptów tekstowych, testować je za pomocą przykładowych skryptów i kopiować uzyskany identyfikator `voice_...` bezpośrednio do kodu aplikacji.

[Wypróbuj w Google AI Studio](https://aistudio.google.com/generate-speech?hl=pl)

Zarówno [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pl) (`gemini-3.8-flash-tts`), jak i [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pl) (`gemini-3.8-flash-lite-tts`) obsługują projektowanie głosu.

## Tworzenie zaprojektowanego głosu

Użyj pakietu Google GenAI SDK (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) lub interfejsu REST API, aby utworzyć niestandardowy głos na podstawie opisu tekstowego. W przypadku głosów `"prompted"` zarówno `voices.create` (`CreateVoice`), jak i `voices.get` (`GetVoice`) zwracają pole `sample_audio` (`mime_type: "audio/wav"`, zakodowane w formacie base64 `data`) tylko do odczytu, dzięki czemu możesz od razu odsłuchać wygenerowany głos:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Jak działa projektowanie głosowe

1. **Utwórz głos na podstawie prompta:** zadzwoń pod numer `voices.create` (`POST /v1beta/voices`)`type="prompted"` i `store=True`.
2. **Otrzymywanie trwałego podglądu `voice_id` i `sample_audio`:** interfejs API generuje tożsamość głosową, zapisuje ją w projekcie i zwraca trwały identyfikator (np. `voice_abc123...`) wraz z `sample_audio` (`mime_type: "audio/wav"`, zakodowany w formacie base64 `data`) zawierającym wygenerowany podgląd dźwięku głosu.
3. **Synteza mowy:** podczas wywoływania funkcji `generateContent` przekaż `voice_id` w `speechConfig.voiceConfig.voice`.

## Syntezowanie mowy za pomocą zaprojektowanego głosu

Przekaż zwrócony identyfikator `id` (`voice_...`) w parametrze `voiceConfig.voice` podczas wywoływania funkcji `generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Zarządzanie głosami

W dowolnym momencie możesz wyświetlić listę zapisanych głosów, filtrować je, sprawdzać i usuwać za pomocą interfejsu Voices API (wszystkie parametry filtrowania znajdziesz w sekcji [Rozszerzona biblioteka głosów i filtrowanie](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pl#voice-library)).

- **Limity miejsca na dane i czas życia danych:** głosy stanowe (`store=True`, współdzielone w przypadku głosów wygenerowanych na podstawie promptu i replikowanych) mają limit **200 głosów na projekt** i **1-roczny czas życia danych**.
- **`sample_audio` dostępność:** `voices.create()` (`CreateVoice`) i `voices.get()` (`GetVoice`) wypełniają `sample_audio` (`mime_type:
  "audio/wav"`, zakodowane w formacie base64 `data`) dla głosów `"prompted"`. Aby uprościć listę, `voices.list()` (`ListVoices`) pomija `sample_audio` (a w przypadku głosów `"replicated"` i `"prebuilt"` parametr `sample_audio` jest nieustawiony).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Sprawdzone metody tworzenia promptów w projektowaniu głosowym

- **Stałe cechy głosu umieszczaj w projekcie Voice, a nie w `style`:** podczas tworzenia głosu w `voices.create` określ niezmienne cechy, takie jak wiek, płeć, barwa, tekstura głosu i akcent regionalny.
- **Zarezerwuj `speech_metadata.style` na emocje sytuacyjne:** po utworzeniu niestandardowego głosu używaj krótkich promptów `style` (np. `"whispered urgently"` lub `"cheerful and energetic"`), aby kierować działaniami krok po kroku bez zmiany podstawowej tożsamości mówcy.
- **Podawaj konkretne i zwięzłe informacje:** jasny opis w 1–2 zdaniach (np. *„Energiczna, wyrazista spikerka sportowa po trzydziestce z lekkim akcentem środkowo-zachodnim”*) daje lepsze i bardziej spójne wyniki niż sprzeczne lub zbyt długie akapity.

## Co dalej?

- Dowiedz się, jak replikować głos istniejącego mówcy w sekcji [Replikacja głosu](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=pl).
- Więcej informacji o stylizacji na poziomie wypowiedzi, tagach wstawianych i dialogach z udziałem wielu rozmówców znajdziesz w [przewodniku po zamianie tekstu na mowę](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-24 UTC."],[],[]]
