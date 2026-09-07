---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=pl
fetched_at: 2026-09-07T05:35:58.336276+00:00
title: "Grounding z\u00a0u\u017cyciem wyszukiwarki Google \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Grounding z użyciem wyszukiwarki Google

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google łączy model Gemini z treściami z internetu w czasie rzeczywistym i działa we wszystkich dostępnych językach. Pozwala to Gemini udzielać dokładniejszych odpowiedzi i cytować zweryfikowane źródła poza jego granicą wiedzy.

Grounding pomaga tworzyć aplikacje, które mogą:

- **zwiększać dokładność faktów:** zmniejszaj halucynacje modelu, opierając odpowiedzi na informacjach ze świata rzeczywistego;
- **uzyskiwać dostęp do informacji w czasie rzeczywistym:** odpowiadaj na pytania dotyczące najnowszych wydarzeń i tematów;
- **podawać cytaty:** buduj zaufanie użytkowników, pokazując źródła twierdzeń modelu.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.7-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Więcej informacji znajdziesz w
notatniku [narzędzia do wyszukiwania.](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=pl)

## Jak działa powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google

Gdy włączysz narzędzie `google_search`, model automatycznie obsługuje cały proces wyszukiwania, przetwarzania i cytowania informacji.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=pl)

1. **Prompt użytkownika:** Twoja aplikacja wysyła prompt użytkownika do Gemini API z włączonym narzędziem `google_search`.
2. **Analiza prompta:** model analizuje prompt i określa, czy wyszukiwanie w Google może poprawić odpowiedź.
3. **Wyszukiwanie w Google:** w razie potrzeby model automatycznie generuje jedno lub kilka zapytań i je wykonuje.
4. **Przetwarzanie wyników wyszukiwania:** model przetwarza wyniki wyszukiwania, syntetyzuje informacje i formułuje odpowiedź.
5. **Odpowiedź oparta na źródłach:** interfejs API zwraca ostateczną, przyjazną dla użytkownika odpowiedź opartą na wynikach wyszukiwania. Ta odpowiedź zawiera tekstową odpowiedź modelu i `groundingMetadata` z zapytaniami, wynikami wyszukiwania i cytatami.

## Informacje o odpowiedzi opartej na źródłach

Gdy odpowiedź jest oparta na źródłach, zawiera pole `groundingMetadata`. Te uporządkowane dane są niezbędne do weryfikowania twierdzeń i tworzenia w aplikacji rozbudowanych cytatów.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API zwraca te informacje z `groundingMetadata`:

- `webSearchQueries` : tablica użytych zapytań. Przydaje się do debugowania i zrozumienia procesu rozumowania modelu.
- `searchEntryPoint` : zawiera kod HTML i CSS do renderowania wymaganych sugestii wyszukiwania. Pełne wymagania dotyczące użytkowania są opisane w [Warunkach
  korzystania z usługi](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-search).
- `groundingChunks` : tablica obiektów zawierających źródła internetowe (`uri` i `title`).
- `groundingSupports` : tablica fragmentów, które łączą odpowiedź modelu `text` ze źródłami w `groundingChunks`. Każdy fragment łączy `segment` tekstu (zdefiniowany przez `startIndex` i `endIndex`) z co najmniej 1 elementem `groundingChunkIndices`. Jest to klucz do tworzenia cytatów w tekście.

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google można też stosować w połączeniu z narzędziem do kontekstu [adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), aby opierać odpowiedzi zarówno na publicznych danych
internetowych, jak i na podanych przez Ciebie adresach URL.

## Podawanie źródeł za pomocą cytatów w tekście

Interfejs API zwraca uporządkowane dane cytatów, co daje Ci pełną kontrolę nad sposobem wyświetlania źródeł w interfejsie użytkownika. Możesz użyć pól `groundingSupports` i `groundingChunks`, aby połączyć stwierdzenia modelu bezpośrednio z ich źródłami. Oto typowy wzorzec przetwarzania metadanych w celu utworzenia odpowiedzi z cytatami w tekście, w które można kliknąć.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

Nowa odpowiedź z cytatami w tekście będzie wyglądać tak:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Ceny

Gdy używasz powiązania ze źródłami informacji przy użyciu wyszukiwarki Google z Gemini 3, projekt jest obciążany za każde zapytanie, które model zdecyduje się wykonać. Jeśli model zdecyduje się
wykonać kilka zapytań, aby odpowiedzieć na 1 prompt (np.
wyszukać hasła `"UEFA Euro 2024 winner"` i `"Spain vs England Euro 2024 final
score"` w ramach tego samego wywołania interfejsu API), będzie to liczone jako 2 płatne użycia narzędzia
w przypadku tego żądania. Na potrzeby rozliczeń ignorujemy puste zapytania podczas zliczania unikalnych zapytań. Ten model rozliczeń dotyczy tylko modeli Gemini 3. Gdy używasz groundingu przy użyciu wyszukiwarki z Gemini 2.5 lub starszymi modelami, projekt jest obciążany za każdy prompt.

Szczegółowe informacje o cenach znajdziesz na stronie cennika [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

Pełne możliwości znajdziesz na stronie przeglądu [modelu](https://ai.google.dev/gemini-api/docs/models?hl=pl).

| Model | Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google |
| --- | --- |
| Gemini 3.7 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image (wersja testowa) | ✔️ |
| Gemini 3.1 Pro (wersja testowa) | ✔️ |
| Gemini 3 Pro Image (wersja testowa) | ✔️ |
| Gemini 3 Flash (wersja testowa) | ✔️ |
| Gemini 3.1 Flash-Lite (wersja testowa) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Obsługiwane kombinacje narzędzi

Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google możesz używać z innymi narzędziami, takimi jak
[wykonanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl),
[kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) i
[powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl) (obsługiwane w
Gemini 3.5 Flash i nowszych modelach), aby obsługiwać bardziej złożone przypadki użycia. Modele Gemini 3 obsługują też łączenie tych wbudowanych narzędzi z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

## Co dalej?

- Wypróbuj [powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google w przewodniku Gemini API Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=pl).
- Dowiedz się więcej o innych dostępnych narzędziach, np. o [wywoływaniu funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl).
- Dowiedz się, jak rozszerzać prompty o konkretne adresy URL za pomocą [narzędzia do
  kontekstu adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-20 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-20 UTC."],[],[]]
