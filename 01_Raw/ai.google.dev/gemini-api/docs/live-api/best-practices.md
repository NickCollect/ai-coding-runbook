---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=it
fetched_at: 2026-10-26T05:43:53.963036+00:00
title: "Best practice per l'API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Best practice per l'API Live

Questa guida illustra le best practice che puoi seguire per
ottimizzare l'utilizzo dell'API Live.
Consulta la pagina [Inizia a utilizzare l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=it) per una panoramica e un codice campione per i casi d'uso comuni.

## Progettare istruzioni di sistema chiare

Per ottenere le migliori prestazioni dall'API Live, ti consigliamo di avere un insieme di istruzioni di sistema (SI) chiaramente definito che definisca la persona dell'agente, le regole conversazionali e le protezioni, in questo ordine.

Per ottenere risultati ottimali, separa ogni agente in un intent di sistema distinto.

1. **Specifica la personalità dell'agente**:fornisci dettagli sul nome, sul ruolo e su eventuali caratteristiche preferite dell'agente. Se vuoi specificare l'accento, assicurati di
   specificare anche la lingua di output preferita (ad esempio un accento britannico per un
   oratore inglese).
2. **Specifica le regole conversazionali**:inserisci queste regole nell'ordine in cui prevedi che il modello le segua. Distinguere gli elementi una tantum della conversazione
   e i loop conversazionali. Ad esempio:

   - **Elemento una tantum:** raccogli i dati di un cliente una sola volta (ad esempio nome,
     posizione, numero di carta fedeltà).
   - **Ciclo conversazionale:** l'utente può discutere di consigli, prezzi,
     resi e consegne e potrebbe voler passare da un argomento all'altro. Comunica al modello che può continuare a interagire in questo ciclo conversazionale per tutto il tempo che l'utente desidera.
3. **Specifica le chiamate agli strumenti all'interno di un flusso in frasi distinte:** ad esempio, se un passaggio
   una tantum per raccogliere i dettagli di un cliente richiede l'invocazione di una funzione `get_user_info`, potresti dire: *Il primo passaggio consiste nel raccogliere le informazioni dell'utente. Innanzitutto,
   chiedi all'utente di fornire il proprio nome, la propria posizione e il numero della carta fedeltà. Poi
   richiama `get_user_info` con questi dettagli.*
4. **Aggiungi eventuali misure di salvaguardia necessarie**:fornisci eventuali misure di salvaguardia generali per la conversazione che non vuoi che il modello esegua. Non esitare a fornire esempi specifici di se si verifica *x*, vuoi che il modello esegua *y*. Se ancora non
   ottieni il livello di precisione preferito, utilizza la parola
   *inconfondibilmente* per guidare il modello a essere preciso.

## Definisci gli strumenti con precisione

