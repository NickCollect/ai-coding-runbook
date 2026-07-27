---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it
fetched_at: 2026-07-27T04:46:18.401006+00:00
title: "Metodi di input dei file \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Metodi di input dei file

Questa guida spiega i diversi modi in cui puoi includere file multimediali come
immagini, audio, video e documenti quando invii richieste all'API Gemini.
I nuovi metodi sono supportati in tutti gli endpoint dell'API Gemini, tra cui
Batch, Interactions e Live API.
La scelta del metodo giusto dipende dalle dimensioni del file, dalla posizione in cui sono archiviati i dati e dalla frequenza con cui prevedi di utilizzare il file.

Il modo più semplice per includere un file come input è leggere un file locale e
includerlo in un prompt. L'esempio seguente mostra come leggere un file PDF locale. I PDF sono limitati a 50 MB per questo metodo. Consulta la
[tabella di confronto dei metodi di input](#method-comparison) per un elenco completo dei tipi di input e dei limiti dei file.

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

## Confronto dei metodi di immissione

La tabella seguente mette a confronto ciascun metodo di input con i limiti dei file e i casi d'uso
ottimali. Tieni presente che il limite di dimensione del file può variare a seconda del tipo di file e
del modello o del tokenizer utilizzato per elaborare il file.

| Metodo | Ideale per | Dimensione massima file | Persistenza |
| --- | --- | --- | --- |
| **Dati in linea** | Test rapidi, file di piccole dimensioni, applicazioni in tempo reale. | 100 MB per richiesta o payload   (**50 MB per i PDF**) | Nessuno (inviato con ogni richiesta) |
| **Caricamento dell'API File** | File di grandi dimensioni, file utilizzati più volte. | 2 GB per file,   fino a 20 GB per progetto | 48 ore |
| **Registrazione dell'URI GCS dell'API File** | File di grandi dimensioni già presenti in Google Cloud Storage, file utilizzati più volte. | 2 GB per file, nessun limite di spazio di archiviazione complessivo | Nessuno (recuperato per richiesta). La registrazione una tantum può fornire l'accesso per un massimo di 30 giorni. |
| **URL esterni** | Dati pubblici o dati in bucket cloud (AWS, Azure, GCS) senza ricaricamento. | 100 MB per richiesta/payload | Nessuno (recuperato per richiesta) |

## Dati in linea

Per i file più piccoli (inferiori a 100 MB o 50 MB per i PDF), puoi trasmettere i dati
direttamente nel payload della richiesta. Questo è il metodo più semplice per test rapidi o
applicazioni che gestiscono dati temporanei in tempo reale. Puoi fornire i dati come stringhe con codifica base64 o leggendo direttamente i file locali.

Per un esempio di lettura da un file locale, consulta l'esempio all'inizio di questa pagina.

### Recuperare da un URL

Puoi anche recuperare un file da un URL, convertirlo in byte e includerlo nell'input.

### Python

```
from google import genai
import httpx

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
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## API Gemini File

L'API File è progettata per file più grandi (fino a 2 GB) o file che intendi
utilizzare in più richieste.

### Caricamento standard dei file

Carica un file locale nell'API Gemini. I file caricati in questo modo vengono archiviati
temporaneamente (48 ore) ed elaborati per un recupero efficiente da parte del modello.

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
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Registra i file Google Cloud Storage

Se i dati si trovano già in Google Cloud Storage, non devi scaricarli e ricaricarli. Puoi registrarlo direttamente con l'API File.

1. Concedi l'accesso al **service agent** a ogni bucket

   1. Abilita l'API Gemini nel tuo progetto Google Cloud.
   2. Crea l'agente di servizio:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Concedi al service agent dell'API Gemini le autorizzazioni** per leggere i tuoi bucket di archiviazione.

      L'utente deve assegnare il [ruolo IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=it#storage.objectViewer) `Storage Object Viewer` a questo service agent nei bucket di archiviazione specifici che intende utilizzare.

   Questo accesso non scade per impostazione predefinita, ma può essere modificato in qualsiasi momento. Puoi anche utilizzare i comandi dell'[SDK Google Cloud Storage IAM](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=it) per concedere le autorizzazioni.
2. Autenticare il servizio

   **Prerequisiti**

   - Abilita API
   - Crea un service account o un agente con le autorizzazioni appropriate.

   Devi prima autenticarti come servizio con autorizzazioni di visualizzazione degli oggetti Storage. La modalità dipende dall'ambiente in cui verrà eseguito il codice di gestione dei file.

   **Al di fuori di Google Cloud**

   Se il tuo codice viene eseguito al di fuori di Google Cloud, ad esempio dal tuo computer,
   scarica le credenziali dell'account dalla console Google Cloud seguendo
   i seguenti passaggi:

   1. Vai alla [console Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=it).
   2. Seleziona il service account pertinente.
   3. Seleziona la scheda **Chiavi** e scegli **Aggiungi chiave, Crea nuova chiave**.
   4. Scegli il tipo di chiave **JSON** e annota la posizione in cui è stato scaricato il file sul tuo computer.

   Per maggiori dettagli, consulta la documentazione ufficiale di Google Cloud sulla
   [gestione delle chiavi del service account](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=it).

   Poi utilizza i seguenti comandi per l'autenticazione. Questi comandi presuppongono che il file dell'account di servizio si trovi nella directory corrente e sia denominato `service-account.json`.

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

   ### Interfaccia a riga di comando

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Su Google Cloud**

   Se esegui l'applicazione direttamente in Google Cloud, ad esempio utilizzando le [funzioni Cloud Run](https://cloud.google.com/functions?hl=it) o un'[istanza Compute Engine](https://cloud.google.com/products/compute?hl=it), avrai credenziali implicite, ma dovrai eseguire nuovamente l'autenticazione per concedere gli ambiti appropriati.

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

   ### Interfaccia a riga di comando

   Questo è un comando interattivo. Per servizi come Compute Engine, puoi collegare gli ambiti al servizio in esecuzione a livello di configurazione. Per un esempio, consulta la [documentazione sul service account gestito dall'utente](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=it#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Registrazione dei file (API Files)

   Utilizza l'API Files per registrare i file e produrre un percorso dell'API Files che può essere utilizzato direttamente nell'API Gemini.

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

   ### Interfaccia a riga di comando

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## HTTP esterno / URL firmati

Puoi trasmettere URL HTTPS accessibili pubblicamente o URL pre-firmati direttamente nella tua
richiesta. L'API Gemini recupererà i contenuti in modo sicuro durante l'elaborazione.
È ideale per i file fino a 100 MB che non vuoi caricare nuovamente.

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

### Accessibilità

Verifica che gli URL forniti non rimandino a pagine che richiedono l'accesso o
sono protette da un paywall. Per i database privati, assicurati di creare un URL firmato
con le autorizzazioni di accesso e la scadenza corrette.

### Controlli di sicurezza

Il sistema esegue un controllo di moderazione dei contenuti sull'URL per verificare che soddisfi
gli standard di sicurezza e delle norme. Se l'URL non supera questo controllo, riceverai un
`url_retrieval_status` di `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipi di contenuti supportati

Questo elenco di tipi di file supportati e limitazioni è inteso come guida iniziale e non è esaustivo. L'insieme effettivo
di tipi supportati è soggetto a modifiche e può variare in base al modello specifico e alla versione del tokenizer in uso. I tipi non supportati genereranno un errore.
Inoltre, il recupero dei contenuti per questi tipi di file
supporta solo gli URL accessibili pubblicamente.

#### Tipi di file di testo

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipi di file dell'applicazione

- `application/json`
- `application/pdf`

#### Tipi di file immagine

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Tipi di file video

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Best practice

- **Scegli il metodo giusto**:utilizza i dati incorporati per i file piccoli e temporanei.
  Utilizza l'API File per i file più grandi o utilizzati di frequente. Utilizza URL esterni
  per i dati già ospitati online.
- **Specifica i tipi MIME**:fornisci sempre il tipo MIME corretto per i dati del file per garantire un'elaborazione corretta.
- **Gestisci gli errori**:implementa la gestione degli errori nel codice per gestire potenziali problemi come errori di rete, problemi di accesso ai file o errori dell'API.

## Limitazioni

- I limiti delle dimensioni dei file variano in base al metodo (vedi la [tabella di confronto](#method-comparison))
  e al tipo di file.
- I dati incorporati aumentano le dimensioni del payload della richiesta.
- I caricamenti dell'API File sono temporanei e scadono dopo 48 ore.
- Il recupero di URL esterni è limitato a 100 MB per payload e supporta tipi di contenuti specifici.

## Passaggi successivi

- Prova a scrivere i tuoi prompt multimodali utilizzando
  [Google AI Studio](http://aistudio.google.com/?hl=it).
- Per informazioni sull'inclusione di file nei prompt, consulta le guide
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=it),
  [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=it) e
  [Elaborazione dei documenti](https://ai.google.dev/gemini-api/docs/document-processing?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-06 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-06 UTC."],[],[]]
