---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=de
fetched_at: 2026-09-28T06:14:52.957890+00:00
title: "Files API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Files API

Gemini kann verschiedene Arten von Eingabedaten gleichzeitig verarbeiten, darunter Text, Bilder und Audio.

In diesem Leitfaden erfahren Sie, wie Sie mit der Files API mit Mediendateien arbeiten. Die grundlegenden Vorgänge sind für Audiodateien, Bilder, Videos, Dokumente und andere unterstützte Dateitypen gleich.

Eine Anleitung zu Datei-Prompts finden Sie im Abschnitt [Leitfaden zu Datei-Prompts](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide).

## Datei hochladen

Sie können die Files API verwenden, um eine Mediendatei hochzuladen. Verwenden Sie immer die Files API, wenn die Gesamtgröße der Anfrage (einschließlich der Dateien, des Text-Prompts, der Systemanweisungen usw.) größer als 100 MB ist. Für PDF-Dateien gilt ein Limit von 50 MB.

Mit dem folgenden Code wird eine Datei hochgeladen und dann in einem Aufruf von `interactions.create` verwendet.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .uri(myFile.uri().orElse(""))
        .mimeType(AudioContentMimeType.of(myFile.mimeType().orElse("audio/mp3")))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe this audio clip",
                }),
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(myFile.URI),
                    MimeType: interactions.AudioContentMimeType(myFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Metadaten für eine Datei abrufen

Sie können prüfen, ob die API die hochgeladene Datei erfolgreich gespeichert hat, und die zugehörigen Metadaten abrufen, indem Sie `files.get` aufrufen.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

String fileName = myFile.name().orElse("");
File fileMetadata = client.files.get(fileName, null);
System.out.println(fileMetadata);
```

### Go

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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileMetadata, err := client.Files.Get(ctx, myFile.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileMetadata)
}
```

### REST

```
# file_info.json was created in the upload example
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## Hochgeladene Dateien auflisten

Mit dem folgenden Code wird eine Liste aller hochgeladenen Dateien abgerufen:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;

Client client = new Client();

System.out.println("My files:");
for (File f : client.files.list(null)) {
  System.out.println("  " + f.name().orElse(""));
}
```

### Go

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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("My files:")
    for f, err := range client.Files.All(ctx) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(" ", f.Name)
    }
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Hochgeladene Dateien löschen

Dateien werden nach 48 Stunden automatisch gelöscht. Sie können eine hochgeladene Datei auch manuell löschen:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

client.files.delete(myFile.name().orElse(""), null);
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    if _, err := client.Files.Delete(ctx, myFile.Name, nil); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Nutzungsinformationen

Mit der Files API können Sie Mediendateien hochladen und mit ihnen interagieren. Mit der Files API können Sie bis zu 20 GB Dateien pro Projekt speichern. Die maximale Größe pro Datei beträgt 2 GB. Dateien werden 48 Stunden lang gespeichert.

In dieser Zeit können Sie die API verwenden, um Metadaten zu den Dateien abzurufen. Von Nutzern hochgeladene Dateien können jedoch nicht heruntergeladen werden. Sie können von Modellen generierte Dateien wie Videos mit der Methode `files.download` herunterladen. Die Files API ist in allen Regionen, in denen die Gemini API verfügbar ist, kostenlos verfügbar.

## Strategien für Dateiprompts

In diesem Abschnitt finden Sie Anleitungen und Best Practices für die Verwendung von Mediendateien mit Prompts für die Gemini API.

Die Möglichkeit, verschiedene Datentypen in Ihren Prompts zu verwenden, bietet Ihnen mehr Flexibilität bei den Aufgaben, die Sie mit der Gemini API erledigen können. Sie können dem Modell zum Beispiel ein Foto von einem leckeren Gericht senden und es bitten, einen kurzen Blogbeitrag über das Gericht zu schreiben.

