---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=fr
fetched_at: 2026-08-03T04:40:25.321063+00:00
title: "G\u00e9n\u00e9rer et modifier des vid\u00e9os avec Gemini\u00a0Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Générer et modifier des vidéos avec Gemini Omni Flash

Gemini Omni Flash (`gemini-omni-flash-preview`) est un modèle multimodal hautes performances conçu pour la génération et la retouche de vidéos à grande vitesse, ainsi que pour le contrôle cinématographique.
Gemini Omni repose sur les fonctionnalités de base suivantes, qui le distinguent des modèles vidéo précédents :

- **Multimodalité native** : il traite simultanément le texte, les images, l'audio et les vidéos, ce qui vous permet d'obtenir des résultats plus cohérents, plus homogènes et plus contrôlables.
- La **retouche conversationnelle**, activée par l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr), vous permet d'affiner et de modifier vos vidéos de manière itérative grâce à une conversation en langage naturel. Décrivez ce que vous souhaitez modifier, et le modèle applique la modification tout en préservant les parties de la vidéo que vous souhaitez conserver.
- **Connaissances du monde** : Gemini Omni combine une compréhension de la physique avec les connaissances de Gemini sur l'histoire, les sciences et le contexte culturel, comblant ainsi le fossé entre le photoréalisme et le storytelling pertinent.

## Génération de vidéos à partir de texte

Générez une vidéo à partir d'un prompt textuel. Le modèle génère une vidéo avec du son à partir de votre description textuelle. Pour obtenir les meilleurs résultats, rédigez des requêtes détaillées (description de la scène, mouvement de caméra, éclairage, ambiance, etc.).

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

### Schéma de réponse REST

Le champ de commodité `interaction.output_video` est **SDK uniquement**.
Obtenez la sortie vidéo à partir du tableau `steps` lorsque vous utilisez directement l'API REST.

**Structure JSON REST brute :**

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

### Contrôler le format

Définissez `aspect_ratio` sur `"9:16"` pour créer des vidéos au format portrait. Le format Paysage (16:9) est défini par défaut.

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

## Génération de vidéos à partir d'images

Vous pouvez fournir une image de référence avec votre prompt textuel. En fonction de votre requête, le modèle décidera comment utiliser l'image. Cela peut être utile pour donner vie à des photos de produits, des illustrations ou des photographies.

L'exemple suivant montre comment utiliser l'image de référence d'un dessin de poisson sautant hors de l'eau :

![Dessin d&#39;un poisson qui saute hors de l&#39;eau](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=fr)

Avec la requête suivante :

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Pour générer une vidéo réaliste du dessin.

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

### Référence de sujet

Vous pouvez générer une vidéo intégrant des sujets spécifiques fournis sous forme d'images de référence.
Par exemple, le code suivant montre comment fournir deux images d'un chat et d'une pelote de laine pour générer une vidéo du chat jouant avec la pelote de laine.

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

### Paramètre "Tasks"

Utilisez le paramètre `task` dans `video-config` pour indiquer clairement le comportement souhaité. Par exemple, si vous souhaitez que le modèle génère une vidéo à partir d'une image, vous pouvez définir le paramètre sur `image_to_video`. Si ce paramètre n'est pas défini, le modèle déduira ce que vous souhaitez à partir de la requête.

Les valeurs autorisées sont les suivantes :

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

L'exemple suivant montre comment définir cette valeur pour l'exemple d'image vers vidéo présenté précédemment.

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

## Montage vidéo avec état

Générez une vidéo et modifiez-la de manière itérative à l'aide de requêtes de suivi. Chaque tour s'appuie sur le résultat précédent. Le modèle se souvient du contexte de la vidéo et applique vos modifications tout en préservant les éléments que vous n'avez pas mentionnés. Utilisez `previous_interaction_id` pour suivre l'historique des conversations et l'état de la vidéo générée sans avoir à réimporter la vidéo précédente.

L'exemple suivant montre comment générer une première vidéo, puis la modifier :

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

Exemple de vidéo initiale :

Exemple de vidéo modifiée :

Chaque tour de conversation génère une nouvelle vidéo. Le modèle comprend le contexte des tours précédents, ce qui vous permet d'apporter des modifications incrémentales, comme ajuster la luminosité et changer l'arrière-plan, sans avoir à redécrire toute la scène.

### Modifier vos propres vidéos

Importez vos vidéos à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) pour les modifier avec Gemini Omni Flash.

L'exemple suivant montre comment modifier la vidéo d'origine suivante :

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

Exemple de vidéo modifiée :

## Récupérer des vidéos avec un URI

Utilisez le paramètre `delivery="uri"` dans `response_format` pour récupérer les vidéos générées de plus de 4 Mo.
Cela renvoie un URI hébergé par Google que vous pouvez interroger jusqu'à ce que la vidéo soit `ACTIVE` avant de la télécharger.

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