Quando utilizzi strumenti con l'API Live, specifica le definizioni degli strumenti.
Assicurati di indicare a Gemini in quali condizioni deve essere richiamata una chiamata allo strumento. Per maggiori dettagli, consulta le [definizioni degli strumenti](#tool-definitions-example) nella sezione degli esempi.

## Creare prompt efficaci

- **Utilizza prompt chiari**:fornisci esempi di ciò che i modelli devono e non devono fare nei prompt e cerca di limitare i prompt a uno per persona o ruolo alla volta. Invece di prompt lunghi e di più pagine, valuta la possibilità di utilizzare il
  concatenamento dei prompt. Il modello funziona meglio con attività con chiamate di funzione singole.
- **Fornisci comandi e informazioni iniziali**:l'API Live si aspetta
  l'input dell'utente prima di rispondere. Per fare in modo che l'API Live avvii la
  conversazione, includi un prompt che le chieda di salutare l'utente o di iniziare la
  conversazione. Includi informazioni sull'utente per consentire all'API Live
  di personalizzare il saluto.

## Specifica la lingua

I modelli audio dell'API Live rilevano e si adattano automaticamente alla lingua parlata dall'utente senza richiedere un codice lingua esplicito.

Se vuoi che il modello risponda in una lingua specifica, includi un'istruzione
nelle istruzioni di sistema:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Streaming

Quando implementi l'audio in tempo reale, segui queste best practice:

- **Dimensioni dei segmenti e latenza**: invia l'audio in segmenti da 20 ms a 40 ms.
- **Gestione delle interruzioni**: quando l'utente parla mentre il modello sta rispondendo,
  il server invia un messaggio `server_content` con `"interrupted": true`. Devi
  eliminare immediatamente il buffer audio lato client per impedire all'agente
  di continuare a parlare sopra l'utente.

## Gestione del contesto

Utilizza `ContextWindowCompressionConfig` per le sessioni lunghe, poiché i token audio nativi
si accumulano rapidamente (circa 25 token al secondo di audio).

## Buffering del client

Non memorizzare nel buffer l'audio di input in modo significativo (ad esempio 1 secondo) prima dell'invio. Invia
piccoli blocchi (20 ms - 100 ms) per ridurre al minimo la latenza.

## Ricampionamento

Assicurati che l'applicazione client esegua il ricampionamento dell'input del microfono (spesso 44,1 kHz o 48 kHz) a 16 kHz prima della trasmissione.

## Gestione sessione

Segui queste linee guida per gestire il ciclo di vita della sessione e garantire un'esperienza utente affidabile:

- **Attiva la compressione della finestra contestuale:** i token audio si accumulano a
  circa 25 token al secondo. Senza compressione, le sessioni solo audio
  sono limitate a 15 minuti e le sessioni audio-video a 2 minuti. Attiva la
  [compressione della finestra contestuale](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=it#context-window-compression)
  per estendere le sessioni a una durata illimitata.
- **Implementa il ripristino della sessione**:il server potrebbe reimpostare periodicamente la connessione WebSocket. Utilizza la
  [ripresa della sessione](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=it#session-resumption)
  per riconnetterti senza problemi senza perdere il contesto. Conserva il token di ripresa
  più recente di `SessionResumptionUpdate` messaggi e passalo come handle durante
  la riconnessione. I token di ripresa sono validi per 2 ore dopo la fine dell'ultima sessione.
- **Gestisci i messaggi GoAway**:il server invia un messaggio
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=it#goaway-message)
  prima di terminare una connessione. Ascolta questo messaggio e utilizza il
  campo `timeLeft` per concludere o riconnetterti prima che la connessione
  si chiuda.
- **Gestisci i segnali generationComplete:** utilizza il messaggio
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=it#generation-complete-message) per sapere quando il modello ha terminato di generare una risposta, in modo che la tua applicazione possa aggiornare la sua UI o procedere con l'azione successiva.

Per i dettagli di implementazione, vedi
[Gestione delle sessioni](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=it).

## Esempi

Questo esempio combina le best practice e le [linee guida per la progettazione delle istruzioni di sistema](#system-instruction-guidelines) per guidare il rendimento del modello in qualità di career coach.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Definizioni degli strumenti

Questo JSON definisce le funzioni pertinenti chiamate nell'esempio di career coach.
Per ottenere risultati ottimali quando definisci le funzioni, includi i relativi nomi, descrizioni,
parametri e condizioni di chiamata.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Prezzi e fatturazione

L'API Gemini Live viene fatturata rigorosamente in base all'utilizzo dei token. Poiché l'API Live mantiene una sessione WebSocket persistente, la fatturazione segue un modello di compounding basato sulla finestra contestuale attiva.

### La finestra contestuale della sessione (costi cumulativi)

L'API ti addebita un costo per turno per tutti i token presenti nella finestra contestuale della sessione. Un "turno" è definito come un input dell'utente e la risposta corrispondente del modello.

- **Accumulo**:la finestra contestuale include i nuovi token del turno corrente più tutti i token accumulati dei turni precedenti.
- **Rifatturazione**:i token precedenti vengono rielaborati e contabilizzati in ogni nuovo turno, fino alle dimensioni della finestra contestuale configurata. Man mano che una sessione si allunga, il costo per turno aumenta perché la cronologia della conversazione viene rielaborata.

### Token audio e trascrizioni

L'API Live è multimodale in modo nativo. Conserva la cronologia delle conversazioni come token audio non elaborati per preservare le sfumature e il tono acustici.

- **Fatturazione audio**:l'API ti addebita i token audio nativi accumulati alla tariffa di input audio standard a ogni turno.
- **Supplemento per la trascrizione**:quando la trascrizione da audio a testo è abilitata (`inputAudioTranscription` o `outputAudioTranscription`), l'API addebita tutti i token di testo generati per la trascrizione alla tariffa di output dei token di testo, oltre ai costi standard dei token audio.

### Gestione dei costi con limiti di contesto

Per evitare una crescita illimitata dei costi nelle sessioni lunghe, configura le dimensioni della finestra contestuale
utilizzando `contextWindowCompression`.

Se imposti un trigger di compressione (ad es. 25.000 token) e una finestra scorrevole
(ad es. 8000 token), l'API elimina automaticamente i token meno recenti una volta raggiunto
il limite. L'API fattura quindi i turni successivi solo per la cronologia
conservata più eventuali nuovi token.

### Audio proattivo

Quando l'audio proattivo è abilitato, l'API addebita i token di input per tutto il tempo in cui l'API Live è in ascolto e addebita i token di output solo quando l'API risponde.

- **Nota per Gemini 3.8:** l'audio proattivo è abilitato in modo permanente in
  `gemini-3.8-live` e `gemini-3.8-live-extended-thinking`.
- **Nota per Gemini 3.1:** l'audio proattivo non è supportato in
  `gemini-3.1-flash-live-preview`. Per questo modello, l'API addebita solo l'audio quando trasmetti attivamente l'input.

Per informazioni più dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-17 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-17 UTC."],[],[]]
