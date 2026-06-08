---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=pl
fetched_at: 2026-06-08T05:36:31.449785+00:00
title: "Integracje z\u00a0partnerami i\u00a0bibliotekami \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Integracje z partnerami i bibliotekami

Ten przewodnik zawiera strategie architektoniczne dotyczące tworzenia bibliotek, platform i bram na podstawie interfejsu Gemini API. Opisuje on kompromisy techniczne między używaniem oficjalnych pakietów GenAI SDK, interfejsu Direct API (REST/gRPC) a warstwy zgodności z OpenAI.

Skorzystaj z tego przewodnika, jeśli tworzysz narzędzia dla innych deweloperów, takie jak platformy open source, bramy dla firm lub agregatory SaaS, i musisz zoptymalizować je pod kątem higieny zależności, rozmiaru pakietu lub równości funkcji.

## Na czym polega integracja z partnerem?

Partnerem jest każdy, kto tworzy integrację między interfejsem Gemini API a deweloperami aplikacji dla użytkowników końcowych. Dzielimy partnerów na 4 archetypy. Określenie, do którego z nich najbardziej pasujesz, pomoże Ci wybrać odpowiednią ścieżkę integracji.

#### Platforma ekosystemu

- **Kim jesteś:** opiekunem platformy open source (np. LangChain, LlamaIndex, Spring AI) lub klientów w określonym języku.
- **Twój cel:** szeroka zgodność. Chcesz, aby Twoja biblioteka działała w dowolnym środowisku wybranym przez użytkownika bez powodowania konfliktów.

#### Platforma środowiska wykonawczego i brzegowa

- **Kim jesteś:** dostawcą platform SaaS, bram AI lub infrastruktury w chmurze (np. Vercel, Cloudflare, Zapier), w których kod jest wykonywany w ograniczonych środowiskach.
- **Twój cel:** wydajność. Potrzebujesz niskiego opóźnienia, minimalnego rozmiaru pakietu i szybkiego uruchamiania „na zimno”.

#### Agregator

- **Kim jesteś:** dostawcą platform, serwerów proxy lub wewnętrznych „Model Gardens”, które normalizują dostęp do wielu różnych dostawców LLM (np. OpenAI, Anthropic, Google) w jednym interfejsie.
- **Twój cel:** przenośność i jednolitość.

#### Brama dla firm

- **Kim jesteś:** zespołem ds. inżynierii platform wewnętrznych w dużych firmach, który tworzy „złote ścieżki” dla setek deweloperów wewnętrznych.
- **Twój cel:** standaryzacja, zarządzanie i ujednolicone uwierzytelnianie.

## Krótkie porównanie

