---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=it
fetched_at: 2026-10-12T07:09:36.724238+00:00
title: "Guida alla risoluzione dei problemi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida alla risoluzione dei problemi

Utilizza questa guida per diagnosticare e risolvere i problemi comuni che si verificano quando
chiami l'API Gemini. Potresti riscontrare problemi con il servizio di backend dell'API Gemini o con gli SDK client. I nostri SDK client sono
open source nei seguenti repository:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Se riscontri problemi con la chiave API, verifica di averla configurata
correttamente seguendo la [guida alla configurazione della chiave API](https://ai.google.dev/gemini-api/docs/api-key?hl=it).

## Codici di errore

Per un riferimento completo a tutti i codici di errore, inclusi i codici di stato HTTP, i codici di generazione bloccata e i codici di errore dei contenuti, consulta la pagina [Errori API](https://ai.google.dev/gemini-api/docs/api-errors?hl=it).

## Strategia di ripetizione dei tentativi

Se ricevi un errore che indica che devi riprovare a inviare la richiesta (ad esempio `429 RESOURCE_EXHAUSTED` o `503 UNAVAILABLE`), ti consigliamo di implementare una strategia di backoff esponenziale. Ciò significa che attenderai un breve periodo di tempo prima del primo tentativo e poi aumenterai gradualmente il tempo di attesa tra i tentativi successivi.

Gli SDK client ufficiali per l'API Gemini, come l'[SDK Python](https://github.com/googleapis/python-genai), includono per impostazione predefinita la logica di ripetizione automatica con backoff esponenziale per la gestione di errori temporanei come timeout, problemi di rete e limiti di frequenza (codici di stato `429` e `5xx`). Ad esempio, l'SDK Python ritenta automaticamente gli errori temporanei fino a quattro volte con un ritardo iniziale di circa 1 secondo e un ritardo massimo di 60 secondi.

Se effettui richieste API REST dirette o personalizzi la logica di ripetizione dei tentativi, segui queste best practice per aumentare la probabilità di una richiesta riuscita ed evitare di sovraccaricare il servizio:

- **Utilizza il backoff esponenziale**:attendi un breve periodo di tempo prima del primo nuovo tentativo (ad esempio, 1 secondo), quindi aumenta il ritardo in modo esponenziale (ad esempio, 2 secondi, 4 secondi, 8 secondi).
- **Aggiungi jitter**:aggiungi un "jitter" casuale al ritardo per evitare che tutti i client riprovino contemporaneamente.
- **Riprova in caso di errori specifici**:riprova solo in caso di errori temporanei (come `429`, `408` o `5xx`). Non riprovare in caso di errori del client (come `400`, `402` o `403`), in quanto indicano problemi come chiavi API non valide, crediti prepagati esauriti o sintassi errata.
- **Imposta il numero massimo di tentativi**:definisci un numero massimo di tentativi per evitare loop infiniti.

## Controllare le chiamate API per errori nei parametri del modello

Verifica che i parametri del modello rientrino nei seguenti valori:

|  |  |
| --- | --- |
| **Parametro modello** | **Valori (intervallo)** |
| Numero di candidati | 1-8 (numero intero) |
| Temperatura | 0-1 |
| Numero massimo di token di output | Utilizza la [pagina dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it) per determinare il numero massimo di token per il modello che stai utilizzando. |
| TopP | 0-1 |

Oltre a controllare i valori dei parametri, assicurati di utilizzare la [versione dell'API](https://ai.google.dev/gemini-api/docs/api-versions?hl=it) corretta (ad es. `/v1` o `/v1beta`) e il modello che supporta le funzionalità di cui hai bisogno. Ad esempio, se una funzionalità è in versione beta, sarà disponibile solo nella versione `/v1beta` dell'API.

## Controllare di avere il modello giusto

Verifica di utilizzare un modello supportato elencato nella nostra [pagina dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

## Latenza o utilizzo dei token più elevati con i modelli di pensiero

Una latenza o un utilizzo di token più elevati si verificano spesso perché i modelli Gemini 3.x hanno
la funzionalità di pensiero abilitata per impostazione predefinita. I modelli Gemini 2.5 ritirati utilizzano anche la
funzione di pensiero predefinita.

I modelli pensanti generano token di ragionamento interni per migliorare la qualità. Questo
processo di ragionamento aumenta sia la latenza della risposta che il consumo totale di token.

Se dai la priorità a una latenza inferiore o devi ridurre al minimo i costi, puoi diminuire il
livello di pensiero o disattivare il pensiero.

Per dettagli sulla configurazione ed esempi di codice, consulta la
[guida alla pianificazione](https://ai.google.dev/gemini-api/docs/thinking?hl=it#thinking-levels).

## Problemi di sicurezza

Se viene visualizzato un prompt bloccato a causa di un'impostazione di sicurezza nella chiamata API,
esamina il prompt rispetto ai filtri impostati nella chiamata API.

Se visualizzi `BlockedReason.OTHER`, la query o la risposta potrebbe violare i [Termini di servizio](https://ai.google.dev/terms?hl=it) o non essere supportata.

## Problema di citazione

Se vedi che il modello smette di generare output a causa del motivo RECITAZIONE, significa che l'output del modello potrebbe assomigliare a determinati dati. Per risolvere il problema, prova a rendere
il prompt / il contesto il più unico possibile e utilizza una temperatura più elevata.

## Problema con i token ripetitivi

Se visualizzi token di output ripetuti, prova i seguenti suggerimenti per
ridurli o eliminarli.

| Descrizione | Causa | Soluzione alternativa suggerita |
| --- | --- | --- |
| Trattini ripetuti nelle tabelle Markdown | Ciò può verificarsi quando i contenuti della tabella sono lunghi perché il modello tenta di creare una tabella Markdown allineata visivamente. Tuttavia, l'allineamento in Markdown non è necessario per il rendering corretto. | Aggiungi istruzioni nel prompt per fornire al modello linee guida specifiche per la generazione di tabelle Markdown. Fornisci esempi che seguano queste linee guida. Puoi anche provare a regolare la temperatura. Per generare codice o output molto strutturato come tabelle Markdown, è stato dimostrato che una temperatura elevata funziona meglio (>= 0,8).  Di seguito è riportato un esempio di linee guida che puoi aggiungere al prompt per evitare questo problema:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Token ripetuti nelle tabelle Markdown | Come per i trattini ripetuti, ciò si verifica quando il modello tenta di allineare visivamente i contenuti della tabella. L'allineamento in Markdown non è obbligatorio per il rendering corretto. | - Prova ad aggiungere istruzioni come le seguenti al prompt di sistema:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Prova a regolare la temperatura. Temperature più alte (>= 0,8)   generalmente aiutano a eliminare ripetizioni o duplicazioni   nell'output. |
| Nuove righe ripetute (`\n`) nell'output strutturato | Quando l'input del modello contiene sequenze di escape o Unicode come `\u` o `\t`, possono verificarsi interruzioni di riga ripetute. | - Controlla e sostituisci le sequenze di escape vietate con caratteri UTF-8 nel prompt. Ad esempio, la sequenza di escape `\u` negli esempi JSON può indurre il modello a utilizzarla anche nel suo output. - Fornisci al modello le sequenze di escape consentite. Aggiungi un'istruzione di sistema come   questa:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Testo ripetuto nell'utilizzo dell'output strutturato | Se l'output del modello ha un ordine diverso per i campi rispetto allo schema strutturato definito, ciò può comportare la ripetizione del testo. | - Non specificare l'ordine dei campi nel prompt. - Rendi obbligatori tutti i campi di output. |
| Chiamate allo strumento ripetitive | Ciò può verificarsi se il modello perde il contesto dei pensieri precedenti e/o chiama un endpoint non disponibile a cui è costretto. | Chiedi al modello di mantenere lo stato durante il processo di pensiero. Aggiungi questo testo alla fine delle istruzioni di sistema:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Testo ripetitivo che non fa parte dell'output strutturato | Ciò può verificarsi se il modello si blocca su una richiesta che non riesce a risolvere. | - Se la funzionalità di pensiero è attiva, evita di dare istruzioni esplicite su come   affrontare un problema. Ti basta chiedere l'output   finale. - Prova una temperatura più alta >= 0,8. - Aggiungi istruzioni come "Sii conciso", "Non ripeterti" o   "Fornisci la risposta una sola volta". |

## Chiavi API bloccate o non funzionanti

Questa sezione descrive come verificare se la chiave API Gemini è bloccata
e cosa fare al riguardo.

### Perché le chiavi vengono bloccate

Abbiamo identificato una vulnerabilità per cui alcune chiavi API potrebbero essere state esposte pubblicamente. Per proteggere i tuoi dati e impedire accessi non autorizzati, abbiamo
bloccato in modo proattivo l'accesso all'API Gemini di queste chiavi di cui è stata accertata la compromissione.

### Conferma se le tue chiavi sono interessate

Se è noto che la tua chiave è stata compromessa, non puoi più utilizzarla con l'API Gemini. Puoi utilizzare [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=it) per verificare se
qualcuna delle tue chiavi API è bloccata per la chiamata all'API Gemini e generare nuove
chiavi. Quando tenti di utilizzare queste chiavi, potresti visualizzare anche il seguente errore:

```
Your API key was reported as leaked. Please use another API key.
```

### Azione per le chiavi API bloccate

Devi generare nuove chiavi API per le tue integrazioni dell'API Gemini utilizzando [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=it). Ti consigliamo vivamente di rivedere le tue pratiche di gestione delle chiavi API per assicurarti che le nuove chiavi siano protette e non siano esposte pubblicamente.

### Addebiti imprevisti dovuti a vulnerabilità

[Invia una richiesta di assistenza per la fatturazione](https://console.cloud.google.com/support/chat?hl=it).
Il nostro team di fatturazione sta lavorando alla questione e ti comunicheremo gli aggiornamenti non appena
possibile.

### Misure di sicurezza di Google per le chiavi compromesse

**In che modo Google mi aiuterà a proteggere il mio account da superamento dei costi e abusi se le mie chiavi API vengono divulgate?**

- Stiamo passando all'emissione di chiavi API quando richiedi una nuova chiave utilizzando
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=it), che per impostazione predefinita sarà
  limitata solo a Google AI Studio e non accetterà chiavi di altri servizi.
  In questo modo si evita l'utilizzo involontario di tasti incrociati.
- Per impostazione predefinita, blocchiamo le chiavi API che vengono divulgate e utilizzate con l'API Gemini, contribuendo a prevenire l'abuso dei costi e dei dati delle applicazioni.
- Potrai trovare lo stato delle tue chiavi API in [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=it) e ci impegneremo a comunicare
  in modo proattivo quando identifichiamo che le tue chiavi API sono state divulgate per un'azione immediata.

## Migliorare l'output del modello

Per ottenere output del modello di qualità superiore, prova a scrivere prompt più strutturati. La pagina
[Guida all'ingegneria del prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it)
introduce alcuni concetti di base, strategie e best practice per iniziare.

## Informazioni sui limiti di token

Leggi la nostra [guida ai token](https://ai.google.dev/gemini-api/docs/tokens?hl=it) per capire meglio come
contare i token e i relativi limiti.

## Problemi noti

- L'API supporta solo un numero limitato di lingue. L'invio di prompt in
  lingue non supportate può produrre risposte inaspettate o persino bloccate. Per gli aggiornamenti, consulta le
  [lingue disponibili](https://ai.google.dev/gemini-api/docs/models?hl=it#supported-languages).

## Segnala un bug

Se hai domande, partecipa alla discussione nel [forum per sviluppatori di Google AI](https://discuss.ai.google.dev?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-01 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-01 UTC."],[],[]]
