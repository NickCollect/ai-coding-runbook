---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it
fetched_at: 2026-09-14T05:50:52.545993+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# API Interactions

L'API Interactions è il modo migliore per creare con i modelli e gli agenti Gemini. A partire da giugno 2026, è disponibile a livello generale ed è consigliata per tutti i nuovi progetti. Sebbene ora sia considerata legacy, l'API originale
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=it)
rimane completamente supportata.

## Perché utilizzare l'API Interactions?

- **Interfaccia universale per tutte le applicazioni**: progettata come interfaccia standard
  per ogni caso d'uso, inclusi la generazione di testo a turno singolo,
  la comprensione multimodale, gli output strutturati, l'orchestrazione degli strumenti e
  i flussi di lavoro agentici.
- **Singola API per modelli e agenti**: un endpoint e un pattern unificati per
  chiamare direttamente i modelli Gemini standard e gli agenti specializzati (come
  Deep Research e gli agenti gestiti personalizzati).
- **Nuove funzionalità predefinite**: funzionalità come lo stato della conversazione lato server facoltativo utilizzando `previous_interaction_id`, passaggi di esecuzione osservabili per il debug e il rendering dell'interfaccia utente ed [esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it) per le attività a lunga esecuzione utilizzando `background=true`.
- **Costo inferiore con tassi di successo della cache più elevati**: quando si utilizzano conversazioni multi-turno, la gestione dello stato lato server facoltativa consente una memorizzazione nella cache del contesto più efficiente tra i turni, riducendo i costi dei token.
- **Dove vengono lanciate le nuove funzionalità**: in futuro, tutti i nuovi modelli, le funzionalità multimodali
  , gli strumenti e le funzionalità agentiche verranno lanciati sull'API Interactions.

Per impostazione predefinita, l'API Interactions memorizza le richieste in modo che tu possa sfruttare le funzionalità di gestione dello stato lato server utilizzando `previous_interaction_id`. Puoi attivare il comportamento stateless impostando `store=false`. Per maggiori dettagli, consulta la sezione sulla [conservazione dei dati](#data-storage-retention).

## Inizia

