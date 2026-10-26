---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=it
fetched_at: 2026-10-26T05:47:51.742028+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Gemini Robotics ER

I modelli Gemini Robotics ER (embodied reasoning) sono modelli di linguaggio visivo (VLM) che consentono ai robot di percepire e interagire con il mondo fisico. Interpretano i dati visivi, eseguono ragionamenti spaziali e temporali, pianificano attività in più passaggi e orchestrano robot e strumenti.

## Modelli

Il modello Gemini Robotics ER 2 è l'ultimo modello di Gemini Robotics.
È il nostro modello di ragionamento aggiornato che consente ai robot di comprendere con precisione l'ambiente circostante. È specializzato in funzionalità di ragionamento basate sull'interazione con il mondo fisico, come l'orchestrazione agentica dei robot (ad es. utilizzando VLA), la comprensione dei video dei robot, tra cui la comprensione dei progressi e il rilevamento del successo, la lettura degli strumenti, il puntamento e il ragionamento spaziale.

Il modello Gemini Robotics ER 2 introduce due endpoint del modello:

- **`gemini-robotics-er-2-preview`**: il modello ER 2 standard. Si basa su Gemini 3.5 Flash con un ragionamento spaziale migliorato, la ricerca di momenti nei video, la classificazione dell'avanzamento dei video, l'orchestrazione multi-robot e l'utilizzo di strumenti in più passaggi.
- **`gemini-robotics-er-2-streaming-preview`**: ottimizzato per lo streaming in tempo reale tramite l'[API Live](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it). Utilizza questo modello per agenti robotici a bassa latenza che elaborano input audio e video continui.

