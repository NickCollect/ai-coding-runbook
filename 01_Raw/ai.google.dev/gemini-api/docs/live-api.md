---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=it
fetched_at: 2026-05-05T13:14:27.943890+00:00
title: "Gemini Live API overview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

- [Home page](https://ai.google.dev/gemini-api/docs/Home page)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documenti](https://ai.google.dev/gemini-api/docs/Documenti)

Invia feedback

# Gemini Live API overview

L'API Live consente interazioni vocali e visive a bassa latenza e in tempo reale con
Gemini. Elabora flussi continui di audio, immagini e testo per fornire
risposte immediate e simili a quelle umane, creando un'esperienza
conversazionale naturale per i tuoi utenti.

![Panoramica dell&#39;API Live](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=it)

[Prova l'API live in Google AI Studiomic](https://ai.google.dev/gemini-api/docs/Prova l'API live in Google AI Studiomic)
[Clona app di esempio da GitHubcode](https://ai.google.dev/gemini-api/docs/Clona app di esempio da GitHubcode)
[Utilizza le competenze dell'agente di codificaterminal](https://ai.google.dev/gemini-api/docs/Utilizza le competenze dell'agente di codificaterminal)

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

## Funzionalità principali

L'API Live offre un insieme completo di funzionalità per la creazione di agenti vocali robusti:

- [**Supporto multilingue**](https://ai.google.dev/gemini-api/docs/**Supporto multilingue**):
  Parla in 70 lingue supportate.
- [**Interruzione**](https://ai.google.dev/gemini-api/docs/**Interruzione**):
  Gli utenti possono interrompere il modello in qualsiasi momento per interazioni reattive.
- [**Uso di strumenti**](https://ai.google.dev/gemini-api/docs/**Uso di strumenti**):
  integra strumenti come la chiamata di funzioni e la Ricerca Google per interazioni dinamiche.
- [**Trascrizioni audio**](https://ai.google.dev/gemini-api/docs/**Trascrizioni audio**):
  Fornisce trascrizioni di testo sia dell'input dell'utente che dell'output del modello.
- [**Audio proattivo**](https://ai.google.dev/gemini-api/docs/**Audio proattivo**):
  consente di controllare quando e in quali contesti il modello risponde.
- [**Dialogo empatico**](https://ai.google.dev/gemini-api/docs/**Dialogo empatico**):
  Adatta lo stile e il tono della risposta in base all'espressione dell'input dell'utente.

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
  [WebSockets](https://ai.google.dev/gemini-api/docs/WebSockets). In genere, il client invia i dati dello stream (audio, video,
  testo) al server, che a sua volta li inoltra all'API Live.
- **Da client a server**: il codice frontend si connette direttamente all'API Live utilizzando [WebSockets](https://ai.google.dev/gemini-api/docs/WebSockets) per trasmettere dati in streaming, bypassando il backend.

## Inizia

Seleziona la guida corrispondente al tuo ambiente di sviluppo:

Server-to-server

### [Tutorial sull'SDK GenAI](https://ai.google.dev/gemini-api/docs/Tutorial sull'SDK GenAI)

Connettiti all'API Gemini Live utilizzando l'SDK GenAI per creare un'applicazione multimodale in tempo reale con un backend Python.

Client-to-server

### [Tutorial su WebSocket](https://ai.google.dev/gemini-api/docs/Tutorial su WebSocket)

Connettiti all'API Gemini Live utilizzando WebSockets per creare un'applicazione multimodale in tempo reale con un frontend JavaScript e token effimeri.

Agent Development Kit

### [Tutorial ADK](https://ai.google.dev/gemini-api/docs/Tutorial ADK)

Crea un agente e utilizza lo streaming dell'Agent Development Kit (ADK) per attivare la comunicazione vocale e video.

## Integrazioni con i partner

Per semplificare lo sviluppo di app audio e video in tempo reale, puoi utilizzare
un'integrazione di terze parti che supporta l'API Gemini Live
tramite WebRTC o WebSockets.

[LiveKit

Utilizza l'API Gemini Live con LiveKit Agents.](https://ai.google.dev/gemini-api/docs/LiveKitUtilizza l'API Gemini Live con LiveKit Agents.)
[Pipecat by Daily

Crea un chatbot AI in tempo reale utilizzando Gemini Live e Pipecat.](https://ai.google.dev/gemini-api/docs/Pipecat by DailyCrea un chatbot AI in tempo reale utilizzando Gemini Live e Pipecat.)
[Fishjam di Software Mansion

Crea applicazioni di streaming video e audio in diretta con Fishjam.](https://ai.google.dev/gemini-api/docs/Fishjam di Software MansionCrea applicazioni di streaming video e audio in diretta con Fishjam.)
[Vision Agents di Stream

Crea applicazioni di AI vocali e video in tempo reale con Vision Agents.](https://ai.google.dev/gemini-api/docs/Vision Agents di StreamCrea applicazioni di AI vocali e video in tempo reale con Vision Agents.)
[Voximplant

Collega le chiamate in entrata e in uscita all'API Live con Voximplant.](https://ai.google.dev/gemini-api/docs/VoximplantCollega le chiamate in entrata e in uscita all'API Live con Voximplant.)
[Agora

Crea applicazioni di AI conversazionale in tempo reale con Agora.](https://ai.google.dev/gemini-api/docs/AgoraCrea applicazioni di AI conversazionale in tempo reale con Agora.)
[Firebase AI SDK

Inizia a utilizzare l'API Gemini Live con Firebase AI Logic.](https://ai.google.dev/gemini-api/docs/Firebase AI SDKInizia a utilizzare l'API Gemini Live con Firebase AI Logic.)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/licenza Creative Commons Attribution 4.0), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://ai.google.dev/gemini-api/docs/licenza Apache 2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://ai.google.dev/gemini-api/docs/norme del sito di Google Developers). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?
