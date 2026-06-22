---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=pl
fetched_at: 2026-06-22T06:34:19.488227+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)

# Szybsze odkrywanie dzięki Gemini for Research

[Pobierz klucz Gemini API](https://aistudio.google.com/apikey?hl=pl)

Modele Gemini mogą być używane do prowadzenia badań podstawowych w różnych dziedzinach.
Oto sposoby, w jakie możesz wykorzystać Gemini w swoich badaniach:

- **Analizowanie i kontrolowanie wyników modelu**: aby przeprowadzić dalszą analizę, możesz zbadać kandydata na odpowiedź wygenerowanego przez model za pomocą narzędzi takich jak
  `CitationMetadata`. Możesz też skonfigurować opcje generowania i wyników modelu, takie jak `responseSchema`, `topP` i `topK`. [Więcej informacji](https://ai.google.dev/api/generate-content?hl=pl).
- **Dane wejściowe multimodalne**: Gemini może przetwarzać obrazy, dźwięk i filmy, co otwiera
  wiele ciekawych kierunków badań. [Więcej informacji](https://ai.google.dev/gemini-api/docs/vision?hl=pl).
- **Możliwości długiego kontekstu**: Gemini 3.0 Flash i Pro mają okno kontekstu o wielkości 1 miliona tokenów. [Więcej informacji](https://ai.google.dev/gemini-api/docs/long-context?hl=pl).
- **Grow with Google**: szybki dostęp do modeli Gemini przez interfejs API i Google AI
  Studio w przypadku zastosowań produkcyjnych. Jeśli szukasz platformy opartej na Google Cloud, Gemini Enterprise Agent Platform może zapewnić dodatkową infrastrukturę pomocniczą.

Aby wspierać badania akademickie i prowadzić nowatorskie badania, Google zapewnia
naukowcom i badaczom akademickim dostęp do środków Gemini API w ramach
[programu Gemini Academic](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=pl#gemini-academic-program).

## Pierwsze kroki z Gemini

Interfejs Gemini API i Google AI Studio pomagają rozpocząć pracę z najnowszymi modelami Google i przekształcić pomysły w aplikacje, które można skalować.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Polecani naukowcy

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=pl)

„Nasze badania dotyczą Gemini jako wizualnego modelu językowego (VLM) i jego zachowań agentowych w różnych środowiskach z perspektywy odporności i bezpieczeństwa. Do tej pory oceniliśmy odporność Gemini na rozpraszacze, takie jak wyskakujące okienka, gdy agenci VLM wykonują zadania na komputerze, i wykorzystaliśmy Gemini do analizowania interakcji społecznych, zdarzeń czasowych oraz czynników ryzyka na podstawie danych wejściowych wideo”.

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=pl)

„Gemini Pro i Flash z długim oknem kontekstu pomagają nam w OK-Robot, naszym projekcie manipulacji mobilnej z otwartym słownikiem. Gemini umożliwia złożone zapytania i polecenia w języku naturalnym dotyczące „pamięci” robota, w tym przypadku wcześniejszych obserwacji dokonanych przez robota podczas długiego okresu działania. Wraz z Mahi Shafiullahem używamy też Gemini do rozkładania zadań na kod, który robot może wykonać w rzeczywistym świecie”.

## Program Gemini Academic

Kwalifikujący się badacze akademiccy (np. wykładowcy, pracownicy i doktoranci) w [obsługiwanych
krajach](https://ai.google.dev/gemini-api/docs/available-regions?hl=pl) mogą ubiegać się o środki Gemini API
i wyższe limity szybkości na potrzeby projektów badawczych. Dzięki temu można zwiększyć przepustowość eksperymentów naukowych i przyspieszyć badania.

Szczególnie interesują nas obszary badawcze wymienione w sekcji poniżej, ale przyjmujemy zgłoszenia z różnych dziedzin nauki:

- **Oceny i testy porównawcze**: metody oceny zatwierdzone przez społeczność, które
  mogą zapewnić silny sygnał skuteczności w takich obszarach jak rzetelność, bezpieczeństwo, wykonywanie instrukcji, rozumowanie i planowanie.
- **Przyspieszanie odkryć naukowych z korzyścią dla ludzkości**: potencjalne
  zastosowania AI w interdyscyplinarnych badaniach naukowych, w tym w takich obszarach
  jak choroby rzadkie i zaniedbane, biologia eksperymentalna, materiałoznawstwo
  i zrównoważony rozwój.
- **Wcielenie i interakcje**: wykorzystanie dużych modeli językowych do
  badania nowych interakcji w dziedzinach AI wcielonej, interakcji otoczenia, robotyki i interakcji człowiek–komputer.
- **Możliwości emergentne**: odkrywanie nowych możliwości agentowych wymaganych do
  ulepszenia rozumowania i planowania oraz sposobów rozszerzania możliwości podczas
  wnioskowania (np. przez wykorzystanie Gemini Flash).
- **Interakcje i rozumienie multimodalne**: identyfikowanie luk i
  możliwości w zakresie multimodalnych modeli podstawowych do analizy, rozumowania,
  i planowania w różnych zadaniach.

Kryteria kwalifikacji: zgłaszać się mogą tylko osoby (wykładowcy, badacze lub osoby o równoważnych kwalifikacjach) powiązane z uznaną instytucją akademicką lub organizacją badawczą. Pamiętaj, że dostęp do interfejsu API i środki będą przyznawane i odbierane według uznania Google. Zgłoszenia sprawdzamy co miesiąc.

### Rozpocznij badania z Gemini API

[Zgłoś się](https://forms.gle/HMviQstU8PxC5iCt5)

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-19 UTC.

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-19 UTC."],[],[]]
