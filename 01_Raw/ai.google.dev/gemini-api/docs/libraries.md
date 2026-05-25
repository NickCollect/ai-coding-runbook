---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=pl
fetched_at: 2026-05-25T05:27:48.943985+00:00
title: "Biblioteki Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Biblioteki Gemini API

Podczas tworzenia aplikacji za pomocą interfejsu Gemini API zalecamy korzystanie z **pakietu Google GenAI SDK**.
Są to oficjalne biblioteki gotowe do użycia w środowisku produkcyjnym, które tworzymy i utrzymujemy w przypadku najpopularniejszych języków. Są one w [Ogólnej Dostępności](https://ai.google.dev/gemini-api/docs/libraries?hl=pl#new-libraries) i używane we wszystkich naszych oficjalnych
dokumentach i przykładach.

Jeśli dopiero zaczynasz korzystać z interfejsu Gemini API, zapoznaj się z naszym [przewodnikiem szybkiego startu](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl).

## Obsługa języków i instalacja

Pakiet Google GenAI SDK jest dostępny w językach Python, JavaScript/TypeScript, Go i Java. Bibliotekę każdego języka możesz zainstalować za pomocą menedżerów pakietów lub odwiedzić repozytoria GitHub, aby uzyskać więcej informacji:

### Python

- Biblioteka: [`google-genai`](https://pypi.org/project/google-genai)
- Repozytorium GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Instalacja: `pip install google-genai`

### JavaScript

- Biblioteka: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Repozytorium GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Instalacja: `npm install @google/genai`

### Go

- Biblioteka: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Repozytorium GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Instalacja: `go get google.golang.org/genai`

### Java

- Biblioteka: `google-genai`
- Repozytorium GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Instalacja: jeśli używasz Maven, dodaj do zależności ten kod:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Biblioteka: `Google.GenAI`
- Repozytorium GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Instalacja: `dotnet add package Google.GenAI`

## Ogólna dostępność

Od maja 2025 r. pakiet Google GenAI SDK jest ogólnie dostępny na wszystkich obsługiwanych platformach i jest zalecaną biblioteką do uzyskiwania dostępu do interfejsu Gemini API.
Jest stabilny, w pełni obsługiwany w środowisku produkcyjnym i aktywnie utrzymywany.
Zapewnia dostęp do najnowszych funkcji i najlepszą wydajność podczas pracy z Gemini.

Jeśli używasz jednej z naszych starszych bibliotek, zdecydowanie zalecamy przejście na nową, aby uzyskać dostęp do najnowszych funkcji i najlepszej wydajności podczas pracy z Gemini. Więcej informacji znajdziesz w sekcji [Starsze biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl#previous-sdks).

## Starsze biblioteki i migracja

[Jeśli używasz jednej z naszych starszych bibliotek, zalecamy przejście na nowe biblioteki.](https://ai.google.dev/gemini-api/docs/migrate?hl=pl)

Starsze biblioteki nie zapewniają dostępu do najnowszych funkcji (takich jak
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) i [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl)) i są
wycofywane z dniem 30 listopada 2025 r.

Stan obsługi każdej starszej biblioteki jest inny. Szczegółowe informacje znajdziesz w tabeli poniżej:

| Język | Starsza biblioteka | Stan obsługi | Zalecana biblioteka |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Nie jest aktywnie utrzymywana | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Nie jest aktywnie utrzymywana | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Nie jest aktywnie utrzymywana | `google.golang.org/genai` |
| **Dart i Flutter** | `google_generative_ai` | Nie jest aktywnie utrzymywana | Użyj [Genkit Dart](https://genkit.dev/docs/dart/get-started/) lub [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Nie jest aktywnie utrzymywana | Użyj [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=pl) |
| **Android** | `generative-ai-android` | Nie jest aktywnie utrzymywana | Użyj [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=pl) |

**Uwaga dla programistów w Javie:** nie było starszego pakietu Java SDK dostarczonego przez Google dla interfejsu Gemini API, więc nie jest wymagana migracja z poprzedniej biblioteki Google. Możesz
od razu zacząć korzystać z nowej biblioteki opisanej w
[sekcji Obsługa języków i instalacja](#install).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-13 UTC."],[],[]]
