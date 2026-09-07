---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=it
fetched_at: 2026-09-07T05:49:58.553046+00:00
title: "Crea app per Android in Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Crea app per Android in Google AI Studio

Google AI Studio ti consente di creare app Android native da un prompt in linguaggio naturale. Descrivi l'app che vuoi e l'
[agente Antigravity](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=it#antigravity-agent)
genera un progetto completo in Kotlin e [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=it). Dal browser, puoi visualizzare l'anteprima dell'app in un emulatore Android basato su browser, installarla su un dispositivo fisico e pubblicarla per i test.

## Inizia

Per iniziare a creare un'app per Android:

1. Vai alla [modalità di creazione](https://aistudio.google.com/apps?hl=it) in Google AI Studio utilizzando il pannello di navigazione a sinistra.
2. Seleziona **Android** dal selettore della piattaforma.
3. Inserisci un prompt che descriva l'app che vuoi creare (ad es. *"Crea un tracker delle attività giornaliere con spazio di archiviazione locale"* o *"Crea una Calcolatrice semplice"*).
4. L'agente genera il progetto e lo avvia nell'emulatore Android basato su browser.

Puoi quindi eseguire l'iterazione sull'app utilizzando il riquadro della chat, proprio come nell'esperienza web. L'agente gestisce tutti i file del progetto Android e propaga le modifiche nel codebase.

## Emulatore Android basato su browser

L'emulatore Android viene eseguito interamente nel cloud e viene trasmesso in streaming al browser.
Non è necessario installare l'SDK Android, Android Studio o un emulatore locale.

L'emulatore fornisce:

- **Simulazione di un dispositivo simile a Pixel**: tocca, scorri e interagisci con l'app
  come su un dispositivo reale.
- **Supporto della rotazione**: passa dall'orientamento verticale a quello orizzontale.
- **Anteprima live**: quando l'agente apporta modifiche al codice, l'app viene ricompilata e
  l'emulatore si aggiorna automaticamente.

### Limitazioni dell'emulatore

L'emulatore basato su browser non supporta tutte le funzionalità hardware. Le seguenti funzionalità non sono disponibili nell'emulatore:

- Acquisizione di foto e video
- NFC e Bluetooth
- GPS (la posizione è simulata)
- Google Play Services (Accedi con Google, Maps e altre funzionalità di Play Services funzionano su un dispositivo reale, ma non nell'emulatore)

## Installazione su un dispositivo con ADB

Puoi installare l'APK creato direttamente su un dispositivo Android fisico collegato al computer tramite USB. Viene utilizzato
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=it) per
comunicare con il dispositivo tramite il browser. Non è richiesta l'installazione di ADB locale.

### Prerequisiti

- Un browser Chrome o Edge che supporti WebUSB.
- Un dispositivo Android con
  [le opzioni sviluppatore e il debug USB](https://developer.android.com/studio/debug/dev-options?hl=it)
  attivati.
- Un cavo USB che collega il dispositivo al computer.

### Installare l'app sul dispositivo

1. Fai clic su **Installa sul dispositivo** nel riquadro di anteprima.
2. Seleziona il tuo dispositivo Android dal selettore di dispositivi USB del browser.
3. L'APK viene trasferito e installato sul dispositivo.
4. L'app si avvia automaticamente.

## Pubblicazione sul Play Store

Puoi pubblicare la tua app per Android nel
[canale di test interno](https://play.google.com/console?hl=it) di
Google Play Console, che ti consente di distribuire l'app a un massimo di 100 tester.

### Prerequisiti

- Un [account sviluppatore Google Play](https://play.google.com/console/signup?hl=it)
  (richiede una commissione di registrazione una tantum di 25 $).
- Un profilo sviluppatore completato in Play Console.

### Pubblicare l'app

1. Apri **Impostazioni > Pubblica** in Google AI Studio.
2. Fai clic su **Pubblica sul Play Store**.
3. Esegui l'autenticazione con il tuo account sviluppatore Google Play.
4. AI Studio firma l'APK, crea la scheda dell'app (o carica una nuova versione) e la pubblica nel canale di test interno.
5. Riceverai un link da condividere con i tuoi tester.

AI Studio gestisce automaticamente la firma dell'APK utilizzando un keystore gestito. Puoi personalizzare la scheda dell'app (icona, screenshot, descrizione) in un secondo momento in Play Console.

## Cosa viene generato

Quando crei un'app per Android, l'agente genera un progetto standard basato su Gradle con la seguente struttura:

- **Configurazione di compilazione**: `build.gradle.kts` file (a livello di progetto e app) che utilizzano Kotlin DSL.
- **Livello UI**: [componenti](https://developer.android.com/develop/ui/compose?hl=it)
  Jetpack Compose con temi [Material 3](https://m3.material.io/).
- **Architettura**: architettura a singola attività con ViewModel e classi di
  dati.
- **Risorse**: `AndroidManifest.xml`, elementi disegnabili, stringhe e altre risorse Android.

L'agente gestisce automaticamente le dipendenze di Gradle, aggiungendo i pacchetti dai repository Maven e Google in base alle necessità.

Puoi visualizzare e modificare il codice generato utilizzando la scheda **Codice** nel riquadro di anteprima. Per continuare lo sviluppo in Android Studio, scarica il progetto come **file ZIP**.

## Limitazioni

La creazione di app per Android in AI Studio presenta le seguenti limitazioni:

### Limitazioni della piattaforma

- **Solo lato client**: le app Android non includono un componente lato server.
  Le funzionalità che richiedono un runtime del server (gestione dei secret, multigiocatore, Firebase, API Google Workspace) non sono disponibili.
- **Architettura a singola attività**: sono supportati solo i progetti a singola attività e a singolo modulo.
- **Solo Jetpack Compose**: le app utilizzano Kotlin e Jetpack Compose. I layout Java e XML non sono supportati.
- **Nessun NDK o codice nativo**: il codice C e C++ non è supportato.
- **Nessun Wear OS o Android TV**: sono supportati solo i fattori di forma di smartphone e tablet.

### Limitazioni per l'esportazione

- **Solo download ZIP**: puoi scaricare il progetto come file ZIP. L'esportazione di GitHub non è ancora disponibile per i progetti Android.

## Passaggi successivi

- [Crea app in Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=it)
- [Sviluppo di app full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=it) (web)
- Consulta gli esempi nella [Galleria app](https://aistudio.google.com/apps?source=showcase&hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-08-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-08-19 UTC."],[],[]]
