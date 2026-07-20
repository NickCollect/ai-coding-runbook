---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de
fetched_at: 2026-07-20T04:42:58.887384+00:00
title: "Logs und Datasets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Logs und Datasets

In diesem Leitfaden erfahren Sie, wie Sie Logs zur Nutzung der Gemini API im Google AI Studio-Dashboard aufrufen, um das Modellverhalten besser zu verstehen und zu sehen, wie Nutzer mit Ihren Anwendungen interagieren. Mit dem Logging können Sie die Nutzung beobachten, Fehler beheben und *optional Nutzungs
feedback an Google senden, um Gemini für Entwickler-Anwendungsfälle zu verbessern*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=de)

Alle `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` API
-Aufrufe und [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=de)-API-Aufrufe mit Ausnahme von
verwalteten KI-Agenten werden unterstützt. Dazu gehören auch Aufrufe über
[OpenAI-Kompatibilitäts](https://ai.google.dev/gemini-api/docs/openai?hl=de) endpunkte.

## Projekt-Logging konfigurieren

Standardmäßig speichert die API alle Interaktionsobjekte (`store=true`), um die Verwendung von serverseitigen Funktionen zur Statusverwaltung zu vereinfachen. Im Gegensatz dazu werden Anfragen von der Generate Content API standardmäßig nicht gespeichert. Die Speicherung muss pro Anfrage oder auf Projektebene in AI Studio aktiviert werden.

In Google [AI Studio](https://aistudio.google.com/logs?hl=de) können Sie das Logging für alle Projekte oder für bestimmte Projekte aktivieren oder
deaktivieren und diese
Einstellungen jederzeit über das Fenster **Einstellungen** auf der Seite
[Logs und Datensätze](https://aistudio.google.com/logs?hl=de) ändern. Das Logging kann unabhängig für die `generateContent` API und die
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=de) API
aktiviert oder deaktiviert werden, um das Standardverhalten für die Speicherung für ein Projekt zu ändern.

### Logging auf Anfrageebene

Das Speicher- und Logging-Verhalten unterscheidet sich je nach API:

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=de):** Anfragen werden standardmäßig gespeichert (`store=true`), um die serverseitige Statusverwaltung zu vereinfachen.
- **Generate Content API (`generateContent`)** : Anfragen werden standardmäßig nicht gespeichert (`store=false`).

So legen Sie die Eigenschaft `store` fest:

**`generateContent` API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Projektlogs in AI Studio ansehen

1. Rufen Sie in [AI Studio](https://aistudio.google.com/logs?hl=de) die Seite „Logs“ auf.
2. Wählen Sie im Drop-down-Menü ein Projekt aus.
3. Die Logs werden in der Tabelle in umgekehrter chronologischer Reihenfolge für die Interactions API angezeigt, sofern sie vorhanden sind.
4. Wenn Sie Projektlogs für die Generate Content API aufrufen möchten, aktivieren Sie diese zuerst im [Fenster „Einstellungen“](#configure-logging).

Klicken Sie auf einen Eintrag, um eine Vorschau der Nutzlast zu sehen. Sie können den vollständigen Prompt und die Antwort von Gemini sowie den Kontext aus den vorherigen Runden prüfen. Bei Anfragen an die **Interactions API** enthalten die Logs auch einen direkten Link zur `previous_interaction_id`.

## Speicheraufbewahrung für Projekte konfigurieren

[Logs laufen nach einem standardmäßigen Aufbewahrungszeitraum von
55 Tagen ab und werden zum Löschen markiert, es sei denn, sie werden in einem Datensatz gespeichert. Datensätze laufen nicht ab.](#create)
Sie können den Aufbewahrungszeitraum für die Logs eines Projekts auf maximal 7, 14, 28 oder 55 Tage festlegen.

## Datensätze erstellen und freigeben

Sie können Logs in Datensätzen speichern, um sie besser zu organisieren und zu exportieren.

- Suchen Sie auf der Seite [Logs](https://aistudio.google.com/logs?hl=de) oben die Filterleiste
  und wählen Sie eine Eigenschaft aus, nach der gefiltert werden soll.
- Wählen Sie in der gefilterten Ansicht mit den Kästchen alle oder einzelne Logs aus.
- Klicken Sie oben in der Liste auf die Schaltfläche **Datensatz erstellen**.
- Geben Sie Ihrem neuen Datensatz einen Namen und optional eine Beschreibung.
- Der gerade erstellte Datensatz wird mit der ausgewählten Gruppe von Logs angezeigt.
- Exportieren Sie den Datensatz zur weiteren Analyse als CSV-, JSONL-Dateien oder in Google Sheets.

Datensätze können für eine Reihe verschiedener Anwendungsfälle nützlich sein.

- **Challenge-Sets zusammenstellen**:Damit können Sie zukünftige Verbesserungen vorantreiben, die auf Bereiche abzielen, in denen Sie die Leistung Ihrer KI verbessern möchten.
- **Beispielsets zusammenstellen**:Zum Beispiel ein Beispiel aus der tatsächlichen Nutzung, um Antworten von einem anderen Modell zu generieren, oder eine Sammlung von Grenzfällen für Routineprüfungen vor der Bereitstellung.
- **Evaluationssets**:Sets, die die tatsächliche Nutzung wichtiger Funktionen repräsentieren, für den Vergleich mit anderen Modellen oder Systemanweisungsiterationen.

Sie können zur Forschung und Entwicklung von Gemini beitragen, indem Sie Ihre Datensätze als Demonstrationsbeispiele für Google freigeben.

## Beschränkungen

Das Logging wird derzeit für Folgendes nicht unterstützt:

- Imagen- und Veo-Modelle
- Gemini-Einbettungsmodelle
- Gemini Robotics-Modell
- Eingaben mit Videos, GIFs oder PDFs
- Öffentliche Vorabversion von KI-Agenten in der Gemini API

## Nächste Schritte

- **Prototyp mit Sitzungsverlauf:** Verwenden Sie [AI Studio Build](https://aistudio.google.com/apps?hl=de), um Apps mit Vibe Coding zu erstellen und Ihren API-Schlüssel hinzuzufügen, um einen Verlauf von Gemini API-Logs für KI-Funktionen zu aktivieren.
- **Logs mit der Gemini Batch API noch einmal ausführen:** Verwenden Sie Datensätze für die Antwortstichprobe
  und die Bewertung von Modellen oder Anwendungslogik, indem Sie Logs mit der
  [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) noch einmal ausführen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-17 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-17 (UTC)."],[],[]]