|  |  |
| --- | --- |
| **Eingabeaufforderung** | **Antwort** |
| Schreibe einen kurzen, ansprechenden Blogbeitrag auf der Grundlage dieses Bildes. Er sollte eine Beschreibung der Mahlzeit auf dem Foto enthalten und über die Vorbereitung der Mahlzeit sprechen.   Kekse | Meal Prep ist eine gute Möglichkeit, Zeit und Geld zu sparen. Außerdem kann es dir helfen, dich gesünder zu ernähren. Dieses Gericht ist ein hervorragendes Beispiel für eine gesunde und leckere Mahlzeit, die im Voraus zubereitet werden kann.  Dieses Gericht besteht aus braunem Reis, geröstetem Gemüse und Hähnchen-Teriyaki. Der braune Reis ist ein gesundes und komplexes Kohlenhydrat, das dir langanhaltende Energie liefert. Das geröstete Gemüse ist eine gute Möglichkeit, deinen täglichen Bedarf an Vitaminen und Mineralstoffen zu decken, und das Hähnchen-Teriyaki ist eine köstliche und proteinreiche Option.  Dieses Gericht ist auch einfach zuzubereiten. Koche einfach den braunen Reis, brate das Gemüse und koche das Hähnchen-Teriyaki. Sobald alles gekocht ist, verteile es auf Behälter für die Essenszubereitung und bewahre es im Kühlschrank auf. So kannst du dir an hektischen Morgen einfach einen Behälter schnappen.  Wenn du auf der Suche nach einem gesunden und leckeren Gericht bist, das du im Voraus zubereiten kannst, ist dieses Gericht eine gute Wahl. Es ist reich an Nährstoffen und schmeckt köstlich. Außerdem macht es satt und zufrieden.  Auf ein gesundes und leckeres Meal Prep! |

Wenn Sie Probleme haben, die gewünschte Ausgabe von Prompts zu erhalten, in denen Mediendateien verwendet werden, können Sie einige Strategien anwenden, um die gewünschten Ergebnisse zu erzielen. In den folgenden Abschnitten finden Sie Designansätze und Tipps zur Fehlerbehebung, mit denen Sie Prompts mit multimodaler Eingabe verbessern können.

Sie können Ihre multimodalen Prompts mit den folgenden Best Practices verbessern:

- ### [Grundlagen des Prompt-Designs](#specific-instructions)

  - **Formulieren Sie spezifische Anweisungen:** Stellen Sie klare und präzise Anweisungen bereit, die möglichst wenig Raum für Fehldeutungen lassen.
  - **Ein paar Beispiele zum Prompt hinzufügen:** Verwenden Sie realistische Few-Shot-Beispiele, um zu veranschaulichen, was Sie erreichen möchten.
  - **Schritt für Schritt aufschlüsseln**: Teilen Sie komplexe Aufgaben in überschaubare Unterziele auf und führen Sie das Modell durch den Prozess.
  - **Ausgabeformat angeben**: Fordern Sie in dem Prompt an, dass die Ausgabe in dem gewünschten Format vorliegt, z. B. Markdown, JSON, HTML und mehr.
  - **Bild zuerst für Aufforderungen mit einem einzelnen Bild platzieren**: Zwar kann Gemini Bild- und -Texteingaben in beliebiger Reihenfolge verarbeiten, für Aufforderungen mit einem einzelnen Bild kann es jedoch besser sein, wenn dieses Bild (oder Video) vor der Textaufforderung platziert wird. Verwenden Sie jedoch für Aufforderungen, die Bilder erfordern, die eng mit Texten verknüpft sein müssen, die am ehesten natürliche Reihenfolge.
- ### [Fehlerbehebung bei multimodalem Prompt](#troubleshooting)

  - **Wenn das Modell aus dem relevanten Teil des Bildes keine Informationen bezieht**:Geben Sie an, aus welchen Aspekte des Bildes der Prompt Informationen abrufen soll.
  - **Wenn die Modellausgabe zu allgemein ist (nicht genug auf die Bild-/Videoeingabe zugeschnitten)** : Versuchen Sie zu Beginn des Prompts, das Modell um eine Beschreibung des Bildes oder Videos zu bitten, bevor Sie die Aufgabe beschreiben. oder bitten Sie das Modell, sich auf den Inhalt des Bildes zu beziehen.
  - **Fehlerbehebung, welcher Teil fehlgeschlagen ist**:Bitten Sie das Modell, das Bild zu beschreiben, oder bitten Sie das Modell, seine Logik zu erläutern, um das ursprüngliche Verständnis des Modells zu messen.
  - **Wenn die Eingabeaufforderung zu halluzinierten Inhalten führt**, sollten Sie die Temperatureinstellung verringern oder das Modell um kürzere Beschreibungen bitten, damit die Wahrscheinlichkeit geringer ist, dass zusätzliche Details angezeigt werden.
  - **Parameter für die Stichprobenerhebung optimieren**:Experimentieren Sie mit verschiedenen Temperatureinstellungen und „Top-K“-Auswahlen, um die Kreativität des Modells anzupassen.

