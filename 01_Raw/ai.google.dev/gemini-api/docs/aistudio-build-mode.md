---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=it
fetched_at: 2026-08-17T02:19:42.114960+00:00
title: "Crea app in Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Crea app in Google AI Studio

Questa pagina descrive come utilizzare Google AI Studio per creare rapidamente (o "vibe
code") ed eseguire il deployment di app che testano le funzionalità più recenti di Gemini, come
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) e l'API [Live](https://ai.google.dev/gemini-api/docs/live?hl=it). Google AI Studio supporta la creazione di **app web** con runtime full stack e **app Android native** con Kotlin e Jetpack Compose, il tutto tramite prompt in linguaggio naturale.

## Inizia

Inizia a utilizzare il vibe coding nella [modalità di creazione](https://aistudio.google.com/apps?hl=it) di Google AI Studio. Puoi iniziare a creare in diversi modi:

- **Inizia con un prompt**: in modalità di creazione, utilizza la casella di input per inserire una
  descrizione di ciò che vuoi creare. Seleziona AI Chips per aggiungere funzionalità specifiche, come la generazione di immagini o i dati di Google Maps, al prompt. Puoi anche dire quello che vuoi utilizzando il pulsante di sintesi vocale.
- **Pulsante "Mi sento fortunato"**: se hai bisogno di un'idea creativa, utilizza il pulsante "Mi
  sento fortunato" e Gemini genererà un prompt con un'idea di progetto
  per aiutarti a iniziare.
- **Remixa un progetto dalla galleria**: apri un progetto dalla [Galleria
  app](https://aistudio.google.com/apps?source=showcase&hl=it) e seleziona **Copia app**.
- **Importa un progetto da GitHub**: in modalità di creazione, seleziona
  **Importa da GitHub** dal menu **Aggiungi file** (icona +) nella casella di input del prompt
  per importare il codice esistente.

Una volta eseguito il prompt, vedrai che vengono generati il codice e i file necessari, con un'anteprima live della tua app che apparirà sul lato destro.

## Che cosa viene creato?

Quando esegui il prompt, AI Studio crea un'applicazione completa. Puoi scegliere di creare un'**app web** o un'**app Android nativa** utilizzando il selettore della piattaforma.

Per le **app web** (impostazione predefinita), AI Studio crea un ambiente full stack che include:

- **Lato client**: un frontend web (React è l'impostazione predefinita).
- **Lato server**: un runtime Node.js che consente chiamate API sicure,
  connessioni al database e utilizzo di pacchetti npm.

Per le **app Android**, AI Studio genera un progetto Kotlin e Jetpack Compose
di cui puoi visualizzare l'anteprima in un emulatore basato su browser, installare su un dispositivo fisico,
e pubblicare sul Play Store per i test. [Scopri di più sulla creazione di app Android
apps](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=it).

Puoi visualizzare il codice generato selezionando la scheda **Codice** nel riquadro di anteprima a destra. L'**agente Antigravity** gestisce in modo intelligente più file nello stack, assicurandosi che le modifiche vengano propagate correttamente.

### L'agente Antigravity

L'**agente Antigravity** è la funzionalità di AI principale di [Google
Antigravity](https://antigravity.google?hl=it) e ora i componenti principali dell'
agente sono alla base dell'esperienza della modalità di creazione in Google AI Studio. Va oltre la semplice generazione di codice mantenendo il contesto dell'intero progetto, gestendo più file e comprendendo istruzioni complesse per creare applicazioni full stack robuste.

Le sue funzionalità principali includono:

- **Rilevamento del contesto**: mantiene il contesto dei prompt precedenti e degli stati dei file.
- **Gestione di più file**: gestisce le dipendenze tra più file.
- **Esecuzione verificata**: verifica gli aggiornamenti del codice per ridurre le allucinazioni.

## Funzionalità full stack

Google AI Studio sfrutta la potenza del moderno ecosistema web, consentendoti di creare prototipi non solo lato client.

- **Runtime lato server e npm**: utilizza la vasta libreria di pacchetti npm. L'agente identificherà e installerà automaticamente i pacchetti necessari per la tua app (ad es. librerie specifiche per la visualizzazione dei dati o client API). Se vuoi, puoi anche richiedere pacchetti specifici.
- **Gestione dei secret**: archivia in modo sicuro chiavi API e secret nel
  **menu Impostazioni**. Questi sono accessibili nel codice lato server, mantenendoli al sicuro dall'esposizione lato client.
- **Multiplayer**: crea esperienze collaborative in tempo reale direttamente in
  AI Studio. Il runtime lato server gestisce lo stato e le connessioni necessarie per l'interazione degli utenti.
- **Firebase Firestore e autenticazione**: esegui automaticamente il provisioning e la configurazione di Firebase,
  inclusi il database Firestore (archiviazione permanente dei dati) e
  l'autenticazione Firebase (flussi di accesso, in particolare "Accedi con Google").
  L'agente gestisce l'intera procedura di configurazione e scrive persino il codice nella tua app per questi servizi.
- **Integrazioni di Google Workspace**: collega la tua app alle API di Google Workspace
  come Gmail, Fogli, Documenti, Drive, Calendar e altro ancora. AI Studio gestisce automaticamente tutta la configurazione OAuth.

[Scopri di più sullo sviluppo di app full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=it)

### App Android

Puoi anche creare app Android native utilizzando Kotlin e Jetpack Compose.
Visualizza l'anteprima dell'app in un emulatore Android basato su browser, installala su un dispositivo fisico utilizzando ADB nel browser e pubblicala sul Play Store per i test interni.

[Scopri di più sulla creazione di app Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=it)

## Continua a creare

Una volta che Google AI Studio genera il codice iniziale per la tua applicazione, puoi continuare a perfezionarlo:

### Crea in Google AI Studio

- **Esegui iterazioni con Gemini**: utilizza il riquadro della chat in **modalità di creazione** per chiedere a Gemini
  di apportare modifiche, aggiungere nuove funzionalità o modificare lo stile.
- **Modifica il codice direttamente**: apri la **scheda Codice** nel riquadro di anteprima per
  apportare modifiche live.

### Sviluppa esternamente

Per workflow più avanzati, puoi esportare il codice e lavorare nell'ambiente che preferisci:

- **Scarica e sviluppa localmente**: esporta il codice generato come **file
  ZIP** e importalo nell'editor di codice.
- **Esegui il push su GitHub**: integra il codice con i processi di sviluppo e
  esecuzione del deployment esistenti eseguendo il push in un **repository GitHub**.

## Funzionalità principali

Google AI Studio include diverse funzionalità per rendere il processo di creazione intuitivo e visivo:

- **Crea ed esegui iterazioni di app full stack**: crea app full stack con un semplice
  prompt ed esegui iterazioni tramite la chat o la **modalità di annotazione**. La modalità di annotazione ti consente di evidenziare qualsiasi parte della UI dell'app e descrivere la modifica che vuoi apportare.
- **Condividi ed esegui il deployment dell'app**: puoi condividere le tue creazioni con altri utenti per
  collaborare o mostrare il tuo lavoro. Quando condividi, le chiamate API vengono conteggiate ai fini dei limiti di utilizzo. Se utilizzi modelli a pagamento, potrebbero essere applicati costi. Quando l'app è pronta, esegui il deployment in Cloud Run.
- **Galleria app**: la Galleria app fornisce una libreria visiva di idee di progetto.
  Puoi sfogliare le possibilità offerte da Gemini, visualizzare immediatamente l'anteprima delle applicazioni e remixarle per personalizzarle.

## Esegui il deployment o l'archiviazione dell'app

Quando l'applicazione è pronta, puoi eseguirne il deployment:

- **Cloud Run**: esegui il deployment dell'applicazione come servizio scalabile.
  Potrebbero essere applicati prezzi per [Google Cloud Run](https://cloud.google.com/run?hl=it) in base
  all'utilizzo. Per scoprire di più sul deployment, consulta
  [Eseguire il deployment da Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=it).
- **GitHub**: esporta il progetto in un repository GitHub.

## Limitazioni

Questa sezione elenca le limitazioni attuali della modalità di creazione in Google AI Studio.

### Gestione delle chiavi API

Quando crei una nuova app che utilizza l'API Gemini, AI Studio configura automaticamente la chiave API Gemini come secret nell'ambiente lato server dell'app.
Puoi visualizzare e gestire questa chiave nel riquadro **Secret**.

- **Configurazione automatica**: la variabile `GEMINI_API_KEY` viene configurata automaticamente. Non è necessaria alcuna configurazione manuale
  per iniziare a creare.
- **Solo lato server**: le chiavi API vengono inserite nel runtime lato server e
  non sono mai incluse nel codice lato client.
- **App esistenti**: per le app create prima del 14 maggio 2026, l'agente aggiornerà
  automaticamente l'integrazione dell'API Gemini all'approccio lato server
  consigliato la prossima volta che modifichi le funzionalità Gemini dell'app.

### Deployment al di fuori di Google AI Studio

- **Cloud Run**: quando esegui il deployment in Cloud Run da AI Studio, la chiave API viene
  inclusa in modo sicuro nell'ambiente lato server. L'app di cui è stato eseguito il deployment utilizzerà la chiave API per tutte le chiamate API Gemini degli utenti.
- **Download ZIP**: se scarichi l'app come file ZIP per eseguirla
  altrove, dovrai impostare la variabile di ambiente `GEMINI_API_KEY` nell'ambiente di hosting. Poiché le chiamate API Gemini dell'app vengono effettuate dal codice lato server, la chiave non viene esposta agli utenti finali.

### Errore durante la condivisione delle app

Se condividi la tua app e l'utente finale riscontra un errore **403 Accesso limitato** quando utilizza l'URL condiviso, potrebbe essere dovuto a uno dei seguenti motivi:

- **Estensioni del browser**: le estensioni per la privacy come Privacy Badger potrebbero bloccare l'app. Disattiva l'estensione per evitare l'errore.
- **Problemi di build**: potrebbero esserci problemi con il codice attuale. Chiedi all'agente di "correggere eventuali problemi di build con il codice attuale" e poi condividi di nuovo l'URL.

## Domande frequenti

### Che cos'è la modalità di creazione in AI Studio?

La modalità di creazione di AI Studio è una piattaforma progettata per trasformare un semplice prompt in un'applicazione basata sull'AI pronta per la produzione utilizzando Gemini. Descrivi ciò che vuoi creare con un prompt e Gemini genererà un'app per te. Puoi anche esplorare la nostra galleria per scoprire le possibilità offerte dall'API Gemini e remixare le app per personalizzarle.

### In che modo la modalità di creazione gestisce la mia chiave API Gemini?

Quando crei un'app che utilizza l'API Gemini, AI Studio configura automaticamente la chiave API Gemini come secret lato server. Le chiamate API Gemini dell'app vengono effettuate dal codice lato server utilizzando questa chiave, quindi non viene mai esposta nel browser. Puoi visualizzare la chiave API nel riquadro **Secret** in Impostazioni.

### La mia chiave API viene esposta quando condivido le app?

No. La chiave API viene memorizzata come secret lato server e non è mai inclusa nel codice lato client. Quando condividi l'app, altri utenti possono utilizzarla, ma non possono vedere la tua chiave API.

Quando condividi le tue app con altri utenti, le chiamate API vengono conteggiate ai fini dei limiti di utilizzo.
Se utilizzi modelli a pagamento, potrebbero essere applicati costi. AI Studio ti avviserà durante la configurazione e prima della condivisione se la tua app potrebbe comportare costi.

### Chi può vedere le mie app?

Per impostazione predefinita, la tua app è privata. Puoi condividere la tua app con altri utenti per consentire loro di utilizzarla. Gli utenti con cui condividi la tua app possono vedere il codice e creare un fork per i propri scopi. Se condividi la tua app con l'autorizzazione di modifica, gli altri utenti possono modificare il codice dell'app.

### Posso eseguire app al di fuori di AI Studio?

Sì. Puoi eseguire il deployment dell'app in
[Cloud Run](https://cloud.google.com/run?hl=it) da AI Studio, che
assegna alla tua app un URL pubblico con la chiave API configurata in modo sicuro nell'
ambiente lato server. Puoi anche scaricare l'app come file ZIP e ospitarla altrove. Dovrai impostare la variabile di ambiente `GEMINI_API_KEY` nell'ambiente di hosting. Poiché le chiamate API Gemini vengono effettuate dal codice lato server, la chiave rimane sicura.

Per scoprire di più sulle opzioni di deployment, consulta [Eseguire il deployment da Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=it).

### Posso sviluppare app localmente con i miei strumenti e poi condividerle qui?

Questa funzionalità non è ancora disponibile. Siamo felici di supportare altri casi d'uso per le app in futuro. Ti invitiamo a inviarci un feedback se hai qualcosa di specifico in mente.

### Come posso utilizzare un database o un altro spazio di archiviazione con le mie app?

Le app di AI Studio sono app standard in esecuzione in un container Cloud Run. Puoi utilizzare qualsiasi soluzione di archiviazione a cui puoi connetterti tramite una rete, a condizione che non esista un firewall che impedisca l'accesso da un intervallo di indirizzi IP dinamici.

Stiamo lavorando per aggiungere il supporto diretto per l'archiviazione in futuro, che potrai configurare direttamente in AI Studio.

### Come posso accedere al microfono, alla webcam e ad altre API Navigator?

Per garantire che gli spettatori siano a conoscenza dell'utilizzo della webcam o di altri
dispositivi da parte di un'app, richiediamo un'ulteriore conferma prima che l'app possa accedere
a queste [API Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
I creatori di app possono aggiungere queste richieste di autorizzazione al file `metadata.json` dell'app. Ad esempio:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

I valori supportati per `requestFramePermissions` sono un sottoinsieme delle
funzionalità standard [controllate dalle norme](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Come posso utilizzare GitHub con le mie app?

L'integrazione di GitHub di AI Studio ti consente di importare un progetto esistente da GitHub per iniziare a creare o esportare il progetto in un repository GitHub ed eseguire il commit delle modifiche più recenti.

### Posso concedere ad altri utenti l'accesso in modifica alla mia app?

Questa funzionalità non è ancora supportata, ma sarà disponibile a breve.

### Perché la mia app è stata segnalata per violazione delle norme?

Disponiamo di sistemi che esaminano automaticamente le app per assicurarsi che rispettino le nostre norme. Se rileviamo che un'app viola le nostre norme, verrà rimossa da AI Studio. Le violazioni delle norme possono includere, a titolo esemplificativo:

- App che contengono malware, phishing o furto d'identità
- App che mostrano o distribuiscono contenuti che violano le norme relative alle immagini di abusi sessuali su minori
- App che mostrano o distribuiscono contenuti che violano le norme relative alle molestie
- App che mostrano o distribuiscono contenuti che violano le norme relative ai discorsi di incitamento all'odio
- App che mostrano o distribuiscono contenuti che violano le norme relative alla tratta di esseri umani
- App che mostrano o distribuiscono contenuti che violano le norme relative ai contenuti sessualmente espliciti
- App che mostrano o distribuiscono contenuti che violano le norme relative a violenza e spargimento di sangue
- App che mostrano o distribuiscono contenuti che violano le norme relative a contenuti dannosi o pericolosi

Se la tua app è stata segnalata per una violazione delle norme e ritieni che si tratti di un errore, puoi presentare un ricorso. Le violazioni ripetute delle nostre norme possono comportare la chiusura dell'accesso ad AI Studio.

### Quali sono le mie responsabilità in qualità di sviluppatore di app?

Ti ricordiamo che, in qualità di proprietario dell'applicazione, sei responsabile del suo comportamento e di tutti i dati che gestisce. È incluso quanto segue:

- **Conformità legale e diritti di terze parti:** assicurati che la tua app sia conforme a tutte le leggi e le normative vigenti e che non violi i diritti di terzi, inclusi i diritti di proprietà intellettuale e di privacy.
- **Monitoraggio dei contenuti:** potrebbero essere applicati termini aggiuntivi ad altri servizi utilizzati dalla tua app. Ad esempio,
  [i Termini di servizio di Google Cloud](https://cloud.google.com/terms?hl=it),
  applicabili a Firestore, richiedono ai clienti che ospitano contenuti di terze parti di
  pubblicare norme che definiscono i contenuti vietati (ad es. contenuti
  illegali) e di monitorare la presenza di questi contenuti illegali.
- **Implementazione sicura:** implementa le misure di sicurezza e gli strumenti di moderazione necessari per impedire l'uso improprio dell'applicazione.

Tieni presente le [limitazioni d'uso](https://ai.google.dev/gemini-api/terms?hl=it#use-restrictions)
indicate nei Termini di servizio.

### Quali termini si applicano alle app nella Galleria app di AI Studio?

I [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it)
si applicano all'utilizzo delle app presenti nella Galleria app di AI Studio, salvo
diversa indicazione.

## Passaggi successivi

- [Sviluppare app full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=it) (web)
- [Creare app Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=it)
- Vedi esempi nella [Galleria app](https://aistudio.google.com/apps?source=showcase&hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-14 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-14 UTC."],[],[]]
