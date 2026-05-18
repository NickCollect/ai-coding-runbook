---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=it
fetched_at: 2026-05-18T05:19:01.360752+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Metodi di input dei file

Questa guida spiega i diversi modi in cui puoi includere file multimediali come immagini, audio, video e documenti quando effettui richieste all'API Gemini.
I nuovi metodi sono supportati in tutti gli endpoint dell'API Gemini, tra cui le API Batch, Interactions e Live.
La scelta del metodo giusto dipende dalle dimensioni del file, dalla posizione in cui sono archiviati i dati e dalla frequenza con cui prevedi di utilizzare il file.

Il modo più semplice per includere un file come input è leggerlo localmente e includerlo in un prompt. L'esempio seguente mostra come leggere un file PDF locale. Per questo metodo, i PDF sono limitati a 50 MB. Per un elenco completo dei tipi e dei limiti di input dei file, consulta la
[tabella di confronto dei metodi di input](#method-comparison).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
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

## Confronto dei metodi di input

La tabella seguente confronta ogni metodo di input con i limiti dei file e i casi d'uso ottimali. Tieni presente che il limite delle dimensioni dei file può variare a seconda del tipo di file e del modello o del tokenizer utilizzato per elaborare il file.

| Metodo | Ideale per | Dimensione massima file | Persistenza |
| --- | --- | --- | --- |
| **Dati in linea** | Test rapidi, file di piccole dimensioni, applicazioni in tempo reale. | 100 MB per richiesta o payload   (**50 MB per i PDF**) | Nessuna (inviata con ogni richiesta) |
| **Caricamento tramite l'API File** | File di grandi dimensioni, file utilizzati più volte. | 2 GB per file,   fino a 20 GB per progetto | 48 ore |
| **Registrazione dell'URI GCS tramite l'API File** | File di grandi dimensioni già presenti in Google Cloud Storage, file utilizzati più volte. | 2 GB per file, nessun limite di spazio di archiviazione complessivo | Nessuna (recuperata per richiesta). La registrazione una tantum può consentire l'accesso per un massimo di 30 giorni. |
| **URL esterni** | Dati pubblici o dati in bucket cloud (AWS, Azure, GCS) senza ricaricarli. | 100 MB per richiesta/payload | Nessuna (recuperata per richiesta) |

## Dati in linea

Per i file più piccoli (meno di 100 MB o 50 MB per i PDF), puoi passare i dati direttamente nel payload della richiesta. Questo è il metodo più semplice per test rapidi o applicazioni che gestiscono dati transitori in tempo reale. Puoi fornire i dati come stringhe con codifica base64 o leggendo direttamente i file locali.

Per un esempio di lettura da un file locale, consulta l'esempio all'inizio di questa pagina.

### Recupero da un URL

Puoi anche recuperare un file da un URL, convertirlo in byte e includerlo nell'input.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import httpx
import base64

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
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
"model": "gemini-3-flash-preview",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## API File di Gemini

L'API File è progettata per file di dimensioni maggiori (fino a 2 GB) o file che intendi utilizzare in più richieste.

### Caricamento standard dei file

Carica un file locale nell'API Gemini. I file caricati in questo modo vengono archiviati temporaneamente (48 ore) ed elaborati per un recupero efficiente da parte del modello.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

# Upload the file
doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

# Use the uploaded file in an interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
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
    model: "gemini-3-flash-preview",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Registrazione dei file di Google Cloud Storage

Se i dati sono già in Google Cloud Storage, non devi scaricarli e ricaricarli. Puoi registrarli direttamente con l'API File.

1. Concedi l'accesso **Service Agent** a ogni bucket

   1. Abilita l'API Gemini nel tuo progetto Google Cloud.
   2. Crea il service agent:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Concedi le autorizzazioni del service agent dell'API Gemini** per leggere i bucket di archiviazione.

      L'utente deve assegnare il `Storage Object Viewer`
      [ruolo IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=it#storage.objectViewer)
      a questo service agent nei bucket di archiviazione specifici che intende utilizzare.

   Per impostazione predefinita, questo accesso non scade, ma può essere modificato in qualsiasi momento. Puoi
   anche utilizzare i
   [comandi dell'SDK IAM di Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=it)
   per concedere le autorizzazioni.
2. Autentica il tuo servizio

   **Prerequisiti**

   - Abilita API
   - Crea un service account o un agente con le autorizzazioni appropriate.

   Innanzitutto, devi autenticarti come il servizio che dispone delle autorizzazioni di visualizzazione degli oggetti di archiviazione. La modalità di autenticazione dipende dall'ambiente in cui verrà eseguito il codice di gestione dei file.

   **Al di fuori di Google Cloud**

   Se il codice viene eseguito al di fuori di Google Cloud, ad esempio dal computer, scarica le credenziali dell'account dalla console Google Cloud seguendo questi passaggi:

   1. Vai alla [console Account di servizio](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=it)
   2. Seleziona il service account pertinente
   3. Seleziona la scheda **Chiavi** e scegli **Aggiungi chiave, Crea nuova chiave**
   4. Scegli il tipo di chiave **JSON** e prendi nota della posizione in cui è stato scaricato il file sul tuo computer.

   Per maggiori dettagli, consulta la documentazione ufficiale di Google Cloud sulla
   [gestione delle chiavi dei service account](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=it).

   Quindi, utilizza i seguenti comandi per l'autenticazione. Questi comandi presuppongono che il file del service account si trovi nella directory corrente e che sia denominato `service-account.json`.

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

   **Su Google Cloud**

   Se esegui l'applicazione direttamente in Google Cloud, ad esempio utilizzando le funzioni di [Cloud
   Run](https://cloud.google.com/functions?hl=it) o un'
   [istanza di Compute Engine](https://cloud.google.com/products/compute?hl=it), avrai
   credenziali implicite, ma dovrai eseguire nuovamente l'autenticazione per concedere gli
   ambiti appropriati.

   ### Python

   Questo codice prevede che il servizio venga eseguito in un ambiente in cui
   [le credenziali predefinite dell'applicazione](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=it)
   possono essere ottenute automaticamente, ad esempio Cloud Run o Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Questo codice prevede che il servizio venga eseguito in un ambiente in cui
   [le credenziali predefinite dell'applicazione](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=it)
   possono essere ottenute automaticamente, ad esempio Cloud Run o Compute Engine.

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

   Questo è un comando interattivo. Per i servizi come Compute Engine, puoi collegare gli ambiti al servizio in esecuzione a livello di configurazione. [Per un esempio, consulta la documentazione relativa ai servizi gestiti dall'utente.](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=it#using)

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Registrazione dei file (API File)

   Utilizza l'API File per registrare i file e generare un percorso dell'API File che può essere utilizzato direttamente nell'API Gemini.

   ### Python

   ```
   # This will only work for SDK newer than 2.0.0
   from google import genai

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   # call interactions.create for each file
   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3-flash-preview",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     # Print the model's text response
     for step in interaction.steps:
         if step.type == "model_output":
             for content_block in step.content:
                 if content_block.type == "text":
                     print(content_block.text)
   ```

   ### JavaScript

   ```
   // This will only work for SDK newer than 2.0.0
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
               model: "gemini-3-flash-preview",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           const modelStep = interaction.steps.find(s => s.type === 'model_output');
           if (modelStep) {
               for (const contentBlock of modelStep.content) {
                   if (contentBlock.type === 'text') console.log(contentBlock.text);
               }
           }
       }
   }

   main();
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

## URL HTTP esterni / firmati

Puoi passare gli URL HTTPS accessibili pubblicamente o gli URL pre-firmati direttamente nella richiesta. L'API Gemini recupererà i contenuti in modo sicuro durante l'elaborazione.
Questa soluzione è ideale per i file fino a 100 MB che non vuoi ricaricare.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -H "Api-Revision: 2026-05-20" \
      -d '{
          "model": "gemini-3-flash-preview",
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

### Accessibilità

Verifica che gli URL forniti non rimandino a pagine che richiedono l'accesso o che si trovino dietro un paywall. Per i database privati, assicurati di creare un URL firmato con le autorizzazioni di accesso e la scadenza corrette.

### Controlli di sicurezza

Il sistema esegue un controllo di moderazione dei contenuti sull'URL per verificare che soddisfi gli standard di sicurezza e delle norme. Se l'URL non supera questo controllo, riceverai un `url_retrieval_status` di `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipi di contenuti supportati

Questo elenco di tipi di file e limitazioni supportati è inteso come guida iniziale e non è esaustivo. L'insieme effettivo di tipi supportati è soggetto a modifiche e può variare in base alla versione specifica del modello e del tokenizer in uso. I tipi non supportati genereranno un errore.
Inoltre, il recupero dei contenuti per questi tipi di file supporta solo gli URL accessibili pubblicamente.

#### Tipi di file di testo

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipi di file di applicazione

- `application/json`
- `application/pdf`

#### Tipi di file immagine

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## Best practice

- **Scegli il metodo giusto**:utilizza i dati in linea per i file piccoli e transitori.
  Utilizza l'API File per i file di dimensioni maggiori o utilizzati di frequente. Utilizza gli URL esterni per i dati già ospitati online.
- **Specifica i tipi MIME**:fornisci sempre il tipo MIME corretto per i dati dei file per garantire un'elaborazione corretta.
- **Gestisci gli errori**:implementa la gestione degli errori nel codice per gestire potenziali problemi come errori di rete, problemi di accesso ai file o errori dell'API.

## Limitazioni

- I limiti delle dimensioni dei file variano in base al metodo (vedi [tabella di confronto](#method-comparison))
  e al tipo di file.
- I dati in linea aumentano le dimensioni del payload della richiesta.
- I caricamenti tramite l'API File sono temporanei e scadono dopo 48 ore.
- Il recupero degli URL esterni è limitato a 100 MB per payload e supporta tipi di contenuti specifici.

## Passaggi successivi

- Prova a scrivere i tuoi prompt multimodali utilizzando
  [Google AI Studio](http://aistudio.google.com/?hl=it).
- Per informazioni sull'inclusione dei file nei prompt, consulta le
  [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=it) all'elaborazione di
  [immagini](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=it),
  [audio](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=it) e
  documenti.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-12 UTC."],[],[]]
