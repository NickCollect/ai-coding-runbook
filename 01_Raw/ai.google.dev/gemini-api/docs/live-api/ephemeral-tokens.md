---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pl
fetched_at: 2026-08-24T02:28:19.099806+00:00
title: "Tokeny tymczasowe \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tokeny tymczasowe

Tokeny tymczasowe to krótkotrwałe tokeny uwierzytelniania, które umożliwiają dostęp do interfejsu Gemini
API przez [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Zostały zaprojektowane tak, aby zwiększać bezpieczeństwo, gdy
łączysz się bezpośrednio z urządzenia użytkownika z interfejsem API (implementacja
[klient-serwer](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach)
). Podobnie jak standardowe klucze interfejsu API tokeny tymczasowe można wyodrębnić z aplikacji po stronie klienta, takich jak przeglądarki internetowe czy aplikacje mobilne. Ponieważ jednak tokeny tymczasowe szybko wygasają i można je ograniczyć, znacznie zmniejszają one zagrożenia bezpieczeństwa w środowisku produkcyjnym. Aby zwiększyć bezpieczeństwo klucza interfejsu API, używaj ich podczas uzyskiwania dostępu do interfejsu Live API bezpośrednio z aplikacji po stronie klienta.

## Jak działają tokeny tymczasowe

Oto ogólny opis działania tokenów tymczasowych:

1. Klient (np. aplikacja internetowa) uwierzytelnia się w backendzie.
2. Backend wysyła żądanie tokena tymczasowego do usługi udostępniania interfejsu Gemini API.
3. Interfejs Gemini API wydaje krótkotrwały token.
4. Backend wysyła token do klienta na potrzeby połączeń WebSocket z interfejsem Live API. Możesz to zrobić, zastępując klucz interfejsu API tokenem tymczasowym.
5. Klient używa tokena tak, jakby był to klucz interfejsu API.

![Omówienie tokenów tymczasowych](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=pl)

Zwiększa to bezpieczeństwo, ponieważ nawet jeśli token zostanie wyodrębniony, będzie krótkotrwały, w przeciwieństwie do długotrwałego klucza interfejsu API wdrożonego po stronie klienta. Ponieważ klient wysyła dane bezpośrednio do Gemini, poprawia to też opóźnienie i eliminuje konieczność przekazywania danych w czasie rzeczywistym przez backendy.

## Tworzenie tokena tymczasowego

Oto uproszczony przykład uzyskiwania tokena tymczasowego z Gemini.
Domyślnie masz 1 minutę na rozpoczęcie nowych sesji interfejsu Live API za pomocą tokena z tego żądania (`newSessionExpireTime`) i 30 minut na wysyłanie wiadomości przez to połączenie (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

Ograniczenia wartości `expireTime`, wartości domyślne i inne specyfikacje pól znajdziesz w [dokumentacji API](https://ai.google.dev/api/live?hl=pl#ephemeral-auth-tokens).
W okresie `expireTime` musisz użyć
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=pl#session-resumption), aby
ponownie nawiązywać połączenie co 10 minut (możesz to zrobić za pomocą tego samego tokena, nawet
jeśli `uses: 1`).

Możesz też zablokować token tymczasowy w przypadku zestawu konfiguracji. Może to być przydatne do dalszego zwiększania bezpieczeństwa aplikacji i przechowywania instrukcji systemowych po stronie serwera.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.1-flash-live-preview",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

Możesz też zablokować podzbiór pól. Więcej informacji znajdziesz w [dokumentacji pakietu SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
.

## Łączenie się z interfejsem Live API za pomocą tokena tymczasowego

Gdy masz token tymczasowy, możesz go używać tak, jakby był to klucz interfejsu API (pamiętaj jednak, że działa on tylko w przypadku interfejsu Live API i tylko w wersji `v1beta` interfejsu API).

Używanie tokenów tymczasowych jest przydatne tylko w przypadku wdrażania aplikacji
które korzystają z implementacji [klient-serwer](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Więcej przykładów znajdziesz w artykule [Pierwsze kroki z interfejsem Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

## Sprawdzone metody

- Ustaw krótki czas wygaśnięcia za pomocą parametru `expire_time`.
- Tokeny wygasają, co wymaga ponownego zainicjowania procesu udostępniania.
- Sprawdź bezpieczne uwierzytelnianie w swoim backendzie. Tokeny tymczasowe będą tak bezpieczne, jak metoda uwierzytelniania backendu.
- Zasadniczo unikaj używania tokenów tymczasowych w przypadku połączeń backendu z Gemini, ponieważ ta ścieżka jest zwykle uważana za bezpieczną.

## Ograniczenia

Tokeny tymczasowe są obecnie zgodne tylko z [interfejsem Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

## Co dalej?

- Więcej informacji znajdziesz w dokumentacji interfejsu Live API [na temat tokenów tymczasowych](https://ai.google.dev/api/live?hl=pl#ephemeral-auth-tokens).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
