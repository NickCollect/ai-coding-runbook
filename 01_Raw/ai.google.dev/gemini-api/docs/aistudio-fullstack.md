---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=it
fetched_at: 2026-08-03T04:26:42.429441+00:00
title: "Sviluppare app full-stack in Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Sviluppare app full-stack in Google AI Studio

Google AI Studio ora supporta lo sviluppo full-stack, consentendoti di creare
applicazioni che vanno oltre i prototipi lato client. Con un runtime lato server, puoi gestire i segreti, connetterti ad API esterne e creare esperienze multiplayer in tempo reale.

## Runtime lato server

Le applicazioni Google AI Studio ora possono includere un componente lato server (Node.js).
In questo modo potrai:

- **Esegui logica lato server**: esegui codice che non deve essere esposto al client.
- **Accedere ai pacchetti npm**: l'[agente antigravità](https://antigravity.google/docs/agent?hl=it)
  può installare e utilizzare pacchetti del vasto ecosistema npm.
- **Gestisci i secret**: utilizza in modo sicuro chiavi API e credenziali.

### Utilizzare i pacchetti npm

Non devi eseguire manualmente `npm install`. Basta chiedere all'agente di aggiungere una funzionalità che richiede un pacchetto e l'agente gestirà l'installazione e l'importazione.

**Esempio**: > "Utilizza `axios` per recuperare i dati dall'API esterna."

## Gestire i secret in modo sicuro

Con la gestione del codice e dei secret lato server, ora puoi creare app che interagiscono con il mondo.

### Chiave API Gemini

Quando crei una nuova app che utilizza l'API Gemini, AI Studio configura automaticamente la tua `GEMINI_API_KEY` come secret lato server, senza richiedere alcuna configurazione manuale. Puoi visualizzare questa chiave nel riquadro **Secret** delle Impostazioni. Le chiamate all'API Gemini della tua app vengono effettuate dal codice lato server utilizzando questa chiave, quindi non viene mai esposta nel browser.

### Chiavi API di terze parti

Per altri servizi, puoi aggiungere le chiavi API manualmente:

- **API di terze parti**: connettiti a servizi come Stripe, SendGrid o API REST personalizzate.
- **Database**: connettiti a database esterni (ad es. tramite Supabase, Firebase o MongoDB Atlas) per conservare i dati oltre la sessione.

Quando crei app reali, spesso devi connetterti a servizi di terze parti
(come Twilio, Slack o database) che richiedono chiavi API. Puoi aggiungere le chiavi
manualmente seguendo questi passaggi:

1. **Aggiungi un secret**: vai al menu **Impostazioni** in Google AI Studio e cerca la sezione Secret.
2. **Memorizza la chiave**: aggiungi qui le tue chiavi API o i tuoi token segreti.
3. **Accesso nel codice**: l'agente può scrivere codice lato server che accede a questi
   segreti in modo sicuro (in genere tramite variabili di ambiente), assicurandosi che non vengano
   mai esposti al browser lato client.

Se necessario, l'agente
mostrerà anche una scheda nella chat che ti chiede di aggiungere le chiavi ogni volta che è necessario un nuovo secret
o quando viene rilevata una nuova chiave nelle variabili di ambiente del progetto.

### Integrazione di Firebase per database e autenticazione

Google AI Studio ora semplifica l'aggiunta di un database o dell'autenticazione alla tua
app tramite un'
[integrazione di Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=it).
L'agente Antigravity può eseguire il provisioning e configurare automaticamente i seguenti servizi:

- **Database Firestore**: un database cloud NoSQL flessibile e scalabile per archiviare
  e sincronizzare i dati per lo sviluppo lato client e lato server.
- **Firebase Authentication**: consente agli utenti di accedere in modo sicuro alla tua
  applicazione utilizzando i flussi "Accedi con Google".

Basta chiedere all'agente di "aggiungere un database alla mia app" o di "configurare Google Sign-in".
L'agente gestirà la configurazione e la generazione del codice necessarie.

Firebase ti consente di iniziare senza costi e, se vuoi, di eseguire lo scale-up con un account a pagamento
quando hai bisogno di una quota maggiore o di utilizzare funzionalità a pagamento.

## API Google Workspace

Google AI Studio ti consente di creare app che si connettono alle API Google Workspace, in modo che i tuoi utenti possano lavorare con i loro dati reali: email, fogli di lavoro, documenti, eventi di calendario e altro ancora, tutto all'interno della tua app. Non è più necessario configurare un progetto Google Cloud, configurare OAuth o gestire manualmente l'API.

### Come funziona

Puoi aggiungere un'integrazione di Workspace in due modi:

- **Descrivilo nel riquadro della chat**: basta dire all'agente cosa vuoi nel riquadro della chat in basso. Ad esempio, *"Crea un tracker delle spese che registri le ricevute nel mio foglio Google"* o *"Crea una dashboard che riepiloghi i miei messaggi Gmail non letti"*.
- **Seleziona dal riquadro delle integrazioni**: apri il riquadro **Integrazioni** nella barra laterale destra della modalità di creazione e attiva l'app Workspace che vuoi connettere.

