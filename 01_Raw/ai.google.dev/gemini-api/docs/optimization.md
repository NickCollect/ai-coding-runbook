---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=it
fetched_at: 2026-05-05T13:10:22.084803+00:00
title: "Inferenza e ottimizzazione dell'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

- [Home page](https://ai.google.dev/gemini-api/docs/Home page)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documenti](https://ai.google.dev/gemini-api/docs/Documenti)

Invia feedback

# Inferenza e ottimizzazione dell'API Gemini

L'API Gemini offre una serie di meccanismi di ottimizzazione per aiutarti a bilanciare velocità, costi e affidabilità in base alle esigenze specifiche del tuo carico di lavoro.
Che tu stia creando bot conversazionali in tempo reale o eseguendo pipeline di elaborazione dei dati offline pesanti, la scelta del paradigma giusto può ridurre significativamente i costi o migliorare il rendimento.

| Funzionalità | Standard | Flex | Priorità | Batch | Memorizzazione nella cache |
| --- | --- | --- | --- | --- | --- |
| **Prezzi** | Prezzo pieno | Sconto del 50% | Dal 75% al 100% in più rispetto allo standard | Sconto del 50% | Sconto del 90% + spazio di archiviazione dei token ripartito proporzionalmente |
| **Latenza** | Da secondi a minuti | Minuti (target 1-15 min) | Secondi | Fino a 24 ore | Time to first token più rapido |
| **Affidabilità** | Alta / medio-alta | Best effort (rimovibile) | Alta (non rimovibile) | Alta (per il throughput) | N/D |
| **Interfaccia** | Sincrona | Sincrona | Sincrona | Asincrona | Stato salvato |
| **Caso d'uso ideale** | Workflow di applicazioni generiche | Catene sequenziali non urgenti | App di produzione rivolte agli utenti | Set di dati di grandi dimensioni, valutazioni offline | Query ricorrenti sullo stesso file |

## Livelli di servizio di inferenza (sincroni)

Puoi passare dal traffico sincrono ottimizzato per l'affidabilità a quello ottimizzato per i costi passando il parametro `service_tier` nelle chiamate di generazione standard.

### Inferenza standard (valore predefinito)

Il livello standard è l'opzione predefinita per la generazione di contenuti sequenziali.
Fornisce tempi di risposta normali senza costi aggiuntivi o code pesanti.

- **Affidabilità:** criticità standard
- **Prezzo:** prezzi standard.
- **Ideale per:** la maggior parte delle applicazioni interattive quotidiane.

### Inferenza con priorità (ottimizzata per la latenza)

[L'elaborazione con priorità](https://ai.google.dev/gemini-api/docs/L'elaborazione con priorità) indirizza le richieste
alle code di calcolo ad alta criticità.
Questo traffico è strettamente non rimovibile (non viene mai sostituito da altri livelli) e offre la massima affidabilità. Se superi i limiti di priorità dinamici, il sistema esegue il downgrade della richiesta all'elaborazione standard anziché generare un errore.

- **Affidabilità:** massima criticità
- **Prezzo:** dal 75% al 100% in più rispetto alle tariffe standard.
- **Ideale per:** chatbot per clienti, rilevamento delle frodi in tempo reale e copiloti mission-critical.

### Inferenza flessibile (ottimizzata per i costi)

[L'inferenza flessibile](https://ai.google.dev/gemini-api/docs/L'inferenza flessibile) offre uno sconto del 50% rispetto alle tariffe standard utilizzando la capacità di calcolo
opportunistica fuori orario di punta. Le richieste vengono elaborate in modo sincrono, il che significa che non devi riscrivere il codice per gestire gli oggetti batch.
Poiché si tratta di traffico "rimovibile", le richieste potrebbero essere sostituite se il sistema registra picchi di traffico standard.

- **Affidabilità:** criticità non garantita e rimovibile
- **Prezzo:** 50% del prezzo standard (fatturato per token).
- **Ideale per:** workflow agentici multi-step in cui la chiamata N+1 dipende dall'output della chiamata N, aggiornamenti CRM in background e valutazioni offline.

## API Batch (bulk, asincrona)

[L'API Batch](https://ai.google.dev/gemini-api/docs/L'API Batch) è progettata per elaborare grandi volumi
di richieste in modo asincrono al
50% del costo standard. Puoi inviare le richieste come dizionari in linea o utilizzando un file di input JSONL (fino a 2 GB). Elabora le richieste utilizzando le code di throughput in background con un tempo di risposta target di 24 ore.

- **Affidabilità:** rimovibile, ma con tentativi automatici e sistema di accodamento di 24 ore
- **Prezzo:** 50% del prezzo standard.
- **Ideale per:** pre-elaborazione di set di dati di grandi dimensioni, esecuzione di suite di test di regressione periodici e generazione di immagini o incorporamenti di grandi dimensioni.

## Memorizzazione nella cache del contesto (risparmio di input)

[La memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/La memorizzazione nella cache del contesto) viene utilizzata quando un contesto iniziale sostanziale
viene referenziato ripetutamente da richieste più brevi.

- **Memorizzazione nella cache implicita:** attivata automaticamente sui modelli Gemini 2.5 e versioni successive.
  Il sistema trasferisce i risparmi sui costi se la richiesta raggiunge le cache esistenti in base ai prefissi di prompt comuni.
- **Memorizzazione nella cache esplicita:** puoi creare manualmente un oggetto cache con un TTL (Time-To-Live) specifico. Una volta creati, fai riferimento ai token memorizzati nella cache per le richieste successive per evitare di passare ripetutamente lo stesso payload del corpus.
- **Prezzo:** fatturato in base al conteggio dei token della cache e alla durata di archiviazione (TTL).
- **Ideale per:** chatbot con istruzioni di sistema estese, analisi ripetitive di file video lunghi o query su set di documenti di grandi dimensioni.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/licenza Creative Commons Attribution 4.0), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://ai.google.dev/gemini-api/docs/licenza Apache 2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://ai.google.dev/gemini-api/docs/norme del sito di Google Developers). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?
