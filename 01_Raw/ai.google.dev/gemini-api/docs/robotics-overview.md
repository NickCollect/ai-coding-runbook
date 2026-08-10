---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl
fetched_at: 2026-08-10T03:12:19.067847+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Gemini Robotics ER

Modele Gemini Robotics ER (embodied reasoning) to modele wizualno-językowe (VLM), które umożliwiają robotom postrzeganie świata fizycznego i interakcję z nim. Interpretują dane wizualne, przeprowadzają rozumowanie przestrzenne i czasowe, planują wieloetapowe zadania oraz koordynują pracę robotów i narzędzi.

## Modele

Model Gemini Robotics ER 2 to najnowszy model w Gemini Robotics.
To nasz zaktualizowany model rozumowania, który umożliwia robotom dokładne zrozumienie otoczenia. Specjalizuje się w rozumowaniu w świecie fizycznym, np.w orkiestracji robotów za pomocą agentów (np. z użyciem dużych modeli językowych), rozumieniu filmów z robotów, w tym w rozumieniu postępów i wykrywaniu sukcesów, odczytywaniu wskazań przyrządów, wskazywaniu i rozumowaniu przestrzennym.

Model Gemini Robotics ER 2 wprowadza 2 punkty końcowe modelu:

- **`gemini-robotics-er-2-preview`**: standardowy model ER2. Wersja Gemini 3.5 Flash z ulepszonym rozumowaniem przestrzennym, wyszukiwaniem momentów w filmach, klasyfikacją postępu w filmach, koordynacją pracy wielu robotów i wieloetapowym korzystaniem z narzędzi.
- **`gemini-robotics-er-2-streaming-preview`**: zoptymalizowany pod kątem przesyłania strumieniowego w czasie rzeczywistym za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl). Użyj tego modelu w przypadku robotów o krótkim czasie oczekiwania, które przetwarzają ciągłe dane audio i wideo.

