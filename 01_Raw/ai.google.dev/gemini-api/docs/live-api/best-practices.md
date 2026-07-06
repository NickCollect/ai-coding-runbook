---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=de
fetched_at: 2026-07-06T05:14:30.190502+00:00
title: "Best Practices f\u00fcr die Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Best Practices für die Live API

In diesem Leitfaden werden Best Practices beschrieben, mit denen Sie die Verwendung der Live API optimieren können.
Auf der Seite [Erste Schritte mit der Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) finden Sie eine Übersicht und Beispielcode für gängige Anwendungsfälle.

## Klare Systemanweisungen erstellen

Damit die Live API optimal funktioniert, empfehlen wir, einen klar definierten Satz von Systemanweisungen zu verwenden, der die Persona des Agents, die Konversationsregeln und die Schutzmaßnahmen in dieser Reihenfolge definiert.

Um optimale Ergebnisse zu erzielen, sollten Sie für jeden Kundenservicemitarbeiter einen separaten SI erstellen.

1. **Agent-Persona angeben**:Geben Sie den Namen, die Rolle und alle bevorzugten Eigenschaften des Agenten an. Wenn Sie den Akzent angeben möchten, müssen Sie auch die bevorzugte Ausgabesprache angeben (z. B. einen britischen Akzent für einen englischen Sprecher).
2. **Regeln für die Konversation festlegen**:Geben Sie die Regeln in der Reihenfolge an, in der das Modell sie befolgen soll. Unterscheiden Sie zwischen einmaligen Elementen der Unterhaltung und Gesprächsschleifen. Beispiel:

   - **Einmaliges Element**:Erfassen Sie die Daten eines Kunden einmalig, z. B. Name, Standort, Kundenkartennummer.
   - **Konversationsschleife**:Der Nutzer kann Empfehlungen, Preise, Rückgaben und die Lieferung besprechen und möglicherweise von Thema zu Thema wechseln. Teilen Sie dem Modell mit, dass es diesen Konversationszyklus so lange fortsetzen kann, wie der Nutzer möchte.
3. **Tool-Aufrufe in einem Ablauf in separaten Sätzen angeben**:Wenn beispielsweise ein einmaliger Schritt zum Erfassen der Kundendetails den Aufruf einer `get_user_info`-Funktion erfordert, könnten Sie Folgendes sagen: *Der erste Schritt besteht darin, Nutzerinformationen zu erfassen. Bitte den Nutzer zuerst, seinen Namen, seinen Standort und seine Kundenkartennummer anzugeben. Rufen Sie dann `get_user_info` mit diesen Details auf.*
4. **Erforderliche Schutzmaßnahmen hinzufügen**:Geben Sie alle allgemeinen Konversationsschutzmaßnahmen an, die das Modell nicht ausführen soll. Sie können auch spezifische Beispiele angeben, z. B. wenn *x* passiert, soll das Modell *y* ausführen. Wenn Sie immer noch nicht die gewünschte Genauigkeit erhalten, verwenden Sie das Wort *unmissverständlich*, um das Modell zu einer präzisen Antwort zu bewegen.

## Tools präzise definieren

