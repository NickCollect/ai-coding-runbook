---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr
fetched_at: 2026-10-05T06:28:38.925341+00:00
title: "R\u00e9solution multim\u00e9dia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Résolution multimédia

Le paramètre `media_resolution` contrôle la façon dont l'API Gemini traite les entrées multimédias telles que les images, les vidéos, l'audio et les documents PDF en déterminant le **nombre maximal de jetons** alloués aux entrées multimédias. Cela vous permet d'équilibrer la qualité de la réponse par rapport à la latence et au coût. Alors que les entrées visuelles et de documents adaptent l'allocation de jetons en fonction du paramètre de résolution, les entrées audio sont tokenisées à un taux fixe par seconde, quel que soit le niveau de résolution. Pour connaître les différents paramètres, les valeurs par défaut et leur correspondance avec les jetons, consultez la section [Nombre de jetons](#token-counts).

Vous pouvez configurer la résolution des éléments multimédias individuels (éléments de contenu) dans votre requête (Gemini 3 uniquement).

## Résolution des contenus multimédias par élément (Gemini 3 uniquement)

Gemini 3 vous permet de définir la résolution des éléments multimédias individuels dans votre requête, ce qui vous permet d'optimiser précisément l'utilisation des jetons. Vous pouvez combiner différents niveaux de résolution dans une même requête. Par exemple, utilisez une haute résolution pour un diagramme complexe et une basse résolution pour une image contextuelle simple.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
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
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
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
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Valeurs de résolution disponibles

L'API Gemini définit les niveaux suivants pour la résolution des contenus multimédias :

- `unspecified` : paramètre par défaut. Le nombre de jetons pour ce niveau varie considérablement entre Gemini 3 et les modèles Gemini antérieurs.
- `low` : nombre de jetons inférieur, ce qui permet un traitement plus rapide et un coût plus faible, mais avec moins de détails.
- `medium` : un équilibre entre le niveau de détail, le coût et la latence.
- `high` : nombre de jetons plus élevé, ce qui permet au modèle de disposer de plus de détails, mais augmente la latence et le coût.
- `ultra_high` (par élément de contenu uniquement) : nombre de jetons le plus élevé, requis pour des cas d'utilisation spécifiques tels que l'[utilisation d'un ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr).

Notez que `high` offre des performances optimales pour la plupart des cas d'utilisation.

Le nombre exact de jetons générés pour chacun de ces niveaux dépend à la fois du **type de contenu multimédia** (image, vidéo, audio, PDF) et de la **version du modèle**.

## Nombre de jetons

Les tableaux ci-dessous récapitulent le nombre approximatif de jetons pour chaque valeur `media_resolution` et type de support par famille de modèles.

**Modèles Gemini 3**

| MediaResolution | Image | Vidéo | Audio | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (par défaut) | 1120 | 70 | 25 (par seconde) | 560 |
| `low` | 280 | 70 | 25 (par seconde) | 280 + texte natif |
| `medium` | 560 | 70 | 25 (par seconde) | 560 + texte natif |
| `high` | 1120 | 280 | 25 (par seconde) | 1120 + texte natif |
| `ultra_high` | 2240 | N/A | N/A | N/A |

## Choisir la bonne résolution

- **Par défaut (`unspecified`)** : commencez par la valeur par défaut. Il est optimisé pour offrir un bon équilibre entre qualité, latence et coût pour la plupart des cas d'utilisation courants.
- **`low`** : à utiliser dans les scénarios où le coût et la latence sont primordiaux, et où les détails précis sont moins importants.
- **`medium` / `high`** : augmentez la résolution lorsque la tâche nécessite de comprendre des détails complexes dans le contenu multimédia. Cela est souvent nécessaire pour l'analyse visuelle complexe, la lecture de graphiques ou la compréhension de documents denses.
- **`ultra_high`** : disponible uniquement pour le paramètre "Par élément de contenu". Recommandé pour des cas d'utilisation spécifiques tels que l'utilisation d'un ordinateur ou lorsque les tests montrent une nette amélioration par rapport à `high`.
- **Contrôle par élément de contenu (Gemini 3)** : optimise l'utilisation des jetons. Par exemple, dans une requête comportant plusieurs images, utilisez `high` pour un diagramme complexe et `low` ou `medium` pour des images contextuelles plus simples.

**Paramètres recommandés**

Vous trouverez ci-dessous les paramètres de résolution média recommandés pour chaque type de média compatible.

| Type de support | Réglage recommandé | Nombre maximal de jetons | Conseils d'utilisation |
| --- | --- | --- | --- |
| **Images** | `high` | 1120 | Recommandé pour la plupart des tâches d'analyse d'images afin de garantir une qualité maximale. |
| **PDF** | `medium` | 560 | Optimal pour la compréhension des documents. La qualité atteint généralement son maximum à `medium`. Augmenter la valeur à `high` améliore rarement les résultats de l'OCR pour les documents standards. |
| **Vidéo** (général) | `low` (ou `medium`) | 70 (par frame) | **Remarque** : Pour les vidéos, les paramètres `low` et `medium` sont traités de manière identique (70 jetons) afin d'optimiser l'utilisation du contexte. Cela suffit pour la plupart des tâches de reconnaissance et de description d'actions. |
| **Vidéo** (avec beaucoup de texte) | `high` | 280 (par frame) | Obligatoire uniquement lorsque le cas d'utilisation implique la lecture de texte dense (OCR) ou de petits détails dans les images vidéo. |
| **Audio** | `unspecified` (par défaut) | 25 (par seconde) | L'audio est tokenisé à un taux fixe de 25 jetons par seconde pour tous les paramètres de résolution compatibles (`unspecified`, `low`, `medium` et `high`). |

Testez et évaluez toujours l'impact des différents paramètres de résolution sur votre application afin de trouver le meilleur compromis entre qualité, latence et coût.

## Relation avec les modes de traitement vidéo

Les paramètres `media_resolution` et de traitement contrôlent différents aspects de l'entrée vidéo :

- `media_resolution` contrôle la **résolution** de chaque frame (nombre de jetons par frame).
- Les commandes `processing` / `media_processing` déterminent **le contenu de la vidéo** qui est chargé dans le contexte.

Vous pouvez définir les deux sur la même entrée vidéo. Par exemple, vous pouvez utiliser le traitement agentique avec une résolution média faible pour minimiser l'utilisation totale de jetons pour une longue vidéo.

Pour en savoir plus sur les modes de traitement vidéo, consultez le guide [Comprendre les vidéos avec l'approche agentique](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#agentic-video-understanding).

## Résumé de la compatibilité des versions

- La définition de `resolution` sur des éléments de contenu individuels est **exclusive aux modèles Gemini 3**.

## Étapes suivantes

- Pour en savoir plus sur les capacités multimodales de l'API Gemini, consultez les guides [Comprendre les images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr), [Comprendre les vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr), [Comprendre l'audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr) et [Comprendre les documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
