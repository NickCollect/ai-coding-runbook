---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=de
fetched_at: 2026-08-03T04:32:18.422012+00:00
title: "Methoden zur Dateieingabe \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Methoden zur Dateieingabe

In dieser Anleitung werden die verschiedenen Möglichkeiten beschrieben, wie Sie Mediendateien wie Bilder, Audio, Video und Dokumente in Anfragen an die Gemini API einfügen können.
Die neuen Methoden werden in allen Gemini API-Endpunkten unterstützt, einschließlich
Batch, Interactions und Live API.
Die richtige Methode hängt von der Größe der Datei, dem aktuellen Speicherort der Daten und der Häufigkeit ab, mit der Sie die Datei verwenden möchten.

Die einfachste Möglichkeit, eine Datei als Eingabe zu verwenden, besteht darin, eine lokale Datei zu lesen und in einen Prompt einzufügen. Im folgenden Beispiel wird gezeigt, wie Sie eine lokale PDF-Datei lesen. Bei dieser Methode sind PDFs auf 50 MB begrenzt. Eine vollständige Liste der Dateieingabetypen und -beschränkungen finden Sie in der
[Vergleichstabelle für Eingabemethoden](#method-comparison).

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## Vergleich der Eingabemethoden

In der folgenden Tabelle werden die einzelnen Eingabemethoden mit Dateibeschränkungen und optimalen Anwendungsfällen verglichen. Die Dateigrößenbeschränkung kann je nach Dateityp und Modell/Tokenizer variieren, das zum Verarbeiten der Datei verwendet wird.

| Methode | Optimal für | Maximale Dateigröße | Persistenz |
| --- | --- | --- | --- |
| **Inlinedaten** | Schnelle Tests, kleine Dateien, Echtzeitanwendungen | 100 MB pro Anfrage/Nutzlast   (**50 MB für PDFs**) | Keine (wird mit jeder Anfrage gesendet) |
| **Dateiupload über die File API** | Große Dateien, Dateien, die mehrmals verwendet werden | 2 GB pro Datei,   bis zu 20 GB pro Projekt | 48 Stunden |
| **Registrierung der GCS-URI über die File API** | Große Dateien, die sich bereits in Google Cloud Storage befinden, Dateien, die mehrmals verwendet werden | 2 GB pro Datei, keine Beschränkungen für den Gesamtspeicher | Keine (wird pro Anfrage abgerufen). Durch eine einmalige Registrierung kann der Zugriff für bis zu 30 Tage gewährt werden. |
| **Externe URLs** | Öffentliche Daten oder Daten in Cloud-Buckets (AWS, Azure, GCS) ohne erneuten Upload | 100 MB pro Anfrage/Nutzlast | Keine (wird pro Anfrage abgerufen) |

## Inlinedaten

Bei kleineren Dateien (unter 100 MB oder 50 MB für PDFs) können Sie die Daten direkt in der Anfrage-Nutzlast übergeben. Dies ist die einfachste Methode für schnelle Tests oder Anwendungen, die Echtzeitdaten verarbeiten. Sie können Daten als base64-codierte Strings bereitstellen oder lokale Dateien direkt lesen.

Ein Beispiel für das Lesen aus einer lokalen Datei finden Sie am Anfang dieser Seite.

### Von einer URL abrufen

Sie können eine Datei auch von einer URL abrufen, sie in Byte umwandeln und in die Eingabe einfügen.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
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

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

Die File API ist für größere Dateien (bis zu 2 GB) oder Dateien konzipiert, die Sie in mehreren Anfragen verwenden möchten.

### Standardmäßiger Dateiupload

Laden Sie eine lokale Datei in die Gemini API hoch. Auf diese Weise hochgeladene Dateien werden vorübergehend (48 Stunden) gespeichert und für den effizienten Abruf durch das Modell verarbeitet.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
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

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### Google Cloud Storage-Dateien registrieren

Wenn sich Ihre Daten bereits in Google Cloud Storage befinden, müssen Sie sie nicht herunterladen und noch einmal hochladen. Sie können sie direkt bei der File API registrieren.

1. Gewähren Sie dem **Dienst-Agent** Zugriff auf jeden Bucket.

   1. Aktivieren Sie die Gemini API in Ihrem Google Cloud-Projekt.
   2. Erstellen Sie den Dienst-Agent:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Gewähren Sie dem Gemini API-Dienst-Agent Berechtigungen** zum Lesen Ihrer Speicher-Buckets.

      Der Nutzer muss diesem Dienst-Agent die `Storage Object Viewer`
      [IAM-Rolle](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=de#storage.objectViewer)
      für die jeweiligen Speicher-Buckets zuweisen, die er verwenden möchte.

   Dieser Zugriff läuft standardmäßig nicht ab, kann aber jederzeit geändert werden. Sie können
   auch die
   [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=de)
   -Befehle verwenden, um Berechtigungen zu gewähren.
2. Dienst authentifizieren

   **Voraussetzungen**

   - API aktivieren
   - Erstellen Sie ein Dienstkonto/einen Dienst-Agent mit den entsprechenden Berechtigungen.

   Sie müssen sich zuerst als der Dienst authentifizieren, der Berechtigungen für den Storage-Objekt-Betrachter hat. Wie das geschieht, hängt von der Umgebung ab, in der Ihr Dateiverwaltungscode ausgeführt wird.

   **Außerhalb von Google Cloud**

   Wenn Ihr Code außerhalb von Google Cloud ausgeführt wird, z. B. auf Ihrem Computer, laden Sie die Kontoberechtigungen mit den folgenden Schritten aus der Google Cloud Console herunter:

   1. Rufen Sie die [Dienstkonto-Konsole](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=de) auf.
   2. Wählen Sie das entsprechende Dienstkonto aus.
   3. Wählen Sie den Tab **Schlüssel** aus und klicken Sie auf **Schlüssel hinzufügen, Neuen Schlüssel erstellen**.
   4. Wählen Sie den Schlüsseltyp **JSON** aus und notieren Sie sich, wohin die Datei auf Ihrem Computer heruntergeladen wurde.

   Weitere Informationen finden Sie in der offiziellen Google Cloud-Dokumentation zur [Verwaltung von Dienstkontoschlüsseln](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=de).

   Verwenden Sie dann die folgenden Befehle, um sich zu authentifizieren. Bei diesen Befehlen wird davon ausgegangen, dass sich Ihre Dienstkontodatei im aktuellen Verzeichnis befindet und den Namen `service-account.json` hat.

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

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Mit Google Cloud**

   Wenn Sie direkt in Google Cloud ausgeführt werden, z. B. mit [Cloud
   Run-Funktionen](https://cloud.google.com/functions?hl=de) oder einer
   [Compute Engine-Instanz](https://cloud.google.com/products/compute?hl=de), haben Sie
   implizite Anmeldedaten, müssen sich aber noch einmal authentifizieren, um die
   entsprechenden Bereiche zu gewähren.

   ### Python

   Dieser Code geht davon aus, dass der Dienst in einer Umgebung ausgeführt wird, in der
   [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de)
   automatisch abgerufen werden können, z. B. Cloud Run oder Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Dieser Code geht davon aus, dass der Dienst in einer Umgebung ausgeführt wird, in der
   [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de)
   automatisch abgerufen werden können, z. B. Cloud Run oder Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   Dies ist ein interaktiver Befehl. Bei Diensten wie Compute Engine können Sie Bereiche auf Konfigurationsebene an den ausgeführten Dienst anhängen. Ein Beispiel finden Sie in der [Dokumentation zu vom Nutzer verwalteten Diensten](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=de#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Dateiregistrierung (Files API)

   Verwenden Sie die Files API, um Dateien zu registrieren und einen Files API-Pfad zu erstellen, der direkt in der Gemini API verwendet werden kann.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.6-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### CLI

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

Sie können öffentlich zugängliche HTTPS-URLs oder vorab signierte URLs (kompatibel mit
[S3-vorab signierten
URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
und Azure SAS) direkt in Ihre Generierungsanfrage einfügen. Die Gemini API ruft die Inhalte während der Verarbeitung sicher ab. Dies ist ideal für Dateien mit bis zu 100 MB, die Sie nicht noch einmal hochladen möchten.

Sie können öffentliche oder signierte URLs als Eingabe verwenden, indem Sie die URLs im Feld `file_uri` verwenden.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### Bedienungshilfen

Prüfen Sie, ob die von Ihnen angegebenen URLs nicht zu Seiten führen, für die eine Anmeldung erforderlich ist oder die sich hinter einer Paywall befinden. Erstellen Sie für private Datenbanken eine signierte URL mit den richtigen Zugriffsberechtigungen und dem richtigen Ablaufdatum.

### Sicherheitsprüfungen

Das System führt eine Überprüfung der Inhaltsmoderation für die URL durch, um zu bestätigen, dass sie den Sicherheits- und Richtlinienstandards entspricht (z.B. Inhalte, für die die Einwilligung nicht widerrufen wurde, und Inhalte hinter einer Paywall). Wenn die von Ihnen angegebene URL diese Überprüfung nicht besteht, erhalten Sie für `url_retrieval_status` den Wert `URL_RETRIEVAL_STATUS_UNSAFE`.

### Unterstützte Inhaltstypen

Diese Liste der unterstützten Dateitypen und -beschränkungen dient als erste Orientierung und ist nicht vollständig. Die tatsächliche Menge der unterstützten Typen kann sich ändern und je nach verwendetem Modell und Tokenizer-Version variieren. Nicht unterstützte Typen führen zu einem Fehler.
Außerdem wird der Abruf von Inhalten für diese Dateitypen derzeit nur für öffentlich zugängliche URLs unterstützt.

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

#### Videodateitypen

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Best Practices

- **Die richtige Methode auswählen**:Verwenden Sie Inlinedaten für kleine, temporäre Dateien.
  Verwenden Sie die File API für größere oder häufig verwendete Dateien. Verwenden Sie externe URLs für Daten, die bereits online gehostet werden.
- **MIME-Typen angeben**:Geben Sie immer den richtigen MIME-Typ für die Dateidaten an, um eine ordnungsgemäße Verarbeitung zu gewährleisten.
- **Fehler behandeln**:Implementieren Sie die Fehlerbehandlung in Ihrem Code, um potenzielle Probleme wie Netzwerkausfälle, Probleme beim Dateizugriff oder API-Fehler zu beheben.
- **GCS-Berechtigungen verwalten**:Wenn Sie die GCS-Registrierung verwenden, gewähren Sie dem Gemini API-Dienst-Agent nur die erforderliche Rolle `Storage Object Viewer` für die jeweiligen Buckets.
- **Sicherheit signierter URLs**:Achten Sie darauf, dass signierte URLs eine angemessene Ablaufzeit und eingeschränkte Berechtigungen haben.

## Beschränkungen

- Die Dateigrößenbeschränkungen variieren je nach Methode (siehe [Vergleichstabelle](#method-comparison))
  und Dateityp.
- Inlinedaten erhöhen die Größe der Anfrage-Nutzlast.
- Dateiuploads über die File API sind temporär und laufen nach 48 Stunden ab.
- Der Abruf externer URLs ist auf 100 MB pro Nutzlast beschränkt und unterstützt bestimmte Inhaltstypen.
- Für die Google Cloud Storage-Registrierung sind eine ordnungsgemäße IAM-Einrichtung und die Verwaltung von OAuth-Tokens erforderlich.

## Nächste Schritte

- Versuchen Sie, mit
  [Google AI Studio](http://aistudio.google.com/?hl=de) eigene multimodale Prompts zu schreiben.
- Informationen zum Einfügen von Dateien in Ihre Prompts finden Sie in den Anleitungen zur
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=de),
  [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=de) und
  [Dokumentverarbeitung](https://ai.google.dev/gemini-api/docs/document-processing?hl=de).
- Weitere Informationen zum Prompt-Design, z. B. zum Optimieren von Sampling-Parametern, finden Sie in der
  [Anleitung zu Prompt-Strategien](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