**Structure JSON REST brute (URI) :**

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

## Bonnes pratiques

- **Utilisez la diffusion par URI pour les vidéos volumineuses** : pour les vidéos de plus de 4 Mo (> 720p lorsque disponible), utilisez `delivery="uri"` dans `response_format` afin d'éviter les limites de taille de charge utile.
- **Performances optimisées** : définissez `background=false`, `store=false` et `stream=false` pour une génération unaire synchrone plus rapide. Notez que le paramètre `store=false` signifie que la vidéo générée ne pourra pas être modifiée lors des tours suivants à l'aide de `previous_interaction_id`.
- **Précision des requêtes** : pour en savoir plus, consultez la section [Conseils pour les requêtes](#prompt-guide).

## Limites

- L'importation et la modification d'images contenant des mineurs ne sont pas disponibles dans l'Espace économique européen, au Royaume-Uni ni en Suisse.
- L'importation et la modification d'images contenant certaines personnes reconnaissables ne sont pas prises en charge.
- La modification des vidéos importées n'est actuellement pas disponible pour les utilisateurs de l'Espace économique européen (EEE), de la Suisse et du Royaume-Uni (la modification des vidéos générées par le modèle est prise en charge).
- L'importation de références audio n'est pas prise en charge dans la version actuelle de l'API.
- Les références vidéo d'une durée maximale de trois secondes sont acceptées par le schéma de l'API, mais ne sont pas traitées correctement par le modèle pour le moment.
- Il n'est pas possible de faire référence à plusieurs vidéos ni de raisonner sur plusieurs vidéos. Si vous essayez d'utiliser plusieurs vidéos dans un même prompt, les performances du modèle peuvent se dégrader ou les résultats peuvent être inattendus.
- L'extension vidéo et l'interpolation vidéo (génération de vidéo entre une première et une dernière image) ne sont pas acceptées.
- La modification vocale n'est pas disponible.
- Le débit provisionné n'est pas pris en charge.
- Les instructions système, la température, `top_p`, les séquences d'arrêt et les requêtes négatives ne sont pas acceptées (vous pouvez inclure vos requêtes négatives dans la requête normale, par exemple "Ne fais pas X").
- L'utilisation de vidéos YouTube comme source multimédia n'est pas acceptée.

## Détails techniques

- Toutes les vidéos générées incluent un filigrane SynthID, qui est invisible pour les spectateurs, mais qui peut être détecté par programmation pour vérifier la provenance.
- Les délais de génération des vidéos varient en fonction de leur durée, de leur résolution et de la charge actuelle de l'API. La génération de vidéos plus longues et en haute résolution prend plus de temps.
- Les filtres de sécurité du contenu sont appliqués aux requêtes saisies et aux vidéos générées (et dépendent de votre région). Les requêtes qui ne respectent pas les règles d'utilisation seront bloquées.
- L'anglais (EN) est entièrement pris en charge, mais les autres langues n'ont pas été évaluées. Il est donc possible qu'elles fonctionnent, mais les résultats peuvent varier.

## Guide sur les prompts Gemini Omni Flash

Cette section contient des conseils et des exemples sur la façon de formuler efficacement des requêtes pour Gemini Omni Flash.

### Scène unique

Par défaut, Omni Flash essaie de créer une vidéo avec plusieurs plans différents.
Il tentera de créer un récit intéressant en fonction de la requête.

Si vous avez besoin que la vidéo de sortie ne contienne qu'une seule scène, vous devez l'indiquer dans votre requête :

- Dans une seule scène continue
- en un seul plan séquence.
- Aucune coupure de scène

Exemple :

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Supprimer les éléments indésirables

Si la vidéo générée contient des éléments que vous ne souhaitez pas voir, incluez des requêtes négatives simples pour les éviter :

- Aucun dialogue
- Aucun embellissement
- Aucun effet sonore supplémentaire

### Requêtes pour la modification

Les requêtes simples fonctionnent mieux pour le montage vidéo. Les requêtes trop descriptives peuvent entraîner des modifications inattendues.

Voici d'autres exemples de requêtes d'édition simples :

- Transforme cette vidéo en anime
- Mets un chapeau à la mode sur cette personne
- Rends l'éclairage plus dramatique
- Change le texte sur le panneau en "Omni Flash"

Lorsque vous modifiez un aspect spécifique de la vidéo, incluez `"Keep everything else the same"` pour maintenir la cohérence visuelle.

Voici quelques exemples pour illustrer l'application de cette technique :

- **À éviter :** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Simplifier** : `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **À éviter :** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Simplifier** : `Make the phone invisible. Keep everything else the
    same.`

### Demander à l'IA de générer de l'audio

Par défaut, le modèle tente de générer une piste audio appropriée pour une vidéo. Ce n'est pas toujours ce que vous souhaitez. Vous pouvez utiliser votre requête pour décrire le type d'audio que vous souhaitez. Ceci est particulièrement important si vous souhaitez inclure de la musique dans votre vidéo :

- Inclure une musique de fond calme
- La vidéo présente un beat techno très énergique
- L'audio est une émission de radio de mauvaise qualité en arrière-plan, qui diffuse une chanson.

### Événements de timing

Vous pouvez demander à ce que des choses se produisent à des moments précis de la vidéo. Aucune syntaxe précise n'est requise, et vous pouvez utiliser le langage naturel. Cela est particulièrement utile pour créer vos propres coupes de scène, séquences rythmiques ou séquences rapides.
Pour obtenir des exemples, consultez les articles suivants :

- Au bout de trois secondes, une femme entre en scène.
- À 5 s, le refrain commence dans l'audio en arrière-plan.
- Toutes les deux secondes, passez à une nouvelle image.
- Dans une séquence de questions-réponses rapides, changez de scène toutes les demi-secondes (12 images à 24 fps).

Vous pouvez également utiliser une syntaxe de code temporel :

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta-prompting

Vous pouvez demander à Gemini Omni Flash de prêter attention aux qualités ou principes généraux de la génération de vidéos :

- Tenez compte des micro-détails, des expressions et du timing pour créer une scène très riche et détaillée, mais entièrement naturelle.
- Soyez extrêmement précis dans vos descriptions des personnages et des environnements.
  Appliquez les principes de conception de costumes aux personnages. Soyez très précis sur les personnes, les éléments et les objets présents dans la scène.
- Incluez de nombreux détails appropriés dans les éléments d'arrière-plan pour que la scène semble réaliste et naturelle.
- Crée une vidéo en rafale qui montre un `[thing]` rare différent toutes les secondes, avec une musique entraînante et un texte pour identifier l'objet.

### Texte dans les vidéos

Vous pouvez demander à inclure du texte dans votre vidéo. Gemini Omni l'affichera de manière correcte et lisible. Si votre vidéo contient du texte de manière naturelle, même dans les éléments d'arrière-plan, il peut être utile de définir ce qu'il doit dire.

- Un mot à la fois à l'écran : "saviez, vous, que, Omni, peut, créer, des, textes, géniaux ?" Chaque mot s'affiche pendant une seconde avec un style d'animation différent. Aucun dialogue.
- Un panneau de rue indique "This is an AI generation by Omni" (Ceci est une génération d'IA par Omni), une vitrine indique "All you need AI" (Tout ce dont vous avez besoin, c'est l'IA) et une voiture porte la plaque d'immatriculation "OMN111".

### Utiliser des tags dans les requêtes pour définir les rôles des images

Vous pouvez utiliser des tags pour associer les contenus multimédias importés à des rôles de génération spécifiques. Cela vous permet d'indiquer si chaque image est une image initiale ou une référence.

#### 1. Balises simples (recommandées)

Dans les cas simples où les rôles des images sont clairs à partir de l'invite, vous pouvez associer directement les images aux rôles :

- **`<FIRST_FRAME>`** : utilisez l'image comme frame de départ de la vidéo, par exemple : `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`** : utiliser l'image comme référence, par exemple : `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combine la référence de style de la première image et la référence de sujet de la deuxième image).
  Les références d'image commencent à 0.

Voici un exemple avec six images de référence :

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Déclarations explicites

Pour les cas plus complexes avec plusieurs images et plusieurs rôles, vous pouvez utiliser des tags de préfixe explicites associés à des suffixes d'instructions en langage naturel.

- **Déclarer les sources et les images de référence** :
  - `[# Sources <FIRST_FRAME>@Image1]` utilisera la première image comme frame de départ.
  - `[# References <IMAGE_REF_0>@Image1]` utilisera la première image comme référence.
  - `[# References <IMAGE_REF_1>@Image2]` utilisera la deuxième image comme référence.
  - `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` utilisera les deux images comme références.
  - `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` utilisera la première image comme frame de départ et la deuxième image comme référence.
- **Instructions de guidage** : ajoutez des instructions de guidage à la toute fin de votre requête :
  - Pour l'image de début : `"Use this image as the starting frame."`
  - Pour les images de référence : `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

Exemple de requête développée :

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## Étape suivante

- Commencez à utiliser Gemini Omni Flash en faisant des tests dans le [notebook Colab de démarrage rapide Omni](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=fr).
- Découvrez comment rédiger des requêtes encore plus efficaces grâce à notre [présentation de la conception des requêtes](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
