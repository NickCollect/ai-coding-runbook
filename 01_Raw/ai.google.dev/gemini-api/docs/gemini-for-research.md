---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=it
fetched_at: 2026-07-20T04:43:51.797515+00:00
title: "Accelera la scoperta con Gemini per la ricerca \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)

# Accelera la scoperta con Gemini per la ricerca

[Ottenere una chiave API Gemini](https://aistudio.google.com/apikey?hl=it)

I modelli Gemini possono essere utilizzati per far progredire la ricerca di base in tutte le discipline.
Ecco alcuni modi in cui puoi esplorare Gemini per la tua ricerca:

- **Analizzare e controllare gli output del modello**: per un'analisi più approfondita, puoi esaminare un
  candidato di risposta generato dal modello utilizzando strumenti come
  `CitationMetadata`. Puoi anche configurare le opzioni per la generazione e gli output del modello, ad esempio `responseSchema`, `topP` e `topK`. [Scopri di più](https://ai.google.dev/api/generate-content?hl=it).
- **Input multimodali**: Gemini può elaborare immagini, audio e video, consentendo una
  moltitudine di entusiasmanti direzioni di ricerca. [Scopri di più](https://ai.google.dev/gemini-api/docs/vision?hl=it).
- **Funzionalità di contesto lungo**: Gemini 3.0 Flash e Pro sono dotati di una finestra contestuale da 1 milione di token. [Scopri di più](https://ai.google.dev/gemini-api/docs/long-context?hl=it).
- **Grow with Google**: accedi rapidamente ai modelli Gemini tramite l'API e Google AI Studio per i casi d'uso di produzione. Se stai cercando una piattaforma basata su Google Cloud, Gemini Enterprise Agent Platform può fornire un'infrastruttura di supporto aggiuntiva.

Per supportare la ricerca accademica e promuovere la ricerca all'avanguardia, Google fornisce
l'accesso ai crediti dell'API Gemini per scienziati e ricercatori accademici tramite il
[programma accademico Gemini](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=it#gemini-academic-program).

## Inizia a utilizzare Gemini

L'API Gemini e Google AI Studio ti aiutano a iniziare a lavorare con i modelli più recenti di Google e a trasformare le tue idee in applicazioni scalabili.

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

## Accademici in primo piano

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=it)

"La nostra ricerca esamina Gemini come modello linguistico visivo (VLM) e i suoi comportamenti agentici in diversi ambienti dal punto di vista della robustezza e della sicurezza. Finora abbiamo valutato la robustezza di Gemini rispetto a distrazioni come le finestre popup quando gli agenti VLM eseguono attività del computer e abbiamo sfruttato Gemini per analizzare l'interazione sociale, gli eventi temporali e i fattori di rischio in base all'input video."

[Sito web di Diyi Yang](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=it)

"Gemini Pro e Flash, con la loro lunga finestra contestuale, ci hanno aiutato in OK-Robot, il nostro progetto di manipolazione mobile a vocabolario aperto. Gemini consente query e comandi complessi in linguaggio naturale sulla "memoria" del robot: in questo caso, le osservazioni precedenti effettuate dal robot durante una lunga durata di funzionamento. Io e Mahi Shafiullah utilizziamo anche Gemini per scomporre le attività in codice che il robot può eseguire nel mondo reale."

[Sito web di Lerrel Pinto](https://www.lerrelpinto.com/)

## Programma accademico Gemini

I ricercatori accademici qualificati (come docenti, personale e studenti di dottorato) nei [paesi
supportati](https://ai.google.dev/gemini-api/docs/available-regions?hl=it) possono richiedere di ricevere crediti dell'API Gemini
e limiti di frequenza più elevati per i progetti di ricerca. Questo supporto consente una maggiore velocità effettiva per gli esperimenti scientifici e fa progredire la ricerca.

Siamo particolarmente interessati alle aree di ricerca nella sezione seguente, ma accettiamo candidature da diverse discipline scientifiche:

- **Valutazioni e benchmark**: metodi di valutazione approvati dalla community che
  possono fornire un forte segnale di rendimento in aree come factualità, sicurezza,
  rispetto delle istruzioni, ragionamento e pianificazione.
- **Accelerare la scoperta scientifica a vantaggio dell'umanità**: potenziali
  applicazioni dell'AI nella ricerca scientifica interdisciplinare, incluse aree
  come malattie rare e trascurate, biologia sperimentale, scienza dei materiali
  e sostenibilità.
- **Incorporazione e interazioni**: utilizzo di modelli linguistici di grandi dimensioni per
  studiare nuove interazioni nei campi dell'AI incorporata, delle interazioni ambientali,
  della robotica e dell'interazione uomo-computer.
- **Funzionalità emergenti**: esplorazione di nuove capacità agentiche necessarie per
  migliorare il ragionamento e la pianificazione e di come le funzionalità possono essere ampliate durante
  l'inferenza (ad es. utilizzando Gemini Flash).
- **Interazione e comprensione multimodali**: identificazione di lacune e
  opportunità per i modelli di base multimodali per l'analisi, il ragionamento,
  e la pianificazione in una varietà di attività.

Idoneità: possono presentare domanda solo le persone (docenti, ricercatori o equivalenti) affiliate a un istituto accademico valido o a un'organizzazione di ricerca accademica. Tieni presente che l'accesso all'API e i crediti verranno concessi e rimossi a discrezione di Google. Esaminiamo le domande su base mensile.

### Inizia la ricerca con l'API Gemini

[Richiedi ora](https://forms.gle/HMviQstU8PxC5iCt5)

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-01 UTC.

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-01 UTC."],[],[]]
