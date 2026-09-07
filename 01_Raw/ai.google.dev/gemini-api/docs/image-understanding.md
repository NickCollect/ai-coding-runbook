---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr
fetched_at: 2026-09-07T05:49:13.815071+00:00
title: "Compr\u00e9hension des images \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Compréhension des images

Les modèles Gemini sont conçus dès le départ pour être multimodaux, ce qui permet d'effectuer un large éventail de tâches de traitement d'images et de vision par ordinateur, y compris, mais sans s'y limiter, la légende d'images, la classification et la réponse visuelle à des questions, sans avoir à entraîner des modèles de ML spécialisés.

En plus de leurs capacités multimodales générales, les modèles Gemini offrent
**une précision accrue** pour des cas d'utilisation spécifiques tels que [la détection d'objets](#object-detection)
et [la segmentation](#segmentation), grâce à un entraînement supplémentaire.

## Transmettre des images à Gemini

Vous pouvez fournir des images en entrée à Gemini à l'aide de plusieurs méthodes :

- [Transmettre une image à l'aide d'une URL](#url-image) : idéal pour les images accessibles au public.
- [Transmettre des données d'image intégrées](#inline-image) : pour les données d'image encodées en base64.
- [Importer des images à l'aide de l'API Files](#upload-image) : recommandé pour les
  fichiers plus volumineux ou pour réutiliser des images dans plusieurs requêtes.

### Transmettre une image à l'aide d'une URL

Vous pouvez importer une image à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) et la transmettre
dans la requête :

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Transmettre des données d'image intégrées

Vous pouvez fournir des données d'image sous forme de chaînes encodées en base64 :

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

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
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Importer des images à l'aide de l'API Files

Pour les fichiers volumineux ou pour pouvoir utiliser le même fichier image à plusieurs reprises, utilisez l'API Files. Consultez le guide de l'API [Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Utiliser plusieurs images dans un prompt

Vous pouvez fournir plusieurs images dans un seul prompt en incluant plusieurs objets image dans le tableau `input` :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
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
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Détection d'objets

Les modèles sont entraînés pour détecter des objets dans une image et obtenir les coordonnées de leur cadre de délimitation. Les coordonnées, par rapport aux dimensions de l'image, sont mises à l'échelle de [0, 1000]. Vous devez déséchelonner ces coordonnées en fonction de la taille d'image d'origine.

 

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

Pour en savoir plus, consultez le [livre de recettes Gemini](https://github.com/google-gemini/cookbook).

## Segmentation

Les modèles Gemini ne se contentent pas de détecter les éléments, ils les segmentent également et fournissent leurs masques de contour.

Le modèle prédit une liste JSON, où chaque élément représente un masque de segmentation. Chaque élément comporte un cadre de délimitation ("`box_2d`") au format `[ymin, xmin, ymax, xmax]` avec des coordonnées normalisées comprises entre 0 et 1000, une étiquette ("`label`") qui identifie l'objet, et enfin le masque de segmentation à l'intérieur du cadre de délimitation sous la forme d'un polygone de coordonnées `[x, y]` normalisées entre 0 et 1000.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![Table avec des cupcakes, avec les objets en bois et en verre mis en évidence](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=fr)

Exemple de sortie de segmentation avec des objets et des masques de segmentation

## Formats d'image compatibles

Gemini est compatible avec les types MIME suivants pour les formats d'image :

- PNG : `image/png`
- JPEG : `image/jpeg`
- WEBP : `image/webp`
- HEIC : `image/heic`
- HEIF : `image/heif`

Pour en savoir plus sur les autres méthodes d'entrée de fichiers, consultez le
[guide Méthodes d'entrée de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

## Capacités

Toutes les versions du modèle Gemini sont multimodales et peuvent être utilisées dans un large éventail de tâches de traitement d'images et de vision par ordinateur, y compris, mais sans s'y limiter, la description d'images, la réponse visuelle à des questions, la classification d'images, la détection d'objet et la segmentation.

Gemini peut réduire le besoin d'utiliser des modèles de ML spécialisés en fonction de vos exigences en termes de qualité et de performances.

[[Les dernières versions du modèle sont spécifiquement entraînées pour améliorer la précision des tâches spécialisées en plus des capacités génériques, comme la détection et la segmentation d'objets améliorées.](#object-detection)](#segmentation)

## Limites et informations techniques clés

### Limite de fichiers

Les modèles Gemini sont compatibles avec un maximum de 3 600 fichiers image par requête.

### Calcul des jetons

- 258 jetons si les deux dimensions sont inférieures ou égales à 384 pixels.
  Les images plus grandes sont divisées en vignettes de 768 x 768 pixels, chacune coûtant 258 jetons.

Voici une formule approximative pour calculer le nombre de vignettes :

- Calculez la taille de l'unité de recadrage, qui est approximativement : `floor(min(width, height)` / 1.5).
- Divisez chaque dimension par la taille de l'unité de recadrage et multipliez-les pour obtenir le nombre de vignettes.

Par exemple, une image de 960 x 540 pixels aurait une taille d'unité de recadrage de 360. Divisez chaque dimension par 360. Le nombre de vignettes est de 3 \* 2 = 6.

### Résolution des contenus multimédias

Gemini 3 introduit un contrôle précis du traitement de la vision multimodale avec le paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image d'entrée ou par image vidéo**.
Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation des jetons et la latence.

## Conseils et bonnes pratiques

- Vérifiez que les images sont correctement pivotées.
- Utilisez des images claires et nettes.
- Lorsque vous utilisez une seule image avec du texte, placez le prompt textuel *avant* l'image dans le tableau `input`.

## Étape suivante

Ce guide explique comment importer des fichiers image et générer des sorties de texte à partir d'entrées d'image. Pour en savoir plus, consultez les ressources suivantes :

- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) : découvrez comment importer et gérer des fichiers à utiliser avec Gemini.
- [Instructions système](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#system-instructions) :
  les instructions système vous permettent d'orienter le comportement du modèle en fonction de vos
  besoins et de vos cas d'utilisation spécifiques.
- [Stratégies de prompt pour les fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide) : l'
  API Gemini est compatible avec les prompts contenant des données de texte, d'image, audio et vidéo, également
  appelés prompts multimodaux.
- [Conseils de sécurité](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr) : les modèles d'IA générative produisent parfois des résultats inattendus, tels que des résultats inexacts, biaisés ou choquants. Le post-traitement et l'évaluation humaine sont essentiels pour limiter le risque de préjudice lié à ces résultats.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
