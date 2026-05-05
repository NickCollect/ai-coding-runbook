---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=de
fetched_at: 2026-05-05T20:05:57.073179+00:00
title: "Gemini API \u2013 Kurzanleitung \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API – Kurzanleitung

In dieser Kurzanleitung erfahren Sie, wie Sie unsere [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de) installieren und Ihre erste Gemini API-Anfrage stellen.

## Hinweis

Für die Verwendung der Gemini API ist ein API-Schlüssel erforderlich. Sie können kostenlos einen erstellen, um loszulegen.

[Gemini API-Schlüssel erstellen](https://aistudio.google.com/app/apikey?hl=de)

## Google GenAI SDK installieren

### Python

Installieren Sie mit [Python 3.9+](https://www.python.org/downloads/) das [`google-genai`-Paket](https://pypi.org/project/google-genai/) mit dem folgenden [pip-Befehl](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Installieren Sie mit [Node.js v18+](https://nodejs.org/en/download/package-manager) das [Google Gen AI SDK für TypeScript und JavaScript](https://www.npmjs.com/package/@google/genai) mit dem folgenden [npm-Befehl](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

### Ok

Installieren Sie [google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) in Ihrem Modulverzeichnis mit dem [Befehl „go get“](https://go.dev/doc/code):

```
go get google.golang.org/genai
```

### Java

Wenn Sie Maven verwenden, können Sie [google-genai](https://github.com/googleapis/java-genai) installieren, indem Sie Ihren Abhängigkeiten Folgendes hinzufügen:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

Installieren Sie [googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) in Ihrem Modulverzeichnis mit dem [dotnet add-Befehl](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add).

```
dotnet add package Google.GenAI
```

### Apps Script

1. Wenn Sie ein neues Apps Script-Projekt erstellen möchten, rufen Sie [script.new](https://script.google.com/u/0/home/projects/create?hl=de) auf.
2. Klicken Sie auf **Unbenanntes Projekt**.
3. Benennen Sie das Apps Script-Projekt in **AI Studio** um und klicken Sie auf **Umbenennen**.
4. [API-Schlüssel](https://developers.google.com/apps-script/guides/properties?hl=de#manage_script_properties_manually) festlegen
   1. Klicken Sie links auf **Projekteinstellungen** ![Symbol für die Projekteinstellungen](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
   2. Klicken Sie unter **Skripteigenschaften** auf **Skripteigenschaft hinzufügen**.
   3. Geben Sie unter **Property** den Schlüsselnamen `GEMINI_API_KEY` ein.
   4. Geben Sie für **Wert** den Wert für den API-Schlüssel ein.
   5. Klicken Sie auf **Skripteigenschaften speichern**.
5. Ersetzen Sie den Inhalt der Datei `Code.gs` durch den folgenden Code:

## Erste Anfrage senden

Hier ist ein Beispiel, in dem die Methode [`generateContent`](https://ai.google.dev/api/generate-content?hl=de#method:-models.generatecontent) verwendet wird, um eine Anfrage mit dem Modell Gemini 2.5 Flash an die Gemini API zu senden.

Wenn Sie Ihren [API-Schlüssel](https://ai.google.dev/gemini-api/docs/api-key?hl=de#set-api-env-var) als Umgebungsvariable `GEMINI_API_KEY` festlegen, wird er automatisch vom Client übernommen, wenn Sie die [Gemini API-Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de) verwenden.
Andernfalls müssen Sie [Ihren API-Schlüssel](https://ai.google.dev/gemini-api/docs/api-key?hl=de#provide-api-key-explicitly) als Argument beim Initialisieren des Clients übergeben.

Beachten Sie, dass in allen Codebeispielen in der Gemini API-Dokumentation davon ausgegangen wird, dass Sie die Umgebungsvariable `GEMINI_API_KEY` festgelegt haben.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Nächste Schritte

Nachdem Sie Ihre erste API-Anfrage gesendet haben, können Sie sich die folgenden Anleitungen ansehen, in denen Gemini in Aktion gezeigt wird:

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de)
- [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)
- [Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de)
- [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de)
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
- [Langer Kontext](https://ai.google.dev/gemini-api/docs/long-context?hl=de)
- [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