### Machen Sie genaue Anweisungen

Prompts haben den größten Erfolg, wenn sie klar und detailliert sind. Wenn Sie eine bestimmte Ausgabe im Hinterkopf haben, sollten Sie diese Anforderung in den Prompt aufnehmen, damit Sie die gewünschte Ausgabe erhalten.

Wenn Sie für dieses Bild eines Flughafenboards die Anfrage an das Modell senden, nur „Dieses Bild beschreiben“ könnte es eine allgemeine Beschreibung generieren. Wenn das Modell die Zeit und die Stadt aus dem Bild parsen soll, können Sie diese Anfrage direkt in den Prompt einfügen.

| Prompt | Modellantwort |
| --- | --- |
| Beschreiben Sie dieses Bild. | Auf dem Bild ist eine Anzeige für Ankunfts- und Abflugfinfos für den Flughafen zu sehen. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Reiseplan Parsen Sie die Uhrzeit und die Stadt vom Flughafenanzeige in dem Bild in eine Liste. | - 10:50 Moskau - 11:05 Edinburgh - 11:05 London - 11:10 Bukarest - 11:30 Kiew - 11:35 Dublin - 11:45 East Midlands - 12:15 Sofia - 12:30 London - 12:30 Newcastle - 12:40 Sankt Petersburg - 12:40 London - 12:45 Manchester |

### Ein paar Beispiele hinzufügen

Das Gemini-Modell kann mehrere Eingaben akzeptieren, die es als Beispiele für das Verständnis der gewünschten Ausgabe verwenden kann. Wenn Sie diese Beispiele hinzufügen, kann das Modell die Muster leichter identifizieren und die Beziehung zwischen den angegebenen Bildern und Antworten auf das neue Beispiel anwenden. Dies wird auch als „Few-Shot“-Lernen bezeichnet.

Im folgenden Beispiel wird die ursprüngliche Ausgabe in Satzform geschrieben und enthält auch das Land (Brasilien). Angenommen, Sie möchten die Ausgabe in einem anderen Format oder Stil haben und nur die Stadt und nicht das Land benötigen. Wenn Sie Ihrer Prompt Few-Shot-Beispiele hinzufügen, können Sie das Modell so steuern, dass es antwortet, wie Sie es möchten.

| **Eingabeaufforderung** | **Modellantwort** |
| --- | --- |
| Reiseplan Bestimmen Sie die Stadt und das Wahrzeichen. | Die Sehenswürdigkeit ist die Cristo Redentor-Statue in Rio de Janeiro, Brasilien. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Bestimmen Sie die Stadt und das Wahrzeichen. Kolosseum | Stadt: Rom, Sehenswürdigkeit: Kolosseum. |
| Die Verbotene Stadt | Stadt: Peking, Sehenswürdigkeit: Verbotene Stadt |
| Die Verbotene Stadt | Stadt: Rio de Janeiro, Sehenswürdigkeit: Cristo Redentor-Statue |

### Schritt-für-Schritt-Anleitung

Bei komplexen Aufgaben wie Aufgaben, die sowohl visuelles Verständnis als auch Logik erfordern, kann es hilfreich sein, die Aufgabe in kleinere, einfachere Schritte aufzuteilen. Alternativ kann es auch sinnvoll sein, wenn Sie das Modell in Ihrem Prompt direkt bitten, schrittweise zu denken.

| Prompt | Modellantwort |
| --- | --- |
| Wann habe ich kein Toilettenpapier mehr? | Bald sind nur noch 3 Rollen übrig. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| 1. Zählen Sie zuerst, wie viele Toilettenpapierrollen auf diesem Bild zu sehen sind. 2. Ermitteln Sie dann, wie viel Toilettenpapier eine typische Person pro Tag verwendet. 3. Berechnen Sie, wie lange diese Rollen von Toilettenpapier halten. | 1. Auf diesem Bild sind drei Rollen Toilettenpapier zu sehen. 2. Eine typische Person verwendet täglich etwa 20 Blätter Toilettenpapier. 3. Wenn jede Rolle 200 Tabellenblatt enthält, hält jede Roll etwa 10 Tage lang. Daher halten die 3 Rollen etwa einen Monat. |