Quando aggiungi un'app Workspace, AI Studio esegue automaticamente le seguenti operazioni:

1. Collega l'API Google necessaria per la tua app.
2. Genera il codice lato server per chiamare l'API.
3. Aggiunge un flusso sicuro di "Accedi con Google" in modo che gli utenti finali della tua app possano autorizzare l'accesso ai propri dati.

### App supportate

Sono disponibili le seguenti app Google Workspace:

| App | Cosa puoi creare |
| --- | --- |
| Google Calendar | Leggere, creare e gestire eventi e calendari |
| Google Chat | Leggere e interagire con conversazioni e spazi di gruppo |
| Documenti Google | Creare, leggere, aggiornare e formattare documenti |
| Google Drive | Organizzare, cercare e gestire file e cartelle |
| Moduli Google | Creare sondaggi, aggiornare le domande e recuperare le risposte |
| Gmail | Leggere, inviare e gestire i contenuti delle email |
| Google Keep | Gestire note, elenchi e allegati |
| Google Meet | Pianificare e gestire le videochiamate |
| Contatti | Sincronizzare e gestire i contatti |
| Fogli Google | Leggere, scrivere e formattare i dati del foglio di lavoro |
| Presentazioni Google | Creare e modificare presentazioni |
| Google Tasks | Creare, gestire e organizzare le attività |

### Autenticazione e autorizzazioni

In qualità di builder, non devi configurare i client OAuth, gestire le credenziali
o configurare un progetto Google Cloud. AI Studio gestisce tutto questo per te.

Le app con le API Workspace integrate utilizzano "Accedi con Google" per autenticare
gli utenti finali. Quando un utente apre la tua app, gli viene chiesto di accedere e concedere
le autorizzazioni specifiche di cui la tua app ha bisogno (ad esempio, l'accesso in sola lettura al
calendario o la possibilità di modificare un foglio di lavoro). La tua app accede solo ai dati della persona che la utilizza. Ogni utente autorizza l'accesso al proprio account.

### Prompt di esempio

Ecco alcune idee per iniziare a utilizzare le integrazioni di Workspace:

- *"Crea un'app che legga il mio Google Calendar e crei bozze di email di preparazione in
  Gmail per ogni riunione".*
- *"Crea uno strumento che prenda un documento Google e generi un riepilogo di 5 slide
  in Presentazioni Google."*
- *"Crea un monitoraggio delle spese in cui carico una ricevuta, Gemini estrae i
  dettagli e registra una nuova riga nel mio Foglio Google."*

### Configura OAuth

Un caso d'uso chiave per la gestione dei secret è la configurazione di OAuth per connettersi ad altri
siti web o app. Quando il prompt include istruzioni su come connettersi a un'app di terze parti che richiede l'autenticazione OAuth, l'agente fornirà istruzioni su come configurare OAuth per l'applicazione. Queste istruzioni
includeranno gli URL di callback necessari per configurare l'applicazione OAuth.
Puoi trovare gli URL di callback anche nella sezione **Integrazioni** nel pannello Impostazioni.

## Creare esperienze multigiocatore

Il runtime full-stack attiva le funzionalità di collaborazione in tempo reale.

- **Stato in tempo reale**: puoi chiedere all'agente di creare funzionalità come "una chat live", "una lavagna collaborativa" o "un gioco multiplayer".
- **Sessioni sincronizzate**: il server gestisce lo stato, consentendo a più utenti
  di interagire con la stessa istanza dell'applicazione in tempo reale.

**Esempio di prompt**: > "Crea un gioco multiplayer in cui i giocatori possono vedere i cursori
degli altri."

### Suggerimenti per testare le app multiplayer

Puoi testare la modalità multigiocatore in due modi prima di eseguire il deployment dell'app.

1. Apri l'app in modalità di creazione di Google AI Studio in più schede. Quando
   sviluppi in modalità Build, la tua app si trova in un container di sviluppo. L'apertura dell'app in più schede ti consentirà di simulare più giocatori che utilizzano la tua app.
2. Condividi l'app con altri utilizzando il menu **Condividi** in alto a destra.
   Poi utilizza l'**URL condiviso** della scheda **Integrazioni**
   del menu **Condividi** per utilizzare l'app con i giocatori con cui l'hai condivisa.

## Best practice

- **Chiamate API Gemini**: il tuo `GEMINI_API_KEY` viene configurato automaticamente come
  secret lato server. Esegui chiamate all'API Gemini dal codice lato server utilizzando
  questa chiave. Puoi visualizzarlo nel riquadro **Secret**.
- **Sicurezza dei secret**: utilizza sempre Secret Manager per le chiavi sensibili.
  Non codificarli mai nei file.
- **Separazione delle responsabilità**: mantieni la logica dell'interfaccia utente nel framework lato client
  (React/Angular) e la logica di business/gestione dei dati lato server.
- **Gestione degli errori**: assicurati che il codice lato server gestisca in modo efficace gli errori
  delle chiamate API esterne per evitare arresti anomali dell'app.

## Passaggi successivi

- [Creare app in Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=it)
- [Deployment da Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=it)
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