Se utilizzi Gemini Robotics ER 1.6, esegui l'upgrade a Gemini Robotics ER 2 sostituendo
`model="gemini-robotics-er-1.6-preview"` con
`model="gemini-robotics-er-2-preview"` o
`model="gemini-robotics-er-2-streaming-preview"` nelle chiamate API. Tieni presente che il modello Gemini Robotics ER 1.6 verrà disattivato alla [fine di agosto](https://ai.google.dev/gemini-api/docs/deprecations?hl=it#robotics-models).

[Prova Gemini Robotics ER 2 in Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=it)

## Funzionalità di robotica

Gemini Robotics ER supporta una serie di funzionalità di ragionamento basate sull'interazione con il mondo fisico.
Seleziona una funzionalità per saperne di più:

| Capacità | Descrizione | Guida |
| --- | --- | --- |
| Ragionamento spaziale | Indica gli oggetti, monitorali nei video, rilevane la presenza con i riquadri di delimitazione, pianifica le traiettorie. | [Ragionamento spaziale](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=it) |
| Visione agentica | Utilizza l'esecuzione di codice per migliorare altre funzionalità sfruttando gli strumenti di manipolazione delle immagini. | [Visione agentica](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=it) |
| Orchestrazione delle attività | Combina il ragionamento spaziale con API di robot personalizzate per completare attività a lungo termine. | [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=it) |
| Streaming (solo endpoint di streaming Gemini Robotics ER 2) | Streaming bidirezionale per agenti robot in tempo reale con chiamata di funzione a bassa latenza. | [Streaming per la robotica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it) |
| Avanzamento video (solo Gemini Robotics ER 2) | Individuazione di momenti e classificazione dei progressi da feed video continui. | [Comprensione dei video](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=it) |

## Per iniziare

L'esempio seguente trova gli oggetti in un'immagine e restituisce le relative etichette e coordinate 2D normalizzate. Puoi passare questo output direttamente a un'API di robotica o a un modello VLA per generare azioni del robot.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
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
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

L'output sarà un array JSON contenente oggetti, ciascuno con un `point` (coordinate `[y, x]` normalizzate) e un `label` che identifica l'oggetto.

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

L'immagine seguente è un esempio di come possono essere visualizzati questi punti:

![Un esempio che mostra i punti degli oggetti in un'immagine](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=it)

## Come funziona

Gemini Robotics ER accetta input di immagini, video o audio con prompt in linguaggio naturale. Identifica gli oggetti, ragiona sul contesto della scena e sulle relazioni spaziali e restituisce un output strutturato come coordinate o riquadri di delimitazione.

Gemini Robotics ER è anche agentico: suddivide le attività complesse in sottoattività e le esegue chiamando le funzioni del robot o eseguendo il codice generato. Ad esempio, "metti la mela nella ciotola" diventa una sequenza di passaggi di individuazione, presa e posizionamento.

Per informazioni dettagliate su come Gemini esegue le chiamate degli strumenti, consulta [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=it#how-it-works).

## Sicurezza

Sebbene Gemini Robotics ER sia stato creato tenendo conto della sicurezza, è tua responsabilità mantenere un ambiente sicuro intorno al robot. I modelli di AI generativa possono commettere errori e i robot fisici possono causare danni. Per saperne di più, visita la [pagina sulla sicurezza della robotica di Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=it).

## Best practice

1. Usa un linguaggio semplice e naturale. Descrivi cosa vuoi che faccia il robot come faresti con una persona. Se un termine non funziona, prova un sinonimo comune.
2. Ottimizza l'input visivo. Ritaglia o aumenta lo zoom su oggetti piccoli o poco chiari prima di inviare l'immagine. L'illuminazione e il basso contrasto cromatico possono influire sul rilevamento.
3. Suddividi le attività complesse in passaggi. Invia ogni passaggio come prompt separato per mantenere il modello concentrato e migliorare l'accuratezza.
4. Esegui query più volte e calcola la media dei risultati per le attività ad alta precisione. Questo approccio basato sul consenso riduce la varianza degli output spaziali.

## Limitazioni

Tieni presenti le seguenti limitazioni durante lo sviluppo con Gemini Robotics ER:

- **Limitazioni delle chiavi API:** l'API Gemini non accetta richieste da chiavi API senza limitazioni e restituisce un errore `403 Forbidden`. Proteggi la tua chiave API aggiungendo limitazioni in [AI Studio](https://aistudio.google.com/api-keys?hl=it).
  Per maggiori dettagli, consulta [Proteggi le chiavi API senza restrizioni](https://ai.google.dev/gemini-api/docs/api-key?hl=it#secure-unrestricted-keys).
- **Latenza e prestazioni:** query complesse, input ad alta risoluzione o livelli di ragionamento elevati possono comportare tempi di elaborazione più lunghi. Per il livello di ragionamento, utilizza Medio per un buon equilibrio tra latenza e prestazioni.
- **Allucinazioni:** come tutti i modelli linguistici di grandi dimensioni, i modelli ER di Gemini Robotics
  possono occasionalmente "generare allucinazioni" o fornire informazioni errate, soprattutto
  per prompt ambigui o input fuori distribuzione.
- **Dipendenza dalla qualità del prompt:** la qualità dell'output dipende dalla chiarezza del prompt di input. Utilizza prompt specifici e ben strutturati.
- **Costo di calcolo:** l'esecuzione del modello, in particolare con input video o
  `thinking_budget` elevati, consuma risorse di calcolo e comporta dei costi.
  Per ulteriori dettagli, consulta la pagina [Ragionamento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it).
- **Tipi di input:** consulta i seguenti argomenti per i dettagli sulle limitazioni di ciascuna modalità.
  - [Input di immagini](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=it#technical-details-image)
  - [Input video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=it#supported-formats)
  - [Input audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=it#supported-formats)

## Informativa sulla privacy

Riconosci che i modelli a cui si fa riferimento in questo documento (i "Modelli di robotica") utilizzano dati video e audio per far funzionare e muovere l'hardware in base alle tue istruzioni. Pertanto, puoi utilizzare i Modelli di robotica in modo che i dati di persone identificabili, come dati vocali, immagini e somiglianze ("Dati personali"), vengano raccolti dai Modelli di robotica. Se scegli di utilizzare i Modelli di robotica in modo da raccogliere
Dati personali, accetti di non consentire a nessuna persona identificabile di
interagire con i Modelli di robotica o di essere presente nell'area circostante,
a meno che e fino a quando tali persone identificabili non siano state sufficientemente informate e
non abbiano acconsentito al fatto che i loro Dati personali possano essere forniti a Google e utilizzati
da Google come descritto nei Termini di servizio aggiuntivi delle API Gemini disponibili all'indirizzo
[https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=it)
(i "Termini"), anche in conformità
con la sezione intitolata "In che modo Google utilizza i tuoi dati". Dovrai assicurarti che tale
informativa consenta la raccolta e l'utilizzo dei Dati personali come descritto nei Termini
e dovrai fare tutto il possibile dal punto di vista commerciale per ridurre al minimo la raccolta e
la distribuzione dei Dati personali utilizzando tecniche come la sfocatura dei volti e
l'utilizzo dei Modelli di robotica in aree che non contengono persone identificabili,
nella misura possibile.

## Prezzi

Per informazioni dettagliate sui prezzi e sulle regioni disponibili, consulta la pagina dei [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Endpoint del modello

### Gemini Robotics ER 2 (anteprima)

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-2-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza con priorità](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Per maggiori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Anteprima: `gemini-robotics-er-2-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |

### Anteprima di Gemini Robotics ER 2 Streaming

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-2-streaming-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Non supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Non supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Non supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Non supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Non supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Non supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Non supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Non supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza con priorità](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Per ulteriori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Anteprima: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |

### Gemini Robotics ER 1.6 Preview

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-1.6-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza con priorità](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Per ulteriori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Arresta: `gemini-robotics-er-1.6-preview` |
| calendar\_monthUltimo aggiornamento | Dicembre 2025 |
| cognition\_2Knowledge cutoff | Gennaio 2025 |

## Passaggi successivi

- [Ragionamento spaziale](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=it): puntamento, monitoraggio, riquadri di delimitazione, traiettorie.
- [Capacità agentiche](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=it): esecuzione di codice, lettura di strumenti, annotazione di immagini.
- [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=it): attività a lungo termine con API dei robot personalizzate.
- [Robotica con streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it): streaming bidirezionale in tempo reale (solo Gemini Robotics ER 2).
- [Comprensione dei video](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=it): individuazione dei momenti e classificazione dei progressi (solo Gemini Robotics ER 2).
- [Sicurezza della robotica di Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=it): ricerca sulla sicurezza alla base della famiglia di modelli.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-21 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-21 UTC."],[],[]]