Mathematische Aufgaben oder andere Arten von Wortproblemen sind gute Kandidaten dafür, das Modell zu bitten, Schritt für Schritt zu denken.

| **Eingabeaufforderung** | **Antwort** |
| --- | --- |
| Was ist der vierte Begriff in der Sequenz? | -135 |

Die Antwort des Modells ist falsch. Zum Verbessern Sie können das Modell beispielsweise bitten, das Problem zu parsen, bevor es den Prompt beantwortet.

| **Eingabeaufforderung** | **Antwort** |
| --- | --- |
| Parsen Sie zuerst die Formel im Bild.  Beantworte dann anhand der Formel: „Was ist der vierte Begriff in der Folge?“. | *Klicken Sie, um das Ergebnis zu maximieren* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Setzen Sie in der Formel n = 4 ein: $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Wir kennen den Wert von b(3) nicht. Setzen Sie daher n = 3 in der Formel ein: $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Wir kennen den Wert von b(2) nicht. Setzen Sie daher n = 2 in der Formel ein: $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Da wir wissen, dass der Wert von b(1) 15 ist, setzen Sie ihn in der Formel ein: $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Nachdem wir den Wert von b(2) kennen, setzen Sie ihn in der Formel für b(3) ein: $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Nachdem wir den Wert von b(3) kennen, setzen Sie ihn in der Formel für b(4) ein: $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Daher ist der vierte Begriff in der Sequenz -405. |

Diese Modellantwort ist korrekt. Wenn Sie die Antwort jetzt noch optimieren möchten, können Sie das Modell bitten, schrittweise zu denken.

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Was ist der vierte Begriff in der Sequenz? Detaillierte Anleitung | Der erste Begriff ist 15.  Der zweite Begriff ist b(1) \* (-3) = 15 \* (-3) = -45.  Der dritte Begriff ist b(2) \* (-3) = -45 \* (-3) = 135.  Der vierte Begriff ist b(3) \* (-3) = 135 \* (-3) = -405. |

### Ausgabeformat angeben

Ein häufiges Problem besteht darin, dass die Modellausgabe in einem bestimmten Format vorliegen muss (z.B. Markdown, JSON, HTML), insbesondere wenn die Modellausgabe von einer nachgelagerten Aufgabe aufgenommen werden muss. Sie können versuchen, eine Ausgabe in diesem Format zu erstellen, indem Sie das Modell im Prompt dazu anweisen. Hier sind zwei Beispiele:

| Prompt | Modellantwort |
| --- | --- |
| Die Tabelle in diesem Bild in das Markdown-Format parsen | ```none | Fach | Status | Zeit | Startdatum | Fällig am | | ------- | ------ | ---- | ---------- | ------ | | Mathematik | Fertig | 1,5 Std. | 29.11.2023 | 1.12.2023 | | Geografie | Fertig | 30 Min. | 2.12.2023 | 4.12.2023 | | Physik | In Bearbeitung | 2 Std. | 3.12.2023 | 5.12.2023 | | Biologie | Nicht gestartet | 6 Std. | 2.11.2016 | 6.12.2023 | ``` |

| **Eingabeaufforderung** | **Modellantwort** |
| --- | --- |
| Geben Sie eine Liste aller folgenden Attribute an:  Zutaten, Art der Küche, vegetarisch oder nicht, im JSON-Format | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### Bild zuerst für Aufforderungen mit einem einzelnen Bild platzieren

Gemini kann Bilder und Text in beliebiger Reihenfolge innerhalb eines Prompts interpretieren. Die Platzierung eines einzelnen Bildes vor dem Text-Prompt kann jedoch zu besseren Ergebnissen führen.
In den folgenden Beispielen sehen Sie, dass das Bild in jedem Prompt zuerst vor dem Text steht.

### Fehlerbehebung bei multimodalem Prompt

Möglicherweise müssen Sie Probleme mit Ihrem Prompt beheben, wenn Sie keine hilfreiche Antwort erhalten. Hier sind einige Strategien, die Sie ausprobieren können:

#### Wenn das Modell keine Informationen aus dem relevanten Bildteil abruft

