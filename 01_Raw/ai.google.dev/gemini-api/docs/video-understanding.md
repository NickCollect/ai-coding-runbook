---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=it
fetched_at: 2026-10-05T06:49:01.011383+00:00
title: "Comprensione dei video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Comprensione dei video

> Per scoprire di più sulla generazione di video, consulta la guida [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=it).

I modelli Gemini possono elaborare video, consentendo molti casi d'uso per gli sviluppatori all'avanguardia
che in passato avrebbero richiesto modelli specifici per il dominio.
Alcune delle funzionalità di visione di Gemini includono la possibilità di descrivere, segmentare ed estrarre informazioni dai video, rispondere a domande sui contenuti video e fare riferimento a timestamp specifici all'interno di un video.

Puoi fornire video come input a Gemini nei seguenti modi:

| Metodo inserimento | Dimensione massima | Caso d'uso consigliato |
| --- | --- | --- |
| [API File](#upload-video) | 20 GB (a pagamento) / 2 GB (senza costi) | File di grandi dimensioni (oltre 100 MB), video lunghi (oltre 10 minuti), file riutilizzabili. |
| [Registrazione di Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it#registration) | 2 GB (per file, senza limiti di spazio di archiviazione) | File di grandi dimensioni (oltre 100 MB), video lunghi (oltre 10 minuti), file persistenti e riutilizzabili. |
| [Dati in linea](#inline-video) | < 100MB | File piccoli (< 100 MB), di breve durata (< 1 minuto), input una tantum. |
| [URL di YouTube](#youtube) | N/D | Video di YouTube pubblici. |

> **Nota**:l'[API File](#upload-video) è consigliata per la maggior parte dei casi d'uso, in particolare per i file di dimensioni superiori a 100 MB o quando vuoi riutilizzare il file in più richieste.

Per scoprire altri metodi di input dei file, ad esempio l'utilizzo di URL esterni o file
archiviati in Google Cloud, consulta la guida
[Metodi di input dei file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it).

### Caricare un file video

Il seguente codice scarica un video di esempio, lo carica utilizzando l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it),
attende l'elaborazione e poi utilizza il riferimento al file caricato per
riassumere il video.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

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
    "time"

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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Per ottimizzare l'efficienza e il rendimento dei token, valuta la possibilità di utilizzare
l'[elaborazione di video con agenti](#agentic-video-understanding).

Utilizza sempre l'API Files quando le dimensioni totali della richiesta (inclusi il file, il prompt di testo, le istruzioni di sistema e così via) superano i 20 MB, la durata del video è significativa o se intendi utilizzare lo stesso video in più prompt.
L'API File accetta direttamente i formati dei file video.

Per saperne di più su come lavorare con i file multimediali, consulta l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Trasmettere i dati video in linea

Anziché caricare un file video utilizzando l'API File, puoi trasmettere video più piccoli direttamente nella richiesta. Questa opzione è adatta ai video più brevi con dimensioni totali della richiesta inferiori a 20 MB.

Ecco un esempio di fornitura di dati video in linea:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

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
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Trasmettere gli URL di YouTube

Puoi trasmettere gli URL di YouTube direttamente all'API Gemini nell'ambito della tua richiesta nel seguente modo:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Limitazioni:**

- Per il livello senza costi, non puoi caricare più di 8 ore di video di YouTube al giorno.
- Per il livello a pagamento, non esiste alcun limite in base alla durata del video.
- Per i modelli precedenti a Gemini 2.5, puoi caricare un solo video per richiesta. Per Gemini 2.5 e modelli successivi, puoi caricare un massimo di 10 video per richiesta.
- Puoi caricare solo video pubblici (non privati o non in elenco).

## Comprensione dei video agentica

Per impostazione predefinita, gli input video utilizzano l'elaborazione statica (estrazione di frame a 1 FPS).
I modelli Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash e 3.5 Flash Lite supportano anche la
**comprensione dei video agentici**, in cui il modello esplora dinamicamente la sequenza temporale del video,
ispezionando selettivamente le trascrizioni e regolando in modo adattivo la frequenza dei fotogrammi e la risoluzione al volo in base al prompt.

| **Modalità** | **Descrizione** | **Modelli supportati** |
| --- | --- | --- |
| **Statica** (impostazione predefinita) | Estrae i fotogrammi a una velocità fissa (1 f/s) e li inserisce nel contesto in un'unica passata. Funziona bene per i clip brevi. | Tutti i modelli Gemini |
| **Agentic** | Il modello naviga dinamicamente nella sequenza temporale del video, caricando solo i contenuti necessari in base al prompt. Fino all'88% in più di efficienza dei token e una qualità superiore di circa il 7% per i contenuti nel formato lungo. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### Scegliere una modalità di elaborazione

Come linea guida generale, inizia con la modalità **agente**, soprattutto quando ottimizzi
per la qualità della risposta o l'efficienza dei token.

- **Agentic**:video nel formato lungo o query che hanno come target momenti specifici. Il modello naviga dinamicamente nella cronologia per individuare informazioni contestualmente pertinenti senza riempire la finestra contestuale.
- **Statica**:query sensibili alla latenza su clip brevi (meno di 5 minuti) o
  casi in cui è necessaria una precisione a livello di frame sull'intero clip.

> **Nota**:per video lunghi o prompt complessi in cui l'elaborazione agentica richiede
> più tempo, utilizza lo streaming (`stream=True`) o l'esecuzione in background
> (`background=True`). In questo modo la connessione rimane attiva, vengono visualizzati i passaggi di ragionamento
> intermedi ed evitati timeout di connessione o autenticazione.

### Imposta la modalità di elaborazione

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **Nota:** per verificare che sia stata utilizzata l'elaborazione con agenti, esamina `interaction.steps`. La presenza di `processing_call` e `processing_result` indica che il modello ha navigato dinamicamente nel video.

### Passaggi per la risposta

L'elaborazione agentica aggiunge due nuovi tipi di passaggi all'array `steps`:

- `processing_call`: il modello ha richiesto un segmento video o una trascrizione audio, identificati da `id`.
- `processing_result`: il risultato del carico, collegato da `call_id`.

Questi vengono visualizzati alternati ai passaggi `thought` (quando i riepiloghi sono attivati) e precedono il passaggio finale `model_output`. Possono essere utilizzati per mostrare una traccia di avanzamento nell'interfaccia utente, ma non richiedono una risposta.

L'esempio seguente mostra il payload della risposta con i passaggi di elaborazione intercalati:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Combinare le modalità di elaborazione tra i video

Puoi impostare diverse modalità di elaborazione per ogni video nella stessa richiesta:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### Conversazioni video multi-turno

Il contesto del video viene mantenuto durante i turni di una conversazione. Quando utilizzi l'elaborazione
con agenti:

- **Modalità stateful** (utilizzando `previous_interaction_id`): il server conserva il contesto del video. Non è necessaria alcuna gestione aggiuntiva.
- **Modalità stateless** (utilizzando `step_list`): in modalità stateless, la risposta
  include i passaggi `processing_call` e `processing_result` che codificano il
  contesto del video. Devi includere tutti i passaggi della risposta nella tua prossima
  richiesta `step_list` per preservare il contesto del video. Sebbene la loro omissione non restituisca
  attualmente un errore API, il contesto del video viene perso, riducendo
  in modo significativo la qualità della risposta alle domande successive. Tieni presente che i passaggi restituiti
  in richieste successive contribuiscono al conteggio dei token di input.

## Fare riferimento ai timestamp nei contenuti

Puoi porre domande su momenti specifici del video utilizzando
timestamp nel formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Estrarre informazioni dettagliate dal video

I modelli Gemini offrono potenti funzionalità per la comprensione dei contenuti video elaborando le informazioni provenienti dai flussi **audio e visivi**. In questo modo puoi
estrarre un ricco insieme di dettagli, tra cui generare descrizioni di ciò che
accade in un video e rispondere a domande sui suoi contenuti.

Per le descrizioni visive, il modello esegue il campionamento del video a una velocità di **1 frame
al secondo** (f/s). Questa frequenza di campionamento predefinita funziona bene per la maggior parte dei contenuti, ma
tieni presente che potrebbe non rilevare i dettagli nei video con movimenti rapidi o cambi di scena veloci.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personalizzare l'elaborazione video

Puoi personalizzare l'elaborazione video nell'API Gemini impostando intervalli di ritaglio
o fornendo un campionamento della frequenza dei fotogrammi personalizzato. Queste opzioni di personalizzazione
sono supportate solo durante l'elaborazione del video in modalità `"static"`.

### Impostare gli intervalli di ritaglio

Puoi tagliare il video specificando `start_offset` e `end_offset` nell'oggetto di configurazione `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Impostare una frequenza fotogrammi personalizzata

Puoi impostare il campionamento personalizzato della frequenza fotogrammi passando un argomento `fps` nell'oggetto di configurazione `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Formati video supportati

Gemini supporta i seguenti tipi MIME di formati video:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Dettagli tecnici sui video

- **Modelli e contesto supportati**: tutti i modelli Gemini possono elaborare i dati video.
  - I modelli con una finestra contestuale di 1 milione di token possono elaborare video della durata massima di 3 ore per impostazione predefinita (a bassa risoluzione multimediale) o della durata massima di 1 ora ad alta risoluzione multimediale.
- **Modalità di elaborazione**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite
  e i modelli successivi supportano due modalità di elaborazione video:
  - **Statico**: i frame vengono estratti a 1 FPS e inseriti nel contesto (valore predefinito
    per tutti i modelli). L'audio viene elaborato a 1 Kbps (singolo canale).
    I timestamp vengono aggiunti ogni secondo. Ideale per clip brevi o quando ogni fotogramma
    è importante (ad esempio per l'ispezione fotogramma per fotogramma). Tieni presente che le sequenze di azioni rapide
    potrebbero perdere dettagli a causa della frequenza di campionamento di 1 FPS.
  - **Agentic**: il modello naviga dinamicamente nel video, caricando
    la trascrizione e/o i frame e/o l'audio su richiesta. In questo modo, vengono utilizzati fino all'88%
    in meno di token per i contenuti nel formato lungo, anche se la navigazione potrebbe aumentare leggermente
    il tempo al primo token (TTFT) nei clip brevi (< 5 minuti) a causa
    del ragionamento interno e dei round trip degli strumenti prima dell'inizio della generazione. Ideale
    per i video nel formato lungo per ottimizzare i costi dei token e la qualità delle risposte.
    Supportato su Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash e 3.5 Flash Lite.
    Per maggiori dettagli, consulta [Comprensione dei video agentica](#agentic-video-understanding).
- **Calcolo dei token (modalità statica)**: ogni secondo di video viene tokenizzato come segue:
  - Singoli fotogrammi (campionati a 1 FPS):
    - Se `media_resolution` è impostato su basso, i frame vengono tokenizzati a 66
      token per frame.
    - In caso contrario, i frame vengono tokenizzati a 258 token per frame.
  - Audio: 32 token al secondo.
  - Sono inclusi anche i metadati.
  - Totale: circa 100 token al secondo di video con risoluzione multimediale predefinita (bassa) o circa 300 token al secondo di video con risoluzione multimediale elevata.
- **Calcolo dei token (modalità agente)**: l'utilizzo dei token varia in base alla complessità dei contenuti e alla strategia di navigazione del modello. I token di ragionamento della navigazione generati durante l'esplorazione dei video vengono conteggiati come **token di pensiero** (`total_thought_tokens`), mentre i frame, l'audio e la trascrizione caricati su richiesta vengono conteggiati come token di utilizzo degli strumenti (`total_tool_use_tokens`). L'elaborazione con agenti in genere utilizza fino all'88% in meno di token totali rispetto all'elaborazione statica per i contenuti nel formato lungo, perché il modello carica solo la trascrizione e/o i frame e/o l'audio necessari per rispondere al prompt (consulta la [guida ai token](https://ai.google.dev/gemini-api/docs/tokens?hl=it#video-token-usage)).
- **Risoluzione dei contenuti multimediali**: Gemini 3 introduce un controllo granulare dell'elaborazione multimodale
  della visione con il parametro `media_resolution`. Il parametro
  `media_resolution` determina il **numero massimo di token
  allocati per ogni immagine di input o frame video.** Risoluzioni più elevate migliorano la capacità del modello di leggere testi piccoli o identificare piccoli dettagli, ma aumentano l'utilizzo dei token e la latenza. I parametri `media_resolution` e `processing`
  sono indipendenti: puoi impostarli entrambi sullo stesso input video.

Per maggiori dettagli sui calcoli dei token, consulta la guida ai [token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

- **Formato del timestamp**: quando fai riferimento a momenti specifici di un video all'interno
  del prompt, utilizza il formato `MM:SS` (ad es. `01:15` per 1 minuto e 15
  secondi).
- **Posizionamento del prompt**: se combini testo e un singolo video, posiziona il prompt testuale
  *dopo* la parte video nell'array `input`.
- **Timeout per richieste lunghe**: per i video che richiedono tempi di elaborazione prolungati o ragionamenti multi-step complessi, utilizza lo streaming (`stream=True`) o l'esecuzione in background (`background=True`). Le richieste sincrone non in streaming che subiscono nuovi tentativi di backend in caso di forte domanda possono superare le finestre di validità della connessione o del token di autenticazione, il che può causare errori `401 Unauthorized` o di timeout imprevisti.
  Lo streaming mantiene attiva la connessione e mostra il ragionamento intermedio
  e l'avanzamento della chiamata allo strumento.

## Passaggi successivi

- [Risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it): controlla la
  risoluzione dei fotogrammi video per bilanciare qualità e utilizzo dei token.
- [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=it): scopri come vengono tokenizzati i contenuti video
  nelle modalità di elaborazione statica e con agenti.
- [Istruzioni di sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions):
  Le istruzioni di sistema ti consentono di orientare il comportamento del modello in base alle tue
  esigenze e ai tuoi casi d'uso specifici.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=it): scopri di più sul caricamento e sulla gestione dei file da utilizzare con Gemini.
- [Strategie di prompt dei file](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide): l'API Gemini
  supporta i prompt con dati di testo, immagini, audio e video, noti anche come
  prompt multimodali.
- [Indicazioni per la sicurezza](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it): a volte i modelli di AI generativa
  producono output inaspettati, ad esempio output imprecisi,
  di parte o offensivi. Il post-processing e la valutazione umana sono essenziali per
  limitare il rischio di danni derivanti da questi output.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
