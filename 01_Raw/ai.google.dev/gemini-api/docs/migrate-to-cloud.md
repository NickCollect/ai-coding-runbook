---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=de
fetched_at: 2026-07-20T04:47:30.534496+00:00
title: "Gemini Developer API im Vergleich zur Gemini Enterprise Agent Platform \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini Developer API im Vergleich zur Gemini Enterprise Agent Platform

Für die Entwicklung von generativen KI-Lösungen mit Gemini bietet Google zwei API-Produkte an: die [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=de) und die [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=de).

Die Gemini Developer API bietet die schnellste Möglichkeit, auf Gemini basierende Anwendungen zu entwickeln, in die Produktion zu bringen und zu skalieren. Die meisten Entwickler sollten die Gemini Developer API verwenden, sofern keine speziellen Unternehmensfunktionen erforderlich sind.

Die Gemini Enterprise Agent Platform bietet ein umfassendes Ökosystem mit unternehmensgerechten Funktionen und Diensten zum Erstellen und Bereitstellen von Anwendungen mit generativer KI, die auf der Google Cloud Platform basieren.

Wir haben die Migration zwischen diesen Diensten vor Kurzem vereinfacht. Sowohl die Gemini Developer API als auch die Gemini Enterprise Agent Platform API sind jetzt über das einheitliche [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=de) zugänglich.

## Codevergleich

Auf dieser Seite finden Sie nebeneinander gestellte Codevergleiche zwischen den Schnellstarts für die Textgenerierung der Gemini Developer API und der Gemini Enterprise Agent Platform.

### Python

Sie können sowohl auf die Gemini Developer API als auch auf die Dienste der Gemini Enterprise Agent Platform über die `google-genai`-Bibliothek zugreifen. Eine Anleitung zur Installation von `google-genai` finden Sie auf der Seite [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de).

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript und TypeScript

Sie können sowohl auf die Gemini Developer API als auch auf die Dienste der Gemini Enterprise Agent Platform über die `@google/genai`-Bibliothek zugreifen. Eine Anleitung zur Installation von `@google/genai` finden Sie auf der Seite [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de).

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Ok

Sie können sowohl auf die Gemini Developer API als auch auf die Dienste der Gemini Enterprise Agent Platform über die `google.golang.org/genai`-Bibliothek zugreifen. Eine Anleitung zur Installation von `google.golang.org/genai` finden Sie auf der Seite [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de).

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Weitere Anwendungsfälle und Plattformen

Weitere Plattformen und Anwendungsfälle finden Sie in den anwendungsfallspezifischen Anleitungen in der [Gemini Developer API-Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de) und der [Dokumentation zur Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=de).

## Hinweise zur Migration

Bei der Migration gilt Folgendes:

- Für die Authentifizierung müssen Sie Google Cloud-Dienstkonten verwenden. Weitere Informationen finden Sie in der [Dokumentation zur Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=de).
- Sie können Ihr vorhandenes Google Cloud-Projekt verwenden (das, mit dem Sie Ihren API-Schlüssel generiert haben) oder [ein neues Google Cloud-Projekt erstellen](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=de).
- Die unterstützten Regionen können für die Gemini Developer API und die Gemini Enterprise Agent Platform API unterschiedlich sein. [Liste der unterstützten Regionen für generative KI in Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=de)
- Alle Modelle, die Sie in Google AI Studio erstellt haben, müssen in der Gemini Enterprise Agent Platform neu trainiert werden.

Wenn Sie Ihren Gemini API-Schlüssel für die Gemini Developer API nicht mehr benötigen, folgen Sie den Best Practices für die Sicherheit und löschen Sie ihn.

So löschen Sie einen API-Schlüssel:

1. Öffnen Sie die Seite [Google Cloud API-Anmeldedaten](https://console.cloud.google.com/apis/credentials?hl=de).
2. Suchen Sie den API-Schlüssel, den Sie löschen möchten, und klicken Sie auf das Symbol **Aktionen**.
3. Wählen Sie **API-Schlüssel löschen** aus.
4. Wählen Sie im Modal **Anmeldedaten löschen** die Option **Löschen** aus.

   Das Löschen eines API-Schlüssels dauert einige Minuten. Danach werden alle Anfragen, für die der gelöschte API-Schlüssel verwendet wird, abgelehnt.

## Nächste Schritte

- Weitere Informationen zu generativen KI-Lösungen auf der Gemini Enterprise Agent Platform finden Sie in der [Übersicht über generative KI auf der Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-22 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-22 (UTC)."],[],[]]
