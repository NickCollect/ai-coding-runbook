---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=it
fetched_at: 2026-06-01T06:08:02.765776+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Risoluzione dei media

Il parametro `media_resolution` controlla il modo in cui l'API Gemini elabora gli input multimediali come immagini, video e documenti PDF determinando il **numero massimo di token** allocati per gli input multimediali, consentendoti di bilanciare la qualità della risposta rispetto a latenza e costi. Per le diverse impostazioni, i valori predefiniti e la loro corrispondenza con i token, consulta la sezione [Conteggio dei token](#token-counts).

Puoi configurare la risoluzione dei media per i singoli oggetti multimediali (elementi di contenuti) all'interno della richiesta (solo Gemini 3).

## Risoluzione dei media per elemento di contenuti (solo Gemini 3)

Gemini 3 ti consente di impostare la risoluzione dei media per i singoli oggetti multimediali all'interno della richiesta, offrendo un'ottimizzazione granulare dell'utilizzo dei token. Puoi combinare i livelli di risoluzione in una singola richiesta. Ad esempio, puoi utilizzare l'alta risoluzione per un diagramma complesso e la bassa risoluzione per un'immagine contestuale semplice.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Valori di risoluzione disponibili

L'API Gemini definisce i seguenti livelli per la risoluzione dei media:

- `unspecified`: l'impostazione predefinita. Il conteggio dei token per questo livello varia in modo significativo tra Gemini 3 e i modelli Gemini precedenti.
- `low`: conteggio dei token inferiore, con conseguente elaborazione più rapida e costi inferiori, ma con meno dettagli.
- `medium`: un equilibrio tra dettagli, costi e latenza.
- `high`: conteggio dei token più elevato, che fornisce più dettagli al modello, a scapito di latenza e costi maggiori.
- `ultra_high` (solo per elemento di contenuti): conteggio dei token più elevato, necessario per casi d'uso specifici come [l'utilizzo del computer](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=it).

Tieni presente che `high` offre prestazioni ottimali per la maggior parte dei casi d'uso.

Il numero esatto di token generati per ciascuno di questi livelli dipende sia dal **tipo di media** (immagine, video, PDF) sia dalla **versione del modello**.

## Conteggio dei token

Le tabelle seguenti riepilogano i conteggi approssimativi dei token per ogni valore `media_resolution` e tipo di media per famiglia di modelli.

**Modelli Gemini 3**

| MediaResolution | Immagine | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (valore predefinito) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + testo nativo |
| `medium` | 560 | 70 | 560 + testo nativo |
| `high` | 1120 | 280 | 1120 + testo nativo |
| `ultra_high` | 2240 | N/D | N/D |

## Scegliere la risoluzione giusta

- **Valore predefinito (`unspecified`):** inizia con il valore predefinito. È ottimizzato per un buon equilibrio tra qualità, latenza e costi per i casi d'uso più comuni.
- **`low`:** utilizza questa impostazione per gli scenari in cui costi e latenza sono fondamentali e i dettagli granulari sono meno importanti.
- **`medium` / `high`:** aumenta la risoluzione quando l'attività richiede la comprensione di dettagli complessi all'interno dei media. Questo è spesso necessario per l'analisi visiva complessa, la lettura di grafici o la comprensione di documenti densi.
- **`ultra_high`** : disponibile solo per l'impostazione per elemento di contenuti. Consigliato per casi d'uso specifici come l'utilizzo del computer o quando i test mostrano un miglioramento netto rispetto a `high`.
- **Controllo per elemento di contenuti (Gemini 3):** ottimizza l'utilizzo dei token. Ad esempio, in un prompt con più immagini, utilizza `high` per un diagramma complesso e `low` o `medium` per immagini contestuali più semplici.

**Impostazioni consigliate**

Di seguito sono elencate le impostazioni di risoluzione dei media consigliate per ogni tipo di media supportato.

| Tipo di media | Impostazione consigliata | Token massimi | Indicazioni per l'utilizzo |
| --- | --- | --- | --- |
| **Google Immagini** | `high` | 1120 | Consigliato per la maggior parte delle attività di analisi delle immagini per garantire la massima qualità. |
| **PDF** | `medium` | 560 | Ottimale per la comprensione dei documenti; la qualità in genere raggiunge il livello massimo con `medium`. L'aumento a `high` raramente migliora i risultati dell'OCR per i documenti standard. |
| **Video** (generale) | `low` (o `medium`) | 70 (per frame) | **Nota:** per i video, le impostazioni `low` e `medium` vengono trattate in modo identico (70 token) per ottimizzare l'utilizzo del contesto. Questo è sufficiente per la maggior parte delle attività di riconoscimento e descrizione delle azioni. |
| **Video** (con molti testi) | `high` | 280 (per frame) | Necessario solo quando il caso d'uso prevede la lettura di testi densi (OCR) o piccoli dettagli all'interno dei frame video. |

Esegui sempre test e valuta l'impatto delle diverse impostazioni di risoluzione sulla tua applicazione per trovare il miglior compromesso tra qualità, latenza e costi.

## Riepilogo della compatibilità delle versioni

- L'impostazione di `resolution` sui singoli elementi di contenuti è **esclusiva dei modelli Gemini 3**.

## Passaggi successivi

- Scopri di più sulle funzionalità multimodali dell'API Gemini nelle guide alla [comprensione delle immagini](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=it), alla [comprensione dei video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=it) e alla [comprensione dei documenti](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-28 UTC."],[],[]]
