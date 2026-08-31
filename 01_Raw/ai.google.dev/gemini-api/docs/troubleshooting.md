---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=it
fetched_at: 2026-08-31T06:32:27.827361+00:00
title: "Guida alla risoluzione dei problemi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida alla risoluzione dei problemi

Utilizza questa guida per diagnosticare e risolvere i problemi comuni che si verificano quando chiami l'API Gemini. Potresti riscontrare problemi con il servizio di backend dell'API Gemini o con gli SDK client. I nostri SDK client sono open source nei seguenti repository:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Se riscontri problemi con la chiave API, verifica di aver configurato
la tua chiave API correttamente seguendo la [guida alla configurazione della chiave API](https://ai.google.dev/gemini-api/docs/api-key?hl=it).

## Codici di errore del servizio di backend dell'API Gemini

Nella tabella che segue sono elencati i codici di errore di backend comuni che potresti riscontrare, insieme alle spiegazioni delle cause e ai passaggi per la risoluzione dei problemi:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Codice HTTP** | **Stato** | **Descrizione** | **Esempio** | **Soluzione** |
| 400 | INVALID\_ARGUMENT | Il corpo della richiesta non è in un formato corretto. | Nella richiesta è presente un errore di battitura o manca un campo obbligatorio. | Consulta il [riferimento dell'API](https://ai.google.dev/api?hl=it) per il formato della richiesta, gli esempi e le versioni supportate. L'utilizzo di funzionalità di una versione più recente dell'API con un endpoint precedente può causare errori. |
| 400 | FAILED\_PRECONDITION | Il livello senza costi dell'API Gemini non è disponibile nel tuo paese. Attiva la fatturazione per il tuo progetto in Google AI Studio. | Stai effettuando una richiesta in una regione in cui il livello senza costi non è supportato e non hai attivato la fatturazione per il tuo progetto in Google AI Studio. | Per utilizzare l'API Gemini, devi configurare un piano a pagamento utilizzando [Google AI Studio](https://aistudio.google.com/apikey?hl=it). |
| 403 | PERMISSION\_DENIED | La tua chiave API non dispone delle autorizzazioni richieste. | Stai utilizzando la chiave API errata; stai tentando di utilizzare un modello ottimizzato senza eseguire [l'autenticazione corretta](https://ai.google.dev/gemini-api/docs/model-tuning?hl=it). | Verifica che la chiave API sia impostata e disponga dell'accesso corretto. Assicurati di eseguire l'autenticazione corretta per utilizzare i modelli ottimizzati. |
| 404 | NOT\_FOUND | La risorsa richiesta non è stata trovata. | Non è stato trovato un file immagine, audio o video a cui si fa riferimento nella richiesta. | Verifica se tutti i [parametri della richiesta sono validi](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=it#check-api) per la tua versione dell'API. |
| 429 | RESOURCE\_EXHAUSTED | Hai superato uno dei limiti di frequenza dell'API (RPM, TPM, RPD, spesa e così via). | Stai inviando troppe richieste, utilizzando troppi token o superando i limiti basati sulla spesa per la cronologia di fatturazione e il livello del tuo account. | Verifica di rispettare i [limiti di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it) del modello. Attendi e riprova dopo un breve periodo. Riduci la frequenza o le dimensioni delle richieste. [Se necessario, richiedi un aumento del limite di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it#request-rate-limit-increase). |
| 499 | CANCELLED | L'operazione è stata annullata, in genere dal chiamante. | Il client ha chiuso la connessione prima che l'API potesse completare la risposta. | Verifica se la tua infrastruttura di rete o client chiude prematuramente la connessione (ad es. a causa di un timeout lato client). |
| 500 | INTERNAL | Si è verificato un errore imprevisto da parte di Google. | Il contesto di input è troppo lungo. | Controlla la [pagina di stato dell'API Gemini](https://aistudio.google.com/status?hl=it) per eventuali incidenti in corso. Riduci il contesto di input o passa temporaneamente a un altro modello (ad es. da Gemini 2.5 Pro a Gemini 2.5 Flash) e verifica se funziona. In alternativa, attendi un po' e riprova a inviare la richiesta. Se il problema persiste dopo aver riprovato, segnalalo utilizzando il pulsante **Invia feedback** in Google AI Studio. |
| 503 | UNAVAILABLE | Il servizio potrebbe essere temporaneamente sovraccarico o non disponibile. | Il servizio sta temporaneamente esaurendo la capacità. | Controlla la [pagina di stato dell'API Gemini](https://aistudio.google.com/status?hl=it) per eventuali incidenti in corso. Passa temporaneamente a un altro modello (ad es. da Gemini 2.5 Pro a Gemini 2.5 Flash) e verifica se funziona. In alternativa, attendi un po' e riprova a inviare la richiesta. Se il problema persiste dopo aver riprovato, segnalalo utilizzando il pulsante **Invia feedback** in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Il servizio non è in grado di completare l'elaborazione entro la scadenza. | Il prompt (o il contesto) è troppo grande per essere elaborato in tempo. | Imposta un "timeout" più lungo nella richiesta del client per evitare questo errore. |

## Strategia di ripetizione dei tentativi

Se ricevi un errore che indica che devi riprovare a inviare la richiesta (ad es. `429 RESOURCE_EXHAUSTED` o `503 UNAVAILABLE`), ti consigliamo di implementare una strategia di backoff esponenziale. Ciò significa che devi attendere un breve periodo di tempo prima del primo tentativo e poi aumentare gradualmente il tempo di attesa tra i tentativi successivi.

Gli SDK client ufficiali per l'API Gemini, come l'[SDK Python](https://github.com/googleapis/python-genai), includono per impostazione predefinita la logica di ripetizione automatica con backoff esponenziale per la gestione degli errori temporanei come timeout, problemi di rete e limiti di frequenza (codici di stato `429` e `5xx`). Ad esempio, l'SDK Python riprova automaticamente a inviare le richieste in caso di errori temporanei fino a quattro volte con un ritardo iniziale di circa 1 secondo e un ritardo massimo di 60 secondi.

Se stai effettuando richieste API REST dirette o personalizzando la logica di ripetizione dei tentativi, segui queste best practice per aumentare la probabilità di una richiesta riuscita ed evitare di sovraccaricare il servizio:

- **Utilizza il backoff esponenziale:** attendi un breve periodo di tempo prima del primo tentativo (ad esempio, 1 secondo), quindi aumenta il ritardo in modo esponenziale (ad esempio, 2 secondi, 4 secondi, 8 secondi).
- **Aggiungi jitter:** aggiungi un "jitter" casuale al ritardo per evitare che tutti i client riprovino esattamente nello stesso momento.
- **Riprova in caso di errori specifici:** riprova solo in caso di errori temporanei (come `429`, `408` o `5xx`). Non riprovare in caso di errori del client (come `400` o `403`), in quanto indicano problemi come chiavi API non valide o sintassi errata.
- **Imposta il numero massimo di tentativi:** definisci un numero massimo di tentativi per evitare loop infiniti.

## Controlla le chiamate API per verificare la presenza di errori nei parametri del modello

Verifica che i parametri del modello rientrino nei seguenti valori:

|  |  |
| --- | --- |
| **Parametro del modello** | **Valori (intervallo)** |
| Conteggio dei candidati | 1-8 (intero) |
| Temperatura | 0.0-1.0 |
| Numero massimo token di output | Utilizza la [pagina dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it) per determinare il numero massimo di token per il modello che stai utilizzando. |
| TopP | 0.0-1.0 |

Oltre a controllare i valori dei parametri, assicurati di utilizzare la versione dell'
[API](https://ai.google.dev/gemini-api/docs/api-versions?hl=it) corretta (ad es. `/v1` o `/v1beta`) e il
modello che supporta le funzionalità di cui hai bisogno. Ad esempio, se una funzionalità è in versione beta, sarà disponibile solo nella versione dell'API `/v1beta`.

## Verifica di avere il modello giusto

Verifica di utilizzare un modello supportato elencato nella nostra [pagina
dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

## Latenza o utilizzo dei token più elevati con i modelli 2.5

Se noti una latenza o un utilizzo dei token più elevati con i modelli 2.5 Flash e Pro, è possibile che sia perché la **funzionalità di ragionamento è attivata per impostazione predefinita** per migliorare la qualità. Se dai la priorità alla velocità o devi ridurre al minimo i costi, puoi modificare o disattivare la funzionalità di ragionamento.

Consulta la pagina relativa alla funzionalità di [ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it#set-budget) per
indicazioni e codice di esempio.

## Problemi di sicurezza

Se vedi che un prompt è stato bloccato a causa di un'impostazione di sicurezza nella chiamata API, esaminalo rispetto ai filtri impostati nella chiamata API.

Se vedi `BlockedReason.OTHER`, la query o la risposta potrebbero violare i [Termini
di servizio](https://ai.google.dev/terms?hl=it) o non essere supportate.

## Problema di citazione

Se vedi che il modello smette di generare output a causa del motivo RECITATION, significa che l'output del modello potrebbe assomigliare a determinati dati. Per risolvere il problema, prova a rendere il prompt / il contesto il più univoco possibile e utilizza una temperatura più elevata.

## Problema dei token ripetitivi

Se vedi token di output ripetuti, prova a seguire questi suggerimenti per ridurli o eliminarli.

| Descrizione | Causa | Soluzione alternativa suggerita |
| --- | --- | --- |
| Trattini ripetuti nelle tabelle Markdown | Questo può verificarsi quando i contenuti della tabella sono lunghi, in quanto il modello tenta di creare una tabella Markdown allineata visivamente. Tuttavia, l'allineamento in Markdown non è necessario per il rendering corretto. | Aggiungi istruzioni nel prompt per fornire al modello linee guida specifiche per la generazione di tabelle Markdown. Fornisci esempi che seguano queste linee guida. Puoi anche provare a regolare la temperatura. Per la generazione di codice o output molto strutturati come le tabelle Markdown, è stato dimostrato che le temperature elevate funzionano meglio (>= 0.8).  Di seguito è riportato un insieme di linee guida di esempio che puoi aggiungere al tuo prompt per evitare questo problema:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Token ripetuti nelle tabelle Markdown | Analogamente ai trattini ripetuti, questo si verifica quando il modello tenta di allineare visivamente i contenuti della tabella. L'allineamento in Markdown non è necessario per il rendering corretto. | - Prova ad aggiungere istruzioni come le seguenti al prompt di sistema:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Prova a regolare la temperatura. Le temperature più elevate (>= 0.8)   in genere aiutano a eliminare le ripetizioni o le duplicazioni nell'   output. |
| Nuovi righi ripetuti (`\n`) nell'output strutturato | Quando l'input del modello contiene sequenze di escape o Unicode come `\u` o `\t`, può portare a nuovi righi ripetuti. | - Cerca e sostituisci le sequenze di escape vietate con caratteri UTF-8   in your prompt. Ad esempio, la sequenza di escape `\u`   negli esempi JSON può fare in modo che il modello la utilizzi anche nell'output. - Indica al modello le sequenze di escape consentite. Aggiungi un'istruzione di sistema come   questa:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Testo ripetuto nell'utilizzo dell'output strutturato | Quando l'output del modello ha un ordine dei campi diverso dallo schema strutturato definito, può portare alla ripetizione del testo. | - Non specificare l'ordine dei campi nel prompt. - Rendi obbligatori tutti i campi di output. |
| Chiamata ripetitiva dello strumento | Questo può verificarsi se il modello perde il contesto dei pensieri precedenti e/o chiama un endpoint non disponibile a cui è costretto. | Indica al modello di mantenere lo stato all'interno del processo di ragionamento. Aggiungi quanto segue alla fine delle istruzioni di sistema:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Testo ripetitivo che non fa parte dell'output strutturato | Questo può verificarsi se il modello si blocca su una richiesta che non riesce a risolvere. | - Se la funzionalità di ragionamento è attivata, evita di dare ordini espliciti su come   pensare a un problema nelle istruzioni. Chiedi solo l'output finale. - Prova con una temperatura più elevata >= 0.8. - Aggiungi istruzioni come "Sii conciso", "Non ripeterti" o   "Fornisci la risposta una sola volta". |

## Chiavi API bloccate o non funzionanti

Questa sezione descrive come verificare se la chiave API Gemini è bloccata e cosa fare in merito.

### Informazioni sul motivo per cui le chiavi vengono bloccate

Abbiamo identificato una vulnerabilità per cui alcune chiavi API potrebbero essere state esposte pubblicamente. Per proteggere i tuoi dati e impedire accessi non autorizzati, abbiamo bloccato in modo proattivo l'accesso all'API Gemini per queste chiavi di cui è nota la compromissione.

### Verifica se le tue chiavi sono interessate

Se è noto che la tua chiave è stata compromessa, non puoi più utilizzarla con l'API Gemini. Puoi utilizzare [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=it) per verificare se l'accesso all'API Gemini è bloccato per una delle
tue chiavi API e generare nuove
chiavi. Quando tenti di utilizzare queste chiavi, potresti anche visualizzare il seguente errore:

```
Your API key was reported as leaked. Please use another API key.
```

### Azioni per le chiavi API bloccate

Devi generare nuove chiavi API per le integrazioni dell'API Gemini utilizzando [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=it). Ti consigliamo vivamente di esaminare le tue pratiche di gestione delle chiavi API per assicurarti che le nuove chiavi siano protette e non esposte pubblicamente.

### Addebiti imprevisti dovuti a vulnerabilità

[Invia una richiesta di assistenza per la fatturazione](https://console.cloud.google.com/support/chat?hl=it).
Il nostro team di fatturazione sta lavorando al problema e ti comunicheremo gli aggiornamenti il prima possibile.

### Misure di sicurezza di Google per le chiavi compromesse

**In che modo Google mi aiuterà a proteggere il mio account da sforamenti di costi e comportamenti illeciti se le mie chiavi API vengono compromesse?**

- Stiamo passando all'emissione di chiavi API quando richiedi una nuova chiave utilizzando
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=it) che per impostazione predefinita sarà
  limitata solo a Google AI Studio e non accetterà chiavi di altri servizi.
  In questo modo si eviterà l'utilizzo involontario di chiavi incrociate.
- Per impostazione predefinita, blocchiamo le chiavi API compromesse e utilizzate con l'API Gemini, contribuendo a prevenire comportamenti illeciti relativi ai costi e ai dati delle applicazioni.
- Potrai trovare lo stato delle tue chiavi API in [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=it) e lavoreremo per comunicare
  in modo proattivo quando identifichiamo le tue chiavi API compromesse per un'azione immediata.

## Migliorare l'output del modello

Per ottenere output del modello di qualità superiore, prova a scrivere prompt più strutturati. La
[pagina della guida all'ingegneria del prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it)
introduce alcuni concetti di base, strategie e best practice per iniziare.

## Informazioni sui limiti dei token

Leggi la nostra [guida ai token](https://ai.google.dev/gemini-api/docs/tokens?hl=it) per comprendere meglio come
contarli e quali sono i limiti.

## Problemi noti

- L'API supporta solo un numero limitato di lingue. L'invio di prompt in lingue non supportate può produrre risposte impreviste o persino bloccate. Per gli aggiornamenti, consulta le
  [lingue disponibili](https://ai.google.dev/gemini-api/docs/models?hl=it#supported-languages) per
  aggiornamenti.

## Segnala un bug

Se hai domande, partecipa alla discussione sul
[forum per sviluppatori di Google AI](https://discuss.ai.google.dev?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-08 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-08 UTC."],[],[]]
