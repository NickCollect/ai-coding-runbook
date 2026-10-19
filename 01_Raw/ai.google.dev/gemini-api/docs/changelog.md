---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=pl
fetched_at: 2026-10-19T05:42:45.740011+00:00
title: "Informacje o wersjach \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Informacje o wersjach

Ta strona zawiera informacje o aktualizacjach interfejsu Gemini API.

## 13 października 2026 r.

- **Ogólna dostępność modelu Gemini 4 Argon (`gemini-4-argon`):** opublikowaliśmy model [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pl) (`gemini-4-argon`), nasz najbardziej zaawansowany model stworzony do wykonywania złożonych zadań związanych z kodowaniem, agentami, matematyką i nauką.

  Informacje o zmianach w interfejsie API, cenach i wskazówki dotyczące migracji znajdziesz w artykule [Co nowego w Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/latest-model?hl=pl).

## 8 października 2026 r.

- **Wycofanie modelu Gemini 3.7 Flash:** model [`gemini-3.7-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.7?hl=pl) został wycofany i zastąpiony modelem [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=pl).
  Nie można go już wybrać w Google AI Studio, a żądania do interfejsu API wysyłane do modelu `gemini-3.7-flash` są automatycznie przekierowywane do modelu `gemini-3.8-flash`. Zaktualizuj ciąg znaków modelu do `gemini-3.8-flash` i zapoznaj się z [przewodnikiem po Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=pl).
- **Wycofanie modelu Gemini 3.5 Flash:** model [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=pl) został wycofany i zastąpiony przez [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=pl).
  Nie można go już wybrać w Google AI Studio, a żądania do interfejsu API wysyłane do modelu `gemini-3.5-flash` są automatycznie przekierowywane do modelu `gemini-3.6-flash`. Zaktualizuj ciąg modelu na `gemini-3.6-flash` (lub [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=pl)) i zapoznaj się z [przewodnikiem po Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=pl).
- **Wycofanie agenta Deep Research**: agent `deep-research-pro-preview-12-2025` zostanie wycofany i [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl#managed-agents) **23 października 2026 r.**`deep-research-pro-preview-12-2025`

  Przenieś prośby do jednej z nowszych wersji agenta [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl):

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=pl):
    zaprojektowany z myślą o szybkości i wydajności, idealny do przesyłania strumieniowego z powrotem do interfejsu klienta.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=pl):
    maksymalna kompleksowość automatycznego gromadzenia i syntezy kontekstu.

  Aby przeprowadzić migrację, zaktualizuj parametr `agent` w żądaniach `interactions.create` z `deep-research-pro-preview-12-2025` na `deep-research-preview-04-2026` (lub `deep-research-max-preview-04-2026`).

## 6 października 2026 r.

- **Ogólna dostępność Gemini Nano Banana 2.1:** udostępniliśmy [Gemini Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=pl) (`gemini-nano-banana-2.1`), najnowszy model do generowania obrazów i edytowania w trybie konwersacyjnym o wysokiej wydajności. Jest to aktualizacja modelu Nano Banana 2 ([`gemini-3.1-flash-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=pl)), która zachowuje szybkość i opłacalność na poziomie modelu Flash, a jednocześnie zapewnia znaczną poprawę jakości wizualnej, zgodności z promptem, spójności postaci w wielu turach, renderowania tekstu oraz generowania obrazów w szerokim i panoramicznym formacie obrazu (`1:4`, `4:1`, `1:8`, `8:1`) w rozdzielczościach `1K`, `2K` i `4K`.

  Aby rozpocząć, zapoznaj się z [przewodnikiem po generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).
- **Ogłoszenie o wycofaniu:** model `gemini-3.1-flash-image` został wycofany (nie ogłoszono daty wyłączenia). Przenieś do [`gemini-nano-banana-2.1`](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=pl).

## 22 września 2026 r.

- **Ogólna dostępność modeli Gemini 3.8 Flash TTS i Gemini 3.8 Flash-Lite TTS:** udostępniliśmy nasze modele audio zamiany tekstu na mowę (TTS) nowej generacji oraz punkt końcowy Gemini API Voices (`/v1beta/voices`):

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pl)
    (`gemini-3.8-flash-tts`)**: flagowy model TTS do zastosowań kreatywnych, zaprojektowany z myślą o jakości dźwięku na poziomie studyjnym, niuansach w interpretacji, dialektach regionalnych i stabilności w przypadku długich, wieloetapowych interakcji.
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pl)(`gemini-3.8-flash-lite-tts`)**: szybki i ekonomiczny model TTS stworzony, aby zastąpić `gemini-3.1-flash-tts-preview` w przypadku produkcji o wysokiej przepustowości i kaskad agentów głosowych w czasie rzeczywistym.
  - **[Projektowanie głosu](https://ai.google.dev/gemini-api/docs/voice-design?hl=pl), [replikacja głosu](https://ai.google.dev/gemini-api/docs/voice-replication?hl=pl) i [rozszerzona biblioteka głosów](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#voice-library):** twórz trwałe, niestandardowe profile głosowe na podstawie promptów tekstowych, replikuj głosy po weryfikacji zgody i wysyłaj zapytania do ponad 150 gotowych i niestandardowych głosów.

  Aby rozpocząć, zapoznaj się z [przewodnikiem po zamianie tekstu na mowę](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).

## 18 września 2026 r.

- **Aktualizacja dostępu do modeli Gemini 2.5:** aby zapewnić niezawodne działanie wszystkim użytkownikom, ograniczamy dostęp do modeli 2.5 do osób, które aktywnie korzystały z nich w przeszłości. Te modele nie są wycofane i będą nadal obsługiwane przez interfejs API do odwołania. W przypadku nowych projektów używaj naszych najnowszych modeli: 3.5 Flash-Lite lub 3.8 Flash. Dzięki temu możemy utrzymać wystarczającą przepustowość zarówno w przypadku dotychczasowych przepływów pracy, jak i nowych aplikacji.

## 17 września 2026 r.

- **agent Antigravity 09-2026**: wydano `antigravity-preview-09-2026`, które zastępuje i wycofuje `antigravity-preview-05-2026`.

  Jeśli uruchamiasz agenta w zdalnym środowisku piaskownicy (`environment: "remote"`) i wykonujesz tylko kroki `output_text` lub `model_output`, zaktualizuj ciąg agenta. Nic innego się nie zmieni.

  Jeśli uruchamiasz narzędzia lokalnie (`local_environment`) lub analizujesz kroki `function_call`, wbudowane narzędzia uległy zmianie. Parametry używają formatu PascalCase zamiast snake\_case, a edycje plików wykorzystują zamianę zakresu wierszy zamiast pełnego przepisywania.

  | Możliwości | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | Tworzenie plików | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | Edytowanie plików | `write_file(path, content)`, pełne przeredagowanie | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | Odczytywanie pliku | `read_file(path, offset, limit)`, przesunięcia bajtów | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | Wykaz kategorii | `list_files(path)` | `list_dir(DirectoryPath)` |
  | Wyszukiwanie plików i Code Search | Żadne, agenty używały poleceń powłoki | `find_by_name(SearchDirectory, Pattern, MaxDepth)` i `grep_search(SearchPath, Query, IsRegex)` |
  | Wykonywanie poleceń powłoki | `code_execution(command, timeout_seconds)` | Bez zmian |
  | Wyszukiwarka Google | `google_search(queries)` | Bez zmian |

  Zapoznaj się z przewodnikiem po [agencie Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl).
  `antigravity-preview-05-2026` zostanie wyłączona 5 października 2026 r. Informacje o tym znajdziesz na stronie [wycofanych funkcji](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl#managed-agents).

## 15 września 2026 r.

- **Ogólna dostępność modeli Gemini 3.8 Live i Gemini 3.8 Live Extended Thinking:** udostępniliśmy 2 nowe modele audio-to-audio do aplikacji głosowych działających w czasie rzeczywistym, które korzystają z interfejsu Live API:

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=pl)): domyślna opcja w przypadku większości funkcji agenta głosowego o krótkim czasie oczekiwania i dialogów w czasie rzeczywistym bez opóźnień w rozumowaniu. Funkcje obejmują przeplatanie rozumowania, domyślne asynchroniczne wywoływanie funkcji i pełne aktualizacje treści klienta sesji.
  - **Gemini 3.8 Live Extended Thinking** ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=pl)): model audio-audio o wysokim poziomie rozumowania, który obsługuje rozumowanie w tle podczas interakcji audio na żywo. Jest zalecany, gdy wymagany jest wyższy poziom rozumowania w tle.

  Aby rozpocząć, zapoznaj się z [przewodnikiem po Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl), [przewodnikiem po możliwościach](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pl) i [przewodnikiem po myśleniu](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=pl).

