---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=de
fetched_at: 2026-11-02T07:28:19.789141+00:00
title: "Google AI Studio \u2013 Kurzanleitung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Google AI Studio – Kurzanleitung

Mit [Google AI Studio](https://aistudio.google.com/?hl=de) können Sie schnell Modelle testen und mit verschiedenen Prompts experimentieren. Wenn Sie bereit sind, können Sie „Code abrufen“ und Ihre bevorzugte Programmiersprache auswählen, um die [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=de) zu verwenden.

## Prompts und Einstellungen

Google AI Studio bietet mehrere Schnittstellen für Prompts, die für verschiedene Anwendungsfälle entwickelt wurden. In diesem Leitfaden geht es um **Chat-Prompts**, die zum Erstellen von Konversationsfunktionen verwendet werden. Bei dieser Prompting-Technik sind mehrere Eingabe- und Antwortrunden möglich, um eine Ausgabe zu generieren. [Hier finden Sie ein Beispiel für einen Chat-Prompt.](#chat_example)
Weitere Optionen sind **Echtzeit-Streaming**, **Video-Gen** und mehr.

AI Studio bietet auch den Bereich **Laufeinstellungen**, in dem Sie [Modellparameter](https://ai.google.dev/docs/prompting-strategies?hl=de#model-parameters) und [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de) anpassen und Tools wie [strukturierte Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de), [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de), [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und [Fundierung](https://ai.google.dev/gemini-api/docs/grounding?hl=de) aktivieren können.

## Beispiel für einen Chat-Prompt: „Erstelle eine benutzerdefinierte Chatanwendung.“

Wenn Sie einen Allzweck-Chatbot wie [Gemini](https://gemini.google.com/?hl=de) verwendet haben, wissen Sie aus erster Hand, wie leistungsstark generative KI-Modelle für offene Dialoge sein können. Diese Allzweck-Chatbots sind zwar nützlich, müssen aber oft für bestimmte Anwendungsfälle angepasst werden.

Vielleicht möchten Sie einen Kundenservice-Chatbot erstellen, der nur Unterhaltungen unterstützt, in denen es um das Produkt eines Unternehmens geht. Vielleicht möchten Sie einen Chatbot entwickeln, der in einem bestimmten Ton oder Stil spricht, z. B. einen Bot, der viele Witze macht, sich wie ein Dichter ausdrückt oder viele Emojis in seinen Antworten verwendet.

In diesem Beispiel wird gezeigt, wie Sie mit Google AI Studio einen freundlichen Chatbot erstellen, der so kommuniziert, als wäre er ein Alien, das auf einem der Jupitermonde, Europa, lebt.

### Schritt 1: Chat-Prompt erstellen

Um einen Chatbot zu erstellen, müssen Sie Beispiele für Interaktionen zwischen einem Nutzer und dem Chatbot angeben, damit das Modell die gewünschten Antworten liefert.

So erstellen Sie einen Chat-Prompt:

1. Öffnen Sie [Google AI Studio](https://aistudio.google.com/?hl=de). Der **Playground** wird standardmäßig mit einem neuen Chat-Prompt geöffnet.
2. Klicken Sie rechts oben auf **Laufzeit-Einstellungen** tune, um das Feld zu maximieren, und suchen Sie nach dem Eingabefeld [**Systemanweisungen**](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions). Fügen Sie Folgendes in das Texteingabefeld ein:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Nachdem Sie die Systemanweisungen hinzugefügt haben, können Sie Ihre Anwendung testen, indem Sie mit dem Modell chatten:

1. Geben Sie in das Texteingabefeld mit der Bezeichnung **Geben Sie etwas ein...** eine Frage oder Beobachtung ein, die ein Nutzer stellen oder machen könnte. Beispiel:

   **Nutzer**:

   ```
   What's the weather like?
   ```
2. Klicken Sie auf den Button **Ausführen**, um eine Antwort vom Chatbot zu erhalten. Die Antwort könnte in etwa so aussehen:

   **Modell**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Schritt 2: Ihrem Bot beibringen, besser zu chatten

Mit einer einzigen Anweisung konnten Sie einen einfachen Chatbot für Europa-Aliens erstellen. Eine einzelne Anweisung reicht jedoch möglicherweise nicht aus, um Konsistenz und Qualität der Antworten des Modells zu gewährleisten. Ohne genauere Anweisungen fällt die Antwort des Modells auf eine Frage zum Wetter in der Regel sehr lang aus und kann sich verselbstständigen.

Sie können den Tonfall Ihres Chatbots anpassen, indem Sie den Systemanweisungen Folgendes hinzufügen:

1. Starten Sie einen neuen Chat-Prompt oder verwenden Sie denselben. Systemanweisungen können nach Beginn der Chatsitzung geändert werden.
2. Ändern Sie im Bereich **Systemanweisungen** die vorhandenen Anweisungen so:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Geben Sie Ihre Frage noch einmal ein (`What's the weather like?`) und klicken Sie auf die Schaltfläche **Ausführen**. Wenn Sie keinen neuen Chat gestartet haben, könnte Ihre Antwort so aussehen:

   **Modell**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

So können Sie dem Chatbot zusätzliche Informationen hinzufügen. Stellen Sie mehr Fragen, bearbeiten Sie die Antworten und verbessern Sie die Qualität Ihres Chatbots. Fügen Sie weitere Anweisungen hinzu oder ändern Sie die vorhandenen und testen Sie, wie sich das Verhalten Ihres Chatbots dadurch ändert.

### Schritt 3: Nächste Schritte

Ähnlich wie bei den anderen Aufforderungstypen können Sie, sobald Sie mit Ihrem Prototyp zufrieden sind, auf die Schaltfläche **Code abrufen** klicken, um mit dem Programmieren zu beginnen, oder Ihre Aufforderung speichern, um später daran zu arbeiten und sie mit anderen zu teilen.

## Weitere Informationen

- Wenn Sie mit dem Programmieren beginnen möchten, lesen Sie die [Startleitfäden für APIs](https://ai.google.dev/gemini-api/docs/get-started?hl=de).
- [Richtlinien zum Prompt-Design](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
