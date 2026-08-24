---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=fr
fetched_at: 2026-08-24T02:31:07.966389+00:00
title: "Compr\u00e9hension des vid\u00e9os \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Compréhension des vidéos

> Pour en savoir plus sur la génération de vidéos, consultez le [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).

Les modèles Gemini peuvent traiter des vidéos, ce qui permet de nombreux cas d'utilisation pour les développeurs de pointe qui auraient historiquement nécessité des modèles spécifiques à un domaine.
Certaines des fonctionnalités de vision de Gemini incluent la possibilité de décrire, de segmenter et d'extraire des informations à partir de vidéos, de répondre à des questions sur le contenu vidéo et de faire référence à des codes temporels spécifiques dans une vidéo.

Vous pouvez fournir des vidéos en entrée à Gemini de différentes manières :

| Mode de saisie | Taille maximale | Cas d'utilisation recommandé |
| --- | --- | --- |
| [API Files](#upload-video) | 20 Go (payant) / 2 Go (sans frais) | Fichiers volumineux (plus de 100 Mo), vidéos longues (plus de 10 minutes), fichiers réutilisables. |
| [Enregistrement Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr#registration) | 2 Go (par fichier, sans limites de stockage) | Fichiers volumineux (plus de 100 Mo), vidéos longues (plus de 10 minutes), fichiers persistants et réutilisables. |
| [Données intégrées](#inline-video) | Moins de 100 Mo | Petits fichiers (moins de 100 Mo), courte durée (moins d'une minute), entrées ponctuelles. |
| [URL YouTube](#youtube) | N/A | Vidéos YouTube publiques. |

> **Remarque** : L'API [Files](#upload-video) est recommandée pour la plupart des cas d'utilisation, en particulier pour les fichiers de plus de 100 Mo ou lorsque vous souhaitez réutiliser le fichier dans plusieurs requêtes.

Pour en savoir plus sur les autres méthodes de saisie de fichiers, telles que l'utilisation d'URL externes ou de fichiers
stockés dans Google Cloud, consultez le
[guide Méthodes de saisie de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

### Importer un fichier vidéo

Le code suivant télécharge un échantillon vidéo, l'importe à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr), attend qu'elle soit traitée, puis utilise la référence du fichier importé pour résumer la vidéo.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.6-flash",
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
    "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Utilisez toujours l'API Files lorsque la taille totale de la requête (y compris le fichier, le prompt textuel, les instructions système, etc.) est supérieure à 20 Mo, que la durée de la vidéo est importante ou si vous prévoyez d'utiliser la même vidéo dans plusieurs prompts.
L'API Files accepte directement les formats de fichiers vidéo.

Pour en savoir plus sur l'utilisation des fichiers multimédias, consultez
[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

### Transmettre des données vidéo intégrées

Au lieu d'importer un fichier vidéo à l'aide de l'API Files, vous pouvez transmettre des vidéos plus petites directement dans la requête à `generateContent`. Cette méthode convient aux vidéos plus courtes dont la taille totale de la requête est inférieure à 20 Mo.

Voici un exemple de fourniture de données vidéo intégrées :

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Vous pouvez transmettre des URL YouTube directement à l'API Gemini dans le cadre de votre requête comme suit :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

**Limites** :

- Pour le niveau sans frais, vous ne pouvez pas importer plus de huit heures de vidéo YouTube par jour.
- Pour le niveau payant, il n'y a pas de limite en fonction de la durée de la vidéo.
- Pour les modèles antérieurs à Gemini 2.5, vous ne pouvez importer qu'une seule vidéo par requête. Pour les modèles Gemini 2.5 et versions ultérieures, vous pouvez importer un maximum de 10 vidéos par requête.
- Vous ne pouvez importer que des vidéos publiques (et non des vidéos privées ou non répertoriées).

## Utiliser la mise en cache du contexte pour les vidéos longues

Pour les vidéos de plus de 10 minutes ou lorsque vous prévoyez d'effectuer plusieurs requêtes
sur le même fichier vidéo, utilisez la mise en cache du [contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) pour
réduire les coûts et améliorer la latence. La mise en cache du contexte vous permet de traiter la vidéo une seule fois et de réutiliser les jetons pour les requêtes suivantes. Elle est donc idéale pour les sessions de chat ou l'analyse répétée de contenus longs.

## Faire référence à des codes temporels dans le contenu

Vous pouvez poser des questions sur des moments spécifiques de la vidéo à l'aide de codes temporels au format `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extraire des insights détaillés d'une vidéo

Les modèles Gemini offrent de puissantes fonctionnalités pour comprendre le contenu vidéo en traitant les informations des flux **audio et visuel**. Vous pouvez ainsi extraire un ensemble riche de détails, y compris générer des descriptions de ce qui se passe dans une vidéo et répondre à des questions sur son contenu.

Pour les descriptions visuelles, le modèle échantillonne la vidéo à une fréquence de **1 image par seconde** (FPS). Cette fréquence d'échantillonnage par défaut fonctionne bien pour la plupart des contenus, mais notez qu'elle peut manquer des détails dans les vidéos avec des mouvements rapides ou des changements de scène rapides.
Pour les contenus à forte mobilité, envisagez de [définir une fréquence d'images personnalisée](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personnaliser le traitement vidéo

Vous pouvez personnaliser le traitement vidéo dans l'API Gemini en définissant des intervalles de découpage ou en fournissant un échantillonnage de fréquence d'images personnalisé.

### Définir des intervalles de découpage

Vous pouvez découper une vidéo en spécifiant `videoMetadata` avec des décalages de début et de fin.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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
const model = 'gemini-3.6-flash';

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

Vous pouvez définir un échantillonnage de fréquence d'images personnalisé en transmettant un argument `fps` à `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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

Par défaut, une image par seconde (FPS) est échantillonnée à partir de la vidéo. Vous pouvez définir une fréquence d'images faible (moins de 1) pour les vidéos longues. Cela est particulièrement utile pour les vidéos principalement statiques (par exemple, les conférences). Utilisez une fréquence d'images plus élevée pour les vidéos nécessitant une analyse temporelle précise, comme la compréhension d'actions rapides ou le suivi du mouvement à grande vitesse.

## Formats vidéo acceptés

Gemini est compatible avec les types MIME de format vidéo suivants :

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Informations techniques sur les vidéos

- **Modèles et contexte compatibles** : tous les modèles Gemini peuvent traiter des données vidéo.
  - Les modèles avec une fenêtre de contexte de 1 million peuvent traiter des vidéos d'une durée maximale d'une heure à la résolution multimédia par défaut ou de trois heures à la résolution multimédia faible.
- **Traitement de l'API Files** : lorsque vous utilisez l'API Files, les vidéos sont stockées à 1
  image par seconde (FPS) et l'audio est traité à 1 kbit/s (canal unique).
  Des codes temporels sont ajoutés toutes les secondes.
  - Ces taux sont susceptibles d'être modifiés à l'avenir pour améliorer l'inférence.
  - Vous pouvez remplacer la fréquence d'échantillonnage de 1 FPS en [définissant une fréquence d'images personnalisée](#custom-frame-rate).
- **Calcul des jetons** : chaque seconde de vidéo est tokenisée comme suit :
  - Images individuelles (échantillonnées à 1 FPS) :
    - Si [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=fr#MediaResolution) est défini
      sur "low", les images sont tokenisées à 66 jetons par image.
    - Sinon, les images sont tokenisées à 258 jetons par image.
  - Audio : 32 jetons par seconde.
  - Les métadonnées sont également incluses.
  - Total : environ 300 jetons par seconde de vidéo à la résolution multimédia par défaut, ou 100 jetons par seconde de vidéo à la résolution multimédia faible.
- **Résolution multimédia** : Gemini 3 introduit un contrôle précis sur le traitement de la vision multimodale
  avec le paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image d'entrée ou image vidéo**.
  Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation des jetons et la latence.

  Pour en savoir plus sur le paramètre et son impact sur les calculs de jetons, consultez le [guide sur la résolution multimédia](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=fr).
- **Format de code temporel** : lorsque vous faites référence à des moments spécifiques d'une vidéo dans votre prompt, utilisez le format `MM:SS` (par exemple, `01:15` pour 1 minute et 15 secondes).
- **Bonnes pratiques** :

  - N'utilisez qu'une seule vidéo par requête de prompt pour des résultats optimaux.
  - Si vous combinez du texte et une seule vidéo, placez le prompt textuel *après* la partie vidéo dans le tableau `contents`.
  - Sachez que les séquences d'action rapides peuvent perdre des détails en raison de la fréquence d'échantillonnage de 1 FPS. Si nécessaire, envisagez de ralentir ces clips.

## Étape suivante

Ce guide explique comment importer des fichiers vidéo et générer des sorties textuelles à partir d'entrées vidéo. Pour en savoir plus, consultez les ressources suivantes :

- [Instructions système](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#system-instructions) :
  les instructions système vous permettent d'orienter le comportement du modèle en fonction de vos
  besoins et de vos cas d'utilisation spécifiques.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) : découvrez comment importer et gérer des
  fichiers à utiliser avec Gemini.
- [Stratégies de prompting de fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide) : l'
  API Gemini est compatible avec le prompting à l'aide de données textuelles, d'images, audio et vidéo, également
  appelé prompting multimodal.
- [Conseils de sécurité](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr) : les modèles d'IA générative produisent parfois des résultats inattendus, tels que des résultats inexacts, biaisés ou choquants. Le post-traitement et l'évaluation humaine sont essentiels pour
  limiter le risque de préjudice lié à ces résultats.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
