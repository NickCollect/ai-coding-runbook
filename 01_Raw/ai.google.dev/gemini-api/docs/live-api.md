---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=de
fetched_at: 2026-05-25T05:28:35.742702+00:00
title: "Gemini Live API overview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini Live API overview

Die Live API ermöglicht latenzarme Sprach- und Bildinteraktionen mit Gemini in Echtzeit. Sie verarbeitet kontinuierliche Streams von Audio, Bildern und Text, um sofortige, menschenähnliche gesprochene Antworten zu liefern und so eine natürliche Unterhaltung für Ihre Nutzer zu ermöglichen.

![Live API – Übersicht](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=de)

[Live API in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?hl=de)
[Beispiel-Apps von GitHub klonencode](https://github.com/google-gemini/gemini-live-api-examples)
[Agenten-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de)

## Anwendungsfälle

Mit der Live API können Sprachagenten in Echtzeit für eine Vielzahl von Branchen entwickelt werden, darunter:

- **E-Commerce und Einzelhandel**:Einkaufsassistenten, die personalisierte Empfehlungen geben, und Kundenservicemitarbeiter, die Kundenprobleme lösen.
- **Gaming**:Interaktive Non-Player Characters (NPCs), In-Game-Hilfeassistenten und Echtzeitübersetzung von In-Game-Inhalten.
- **Schnittstellen der nächsten Generation**:Sprach- und videofähige Erlebnisse in Robotik, Smart Glasses und Fahrzeugen.
- **Gesundheitswesen**:Gesundheitsbegleiter für die Unterstützung und Aufklärung von Patienten.
- **Finanzdienstleistungen**:KI-Berater für die Vermögensverwaltung und Anlageberatung.
- **Bildung**:KI-Mentoren und Lernbegleiter, die personalisierte Anleitungen und Feedback geben.

## Wichtige Features

Die Live API bietet eine umfassende Reihe von Funktionen zum Erstellen robuster Sprachagenten:

- [**Mehrsprachiger Support**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#supported-languages):
  Unterhaltungen in 70 unterstützten Sprachen.
- [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#interruptions):
  Nutzer können das Modell jederzeit unterbrechen, um reaktionsschnelle Interaktionen zu ermöglichen.
- [**Tool-Nutzung**](https://ai.google.dev/gemini-api/docs/live-tools?hl=de):
  Tools wie Funktionsaufrufe und die Google Suche für dynamische
  Interaktionen einbinden.
- [**Audio-Transkriptionen**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#audio-transcription):
  Texttranskripte der Nutzereingabe und der Modellausgabe bereitstellen.
- [**Proaktives Audio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#proactive-audio):
  Sie können festlegen, wann und in welchen Kontexten das Modell antwortet.
- [**Affektiver Dialog**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#affective-dialog):
  Antwortstil und Tonfall an die Ausdrucksweise des Nutzers anpassen.

## Technische Spezifikationen

In der folgenden Tabelle sind die technischen Spezifikationen für die Live API aufgeführt:

| Kategorie | Details |
| --- | --- |
| Eingabemodalitäten | Audio (rohes 16-Bit-PCM-Audio, 16 kHz, Little-Endian), Bilder (JPEG <= 1 FPS), Text |
| Ausgabemodalitäten | Audio (rohes 16-Bit-PCM-Audio, 24 kHz, Little-Endian) |
| Protokoll | Zustandsbehaftete WebSocket-Verbindung (WSS) |

## Implementierungsansatz auswählen

Bei der Einbindung in die Live API müssen Sie einen der folgenden Implementierungsansätze auswählen:

- **Server-zu-Server**: Ihr Back-End stellt über
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) eine Verbindung zur Live API her. In der Regel sendet Ihr Client Streamdaten (Audio, Video, Text) an Ihren Server, der sie dann an die Live API weiterleitet.
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

## Jetzt starten

Wählen Sie die Anleitung aus, die zu Ihrer Entwicklungsumgebung passt:

Server-zu-Server

### [GenAI SDK-Tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de)

Stellen Sie mit dem GenAI SDK eine Verbindung zur Gemini Live API her, um eine multimodale Echtzeitanwendung mit einem Python-Back-End zu erstellen.

Client-zu-Server

### [WebSocket-Tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=de)

Stellen Sie mit WebSockets eine Verbindung zur Gemini Live API her, um eine multimodale Echtzeitanwendung mit einem JavaScript-Front-End und ephemeren Tokens zu erstellen.

Agent Development Kit

### [ADK-Tutorial](https://google.github.io/adk-docs/streaming/)

Erstellen Sie einen Agenten und verwenden Sie das Agent Development Kit (ADK) Streaming, um die Sprach- und Videokommunikation zu aktivieren.

## Einbindung in Partnerlösungen

Um die Entwicklung von Audio- und Video-Apps in Echtzeit zu optimieren, können Sie
eine Drittanbieterintegration verwenden, die die Gemini Live
API über WebRTC oder WebSockets unterstützt.

[LiveKit

Gemini Live API mit LiveKit-Agenten verwenden](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat von Daily

Echtzeit-KI-Chatbot mit Gemini Live und Pipecat erstellen](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam von Software Mansion

Live-Video- und -Audiostreaming-Anwendungen mit Fishjam erstellen](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agents von Stream

KI-Anwendungen für Audio und Video in Echtzeit mit Vision Agents erstellen](https://visionagents.ai/integrations/gemini)
[Voximplant

Eingehende und ausgehende Anrufe mit Voximplant mit der Live API verbinden](https://voximplant.com/products/gemini-client)
[Agora

Konversationelle KI-Anwendungen in Echtzeit mit Agora erstellen](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Erste Schritte mit der Gemini Live API mit Firebase AI Logic](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
