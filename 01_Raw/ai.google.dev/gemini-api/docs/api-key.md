---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=de
fetched_at: 2026-08-31T06:32:07.556065+00:00
title: "Gemini API-Schl\u00fcssel verwenden \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API-Schlüssel verwenden

Wenn Sie die Gemini API verwenden möchten, müssen Sie Ihre Anfragen authentifizieren. Sie können sich mit einem Standard- oder Autorisierungs-API-Schlüssel authentifizieren.

[Gemini API-Schlüssel erstellen oder ansehen](https://aistudio.google.com/apikey?hl=de)

## API-Schlüsseltypen: Standard vs. Autorisierung

API-Schlüssel ermöglichen den Zugriff auf die Gemini API, unterscheiden sich jedoch in ihren Sicherheitsmerkmalen. Die Gemini API wird von Standard-API-Schlüsseln auf Autorisierungsschlüssel umgestellt, um die Sicherheit zu verbessern:

- **Standard-API-Schlüssel**: Verknüpfen Anfragen mit einem Google Cloud-Projekt für
  Abrechnungs- und Kontingentzwecke. Standard-API-Schlüssel identifizieren keinen Aufrufer, was die Granularität der Berechtigungen und der Zugriffssteuerung einschränkt, die sie unterstützen können.
- **Autorisierungsschlüssel**: Sind direkt an ein Google Cloud-Dienstkonto gebunden. Wenn Sie einen Autorisierungsschlüssel verwenden, werden Ihre Anfragen unter der Identität dieses gebundenen Dienstkontos verarbeitet, wodurch eine detaillierte Zugriffssteuerung möglich ist. Autorisierungsschlüssel sind standardmäßig auf die Generative Language API (Gemini API) beschränkt und bieten eine schnell wirkende Durchsetzung bei Lecks von Schlüsseln, die die Verwendung von Leck-Schlüsseln, die von unseren Systemen erkannt wurden, schnell beendet.

Um eine sichere Verwendung zu gewährleisten, wird die Gemini API von Standard-API-Schlüsseln auf Autorisierungsschlüssel umgestellt:

- **Standardmäßig Autorisierungsschlüssel**: Alle neuen API-Schlüssel, die in Google AI Studio
  werden automatisch als Autorisierungsschlüssel erstellt.
- **Nicht eingeschränkte Schlüssel werden abgelehnt**: Die Gemini API lehnt Anfragen
  von **nicht eingeschränkten Standard-API-Schlüsseln** ab. Standard-API-Schlüssel, auf die explizite Einschränkungen angewendet wurden, funktionieren weiterhin. Diese Einschränkung verhindert die unbefugte Verwendung von Schlüsseln, die öffentlich freigegeben oder mit anderen Diensten verknüpft sein könnten.
- **Im September 2026** lehnt die Gemini API Anfragen von **Standard
  API-Schlüsseln** ab. Sie müssen [vor diesem Datum zu Autorisierungsschlüsseln migrieren](#migrate-to-auth-key)
  , um Dienstunterbrechungen zu vermeiden. Migrieren Sie vor September 2026 zu Autorisierungsschlüsseln.

## API-Schlüssel in Google AI Studio verwalten

Sie können Ihre Projekte und Schlüssel direkt in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) verwalten.

### Google Cloud-Projekte

Jeder Gemini API-Schlüssel ist mit einem [Google Cloud-Projekt](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=de) verknüpft.
In Google Cloud-Projekten werden Abrechnung, Mitarbeiter und Berechtigungen verwaltet. Google AI Studio bietet eine einfache Benutzeroberfläche für den Zugriff auf diese Projekte.

- **Standardprojekt**: Wenn Sie ein neuer Nutzer sind, erstellt Google AI Studio automatisch
  ein Standard-Google Cloud-Projekt und einen API-Schlüssel, nachdem Sie die
  Nutzungsbedingungen akzeptiert haben. Sie können dieses Projekt umbenennen, indem Sie in Ihrem Dashboard zur Ansicht **Projekte** navigieren.
- **Vorhandene Projekte**: Wenn Sie bereits ein Google Cloud-Konto haben, erstellt AI
  Studio kein Standardprojekt. Stattdessen müssen Sie Ihre vorhandenen Projekte importieren.

### Projekte importieren

Standardmäßig werden in Google AI Studio nicht alle Ihre Google Cloud-Projekte angezeigt. Sie müssen die Projekte importieren, die Sie verwenden möchten:

1. Rufen Sie [Google AI Studio](https://aistudio.google.com?hl=de) auf.
2. Öffnen Sie im linken Bereich das **Dashboard** und wählen Sie **Projekte** aus.
3. Klicken Sie auf die Schaltfläche **Projekte importieren**.
4. Suchen Sie nach dem Google Cloud-Projekt, das Sie importieren möchten, wählen Sie es aus und klicken Sie auf **Importieren**.
5. Navigieren Sie nach dem Importieren im Dashboard zur Seite **API-Schlüssel**, um einen Schlüssel in diesem Projekt zu erstellen.

### Fehlerbehebung bei Berechtigungen zum Erstellen von Schlüsseln

Wenn die Schaltfläche **API-Schlüssel erstellen** nicht verfügbar ist und die Meldung
*„Sie sind nicht berechtigt, einen Schlüssel in diesem Projekt zu erstellen“* angezeigt wird, fehlen Ihnen die
erforderlichen IAM-Berechtigungen.

Bitten Sie Ihren Google Cloud-Projekt- oder -Organisationsadministrator, Ihnen eine Rolle mit den folgenden Berechtigungen zuzuweisen (z. B. Projektbearbeiter):

- `resourcemanager.projects.get`: Ermöglicht AI Studio, das Projekt zu überprüfen.
- `apikeys.keys.create`: Ermöglicht die Schlüsselerstellung.
- `serviceusage.services.enable`: Stellt sicher, dass die Generative Language API aktiviert ist.
- `iam.serviceAccounts.create`: Erforderlich, um das verknüpfte Dienstkonto zu erstellen.
- `iam.serviceAccountApiKeyBindings.create`: Bindet das Dienstkonto an den API-Schlüssel.

Wenn Sie keinen Administratorzugriff erhalten können, können Sie ein neues Google Cloud-Projekt erstellen, das nicht mit einer Organisation verknüpft ist, um Ihre Schlüssel zu generieren.

## Umgebung einrichten

Sobald Sie einen Schlüssel haben, konfigurieren Sie Ihre Umgebung so, dass er sicher in Ihren Anwendungen verwendet werden kann.

### Option 1: Umgebungsvariablen verwenden (empfohlen)

Legen Sie die Umgebungsvariable `GEMINI_API_KEY` oder `GOOGLE_API_KEY` fest. Die Gemini API-Clientbibliotheken erkennen und verwenden diese Variablen automatisch. Wenn beide festgelegt sind, hat `GOOGLE_API_KEY` Vorrang.

Wählen Sie Ihr Betriebssystem aus, um die Variable festzulegen:

### Linux/macOS – Bash

Prüfen Sie, ob Sie eine Bash-Konfigurationsdatei haben:

```
~/.bashrc
```

Wenn nicht, erstellen Sie eine und öffnen Sie sie:

```
touch ~/.bashrc && open ~/.bashrc
```

Fügen Sie am Ende der Datei den Exportbefehl hinzu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Speichern Sie die Datei und übernehmen Sie die Änderungen:

```
source ~/.bashrc
```

### macOS – Zsh

Prüfen Sie, ob Sie eine Zsh-Konfigurationsdatei haben:

```
~/.zshrc
```

Wenn nicht, erstellen Sie eine und öffnen Sie sie:

```
touch ~/.zshrc && open ~/.zshrc
```

Fügen Sie den Exportbefehl hinzu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Speichern Sie die Datei und übernehmen Sie die Änderungen:

```
source ~/.zshrc
```

### Windows

1. Suchen Sie in der Windows-Suchleiste nach „Umgebungsvariablen“.
2. Klicken Sie im Dialogfeld „Systemeigenschaften“ auf **Umgebungsvariablen**.
3. Klicken Sie unter **Benutzervariablen** oder **Systemvariablen** auf **Neu...**.
4. Legen Sie den Variablennamen auf `GEMINI_API_KEY` und den Wert auf Ihren API-Schlüssel fest.
5. Klicken Sie zum Speichern auf **OK**. Öffnen Sie eine neue Terminalsitzung, um die Variable zu laden.

### Option 2: API-Schlüssel explizit im Code angeben

Sie können den API-Schlüssel explizit übergeben, wenn Sie den Client initialisieren. Tun Sie dies nur, wenn Sie keine Umgebungsvariablen verwenden können.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
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
    "google.golang.org/genai/interactions"
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

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.6-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.6-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Sicherheits- und Secret-Verwaltung

Behandeln Sie Ihren Gemini API-Schlüssel wie ein Passwort. Wenn er kompromittiert wird, können andere das Kontingent Ihres Projekts nutzen, unerwartete Abrechnungsgebühren verursachen und auf private Ressourcen zugreifen.

### Wichtige Sicherheitsregeln

- **Schlüssel vertraulich behandeln**: Checken Sie API-Schlüssel niemals in Quellverwaltungssysteme
  wie Git ein.
- **Schlüssel in der Produktion niemals clientseitig freigeben**: Codieren Sie API-Schlüssel
  nicht direkt in Web- oder mobilen Apps. Schlüssel, die in clientseitigen Code kompiliert wurden, können von Nutzern extrahiert werden. Um clientseitige Apps zu schützen, führen Sie einen Backend-Proxyserver aus, um die eigentlichen API-Aufrufe auszuführen.

### Best Practices für die Secret-Verwaltung

- **Umgebungsvariablen**: Lesen Sie Schlüssel aus Umgebungsvariablen anstelle von
  Konfigurationsdateien.
- **Secret Manager**: Speichern Sie Ihre Schlüssel für die Produktion in einem sicheren Secret-Speicher
  wie [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=de).
- **Abrechnungsbenachrichtigungen**: Richten Sie in der Google Cloud Console Abrechnungsbenachrichtigungen ein, um
  benachrichtigt zu werden, wenn die Nutzung oder die Kosten steigen.

### Checkliste für die Reaktion auf Lecks

Wenn Sie vermuten, dass Ihr API-Schlüssel offengelegt wurde, gehen Sie so vor:

1. **Neuen Schlüssel generieren**: Erstellen Sie in Google AI Studio oder der
   Cloud Console einen Ersatzschlüssel.
2. **Anwendung aktualisieren**: Stellen Sie Ihren Code mit dem neuen Schlüssel bereit.
3. **Kompromittierten Schlüssel deaktivieren oder löschen**: Deaktivieren Sie den offengelegten Schlüssel in der
   Cloud Console, sobald der neue Schlüssel bestätigt wurde. Löschen Sie den alten Schlüssel erst, wenn der neue Schlüssel vollständig aktiv ist, um Ausfallzeiten der Anwendung zu vermeiden.
4. **Nutzung prüfen**: Prüfen Sie in der Google Cloud
   Console Abrechnungsprotokolle und API-Nutzung, um unbefugte Aktivitäten zu erkennen.

## Schlüssel einschränken und sichern

Wenn Sie Ihren API-Schlüsseln Einschränkungen hinzufügen, wird der potenzielle Schaden minimiert, falls ein Schlüssel kompromittiert wird.

### Einschränkungen für den Ursprung von Anfragen anwenden

Einschränkungen für den Ursprung beschränken, welche IP-Adressen, Websites oder Anwendungen Ihren Schlüssel verwenden können.

1. Rufen Sie in der [Google Cloud Console die Seite „Anmeldedaten“ auf](https://console.cloud.google.com/apis/credentials?hl=de).
2. Wählen Sie Ihr Projekt aus und klicken Sie auf den Namen des API-Schlüssels, den Sie einschränken möchten.
3. Wählen Sie unter **Anwendungseinschränkungen** die Option **IP-Adressen** (oder den
   entsprechenden Einschränkungstyp für Ihre Umgebung) aus.
4. Geben Sie die zulässigen IP-Adressen oder -Bereiche an und klicken Sie auf **Speichern**.

### Nicht eingeschränkte Standard-API-Schlüssel sichern

Wenn Sie die Gemini API weiterhin verwenden möchten, müssen Sie alle nicht eingeschränkten Schlüssel sichern.

#### Methode A: Schlüssel nur auf die Gemini API beschränken (AI Studio)

Wenn Sie den Schlüssel nur für die Gemini API verwenden, sichern Sie ihn direkt in AI Studio:

1. Suchen Sie auf der Seite **API-Schlüssel** in [Google AI Studio](https://aistudio.google.com/api-keys?hl=de) nach Schlüsseln, die mit dem
   **Nicht eingeschränkt** Label gekennzeichnet sind.
2. Bewegen Sie den Mauszeiger auf das Label und klicken Sie im Dialogfeld auf **Einschränkungen hinzufügen**.
3. Wählen Sie **Nur auf die Gemini API beschränken** aus.
4. Klicken Sie zur Bestätigung auf **Schlüssel einschränken**.

#### Methode B: Schlüssel für andere Dienste einschränken (Google Cloud Console)

Wenn der Schlüssel für andere Google APIs freigegeben ist (nicht empfohlen), schränken Sie ihn in der Cloud Console ein. **Hinweis: Anfragen an die Gemini API mit diesem Schlüssel schlagen fehl, nachdem
diese Einschränkungen angewendet wurden.**

1. Rufen Sie in der [Google Cloud Console die Seite „Anmeldedaten“](https://console.cloud.google.com/apis/credentials?hl=de) auf.
2. Wählen Sie das Projekt und den API-Schlüssel aus.
3. Wählen Sie unter **API-Einschränkungen** im Drop-down-Menü **API-Einschränkungen auswählen** die APIs aus, auf die dieser Schlüssel zugreifen soll. Wählen Sie nicht die **Generative Language API** aus.
4. Klicken Sie auf **Speichern**. Erstellen Sie in AI Studio einen separaten, eingeschränkten Schlüssel, um die Gemini API weiterhin verwenden zu können.

### Blockierte inaktive Schlüssel

Ab dem 7. Mai 2026 blockiert die Gemini API nicht eingeschränkte API-Schlüssel, die längere Zeit inaktiv waren. Diese Schlüssel haben in AI Studio das Tag **Blockiert**. Sie müssen einen neuen Schlüssel generieren oder einen vorhandenen eingeschränkten Schlüssel verwenden, um fortzufahren.

## Zu einem Autorisierungsschlüssel migrieren

Führen Sie die folgenden Schritte aus, um einen neuen Autorisierungs-API-Schlüssel zu erstellen und Ihre Anwendungen zu aktualisieren:

1. Rufen Sie die Seite „[API-Schlüssel](https://aistudio.google.com/api-keys?hl=de)“ in AI Studio auf.
2. Prüfen Sie in der Spalte **Schlüsseltyp** , ob Schlüssel als **Standard** aufgeführt sind.
3. Klicken Sie auf **API-Schlüssel erstellen** , um einen neuen Schlüssel zu generieren. Alle neuen Schlüssel, die in AI Studio erstellt werden, werden automatisch als Autorisierungsschlüssel erstellt.
4. Kopieren Sie den neuen Autorisierungs-API-Schlüssel.
5. Aktualisieren Sie Ihren Anwendungscode, die Umgebungsvariablen und alle Bereitstellungskonfigurationen, um den neuen Autorisierungs-API-Schlüssel zu verwenden.
6. Testen Sie Ihre Anwendung, um zu bestätigen, dass sie mit dem neuen Schlüssel ordnungsgemäß funktioniert.
7. Löschen oder widerrufen Sie nach der Bestätigung Ihren alten Trafficschlüssel, um Missbrauch zu verhindern.

## Beschränkungen

Google AI Studio unterliegt den folgenden Einschränkungen für die Projekt- und Schlüsselverwaltung:

- Sie können maximal 10 Projekte gleichzeitig auf der Seite **Projekte** in Google AI Studio erstellen.
- Auf den Seiten **API-Schlüssel** und **Projekte** werden maximal 100 Schlüssel und 50 Projekte angezeigt.
- Es werden nur API-Schlüssel angezeigt, die nicht eingeschränkt oder speziell auf die Generative Language API (Gemini API) beschränkt sind.

Für die erweiterte Projektverwaltung oder zum Ändern von Schlüsseln mit anderen Einschränkungen verwenden Sie
die [Seite „Anmeldedaten“ in der Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