Jeśli używasz Gemini Robotics ER 1.6, przejdź na Gemini Robotics ER 2, zastępując w wywołaniach interfejsu API ciąg znaków
`model="gemini-robotics-er-1.6-preview"` ciągiem
`model="gemini-robotics-er-2-preview"` lub
`model="gemini-robotics-er-2-streaming-preview"`. Pamiętaj, że model Gemini Robotics ER 1.6 zostanie wyłączony [pod koniec sierpnia](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl#robotics-models).

[Wypróbuj Gemini Robotics ER 2 w Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=pl)

## Możliwości robotów

Gemini Robotics ER obsługuje szereg funkcji rozumowania w świecie fizycznym.
Wybierz funkcję, aby dowiedzieć się więcej:

| Możliwości | Opis | Przewodnik |
| --- | --- | --- |
| rozumowanie przestrzenne, | wskazywać obiekty, śledzić je w filmach, wykrywać za pomocą ramek ograniczających i planować trajektorie. | [Rozumowanie przestrzenne](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=pl) |
| Agentic Vision | Używaj wykonywania kodu, aby zwiększać możliwości innych funkcji, korzystając z narzędzi do manipulowania obrazami. | [Wizja agentowa](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=pl) |
| Orkiestracja zadań | Łącz rozumowanie przestrzenne z niestandardowymi interfejsami API robotów, aby wykonywać zadania długoterminowe. | [Orkiestracja zadań](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl) |
| Streaming (tylko punkt końcowy Gemini Robotics ER 2 Streaming) | Dwukierunkowe przesyłanie strumieniowe dla robotów w czasie rzeczywistym z małymi opóźnieniami i wywoływaniem funkcji. | [Streaming dla robotyki](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) |
| Postępy odtwarzania filmu (tylko Gemini Robotics ER2) | Wyszukiwanie momentów i klasyfikowanie postępów na podstawie ciągłych strumieni wideo. | [Rozumienie filmów](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl) |

## Pierwsze kroki

Ten przykład znajduje obiekty na obrazie i zwraca ich znormalizowane współrzędne 2D oraz etykiety. Możesz przekazać te dane wyjściowe bezpośrednio do interfejsu API robotyki lub modelu VLA, aby wygenerować działania robota.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

Dane wyjściowe będą tablicą JSON zawierającą obiekty, z których każdy będzie miał `point` (znormalizowane współrzędne `[y, x]`) i `label` identyfikujące obiekt.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Na tym obrazie widać, jak mogą być wyświetlane te punkty:

![Przykład wyświetlający punkty obiektów na obrazie](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=pl)

## Jak to działa

Gemini Robotics ER przyjmuje dane wejściowe w postaci obrazów, filmów lub dźwięku z promptami w języku naturalnym. Identyfikuje obiekty, analizuje kontekst sceny i relacje przestrzenne oraz zwraca uporządkowane dane wyjściowe, takie jak współrzędne lub ramki ograniczające.

Gemini Robotics ER jest też agentem: dzieli złożone zadania na podzadania i wykonuje je, wywołując funkcje robota lub uruchamiając wygenerowany kod. Na przykład „włóż jabłko do miski” staje się sekwencją kroków: zlokalizuj, chwyć i umieść.

Więcej informacji o tym, jak Gemini wykonuje wywołania narzędzi, znajdziesz w sekcji [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=pl#how-it-works).

## Bezpieczeństwo

Gemini Robotics ER zostało zaprojektowane z myślą o bezpieczeństwie, ale to Ty odpowiadasz za utrzymanie bezpiecznego środowiska wokół robota. Modele generatywnej AI mogą popełniać błędy, a roboty fizyczne mogą powodować uszkodzenia. Więcej informacji znajdziesz na [stronie Google DeepMind poświęconej bezpieczeństwu robotów](https://deepmind.google/models/gemini-robotics/safety?hl=pl).

## Sprawdzone metody

1. Używaj prostego, języka naturalnego. Opisz, co ma robić robot, tak jakbyś mówił(-a) do człowieka. Jeśli dane słowo nie działa, wypróbuj popularny synonim.
2. Optymalizuj dane wizualne. Przed wysłaniem obrazu możesz przyciąć lub powiększyć małe lub niewyraźne obiekty. Oświetlenie i niski kontrast kolorów mogą wpływać na wykrywanie.
3. Podziel skomplikowane zadania na etapy. Każdy krok wysyłaj jako osobny prompt, aby model był bardziej skupiony i dokładniejszy.
4. W przypadku zadań wymagających dużej precyzji wykonuj zapytania wielokrotnie i obliczaj średnią wyników. To podejście oparte na konsensusie zmniejsza wariancję danych przestrzennych.

## Ograniczenia

Podczas tworzenia aplikacji z użyciem Gemini Robotics ER pamiętaj o tych ograniczeniach:

- **Ograniczenia dotyczące klucza interfejsu API:** interfejs Gemini API nie akceptuje żądań z nieograniczonych kluczy interfejsu API i zwraca błąd `403 Forbidden`. Zabezpiecz klucz interfejsu API, dodając ograniczenia w [AI Studio](https://aistudio.google.com/api-keys?hl=pl).
  Więcej informacji znajdziesz w artykule [Zabezpieczanie kluczy interfejsu API bez ograniczeń](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#secure-unrestricted-keys).
- **Opóźnienie a wydajność:** złożone zapytania, dane wejściowe o wysokiej rozdzielczości lub wysoki poziom myślenia mogą wydłużyć czas przetwarzania. W przypadku poziomu myślenia wybierz średni, aby zachować równowagę między czasem oczekiwania a wydajnością.
- **Halucynacje:** podobnie jak wszystkie duże modele językowe, modele Gemini Robotics ER mogą czasami „halucynować” lub podawać nieprawidłowe informacje, zwłaszcza w przypadku niejednoznacznych promptów lub danych wejściowych spoza zakresu.
- **Zależność od jakości prompta:** jakość wygenerowanych treści zależy od precyzji prompta. Używaj konkretnych, dobrze skonstruowanych promptów.
- **Koszt obliczeniowy:** uruchamianie modelu, zwłaszcza w przypadku danych wejściowych w postaci filmów lub wysokich wartości `thinking_budget`, zużywa zasoby obliczeniowe i generuje koszty.
  Więcej informacji znajdziesz na stronie [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).
- **Rodzaje danych wejściowych:** szczegółowe informacje o ograniczeniach w przypadku każdego trybu znajdziesz w tych artykułach.
  - [Dane wejściowe dotyczące obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#technical-details-image)
  - [Wejścia wideo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#supported-formats)
  - [Wejścia audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl#supported-formats)

## Informacje na temat ochrony prywatności

Przyjmujesz do wiadomości, że modele, o których mowa w tym dokumencie („Modele robotyczne”), wykorzystują dane wideo i audio do działania i poruszania sprzętem zgodnie z Twoimi instrukcjami. W związku z tym możesz używać modeli robotów w taki sposób, aby zbierały dane od osób, które można zidentyfikować, takie jak dane głosowe, obrazy i dane dotyczące podobieństwa („Dane osobowe”). Jeśli zdecydujesz się korzystać z modeli robotów w sposób, który umożliwia zbieranie danych osobowych, nie możesz zezwolić żadnym osobom, których tożsamość można ustalić, na interakcję z modelami robotów ani na przebywanie w ich pobliżu, dopóki nie zostaną one odpowiednio poinformowane o tym, że ich dane osobowe mogą być przekazywane do Google i wykorzystywane przez Google zgodnie z Dodatkowymi warunkami korzystania z usługi Gemini API, które znajdziesz na stronie [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=pl) (dalej „Warunki”), w tym zgodnie z sekcją zatytułowaną „Jak Google wykorzystuje Twoje dane”. Zapewnisz, że takie powiadomienie zezwala na zbieranie i wykorzystywanie danych osobowych w sposób określony w Warunkach, oraz podejmiesz uzasadnione ekonomicznie starania, aby zminimalizować zbieranie i rozpowszechnianie danych osobowych, stosując techniki takie jak rozmywanie twarzy i używając modeli robotów w obszarach, w których nie ma osób umożliwiających identyfikację, w największym możliwym zakresie.

## Ceny

Szczegółowe informacje o cenach i dostępnych regionach znajdziesz na stronie [cennika](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Punkty końcowe modelu

### Gemini Robotics ER 2 (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-2-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handyman Możliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Obsługiwane  **[Wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Obsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Obsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Obsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Obsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Nieobsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Ustrukturyzowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Obsługiwane  **[Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Obsługiwane |
| speed Opcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Obsługiwane  **[Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Priorytet wnioskowania](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| Wersje 123 | Więcej informacji znajdziesz w [wzorcach wersji modelu](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#model-versions).  - Podgląd: `gemini-robotics-er-2-preview` |
| calendar\_monthOstatnia aktualizacja | Lipiec 2026 r. |
| id\_cardKarta modelu | [Karta modelu](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pl) |

### Gemini Robotics ER 2 Streaming Preview

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-2-streaming-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handyman Możliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Nieobsługiwane  **[Wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Nieobsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Nieobsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Nieobsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Nieobsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Obsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Ustrukturyzowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Nieobsługiwane  **[Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Nieobsługiwane |
| speed Opcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Nieobsługiwane  **[Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Priorytet wnioskowania](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| Wersje 123 | Więcej informacji znajdziesz w [wzorcach wersji modelu](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#model-versions).  - Podgląd: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthOstatnia aktualizacja | Lipiec 2026 r. |
| id\_cardKarta modelu | [Karta modelu](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pl) |

### Gemini Robotics ER 1.6 (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-1.6-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handyman Możliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Obsługiwane  **[Wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Obsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Obsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Obsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Obsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Nieobsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Ustrukturyzowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Obsługiwane  **[Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Obsługiwane |
| speed Opcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Obsługiwane  **[Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Priorytet wnioskowania](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| Wersje 123 | Więcej informacji znajdziesz w [wzorcach wersji modelu](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl#model-versions).  - Podgląd: `gemini-robotics-er-1.6-preview` |
| calendar\_monthOstatnia aktualizacja | Grudzień 2025 r. |
| cognition\_2Granica wiedzy | Styczeń 2025 r. |

## Co dalej?

- [Rozumowanie przestrzenne](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=pl) – wskazywanie, śledzenie, ramki ograniczające, trajektorie.
- [Funkcje agentowe](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=pl) – wykonywanie kodu, odczytywanie instrumentów, adnotacje do obrazów.
- [Orkiestracja zadań](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl) – zadania długoterminowe z niestandardowymi interfejsami API robotów.
- [Robotyka z transmisją strumieniową](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) – dwukierunkowa transmisja strumieniowa w czasie rzeczywistym (tylko Gemini Robotics ER 2).
- [Rozumienie wideo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl) – wyszukiwanie momentów i klasyfikacja postępów (tylko Gemini Robotics ER 2).
- [Bezpieczeństwo robotów Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=pl) – badania nad bezpieczeństwem modeli.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