Um eine spezifischere Antwort zu erhalten, können Sie angeben, aus welchen Aspekten des Bildes Informationen herausgegeben werden sollen.

| Prompt | Modellantwort |
| --- | --- |
| Wie viele Tage halten diese Windeln für ein Baby? | Die Windel halten 198 Tage, bevor sie aufgebraucht sind. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Wie lange halten diese Windeln?  Verwenden Sie das auf dem Feld angezeigte Gewicht, um das Alter des Kindes zu bestimmen. Verwenden Sie dann die Gesamtzahl der Windeln im Feld.  Teilen Sie die Gesamtzahl durch die Anzahl der Windeln, die das Kind pro Tag benötigt. | Die Verpackung enthält 198 Windeln. Die Verpackung besagt, dass die Windel für ein Kind mit einem Gewicht von 22-37 lbs gedacht sind.  Das durchschnittliche Kind in diesem Gewichtbereich ist wahrscheinlich zwischen 1 und 2 Jahren alt.  Eine Zweijährige braucht in der Regel sechs Windeln pro Tag, daher halten sie etwa 33 Tage (198/6). |

#### Wenn die Modellausgabe zu allgemein und nicht ausreichend auf die Bildeingabe zugeschnitten ist

Damit das Modell seine Antwort auf das Bild bzw. die Bilder anpassen kann, bitten Sie es, das Bild zu beschreiben, bevor das Modell die Logik ausführt.

| Prompt | Modellantwort |
| --- | --- |
| Was haben diese Bilder gemeinsam? | Alle vier Bilder sind Beispiele für Bilder im Querformat. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Beschreiben Sie zuerst im Detail, was die einzelnen Bilder enthalten. Was haben diese Bilder gemeinsam? | Das erste Bild zeigt eine Person, die einen Koffer verpackt, das zweite zeigt einen leeren Flur in einem Einkaufszentrum, das dritte Bild zeigt einen Rolle von Toilettenpapier und das vierte Bild ein dunkles und stürmisches Meer.  Die Gemeinsamkeiten zwischen diesen Bildern sind, dass sie alle Beispiele für Grenzbereiche sind. Grenzbereich sind Orte oder Situationen, die zwischen zwei anderen Orten oder Situationen liegen. Sie sind oft durch ein Gefühl von Unsicherheit oder Mehrdeutigkeit gekennzeichnet.  Das erste Bild zeigt die Person, die zwischen der zu Hause und einer Reise steht. Die zweite Abbildung zeigt den Flur zwischen zwei Geschäften. Das dritte Bild ist Toilettenpapier, das ein Bad darstellen kann. Ein Badezimmer ist ein Übergangsraum zwischen privaten und öffentlichen Bereichen. Es ist ein Ort, an dem wir uns darauf vorbereiten, die Außenwelt zu betreten und zu verlassen.  Das vierte Bild zeigt das Meer zwischen Ruhe und Sturm.  Grenzbereiche können sowohl interessant als auch unübersichtlich sein. Sie können ein Ort für einen neuen Anfang oder ein Ort mit Endungen sein. Sie können ein Ort der Reflexion oder ein Handlungsort sein. |

Sie können auch versuchen, das Modell explizit auffordern, auf den Inhalt des Bildes zu verweisen.

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Was haben diese Bilder gemeinsam? In der Antwort auf den Inhalt der Bildern verweisen | Alle Bilder beziehen sich auf Reisen. Das erste Bild zeigt eine Person, die einen Koffer packt, das zweite einen leeren Flur in einem Einkaufszentrum, das dritte einen Stapel Toilettenpapier und das vierte ein dunkles und stürmisches Meer.  Diese Bilder beziehen sich alle auf Reisen, da es alles ist, was Nutzer auf Reisen brauchen oder verwenden. Das erste Bild zeigt eine Person, die einen Koffer verpackt. Dies ist etwas, was Nutzer vor einer Reise tun. Das zweite Bild zeigt einen leeren Flur in einem Einkaufszentrum, in dem Nutzer häufig Dinge für ihre Reisen kaufen. Das dritte Bild zeigt einen Stapel von Toilettenpapier, das Menschen häufig auf Reisen verwenden. Das vierte Bild zeigt ein dunkles und stürmisches Meer. Dies ist eines der Dinge, auf die Menschen häufig auf Reisen treffen. |

