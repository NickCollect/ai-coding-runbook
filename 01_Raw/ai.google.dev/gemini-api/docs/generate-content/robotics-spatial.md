---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=fr
fetched_at: 2026-10-26T06:01:22.412920+00:00
title: "Raisonnement spatial \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Raisonnement spatial

Les modèles Gemini Robotics ER peuvent pointer vers des objets, les suivre dans une vidéo, les détecter avec des cadres de délimitation et générer des trajectoires de mouvement. Tous les exemples de cette page utilisent des prompts en langage naturel avec `generateContent`.

Pour obtenir le code exécutable complet, consultez le
[livre de recettes sur la robotique](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Pointer vers des objets

L'exemple suivant recherche des objets spécifiques dans une image et renvoie leurs coordonnées `[y, x]` normalisées :

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

# Load your image
with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

image_response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
        PROMPT
    ],
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(image_response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

La sortie sera un tableau JSON contenant des objets, chacun avec un `point` (coordonnées `[y, x]` normalisées) et un `label` identifiant l'objet.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

L'image suivante montre comment ces points peuvent être affichés :

![Exemple affichant les points des objets dans une image](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=fr)

## Suivre des objets dans une vidéo

Gemini Robotics ER 2 peut également analyser des images vidéo pour suivre des objets au fil du temps. Pour obtenir la liste des formats vidéo compatibles, consultez [Entrées vidéo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#supported-formats).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your video
with open("my-video.mp4", 'rb') as f:
    video_bytes = f.read()

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=video_bytes,
      mime_type='video/mp4',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

## Détection d'objets et cadres de délimitation

En plus des points, vous pouvez demander au modèle de renvoyer des cadres de délimitation 2D, qui fournissent plus de détails spatiaux pour les objets détectés.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/png',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="low")
  )
)

print(image_response.text)
```

## Trajectoires

Gemini Robotics ER 2 peut générer des séquences de points qui définissent une trajectoire, ce qui est utile pour guider le mouvement d'un robot.

Cet exemple demande une trajectoire pour déplacer un stylo rouge vers un organiseur, y compris une estimation des points de passage intermédiaires. Le code a été réduit pour n'afficher que le prompt.

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## Faire de la place pour un ordinateur portable

Cet exemple montre comment Gemini Robotics ER peut raisonner sur un espace. Le prompt demande au modèle d'identifier l'objet à déplacer pour créer de l'espace pour un autre élément.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

La réponse contient une coordonnée 2D de l'objet qui répond à la question de l'utilisateur, en l'occurrence l'objet qui doit être déplacé pour faire de la place pour un ordinateur portable.

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![Exemple montrant quel objet doit être déplacé pour un autre objet](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=fr)

## Préparer un déjeuner

Le modèle peut également fournir des instructions pour les tâches en plusieurs étapes et pointer vers les objets pertinents pour chaque étape. Cet exemple montre comment le modèle planifie une série d'étapes pour préparer un sac de déjeuner.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-of-lunch.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

La réponse à ce prompt est un ensemble d'instructions détaillées sur la façon de préparer un sac de déjeuner à partir de l'image d'entrée.

**Image d'entrée**

![Image d'une boîte à lunch et des éléments à y mettre](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=fr)

**Sortie du modèle**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

## Étape suivante

- [Capacités agentiques](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=fr) : exécution de code, lecture d'instruments, annotation d'images.
- [Orchestration des tâches](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=fr) : tâches à long terme avec des API de robot personnalisées.
- [Robotique avec streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr) : streaming bidirectionnel en temps réel (Gemini Robotics ER 2 uniquement).
- [Compréhension vidéo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fr) : recherche de moments et classification de la progression (Gemini Robotics ER 2 uniquement).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/09 (UTC)."],[],[]]