**Globalna sprawdzona metoda:** wszyscy partnerzy muszą wysyłać nagłówek [`x-goog-api-client`
header](#client-id) niezależnie od wybranej ścieżki.

| Jeśli jesteś... | Zalecana ścieżka | Najważniejsza zaleta | Najważniejszy kompromis | Sprawdzona metoda |
| --- | --- | --- | --- | --- |
| **Brama dla firm, platforma ekosystemu** | **[Google GenAI SDK](#genai-sdk)** | **Równość i szybkość platformy agentów Gemini Enterprise.** Wbudowana obsługa typów, uwierzytelniania i złożonych funkcji (np. przesyłania plików). Bezproblemowa migracja do Google Cloud. | **Waga zależności.** Zależności przechodnie mogą być złożone i poza Twoją kontrolą. Ograniczone do obsługiwanych języków (Python, Node, Go, Java). | **Blokowanie wersji.** Przypnij wersje pakietu SDK w wewnętrznych obrazach podstawowych, aby zapewnić stabilność w zespołach. |
| **Platforma ekosystemu, platformy brzegowe i agregatory** | **[Direct API](#rest)**  *(REST / gRPC)* | **Brak zależności.** Masz kontrolę nad klientem HTTP i dokładnym rozmiarem pakietu. Pełny dostęp do wszystkich funkcji interfejsu API i modelu. | **Duże obciążenie dewelopera.** Struktury JSON mogą być głęboko zagnieżdżone i wymagać ścisłej ręcznej weryfikacji oraz sprawdzania typów. | **Używanie specyfikacji OpenAPI.** Zautomatyzuj generowanie typów za pomocą naszych oficjalnych specyfikacji zamiast pisać je ręcznie. |
| **Agregator korzystający z pakietów OpenAI SDK, które wymagają tylko przepływów pracy opartych na tekście**  *(Optymalizacja pod kątem zgodności ze starszymi wersjami)* | **[Zgodność z OpenAI](#openai)** | **Natychmiastowa przenośność.** Ponowne używanie istniejącego kodu lub bibliotek zgodnych z OpenAI. | **Ograniczenia funkcji.** Funkcje specyficzne dla modelu (natywny film, buforowanie) mogą być niedostępne. | **Plan migracji.** Użyj go do szybkiej weryfikacji, ale zaplanuj przejście na Direct API, aby korzystać z pełnej funkcjonalności interfejsu API. |

## Integracja z Google GenAI SDK

W przypadku platform implementacja [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=pl)
jest często najprostszą ścieżką, ponieważ wymaga najmniejszej liczby wierszy kodu w obsługiwanych
językach.

W przypadku zespołów ds. platform wewnętrznych głównym produktem jest często „złota ścieżka”, która umożliwia inżynierom produktu szybkie działanie przy jednoczesnym zachowaniu zgodności z zasadami bezpieczeństwa.

**Korzyści:**

- **Ujednolicony interfejs do migracji na platformę agentów Gemini Enterprise:** deweloperzy wewnętrzni często tworzą prototypy za pomocą kluczy interfejsu API (Gemini API) i wdrażają je na platformie agentów Gemini Enterprise (IAM) w celu zapewnienia zgodności z wymaganiami produkcyjnymi. Pakiet SDK abstrahuje od tych różnic w uwierzytelnianiu.
  Podobnie w przypadku platform możesz zaimplementować jedną ścieżkę kodu i obsługiwać 2 grupy użytkowników.
- **Pomocnicy po stronie klienta:** pakiet SDK zawiera idiomatyczne narzędzia, które zmniejszają ilość kodu powtarzalnego w przypadku złożonych zadań.
  - *Przykłady:* bezpośrednia obsługa obiektów obrazów `PIL` w promptach, automatyczne wywoływanie funkcji i kompleksowe typy.
- **Dostęp do funkcji od dnia premiery:** nowe funkcje interfejsu API są dostępne w momencie premiery za pomocą pakietów SDK.
- **Ulepszona obsługa generowania kodu:** lokalna instalacja pakietu SDK udostępnia definicje typów i docstringi asystentom kodowania (np. Cursor, Copilot).
  Ten kontekst zwiększa dokładność generowania kodu w porównaniu z generowaniem surowych żądań REST.

**Kompromis:**

- **Waga i złożoność zależności:** pakiety SDK mają własne zależności, co może zwiększyć rozmiar pakietu i potencjalnie ryzyko związane z łańcuchem dostaw.
- **Wersjonowanie:** nowe funkcje interfejsu API są często przypinane do minimalnych wersji pakietu SDK.
  Aby użytkownicy mogli korzystać z nowych funkcji lub modeli, może być konieczne wysłanie do nich aktualizacji. W niektórych przypadkach może to wymagać zmian w zależnościach przechodnich, które mają wpływ na użytkowników.
- **Limity protokołu:** pakiety SDK obsługują tylko HTTPS w przypadku głównego interfejsu API i WebSocketów (WSS) w przypadku interfejsu Live API. gRPC nie jest obsługiwany w przypadku klientów pakietu SDK wysokiego poziomu.
- **Obsługa języków:** pakiety SDK obsługują *aktualne* wersje języków. Jeśli musisz obsługiwać wersje EOL (np. Python 3.9), musisz utrzymywać rozwidlenie.

**Sprawdzona metoda:**

- **Blokowanie wersji:** przypnij wersję pakietu SDK w wewnętrznych obrazach podstawowych, aby zapewnić stabilność w zespołach.

## Integracja z Direct API

Jeśli rozpowszechniasz bibliotekę wśród tysięcy deweloperów, działasz w ograniczonym środowisku lub tworzysz agregator, który wymaga najnowszych funkcji Gemini, może być konieczne bezpośrednie zintegrowanie się z interfejsem API za pomocą REST lub gRPC.

**Zalety:**

- **Pełny dostęp do funkcji:** w przeciwieństwie do warstwy zgodności z OpenAI bezpośrednie korzystanie z interfejsu API umożliwia korzystanie z funkcji specyficznych dla Gemini, takich jak przesyłanie do interfejsu File API, tworzenie buforowania treści i korzystanie z dwukierunkowego interfejsu Live API.
- **Minimalne zależności:** w środowisku, w którym zależności są wrażliwe ze względu na rozmiar lub koszty audytu. Bezpośrednie korzystanie z interfejsu API za pomocą standardowej biblioteki, takiej jak `fetch`, lub za pomocą otoki, takiej jak `httpx`, zapewnia, że biblioteka pozostanie lekka.
- **Niezależność od języka:** jest to jedyna ścieżka dla języków nieobsługiwanych przez pakiety SDK, takich jak Rust, PHP i Ruby, ponieważ nie ma ograniczeń językowych.
- **Wydajność:** Direct API nie ma narzutu na inicjowanie, co minimalizuje uruchamianie „na zimno” w funkcjach bezserwerowych.

**Kompromis:**

- **Ręczna implementacja platformy agentów Gemini Enterprise:** w przeciwieństwie do pakietu SDK bezpośrednie korzystanie z interfejsu API nie obsługuje automatycznie różnic w uwierzytelnianiu między AI Studio (klucz interfejsu API) a platformą agentów Gemini Enterprise (IAM). Jeśli chcesz obsługiwać oba środowiska, musisz zaimplementować osobne moduły obsługi uwierzytelniania.
- **Brak typów natywnych i pomocników:** nie otrzymujesz uzupełniania kodu ani sprawdzania obiektów żądań w czasie kompilacji, chyba że zaimplementujesz je samodzielnie. Nie ma „pomocników” klienta (np. konwerterów funkcji na schematy), więc musisz samodzielnie napisać tę logikę.

**Sprawdzona metoda**

Udostępniamy specyfikację czytelną dla maszyn, której możesz użyć do wygenerowania definicji typów dla swojej biblioteki, co pozwoli Ci uniknąć ręcznego pisania. Pobierz specyfikację podczas procesu kompilacji, wygeneruj typy i prześlij skompilowany kod.

- **Punkt końcowy:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integracja z OpenAI SDK

Jeśli jesteś platformą, która priorytetowo traktuje ujednolicony schemat (OpenAI Chat Completions) zamiast funkcji specyficznych dla modelu, jest to najszybsza ścieżka.

**Zalety:**

- **Niewielkie utrudnienia:** często możesz dodać obsługę Gemini, zmieniając `baseURL` i `apiKey`. Jest to szybki sposób na zintegrowanie implementacji „Bring Your Own Key” i dodanie obsługi Gemini bez pisania nowego kodu.
- **Ograniczenia:** ta ścieżka jest zalecana tylko wtedy, gdy masz ograniczone możliwości korzystania z pakietu OpenAI SDK i nie potrzebujesz zaawansowanych funkcji Gemini, takich jak interfejs File API, lub ręcznego dodawania obsługi narzędzi takich jak Grounding z wyszukiwarką Google.

**Kompromis:**

- **Ograniczenia funkcji:** warstwa zgodności wprowadza ograniczenia podstawowych funkcji Gemini. Dostępne narzędzia po stronie serwera różnią się w zależności od platformy i mogą wymagać ręcznej obsługi, aby współpracować z narzędziami Gemini API.
- **Narzut na tłumaczenie:** ponieważ schemat OpenAI nie jest mapowany 1:1 na architekturę Gemini, korzystanie z warstwy zgodności wprowadza pewne złożoności, które wymagają dodatkowej pracy implementacyjnej, np. mapowania narzędzia „wyszukiwania” użytkownika na odpowiednie narzędzie platformy.
  Jeśli potrzebujesz znacznej ilości specjalnych przypadków, może być bardziej opłacalne używanie dedykowanego pakietu SDK lub interfejsu API dla każdej platformy.

**Sprawdzona metoda**

Jeśli to możliwe, zintegruj się bezpośrednio z interfejsem Gemini API. Aby jednak zapewnić maksymalną zgodność, rozważ użycie biblioteki, która rozpoznaje różnych dostawców i może obsługiwać mapowanie narzędzi i wiadomości.

## Sprawdzona metoda dla wszystkich partnerów: identyfikacja klienta

Wywołując interfejs Gemini API jako platforma lub biblioteka, musisz zidentyfikować klienta za pomocą nagłówka `x-goog-api-client`.

Umożliwia to Google identyfikowanie konkretnych segmentów ruchu, a jeśli Twoja biblioteka generuje określony wzorzec błędów, możemy się z Tobą skontaktować, aby pomóc w debugowaniu.

Użyj formatu `company-product/version` (np. `acme-framework/1.2.0`).

### Przykłady implementacji

### GenAI SDK

Dzięki udostępnieniu klienta interfejsu API pakiet SDK automatycznie dołącza Twój niestandardowy nagłówek do nagłówków wewnętrznych.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Dalsze kroki

- Aby dowiedzieć się więcej o
  pakietach GenAI SDK, otwórz [omówienie biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).
- Przejrzyj [dokumentację interfejsu API](https://ai.google.dev/api?hl=pl).
- Przeczytaj [przewodnik po zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