Wenn Sie Tools mit der Live API verwenden, müssen Sie die Tool-Definitionen genau angeben.
Geben Sie unbedingt an, unter welchen Bedingungen ein Toolaufruf erfolgen soll. Weitere Informationen finden Sie im Abschnitt mit Beispielen unter [Tool-Definitionen](#tool-definitions-example).

## Effektive Prompts erstellen

- **Klare Prompts verwenden**:Geben Sie in den Prompts Beispiele dafür an, was die Modelle tun sollen und was nicht. Beschränken Sie die Prompts auf jeweils einen Prompt pro Persona oder Rolle. Anstelle von langen, mehrseitigen Prompts sollten Sie Prompt-Chaining verwenden. Das Modell eignet sich am besten für Aufgaben mit einzelnen Funktionsaufrufen.
- **Startbefehle und Informationen angeben**:Die Live API erwartet Nutzereingaben, bevor sie antwortet. Damit die Live API die Unterhaltung beginnt, müssen Sie einen Prompt einfügen, in dem sie aufgefordert wird, den Nutzer zu begrüßen oder die Unterhaltung zu beginnen. Fügen Sie Informationen zum Nutzer hinzu, damit die Live API die Begrüßung personalisieren kann.

## Sprache angeben

Für eine optimale Leistung bei der kaskadierten `gemini-live-2.5-flash` der Live API muss die `language_code` der API mit der Sprache übereinstimmen, die vom Nutzer gesprochen wird.

Wenn das Modell in einer anderen Sprache als Englisch antworten soll, fügen Sie Folgendes in die Systemanweisungen ein:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Streaming

Beachten Sie beim Implementieren von Echtzeit-Audio die folgenden Best Practices:

- **Blockgröße und Latenz**: Senden Sie Audio in Blöcken von 20 bis 40 ms.
- **Unterbrechungen verarbeiten**: Wenn der Nutzer spricht, während das Modell antwortet, sendet der Server eine `server_content`-Nachricht mit `"interrupted": true`. Sie müssen den clientseitigen Audio-Puffer sofort verwerfen, damit der Kundenservicemitarbeiter nicht weiter über den Nutzer spricht.

## Kontextverwaltung

Verwenden Sie `ContextWindowCompressionConfig` für lange Sitzungen, da sich native Audio-Tokens schnell ansammeln (ca. 25 Tokens pro Sekunde Audio).

## Clientseitiges Puffern

Puffern Sie das eingegebene Audio nicht wesentlich (z. B. 1 Sekunde) vor dem Senden. Senden Sie kleine Chunks (20–100 ms), um die Latenz zu minimieren.

## Resampling

Ihre Clientanwendung muss Mikrofoneingaben (häufig 44,1 kHz oder 48 kHz) vor der Übertragung auf 16 kHz resamplen.

## Sitzungsverwaltung

Beachten Sie die folgenden Richtlinien, um den Sitzungslebenszyklus zu verwalten und eine zuverlässige Nutzererfahrung zu gewährleisten:

- **Kontextfenster-Komprimierung aktivieren**:Audiotokens werden mit etwa 25 Tokens pro Sekunde angesammelt. Ohne Komprimierung sind reine Audio-Sitzungen auf 15 Minuten und Audio-Video-Sitzungen auf 2 Minuten begrenzt. Aktivieren Sie die [Kontextfensterkomprimierung](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de#context-window-compression), um Sitzungen auf unbegrenzte Dauer zu verlängern.
- **Sitzungswiederaufnahme implementieren**:Der Server kann die WebSocket-Verbindung regelmäßig zurücksetzen. Mit der [Wiederaufnahme von Sitzungen](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de#session-resumption) können Sie nahtlos wieder eine Verbindung herstellen, ohne den Kontext zu verlieren. Das letzte Fortsetzungs-Token aus `SessionResumptionUpdate` Nachrichten beibehalten und beim erneuten Verbinden als Handle übergeben. Fortsetzungstokens sind 2 Stunden nach dem Beenden der letzten Sitzung gültig.
- **GoAway-Nachrichten verarbeiten**:Der Server sendet eine [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de#goaway-message)-Nachricht, bevor eine Verbindung beendet wird. Achten Sie auf diese Nachricht und verwenden Sie das Feld `timeLeft`, um die Verbindung ordnungsgemäß zu beenden oder wiederherzustellen, bevor sie geschlossen wird.
- **„generationComplete“-Signale verarbeiten**:Verwenden Sie die [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de#generation-complete-message)-Nachricht, um zu erfahren, wann das Modell die Generierung einer Antwort abgeschlossen hat. So kann Ihre Anwendung die Benutzeroberfläche aktualisieren oder mit der nächsten Aktion fortfahren.

Einzelheiten zur Implementierung finden Sie unter [Sitzungsverwaltung](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de).

## Beispiele

In diesem Beispiel werden sowohl die Best Practices als auch die [Richtlinien für das Erstellen von Systemanweisungen](#system-instruction-guidelines) kombiniert, um die Leistung des Modells als Karrierecoach zu optimieren.

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

### Tooldefinitionen

In diesem JSON-Code werden die relevanten Funktionen definiert, die im Beispiel für den Karriere-Coach aufgerufen werden.
Für optimale Ergebnisse sollten Sie beim Definieren von Funktionen deren Namen, Beschreibungen, Parameter und Aufrufbedingungen angeben.

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

## Preise und Abrechnung

Die Gemini Live API wird ausschließlich nach Tokennutzung abgerechnet. Da bei der Live API eine dauerhafte WebSocket-Sitzung aufrechterhalten wird, erfolgt die Abrechnung nach einem zusammengesetzten Modell basierend auf dem aktiven Kontextfenster.

### Das Sitzungskontextfenster (kumulative Kosten)

Die API berechnet Ihnen pro Runde alle Tokens, die im Sitzungskontextfenster vorhanden sind. Ein „Turn“ ist eine Nutzereingabe und die entsprechende Antwort des Modells.

- **Akkumulierung**:Das Kontextfenster enthält neue Tokens aus dem aktuellen Zug sowie alle akkumulierten Tokens aus vorherigen Zügen.
- **Erneute Abrechnung**:Frühere Tokens werden in jeder neuen Runde noch einmal verarbeitet und berücksichtigt, bis die von Ihnen konfigurierte Kontextfenstergröße erreicht ist. Mit zunehmender Sitzungsdauer steigen die Kosten pro Runde, da der Unterhaltungsverlauf neu verarbeitet wird.

### Audio-Tokens und ‑Transkripte

Die Live API ist nativ multimodal. Der Unterhaltungsverlauf wird als rohe Audio-Tokens beibehalten, um akustische Nuancen und den Tonfall zu bewahren.

- **Abrechnung von Audio:** Die API berechnet Ihnen die angesammelten nativen Audio-Tokens in jeder Runde zum Standardtarif für Audioeingabe.
- **Transkriptionszuschlag**:Wenn die Audio-zu-Text-Transkription aktiviert ist (`inputAudioTranscription` oder `outputAudioTranscription`), werden für alle Text-Tokens, die für die Transkription generiert werden, zusätzlich zu den Standardkosten für Audio-Tokens die Kosten für die Ausgabe von Text-Tokens berechnet.

### Kosten mit Kontextlimits verwalten

Um unbegrenztes Kostenwachstum bei langen Sitzungen zu verhindern, konfigurieren Sie die Größe des Kontextfensters mit `contextWindowCompression`.

Wenn Sie einen Komprimierungsauslöser (z. B. 25.000 Tokens) und ein gleitendes Fenster (z. B. 8.000 Tokens) festlegen, werden ältere Tokens automatisch entfernt, sobald der Schwellenwert erreicht ist. Bei nachfolgenden Anfragen werden dann nur das beibehaltene Protokoll und alle neuen Tokens in Rechnung gestellt.

### Proaktiver Audiomodus

Wenn der proaktive Audiomodus aktiviert ist, werden Eingabetokens für die gesamte Zeit berechnet, in der die Live API zuhört. Ausgabetokens werden nur berechnet, wenn die API antwortet.

- **Hinweis zu Gemini 3.1**:Der proaktive Audiomodus wird in `gemini-3.1-flash-live-preview` nicht unterstützt. Bei diesem Modell wird Ihnen Audio nur in Rechnung gestellt, wenn Sie aktiv Eingaben streamen.

Detaillierte Preisinformationen finden Sie auf der [Seite „Gemini API-Preise“](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
