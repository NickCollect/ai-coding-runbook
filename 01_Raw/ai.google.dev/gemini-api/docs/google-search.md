---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=it
fetched_at: 2026-05-25T05:29:23.282965+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Grounding con la Ricerca Google

Il grounding con la Ricerca Google collega il modello Gemini ai contenuti web in tempo reale
e funziona con tutte le lingue disponibili. In questo modo,
Gemini può fornire risposte più accurate e citare fonti verificabili oltre il suo knowledge cutoff.

La base di riferimento ti aiuta a creare applicazioni che possono:

- **Aumentare l'accuratezza fattuale:** ridurre le allucinazioni del modello basando
  le risposte su informazioni del mondo reale.
- **Accedere a informazioni in tempo reale:** rispondere a domande su eventi e argomenti recenti.
- **Fornisci citazioni**:crea fiducia negli utenti mostrando le fonti delle affermazioni del modello.

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Per saperne di più, prova il [notebook
dello strumento di ricerca](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=it).

## Come funziona il grounding con la Ricerca Google

Quando attivi lo strumento `google_search`, il modello gestisce automaticamente l'intero flusso di lavoro di ricerca, elaborazione e citazione delle informazioni.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=it)

1. **Prompt utente**:la tua applicazione invia un prompt dell'utente all'API Gemini
   con lo strumento `google_search` abilitato.
2. **Analisi del prompt**:il modello analizza il prompt e determina se una ricerca Google può migliorare la risposta.
3. **Ricerca Google**:se necessario, il modello genera automaticamente una o più query di ricerca e le esegue.
4. **Elaborazione dei risultati di ricerca:** il modello elabora i risultati di ricerca,
   sintetizza le informazioni e formula una risposta.
5. **Risposta fondata**:l'API restituisce una risposta finale e di facile utilizzo
   basata sui risultati di ricerca. Questa risposta include il testo della risposta del modello e `groundingMetadata` con le query di ricerca, i risultati web e le citazioni.

## Informazioni sulla risposta di grounding

Quando una risposta viene fondata correttamente, include un campo `groundingMetadata`. Questi dati strutturati sono essenziali per verificare
le rivendicazioni e creare un'esperienza di citazione avanzata nella tua applicazione.

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

L'API Gemini restituisce le seguenti informazioni con `groundingMetadata`:

- `webSearchQueries` : array delle query di ricerca utilizzate. Questo è utile per
  il debug e la comprensione del processo di ragionamento del modello.
- `searchEntryPoint` : contiene HTML e CSS per il rendering dei suggerimenti di ricerca richiesti. I requisiti di utilizzo completi sono descritti in dettaglio nei [Termini di
  servizio](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-search).
- `groundingChunks` : array di oggetti contenenti le origini web (`uri` e `title`).
- `groundingSupports` : array di blocchi per collegare la risposta del modello `text` alle fonti in `groundingChunks`. Ogni blocco collega un testo `segment` (definito
  da `startIndex` e `endIndex`) a uno o più `groundingChunkIndices`. Questa
  è la chiave per creare citazioni in linea.

Il grounding con la Ricerca Google può essere utilizzato anche in combinazione con lo [strumento di contesto
URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) per basare le risposte sia sui dati web pubblici sia sugli URL specifici che fornisci.

## Attribuire le fonti con le citazioni in linea

L'API restituisce dati strutturati sulle citazioni, offrendoti il controllo completo su come
visualizzare le fonti nell'interfaccia utente. Puoi utilizzare i campi `groundingSupports` e `groundingChunks` per collegare le affermazioni del modello direttamente alle relative fonti. Di seguito è riportato un pattern comune per l'elaborazione dei metadati per creare una
risposta con citazioni in linea e cliccabili.

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

La nuova risposta con citazioni in linea sarà simile alla seguente:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Prezzi

Quando utilizzi Grounding con la Ricerca Google con Gemini 3, il tuo progetto viene fatturato
per ogni query di ricerca che il modello decide di eseguire. Se il modello decide di
eseguire più query di ricerca per rispondere a un singolo prompt (ad esempio,
cercando `"UEFA Euro 2024 winner"` e `"Spain vs England Euro 2024 final
score"` nella stessa chiamata API), questo viene conteggiato come due utilizzi fatturabili dello strumento
per quella richiesta. Ai fini della fatturazione, ignoriamo le query di ricerca web vuote
quando conteggiamo le query uniche. Questo modello di fatturazione si applica solo ai modelli Gemini 3. Quando utilizzi la ricerca basata su grounding con Gemini 2.5 o modelli precedenti, il tuo progetto viene fatturato per prompt.

Per informazioni più dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

Puoi trovare le funzionalità complete nella pagina [Panoramica
modello](https://ai.google.dev/gemini-api/docs/models?hl=it).

| Modello | Grounding con la Ricerca Google |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image (anteprima) | ✔️ |
| Gemini 3.1 Pro (anteprima) | ✔️ |
| Gemini 3 Pro Image (anteprima) | ✔️ |
| Gemini 3 Flash (anteprima) | ✔️ |
| Gemini 3.1 Flash-Lite (anteprima) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinazioni di strumenti supportate

Puoi utilizzare Grounding con la Ricerca Google con altri strumenti come
[l'esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e
[il contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) per supportare casi d'uso più complessi.

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come il grounding con la Ricerca Google) con strumenti personalizzati (chiamata di funzioni). Scopri di più nella pagina
[Combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Passaggi successivi

- Prova la funzionalità [Grounding con la Ricerca Google nel cookbook dell'API Gemini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=it).
- Scopri altri strumenti disponibili, come la [chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).
- Scopri come arricchire i prompt con URL specifici utilizzando lo [strumento
  Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
