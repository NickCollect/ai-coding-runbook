---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=de
fetched_at: 2026-06-15T06:28:24.328552+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Methoden für die Dateieingabe

In diesem Leitfaden wird beschrieben, wie Sie Medien wie Bilder, Audio, Videos und Dokumente in Anfragen an die Gemini API einfügen können.
Die neuen Methoden werden in allen Gemini API-Endpunkten unterstützt, einschließlich Batch, Interactions und Live API.
Die Auswahl der richtigen Methode hängt von der Größe der Datei, dem Speicherort der Daten und der Häufigkeit ab, mit der Sie die Datei verwenden möchten.

Die einfachste Methode, eine Datei als Eingabe zu verwenden, besteht darin, eine lokale Datei zu lesen und in einen Prompt einzufügen. Im folgenden Beispiel wird gezeigt, wie eine lokale PDF-Datei gelesen wird. PDFs dürfen für diese Methode maximal 50 MB groß sein. Eine vollständige Liste der Dateieingabetypen und ‑beschränkungen finden Sie in der [Vergleichstabelle für Eingabemethoden](#method-comparison).

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## Vergleich der Eingabemethoden

In der folgenden Tabelle werden die einzelnen Eingabemethoden mit Dateibeschränkungen und Anwendungsfällen verglichen. Beachten Sie, dass die maximale Dateigröße je nach Dateityp und Modell oder Tokenizer, der zum Verarbeiten der Datei verwendet wird, variieren kann.

| Methode | Optimal für | Maximale Dateigröße | Persistenz |
| --- | --- | --- | --- |
| **Inlinedaten** | Schnelle Tests, kleine Dateien, Echtzeitanwendungen. | 100 MB pro Anfrage oder Nutzlast   (**50 MB für PDFs**) | Keine (wird mit jeder Anfrage gesendet) |
| **Datei-API-Upload** | Große Dateien, Dateien, die mehrmals verwendet werden. | 2 GB pro Datei,   bis zu 20 GB pro Projekt | 48 Stunden |
| **Registrierung von GCS-URIs für die File API** | Große Dateien, die sich bereits in Google Cloud Storage befinden, Dateien, die mehrmals verwendet werden. | 2 GB pro Datei, keine Speicherplatzbeschränkungen insgesamt | Keine (werden pro Anfrage abgerufen). Eine einmalige Registrierung kann bis zu 30 Tage lang Zugriff gewähren. |
| **Externe URLs** | Öffentliche Daten oder Daten in Cloud-Buckets (AWS, Azure, GCS), ohne sie noch einmal hochzuladen. | 100 MB pro Anfrage/Nutzlast | Keine (werden pro Anfrage abgerufen) |

## Inline-Daten

Bei kleineren Dateien (unter 100 MB oder 50 MB für PDFs) können Sie die Daten direkt im Anfrage-Payload übergeben. Dies ist die einfachste Methode für schnelle Tests oder Anwendungen, die Echtzeit- und temporäre Daten verarbeiten. Sie können Daten als base64-codierte Strings bereitstellen oder lokale Dateien direkt lesen.

Ein Beispiel für das Lesen aus einer lokalen Datei finden Sie am Anfang dieser Seite.

### Von einer URL abrufen

Sie können auch eine Datei über eine URL abrufen, sie in Byte konvertieren und in die Eingabe einfügen.

### Python

```
from google import genai
import httpx
import base64

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.5-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

Die File API ist für größere Dateien (bis zu 2 GB) oder Dateien vorgesehen, die Sie in mehreren Anfragen verwenden möchten.

### Standard-Dateiupload

Laden Sie eine lokale Datei in die Gemini API hoch. Auf diese Weise hochgeladene Dateien werden vorübergehend (48 Stunden) gespeichert und verarbeitet, damit das Modell sie effizient abrufen kann.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Google Cloud Storage-Dateien registrieren

Wenn sich Ihre Daten bereits in Google Cloud Storage befinden, müssen Sie sie nicht herunterladen und neu hochladen. Sie können sie direkt mit der File API registrieren.

1. **Dienst-Agent** Zugriff auf jeden Bucket gewähren

   1. Aktivieren Sie die Gemini API in Ihrem Google Cloud-Projekt.
   2. Dienst-Agent erstellen:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Gewähren Sie dem Gemini API-Dienst-Agent Berechtigungen** zum Lesen Ihrer Speicher-Buckets.

      Der Nutzer muss diesem Dienst-Agenten die `Storage Object Viewer`-[IAM-Rolle](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=de#storage.objectViewer) für die jeweiligen Speicher-Buckets zuweisen, die er verwenden möchte.

   Dieser Zugriff läuft nicht automatisch ab, kann aber jederzeit geändert werden. Sie können auch die Befehle des [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=de) verwenden, um Berechtigungen zu erteilen.
2. Dienst authentifizieren

   **Voraussetzungen**

   - API aktivieren
   - Erstellen Sie ein Dienstkonto oder einen Agent mit den entsprechenden Berechtigungen.

   Sie müssen sich zuerst als der Dienst authentifizieren, der über die Berechtigungen für den Storage-Objekt-Betrachter verfügt. Wie das geschieht, hängt von der Umgebung ab, in der Ihr Dateiverwaltungscode ausgeführt wird.

   **Außerhalb von Google Cloud**

   Wenn Ihr Code außerhalb von Google Cloud ausgeführt wird, z. B. auf Ihrem Computer, laden Sie die Kontoanmeldedaten mit den folgenden Schritten aus der Google Cloud Console herunter:

   1. Rufen Sie die [Dienstkontokonsole](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=de) auf.
   2. Relevantes Dienstkonto auswählen
   3. Wählen Sie den Tab **Schlüssel** aus und klicken Sie auf **Schlüssel hinzufügen, Neuen Schlüssel erstellen**.
   4. Wählen Sie den Schlüsseltyp **JSON** aus und notieren Sie sich, wohin die Datei auf Ihrem Computer heruntergeladen wurde.

   Weitere Informationen finden Sie in der offiziellen Google Cloud-Dokumentation zur [Verwaltung von Dienstkontoschlüsseln](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=de).

   Verwenden Sie dann die folgenden Befehle zur Authentifizierung. Bei diesen Befehlen wird davon ausgegangen, dass sich die Dienstkontodatei im aktuellen Verzeichnis befindet und den Namen `service-account.json` hat.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### Befehlszeile

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Mit Google Cloud**

   Wenn Sie direkt in Google Cloud ausgeführt werden, z. B. mit [Cloud Run-Funktionen](https://cloud.google.com/functions?hl=de) oder einer [Compute Engine-Instanz](https://cloud.google.com/products/compute?hl=de), haben Sie implizite Anmeldedaten, müssen sich aber neu authentifizieren, um die entsprechenden Zugriffsbereiche zu gewähren.

   ### Python

   In diesem Code wird davon ausgegangen, dass der Dienst in einer Umgebung ausgeführt wird, in der [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de) automatisch abgerufen werden können, z. B. in Cloud Run oder Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   In diesem Code wird davon ausgegangen, dass der Dienst in einer Umgebung ausgeführt wird, in der [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de) automatisch abgerufen werden können, z. B. in Cloud Run oder Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### Befehlszeile

   Dies ist ein interaktiver Befehl. Für Dienste wie Compute Engine können Sie Bereiche auf Konfigurationsebene an den ausgeführten Dienst anhängen. Ein Beispiel finden Sie in der [Dokumentation zu vom Nutzer verwalteten Diensten](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=de#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Dateiregistrierung (Files API)

   Mit der Files API können Sie Dateien registrieren und einen Files API-Pfad erstellen, der direkt in der Gemini API verwendet werden kann.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.5-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.5-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

   ### Befehlszeile

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## Externe HTTP-/signierte URLs

Sie können öffentlich zugängliche HTTPS-URLs oder vorab signierte URLs direkt in Ihrer Anfrage übergeben. Die Gemini API ruft die Inhalte während der Verarbeitung sicher ab.
Das ist ideal für Dateien mit einer Größe von bis zu 100 MB, die Sie nicht noch einmal hochladen möchten.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -H "Api-Revision: 2026-05-20" \
      -d '{
          "model": "gemini-3.5-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### Bedienungshilfen

Prüfen Sie, ob die von Ihnen angegebenen URLs zu Seiten führen, für die eine Anmeldung erforderlich ist oder die sich hinter einer Paywall befinden. Bei privaten Datenbanken müssen Sie eine signierte URL mit den richtigen Zugriffsberechtigungen und dem richtigen Ablaufdatum erstellen.

### Sicherheitschecks

Das System führt eine Inhaltsmoderationsprüfung der URL durch, um zu bestätigen, dass sie den Sicherheits- und Richtlinienstandards entspricht. Wenn die URL diese Prüfung nicht besteht, erhalten Sie eine `url_retrieval_status` mit dem Wert `URL_RETRIEVAL_STATUS_UNSAFE`.

### Unterstützte Inhaltstypen

Diese Liste der unterstützten Dateitypen und Einschränkungen dient als erste Orientierung und ist nicht vollständig. Die effektive Menge der unterstützten Typen kann sich ändern und je nach verwendetem Modell und Tokenizer-Version variieren. Nicht unterstützte Typen führen zu einem Fehler.
Außerdem werden für das Abrufen von Inhalten für diese Dateitypen nur öffentlich zugängliche URLs unterstützt.

#### Textdateitypen

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Anwendungsdateitypen

- `application/json`
- `application/pdf`

#### Bilddateitypen

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## Best Practices

- **Die richtige Methode auswählen**:Verwenden Sie Inline-Daten für kleine, vorübergehende Dateien.
  Verwenden Sie die File API für größere oder häufig verwendete Dateien. Verwenden Sie externe URLs für Daten, die bereits online gehostet werden.
- **MIME-Typen angeben**:Geben Sie immer den richtigen MIME-Typ für die Dateidaten an, damit sie richtig verarbeitet werden.
- **Fehlerbehandlung:** Implementieren Sie eine Fehlerbehandlung in Ihrem Code, um potenzielle Probleme wie Netzwerkfehler, Probleme beim Dateizugriff oder API-Fehler zu beheben.

## Beschränkungen

- Die Dateigrößenbeschränkungen variieren je nach Methode (siehe [Vergleichstabelle](#method-comparison)) und Dateityp.
- Durch Inline-Daten wird die Nutzlastgröße der Anfrage erhöht.
- File API-Uploads sind temporär und laufen nach 48 Stunden ab.
- Das Abrufen externer URLs ist auf 100 MB pro Nutzlast begrenzt und unterstützt bestimmte Inhaltstypen.

## Nächste Schritte

- Sie können auch eigene multimodale Prompts in [Google AI Studio](http://aistudio.google.com/?hl=de) erstellen.
- Informationen zum Einbinden von Dateien in Ihre Prompts finden Sie in den Anleitungen zu [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=de), [Audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=de) und [Dokumentverarbeitung](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
