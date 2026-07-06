---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pl
fetched_at: 2026-07-06T05:20:45.124690+00:00
title: "Pierwsze kroki z\u00a0interfejsem Gemini Live API za pomoc\u0105 pakietu Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Pierwsze kroki z interfejsem Gemini Live API za pomocą pakietu Google GenAI SDK

Interfejs Gemini Live API umożliwia dwukierunkową interakcję w czasie rzeczywistym z modelami Gemini, obsługującą wejścia audio, wideo i tekstowe oraz natywne wyjścia audio. Z tego przewodnika dowiesz się, jak zintegrować interfejs API za pomocą pakietu Google GenAI SDK na serwerze.

[Wypróbuj interfejs Live API w Google AI Studiomic](https://aistudio.google.com/live?hl=pl)
[Sklonuj przykładową aplikację z GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Korzystaj z umiejętności agenta do kodowaniaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl)

## Przegląd

Interfejs Gemini Live API używa protokołu WebSocket do komunikacji w czasie rzeczywistym. Pakiet SDK `google-genai` udostępnia interfejs asynchroniczny wysokiego poziomu do zarządzania tymi połączeniami.

Kluczowe pojęcia:

- **Sesja:** trwałe połączenie z modelem.
- **Konfiguracja:** ustawianie trybów (dźwięk/tekst), głosu i instrukcji systemowych.
- **Dane wejściowe w czasie rzeczywistym:** wysyłanie klatek audio i wideo jako obiektów binarnych.

## Łączenie z interfejsem Live API

Rozpocznij sesję Live API za pomocą klucza interfejsu API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

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

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
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

## Wysyłam tekst

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

## Wysyłanie dźwięku

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

Przykład pobierania dźwięku z urządzenia klienta (np. przeglądarki) znajdziesz w kompleksowym przykładzie w [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Wysyłam film

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

Przykład pobierania filmu z urządzenia klienta (np. przeglądarki) znajdziesz w kompleksowym przykładzie w [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Odbieranie dźwięku

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

Przykład aplikacji znajdziesz na GitHubie. Dowiesz się z niego, jak [odbierać dźwięk na serwerze](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) i [odtwarzać go w przeglądarce](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Odbieram wiadomość

Transkrypcje danych wejściowych użytkownika i danych wyjściowych modelu są dostępne w treści serwera.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Obsługa wywołań narzędzi

Interfejs API obsługuje wywoływanie narzędzi (wywoływanie funkcji). Gdy model zażąda wywołania narzędzia, musisz wykonać funkcję i odesłać odpowiedź.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## Co dalej?

- Przeczytaj pełny przewodnik po [możliwościach](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl) interfejsu Live API, aby poznać kluczowe funkcje i konfiguracje, w tym wykrywanie aktywności głosowej i natywne funkcje audio.
- Przeczytaj przewodnik [Korzystanie z narzędzi](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl), aby dowiedzieć się, jak zintegrować interfejs Live API z narzędziami i wywoływaniem funkcji.
- Aby dowiedzieć się, jak zarządzać długimi rozmowami, przeczytaj przewodnik [Zarządzanie sesjami](https://ai.google.dev/gemini-api/docs/live-session?hl=pl).
- Przeczytaj przewodnik [Tokeny tymczasowe](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pl), aby dowiedzieć się więcej o bezpiecznym uwierzytelnianiu w aplikacjach [klient-serwer](#implementation-approach).
- Więcej informacji o bazowym interfejsie WebSockets API znajdziesz w [dokumentacji interfejsu WebSockets API](https://ai.google.dev/api/live?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
