---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr
fetched_at: 2026-09-07T05:40:29.717085+00:00
title: "Compr\u00e9hension des vid\u00e9os \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
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

Pour en savoir plus sur les autres méthodes d'entrée de fichiers, telles que l'utilisation d'URL externes ou de fichiers
stockés dans Google Cloud, consultez le
[guide Méthodes d'entrée de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

### Importer un fichier vidéo

Le code suivant télécharge un échantillon vidéo, l'importe à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr), attend qu'elle soit traitée, puis utilise la référence du fichier importé pour résumer la vidéo.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Utilisez toujours l'API Files lorsque la taille totale de la requête (y compris le fichier, le prompt textuel, les instructions système, etc.) est supérieure à 20 Mo, que la durée de la vidéo est importante ou si vous prévoyez d'utiliser la même vidéo dans plusieurs prompts.
L'API Files accepte directement les formats de fichiers vidéo.

Pour en savoir plus sur l'utilisation des fichiers multimédias, consultez
[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

### Transmettre des données vidéo intégrées

Au lieu d'importer un fichier vidéo à l'aide de l'API Files, vous pouvez transmettre des vidéos plus petites directement dans la requête. Cette approche convient aux vidéos plus courtes dont la taille totale de la requête est inférieure à 20 Mo.

Voici un exemple de fourniture de données vidéo intégrées :

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
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

### Transmettre des URL YouTube

Vous pouvez transmettre des URL YouTube directement à l'API Gemini dans le cadre de votre requête comme suit :

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Limites** :

- Pour le niveau sans frais, vous ne pouvez pas importer plus de huit heures de vidéo YouTube par jour.
- Pour le niveau payant, il n'existe aucune limite basée sur la durée de la vidéo.
- Pour les modèles antérieurs à Gemini 2.5, vous ne pouvez importer qu'une seule vidéo par requête. Pour les modèles Gemini 2.5 et ultérieurs, vous pouvez importer jusqu'à 10 vidéos par requête.
- Vous ne pouvez importer que des vidéos publiques (et non des vidéos privées ou non répertoriées).

## Faire référence à des codes temporels dans le contenu

Vous pouvez poser des questions sur des moments spécifiques de la vidéo à l'aide de codes temporels au format `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extraire des insights détaillés d'une vidéo

Les modèles Gemini offrent de puissantes fonctionnalités pour comprendre le contenu vidéo en traitant les informations des flux **audio et visuel**. Vous pouvez ainsi extraire un ensemble riche de détails, y compris générer des descriptions de ce qui se passe dans une vidéo et répondre à des questions sur son contenu.

Pour les descriptions visuelles, le modèle échantillonne la vidéo à une fréquence de **1 image par seconde** (FPS). Cette fréquence d'échantillonnage par défaut fonctionne bien pour la plupart des contenus, mais notez qu'elle peut manquer des détails dans les vidéos avec des mouvements rapides ou des changements de scène rapides.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Formats vidéo acceptés

Gemini est compatible avec les types MIME de format vidéo suivants :

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Informations techniques sur les vidéos

- **Modèles et contexte compatibles** : tous les modèles Gemini peuvent traiter des données vidéo.
  - Les modèles avec une fenêtre de contexte de 1 million peuvent traiter des vidéos d'une durée maximale d'une heure à la résolution multimédia par défaut ou de trois heures à une faible résolution multimédia.
- **Traitement de l'API Files** : lorsque vous utilisez l'API Files, les vidéos sont stockées à 1
  image par seconde (FPS) et l'audio est traité à 1 kbit/s (canal unique).
  Des codes temporels sont ajoutés toutes les secondes.
  - Ces taux sont susceptibles d'être modifiés à l'avenir pour améliorer l'inférence.
- **Calcul des jetons** : chaque seconde de vidéo est tokenisée comme suit :
  - Images individuelles (échantillonnées à 1 FPS) :
    - Si `media_resolution` est défini sur "low", les images sont tokenisées à 66 jetons par image.
    - Sinon, les images sont tokenisées à 258 jetons par image.
  - Audio : 32 jetons par seconde.
  - Les métadonnées sont également incluses.
  - Total : environ 300 jetons par seconde de vidéo à la résolution multimédia par défaut, ou 100 jetons par seconde de vidéo à faible résolution multimédia.
- **Résolution multimédia** : Gemini 3 introduit un contrôle précis sur le traitement de la vision multimodale
  avec le paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image d'entrée ou image vidéo**.
  Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation des jetons et la latence.

  Pour en savoir plus sur le calcul des jetons, consultez le [guide sur les jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr).
- **Format du code temporel** : lorsque vous faites référence à des moments spécifiques d'une vidéo dans votre prompt, utilisez le format `MM:SS` (par exemple, `01:15` pour 1 minute et 15 secondes).
- **Bonnes pratiques** :

  - Pour des résultats optimaux, n'utilisez qu'une seule vidéo par requête de prompt.
  - Si vous combinez du texte et une seule vidéo, placez le prompt textuel *après* la partie vidéo dans le tableau `input`.
  - Sachez que les séquences d'action rapides peuvent perdre des détails en raison de la fréquence d'échantillonnage de 1 FPS. Si nécessaire, envisagez de ralentir ces clips.

## Étape suivante

Ce guide explique comment importer des fichiers vidéo et générer des sorties de texte à partir d'entrées vidéo. Pour en savoir plus, consultez les ressources suivantes :

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
