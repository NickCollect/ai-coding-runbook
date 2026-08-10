---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=it
fetched_at: 2026-08-10T03:12:39.795455+00:00
title: "Genera e modifica video con Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Genera e modifica video con Gemini Omni Flash

Gemini Omni Flash (`gemini-omni-flash-preview`) è un modello multimodale ad alte prestazioni progettato per la generazione, la modifica e il controllo cinematografico di video ad alta velocità.
Gemini Omni si basa sulle seguenti funzionalità principali che lo distinguono dai
modelli video precedenti:

- **Multimodalità nativa:** elabora testo, immagini, audio e video
  contemporaneamente, offrendoti un output più coeso, coerente e controllabile.
- **Modifica conversazionale**:attivata dall'[API
  Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it), ti consente di perfezionare
  e modificare in modo iterativo i tuoi video tramite conversazioni in linguaggio naturale. Descrivi cosa
  vuoi cambiare e il modello applica la modifica preservando le
  parti del video che vuoi conservare.
- **Conoscenza del mondo:** Gemini Omni combina la comprensione della fisica con la conoscenza di storia, scienza e contesto culturale di Gemini, colmando il divario tra fotorealismo e narrazione significativa.

## Generazione di video da testo

Genera un video da un prompt di testo. Il modello genera un video con audio
in base alla descrizione testuale. Scrivi prompt con dettagli come la descrizione della scena,
il movimento della videocamera, l'illuminazione e l'atmosfera per ottenere risultati ottimali.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({  
  model: 'gemini-omni-flash-preview',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### Schema di risposta REST

Il campo di convenienza `interaction.output_video` è **solo SDK**.
Ottieni l'output video dall'array `steps` quando utilizzi direttamente l'API REST.

**Struttura JSON REST non elaborato:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

### Controllare le proporzioni

Imposta `aspect_ratio` su `"9:16"` per creare video verticali. Orizzontale (16:9)
è l'impostazione predefinita.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

## Generazione di video da immagini

Puoi fornire un'immagine di riferimento con il prompt testuale. A seconda del
prompt, il modello deciderà
come utilizzare l'immagine. Questa funzionalità è utile per dare vita a scatti di prodotti, illustrazioni o fotografie.

L'esempio seguente mostra come utilizzare l'immagine di riferimento di un disegno di un
pesce che salta fuori dall'acqua:

![Disegno di un pesce che salta fuori dall&#39;acqua](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=it)

Con il seguente prompt:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Per generare un video realistico del disegno.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Riferimento oggetto

Puoi generare un video che incorpori soggetti specifici forniti come immagini di riferimento.
Ad esempio, il seguente codice mostra come fornire due immagini di un gatto e di un gomitolo
per generare un video del gatto che gioca con il gomitolo.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parametro Tasks

Utilizza il parametro `task` in `video-config` per indicare chiaramente il comportamento previsto. Ad esempio, se vuoi che il modello generi un video da un'immagine, puoi impostare il parametro su `image_to_video`. Se non viene impostato, il modello dedurrà ciò che vuoi dal prompt.

I valori consentiti sono i seguenti:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

L'esempio seguente mostra come impostare questa opzione per l'esempio di immagine
in video mostrato in precedenza.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-flash-preview",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## Editing video stateful

Genera un video e modificalo in modo iterativo utilizzando prompt di follow-up. Ogni turno
si basa sul risultato precedente. Il modello ricorda il contesto del video e applica
le modifiche preservando gli elementi che non hai menzionato. Utilizza
`previous_interaction_id` per monitorare la cronologia della conversazione e lo stato del video generato
senza ricaricare il video precedente.

Il seguente esempio mostra come generare un primo video e poi modificarlo:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-flash-preview", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-flash-preview",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Esempio di video iniziale:

Esempio di video modificato:

Ogni turno della conversazione produce un nuovo video. Il modello comprende
il contesto dei turni precedenti, consentendoti di apportare modifiche incrementali come la regolazione
dell'illuminazione e lo scambio di sfondi, senza dover descrivere nuovamente l'intera scena.

### Modificare i propri video

Carica i tuoi video utilizzando l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per modificarli
con Gemini Omni Flash.

Il seguente esempio mostra come modificare il video originale:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-flash-preview",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

Esempio di video modificato:

## Recupero di video con un URI

Utilizza il parametro `delivery="uri"` in
`response_format` per recuperare i video generati di dimensioni superiori a 4 MB.
Viene restituito un URI ospitato da Google che puoi interrogare finché il
video non è `ACTIVE` prima del download.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Struttura JSON REST non elaborata (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

## Best practice

- **Utilizza la distribuzione URI per i video di grandi dimensioni:** per i video di dimensioni superiori a 4 MB (>720p
  se disponibili), utilizza `delivery="uri"` in `response_format` per evitare limiti
  alle dimensioni del payload.
- **Rendimento ottimizzato:** imposta `background=false`, `store=false` e
  `stream=false` per una generazione sincrona e più rapida di numeri binari. Tieni presente che l'impostazione
  `store=false` significa che il video generato non sarà modificabile nei turni
  successivi utilizzando `previous_interaction_id`.
- **Precisione dei prompt**:consulta la sezione [Indicazioni per i prompt](#prompt-guide) per
  maggiori dettagli.

## Limitazioni

- Il caricamento e la modifica di immagini contenenti minori non sono supportati nello Spazio economico europeo, in Svizzera e nel Regno Unito.
- Il caricamento e la modifica di immagini contenenti determinate persone riconoscibili non sono supportati.
- La modifica dei video caricati non è attualmente disponibile per gli utenti nello Spazio economico europeo (SEE), in Svizzera e nel Regno Unito (la modifica dei video generati dal modello è supportata).
- Il caricamento di riferimenti audio non è supportato nella versione attuale dell'API.
- I riferimenti video di durata massima di 3 secondi sono accettati dallo schema dell'API, ma al momento non vengono elaborati correttamente dal modello.
- Non è supportato il riferimento o il ragionamento su più video. Il tentativo di utilizzare prompt multi-video potrebbe comportare un peggioramento delle prestazioni del modello o output imprevisti.
- L'estensione video e l'interpolazione video (generazione di video tra il primo e l'ultimo fotogramma) non sono supportate.
- La modifica vocale non è supportata.
- Il throughput di cui è stato eseguito il provisioning non è supportato.
- Le istruzioni di sistema, la temperatura, `top_p`, le sequenze di interruzione e i prompt negativi non sono supportati (puoi inserire i prompt negativi nel prompt normale, ad esempio "Non fare X").
- L'utilizzo di video di YouTube come origine media non è supportato.

## Dettagli tecnici

- Tutti i video generati includono il watermarking SynthID, che è invisibile agli spettatori, ma può essere rilevato a livello di programmazione per la verifica della provenienza.
- I tempi di generazione dei video variano in base a durata, risoluzione e carico attuale dell'API. I video più lunghi e con una risoluzione più elevata richiedono più tempo per essere generati.
- I filtri di sicurezza dei contenuti vengono applicati sia ai prompt di input sia al video generato (e dipendono dalla tua regione). I prompt che violano le norme di utilizzo verranno bloccati.
- L'inglese (EN) è completamente supportato, ma altre lingue non sono state valutate, quindi potrebbero funzionare, ma i risultati possono variare.

## Guida ai prompt di Gemini Omni Flash

Questa sezione contiene suggerimenti ed esempi su come utilizzare Gemini Omni Flash in modo efficace.

### Singola scena

Per impostazione predefinita, Omni Flash tenterà di creare un video con diverse inquadrature.
Tenterà di creare una narrazione interessante basata sul prompt.

Se vuoi che il video di output contenga una sola scena, devi specificarlo nel prompt:

- In un'unica scena ininterrotta
- In una singola ripresa continua
- Nessun taglio di scena

Ad esempio:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Rimozione degli elementi indesiderati

Se il video generato contiene elementi che non vuoi, includi semplici prompt negativi per evitarli:

- Nessun dialogo
- Nessuna decorazione
- Nessun effetto sonoro aggiuntivo

### Prompt per la modifica

I prompt semplici funzionano meglio per l'editing video. Prompt eccessivamente descrittivi possono portare a modifiche indesiderate.

Di seguito sono riportati altri esempi di prompt di modifica semplici:

- Trasforma questo video in un anime
- Metti un cappello alla moda a questa persona
- Modifica l'illuminazione per renderla più drammatica
- Modifica il testo sul cartello in modo che dica "Omni Flash"

Quando modifichi un aspetto specifico del video, includi `"Keep everything else the same"` per mantenere la coerenza visiva.

Di seguito sono riportati alcuni esempi per mostrare come applicare questa tecnica:

- **Pratiche non consigliate:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Semplifica:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Pratiche non consigliate:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Semplifica:** `Make the phone invisible. Keep everything else the
    same.`

### Richiesta dell'audio

Per impostazione predefinita, il modello tenterà di generare una traccia audio appropriata per un video. Potrebbe non essere sempre quello che vuoi. Puoi utilizzare il prompt per
descrivere il tipo di audio che vuoi. Ciò è particolarmente importante se vuoi
inserire musica nel tuo video:

- Includi musica di sottofondo rilassante
- Il video ha un ritmo techno ad alta energia
- L'audio è una trasmissione radiofonica di bassa qualità in sottofondo, che riproduce una canzone

### Eventi di temporizzazione

Puoi richiedere che determinate azioni vengano eseguite in momenti specifici del video. Non è necessaria una sintassi precisa e puoi utilizzare il linguaggio naturale. Questa funzionalità è particolarmente
utile per creare tagli di scena, ritmi o sequenze rapide.
Vedi di seguito alcuni esempi:

- Dopo 3 secondi, entra in scena una donna.
- Al secondo 5 inizia il ritornello nell'audio in background.
- Ogni 2 secondi viene visualizzato un nuovo fotogramma.
- In una sequenza di scatti rapidi, ogni mezzo secondo (12 frame a 24 fps) cambia la scena in una nuova posizione.

Puoi anche utilizzare una sintassi del timecode:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta-prompting

Puoi chiedere a Gemini Omni Flash di prestare attenzione a qualità generali o
principi di generazione video:

- Considera i microdettagli, l'espressione e la tempistica per creare una scena molto ricca e dettagliata, ma del tutto naturale.
- Fornisci descrizioni estremamente dettagliate di personaggi e ambienti.
  Applica i principi di progettazione dei costumi ai personaggi. Descrivi in modo molto specifico
  le persone, gli articoli e gli oggetti nella scena.
- Includi molti dettagli appropriati negli elementi di sfondo per rendere la scena realistica e naturale.
- Crea un video in rapida successione che mostri un diverso `[thing]` raro ogni secondo, con musica
  allegra e testo per etichettare l'oggetto.

### Testo nei video

Puoi chiedere di includere del testo nel video e Gemini Omni lo renderà in modo corretto e leggibile. Se nel video è presente del testo naturale, anche negli elementi di sfondo, può essere utile definire cosa deve dire.

- Una parola alla volta sullo schermo: "did, you, know, that, Omni, can, do,
  awesome, text?" (lo sapevi che Omni può creare testi fantastici?) Ogni parola viene visualizzata per 1 secondo con uno stile animato diverso. Nessun
  dialogo.
- C'è un segnale stradale con la scritta: "This is an AI generation by Omni" (Questa è una generazione di AI di Omni),
  una vetrina con la scritta: "All you need AI" (Tutto ciò che ti serve è l'AI), un'auto con la targa
  "OMN111".

### Utilizzare i tag nei prompt per impostare i ruoli delle immagini

Puoi utilizzare i tag per associare i contenuti multimediali caricati a ruoli di generazione specifici. In questo modo puoi specificare se ogni immagine è un frame iniziale o un riferimento.

#### 1. Tag semplici (consigliati)

Per i casi semplici in cui i ruoli delle immagini sono chiari dal prompt, puoi associare
le immagini ai ruoli direttamente:

- **`<FIRST_FRAME>`**: utilizza l'immagine come fotogramma iniziale del video, ad esempio: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: utilizza l'immagine come riferimento, ad esempio: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina il riferimento allo stile
  della prima immagine e il riferimento al soggetto della seconda immagine).
  I riferimenti alle immagini iniziano da 0.

Di seguito è riportato un esempio con 6 immagini di riferimento:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Dichiarazioni esplicite

Per i casi più complessi con più immagini e più ruoli, puoi utilizzare
tag di prefisso espliciti abbinati a suffissi di istruzioni in linguaggio naturale.

- **Dichiarazione di fonti e immagini di riferimento**:
  - `[# Sources <FIRST_FRAME>@Image1]` utilizzerà la prima immagine come fotogramma iniziale.
  - `[# References <IMAGE_REF_0>@Image1]` utilizzerà la prima immagine come riferimento.
  - `[# References <IMAGE_REF_1>@Image2]` utilizzerà la seconda immagine come riferimento.
  - `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` utilizzerà entrambe le immagini come riferimenti.
  - `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` utilizzerà la prima immagine come fotogramma iniziale e la seconda come riferimento.
- **Istruzioni guida**: aggiungi istruzioni guida alla fine del prompt:
  - Per il frame iniziale: `"Use this image as the starting frame."`
  - Per le immagini di riferimento: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

Esempio di prompt espanso:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## Passaggi successivi

- Inizia a utilizzare Gemini Omni Flash sperimentando in [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=it).
- Scopri come scrivere prompt ancora migliori con la nostra [Introduzione alla progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
