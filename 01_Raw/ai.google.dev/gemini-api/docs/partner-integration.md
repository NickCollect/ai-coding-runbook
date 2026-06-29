---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=it
fetched_at: 2026-06-29T05:32:07.445134+00:00
title: "Integrazioni con partner e biblioteche \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Integrazioni con partner e biblioteche

Questa guida illustra le strategie di architettura per la creazione di librerie, piattaforme e gateway basati sull'API Gemini. Descrive in dettaglio i compromessi tecnici tra l'utilizzo degli SDK GenAI ufficiali, dell'API diretta (REST/gRPC) e del livello di compatibilità OpenAI.

Utilizza questa guida se stai creando strumenti per altri sviluppatori, come framework open source, gateway aziendali o aggregatori SaaS, e devi ottimizzare l'igiene delle dipendenze, le dimensioni del bundle o la parità delle funzionalità.

## Che cos'è l'integrazione dei partner?

Un partner è chiunque crei un'integrazione tra l'API Gemini e gli sviluppatori di utenti finali. Classifichiamo i partner in quattro archetipi. Identificare quello che ti corrisponde maggiormente ti aiuterà a scegliere il percorso di integrazione giusto.

#### Framework dell'ecosistema

- **Chi sei:** gestore di un framework open source (ad es. LangChain, LlamaIndex, Spring AI) o di client specifici per la lingua.
- **Il tuo obiettivo:** ampia compatibilità. Vuoi che la tua libreria funzioni in qualsiasi ambiente scelto dall'utente senza forzare conflitti.

#### Piattaforma di runtime ed edge

- **Chi sei:** piattaforme SaaS, gateway AI o provider di infrastrutture cloud (ad es. Vercel, Cloudflare, Zapier) in cui l'esecuzione del codice avviene in ambienti con limitazioni.
- **Il tuo obiettivo:** rendimento. Hai bisogno di una bassa latenza, dimensioni minime del bundle e avvii a freddo rapidi.

#### Aggregatore

- **Chi sei:** piattaforme, proxy o "Model Garden" interni che normalizzano l'accesso a molti provider LLM diversi (ad es. OpenAI, Anthropic, Google) in un'unica interfaccia.
- **Il tuo obiettivo:** portabilità e uniformità.

#### Gateway aziendale

- **Chi sei:** team di ingegneria delle piattaforme interne di grandi aziende che creano "percorsi consigliati" per centinaia di sviluppatori interni.
- **Il tuo obiettivo:** standardizzazione, governance e autenticazione unificata.

## Confronto riepilogativo

