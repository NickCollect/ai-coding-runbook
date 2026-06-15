---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=de
fetched_at: 2026-06-15T06:31:01.874508+00:00
title: "Gemini API-Schl\u00fcssel verwenden \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API-Schlüssel verwenden

Wenn Sie die Gemini API verwenden möchten, müssen Sie Ihre Anfragen authentifizieren. Sie können sich mit einem Standard- oder Autorisierungs-API-Schlüssel authentifizieren.

[Gemini API-Schlüssel erstellen oder ansehen](https://aistudio.google.com/apikey?hl=de)

## API-Schlüsseltypen: Standard- und Autorisierungsschlüssel

API-Schlüssel ermöglichen den Zugriff auf die Gemini API, aber ihre Sicherheitsmerkmale unterscheiden sich. Die Gemini API wird von Standard-API-Schlüsseln auf Autorisierungsschlüssel umgestellt, um die Sicherheit zu verbessern:

- **Standard-API-Schlüssel**: Verknüpfen Anfragen mit einem Google Cloud-Projekt für Abrechnungs- und Kontingentzwecke. Mit Standardschlüsseln wird kein Aufrufer identifiziert. Daher ist die Granularität der Berechtigungen und der Zugriffssteuerung, die sie unterstützen können, begrenzt.
- **Autorisierungsschlüssel**: Direkt an ein Google Cloud-Dienstkonto gebunden. Wenn Sie einen Autorisierungsschlüssel verwenden, werden Ihre Anfragen unter der Identität des verknüpften Dienstkontos verarbeitet. So können Sie den Zugriff detailliert steuern. Autorisierungsschlüssel sind standardmäßig auf die Generative Language API (Gemini API) beschränkt und ermöglichen eine schnelle Durchsetzung bei geleakten Schlüsseln. Die Verwendung von geleakten Schlüsseln, die von unseren Systemen erkannt werden, wird so schnell unterbunden.

Um eine sichere Nutzung zu gewährleisten, wird bei der Gemini API von Standardschlüsseln auf Authentifizierungsschlüssel umgestellt:

- **Standardmäßige Autorisierungsschlüssel**: Alle neuen API-Schlüssel, die in Google AI Studio erstellt werden, werden automatisch als Autorisierungsschlüssel erstellt.
- **Am 19. Juni 2026**: Die Gemini API lehnt Anfragen von **nicht eingeschränkten Standardschlüsseln** ab. Standard-API-Schlüssel, für die explizite Einschränkungen gelten, funktionieren weiterhin. Diese Einschränkung verhindert die unbefugte Verwendung von Schlüsseln, die möglicherweise öffentlich freigegeben oder mit anderen Diensten verknüpft sind.
- **September 2026**: Die Gemini API lehnt Anfragen von **Standardschlüsseln** ab. Sie müssen [vor diesem Datum zu Authentifizierungsschlüsseln migrieren](#migrate-to-auth-key), um Dienstunterbrechungen zu vermeiden. Migrieren Sie vor September 2026 zu Authentifizierungsschlüsseln.

## API-Schlüssel in Google AI Studio verwalten

Sie können Ihre Projekte und Schlüssel direkt in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) verwalten.

### Google Cloud-Projekte

Jeder Gemini API-Schlüssel ist mit einem [Google Cloud-Projekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=de) verknüpft.
In Google Cloud-Projekten werden Abrechnung, Mitbearbeiter und Berechtigungen verwaltet. Google AI Studio bietet eine einfache Oberfläche für den Zugriff auf diese Projekte.

- **Standardprojekt**: Wenn Sie ein neuer Nutzer sind, werden in Google AI Studio automatisch ein Standard-Google Cloud-Projekt und ein API-Schlüssel erstellt, nachdem Sie die Nutzungsbedingungen akzeptiert haben. Sie können dieses Projekt umbenennen, indem Sie in Ihrem Dashboard zur Ansicht **Projekte** wechseln.
- **Vorhandene Projekte**: Wenn Sie bereits ein Google Cloud-Konto haben, wird in AI Studio kein Standardprojekt erstellt. Stattdessen müssen Sie Ihre vorhandenen Projekte importieren.

### Projekte importieren

Standardmäßig werden in Google AI Studio nicht alle Ihre Google Cloud-Projekte angezeigt. Sie müssen die Projekte importieren, die Sie verwenden möchten:

1. Rufen Sie [Google AI Studio](https://aistudio.google.com?hl=de) auf.
2. Öffnen Sie das **Dashboard** im linken Bereich und wählen Sie **Projekte** aus.
3. Klicken Sie auf die Schaltfläche **Projekte importieren**.
4. Suchen Sie nach dem Google Cloud-Projekt, das Sie importieren möchten, und wählen Sie es aus. Klicken Sie dann auf **Importieren**.
5. Rufen Sie nach dem Importieren im Dashboard die Seite **API-Schlüssel** auf, um einen Schlüssel in diesem Projekt zu erstellen.

### Fehlerbehebung bei Berechtigungen zum Erstellen von Schlüsseln

Wenn die Schaltfläche **API-Schlüssel erstellen** nicht verfügbar ist und die Meldung *Sie sind nicht berechtigt, in diesem Projekt einen Schlüssel zu erstellen* angezeigt wird, fehlen Ihnen die erforderlichen IAM-Berechtigungen.

Bitten Sie Ihren Google Cloud-Projekt- oder Organisationsadministrator, Ihnen eine Rolle mit den folgenden Berechtigungen zuzuweisen, z. B. „Projektbearbeiter“:

- `resourcemanager.projects.get`: Ermöglicht AI Studio, das Projekt zu überprüfen.
- `apikeys.keys.create`: Ermöglicht die Schlüsselgenerierung.
- `serviceusage.services.enable`: Stellt sicher, dass die Generative Language API aktiviert ist.
- `iam.serviceAccounts.create`: Erforderlich, um das verknüpfte Dienstkonto zu erstellen.
- `iam.serviceAccountApiKeyBindings.create`: Bindet das Dienstkonto an den API-Schlüssel.

Wenn Sie keinen Administratorzugriff erhalten können, können Sie ein neues Google Cloud-Projekt erstellen, das nicht mit einer Organisation verknüpft ist, um Ihre Schlüssel zu generieren.

## Umgebung einrichten

Nachdem Sie einen Schlüssel haben, konfigurieren Sie Ihre Umgebung so, dass er sicher in Ihren Anwendungen verwendet wird.

### Umgebungsvariablen verwenden (empfohlen)

Legen Sie die Umgebungsvariable `GEMINI_API_KEY` oder `GOOGLE_API_KEY` fest. Die Gemini API-Clientbibliotheken erkennen und verwenden diese Variablen automatisch. Wenn beide festgelegt sind, hat `GOOGLE_API_KEY` Vorrang.

Wählen Sie Ihr Betriebssystem aus, um die Variable festzulegen:

### Linux/macOS – Bash

Prüfen Sie, ob Sie eine Bash-Konfigurationsdatei haben:

```
~/.bashrc
```

Falls nicht, erstellen Sie eine und öffnen Sie sie:

```
touch ~/.bashrc && open ~/.bashrc
```

Fügen Sie am Ende der Datei den Exportbefehl hinzu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Speichern Sie die Datei und wenden Sie dann die Änderungen an:

```
source ~/.bashrc
```

### macOS – Zsh

Prüfen Sie, ob Sie eine ZSH-Konfigurationsdatei haben:

```
~/.zshrc
```

Falls nicht, erstellen Sie eine und öffnen Sie sie:

```
touch ~/.zshrc && open ~/.zshrc
```

Fügen Sie den Exportbefehl hinzu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Speichern Sie die Datei und wenden Sie dann die Änderungen an:

```
source ~/.zshrc
```

### Windows

1. Suchen Sie in der Windows-Suchleiste nach „Umgebungsvariablen“.
2. Klicken Sie im Dialogfeld „Systemeigenschaften“ auf **Umgebungsvariablen**.
3. Klicken Sie unter **Nutzervariablen** oder **Systemvariablen** auf **Neu…**.
4. Legen Sie den Variablennamen auf `GEMINI_API_KEY` und den Wert auf Ihren API-Schlüssel fest.
5. Klicken Sie zum Speichern auf **OK**. Öffnen Sie eine neue Terminalsitzung, um die Variable zu laden.

### API-Schlüssel explizit im Code angeben

Sie können den API-Schlüssel explizit übergeben, wenn Sie den Client initialisieren. Tun Sie dies nur, wenn Sie keine Umgebungsvariablen verwenden können.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
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
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
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

## Sicherheits- und Secret-Verwaltung

Behandeln Sie Ihren Gemini API-Schlüssel wie ein Passwort. Wenn Ihr Projekt manipuliert wird, können andere das Kontingent Ihres Projekts nutzen, unerwartete Abrechnungsgebühren verursachen und auf private Ressourcen zugreifen.

### Kritische Sicherheitsregeln

- **Schlüssel vertraulich behandeln**: Checken Sie API-Schlüssel niemals in Quellcodeverwaltungssysteme wie Git ein.
- **Schlüssel niemals clientseitig in der Produktion preisgeben**: API-Schlüssel dürfen nicht direkt in Web- oder mobilen Apps hartcodiert werden. Schlüssel, die in clientseitigem Code kompiliert werden, können von Nutzern extrahiert werden. Um clientseitige Apps zu schützen, können Sie einen Backend-Proxyserver ausführen, über den die eigentlichen API-Aufrufe erfolgen.

### Best Practices für die Secret-Verwaltung

- **Umgebungsvariablen**: Schlüssel werden aus Umgebungsvariablen anstatt aus Konfigurationsdateien gelesen.
- **Secret Manager**: Speichern Sie Ihre Schlüssel für die Produktion in einem sicheren Secret-Speicher wie [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=de).
- **Abrechnungsbenachrichtigungen**: Richten Sie in der Google Cloud Console Abrechnungsbenachrichtigungen ein, um benachrichtigt zu werden, wenn die Nutzung oder die Kosten steigen.

### Checkliste für die Reaktion auf Datenlecks

Wenn Sie vermuten, dass Ihr API-Schlüssel offengelegt wurde, gehen Sie so vor:

1. **Neuen Schlüssel generieren**: Erstellen Sie einen Ersatzschlüssel in Google AI Studio oder in der Cloud Console.
2. **Anwendung aktualisieren**: Stellen Sie Ihren Code mit dem neuen Schlüssel bereit.
3. **Manipulierten Schlüssel deaktivieren oder löschen**: Deaktivieren Sie den geleakten Schlüssel in der Cloud Console, sobald der neue Schlüssel bestätigt wurde. Löschen Sie den alten Schlüssel erst, wenn der neue Schlüssel vollständig aktiv ist, um Ausfallzeiten der Anwendung zu vermeiden.
4. **Nutzung prüfen**: Prüfen Sie Abrechnungslogs und API-Nutzung in der Google Cloud Console, um unautorisierte Aktivitäten zu erkennen.

## Schlüssel einschränken und schützen

Wenn Sie Ihren API-Schlüsseln Einschränkungen hinzufügen, minimieren Sie den potenziellen Schaden, falls ein Schlüssel manipuliert wird.

### Einschränkungen für den Ursprung von Anfragen anwenden

Mit Ursprungseinschränkungen wird festgelegt, welche IP-Adressen, Websites oder Anwendungen Ihren Schlüssel verwenden dürfen.

1. Rufen Sie die [Seite „Anmeldedaten“ in der Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=de) auf.
2. Wählen Sie Ihr Projekt aus und klicken Sie auf den Namen des API-Schlüssels, den Sie einschränken möchten.
3. Wählen Sie unter **Anwendungseinschränkungen** die Option **IP-Adressen** (oder den für Ihre Umgebung geeigneten Einschränkungstyp) aus.
4. Geben Sie die zulässigen IP-Adressen oder ‑Bereiche an und klicken Sie auf **Speichern**.

### Uneingeschränkte Standard-API-Schlüssel sichern

Wenn Sie die Gemini API nach dem 19. Juni 2026 weiterhin verwenden möchten, müssen Sie alle nicht eingeschränkten Schlüssel sichern.

#### Schlüssel über AI Studio nur auf die Gemini API beschränken

Wenn Sie den Schlüssel nur für die Gemini API verwenden, können Sie ihn direkt in AI Studio schützen:

1. Suchen Sie auf der Seite **API-Schlüssel** in [Google AI Studio](https://aistudio.google.com/api-keys?hl=de) nach Schlüsseln, die mit dem Label **Uneingeschränkt** gekennzeichnet sind.
2. Bewegen Sie den Mauszeiger auf das Label und klicken Sie im Dialogfeld auf **Einschränkungen hinzufügen**.
3. Wählen Sie **Nur auf Gemini API beschränken** aus.
4. Klicken Sie zur Bestätigung auf **Schlüssel einschränken**.

#### Schlüssel für andere Dienste über die Google Cloud Console einschränken

Wenn der Schlüssel für andere Google-APIs freigegeben ist (nicht empfohlen), schränken Sie ihn in der Cloud Console ein. **Hinweis: Gemini API-Anfragen mit diesem Schlüssel schlagen fehl, nachdem diese Einschränkungen angewendet wurden.**

1. Rufen Sie die [Seite „Anmeldedaten“ in der Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=de) auf.
2. Wählen Sie das Projekt und den API-Schlüssel aus.
3. Wählen Sie unter **API-Einschränkungen** die Option **Schlüssel einschränken** aus.
4. Wählen Sie im Drop-down-Menü die APIs aus, auf die mit diesem Schlüssel zugegriffen werden soll. Wählen Sie nicht die **Generative Language API** aus.
5. Klicken Sie auf **Speichern**. Erstellen Sie in AI Studio einen separaten, eingeschränkten Schlüssel, um die Gemini API weiterhin verwenden zu können.

### Blockierte inaktive Schlüssel

Ab dem 7. Mai 2026 werden nicht eingeschränkte API-Schlüssel, die über einen längeren Zeitraum nicht verwendet wurden, von der Gemini API blockiert. Für diese Schlüssel wird in AI Studio das Tag **Gesperrt** angezeigt. Sie müssen einen neuen Schlüssel generieren oder einen vorhandenen eingeschränkten Schlüssel verwenden, um fortzufahren.

## Zu einem Authentifizierungsschlüssel migrieren

So erstellen Sie einen neuen API-Schlüssel für die Authentifizierung und aktualisieren Ihre Anwendungen:

1. Rufen Sie die Seite [AI Studio-API-Schlüssel](https://aistudio.google.com/api-keys?hl=de) auf.
2. Sehen Sie in der Spalte **Key Type** (Schlüsseltyp) nach, ob Schlüssel als **Standard** aufgeführt sind.
3. Klicken Sie auf **API-Schlüssel erstellen**, um einen neuen Schlüssel zu generieren. Alle neuen Schlüssel, die in AI Studio erstellt werden, sind automatisch Autorisierungsschlüssel.
4. Kopieren Sie den neuen API-Schlüssel für die Authentifizierung.
5. Aktualisieren Sie Ihren Anwendungscode, Ihre Umgebungsvariablen und alle Bereitstellungskonfigurationen, um den neuen API-Schlüssel für die Authentifizierung zu verwenden.
6. Testen Sie Ihre Anwendung, um zu prüfen, ob sie mit dem neuen Schlüssel ordnungsgemäß funktioniert.
7. Löschen oder widerrufen Sie nach der Bestätigung Ihren alten Traffic-Schlüssel, um Missbrauch zu verhindern.

## Beschränkungen

Für Google AI Studio gelten die folgenden Einschränkungen für die Projekt- und Schlüsselverwaltung:

- Sie können maximal 10 Projekte gleichzeitig über die Seite **Projekte** in Google AI Studio erstellen.
- Auf den Seiten **API-Schlüssel** und **Projekte** werden maximal 100 Schlüssel und 50 Projekte angezeigt.
- Es werden nur API-Schlüssel angezeigt, die uneingeschränkt sind oder speziell auf die Generative Language API (Gemini API) beschränkt sind.

Für die erweiterte Projektverwaltung oder zum Ändern von Schlüsseln mit anderen Einschränkungen verwenden Sie die [Seite „Anmeldedaten“ in der Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-11 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-11 (UTC)."],[],[]]
