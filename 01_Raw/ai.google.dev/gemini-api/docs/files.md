---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=fr
fetched_at: 2026-10-26T05:57:33.005774+00:00
title: "API Files \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Files

Gemini peut traiter simultanément différents types de données d'entrée, y compris du texte, des images et de l'audio.

Ce guide vous explique comment utiliser des fichiers multimédias à l'aide de l'API Files. Les opérations de base sont les mêmes pour les fichiers audio, les images, les vidéos, les documents et les autres types de fichiers acceptés.

Pour obtenir des conseils sur les prompts de fichiers, consultez la section [Guide sur les prompts de fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide).

## Importer un fichier

Vous pouvez utiliser l'API Files pour importer un fichier multimédia. Utilisez toujours l'API Files lorsque la taille totale de la requête (y compris les fichiers, le prompt textuel, les instructions système, etc.) est supérieure à 100 Mo. Pour les fichiers PDF, la limite est de 50 Mo.

Le code suivant importe un fichier, puis l'utilise dans un appel à `interactions.create`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .uri(myFile.uri().orElse(""))
        .mimeType(AudioContentMimeType.of(myFile.mimeType().orElse("audio/mp3")))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

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

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe this audio clip",
                }),
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(myFile.URI),
                    MimeType: interactions.AudioContentMimeType(myFile.MIMEType).ToPointer(),
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
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Obtenir les métadonnées d'un fichier

Vous pouvez vérifier que l'API a bien stocké le fichier importé et obtenir ses métadonnées en appelant `files.get`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

String fileName = myFile.name().orElse("");
File fileMetadata = client.files.get(fileName, null);
System.out.println(fileMetadata);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileMetadata, err := client.Files.Get(ctx, myFile.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileMetadata)
}
```

### REST

```
# file_info.json was created in the upload example
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## Lister les fichiers importés

Le code suivant permet d'obtenir la liste de tous les fichiers importés :

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;

Client client = new Client();

