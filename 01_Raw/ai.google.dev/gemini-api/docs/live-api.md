---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=it
fetched_at: 2026-08-31T06:33:20.298098+00:00
title: "Panoramica dell'API Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Panoramica dell'API Gemini Live

L'API Live consente interazioni vocali e visive in tempo reale a bassa latenza con
Gemini. Elabora flussi continui di audio, immagini e testo per fornire
risposte immediate e simili a quelle umane, creando un'esperienza
conversazionale naturale per i tuoi utenti.

![Panoramica dell&#39;API Live](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=it)

[Prova l'API live in Google AI Studiomic](https://aistudio.google.com/live?hl=it)
[Clona app di esempio da GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Utilizza le competenze dell'agente di codificaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)

## Casi d'uso

L'API Live può essere utilizzata per creare agenti vocali in tempo reale per una
varietà di settori, tra cui:

- **E-commerce e vendita al dettaglio:** assistenti per lo shopping che offrono consigli personalizzati e agenti di assistenza che risolvono i problemi dei clienti.
- **Gaming**:personaggi non giocanti (NPC) interattivi, assistenti di aiuto in-game e traduzione in tempo reale dei contenuti in-game.
- **Interfacce di nuova generazione**:esperienze abilitate per voce e video in robotica,
  occhiali smart e veicoli.
- **Sanità**:assistenti per la salute per l'assistenza e l'istruzione dei pazienti.
- **Servizi finanziari**:consulenti AI per la gestione patrimoniale e la consulenza
  sugli investimenti.
- **Istruzione**:mentori AI e compagni di apprendimento che forniscono istruzioni e feedback personalizzati.
- **Traduzione e localizzazione**:traduzione in tempo reale e a bassa latenza di conversazioni parlate, consentendo una comunicazione multilingue senza interruzioni.

## Funzionalità principali

L'API Live offre un insieme completo di funzionalità per la creazione di agenti vocali robusti:

- [**Supporto multilingue**](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#supported-languages):
  Parla in 70 lingue supportate.
- [**Interruzione**](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#interruptions):
  Gli utenti possono interrompere il modello in qualsiasi momento per interazioni reattive.
- [**Uso di strumenti**](https://ai.google.dev/gemini-api/docs/live-tools?hl=it):
  Integra strumenti come la chiamata di funzioni e la Ricerca Google per interazioni dinamiche.
- [**Trascrizioni audio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#audio-transcription):
  Fornisce trascrizioni di testo sia dell'input dell'utente che dell'output del modello.
- [**Audio proattivo**](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#proactive-audio):
  Consente di controllare quando e in quali contesti il modello risponde.
- [**Dialogo empatico**](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#affective-dialog):
  Adatta lo stile e il tono della risposta in base all'espressione dell'input dell'utente.
- [**Traduzione dal vivo**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=it):
  Traduzione vocale in tempo reale in oltre 70 lingue.

## Specifiche tecniche

La seguente tabella descrive le specifiche tecniche dell'API Live:

| Categoria | Dettagli |
| --- | --- |
| Modalità di input | Audio (audio PCM a 16 bit non elaborato, 16 kHz, little-endian), immagini (JPEG <= 1 FPS), testo |
| Modalità di output | Audio (audio PCM a 16 bit non elaborato, 24 kHz, little-endian) |
| Protocollo | Connessione WebSocket con stato (WSS) |

## Scegliere un approccio di implementazione

Quando esegui l'integrazione con l'API Live, devi scegliere uno dei seguenti approcci di implementazione:

- **Da server a server**: il backend si connette all'API Live utilizzando
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). In genere, il client invia i dati dello stream (audio, video,
  testo) al server, che a sua volta li inoltra all'API Live.
- **Da client a server**: il codice frontend si connette direttamente all'API Live utilizzando [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) per trasmettere i dati in streaming, bypassando il backend.

## Inizia

Seleziona la guida corrispondente al tuo ambiente di sviluppo:

Server-to-server

### [Tutorial sull'SDK GenAI](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=it)

Connettiti all'API Gemini Live utilizzando l'SDK GenAI per creare un'applicazione multimodale in tempo reale con un backend Python.

Client-to-server

### [Tutorial su WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=it)

Connettiti all'API Gemini Live utilizzando WebSockets per creare un'applicazione multimodale in tempo reale con un frontend JavaScript e token effimeri.

Agent Development Kit

### [Tutorial ADK](https://google.github.io/adk-docs/streaming/)

Crea un agente e utilizza lo streaming dell'Agent Development Kit (ADK) per attivare la comunicazione vocale e video.

## Integrazioni con i partner

Per semplificare lo sviluppo di app audio e video in tempo reale, puoi utilizzare
un'integrazione di terze parti che supporta l'API Gemini Live
tramite WebRTC o WebSocket.

[LiveKit

Utilizza l'API Gemini Live con LiveKit Agents.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Crea un chatbot AI in tempo reale utilizzando Gemini Live e Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam di Software Mansion

Crea applicazioni di streaming video e audio in diretta con Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agents di Stream

Crea applicazioni AI vocali e video in tempo reale con Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

Collega le chiamate in entrata e in uscita all'API Live con Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Crea applicazioni di AI conversazionale in tempo reale con Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Inizia a utilizzare l'API Gemini Live utilizzando Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-12 UTC."],[],[]]
