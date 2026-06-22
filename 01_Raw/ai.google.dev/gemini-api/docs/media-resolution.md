---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr
fetched_at: 2026-06-22T06:26:30.262452+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Résolution du contenu multimédia

Le paramètre `media_resolution` contrôle la façon dont l'API Gemini traite les entrées multimédias telles que les images, les vidéos et les documents PDF en déterminant le **nombre maximal de jetons** alloués aux entrées multimédias. Vous pouvez ainsi équilibrer la qualité de la réponse par rapport à la latence et au coût. Pour en savoir plus sur les différents paramètres, les valeurs par défaut et leur correspondance avec les jetons, consultez la section [Nombre de jetons](#token-counts).

Vous pouvez configurer la résolution du contenu multimédia de deux manières :

- [Par partie](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr#per-part-media-resolution) (Gemini 3 uniquement)
- [Globalement](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr#global-media-resolution) pour l'ensemble d'une requête `generateContent` (tous les modèles multimodaux)

## Résolution du contenu multimédia par partie (Gemini 3 uniquement)

Gemini 3 vous permet de définir la résolution des éléments multimédias individuels dans votre requête, ce qui vous permet d'optimiser précisément l'utilisation des jetons. Vous pouvez combiner différents niveaux de résolution dans une même requête. Par exemple, utilisez une haute résolution pour un diagramme complexe et une basse résolution pour une image contextuelle simple. Ce paramètre remplace toute configuration globale pour une pièce spécifique. Pour connaître les paramètres par défaut, consultez la section [Nombre de jetons](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Résolution média globale

Vous pouvez définir une résolution par défaut pour tous les éléments multimédias d'une requête à l'aide de `GenerationConfig`. Cette fonctionnalité est compatible avec tous les modèles multimodaux. Si une demande inclut à la fois des paramètres globaux et des [paramètres par partie](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr#per-part-media-resolution), les paramètres par partie sont prioritaires pour cet élément spécifique.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Valeurs de résolution disponibles

L'API Gemini définit les niveaux suivants pour la résolution des contenus multimédias :

- `MEDIA_RESOLUTION_UNSPECIFIED` : paramètre par défaut. Le nombre de jetons pour ce niveau varie considérablement entre Gemini 3 et les modèles Gemini précédents.
- `MEDIA_RESOLUTION_LOW` : nombre de jetons inférieur, ce qui permet un traitement plus rapide et un coût plus faible, mais avec moins de détails.
- `MEDIA_RESOLUTION_MEDIUM` : un équilibre entre le niveau de détail, le coût et la latence.
- `MEDIA_RESOLUTION_HIGH` : nombre de jetons plus élevé, fournissant plus de détails au modèle, au détriment de la latence et du coût.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (par partie uniquement) : nombre de jetons le plus élevé, requis pour des cas d'utilisation spécifiques tels que l'[utilisation d'un ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr).

Notez que `MEDIA_RESOLUTION_HIGH` offre des performances optimales pour la plupart des cas d'utilisation.

Le nombre exact de jetons générés pour chacun de ces niveaux dépend à la fois du **type de média** (image, vidéo, PDF) et de la **version du modèle**.

## Nombre de jetons

Les tableaux ci-dessous récapitulent le nombre approximatif de jetons pour chaque valeur `media_resolution` et type de support par famille de modèles.

**Modèles Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Vidéo** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (par défaut) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + texte natif |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + texte natif |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + texte natif |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | ND | ND |

**Modèles Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Vidéo** | **PDF (scanné)** | **PDF (natif)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (par défaut) | 256 + Pan & Scan (~2048) | 256 | 256 + OCR | 256 + texte natif |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + Texte natif |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + texte natif |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan &Scan | 256 | 256 + OCR | 256 + texte natif |

## Choisir la bonne résolution

- **Par défaut (`UNSPECIFIED`)** : commencez par la valeur par défaut. Il est optimisé pour offrir un bon équilibre entre qualité, latence et coût pour les cas d'utilisation les plus courants.
- **`LOW`** : à utiliser dans les scénarios où le coût et la latence sont primordiaux, et où les détails précis sont moins importants.
- **`MEDIUM` / `HIGH`** : augmentez la résolution lorsque la tâche nécessite de comprendre des détails complexes dans le contenu multimédia. Cela est souvent nécessaire pour l'analyse visuelle complexe, la lecture de graphiques ou la compréhension de documents denses.
- **`ULTRA HIGH`** : disponible uniquement pour le paramètre "Par partie". Recommandé pour des cas d'utilisation spécifiques tels que l'utilisation d'un ordinateur ou lorsque les tests montrent une nette amélioration par rapport à `HIGH`.
- **Contrôle par partie (Gemini 3)** : optimise l'utilisation des jetons. Par exemple, dans une requête comportant plusieurs images, utilisez `HIGH` pour un diagramme complexe et `LOW` ou `MEDIUM` pour des images contextuelles plus simples.

**Paramètres recommandés**

Vous trouverez ci-dessous les paramètres de résolution média recommandés pour chaque type de contenu multimédia compatible.

|  |  |  |  |
| --- | --- | --- | --- |
| **Type de contenu** | **Paramètre recommandé** | **Nombre maximal de jetons** | **Conseils d'utilisation** |
| **Images** | `MEDIA_RESOLUTION_HIGH` | 1120 | Recommandé pour la plupart des tâches d'analyse d'images afin de garantir une qualité maximale. |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Optimal pour la compréhension des documents. La qualité atteint généralement son maximum à `medium`. Augmenter la valeur à `high` améliore rarement les résultats de l'OCR pour les documents standards. |
| **Vidéo** (général) | `MEDIA_RESOLUTION_LOW` (ou `MEDIA_RESOLUTION_MEDIUM`) | 70 (par frame) | **Remarque** : Pour les vidéos, les paramètres `low` et `medium` sont traités de manière identique (70 jetons) afin d'optimiser l'utilisation du contexte. Cela suffit pour la plupart des tâches de reconnaissance et de description d'actions. |
| **Vidéo** (avec beaucoup de texte) | `MEDIA_RESOLUTION_HIGH` | 280 (par frame) | Obligatoire uniquement lorsque le cas d'utilisation implique la lecture de texte dense (OCR) ou de petits détails dans les images vidéo. |

Testez et évaluez toujours l'impact des différents paramètres de résolution sur votre application spécifique pour trouver le meilleur compromis entre qualité, latence et coût.

## Résumé de la compatibilité des versions

- L'énumération `MediaResolution` est disponible pour tous les modèles acceptant les entrées multimédias.
- Le nombre de jetons associé à chaque niveau d'énumération **diffère** entre les modèles Gemini 3 et les versions Gemini antérieures.
- Le paramètre `media_resolution` sur les objets `Part` individuels est **exclusivement disponible pour les modèles Gemini 3**.

## Étapes suivantes

- Pour en savoir plus sur les capacités multimodales de l'API Gemini, consultez les guides sur la [compréhension d'images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr), la [compréhension des vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr) et la [compréhension des documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/19 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/19 (UTC)."],[],[]]
