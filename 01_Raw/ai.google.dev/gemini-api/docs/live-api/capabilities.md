---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pl
fetched_at: 2026-05-05T20:43:37.695868+00:00
title: "Live API capabilities guide \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Live API capabilities guide

Jest to obszerny przewodnik, który zawiera informacje o możliwościach i konfiguracjach dostępnych w ramach interfejsu Live API.
Na stronie [Pierwsze kroki z interfejsem Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) znajdziesz omówienie i przykładowy kod dla typowych przypadków użycia.

## Zanim zaczniesz

- **Zapoznaj się z podstawowymi pojęciami:** jeśli jeszcze tego nie zrobiono, najpierw przeczytaj stronę [Wprowadzenie do interfejsu Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) .
  Poznasz podstawowe zasady działania interfejsu Live API, jego działanie i różne [metody implementacji](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach).
- **Wypróbuj interfejs Live API w AI Studio:** przed rozpoczęciem tworzenia możesz wypróbować interfejs Live API w [Google AI Studio](https://aistudio.google.com/app/live?hl=pl). Aby używać interfejsu Live API w Google AI Studio, wybierz **Stream** (Strumień).

## Porównanie modeli

W tej tabeli zestawiono najważniejsze różnice między modelami [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pl) i [Gemini 2.5 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=pl):

| Funkcja | Gemini 3.1 Flash (wersja testowa) | Podgląd na żywo Gemini 2.5 Flash |
| --- | --- | --- |
| **[Myślenie](#native-audio-output-thinking)** | Wykorzystuje `thinkingLevel` do kontrolowania głębokości myślenia za pomocą ustawień takich jak `minimal`, `low`, `medium` i `high`. Domyślnie jest ustawiona wartość `minimal`, aby optymalizować pod kątem najmniejszego opóźnienia. Zobacz [Poziomy i budżety](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#levels-budgets). | Używa parametru `thinkingBudget` do ustawiania liczby tokenów myślenia. Dynamiczne myślenie jest domyślnie włączone. Aby wyłączyć tę opcję, ustaw wartość `thinkingBudget` na `0`. Zobacz [Poziomy i budżety](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#levels-budgets). |
| **[Otrzymywanie odpowiedzi](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentservercontent)** | Pojedyncze zdarzenie serwera może zawierać jednocześnie wiele części treści (np. `inlineData` i transkrypcję). Aby uniknąć pominięcia treści, upewnij się, że kod przetwarza wszystkie części każdego zdarzenia. | Każde zdarzenie serwera zawiera tylko jedną część treści. Części są dostarczane w ramach osobnych zdarzeń. |
| **[Treści klienta](#incremental-updates)** | `send_client_content` jest obsługiwane tylko w przypadku wypełniania początkowej historii kontekstu (wymaga ustawienia `initial_history_in_client_content` w konfiguracji sesji). Aby wysyłać aktualizacje tekstowe podczas rozmowy, użyj ikony `send_realtime_input`. | `send_client_content` jest obsługiwany w trakcie całej rozmowy, aby wysyłać przyrostowe aktualizacje treści i ustalać kontekst. |
| **[Pokrycie](https://ai.google.dev/api/live?hl=pl#turncoverage)** | Domyślna wartość to `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. Tura modelu obejmuje wykrytą aktywność audio i wszystkie klatki wideo. | Domyślna wartość to `TURN_INCLUDES_ONLY_ACTIVITY`. Tura modelu obejmuje tylko wykrytą aktywność. |
| **[Niestandardowe VAD](#disable-automatic-vad)** (`activity_start`/`activity_end`) | Obsługiwane Wyłącz automatyczne wykrywanie aktywności głosowej i wysyłaj ręcznie wiadomości `activityStart` i `activityEnd`, aby kontrolować granice tur. | Obsługiwane Wyłącz automatyczne wykrywanie aktywności głosowej i wysyłaj ręcznie wiadomości `activityStart` i `activityEnd`, aby kontrolować granice tur. |
| **[Automatyczna konfiguracja VAD](#configure-automatic-vad)** | Obsługiwane Skonfiguruj parametry takie jak `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` i `silence_duration_ms`. | Obsługiwane Skonfiguruj parametry takie jak `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` i `silence_duration_ms`. |
| **[Asynchroniczne wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl#async-function-calling)** (`behavior: NON_BLOCKING`) | Nieobsługiwane Wywoływanie funkcji jest tylko sekwencyjne. Model nie zacznie odpowiadać, dopóki nie wyślesz odpowiedzi narzędzia. | Obsługiwane Ustaw wartość `behavior` na `NON_BLOCKING` w deklaracji funkcji, aby umożliwić modelowi dalsze interakcje podczas działania funkcji. Określ, jak model ma obsługiwać odpowiedzi, za pomocą parametru `scheduling` (`INTERRUPT`, `WHEN_IDLE` lub `SILENT`). |
| **[Proaktywny dźwięk](#proactive-audio)** | Nieobsługiwane | Obsługiwane Po włączeniu tej funkcji model może proaktywnie decydować, czy nie odpowiadać, jeśli treść wejściowa jest nieistotna. Ustaw wartość `proactive_audio` na `true` w konfiguracji `proactivity` (wymaga `v1alpha`). |
| **[Afektywny dialog](#affective-dialog)** | Nieobsługiwane | Obsługiwane Model dostosowuje styl odpowiedzi do ekspresji i tonu danych wejściowych. Ustaw `enable_affective_dialog` na `true` w konfiguracji sesji (wymaga `v1alpha`). |

Aby przeprowadzić migrację z Gemini 2.5 Flash Live na Gemini 3.1 Flash Live, zapoznaj się z [przewodnikiem po migracji](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pl#migrating).

## Nawiązywanie połączenia

Poniższy przykład pokazuje, jak utworzyć połączenie za pomocą klucza interfejsu API:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Rodzaje interakcji

W kolejnych sekcjach znajdziesz przykłady i kontekst różnych trybów wejścia i wyjścia dostępnych w interfejsie Live API.

### Wysyłanie dźwięku

Dźwięk musi być przesyłany jako nieprzetworzone dane PCM (nieprzetworzone 16-bitowe audio PCM, 16 kHz, little-endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### Formaty audio

Dane audio w interfejsie Live API są zawsze w formacie surowym, little-endian, 16-bitowym PCM. Wyjście audio zawsze korzysta z częstotliwości próbkowania 24 kHz. Dźwięk wejściowy ma natywną częstotliwość próbkowania 16 kHz, ale interfejs Live API w razie potrzeby zmieni częstotliwość próbkowania, więc można wysyłać dowolną częstotliwość próbkowania. Aby przekazać częstotliwość próbkowania dźwięku wejściowego, ustaw typ MIME każdego obiektu [Blob](https://ai.google.dev/api/caching?hl=pl#Blob) zawierającego dźwięk na wartość taką jak `audio/pcm;rate=16000`.

### Odbieranie dźwięku

Odpowiedzi dźwiękowe modelu są odbierane jako fragmenty danych.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### Wysyłam tekst

Tekst można wysyłać za pomocą funkcji `send_realtime_input` (Python) lub `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### Wysyłam film

Klatki wideo są wysyłane jako pojedyncze obrazy (np. JPEG lub PNG) z określoną liczbą klatek na sekundę (maksymalnie 1 klatka na sekundę).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### Aktualizacje przyrostowe treści

Używaj aktualizacji przyrostowych, aby wysyłać tekst, ustalać kontekst sesji lub przywracać kontekst sesji. W przypadku krótkich kontekstów możesz wysyłać interakcje krok po kroku, aby odzwierciedlić dokładną sekwencję zdarzeń:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

W przypadku dłuższych kontekstów zalecamy podanie podsumowania pojedynczej wiadomości, aby zwolnić okno kontekstu na potrzeby kolejnych interakcji. Inną metodę wczytywania kontekstu sesji znajdziesz w sekcji [Wznawianie sesji](https://ai.google.dev/gemini-api/docs/live-session?hl=pl#session-resumption).

### Zapisy tekstowe

Oprócz odpowiedzi modelu możesz też otrzymywać transkrypcje zarówno wyjścia audio, jak i wejścia audio.

Aby włączyć transkrypcję wyjścia audio modelu, w konfiguracji wysyłania ustaw wartość `output_audio_transcription`. Język transkrypcji jest wywnioskowany z odpowiedzi modelu.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Aby włączyć transkrypcję danych wejściowych audio modelu, w konfiguracji wysyłania ustawień wyślij `input_audio_transcription`.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Zmienianie głosu i języka

Modele [natywnego wyjścia audio](#native-audio-output) obsługują wszystkie głosy dostępne w naszych modelach [zamiany tekstu na mowę (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#voices). Wszystkie głosy możesz odsłuchać w [AI Studio](https://aistudio.google.com/app/live?hl=pl).

Aby określić głos, ustaw nazwę głosu w obiekcie `speechConfig` w ramach konfiguracji sesji:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Interfejs Live API obsługuje [wiele języków](#supported-languages).
Modele [natywnego wyjścia audio](#native-audio-output) automatycznie wybierają odpowiedni język i nie obsługują jawnego ustawiania kodu języka.

## Funkcje natywnego dźwięku

Nasze najnowsze modele mają [natywne wyjście audio](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pl), które zapewnia naturalnie brzmiącą mowę i lepszą wydajność w przypadku wielu języków.

### Myślę

Modele Gemini 3.1 używają parametru `thinkingLevel` do kontrolowania głębi myślenia. Dostępne są ustawienia takie jak `minimal`, `low`, `medium` i `high`. Domyślna wartość to `minimal`, aby zoptymalizować opóźnienie. Modele Gemini 2.5 używają parametru
`thinkingBudget` do ustawiania liczby tokenów myślenia. Więcej informacji o poziomach i budżetach znajdziesz w artykule [Poziomy i budżety](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#levels-budgets).

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Możesz też włączyć podsumowania myśli, ustawiając w konfiguracji wartość `includeThoughts` na `true`. Więcej informacji znajdziesz w sekcji [podsumowania myśli](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#summaries):

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Afektywny dialog

Ta funkcja umożliwia Gemini dostosowywanie stylu odpowiedzi do ekspresji i tonu rozmówcy.

Aby używać dialogu afektywnego, ustaw wersję interfejsu API na `v1alpha` i w wiadomości konfiguracyjnej ustaw `enable_affective_dialog` na `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Proaktywny dźwięk

Gdy ta funkcja jest włączona, Gemini może samodzielnie podjąć decyzję o nieudzieleniu odpowiedzi, jeśli treść jest nieistotna.

Aby go użyć, ustaw wersję interfejsu API na `v1alpha` i skonfiguruj pole `proactivity` w wiadomości konfiguracyjnej oraz ustaw `proactive_audio` na `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Wykrywanie aktywności głosowej (VAD)

Wykrywanie aktywności głosowej (VAD) umożliwia modelowi rozpoznawanie, kiedy ktoś mówi. Jest to niezbędne do prowadzenia naturalnych rozmów, ponieważ umożliwia użytkownikowi przerwanie modelu w dowolnym momencie.

Gdy VAD wykryje przerwę, bieżące generowanie zostanie anulowane i odrzucone. W historii sesji zachowywane są tylko informacje, które zostały już wysłane do klienta. Serwer wysyła wtedy wiadomość [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentservercontent), aby zgłosić przerwę.

Serwer Gemini odrzuca następnie wszystkie oczekujące wywołania funkcji i wysyła wiadomość `BidiGenerateContentServerContent` z identyfikatorami anulowanych wywołań.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### Automatyczne dostarczanie aplikacji wirtualnych

Domyślnie model automatycznie wykonuje VAD na ciągłym strumieniu wejściowym audio. VAD można skonfigurować za pomocą pola [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=pl#RealtimeInputConfig.AutomaticActivityDetection) w [konfiguracji](https://ai.google.dev/api/live?hl=pl#BidiGenerateContentSetup).

Gdy strumień audio zostanie wstrzymany na dłużej niż sekundę (np. z powodu wyłączenia mikrofonu przez użytkownika), należy wysłać zdarzenie [`audioStreamEnd`](https://ai.google.dev/api/live?hl=pl#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end), aby opróżnić pamięć podręczną dźwięku. Klient może w dowolnym momencie wznowić wysyłanie danych audio.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

W przypadku `send_realtime_input` interfejs API będzie automatycznie odpowiadać na dźwięk na podstawie VAD. Funkcja `send_client_content` dodaje wiadomości do kontekstu modelu w określonej kolejności, a `send_realtime_input` jest zoptymalizowana pod kątem szybkości reakcji kosztem deterministycznej kolejności.

### Automatyczna konfiguracja VAD

Aby mieć większą kontrolę nad aktywnością VAD, możesz skonfigurować te parametry: Więcej informacji znajdziesz w [dokumentacji API](https://ai.google.dev/api/live?hl=pl#automaticactivitydetection).

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### Wyłączanie automatycznego wykrywania aktywności głosowej

Automatyczne wykrywanie głosu można też wyłączyć, ustawiając wartość `realtimeInputConfig.automaticActivityDetection.disabled` na `true` w wiadomości konfiguracyjnej. W tej konfiguracji klient odpowiada za wykrywanie mowy użytkownika i wysyłanie wiadomości [`activityStart`](https://ai.google.dev/api/live?hl=pl#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) i [`activityEnd`](https://ai.google.dev/api/live?hl=pl#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) we właściwym czasie. W tej konfiguracji nie jest wysyłany `audioStreamEnd`. Zamiast tego każda przerwa w strumieniu jest oznaczana komunikatem `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

## Liczba tokenów

Łączną liczbę wykorzystanych tokenów znajdziesz w polu [usageMetadata](https://ai.google.dev/api/live?hl=pl#usagemetadata) zwróconej wiadomości serwera.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Rozdzielczość multimediów

Możesz określić rozdzielczość multimediów wejściowych, ustawiając pole `mediaResolution` w ramach konfiguracji sesji:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## Ograniczenia

Podczas planowania projektu weź pod uwagę te ograniczenia interfejsu Live API.

### Sposoby odpowiedzi

Modele audio obsługują tylko modalność odpowiedzi `AUDIO. Jeśli potrzebujesz odpowiedzi modelu w formie tekstu, użyj funkcji [transkrypcji dźwięku wyjściowego](#audio-transcription).

### Uwierzytelnianie klienta

Interfejs Live API domyślnie udostępnia tylko uwierzytelnianie serwer-serwer. Jeśli implementujesz aplikację Live API, korzystając z [podejścia klient-serwer](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach), musisz używać [tokenów tymczasowych](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pl), aby ograniczyć ryzyko związane z bezpieczeństwem.

### Czas trwania sesji

Sesje tylko audio są ograniczone do 15 minut, a sesje audio i wideo – do 2 minut.
Możesz jednak skonfigurować różne [techniki zarządzania sesją](https://ai.google.dev/gemini-api/docs/live-session?hl=pl), aby nieograniczenie wydłużać czas trwania sesji.

### Okno kontekstu

Sesja ma limit okna kontekstu wynoszący:

- 128 tys. tokenów w przypadku modeli [natywnego wyjścia audio](#native-audio-output)
- 32 tys. tokenów w przypadku innych modeli Live API

## Obsługiwane języki

Interfejs Live API obsługuje te 97 języków.

| Język | Kod BCP-47 | Język | Kod BCP-47 |
| --- | --- | --- | --- |
| afrikaans | `af` | łotewski | `lv` |
| akan | `ak` | litewski | `lt` |
| albański | `sq` | macedoński | `mk` |
| amharski | `am` | malajski | `ms` |
| arabski | `ar` | malajalam | `ml` |
| ormiański | `hy` | maltański | `mt` |
| asamski | `as` | maoryski | `mi` |
| azerski | `az` | marathi | `mr` |
| baskijski | `eu` | mongolski | `mn` |
| białoruski | `be` | nepalski | `ne` |
| bengalski | `bn` | norweski | `no` |
| bośniacki | `bs` | orija | `or` |
| bułgarski | `bg` | oromo | `om` |
| birmański | `my` | paszto | `ps` |
| kataloński | `ca` | perski | `fa` |
| cebuański | `ceb` | polski | `pl` |
| chiński | `zh` | portugalski | `pt` |
| chorwacki | `hr` | pendżabski | `pa` |
| czeski | `cs` | keczua | `qu` |
| duński | `da` | rumuński | `ro` |
| niderlandzki | `nl` | retoromański | `rm` |
| angielski | `en` | rosyjski | `ru` |
| estoński | `et` | serbski | `sr` |
| farerski | `fo` | sindhi | `sd` |
| filipiński | `fil` | syngaleski | `si` |
| fiński | `fi` | słowacki | `sk` |
| francuski | `fr` | słoweński | `sl` |
| galicyjski | `gl` | somalijski | `so` |
| gruziński | `ka` | sotho południowy | `st` |
| niemiecki | `de` | hiszpański | `es` |
| Kuchnia grecka | `el` | suahili | `sw` |
| gudżarati | `gu` | szwedzki | `sv` |
| hausa | `ha` | tadżycki | `tg` |
| hebrajski | `iw` | tamilski | `ta` |
| hindi | `hi` | telugu | `te` |
| węgierski | `hu` | tajski | `th` |
| islandzki | `is` | tswana | `tn` |
| indonezyjski | `id` | turecki | `tr` |
| irlandzki | `ga` | turkmeński | `tk` |
| włoski | `it` | ukraiński | `uk` |
| japoński | `ja` | urdu | `ur` |
| kannada | `kn` | uzbecki | `uz` |
| kazachski | `kk` | wietnamski | `vi` |
| khmerski | `km` | walijski | `cy` |
| ruanda-rundi | `rw` | zachodniofryzyjski | `fy` |
| koreański | `ko` | wolof | `wo` |
| kurdyjski | `ku` | joruba | `yo` |
| kirgiski | `ky` | zulu | `zu` |
| laotański | `lo` |  |  |

## Co dalej?

- Zapoznaj się z przewodnikami [Korzystanie z narzędzi](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl) i [Zarządzanie sesjami](https://ai.google.dev/gemini-api/docs/live-session?hl=pl), aby uzyskać najważniejsze informacje o skutecznym korzystaniu z interfejsu Live API.
- Wypróbuj interfejs Live API w [Google AI Studio](https://aistudio.google.com/app/live?hl=pl).
- Więcej informacji o modelach Live API znajdziesz na stronie Modele w sekcji [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-native-audio).
- Więcej przykładów znajdziesz w [książce kucharskiej Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=pl), [książce kucharskiej narzędzi Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=pl) i [skrypcie Live API Get Started](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