## 3 września 2026 r.

- **Lyria 3.5 w wersji ogólnodostępnej:** udostępniliśmy model generowania muzyki nowej generacji od Google:

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=pl): generowanie pełnych utworów z ulepszoną spójnością muzyczną, naturalnym wokalem oraz szczegółową kontrolą nad czasem trwania i strukturą.

  Model obsługuje dane wejściowe w formie tekstu i obrazu oraz generuje wysokiej jakości dźwięk stereo o częstotliwości próbkowania 44,1 kHz. Szczegółowe informacje i przykłady kodu znajdziesz w przewodniku po [generowaniu muzyki](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl).

## 2 września 2026 r.

- **Ogólnie dostępny model Gemini 3.8 Flash:** wydany`gemini-3.8-flash`, nasz najbardziej inteligentny model Flash, zaprojektowany z myślą o długofalowej inżynierii oprogramowania, autonomicznych agentach i złożonych firmowych przepływach pracy.

  Aby rozpocząć, zapoznaj się ze stroną modelu [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pl) i [przewodnikiem po Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=pl).

## 1 września 2026 r.

- **Rozumienie filmów przez agentów:** udostępniliśmy rozumienie filmów przez agentów w modelach Gemini 3.7 Flash, 3.6 Flash i 3.5 Flash-Lite w interfejsach Interactions i GenerateContent API. Model dynamicznie porusza się po osiach czasu filmów,
  żądając transkrypcji, klatek lub ścieżek audio na żądanie. W przypadku długich treści ta metoda wykorzystuje nawet o 88% mniej tokenów niż przetwarzanie statyczne.

  Więcej informacji znajdziesz w przewodniku [Analizowanie filmów przez agenta](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#agentic-video-understanding).

## 27 sierpnia 2026 r.

- **Ogólna dostępność Gemini Omni Flash:** `gemini-omni-1.1-flash` udostępniliśmy ogólnie dostępną wersję naszego szybkiego, konwersacyjnego modelu do generowania i edytowania filmów. Ta wersja zawiera ważne nowe funkcje:

  - **Rozszerzenie filmu:** możesz płynnie rozszerzać istniejące filmy, generując kontynuacje na końcu klipu za pomocą zadania `extend` lub bezpośrednio za pomocą prompta.
  - **Interpolacja (pierwsza i ostatnia klatka):** wygeneruj film z przejściem między 2 obrazami, używając zadania `image_to_video` z maksymalnie 2 obrazami.
  - **Kontrola rozdzielczości:** nowy parametr `resolution` w `video_config` obsługuje dane wyjściowe `360p`, `720p` (domyślnie), `1080p` i `4k`.
    Dane wyjściowe w rozdzielczości 1080p i 4K są generowane za pomocą skalowania.

  Obecny punkt końcowy `gemini-omni-flash-preview` zostanie wycofany 30 września 2026 r.

  Aby rozpocząć, zapoznaj się ze stroną modelu [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=pl) i [przewodnikiem po modelu Omni](https://ai.google.dev/gemini-api/docs/omni?hl=pl).

## 26 sierpnia 2026 r.

- **Ogólna dostępność Gemini 3.5 Transcribe:** udostępniliśmy 2 dedykowane modele zamiany mowy na tekst oparte na rozumieniu dźwięku przez Gemini:

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`): bardzo dokładna, o niskim opóźnieniu, niestrumieniowa funkcja zamiany mowy na tekst z wykrywaniem języka na podstawie wypowiedzi w ponad 85 językach, rozróżnianiem mówców, znacznikami czasu na poziomie słów i ustawianiem preferencji dla słownictwa niestandardowego (do 1000 terminów).
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`):
    dwukierunkowe przesyłanie strumieniowe zamiany mowy na tekst z małymi opóźnieniami przez WebSockets przy użyciu interfejsu Live API, obsługujące tymczasowe i sfinalizowane zdarzenia transkrypcji, tryb inteligentnej transkrypcji oraz wiele strategii wykrywania aktywności głosowej (VAD).

  Aby rozpocząć, zapoznaj się z [przewodnikiem po transkrypcji dźwięku](https://ai.google.dev/gemini-api/docs/transcribe?hl=pl), [przewodnikiem po transkrypcji na żywo](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=pl) i [stroną modelu Gemini 3.5 Transcribe](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=pl).

## 13 sierpnia 2026 r.

- **Ogólna dostępność Gemini 3.7 Flash:** udostępniliśmy nasz najbardziej inteligentny model do kodowania i agentów:

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`): znaczne ulepszenia w zakresie inżynierii oprogramowania, tworzenia stron internetowych i Agentic Workflows, dostępne w cenie początkowej do 31 grudnia 2026 r.

  Aby rozpocząć, zapoznaj się ze stroną modelu [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=pl) i [przewodnikiem po najnowszych modelach](https://ai.google.dev/gemini-api/docs/latest-model?hl=pl).

## 30 lipca 2026 r.

- **Gemini Robotics ER 2 w publicznej wersji przedpremierowej:** udostępniliśmy 2 nowe punkty końcowe modeli rozumowania ucieleśnionego na potrzeby robotyki:

  - `gemini-robotics-er-2-preview`: zaawansowane rozumowanie przestrzenne, wykonywanie kodu przez agenta, wieloetapowe koordynowanie narzędzi, wyszukiwanie momentów w filmie, klasyfikowanie postępów i koordynacja wielu robotów.
  - `gemini-robotics-er-2-streaming-preview`: zoptymalizowany pod kątem strumieniowego przesyłania tekstu w czasie rzeczywistym za pomocą interfejsu Live API, co umożliwia działanie agentów robotów z niskim opóźnieniem i dwukierunkowym wejściem audio i wideo.

  Oba punkty końcowe modelu akceptują dane wejściowe w formie tekstu, obrazu, filmu i dźwięku oraz obsługują wywoływanie funkcji z zachowaniem blokującym w przypadku działań fizycznych robotów.
  Aby rozpocząć, zapoznaj się z [omówieniem Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl). W przypadku zastosowań strumieniowania w czasie rzeczywistym zapoznaj się z sekcją [Robotyka ze strumieniowaniem](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl).
- **Ogłoszenie o wycofaniu:** model `gemini-robotics-er-1.6-preview` zostanie [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 31 sierpnia 2026 r.

## 21 lipca 2026 r.

- **Ogólna dostępność modeli Gemini 3.6 Flash i Gemini 3.5 Flash-Lite:**
  udostępniliśmy stabilne, gotowe do wykorzystania w środowisku produkcyjnym wersje naszych najnowszych modeli Flash 3.x:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): model o większej wydajności tokenów i lepszych możliwościach planowania kodu/agentów w porównaniu z modelem 3.5 Flash, ale w niższej cenie. Odpowiada na uwagi deweloperów dotyczące nadmiernej szczegółowości danych wyjściowych.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): opcja podagenta o niskim opóźnieniu i wysokiej opłacalności, zaprojektowana do automatyzacji dużych ilości danych.

  Więcej informacji znajdziesz w [przewodniku po Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=pl).
- **Wycofane parametry:** parametry próbkowania `temperature`, `top_p` i `top_k` zostały wycofane. Szczegółowe informacje znajdziesz w [przewodniku po Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=pl#sampling-parameter-deprecation).

## 6 lipca 2026 r.

- [Logi dewelopera](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl) w przypadku interfejsu Interactions API: logi obsługiwanych wywołań interfejsu API Interactions są teraz widoczne na [panelu AI Studio](https://aistudio.google.com/logs?hl=pl).

## 30 czerwca 2026 r.

- **Gemini Omni Flash w publicznej wersji przedpremierowej**: `gemini-omni-flash-preview` udostępniliśmy wysokowydajny model multimodalny zaprojektowany do szybkiego generowania filmów i konwersacyjnej edycji filmów. Za pomocą [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) możesz generować filmy o długości 3–10 sekund w rozdzielczości 720p na podstawie opisów tekstowych lub animować obrazy, a następnie edytować i ulepszać wyniki w trybie konwersacyjnym. Aby rozpocząć, zapoznaj się z przewodnikiem po [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=pl) i kartą modelu [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=pl).
- Udostępniliśmy ogólnie model `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite), czyli nasz wbudowany model multimodalny zoptymalizowany pod kątem bardzo małych opóźnień oraz ekonomicznego generowania i edytowania obrazów. Zapoznaj się z kartą modelu [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=pl) i przewodnikiem [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

## 24 czerwca 2026 r.

- **Computer Use:** udostępniliśmy publiczną wersję przedpremierową narzędzia [Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl) w Gemini 3.5 Flash. Ta wersja obejmuje uproszczone działania z intencjami, wbudowaną obsługę środowisk przeglądarki, urządzeń mobilnych i komputerów, konfigurowalne zasady bezpieczeństwa oraz zaawansowane wykrywanie wstrzykiwania promptów.

## 17 czerwca 2026 r.

- **Obsługa strumieniowego przesyłania danych na potrzeby generowania mowy:** strumieniowe przesyłanie danych za pomocą `streamGenerateContent` (i `stream: true` w interfejsie Interactions API) jest teraz obsługiwane w przypadku modelu `gemini-3.1-flash-tts-preview`. Więcej informacji znajdziesz w przewodniku [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#streaming).

## 15 czerwca 2026 r.

- **Ogłoszenie o wycofaniu:**  te modele generowania obrazów zostaną wycofane i [wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) **17 sierpnia 2026 r.**:

  - **Modele Imagen 4 i Gemini 3 do generowania obrazów:**
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  Aby przenieść kod do nowszych stabilnych lub testowych punktów końcowych, zapoznaj się ze stroną [Wycofywanie Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl#imagen-models).
- **Ogłoszenie o wycofaniu:**  te modele do generowania filmów zostaną wycofane i [wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) **30 czerwca 2026 r.**:

  - **Modele Veo:**
    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

  Aby uniknąć przerw w działaniu usługi, zaktualizuj integrację, tak aby używała identyfikatorów modeli Veo 3.1 w wersji testowej (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) lub modeli 3.1 GA dostępnych na platformie [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=pl).
- **Ogłoszenie o wycofaniu:**  eksperymentalne narzędzie GMP Contextual View (stały interfejs do powiązania ze źródłami informacji przy użyciu Map Google) zostanie [wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) **15 czerwca 2026 r.**:

## 1 czerwca 2026 r.

- Te modele Gemini 2.0 zostały [wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Zamiast niej użyj [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) lub [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl).

## 28 maja 2026 r.

- Wprowadziliśmy `gemini-3.1-flash-image` (Nano Banana 2) i `gemini-3-pro-image` (Nano Banana Pro), czyli ogólnodostępne wersje naszych natywnych modeli wizualnych: [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=pl) i [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=pl).
- **Generowanie obrazów na podstawie filmów:** możesz teraz przekazywać plik wideo (przez bezpośrednie przesłanie lub jako publiczny adres URL w YouTube) jako kontekst multimodalny wraz z promptem tekstowym, aby generować wysokiej jakości miniatury, plakaty filmowe lub infografiki podsumowujące. Ta funkcja jest obsługiwana wyłącznie w modelu `gemini-3.1-flash-image`. Więcej informacji znajdziesz w przewodniku [Generowanie obrazów z filmów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#video-to-image).
- Ogłoszenie o wycofaniu: modele `gemini-3.1-flash-image-preview` i `gemini-3-pro-image-preview` zostały wycofane i [zostaną wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 25 czerwca 2026 r.

## 25 maja 2026 r.

- Model `gemini-3.1-flash-lite-preview` został [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl). Zamiast niej używaj [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl).

## 19 maja 2026 r.

- `gemini-3.5-flash` udostępniliśmy ogólnie dostępną wersję [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl), naszego najinteligentniejszego modelu, który zapewnia stałą, przełomową wydajność w zadaniach agentowych i związanych z kodowaniem. Jest to teraz model, na którym opiera się `gemini-flash-latest`.
- Udostępniliśmy w publicznej wersji przedpremierowej **zarządzane agenty w Gemini API**. Dzięki temu deweloperzy mogą tworzyć i wdrażać autonomiczne, stanowe agenty, które działają w bezpiecznych, odizolowanych środowiskach piaskownicy Linux hostowanych przez Google. Więcej informacji znajdziesz na stronie [Omówienie agentów](https://ai.google.dev/gemini-api/docs/agents?hl=pl) i w [szybkim wprowadzeniu](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl).
- Udostępniliśmy w publicznej wersji przedpremierowej agenta zarządzanego **agent Antigravity**[`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=pl) do zwykłych obciążeń.
  Agent Antigravity może samodzielnie planować, analizować, pisać i uruchamiać kod, zarządzać plikami oraz przeglądać internet w kontenerze piaskownicy. Zobacz przewodnik [agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl), aby zapoznać się z przykładami kodu i specyfikacjami.

## 7 maja 2026 r.

- Udostępniliśmy `gemini-3.1-flash-lite` wersję ogólnej dostępności (GA) [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl), zoptymalizowaną pod kątem szybkości, skali i opłacalności.
- Ogłoszenie o wycofaniu: model `gemini-3.1-flash-lite-preview` zostanie wycofany 11 maja 2026 r. i [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 25 maja 2026 r.

## 6 maja 2026 r.

- **Nadchodząca zmiana powodująca niezgodność:** schemat żądania i odpowiedzi [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) (`outputs` → `steps`) oraz konfiguracja formatu wyjściowego (`response_format`) ulegają zmianie. Nowy schemat stanie się domyślny **26 maja**, a starszy schemat zostanie usunięty **8 czerwca**.
  Szczegółowe informacje znajdziesz w [przewodniku po migracji](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pl).

## 5 maja 2026 r.

- Zaktualizowano **wyszukiwanie plików**, aby obsługiwało wyszukiwanie wielomodalne. Możesz teraz natywnie osadzać obrazy i wyszukiwać je za pomocą modelu `gemini-embedding-2`.
  Metadane umocowania zawierają teraz `media_id` w przypadku cytatów wizualnych i `page_numbers`, które wskazują, gdzie można znaleźć informacje. Więcej informacji znajdziesz w przewodniku po [wyszukiwaniu plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl).

## 4 maja 2026 r.

- Wprowadziliśmy obsługę [webhooków](https://ai.google.dev/gemini-api/docs/webhooks?hl=pl) opartych na zdarzeniach w interfejsie Gemini API, aby zastąpić przepływy pracy związane z odpytywaniem w przypadku interfejsu Batch API i operacji długotrwałych.

## 30 kwietnia 2026 r.

- Model `gemini-robotics-er-1.5-preview` został [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl). Zamiast niej używaj [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=pl).

## 22 kwietnia 2026 r.

- Udostępniliśmy `gemini-embedding-2` w ramach ogólnej dostępności. Więcej informacji znajdziesz na stronie [Osadzanie](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl).

## 21 kwietnia 2026 r.

- Wydaliśmy nowe wersje agenta [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) ze wspólnym planowaniem, obsługą wizualizacji, integracją z serwerem MCP i wyszukiwaniem plików:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=pl): zaprojektowany z myślą o szybkości i wydajności, idealny do przesyłania strumieniowego z powrotem do interfejsu klienta.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=pl): maksymalna kompleksowość w zakresie automatycznego zbierania i syntezy kontekstu.

## 15 kwietnia 2026 r.

- wprowadziliśmy [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pl), nasz ekonomiczny, ekspresyjny i sterowalny model zamiany tekstu na mowę; Więcej informacji znajdziesz w dokumentacji [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).

## 14 kwietnia 2026 r.

- Opublikowaliśmy `gemini-robotics-er-1.6-preview`, nasz zaktualizowany model robotyki.
  Ma teraz nowe funkcje, takie jak odczytywanie instrumentów, ulepszone możliwości rozumowania przestrzennego i fizycznego. Więcej informacji znajdziesz na stronie [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl) i na [blogu](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=pl).
- Ogłoszenie o wycofaniu: model `gemini-robotics-er-1.5-preview` zostanie [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 30 kwietnia 2026 r. o godzinie 9:00 czasu PST.

## 2 kwietnia 2026 r.

- Wprowadziliśmy `gemma-4-26b-a4b-it` i `gemma-4-31b-it`, które są dostępne w [AI Studio](https://aistudio.google.com?hl=pl) i za pomocą Gemini API w ramach premiery [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=pl).

## 1 kwietnia 2026 r.

- Wprowadziliśmy nowe poziomy wnioskowania [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl) i [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl), które oferują więcej opcji optymalizacji kosztów i opóźnień.

## 31 marca 2026 r.

- Wprowadziliśmy wersję testową Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=pl), naszego najbardziej opłacalnego modelu do [generowania filmów](https://ai.google.dev/gemini-api/docs/video?hl=pl), który został zaprojektowany z myślą o szybkim wprowadzaniu zmian i tworzeniu aplikacji o dużej skali.
- Model `gemini-2.5-flash-lite-preview-09-2025` został wyłączony. Zamiast tego użyj [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pl).

## 26 marca 2026 r.

- Wydaliśmy [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=pl), najnowszy model audio-to-audio (A2A) przeznaczony do dialogów w czasie rzeczywistym i aplikacji AI opartych na głosie. Aby rozpocząć, zapoznaj się z dokumentacją [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl).

## 25 marca 2026 r.

- Wprowadziliśmy modele do generowania muzyki [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=pl) (30-sekundowe klipy) i [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=pl) (pełne utwory). Oba modele akceptują dane wejściowe w postaci tekstu i obrazu oraz generują wysokiej jakości dźwięk stereo 48 kHz. Szczegółowe informacje i przykłady kodu znajdziesz w przewodniku [Generowanie muzyki](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl).

## 23 marca 2026 r.

- Wprowadziliśmy w AI Studio [plany płatności z przedpłatą i płatnością po wykonaniu usługi](https://ai.google.dev/gemini-api/docs/billing?hl=pl). Może to mieć wpływ na istniejące konta. Więcej informacji znajdziesz w dokumentacji dotyczącej [rozliczeń](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

## 18 marca 2026 r.

- Wprowadziliśmy nową funkcję [Połączenie wbudowanych narzędzi i wywoływania funkcji](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl), która umożliwia korzystanie z wbudowanych narzędzi Gemini wraz z niestandardowymi narzędziami do wywoływania funkcji w ramach jednego wywołania interfejsu API.
- [Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl#supported_models) jest teraz obsługiwane w modelach Gemini 3.

## 16 marca 2026 r.

- Wprowadziliśmy ulepszone [poziomy wykorzystania](https://ai.google.dev/gemini-api/docs/billing?hl=pl#about-billing) i [limity wydatków na koncie rozliczeniowym](https://ai.google.dev/gemini-api/docs/billing?hl=pl#tier-spend-caps), aby zapewnić użytkownikom lepsze wrażenia związane z rozliczeniami.

## 12 marca 2026 r.

- Wprowadziliśmy [limity wydatków na poziomie projektu](https://ai.google.dev/gemini-api/docs/billing?hl=pl#project-spend-caps) w rozliczeniach w AI Studio.

## 10 marca 2026 r.

- Udostępniliśmy `gemini-embedding-2-preview`, nasz pierwszy multimodalny model wektorów dystrybucyjnych.
  Obsługuje dane wejściowe w formie tekstu, obrazu, filmu, dźwięku i pliku PDF, mapując wszystkie typy treści na ujednoliconą przestrzeń wektorów dystrybucyjnych. Więcej informacji znajdziesz w artykule o [wektorach dystrybucyjnych](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl).
- Ogłoszenie o wycofaniu: `gemini-2.5-flash-lite-preview-09-2025` model zostanie [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 31 marca 2026 r.

## 9 marca 2026 r.

- Model Gemini 3 Pro w wersji testowej został [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl). `gemini-3-pro-preview` wskazuje teraz [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl).

## 3 marca 2026 r.

- Udostępniliśmy Gemini 3.1 Flash-Lite Preview, pierwszy model Flash-Lite z serii Gemini 3. Dane techniczne, konkretne aktualizacje i wskazówki dla deweloperów znajdziesz na [stronie modelu](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pl).

## 26 lutego 2026 r.

- Wprowadziliśmy Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=pl), czyli bardzo wydajny model zoptymalizowany pod kątem szybkości i przypadków użycia na dużą skalę.
- Ogłoszenie o wycofaniu: wersja testowa Gemini 3 Pro (`gemini-3-pro-preview`) zostanie [wyłączona](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) 9 marca 2026 r.

## 19 lutego 2026 r.

- Udostepniliśmy [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl), najnowszą wersję z nowej serii Gemini 3.
- Uruchomiliśmy osobny punkt końcowy `gemini-3.1-pro-preview-customtools`, który lepiej ustala priorytety narzędzi niestandardowych w przypadku użytkowników korzystających z kombinacji bash i narzędzi.

## 18 lutego 2026 r.

- Ogłoszenie o wycofaniu: 1 czerwca 2026 r. [wyłączymy](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) te modele:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 lutego 2026 r.

- Te modele zostały [wyłączone](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 stycznia 2026 r.

- Wprowadziliśmy obsługę narzędzia Korzystanie z komputera w `gemini-3-pro-preview` i `gemini-3-flash-preview`.

## 21 stycznia 2026 r.

- Zmieniono pseudonimy `latest`:

  - `gemini-pro-latest` przełączył(a) się na `gemini-3-pro-preview`
  - `gemini-flash-latest` przełączył(a) się na `gemini-3-flash-preview`

## 15 stycznia 2026 r.

- Ogłoszenie o wycofaniu: 17 lutego 2026 r. [wyłączymy](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl) te modele:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Model `gemini-2.5-flash-image-preview` został wyłączony.

## 14 stycznia 2026 r.

- Model `text-embedding-004` został [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl).

## 13 stycznia 2026 r.

- Dodaliśmy rozdzielczość wyjściową 4K w [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl) i rozszerzyliśmy obsługę filmów w orientacji pionowej we wszystkich rozdzielczościach.

## 12 stycznia 2026 r.

- Udostępniono funkcję cyklu życia modelu. Niektóre modele będą teraz określać
  etap cyklu życia i harmonogram wycofania. Więcej informacji znajdziesz w tych zasobach:

  - [Etapy modelu](https://ai.google.dev/api/generate-content?hl=pl#ModelStatus)

## 8 stycznia 2026 r.

- Wprowadziliśmy obsługę zasobników Cloud Storage oraz dowolnych publicznych i prywatnych adresów URL z podpisem wstępnym bazy danych jako źródła danych wejściowych dla interfejsu Gemini API. Zwiększyliśmy też limit rozmiaru pliku z 20 MB do 100 MB. Więcej informacji znajdziesz w [przewodniku po metodach przesyłania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

## 19 grudnia 2025 r.

- Wprowadziliśmy zmianę powodującą niezgodność w interfejsie Interactions API w wersji 1 beta. Nazwa pola `total_reasoning_tokens` została zmieniona na `total_thought_tokens`, aby lepiej pasowała do koncepcji „myśli” w modelach myślących.

## 17 grudnia 2025 r.

- Wprowadziliśmy Gemini 3 Flash Preview (`gemini-3-flash-preview`), który zapewnia szybkie działanie na najwyższym poziomie, dorównujące większym modelom, za ułamek ich ceny. Dzięki ulepszonemu rozumowaniu wizualnemu i przestrzennemu oraz możliwościom kodowania agentowego. Przeczytaj dokumentację dotyczącą niektórych nowych funkcji, takich jak:

  - [Odpowiedzi funkcji multimodalnych](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#multimodal)
  - [Wykonywanie kodu z obrazami](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl#images)

## 12 grudnia 2025 r.

- Wprowadziliśmy `gemini-2.5-flash-native-audio-preview-12-2025`, nowy natywny model audio dla interfejsu Live API. Ta aktualizacja zwiększa możliwości modelu w zakresie obsługi złożonych przepływów pracy. Więcej informacji znajdziesz w [przewodniku po interfejsie Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl) i w artykule o [natywnej obsłudze dźwięku w Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=pl).

## 11 grudnia 2025 r.

- Udostępniliśmy interfejs Interactions API. Ten interfejs API udostępnia ujednolicony interfejs
  do korzystania z modeli i agentów Gemini. Więcej informacji znajdziesz w przewodniku po [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).
- Uruchomiliśmy agenta Gemini Deep Research w wersji testowej. Może ona samodzielnie planować, wykonywać i syntetyzować wyniki wieloetapowych zadań badawczych. Szczegółowe informacje znajdziesz w przewodniku po [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).

## 10 grudnia 2025 r.

- Wprowadziliśmy ulepszenia w naszych [modelach zamiany tekstu na mowę](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl), Gemini 2.5 Flash TTS w wersji testowej (zoptymalizowany pod kątem niskiego opóźnienia) i Gemini 2.5 Pro TTS w wersji testowej (zoptymalizowany pod kątem jakości), w tym ulepszoną ekspresję, precyzyjne tempo i płynne dialogi.

## 9 grudnia 2025 r.

- Te modele Gemini Live API zostały wyłączone:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 grudnia 2025 r.

- Naliczanie opłat za Gemini 3 w przypadku [powiązania ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) rozpocznie się 5 stycznia 2026 r.

## 4 grudnia 2025 r.

- Ogłoszenie o wycofaniu: model `gemini-2.5-flash-image-preview` zostanie wyłączony 15 stycznia 2026 r.

## 3 grudnia 2025 r.

- Ogłoszenie o wycofaniu: model `text-embedding-004` zostanie wyłączony 14 stycznia 2026 r.

## 20 listopada 2025 r.

- Udostępniliśmy Gemini 3 Pro Image Preview, `gemini-3-pro-image-preview`, czyli kolejną wersję modelu Nano Banana. Więcej informacji znajdziesz na stronie [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

## 18 listopada 2025 r.

- Uruchomiliśmy pierwszy model z serii Gemini 3, `gemini-3-pro-preview`, który jest naszym najnowocześniejszym modelem do rozumowania i rozpoznawania multimodalnego z zaawansowanymi funkcjami agentowymi i kodowania.

  Oprócz ulepszeń w zakresie inteligencji i wydajności Gemini 3 Pro Preview wprowadza nowe funkcje dotyczące:

  - [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl)
  - [Podpisy myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl)
  - [Poziomy rozumowania](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#thinking-levels)

  Przeczytaj [przewodnik dla programistów dotyczący Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=pl), aby dowiedzieć się więcej o migracji, nowych funkcjach i specyfikacjach.

## 11 listopada 2025 r.

- Ogłoszenie o wycofaniu: te modele zostaną wyłączone:

  - 12 listopada:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 listopada:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 listopada 2025 r.

- Ten model zostanie wyłączony:

  - `imagen-3.0-generate-002`

  Zamiast tego użyj [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=pl#imagen-4). Więcej informacji znajdziesz w [tabeli wycofanych funkcji Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl).

## 6 listopada 2025 r.

- Udostępniliśmy interfejs File Search API w publicznej wersji przedpremierowej, dzięki czemu deweloperzy mogą opierać odpowiedzi na własnych danych. Więcej informacji znajdziesz na nowej stronie [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl).

## 4 listopada 2025 r.

- W przypadku [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) liczba tokenów wejściowych dla obrazów została zmniejszona z 1290 do 258, co obniża koszt edycji obrazów.
- Ogłoszenie o wycofaniu: te modele zostaną wyłączone:

  - 18 listopada:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 grudnia:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 grudnia:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 października 2025 r.

- Uruchomiliśmy nowe narzędzie do [logowania i zbiorów danych](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl) dla interfejsu Gemini API.

## 20 października 2025 r.

- Te modele Gemini Live API zostały wyłączone:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Zamiast tego możesz użyć `gemini-2.5-flash-native-audio-preview-09-2025`.
- Ogłoszenie o wycofaniu: 9 grudnia 2025 r. wyłączymy `gemini-2.0-flash-live-001` i `gemini-live-2.5-flash-preview`.

## 17 października 2025 r.

- **Powiązanie ze źródłami informacji przy użyciu Map Google** jest teraz ogólnie dostępne. Więcej informacji znajdziesz w dokumentacji [powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl).

## 15 października 2025 r.

- Udostępniliśmy modele [Veo 3.1 i 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=pl#veo-3.1) w publicznej wersji przedpremierowej z nowymi funkcjami, takimi jak:

  - Przedłużanie filmów utworzonych przez Veo.
  - odwoływać się do maksymalnie 3 obrazów, aby wygenerować film;
  - dostarczanie obrazów pierwszej i ostatniej klatki do generowania filmów;

  Wprowadziliśmy też więcej opcji długości filmów wyjściowych w przypadku modelu Veo 3: 4, 6 i 8 sekund.
- Ogłoszenie o wycofaniu: 12 listopada 2025 r. wyłączymy `veo-3.0-generate-preview` i `veo-3.0-fast-generate-preview`.

## 7 października 2025 r.

- Udostępniliśmy [wersję testową Gemini 2.5 do użytku na komputerach](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

## 2 października 2025 r.

- Wprowadziliśmy ogólną dostępność Gemini 2.5 Flash Image: [generowanie obrazów za pomocą Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)

## 29 września 2025 r.

- Te modele Gemini 1.5 zostały wyłączone:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 września 2025 r.

- Opublikowaliśmy model Gemini Robotics ER 1.5 w wersji testowej. Aby dowiedzieć się, jak używać modelu w aplikacji robotycznej, zapoznaj się z [omówieniem robotyki](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl).
- Udostępniliśmy te modele w wersji testowej:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Więcej informacji znajdziesz na stronie [Modele](https://ai.google.dev/gemini-api/docs/models?hl=pl).

## 23 września 2025 r.

- Wprowadziliśmy `gemini-2.5-flash-native-audio-preview-09-2025`, nowy natywny model audio dla interfejsu Live API z ulepszonym wywoływaniem funkcji i obsługą odcinania mowy. Więcej informacji znajdziesz w [przewodniku po interfejsie Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl) i w artykule [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-native-audio).

## 16 września 2025 r.

- Ogłoszenie o wycofaniu: w październiku 2025 r. wyłączymy te modele:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Szczegółowe informacje o najnowszym modelu wektorów dystrybucyjnych znajdziesz na stronie [Wektory dystrybucyjne](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl).

## 10 września 2025 r.

- Udostępniliśmy obsługę [modelu wektorów dystrybucyjnych w interfejsie Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl#batch-embedding) i dodaliśmy interfejs Batch API do [biblioteki zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl#batch), aby jeszcze bardziej ułatwić rozpoczęcie korzystania z zapytań zbiorczych.

## 9 września 2025 r.

- Udostępniliśmy modele Veo 3 i Veo 3 Fast w wersji GA z niższymi cenami i nowymi opcjami formatu obrazu, rozdzielczości i seeding. Więcej informacji znajdziesz w [dokumentacji Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl#model-features).

## 26 sierpnia 2025 r.

- Udostępniliśmy [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-image-preview), nasz najnowszy natywny model do generowania obrazów.

## 18 sierpnia 2025 r.

- Udostępniliśmy ogólnie [narzędzie do kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), które umożliwia podawanie adresów URL jako dodatkowego kontekstu w promptach. Za tydzień wycofamy obsługę kontekstu adresu URL w przypadku modelu `gemini-2.0-flash` (dostępnego w wersji eksperymentalnej).

## 14 sierpnia 2025 r.

- Udostępniliśmy modele Imagen 4 Ultra, Standard i Fast w wersji ogólnodostępnej (GA). Więcej informacji znajdziesz na stronie [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pl).

## 7 sierpnia 2025 r.

- Ustawienie `allow_adult` w generowaniu filmów z obrazów jest już dostępne w regionach z ograniczeniami. Szczegółowe informacje znajdziesz na stronie [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=pl#veo-model-parameters).

## 31 lipca 2025 r.

- Udostępniliśmy generowanie filmów na podstawie obrazów za pomocą modelu Veo 3 w wersji testowej.
- Udostępniliśmy model Veo 3 Fast w wersji testowej.
- Więcej informacji o Veo 3 znajdziesz na stronie [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl).

## 22 lipca 2025 r.

- Wprowadziliśmy `gemini-2.5-flash-lite`, nasz szybki, niedrogi i wydajny model Gemini 2.5. Więcej informacji znajdziesz w artykule [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-lite).

## July 17, 2025

- Wprowadziliśmy `veo-3.0-generate-preview`, najnowszą aktualizację Veo, która umożliwia generowanie filmów z dźwiękiem. Więcej informacji o Veo 3 znajdziesz na stronie [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- Zwiększone limity liczby żądań dla modeli Imagen 4 Standard i Ultra. Więcej informacji znajdziesz na stronie [Limity żądań](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl).

## 14 lipca 2025 r.

- Opublikowaliśmy `gemini-embedding-001`, wersję stabilną naszego modelu wektora dystrybucyjnego tekstu. Więcej informacji znajdziesz w artykule o [wektorach dystrybucyjnych](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl). Model `gemini-embedding-exp-03-07` zostanie wycofany 14 sierpnia 2025 r.

## 7 lipca 2025 r.

- Udostępniliśmy tryb wsadowy interfejsu Gemini API. Grupuj żądania i wysyłaj je do przetwarzania asynchronicznego. Więcej informacji znajdziesz w artykule [Tryb wsadowy](https://ai.google.dev/gemini-api/docs/batch-mode?hl=pl).

## 26 czerwca 2025 r.

- Modele w wersji testowej `gemini-2.5-pro-preview-05-06` i `gemini-2.5-pro-preview-03-25` przekierowują teraz do najnowszej wersji stabilnej `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` jest wyłączony.

## 24 czerwca 2025 r.

- Udostępniliśmy modele Imagen 4 Ultra i Standard w wersji testowej. Więcej informacji znajdziesz na stronie [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

## 17 czerwca 2025 r.

- Udostępniliśmy `gemini-2.5-pro`, wersję stabilną naszego najpotężniejszego modelu, teraz z adaptacyjnym myśleniem. Więcej informacji znajdziesz w sekcjach [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-pro) i [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl). `gemini-2.5-pro-preview-05-06`
  zostanie przekierowana na stronę `gemini-2.5-pro` 26 czerwca 2025 r.
- Udostępniliśmy `gemini-2.5-flash`, nasz pierwszy stabilny model 2.5 Flash. Więcej informacji znajdziesz w artykule o [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` zostanie wycofana 15 lipca 2025 r.
- W `gemini-2.5-flash-lite-preview-06-17` udostępniliśmy Gemini 2.5 – niedrogi i wydajny model. Więcej informacji znajdziesz w artykule [Gemini 2.5 Flash-Lite (wersja testowa)](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-lite).

## 5 czerwca 2025 r.

- Udostępniliśmy `gemini-2.5-pro-preview-06-05`, nową wersję naszego najpotężniejszego modelu, która teraz ma funkcję adaptacyjnego myślenia. Więcej informacji znajdziesz w [Gemini 2.5 Pro Preview](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-pro-preview-06-05) i w [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).
  26 czerwca 2025 r. `gemini-2.5-pro-preview-05-06` zostanie przekierowany na stronę `gemini-2.5-pro`.

## 27 maja 2025 r.

- Ostatni dostępny model dostrajania, Gemini 1.5 Flash 001, został wyłączony.
  Dostrajanie nie jest już obsługiwane w przypadku żadnych modeli.
  Zobacz [Dostrajanie za pomocą interfejsu Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pl).

## 20 maja 2025 r.

**Aktualizacje interfejsu API:**

- Wprowadziliśmy obsługę [niestandardowego wstępnego przetwarzania filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#customize-video-processing) za pomocą interwałów przycinania i konfigurowalnego próbkowania liczby klatek.
- Wprowadziliśmy możliwość korzystania z wielu narzędzi, która umożliwia konfigurowanie [wykonania kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) i [powiązania ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl) w tym samym żądaniu `generateContent`.
- Wprowadziliśmy obsługę [asynchronicznych wywołań funkcji](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl#async-function-calling) w interfejsie Live API.
- Uruchomiliśmy eksperymentalne [narzędzie do kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), które umożliwia podawanie adresów URL jako dodatkowego kontekstu w promptach.

**Aktualizacje modeli:**

- Udostępniliśmy model `gemini-2.5-flash-preview-05-20`, czyli model Gemini w [wersji testowej](https://ai.google.dev/gemini-api/docs/models?hl=pl#model-versions) zoptymalizowany pod kątem stosunku ceny do wydajności i adaptacyjnego myślenia. Więcej informacji znajdziesz w sekcjach [Wersja testowa Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-preview) i [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).
- Udostępniliśmy modele [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-pro-preview-tts) i [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-preview-tts), które mogą [generować mowę](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl) z jednym lub dwoma rozmówcami.
- Wydaliśmy model `lyria-realtime-exp`, który [generuje muzykę](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl) w czasie rzeczywistym.
- Udostępniliśmy modele `gemini-2.5-flash-preview-native-audio-dialog` i `gemini-2.5-flash-exp-native-audio-thinking-dialog`, czyli nowe modele Gemini dla interfejsu Live API z funkcją natywnego wyjścia audio. Więcej informacji znajdziesz w [przewodniku po interfejsie Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl#native-audio-output) i [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-native-audio).
- Wydaliśmy wersję testową `gemma-3n-e4b-it`, która jest dostępna w [AI Studio](https://aistudio.google.com?hl=pl) i przez interfejs Gemini API w ramach premiery [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=pl).

## 7 maja 2025 r.

- Udostępniliśmy `gemini-2.0-flash-preview-image-generation`, model w wersji testowej do generowania i edytowania obrazów. Więcej informacji znajdziesz w sekcjach [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) i [Generowanie obrazów w Gemini 2.0 Flash Image (wersja testowa)](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.0-flash-preview-image-generation).

## 6 maja 2025 r.

- Udostępniliśmy `gemini-2.5-pro-preview-05-06`, nową wersję naszego najbardziej zaawansowanego modelu, z ulepszeniami w zakresie kodu i wywoływania funkcji. `gemini-2.5-pro-preview-03-25` będzie automatycznie wskazywać nową wersję modelu.

## 17 kwietnia 2025 r.

- Udostępniliśmy `gemini-2.5-flash-preview-04-17`, czyli model Gemini w [wersji testowej](https://ai.google.dev/gemini-api/docs/models?hl=pl#model-versions) zoptymalizowany pod kątem stosunku ceny do wydajności i adaptacyjnego myślenia. Więcej informacji znajdziesz w artykułach [Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-flash-preview) i [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).

## 16 kwietnia 2025 r.

- Wprowadziliśmy zapisywanie kontekstu w pamięci podręcznej w przypadku [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.0-flash).

## 9 kwietnia 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `veo-2.0-generate-001`, ogólnie dostępny model do generowania filmów z tekstu i obrazów, który może tworzyć szczegółowe i artystycznie dopracowane filmy. Więcej informacji znajdziesz w [dokumentacji Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- `gemini-2.0-flash-live-001` udostępniliśmy publiczną wersję testową modelu [Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) z włączonymi płatnościami.

  - **Ulepszone zarządzanie sesjami i niezawodność**

    - **Wznawianie sesji:** utrzymywanie sesji w przypadku tymczasowych przerw w działaniu sieci. Interfejs API obsługuje teraz przechowywanie stanu sesji po stronie serwera (przez maksymalnie 24 godziny) i udostępnia uchwyty (session\_resumption) do ponownego nawiązywania połączenia i wznawiania sesji od miejsca, w którym została przerwana.
    - **Dłuższe sesje dzięki kompresji kontekstu:** umożliwia dłuższe interakcje, które wykraczają poza wcześniejsze limity czasowe. Skonfiguruj kompresję okna kontekstu za pomocą mechanizmu okna przesuwnego, aby automatycznie zarządzać długością kontekstu i zapobiegać nagłemu zakończeniu działania z powodu limitów kontekstu.
    - **Powiadomienie o grzecznym rozłączeniu:** otrzymuj komunikat z serwera `GoAway` informujący o tym, kiedy połączenie zostanie zamknięte, co umożliwi grzeczne zakończenie połączenia.
  - **Większa kontrola nad dynamiką interakcji**
  - **Konfigurowalne wykrywanie aktywności głosowej (VAD):** wybierz poziomy czułości lub całkowicie wyłącz automatyczne wykrywanie aktywności głosowej i używaj nowych zdarzeń klienta (`activityStart`, `activityEnd`) do ręcznego sterowania turami.
  - **Konfigurowalna obsługa przerywania:** zdecyduj, czy dane wejściowe użytkownika powinny przerywać odpowiedź modelu.
  - **Konfigurowane pokrycie tur:** możesz wybrać, czy interfejs API ma przetwarzać wszystkie dane wejściowe audio i wideo w sposób ciągły, czy tylko wtedy, gdy wykryje, że użytkownik końcowy mówi.
  - **Konfigurowalna rozdzielczość multimediów:** optymalizuj pod kątem jakości lub wykorzystania tokenów, wybierając rozdzielczość multimediów wejściowych.
  - **Bogatsze dane wyjściowe i funkcje**
  - **Rozszerzone opcje głosu i języka:** wybierz jeden z 2 nowych głosów i 30 nowych języków wyjścia audio. Język wyjściowy można teraz skonfigurować w `speechConfig`.
  - **Strumieniowanie tekstu:** otrzymywanie odpowiedzi tekstowych w miarę ich generowania, co umożliwia szybsze wyświetlanie ich użytkownikowi.
  - **Raportowanie wykorzystania tokenów:** uzyskaj informacje o wykorzystaniu dzięki szczegółowej liczbie tokenów podanej w polu `usageMetadata` wiadomości serwera, z podziałem na modalność i fazy promptu lub odpowiedzi.

## 4 kwietnia 2025 r.

- Wprowadziliśmy `gemini-2.5-pro-preview-03-25` publiczną wersję przedpremierową Gemini 2.5 Pro z włączonymi rozliczeniami. Możesz nadal korzystać z usługi `gemini-2.5-pro-exp-03-25` w ramach poziomu bezpłatnego.

## 25 marca 2025 r.

- Udostępniliśmy `gemini-2.5-pro-exp-03-25`, publiczny eksperymentalny model Gemini z trybem myślenia zawsze domyślnie włączonym.
  Więcej informacji znajdziesz w artykule o [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-2.5-pro-preview-03-25).

## 12 marca 2025 r.

**Aktualizacje modeli:**

- Wprowadziliśmy eksperymentalny model [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#gemini), który umożliwia generowanie i edytowanie obrazów.
- Model `gemma-3-27b-it` został udostępniony w [AI Studio](https://aistudio.google.com?hl=pl) i przez Gemini API w ramach premiery [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=pl).

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [adresów URL YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=pl#youtube) jako źródła multimediów.
- Dodaliśmy obsługę [filmów w tekście](https://ai.google.dev/gemini-api/docs/vision?hl=pl#inline-video) o rozmiarze mniejszym niż 20 MB.

## 11 marca 2025 r.

**Aktualizacje pakietu SDK:**

- Udostępniliśmy publiczną wersję przedpremierową [pakietu Google Gen AI SDK dla TypeScript i JavaScriptu](https://googleapis.github.io/js-genai).

## 7 marca 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-embedding-exp-03-07` [eksperymentalny](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=pl) model osadzania oparty na Gemini w publicznej wersji przedpremierowej.

## 28 lutego 2025 r.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [wyszukiwarki jako narzędzia](https://ai.google.dev/gemini-api/docs/grounding?hl=pl) do `gemini-2.0-pro-exp-02-05`, modelu eksperymentalnego opartego na Gemini 2.0 Pro.

## 25 lutego 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-2.0-flash-lite` wersję [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-2.0-flash-lite) w ogólnej dostępności (GA), która jest zoptymalizowana pod kątem szybkości, skali i opłacalności.

## 19 lutego 2025 r.

**Aktualizacje AI Studio:**

- Dodaliśmy obsługę [kolejnych regionów](https://ai.google.dev/gemini-api/docs/available-regions?hl=pl) (Kosowo, Grenlandia i Wyspy Owcze).

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [kolejnych regionów](https://ai.google.dev/gemini-api/docs/available-regions?hl=pl) (Kosowo, Grenlandia i Wyspy Owcze).

## 18 lutego 2025 r.

**Aktualizacje modeli:**

- Model Gemini 1.0 Pro nie jest już obsługiwany. Listę obsługiwanych modeli znajdziesz w artykule o [modelach Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

## 11 lutego 2025 r.

**Aktualizacje interfejsu API:**

- Aktualizacje dotyczące [zgodności z bibliotekami OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

## 6 lutego 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `imagen-3.0-generate-002` ogólnodostępną wersję [Imagen 3 w interfejsie Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=pl).

**Aktualizacje pakietu SDK:**

- Udostępniliśmy [pakiet SDK Gen AI od Google w wersji na Javę](https://github.com/googleapis/java-genai) w ramach publicznej wersji przedpremierowej.

## 5 lutego 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-2.0-flash-001` ogólnodostępną wersję [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-2.0-flash), która obsługuje tylko tekstowe dane wyjściowe.
- Wprowadziliśmy `gemini-2.0-pro-exp-02-05` [eksperymentalną](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=pl) wersję testową Gemini 2.0 Pro dostępną publicznie.
- Udostępniliśmy `gemini-2.0-flash-lite-preview-02-05`, eksperymentalny [model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-2.0-flash-lite) w publicznej wersji przedpremierowej zoptymalizowany pod kątem efektywności kosztowej.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [plików wejściowych i wykresów wyjściowych](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl#input-output) w ramach wykonywania kodu.

**Aktualizacje pakietu SDK:**

- Udostępniliśmy ogólnie dostępny [pakiet SDK Gen AI od Google dla Pythona](https://googleapis.github.io/python-genai/).

## 21 stycznia 2025 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-2.0-flash-thinking-exp-01-21`, najnowszą wersję testową modelu, na którym opiera się [model Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).

## 19 grudnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy tryb modelu Gemini 2.0 Flash Thinking w publicznej wersji przedpremierowej. Tryb myślący to model obliczeniowy czasu testu, który pozwala zobaczyć proces myślowy modelu podczas generowania odpowiedzi i zapewnia odpowiedzi o lepszych możliwościach wnioskowania.

  Więcej informacji o trybie Gemini 2.0 Flash Thinking znajdziesz na naszej [stronie z omówieniem](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=pl).

## 11 grudnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy model [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-2.0-flash) w publicznej wersji przedpremierowej. Częściowa lista funkcji Gemini 2.0 Flash Experimental obejmuje:
  - 2 razy szybszy niż Gemini 1.5 Pro
  - Strumieniowanie dwukierunkowe za pomocą interfejsu Live API
  - Generowanie odpowiedzi multimodalnych w postaci tekstu, obrazów i mowy
  - Korzystanie z wbudowanych narzędzi z wielokrotnym wnioskowaniem, aby używać funkcji takich jak wykonywanie kodu, wyszukiwanie, wywoływanie funkcji itp.

Więcej informacji o Gemini 2.0 Flash znajdziesz na [stronie z omówieniem](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=pl).

## 21 listopada 2024 r.

**Aktualizacje modeli:**

- Wprowadziliśmy `gemini-exp-1121`, jeszcze bardziej zaawansowany eksperymentalny model interfejsu Gemini API.

**Aktualizacje modeli:**

- Zaktualizowano aliasy modeli `gemini-1.5-flash-latest` i `gemini-1.5-flash`, aby używały modelu `gemini-1.5-flash-002`.
  - Zmiana parametru `top_k`: model `gemini-1.5-flash-002` obsługuje wartości `top_k` od 1 do 41 (wyłącznie).
    Wartości większe niż 40 zostaną zmienione na 40.

## 14 listopada 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-exp-1114`, zaawansowany eksperymentalny model Gemini API.

## 8 listopada 2024 r.

**Aktualizacje interfejsu API:**

- Dodano [obsługę Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=pl) w bibliotekach OpenAI i interfejsie REST API.

## 31 października 2024 r.

**Aktualizacje interfejsu API:**

- Dodaliśmy [obsługę powiązania ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl).

## 3 października 2024 r.

**Aktualizacje modeli:**

- Wprowadziliśmy `gemini-1.5-flash-8b-001`, stabilną wersję naszego najmniejszego modelu API Gemini.

## 24 września 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-1.5-pro-002` i `gemini-1.5-flash-002`, dwie nowe stabilne wersje modeli Gemini 1.5 Pro i 1.5 Flash, w ramach ogólnej dostępności.
- Zaktualizowano kod modelu `gemini-1.5-pro-latest`, aby używał `gemini-1.5-pro-002`, oraz kod modelu `gemini-1.5-flash-latest`, aby używał `gemini-1.5-flash-002`.
- Wydano `gemini-1.5-flash-8b-exp-0924`, aby zastąpić `gemini-1.5-flash-8b-exp-0827`.
- Udostępniliśmy [filtr bezpieczeństwa dotyczący uczciwości obywatelskiej](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl#safety-filters) w Gemini API i AI Studio.
- Wprowadziliśmy obsługę 2 nowych parametrów dla Gemini 1.5 Pro i 1.5 Flash w Pythonie i NodeJS: [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=pl#FIELDS.frequency_penalty) i [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=pl#FIELDS.presence_penalty).

## 19 września 2024 r.

**Aktualizacje AI Studio:**

- Dodaliśmy przyciski „Lubię” i „Nie lubię” do odpowiedzi modelu, aby umożliwić użytkownikom przekazywanie opinii o jakości odpowiedzi.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę środków Google Cloud, które można teraz wykorzystać na korzystanie z Gemini API.

## 17 września 2024 r.

**Aktualizacje AI Studio:**

- Dodaliśmy przycisk **Otwórz w Colab**, który eksportuje prompta i kod do jego uruchomienia do notatnika Colab. Ta funkcja nie obsługuje jeszcze promptów z narzędziami (tryb JSON, wywoływanie funkcji lub wykonywanie kodu).

## 13 września 2024 r.

**Aktualizacje AI Studio:**

- Dodaliśmy obsługę trybu porównywania, który umożliwia porównywanie odpowiedzi z różnych modeli i promptów, aby znaleźć najlepsze rozwiązanie dla Twojego zastosowania.

## 30 sierpnia 2024 r.

**Aktualizacje modeli:**

- Gemini 1.5 Flash obsługuje [podawanie schematu JSON za pomocą konfiguracji modelu](https://ai.google.dev/gemini-api/docs/json-mode?hl=pl#supply-schema-in-config).

## 27 sierpnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy te [modele eksperymentalne](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=pl):
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 sierpnia 2024 r.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [przetwarzania plików PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).

## 5 sierpnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy obsługę dostrajania Gemini 1.5 Flash.

## 1 sierpnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy `gemini-1.5-pro-exp-0801`, nową wersję eksperymentalną modelu [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-1.5-pro).

## 12 lipca 2024 r.

**Aktualizacje modeli:**

- Usunięcie obsługi Gemini 1.0 Pro Vision z usług i narzędzi AI od Google.

## 27 czerwca 2024 r.

**Aktualizacje modeli:**

- Ogólna dostępność okna kontekstu o 2 milionach tokenów w Gemini 1.5 Pro.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [wykonywania kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl).

## 18 czerwca 2024 r.

**Aktualizacje interfejsu API:**

- Dodaliśmy obsługę [pamięci podręcznej kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl).

## 12 czerwca 2024 r.

**Aktualizacje modeli:**

- Wycofanie modelu Gemini 1.0 Pro Vision.

## 23 maja 2024 r.

**Aktualizacje modeli:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-1.5-pro) (`gemini-1.5-pro-001`) jest ogólnie dostępny.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-1.5-flash) (`gemini-1.5-flash-001`) jest ogólnie dostępny.

## 14 maja 2024 r.

**Aktualizacje interfejsu API:**

- Wprowadziliśmy okno kontekstu o wielkości 2 mln tokenów w przypadku Gemini 1.5 Pro (lista oczekujących).
- Wprowadziliśmy [płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl) za Gemini 1.0 Pro w systemie „płatność według wykorzystania”. Gemini 1.5 Pro i Gemini 1.5 Flash – już wkrótce.
- Wprowadziliśmy wyższe limity liczby żądań dla nadchodzącego płatnego poziomu Gemini 1.5 Pro.
- Dodaliśmy do interfejsu [File API](https://ai.google.dev/api/rest/v1beta/files?hl=pl) wbudowaną obsługę filmów.
- Dodaliśmy obsługę zwykłego tekstu w [File API](https://ai.google.dev/api/rest/v1beta/files?hl=pl).
- Dodaliśmy obsługę równoległego wywoływania funkcji, które zwraca więcej niż jedno wywołanie naraz.

## 10 maja 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-1.5-flash) (`gemini-1.5-flash-latest`) w wersji testowej.

## 9 kwietnia 2024 r.

**Aktualizacje modeli:**

- Udostępniliśmy [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#gemini-1.5-pro) (`gemini-1.5-pro-latest`) w wersji testowej.
- Udostępniliśmy nowy model wektorów dystrybucyjnych tekstu `text-embeddings-004`, który obsługuje rozmiary [elastycznych wektorów dystrybucyjnych](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl#elastic-embedding) poniżej 768.

**Aktualizacje interfejsu API:**

- Udostępniliśmy interfejs [File API](https://ai.google.dev/api/rest/v1beta/files?hl=pl) do tymczasowego przechowywania plików multimedialnych na potrzeby promptów.
- Dodaliśmy obsługę promptów z danymi tekstowymi, obrazami i dźwiękami, czyli promptów *multimodalnych*. Więcej informacji znajdziesz w artykule [Prompting with media](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=pl) (Prompty z multimediami).
- Udostępniliśmy [instrukcje systemowe](https://ai.google.dev/gemini-api/docs/system-instructions?hl=pl) w wersji beta.
- Dodaliśmy [tryb wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#function_calling_mode), który określa sposób wykonywania wywołań funkcji.
- Dodaliśmy obsługę opcji konfiguracji `response_mime_type`, która umożliwia żądanie odpowiedzi w [formacie JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=pl#json).

## 19 marca 2024 r.

**Aktualizacje modeli:**

- Dodaliśmy obsługę [dostrajania Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) w Google AI Studio lub za pomocą interfejsu Gemini API.

## 13 grudnia 2023 r.

**Aktualizacje modeli:**

- gemini-pro: nowy model tekstowy do wielu różnych zadań. Zapewnia równowagę między możliwościami a wydajnością.
- gemini-pro-vision: nowy model multimodalny do wielu różnych zadań.
  Równoważy możliwości i wydajność.
- embedding-001: nowy model wektorów dystrybucyjnych.
- aqa: nowy, specjalnie dostrojony model, który jest trenowany pod kątem odpowiadania na pytania
  z użyciem fragmentów tekstu jako podstawy generowanych odpowiedzi;

Więcej informacji znajdziesz w artykule o [modelach Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

**Aktualizacje wersji interfejsu API:**

- v1: stabilny kanał interfejsu API.
- v1beta: wersja beta. Ten kanał zawiera funkcje, które mogą być w trakcie opracowywania.

Więcej informacji znajdziesz w [temacie dotyczącym wersji interfejsu API](https://ai.google.dev/gemini-api/docs/api-versions?hl=pl).

**Aktualizacje interfejsu API:**

- `GenerateContent` to jeden ujednolicony punkt końcowy do czatu i tekstu.
- Przesyłanie strumieniowe jest dostępne za pomocą metody `StreamGenerateContent`.
- Możliwości multimodalne: obraz to nowy obsługiwany tryb
- Nowe funkcje w wersji beta:
  - [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
  - Attributed Question Answering (AQA)
- Zaktualizowana liczba kandydatów: modele Gemini zwracają tylko 1 kandydata.
- Różne kategorie SafetySettings i SafetyRating. Więcej informacji znajdziesz w [ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl).
- Dostrajanie modeli Gemini nie jest jeszcze obsługiwane (prace w toku).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-14 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-14 UTC."],[],[]]