- **Configura l'agente di programmazione**: connettiti a **Gemini Docs MCP** e installa
  la skill `gemini-interactions-api` per consentire all'assistente di accedere direttamente a
  documentazione per gli sviluppatori e best practice più recenti. Per la procedura dettagliata, consulta la
  [guida Configurare l'agente di programmazione](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)
- **Esegui la migrazione da `generateContent`**: se hai un'integrazione esistente,
  segui la [Guida alla migrazione](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=it) per
  passare all'API Interactions.
- **Inizia**: segui i passaggi descritti nella [guida introduttiva all'API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=it).

### Guide alle funzionalità

Esplora le funzionalità specifiche dell'API Interactions tramite queste guide. Puoi utilizzare l'opzione di attivazione/disattivazione in queste pagine per passare da generateContent all'API Interactions:

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it)
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it)
- [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/audio?hl=it)
- [Comprensione dei video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it)
- [Elaborazione dei documenti](https://ai.google.dev/gemini-api/docs/document-processing?hl=it)
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
- [Output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it)
- [Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)
- [Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)

## Come funziona l'API Interactions

L'API Interactions è incentrata su una risorsa principale: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=it#Resource:Interaction). Un'`Interaction` rappresenta un turno completo in una conversazione o un'attività. Funge da record di sessione, contenente l'intera cronologia di un'interazione come sequenza cronologica di **passaggi di esecuzione**. Questi passaggi includono i pensieri del modello, le chiamate e i risultati degli strumenti lato server o lato client (come `function_call` e `function_result`) e l'`model_output` finale. La risorsa archiviata (recuperata tramite `interactions.get`) include anche i passaggi `user_input` per il contesto completo, anche se la risposta `interactions.create` restituisce solo i passaggi generati dal modello.

Quando effettui una chiamata a
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=it#CreateInteraction), stai
creando una nuova risorsa `Interaction`.

### Gestione dello stato lato server

Puoi utilizzare il `id` di un'interazione completata in una chiamata successiva utilizzando il
`previous_interaction_id` parametro per continuare la conversazione. Il server utilizza questo ID per recuperare la cronologia delle conversazioni, evitando di dover inviare di nuovo l'intera cronologia chat.

Il parametro `previous_interaction_id` conserva solo la cronologia delle conversazioni (input e output) utilizzando `previous_interaction_id`. Gli altri parametri sono **ambito di interazione** e si applicano solo all'interazione specifica che stai generando:

- `tools`
- `system_instruction`
- `generation_config` (inclusi `thinking_level`, `temperature` e così via)

Ciò significa che devi specificare di nuovo questi parametri in ogni nuova interazione se vuoi che vengano applicati. Questa gestione dello stato lato server è facoltativa; puoi anche operare in modalità stateless inviando la cronologia completa delle conversazioni in ogni richiesta.

### Archiviazione e conservazione dei dati

Per impostazione predefinita, l'API archivia tutti gli oggetti Interaction (`store=true`) per
semplificare l'utilizzo delle funzionalità di gestione dello stato lato server (con
`previous_interaction_id`), [l'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it) (utilizzando `background=true`) e
per scopi di osservabilità.

- **Livello a pagamento**: il sistema conserva le interazioni per **55 giorni**.
- **Livello senza costi**: il sistema conserva le interazioni per **1 giorno**.

Se non vuoi che ciò accada, puoi impostare `store=false` nella richiesta. Questo controllo è separato dalla gestione dello stato; puoi disattivare l'archiviazione per qualsiasi interazione. Tuttavia, tieni presente che
`store=false` non è compatibile con [l'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it) e impedisce l'utilizzo di
`previous_interaction_id` per i turni successivi.

Per i progetti di livello a pagamento, puoi configurare la finestra di conservazione in
[AI Studio](https://aistudio.google.com/logs?hl=it) per contrassegnare automaticamente i log per
l'eliminazione dallo spazio di archiviazione del progetto dopo 7, 14, 28 o 55 giorni. Una conservazione più breve potrebbe influire sul recupero delle conversazioni passate.

Puoi eliminare le interazioni archiviate in qualsiasi momento utilizzando il metodo [`delete`](https://ai.google.dev/api/interactions-api?hl=it#deleteInteraction) a livello di programmazione, che
richiede l'ID interazione. Puoi anche visualizzare e gestire i log delle interazioni archiviate, inclusa l'eliminazione dallo spazio di archiviazione del progetto, in
[AI Studio](https://aistudio.google.com/logs?hl=it).

Al termine del periodo di conservazione, i dati verranno eliminati automaticamente.

Gli oggetti Interactions vengono elaborati in base ai [termini](https://ai.google.dev/gemini-api/terms?hl=it).

### Visualizzare le interazioni in AI Studio

L'API archivia le richieste dell'API Interactions eseguite con `store=true` per i progetti di livello a pagamento. Puoi visualizzarli direttamente dalla
[pagina Log in Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=it). Per saperne di più, consulta la guida
[Log](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it).

## Best practice

- **Tasso di successo della cache**: la memorizzazione nella cache implicita è supportata sia in modalità stateful che
  stateless (vedi
  [Guida rapida](https://ai.google.dev/gemini-api/docs/get-started?hl=it#4_multi-turn_conversations)). L'utilizzo di `previous_interaction_id` (stateful) per continuare le conversazioni consente al sistema di utilizzare più facilmente la memorizzazione nella cache implicita per la cronologia delle conversazioni, il che migliora le prestazioni e riduce i costi.
- **Combinazione di interazioni**: hai la flessibilità di combinare le interazioni di agenti e
  modelli all'interno di una conversazione. Ad esempio, puoi utilizzare un agente specializzato, come l'agente Deep Research, per la raccolta iniziale dei dati e poi utilizzare un modello Gemini standard per le attività di follow-up, come il riepilogo o la riformattazione, collegando questi passaggi con `previous_interaction_id`.

## Modelli e agenti supportati

| Nome modello | Tipo | ID modello |
| --- | --- | --- |
| Gemini 3.6 Flash | Modello | `gemini-3.6-flash` |
| Gemini 3.5 Flash | Modello | `gemini-3.5-flash` |
| Gemini 3.1 Pro (anteprima) | Modello | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Modello | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Modello | `gemini-3.1-flash-lite` |
| Gemini 3 Flash (anteprima) | Modello | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modello | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modello | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | Modello | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modello | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | Modello | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS (anteprima) | Modello | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modello | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modello | `gemma-4-26b-a4b-it` |
| Lyria 3 Clip (anteprima) | Modello | `lyria-3-clip-preview` |
| Lyria 3 Pro (anteprima) | Modello | `lyria-3-pro-preview` |
| Deep Research (anteprima) | Agente | `deep-research-preview-04-2026` |
| Deep Research (anteprima) | Agente | `deep-research-max-preview-04-2026` |
| Antigravity (anteprima) | Agente | `antigravity-preview-05-2026` |

## SDK

Puoi utilizzare la versione più recente degli SDK Google GenAI per accedere all'API Interactions.

- In Python, questo è il pacchetto `google-genai` dalla versione `2.3.0` in poi.
- In JavaScript, questo è il pacchetto `@google/genai` dalla versione `2.3.0` in poi.

Puoi scoprire di più su come installare gli SDK nella pagina
[Librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it).

## Limitazioni

- **MCP remoto**: Gemini 3 non supporta MCP remoto, ma questa funzionalità sarà disponibile a breve.
- **Compatibilità dei modelli a più turni**: quando si combinano modelli diversi in una
  conversazione (stateful o stateless), i modelli successivi devono supportare
  le modalità di output dei modelli precedenti come input. Ad esempio, se generi un'immagine utilizzando `gemini-3.1-flash-image`, non puoi continuare la conversazione con un modello che non accetta input di immagini (ad esempio un modello solo di testo o un modello di generazione di musica come Lyria).

Le seguenti funzionalità sono supportate dall'
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=it) API, ma **non sono ancora
disponibili** nell'API Interactions:

- **[Metadati video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it)**: il campo `video_metadata`, utilizzato per impostare gli intervalli di ritaglio
  e le frequenze fotogrammi personalizzate per la comprensione dei video.
- **[API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**
- **[Chiamata di funzione automatica (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=it#automatic_function_calling_python_only)**
- **[Memorizzazione nella cache esplicita](https://ai.google.dev/gemini-api/docs/caching?hl=it)**: tieni presente che la memorizzazione nella cache implicita lato server è disponibile nell'API Interactions
  tramite `previous_interaction_id`.
- **[Impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it)**: le impostazioni di sicurezza personalizzate
  non sono supportate nell'API Interactions.

## Feedback

Il tuo feedback è fondamentale per lo sviluppo dell'API Interactions.
Condividi le tue opinioni, segnala bug o richiedi funzionalità nel nostro
[forum della community di sviluppatori di Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=it).

## Passaggi successivi

- Prova il [notebook di avvio rapido dell'API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=it).
- Scopri di più sull'[agente Deep Research di Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