Dieselben Tipps gelten auch für die Creative-Ausgabe von Bildern. Im folgenden Beispiel mit dem Kaninchen kann es hilfreich sein, das Modell explizit aufzufordern, Aspekte aus dem Bild in das Modell aufzunehmen.

| Prompt | Modellantwort |
| --- | --- |
| Kannst du mir ein Gedicht zu diesem Bild schreiben? | Kleines Kaninchen, so weich und braun,  will am liebsten im Feld abhau'n.  Die Ohren so lang, der Schwanz so klein,  Es ist so süß und trefflich fein.  Du knabberst am Gras, so grün und süß,  und rennst davon, wenn du mich siehst.  Aber ich bin immer dein Freund,  denke ich mir verträumt. |

| **Aktualisierter Prompt** | **Verbesserte Reaktion** |
| --- | --- |
| Können Sie mir ein beschreibendes und pathetisches Gedicht zu diesem Bild schreiben und den Standort einbeziehen? | Kleines Kaninchen im Grün,  Ohren, so lang und kühn.  Was siehst du in der Ferne liegen,  wohin deine Blicke fliegen?  Ist es der blaue Ozean,  funkelnd in der Sonne Bahn?  Oder die Wellen, die brechen und brüllen,  ein Rhythmus, der dich will erfüllen?  Kleines Wesen sage mir,  was nur fasziniert dich hier?  Ist es die salzige und starke Brise,  oder der Möwenruf über der Wiese?  Vielleicht ist es die Unermesslichkeit des Seins,  Die Welt, so groß und auch so klein.  Ein Ort, an dem sich Träume formen können,  und Abenteuer sich enthemmen.  Ich frage mich, was ist wohl dein Traum,  wenn du so heiter im Grase sitzt im Raum?  Möchtest du in die Tiefe vordringen,  oder bleiben an Land, wo du kannst springen?  Was auch immer es ist, kleines Kaninchen,  behalte den Eindruck dieses Wunderlichen!  In den Träumen und Wünschen Deinen,  liegt eine Welt, die du sollst vereinen. |

#### Fehlerbehebung, welcher Teil der Prompt fehlgeschlagen ist

Es ist möglicherweise schwierig zu erkennen, ob eine Eingabeaufforderung fehlgeschlagen ist, weil das Modell **nicht verstanden hat, mit welchem Bild** zu beginnen ist oder wenn es das Bild verstanden hat, nicht die richtigen **logischen Schritte ausgeführt** hat.
Um zwischen diesen Logiken zu unterscheiden, bitten Sie das Modell, den Inhalt des Bildes zu beschreiben.

Wenn das Modell im folgenden Beispiel mit Snacks antwortet, die bei Kombination mit Tee (z.B. Popcorn) überraschend sind, können Sie zuerst eine Fehlerbehebung durchführen, um festzustellen, ob das Modell richtig erkannt hat, dass das Bild Tee zeigt.

| Prompt | Prompt zur Fehlerbehebung |
| --- | --- |
| Welchen Snack kann ich in einer Minute machen, der dazu gut passe würde? | Beschreiben Sie den Inhalt des Bildes. |

Eine andere Strategie besteht darin, das Modell um seine Logik zu bitten. So können Sie gegebenenfalls ermitteln, welcher Teil der Logik aufgeschlüsselt wurde.

| Prompt | Prompt zur Fehlerbehebung |
| --- | --- |
| Welchen Snack kann ich in einer Minute machen, der dazu gut passe würde? | Welchen Snack kann ich in einer Minute machen, der dazu gut passe würde? Bitte erläutere, weshalb du sie erreicht bzw. nicht erreicht hast. |

## Nächste Schritte

- Probieren Sie aus, eigene multimodale Prompts mit [Google AI Studio](http://aistudio.google.com?hl=de) zu erstellen.
- Informationen zur Verwendung der Gemini Files API zum Hochladen von Media-Dateien und zum Einbinden in Ihre Prompts finden Sie in den Leitfäden [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=de), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=de) und [Dokumentverarbeitung](https://ai.google.dev/gemini-api/docs/document-processing?hl=de).
- Weitere Informationen zum Prompt-Design, z. B. zum Anpassen von Sampling-Parametern, finden Sie auf der Seite [Prompt-Strategien](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