**Best practice globale:** tutti i partner devono inviare l'[`x-goog-api-client`
intestazione](#client-id) indipendentemente dal percorso scelto.

| Se sei... | Percorso consigliato | Vantaggio principale | Compromesso principale | Best practice |
| --- | --- | --- | --- | --- |
| **Gateway aziendale, framework dell'ecosistema** | **[SDK Google GenAI](#genai-sdk)** | **Parità e velocità di Gemini Enterprise Agent Platform.** Gestione integrata per tipi, autenticazione e funzionalità complesse (ad es. caricamenti di file). Migrazione senza problemi a Google Cloud. | **Peso delle dipendenze.** Le dipendenze transitive possono essere complesse e al di fuori del tuo controllo. Limitato alle lingue supportate (Python/Node/Go/Java). | **Blocca le versioni.** Fissa le versioni dell'SDK nelle immagini di base interne per garantire la stabilità tra i team. |
| **Framework dell'ecosistema, piattaforme edge e aggregatori** | **[API diretta](#rest)**  *(REST / gRPC)* | **Nessuna dipendenza.** Controlli il client HTTP e le dimensioni esatte del bundle. Accesso completo a tutte le funzionalità dell'API e del modello. | **Elevato overhead per gli sviluppatori.** Le strutture JSON possono essere nidificate in profondità e richiedono una rigorosa convalida manuale e un controllo dei tipi. | **Utilizza le specifiche OpenAPI.** Automatizza la generazione dei tipi utilizzando le nostre specifiche ufficiali anziché scriverle a mano. |
| **Aggregatore che utilizza gli SDK OpenAI che richiedono solo workflow basati su testo**  *(Ottimizzazione per la portabilità legacy)* | **[Compatibilità OpenAI](#openai)** | **Portabilità immediata.** Riutilizza il codice o le librerie esistenti compatibili con OpenAI. | **Limite di funzionalità.** Le funzionalità specifiche del modello (video nativo, memorizzazione nella cache) potrebbero non essere disponibili. | **Piano di migrazione.** Utilizza questo piano per una convalida rapida, ma pianifica l'upgrade all'API diretta per la funzionalità completa dell'API. |

## Integrazione dell'SDK Google GenAI

Per i framework, l'implementazione dell'[SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=it)
è spesso il percorso più semplice, dato che richiede il minor numero di righe di codice nelle lingue supportate.

Per i team di piattaforme interne, il risultato principale è spesso un "percorso consigliato" che consente agli ingegneri di prodotto di muoversi rapidamente rispettando le norme di sicurezza.

**Vantaggi:**

- **Interfaccia unificata per la migrazione della piattaforma agentica Gemini Enterprise:** gli sviluppatori interni spesso creano prototipi utilizzando le chiavi API (API Gemini) ed eseguono il deployment sulla piattaforma agentica Gemini Enterprise (IAM) per la conformità alla produzione. L'SDK astrae queste differenze di autenticazione.
  Allo stesso modo, per i framework puoi implementare un percorso di codice e supportare due gruppi di utenti.
- **Helper lato client:** l'SDK include utilità idiomatiche che riducono il codice boilerplate per le attività complesse.
  - *Esempi:* supporto degli oggetti immagine `PIL` direttamente negli inviti all'azione, chiamata di funzione automatica e tipi completi.
- **Accesso alle funzionalità del giorno zero:** le nuove funzionalità dell'API sono disponibili al momento del lancio tramite gli SDK.
- **Supporto migliorato per la generazione di codice:** l'installazione dell'SDK locale espone le definizioni dei tipi e le stringhe di documentazione agli assistenti di codifica (ad es. Cursor, Copilot).
  Questo contesto migliora l'accuratezza della generazione del codice rispetto alla generazione di richieste REST non elaborate.

**Il compromesso:**

- **Peso e complessità delle dipendenze:** gli SDK hanno le proprie dipendenze, che possono aumentare le dimensioni del bundle e potenzialmente il rischio della supply chain.
- **Controllo delle versioni:** le nuove funzionalità dell'API sono spesso associate alle versioni minime dell'SDK.
  Potresti dover inviare aggiornamenti agli utenti per accedere a nuove funzionalità o modelli, il che in alcuni casi potrebbe richiedere modifiche nelle dipendenze transitive che interessano i tuoi utenti.
- **Limiti di protocollo:** gli SDK supportano solo HTTPS per l'API principale e WebSocket (WSS) per l'API Live. gRPC non è supportato utilizzando i client SDK di alto livello.
- **Supporto linguistico:** gli SDK supportano le versioni linguistiche *correnti*. Se devi supportare le versioni EOL (ad es. Python 3.9), dovrai gestire un fork.

**Best practice:**

- **Blocca le versioni:** fissa la versione dell'SDK nelle immagini di base interne per garantire la stabilità tra i team.

## Integrazione dell'API diretta

Se stai distribuendo una libreria a migliaia di sviluppatori, eseguendo in un ambiente con limitazioni o creando un aggregatore che richiede le funzionalità all'avanguardia di Gemini, potresti dover integrare l'API direttamente utilizzando REST o gRPC.

**Vantaggi:**

- **Accesso completo alle funzionalità:** a differenza del livello di compatibilità OpenAI, l'utilizzo diretto dell'API consente di utilizzare funzionalità specifiche di Gemini, come il caricamento nell'API File, la creazione della memorizzazione nella cache dei contenuti e l'utilizzo dell'API Live bidirezionale.
- **Dipendenze minime:** in un ambiente in cui le dipendenze sono sensibili a causa delle dimensioni o dei costi di audit. L'utilizzo diretto dell'API tramite una libreria standard come `fetch` o tramite un wrapper come `httpx` garantisce che la libreria rimanga leggera.
- **Indipendente dalla lingua:** questo è l'unico percorso per le lingue non coperte dagli SDK, come Rust, PHP e Ruby, poiché non esistono limitazioni linguistiche.
- **Rendimento:** l'API diretta non ha overhead di inizializzazione, il che riduce al minimo gli avvii a freddo nelle funzioni serverless.

**Il compromesso:**

- **Implementazione manuale della piattaforma agentica Gemini Enterprise:** a differenza dell'SDK, l'utilizzo diretto dell'API non gestisce automaticamente le differenze di autenticazione tra AI Studio (chiave API) e la piattaforma agentica Gemini Enterprise (IAM). Se vuoi supportare entrambi gli ambienti, devi implementare gestori di autenticazione separati.
- **Nessun tipo o helper nativo:** non ricevi completamenti di codice o controlli in fase di compilazione per gli oggetti di richiesta, a meno che non li implementi tu. Non esistono "helper" client (ad es. convertitori da funzione a schema), quindi devi scrivere manualmente questa logica.

**Best practice**

Esporiamo una specifica leggibile dalla macchina che puoi utilizzare per generare definizioni di tipi per la tua libreria, evitando di scriverle a mano. Scarica la specifica durante il processo di compilazione, genera i tipi e distribuisci il codice compilato.

- **Endpoint:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integrazione dell'SDK OpenAI

Se sei una piattaforma che dà la priorità a uno schema unificato (OpenAI Chat Completions) rispetto alle funzionalità specifiche del modello, questo è il percorso più veloce.

**Vantaggi:**

- **Basso attrito:** spesso puoi aggiungere il supporto di Gemini modificando `baseURL` e `apiKey`. Questo è un modo rapido per integrare le implementazioni "Bring Your Own Key", aggiungendo il supporto di Gemini senza scrivere nuovo codice.
- **Vincoli:** questo percorso è consigliato solo se sei limitato all'SDK OpenAI e non hai bisogno di funzionalità avanzate di Gemini come l'API File o l'aggiunta manuale del supporto per strumenti come Grounding con la Ricerca Google.

**Il compromesso:**

- **Limitazioni delle funzionalità:** il livello di compatibilità fornisce limitazioni alle funzionalità principali di Gemini. Gli strumenti lato server disponibili variano a seconda delle piattaforme e potrebbero richiedere una gestione manuale per funzionare con gli strumenti dell'API Gemini.
- **Overhead di traduzione:** poiché lo schema OpenAI non esegue il mapping 1:1 all'architettura di Gemini, l'utilizzo del livello di compatibilità introduce alcune complessità che richiedono un lavoro di implementazione aggiuntivo per essere risolte, ad esempio il mapping di uno strumento di "ricerca" utente allo strumento della piattaforma corretta.
  Se hai bisogno di una quantità significativa di casi speciali, potrebbe essere più utile utilizzare un SDK o un'API dedicati per ogni piattaforma.

**Best practice**

Se possibile, esegui l'integrazione direttamente con l'API Gemini. Tuttavia, per la massima compatibilità, valuta la possibilità di utilizzare una libreria che riconosca i diversi provider e possa gestire il mapping di strumenti e messaggi.

## Best practice per tutti i partner: identificazione del client

Quando effettui chiamate all'API Gemini come piattaforma o libreria, devi identificare il tuo client utilizzando l'intestazione `x-goog-api-client`.

In questo modo, Google può identificare i segmenti di traffico specifici e, se la tua libreria produce un pattern di errore specifico, possiamo contattarti per aiutarti a eseguire il debug.

Utilizza il formato `company-product/version` (ad es. `acme-framework/1.2.0`).

### Esempi di implementazione

### SDK GenAI

Fornendo il client API, l'SDK aggiunge automaticamente l'intestazione personalizzata alle intestazioni interne.

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

### API diretta (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### SDK OpenAI

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

## Passaggi successivi

- Visita la [panoramica della libreria](https://ai.google.dev/gemini-api/docs/libraries?hl=it) per scoprire di più su
  gli SDK GenAI
- Sfoglia il [riferimento API](https://ai.google.dev/api?hl=it)
- Leggi la [guida alla compatibilità con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-22 UTC."],[],[]]
