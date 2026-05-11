---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=pl
fetched_at: 2026-05-11T05:01:12.326551+00:00
title: "Gemini Live API overview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Gemini Live API overview

Interfejs Live API umożliwia interakcje głosowe i wizualne z Gemini w czasie rzeczywistym z niewielkimi opóźnieniami. Przetwarza ciągłe strumienie dźwięku, obrazów i tekstu, aby dostarczać natychmiastowe, podobne do ludzkich odpowiedzi głosowe, tworząc naturalne doświadczenie konwersacyjne dla użytkowników.

![Omówienie interfejsu Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=pl)

[Wypróbuj interfejs Live API w Google AI Studiomic](https://aistudio.google.com/live?hl=pl)
[Sklonuj przykładowe aplikacje z GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Korzystaj z umiejętności agenta do kodowaniaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl)

## Przypadki użycia

Interfejs Live API może być używany do tworzenia agentów głosowych w czasie rzeczywistym w różnych branżach, m.in.:

- **E-commerce i handel detaliczny:** asystenci zakupów, którzy oferują spersonalizowane rekomendacje, oraz agenci obsługi klienta, którzy rozwiązują problemy klientów.
- **Gry:** interaktywne postacie niezależne, pomoc w grze i tłumaczenie treści w czasie rzeczywistym.
- **Interfejsy nowej generacji:** funkcje głosowe i wideo w robotyce, inteligentnych okularach i pojazdach.
- **Opieka zdrowotna:** towarzysze zdrowia, którzy wspierają pacjentów i edukują ich.
- **Usługi finansowe:** doradcy AI w zakresie zarządzania kapitałem i inwestycjami.
- **Edukacja:** mentorzy i towarzysze nauki oparte na AI, którzy zapewniają spersonalizowane instrukcje i opinie.

## Najważniejsze funkcje

Interfejs Live API oferuje kompleksowy zestaw funkcji do tworzenia niezawodnych agentów głosowych:

- [**Obsługa wielu języków:**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#supported-languages) rozmawiaj w 70 obsługiwanych językach.
- [**Przerwanie**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#interruptions): użytkownicy mogą w dowolnym momencie przerwać działanie modelu, aby uzyskać interaktywne odpowiedzi.
- [**Korzystanie z narzędzi:**](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl)
  integruje narzędzia takie jak wywoływanie funkcji i wyszukiwarka Google, aby umożliwiać dynamiczne interakcje.
- [**Transkrypcje audio:**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#audio-transcription) udostępnia transkrypcje tekstowe zarówno danych wejściowych użytkownika, jak i danych wyjściowych modelu.
- [**Aktywny dźwięk:**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#proactive-audio) pozwala kontrolować, kiedy i w jakich kontekstach model odpowiada.
- [**Dialog afektywny:**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#affective-dialog) dostosowuje styl i ton odpowiedzi do ekspresji użytkownika.

## Specyfikacja techniczna

W tabeli poniżej znajdziesz dane techniczne interfejsu Live API:

| Kategoria | Szczegóły |
| --- | --- |
| Rodzaje danych wejściowych | Audio (surowe 16-bitowe audio PCM, 16 kHz, little-endian), obrazy (JPEG <= 1 kl./s), tekst |
| Rodzaje danych wyjściowych | Audio (surowe 16-bitowe audio PCM, 24 kHz, little-endian) |
| Protokół | Połączenie WebSocket z zachowywaniem stanu (WSS) |

## Wybierz metodę implementacji

Podczas integracji z interfejsem Live API musisz wybrać jedną z tych metod implementacji:

- **Serwer-serwer:** backend łączy się z interfejsem Live API za pomocą [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Zwykle klient wysyła dane strumieniowe (audio, wideo, tekst) na serwer, który następnie przekazuje je do interfejsu Live API.
- **Klient-serwer:** kod frontendu łączy się bezpośrednio z interfejsem Live API za pomocą [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API), aby przesyłać strumieniowo dane z pominięciem backendu.

## Rozpocznij

Wybierz przewodnik odpowiedni dla Twojego środowiska programistycznego:

Serwer-serwer

### [Samouczek dotyczący pakietu GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pl)

Połącz się z interfejsem Gemini Live API za pomocą pakietu GenAI SDK, aby utworzyć wielomodową aplikację w czasie rzeczywistym z backendem w Pythonie.

Klient-serwer

### [Samouczek dotyczący WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pl)

Połącz się z interfejsem Gemini Live API za pomocą protokołu WebSocket, aby utworzyć multimodalną aplikację w czasie rzeczywistym z interfejsem JavaScript i tokenami tymczasowymi.

Pakiet Agent Development Kit

### [Samouczek pakietu ADK](https://google.github.io/adk-docs/streaming/)

Tworzenie agenta i korzystanie z pakietu Agent Development Kit (ADK) Streaming w celu włączenia komunikacji głosowej i wideo.

## Integracje z partnerami

Aby usprawnić tworzenie aplikacji audio i wideo działających w czasie rzeczywistym, możesz użyć integracji innej firmy, która obsługuje interfejs Gemini Live API przez WebRTC lub WebSockets.

[LiveKit

Korzystanie z interfejsu Gemini Live API z agentami LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Tworzenie czatbota AI działającego w czasie rzeczywistym za pomocą Gemini Live i Pipecat](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam od Software Mansion

Twórz aplikacje do strumieniowego przesyłania obrazu i audio na żywo za pomocą Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Agenty Vision według strumienia

Twórz aplikacje AI do obsługi głosu i wideo w czasie rzeczywistym za pomocą agentów Vision.](https://visionagents.ai/integrations/gemini)
[Voximplant

Łączenie połączeń przychodzących i wychodzących z interfejsem Live API za pomocą Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Twórz aplikacje konwersacyjne AI w czasie rzeczywistym za pomocą Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Pakiet Firebase AI SDK

Pierwsze kroki z interfejsem Gemini Live API przy użyciu Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
