---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=fr
fetched_at: 2026-09-28T06:24:09.103195+00:00
title: "Compr\u00e9hension des vid\u00e9os \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Compréhension des vidéos

> Pour en savoir plus sur la génération de vidéos, consultez le guide [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=fr).

Les modèles Gemini peuvent traiter des vidéos, ce qui permet de nombreux cas d'utilisation pour les développeurs de pointe qui auraient historiquement nécessité des modèles spécifiques à un domaine.
Voici quelques-unes des fonctionnalités de vision de Gemini : décrire, segmenter et extraire des informations à partir de vidéos, répondre à des questions sur le contenu vidéo et faire référence à des codes temporels spécifiques dans une vidéo.

Vous pouvez fournir des vidéos à Gemini de différentes manières :

| Mode de saisie | Taille maximale | Cas d'utilisation recommandé |
| --- | --- | --- |
| [API File](#upload-video) | 20 Go (payant) / 2 Go (sans frais) | Fichiers volumineux (plus de 100 Mo), vidéos longues (plus de 10 minutes), fichiers réutilisables |
| [Enregistrement Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr#registration) | 2 Go (par fichier, sans limite de stockage) | Fichiers volumineux (plus de 100 Mo), vidéos longues (plus de 10 minutes), fichiers persistants et réutilisables. |
| [Données intégrées](#inline-video) | < 100 Mo | Petits fichiers (< 100 Mo), courte durée (< 1 min), entrées ponctuelles. |
| [URL YouTube](#youtube) | N/A | Vidéos YouTube publiques |

> **Remarque** : L'[API File](#upload-video) est recommandée pour la plupart des cas d'utilisation, en particulier pour les fichiers de plus de 100 Mo ou lorsque vous souhaitez réutiliser le fichier dans plusieurs requêtes.

Pour en savoir plus sur les autres méthodes d'entrée de fichiers, comme l'utilisation d'URL externes ou de fichiers stockés dans Google Cloud, consultez le guide [Méthodes d'entrée de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

### Importer un fichier vidéo

Le code suivant télécharge un exemple de vidéo, l'importe à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr), attend qu'elle soit traitée, puis utilise la référence du fichier importé pour résumer la vidéo.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
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
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Pour optimiser l'efficacité et les performances des jetons, envisagez d'utiliser le [traitement agentique des vidéos](#agentic-video-understanding).

Utilisez toujours l'API Files lorsque la taille totale de la requête (y compris le fichier, l'invite de texte, les instructions système, etc.) est supérieure à 20 Mo, que la durée de la vidéo est importante ou si vous avez l'intention d'utiliser la même vidéo dans plusieurs invites.
L'API File accepte directement les formats de fichiers vidéo.

Pour en savoir plus sur l'utilisation des fichiers multimédias, consultez l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

### Transmettre des données vidéo de manière intégrée

Au lieu d'importer un fichier vidéo à l'aide de l'API File, vous pouvez transmettre des vidéos plus petites directement dans la requête à `generateContent`. Cette option convient aux vidéos plus courtes, dont la taille totale de la requête est inférieure à 20 Mo.

Voici un exemple de données vidéo intégrées :

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### Transmettre des URL YouTube

Vous pouvez transmettre des URL YouTube directement à l'API Gemini dans votre requête, comme suit :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Limites :**

- Avec le forfait sans frais, vous ne pouvez pas importer plus de huit heures de vidéos YouTube par jour.
- Pour le niveau payant, il n'y a pas de limite de durée pour les vidéos.
- Pour les modèles antérieurs à Gemini 2.5, vous ne pouvez importer qu'une seule vidéo par requête. Pour les modèles Gemini 2.5 et ultérieurs, vous pouvez importer jusqu'à 10 vidéos par requête.
- Vous ne pouvez mettre en ligne que des vidéos publiques (et non des vidéos privées ou non répertoriées).

## Compréhension agentique des vidéos

Par défaut, les entrées vidéo utilisent un traitement statique (extraction d'images à 1 FPS).
Les modèles Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash et 3.5 Flash Lite sont également compatibles avec la **compréhension agentique des vidéos**, où le modèle explore dynamiquement la timeline vidéo, en inspectant sélectivement les transcriptions et en ajustant de manière adaptative la fréquence d'images et la résolution à la volée en fonction de la requête.

| **Mode** | **Description** | **Modèles compatibles** |
| --- | --- | --- |
| **Statique** (par défaut) | Extrait les frames à une fréquence fixe (1 FPS) et les place dans le contexte en une seule passe. Fonctionne bien pour les extraits courts. | Tous les modèles Gemini |
| **Agentic** | Le modèle navigue de manière dynamique dans la timeline de la vidéo et ne charge que le contenu dont il a besoin en fonction de la requête. Jusqu'à 88% plus efficace en termes de jetons et environ 7% de meilleure qualité pour les contenus longs. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite |

### Choisir un mode de traitement

En règle générale, commencez par le mode **agentique**, en particulier lorsque vous optimisez la qualité des réponses ou l'efficacité des jetons.

- **Agentic** : vidéos longues ou requêtes ciblant des moments spécifiques. Le modèle parcourt la chronologie de manière dynamique pour cibler les informations contextuellement pertinentes sans remplir la fenêtre de contexte.
- **Statique** : requêtes sensibles à la latence sur des extraits courts (moins de cinq minutes) ou cas où une précision au niveau des frames est requise pour l'intégralité de l'extrait.

> **Remarque** : Pour les vidéos longues ou les requêtes complexes où le traitement par l'agent prend plus de temps, utilisez le streaming (`client.models.generate_content_stream`). Cela permet de maintenir la connexion active, d'afficher les étapes de raisonnement intermédiaires et d'éviter les délais d'expiration de la connexion ou de l'authentification.

### Définir le mode de traitement

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Remarque** : Pour vérifier que le traitement agentique a été utilisé, inspectez `response.candidates[0].content.parts`. La présence de parties `tool_call` et `tool_response` avec le type d'outil `MEDIA_PROCESSING` indique que le modèle a navigué de manière dynamique dans la vidéo.

> **Remarque** : Contrairement à d'autres outils côté serveur (comme la recherche Google ou le contexte d'URL), la vidéo agentique ne nécessite pas de définir `include_server_side_tool_invocations=True` dans `ToolConfig` pour que les appels et les résultats d'outils soient renvoyés ou diffusés. Les parties `tool_call` et `tool_response` pour la navigation vidéo sont renvoyées automatiquement lorsque `media_processing="AGENTIC"` est défini sur une partie d'entrée.

### Structure de la réponse

Lorsque le traitement agentique est activé, la réponse inclut des parties supplémentaires qui exposent la trace de navigation interne :

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`) : émis chaque fois que le modèle demande un segment vidéo ou une transcription audio.
- `tool_response` **parts** (`tool_type: "MEDIA_PROCESSING"`) : résultat de chaque opération de chargement.

Vous n'avez pas besoin de gérer ni de répondre manuellement à ces parties : transmettez la réponse complète en tant qu'historique des conversations, et elles seront traitées automatiquement.

Si `include_thoughts=True` est défini dans `ThinkingConfig`, les étapes de raisonnement apparaissent sous forme de parties `thought: true` entrelacées avec les paires d'appels/réponses d'outil. Lorsque les pensées sont désactivées, le texte de la pensée est omis, mais les parties de l'outil sont toujours présentes.

L'exemple suivant montre la charge utile de la réponse avec des parties de réponse et d'appel d'outil entrelacées :

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Combiner les modes de traitement pour différentes vidéos

Vous pouvez définir différents modes de traitement pour chaque partie d'une même vidéo dans une même requête :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Utiliser la mise en cache du contexte pour les vidéos longues

Pour les vidéos de plus de 10 minutes ou lorsque vous prévoyez d'envoyer plusieurs requêtes pour le même fichier vidéo, utilisez la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) afin de réduire les coûts et d'améliorer la latence. La mise en cache du contexte vous permet de traiter la vidéo une seule fois et de réutiliser les jetons pour les requêtes suivantes. Elle est idéale pour les sessions de chat ou l'analyse répétée de contenus longs.

## Faites référence aux codes temporels dans le contenu.

Vous pouvez poser des questions sur des moments précis de la vidéo à l'aide d'un code temporel au format `MM:SS`.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Extraire des insights détaillés à partir de vidéos

Les modèles Gemini offrent de puissantes fonctionnalités pour comprendre le contenu vidéo en traitant les informations des flux **audio et visuel**. Vous pouvez ainsi extraire un ensemble détaillé d'informations, y compris générer des descriptions de ce qui se passe dans une vidéo et répondre à des questions sur son contenu.

Pour les descriptions visuelles, le modèle échantillonne la vidéo à un taux de **1 image par seconde** (FPS). Ce taux d'échantillonnage par défaut fonctionne bien pour la plupart des contenus, mais notez qu'il peut manquer des détails dans les vidéos avec des mouvements rapides ou des changements de scène rapides.
Pour ce type de contenu, envisagez de [définir une fréquence d'images personnalisée](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Personnaliser le traitement des vidéos

Vous pouvez personnaliser le traitement vidéo dans l'API Gemini en définissant des intervalles de découpage ou en fournissant un échantillonnage de fréquence d'images personnalisé. Ces options de personnalisation ne sont disponibles que lorsque la vidéo est traitée en mode `"static"`.

### Définir des intervalles de clipping

Vous pouvez couper une vidéo en spécifiant `videoMetadata` avec des décalages de début et de fin.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Définir une fréquence d'images personnalisée

Vous pouvez définir un échantillonnage personnalisé de la fréquence d'images en transmettant un argument `fps` à `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

Par défaut, une image par seconde (FPS) est échantillonnée à partir de la vidéo. Vous pouvez définir un faible nombre d'images par seconde (< 1) pour les vidéos longues. Cela est particulièrement utile pour les vidéos principalement statiques (par exemple, les conférences). Utilisez un nombre de FPS plus élevé pour les vidéos nécessitant une analyse temporelle précise, comme la compréhension d'actions rapides ou le suivi du mouvement à grande vitesse.

## Formats vidéo acceptés

Gemini est compatible avec les types MIME de format vidéo suivants :

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Détails techniques sur les vidéos

- **Modèles et contexte compatibles** : tous les modèles Gemini peuvent traiter des données vidéo.
  - Les modèles avec une fenêtre de contexte d'un million de jetons peuvent traiter des vidéos d'une durée maximale de trois heures par défaut (à basse résolution média) ou d'une heure (à haute résolution média).
- **Modes de traitement** : les modèles Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite et les modèles ultérieurs sont compatibles avec deux modes de traitement vidéo :
  - **Statique** : les images sont extraites à 1 FPS et placées dans le contexte (par défaut pour tous les modèles). L'audio est traité à 1 kbit/s (canal unique).
    Des codes temporels sont ajoutés chaque seconde. Idéal pour les extraits courts ou lorsque chaque image compte (par exemple, pour une inspection image par image). Notez que les séquences d'action rapides peuvent perdre des détails en raison du taux d'échantillonnage d'une image par seconde.
  - **Agentique** : le modèle navigue de manière dynamique dans la vidéo, en chargeant la transcription et/ou les images et/ou l'audio à la demande. Cette méthode utilise jusqu'à 88 % de jetons en moins pour les contenus longs. Toutefois, la navigation peut légèrement augmenter le temps avant le premier jeton (TTFT) sur les clips courts (< 5 minutes) en raison du raisonnement interne et des allers-retours des outils avant le début de la génération.
    Les réponses incluent des parties d'appel et de réponse d'outil `MEDIA_PROCESSING` pour préserver le contexte de raisonnement entre les tours. Idéal pour les vidéos longues afin d'optimiser les coûts en jetons et la qualité des réponses. Compatible avec Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash et 3.5 Flash Lite. Pour en savoir plus, consultez [Compréhension agentique des vidéos](#agentic-video-understanding).
- **Calcul des jetons (mode statique)** : chaque seconde de vidéo est tokenisée comme suit :
  - Images individuelles (échantillonnées à 1 FPS) :
    - Si `media_resolution` est défini sur "faible", les frames sont tokenisés à 66 jetons par frame.
    - Sinon, les frames sont tokenisés à 258 jetons par frame.
  - Audio : 32 jetons par seconde.
  - Les métadonnées sont également incluses.
  - Total : environ 100 jetons par seconde de vidéo à la résolution média par défaut (faible), ou environ 300 jetons par seconde de vidéo à la résolution média élevée.
- **Calcul des jetons (mode agentique)** : l'utilisation des jetons varie en fonction de la complexité du contenu et de la stratégie de navigation du modèle. Les jetons de raisonnement de navigation générés lors de l'exploration de vidéos sont comptabilisés comme **jetons de réflexion** (`thoughts_token_count`), tandis que les frames, l'audio et la transcription chargés à la demande sont comptabilisés comme jetons d'invite d'outil (`tool_use_prompt_token_count`). Le traitement agentique utilise généralement jusqu'à 88% de jetons en moins que le traitement statique pour les contenus longs, car le modèle ne charge que la transcription et/ou les frames et/ou l'audio dont il a besoin pour répondre à la requête (voir le [guide sur les jetons](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=fr#video-token-usage)).
- **Résolution du contenu multimédia** : Gemini 3 permet de contrôler précisément le traitement multimodal de la vision grâce au paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons** alloués par image ou frame vidéo en entrée. Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation de jetons et la latence. Les paramètres `media_resolution` et `media_processing` sont indépendants : vous pouvez les définir tous les deux sur la même partie de la vidéo.

Pour en savoir plus sur le calcul des jetons, consultez le guide [Jetons](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=fr).

- **Format d'horodatage** : lorsque vous faites référence à des moments spécifiques d'une vidéo dans votre requête, utilisez le format `MM:SS` (par exemple, `01:15` pour 1 minute et 15 secondes).
- **Emplacement du prompt** : si vous combinez du texte et une seule vidéo, placez le prompt textuel *après* la partie vidéo dans le tableau `contents`.
- **Délai d'expiration pour les requêtes longues** : pour les vidéos qui nécessitent un temps de traitement prolongé ou un raisonnement en plusieurs étapes complexe, utilisez le streaming (`client.models.generate_content_stream`). Les requêtes synchrones sans streaming qui subissent des tentatives de réexécution du backend en cas de forte demande peuvent dépasser les fenêtres de validité des jetons de connexion ou d'authentification, ce qui peut entraîner des erreurs `401 Unauthorized` ou de délai d'expiration inattendues. Le streaming maintient la connexion active et affiche la progression du raisonnement intermédiaire et de l'appel d'outil.

## Étape suivante

- [Résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=fr) : contrôlez la résolution des images vidéo pour trouver un équilibre entre qualité et utilisation de jetons.
- [Jetons](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=fr) : découvrez comment le contenu vidéo est tokenisé en mode de traitement statique et agentique.
- [Instructions système](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=fr#system-instructions) : elles vous permettent d'orienter le comportement du modèle en fonction de vos besoins et de vos cas d'utilisation spécifiques.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) : découvrez comment importer et gérer des fichiers à utiliser avec Gemini.
- [Stratégies de prompting avec des fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide) : l'API Gemini accepte les promptings avec des données textuelles, d'image, audio et vidéo, également appelées promptings multimodaux.
- [Consignes de sécurité](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr) : les modèles d'IA générative produisent parfois des résultats inattendus, par exemple inexacts, biaisés ou choquants. Le post-traitement et l'évaluation humaine sont essentiels pour limiter le risque de préjudice lié à ces résultats.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/18 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/18 (UTC)."],[],[]]