System.out.println("My files:");
for (File f : client.files.list(null)) {
  System.out.println("  " + f.name().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("My files:")
    for f, err := range client.Files.All(ctx) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(" ", f.Name)
    }
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Supprimer des fichiers importés

Les fichiers sont automatiquement supprimés au bout de 48 heures. Vous pouvez également supprimer manuellement un fichier importé :

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

client.files.delete(myFile.name().orElse(""), null);
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    if _, err := client.Files.Delete(ctx, myFile.Name, nil); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Informations sur l'utilisation

Vous pouvez utiliser l'API Files pour importer des fichiers multimédias et interagir avec eux. L'API Files vous permet de stocker jusqu'à 20 Go de fichiers par projet, avec une taille maximale de 2 Go par fichier. Les fichiers sont stockés pendant 48 heures.

Pendant ce temps, vous pouvez utiliser l'API pour obtenir des métadonnées sur les fichiers. Toutefois, vous ne pouvez pas télécharger les fichiers importés par les utilisateurs. Vous pouvez télécharger les fichiers générés par les modèles, tels que les vidéos, à l'aide de la méthode `files.download`. L'API Files est disponible sans frais dans toutes les régions où l'API Gemini est disponible.

## Stratégies de prompting de fichiers

Cette section fournit des conseils et des bonnes pratiques pour utiliser des fichiers multimédias avec des requêtes pour l'API Gemini.

La possibilité d'utiliser différents types de données dans vos requêtes vous offre plus de flexibilité quant aux tâches que vous pouvez effectuer avec l'API Gemini. Par exemple, vous pouvez envoyer au modèle la photo d'un délicieux repas et lui demander d'écrire un court article de blog à ce sujet.

|  |  |
| --- | --- |
| **Prompt** (Requête) | **Réponse** |
| Rédigez un article de blog court et attrayant basé sur cette photo. Il doit inclure une description du repas sur la photo et parler de ma méthode de préparation de repas.   Cookies | Préparer ses repas à l'avance est un excellent moyen de gagner du temps et de l'argent, et cela peut également vous aider à manger plus sainement. Ce repas est un excellent exemple de plat sain et délicieux qui peut être préparé à l'avance.  Ce repas se compose de riz brun, de légumes rôtis et de poulet teriyaki. Le riz brun est un glucide complexe et sain qui vous apportera de l'énergie de façon durable. Les légumes rôtis sont un excellent moyen d'obtenir votre dose quotidienne de vitamines et de minéraux, et le poulet teriyaki est une option délicieuse et riche en protéines.  Ce repas est également simple à préparer. Il vous suffit de faire cuire le riz brun, de rôtir les légumes et de faire cuire le poulet teriyaki. Une fois que tout est cuit, répartissez les aliments dans des boîtes de préparation de repas et conservez-les au réfrigérateur. Vous pouvez ensuite prendre un conteneur et partir les matins chargés !  Si vous cherchez un repas sain et délicieux qui peut être préparé à l'avance, ce plat est une excellente option. Il est riche en nutriments et en saveurs, et vous permettra de vous sentir rassasié et satisfait.  Bonne préparation de repas sains et délicieux ! |

Si vous ne parvenez pas à obtenir le résultat souhaité à partir de requêtes utilisant des fichiers multimédias, certaines stratégies peuvent vous aider à obtenir les résultats souhaités. Les sections suivantes fournissent des approches de conception et des conseils de dépannage pour améliorer les prompts qui utilisent des entrées multimodales.

Vous pouvez améliorer vos requêtes multimodales en suivant ces bonnes pratiques :

- ### [Principes de base de la conception d'invites](#specific-instructions)

  - **Soyez précis dans vos instructions** : définissez des instructions claires et concises qui laissent peu de place aux erreurs d'interprétation.
  - **Ajoutez quelques exemples à votre requête** :utilisez des exemples réalistes pour illustrer votre objectif.
  - **Décomposez la tâche étape par étape** : divisez les tâches complexes en sous-objectifs gérables pour guider le modèle tout au long du processus.
  - **Spécifiez le format de sortie** : dans votre requête, demandez la sortie au format souhaité, tel que Markdown, JSON, HTML, etc.
  - **Mettez en avant votre image pour les requêtes liées à une seule image** : bien que Gemini puisse gérer les entrées d'image et de texte dans n'importe quel ordre, les requêtes qui contiennent une seule image peuvent fonctionner mieux si cette image (ou vidéo) est placée avant la requête de texte. Toutefois, pour les requêtes qui nécessitent que les images soient fortement imbriquées avec les textes pour avoir du sens, utilisez l'ordre le plus naturel.
- ### [Résoudre les problèmes liés à un prompt multimodal](#troubleshooting)

  - **Si le modèle n'extrait pas d'informations de la partie pertinente de l'image** : ajoutez des indications sur les aspects de l'image à partir desquels vous souhaitez que la requête puise des informations.
  - **Si le résultat du modèle est trop générique (non adapté à l'entrée image/vidéo)** : au début de la requête, essayez de demander au modèle de décrire les images ou les vidéos avant de fournir les instructions de la tâche. ou essayez de demander au modèle de faire référence à ce qui est illustré.
  - **Dépannage** : demandez au modèle de décrire l'image ou demandez au modèle d'expliquer sa raisonnement pour évaluer sa compréhension initiale.
  - **Si votre requête génère du contenu incohérent**, essayez de réduire le paramétrage de la température ou de demander au modèle des descriptions plus courtes afin de réduire les risques d'extrapolation.
  - **Réglez les paramètres d'échantillonnage** : testez différents paramètres de température et des sélections en haut de la plage pour ajuster la créativité du modèle.

### Indiquez des instructions précises.

Les requêtes sont plus efficaces lorsqu'elles sont claires et détaillées. Si vous avez une sortie spécifique en tête, il est préférable d'inclure cette exigence dans la requête pour vous assurer d'obtenir le résultat souhaité.

Pour cette image de tableau d'aéroport, demander au modèle de "décrire cette image" peut générer une description générale. Si vous avez besoin du modèle pour analyser une heure et une ville à partir de l'image, vous pouvez inclure cette requête directement dans votre prompt.

| Prompt | Réponse de modèle |
| --- | --- |
| Décrivez cette image. | L'image montre un tableau des arrivées et des départs d'aéroport. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Horaires de transport Analysez les heures et les villes du tableau d'aéroport présent l'image ci-dessous et affichez-les sous forme de liste. | - 10:50 Moscou - 11:05 Édimbourg - 11:05 Londres - 11:10 Bucarest - 11:30 Kiev - 11:35 Dublin - 11:45 Midlands de l'Est - 12:15 Sofia - 12:30 Londres - 12:30 Newcastle - 12:40 Saint-Pétersbourg - 12:40 Londres - 12:45 Manchester |

### Ajouter quelques exemples

Le modèle Gemini peut accepter plusieurs entrées qu'il peut utiliser comme exemples pour comprendre la sortie que vous souhaitez. L'ajout de ces exemples peut aider le modèle à identifier les schémas et à appliquer la relation entre les images et les réponses fournies au nouvel exemple. C'est ce qu'on appelle l'apprentissage few-shot.

Dans l'exemple suivant, la sortie initiale est rédigée sous forme de phrase et contient également le pays (Brésil). Supposons que vous souhaitiez que le résultat soit présenté dans un format ou un style différent, et que vous ne souhaitiez obtenir que la ville, et non le pays. En ajoutant des exemples few-shot à votre requête, vous pouvez orienter le modèle pour qu'il réponde comme vous le souhaitez.

| **Prompt** (Requête) | **Réponse de modèle** |
| --- | --- |
| Horaires de transport Déterminez la ville et le repère. | Le repère est la statue du Christ Rédempteur à Rio de Janeiro, au Brésil. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Déterminez la ville et le repère. colisée | ville : Rome ; repère : le Colisée. |
| Cité interdite | ville : Pékin ; repère : la Cité interdite |
| forbidden-city | Ville : Rio de Janeiro ; repère : statue du Christ Rédempteur |

### Procéder étape par étape

Pour les tâches complexes telles que celles nécessitant une compréhension visuelle et un raisonnement, il peut être utile de diviser la tâche en étapes plus petites et plus simples. Cela peut également être efficace si vous demandez directement au modèle de "penser étape par étape" dans votre requête.

| Prompt | Réponse de modèle |
| --- | --- |
| Quand vais-je manquer de papier toilette ? | Bientôt, car il ne vous reste que trois rouleaux. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| 1. Commencez par compter le nombre de rouleaux de papier toilette apparaissant sur cette photo. 2. Déterminez ensuite la quantité de papier toilette qu'une personne type utilise par jour. 3. Calculez la durée de vie de ces rouleaux de papier toilette. | 1. Sur cette photo, on voit trois rouleaux de papier toilette. 2. Une personne type utilise environ 20 feuilles de papier toilette par jour. 3. Si un rouleau contient 200 feuilles, chaque rouleau dure environ 10 jours. Par conséquent, les trois rouleaux dureront environ un mois. |

Les problèmes mathématiques ou les problèmes basés sur les mots sont d'excellents candidats pour demander au modèle de réfléchir étape par étape.

| **Prompt** (Requête) | **Response** (Réponse) |
| --- | --- |
| Quel est le quatrième terme de la séquence ? | -135 |

La réponse du modèle est incorrecte. Pour améliorer cela, vous pouvez demander au modèle d'analyser le problème avant de répondre à la requête.

| **Prompt** (Requête) | **Response** (Réponse) |
| --- | --- |
| Analyse d'abord la formule dans l'image.  Ensuite, en fonction de la formule, répondez à la question "Quel est le quatrième terme de la séquence ?". | *Cliquez pour développer le résultat* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Remplacez "n = 4" dans la formule : $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Nous ne connaissons pas la valeur de b(3). Remplacez donc n = 3 dans la formule : $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Nous ne connaissons pas la valeur de b(2). Remplacez donc n = 2 dans la formule : $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Nous savons que la valeur de b(1) est 15. Remplacez-la par la formule : $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Maintenant que nous connaissons la valeur de b(2), remplacez-la dans la formule de b(3) : $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Maintenant que nous connaissons la valeur de b(3), remplacez-la dans la formule de b(4) : $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Par conséquent, le quatrième terme de la séquence est -405. |

La réponse du modèle est correcte. Pour la rendre encore plus fluide, vous pouvez demander au modèle de réfléchir étape par étape.

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Quel est le quatrième terme de la séquence ? Réfléchir étape par étape | Le premier terme est 15.  Le deuxième terme est b(1) \* (-3) = 15 \* (-3) = -45.  Le troisième terme est b(2) \* (-3) = -45 \* (-3) = 135.  Le quatrième terme est b(3) \* (-3) = 135 \* (-3) = -405. |

### Spécifier le format de sortie

Un problème courant est le besoin d'avoir un format spécifique pour la sortie du modèle (par exemple, Markdown, JSON, HTML), en particulier si celle-ci doit être ingérée par une tâche en aval. Vous pouvez essayer de produire un résultat dans ce format en demandant au modèle via la requête. Voici deux exemples :

| Prompt | Réponse de modèle |
| --- | --- |
| Analysez le tableau de cette image au format Markdown | ```none | Sujet | État | Durée | Date de début | Date limite | | ------- | ------ | ---- | ---------- | ------ | | Mathématiques | Terminé | 1,5 h | 29/11/2023 | 01/12/2023 | | Géographie | Terminé | 30 min | 02/12/2023 | 04/12/2023 | | Physique | En cours | 2 h | 03/12/2023 | 05/12/2023 | | Biologie | Non commencé | 6 h | 02/11/2016 | 06/12/2023 | ``` |

| **Prompt** (Requête) | **Réponse de modèle** |
| --- | --- |
| Fournissez la liste de tous les attributs suivants :  ingrédients, type de cuisine, végétarien ou non, au format JSON | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### Utilisez votre image en premier pour les requêtes liées à une seule image

Bien que Gemini puisse interpréter l'image et le texte dans n'importe quel ordre dans un prompt, le fait de placer une seule image avant le prompt textuel peut offrir de meilleurs résultats.
Dans les exemples suivants, vous remarquerez que l'image précède le texte dans chaque requête.

### Résoudre les problèmes liés à un prompt multimodal

Vous devrez peut-être résoudre les problèmes liés à votre prompt si vous n'obtenez pas de réponse utile. Voici quelques stratégies que vous pouvez essayer.

#### Si le modèle n'extrait pas d'informations de la partie pertinente de l'image

Pour obtenir une réponse plus spécifique, vous pouvez indiquer les aspects de l'image à partir desquels vous souhaitez que la requête extraie des informations pour éclairer sa réponse.

| Prompt | Réponse de modèle |
| --- | --- |
| Combien de jours ces couches vont-elles durer avec un bébé ? | Les couches vont durer 198 jours avant d'être épuisées. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Combien de temps vont durer ces couches avant d'être épuisées ?  Utilisez le poids indiqué sur la boîte pour déterminer l'âge de l'enfant et le nombre total de couches dans la boîte.  Divisez le nombre total par le nombre de couches utilisées par l'enfant chaque jour. | La boîte contient 198 couches. La boîte indique que les couches sont destinées à un enfant pesant entre 22 et 37 livres.  L'enfant correspondant à cette plage de poids a probablement 1 à 2 ans.  Un enfant de deux ans utilise généralement six couches par jour. Par conséquent, les couches vont durer environ 33 jours (198/6). |

#### Si les résultats du modèle sont trop génériques et ne sont pas suffisamment adaptés à l'entrée de type image

Pour aider le modèle à adapter sa réponse aux images, essayez de lui demander de les décrire avant d'effectuer sa tâche de raisonnement.

| Prompt | Réponse de modèle |
| --- | --- |
| Quel est le point commun entre ces images ? | Les quatre images sont des exemples de photographie de paysage. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Tout d'abord, décrivez en détail ce que contient chaque image. Quel est le point commun entre ces images ? | La première image montre une personne préparant une valise. La deuxième image montre un couloir vide dans un centre commercial. La troisième image montre un rouleau de papier toilette. La quatrième image montre une mer sombre et orageuse.  Le point commun de ces images est qu'elles sont toutes des exemples d'espaces liminaux. Les espaces liminaux sont des lieux ou des situations situés entre deux autres lieux ou situations. Elles se caractérisent souvent par un sentiment d'incertitude ou d'ambiguïté.  La première image montre la personne entre le moment où elle est chez elle et celui où elle est en voyage. La deuxième image montre le couloir entre deux magasins. La troisième image montre du papier toilette, ce qui peut représenter une salle de bain. Une salle de bain est un espace de transition entre les domaines privé et public. C'est un endroit où nous nous préparons à pénétrer ou à quitter le monde extérieur.  La quatrième image montre une mer entre calme et agitée.  Les espaces liminaux peuvent être à la fois intéressants et étranges. Ils peuvent constituer un début ou une fin. Ils peuvent représenter un lieu de réflexion ou d'action. |

Vous pouvez également essayer de demander explicitement au modèle de faire référence à ce qui est illustré.

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Quel est le point commun entre ces images ? Reportez-vous au contenu des images dans votre réponse. | Toutes les images sont liées au voyage. La première image montre une personne préparant une valise, la deuxième montre un couloir vide dans un centre commercial, la troisième une pile de rouleaux de papier toilette, et la quatrième image montre une mer sombre et orageuse.  Ces images sont toutes liées au voyage, car elles correspondent à tout ce dont les gens ont besoin ou utilisent lorsqu'ils voyagent. La première image montre une personne préparant une valise. C'est une chose que font les personnes qui partent en voyage. La deuxième image montre un couloir vide dans un centre commercial. C'est un lieu où les gens se rendent pour acheter les articles dont ils ont besoin pour leur voyage. La troisième image montre une pile de rouleaux de papier toilette. C'est quelque chose que les gens utilisent lorsqu'ils voyagent. La quatrième image montre une mer sombre et orageuse. C'est ce que les gens rencontrent souvent lorsqu'ils voyagent. |

Il en va de même pour les sorties créatives issues des images. Dans l'exemple suivant, avec le lapin, demandez explicitement au modèle d'inclure certains aspects de l'image pouvant améliorer le résultat.

| Prompt | Réponse de modèle |
| --- | --- |
| Peux-tu m'écrire un poème sur cette image ? | Petit lapin, si doux et marron,  Sautant à travers champ, de haut en bas.  Tes oreilles sont si longues, ta queue si petite,  tu es la créature la plus mignonne de toutes.  Tu grignotes l'herbe, si verte et douce,  et tu sautes lorsque tu me vois.  Mais je serai toujours ton ami,  Petit lapin, jusqu'à la fin. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Peux-tu m'écrire un poème descriptif et théâtral sur cette image et y inclure le lieu ? | Petit lapin sur la pelouse,  Les oreilles sont si longues, si fines.  Que vois-tu là-bas,  Au loin, là où tu regardes ?  Est-ce le bleu de l'océan,  Étincelant dans la lumière du soleil ?  Ou les vagues qui s'écrasent et rugissent,  Un rythme que tu adores ?  Petit lapin, dis-moi la vérité,  Qu'est-ce qui retient tant ton attention ?  Est-ce la brise salée,  ou les cris des mouettes qui supplient ?  Peut-être est-ce toute cette immensité,  un monde si grand et si petit à la fois.  Un lieu où les rêves peuvent vagabonder  et où les aventures peuvent être créées.  Petit lapin, je me demande à quoi à quoi tu rêves,  Quand tu es assis sur l'herbe, si serein.  As-tu envie d'explorer les profondeurs,  ou de rester sur la terre ferme, là où tu peux sauter ?  Quoi qu'il en soit, petit lapin,  Garde cette étincelle qui brille en toi. Car dans tes rêves et tes aspirations,  se trouve un monde qui n'attend que d'être créé. |

#### Savoir quelle partie de la requête a échoué

Il peut être difficile de savoir si une requête a échoué car le modèle n'a pas **compris l'image** avec laquelle commencer, ou s'il a compris l'image, mais n'a pas effectué les bonnes **étapes de raisonnement**.
Pour faire la distinction entre les deux, demandez au modèle de décrire le contenu de l'image.

Dans l'exemple suivant, si le modèle répond avec un aliment qui ne semble pas correspondre au thé (par exemple, du pop-corn), vous pouvez d'abord chercher à déterminer si le modèle a correctement reconnu que l'image contient du thé.

| Prompt | Requête pour le dépannage |
| --- | --- |
| Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? | Décris ce que tu vois sur cette image. |

Une autre stratégie consiste à demander au modèle d'expliquer son raisonnement. Cela peut vous aider à déterminer la partie du raisonnement qui a échoué, le cas échéant.

| Prompt | Requête pour le dépannage |
| --- | --- |
| Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? | Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? Merci d'indiquer pour quelle raison. |

## Étape suivante

- Essayez d'écrire vos propres prompts multimodaux à l'aide de [Google AI Studio](http://aistudio.google.com?hl=fr).
- Pour en savoir plus sur l'utilisation de l'API Gemini Files pour importer des fichiers multimédias et les inclure dans vos requêtes, consultez les guides [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=fr), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr) et [Traitement des documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).
- Pour obtenir d'autres conseils sur la conception de requêtes, comme l'ajustement des paramètres d'échantillonnage, consultez la page [Stratégies de requête](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/14 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/14 (UTC)."],[],[]]
