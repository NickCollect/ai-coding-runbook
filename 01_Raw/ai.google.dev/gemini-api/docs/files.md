---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=fr
fetched_at: 2026-05-11T05:05:45.225185+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Files

Gemini peut traiter simultanément différents types de données d'entrée, y compris du texte, des images et de l'audio.

Ce guide vous explique comment utiliser des fichiers multimédias avec l'API Files. Les opérations de base sont les mêmes pour les fichiers audio, les images, les vidéos, les documents et les autres types de fichiers compatibles.

Pour obtenir des conseils sur les prompts de fichiers, consultez la section [Guide sur les prompts de fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide).

## Importer un fichier

Vous pouvez utiliser l'API Files pour importer un fichier multimédia. Utilisez toujours l'API Files lorsque la taille totale de la requête (y compris les fichiers, l'invite de texte, les instructions système, etc.) est supérieure à 100 Mo. Pour les fichiers PDF, la limite est de 50 Mo.

Le code suivant importe un fichier, puis l'utilise dans un appel à `generateContent`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

resp, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", []*genai.Content{
  {
    Parts: []*genai.Part{
      genai.NewPartFromFile(*file),
      genai.NewPartFromText("Describe this audio clip"),
    },
  },
}, nil)

if err != nil {
    log.Fatal(err)
}

printResponse(resp)
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

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
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

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await ai.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
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

const ai = new GoogleGenAI({});

async function main() {
  const listResponse = await ai.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
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

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await ai.files.delete({ name: fileName });
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Infos sur l'utilisation

Vous pouvez utiliser l'API Files pour importer des fichiers multimédias et interagir avec eux. L'API Files vous permet de stocker jusqu'à 20 Go de fichiers par projet, avec une taille maximale de 2 Go par fichier. Les fichiers sont stockés pendant 48 heures. Pendant cette période, vous pouvez utiliser l'API pour obtenir des métadonnées sur les fichiers, mais vous ne pouvez pas les télécharger.
L'API Files est disponible sans frais dans toutes les régions où l'API Gemini est disponible.

## Stratégies de requête pour les fichiers

Cette section fournit des conseils et des bonnes pratiques pour utiliser des fichiers multimédias avec des requêtes pour l'API Gemini.

La possibilité d'utiliser différents types de données dans vos requêtes vous offre plus de flexibilité quant aux tâches que vous pouvez effectuer avec l'API Gemini. Par exemple, vous pouvez envoyer au modèle la photo d'un délicieux repas et lui demander d'écrire un court article de blog à ce sujet.

|  |  |
| --- | --- |
| **Prompt** (Requête) | **Réponse** |
| Rédigez un article de blog court et attrayant basé sur cette photo. Il doit inclure une description du repas sur la photo et parler de ma méthode de préparation de repas.   Cookies | Préparer ses repas est un excellent moyen de gagner du temps et de l'argent, et cela peut aussi vous aider à manger plus sainement. Ce repas est un excellent exemple de plat sain et délicieux qui peut être facilement préparé à l'avance.  Ce plat se compose de riz brun, de légumes rôtis et de poulet teriyaki. Le riz brun est un glucide complexe et sain qui vous apportera une énergie durable. Les légumes rôtis sont un excellent moyen d'obtenir votre dose quotidienne de vitamines et de minéraux, et le poulet teriyaki est une option délicieuse et riche en protéines.  Ce plat est également très facile à préparer. Il vous suffit de cuire le riz complet, de rôtir les légumes et de cuire le poulet teriyaki. Une fois que tout est cuit, divisez-le en récipients pour la préparation des repas et conservez-les au réfrigérateur. Vous pouvez ensuite prendre un récipient et partir les matins chargés !  Si vous recherchez un repas sain et délicieux qui peut être facilement préparé à l'avance, cette recette est une excellente option. Il est riche en nutriments et en saveurs, et vous rassasiera à coup sûr.  À la préparation de repas sains et délicieux ! |

Si vous ne parvenez pas à obtenir le résultat souhaité à partir de requêtes utilisant des fichiers multimédias, voici quelques stratégies qui peuvent vous aider. Les sections suivantes fournissent des approches de conception et des conseils de dépannage pour améliorer les requêtes qui utilisent des entrées multimodales.

Vous pouvez améliorer vos requêtes multimodales en suivant ces bonnes pratiques :

- ### [Principes de base de la conception d'invites](#specific-instructions)

  - **Soyez précis dans vos instructions** : définissez des instructions claires et concises qui laissent peu de place aux erreurs d'interprétation.
  - **Ajoutez quelques exemples à votre requête** :utilisez des exemples réalistes pour illustrer votre objectif.
  - **Décomposez la tâche étape par étape** : divisez les tâches complexes en sous-objectifs gérables pour guider le modèle tout au long du processus.
  - **Spécifiez le format de sortie** : dans votre requête, demandez la sortie au format souhaité, tel que Markdown, JSON, HTML, etc.
  - **Mettez en avant votre image pour les requêtes liées à une seule image** : bien que Gemini puisse gérer les entrées d'image et de texte dans n'importe quel ordre, les requêtes qui contiennent une seule image peuvent fonctionner mieux si cette image (ou vidéo) est placée avant la requête de texte. Toutefois, pour les requêtes qui nécessitent que les images soient fortement imbriquées avec le texte pour avoir du sens, utilisez l'ordre le plus naturel.
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

Dans l'exemple ci-dessous, le résultat initial est rédigé sous forme de phrase et contient également le pays (Brésil). Supposons que vous souhaitiez obtenir le résultat dans un autre format ou style, et que vous ne vouliez que la ville, et non le pays. En ajoutant des exemples few-shot à votre requête, vous pouvez orienter le modèle pour qu'il réponde comme vous le souhaitez.

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

| Requête | Réponse de modèle |
| --- | --- |
| Quand vais-je manquer de papier toilette ? | Bientôt, car il ne vous reste que trois rouleaux. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| 1. Commencez par compter le nombre de rouleaux de papier toilette apparaissant sur cette photo.  2. Déterminez ensuite la quantité de papier toilette qu'une personne type utilise par jour.  3. Calculez la durée de vie de ces rouleaux de papier toilette. | 1. Sur cette photo, on voit trois rouleaux de papier toilette.  2. Une personne type utilise environ 20 feuilles de papier toilette par jour.  3. Si un rouleau contient 200 feuilles, chaque rouleau dure environ 10 jours. Par conséquent, les trois rouleaux dureront environ un mois. |

Les problèmes mathématiques ou les problèmes basés sur les mots sont d'excellents candidats pour demander au modèle de réfléchir étape par étape.

| **Prompt** (Requête) | **Response** (Réponse) |
| --- | --- |
| Quel est le quatrième terme de la séquence ? | -135 |

La réponse du modèle est incorrecte. Pour améliorer cela, vous pouvez demander au modèle d'analyser le problème avant de répondre à la requête.

| **Prompt** (Requête) | **Response** (Réponse) |
| --- | --- |
| Commencez par analyser la formule dans l'image.  Ensuite, en fonction de la formule, répondez à la question "Quel est le quatrième terme de la séquence ?". | *Cliquez pour développer le résultat* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Remplacez "n = 4" dans la formule :  $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Nous ne connaissons pas la valeur de b(3). Remplacez donc n = 3 dans la formule :  $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Nous ne connaissons pas la valeur de b(2). Remplacez donc n = 2 dans la formule :  $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Nous savons que la valeur de b(1) est 15. Remplacez-la par la formule :  $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Maintenant que nous connaissons la valeur de b(2), remplacez-la dans la formule de b(3) :  $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Maintenant que nous connaissons la valeur de b(3), remplacez-la dans la formule de b(4) :  $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Par conséquent, le quatrième terme de la séquence est -405. |

La réponse de ce modèle est correcte. Pour la rendre encore plus simple, vous pouvez lui demander de réfléchir par étapes.

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Quel est le quatrième terme de la séquence ? Réfléchir étape par étape | Le premier terme est 15.  Le deuxième terme est b(1) \* (-3) = 15 \* (-3) = -45.  Le troisième terme est b(2) \* (-3) = -45 \* (-3) = 135.  Le quatrième terme est b(3) \* (-3) = 135 \* (-3) = -405. |

### Spécifier le format de sortie

Un problème courant est le besoin d'avoir un format spécifique pour la sortie du modèle (par exemple, Markdown, JSON, HTML), en particulier si celle-ci doit être ingérée par une tâche en aval. Vous pouvez essayer de produire un résultat dans ce format en demandant au modèle via la requête. Vous trouverez deux exemples ci-dessous :

| Requête | Réponse de modèle |
| --- | --- |
| Analysez le tableau de cette image au format Markdown | | Sujet | État | Heure | Date de début | Date limite |  | ------- | ------ | ---- | ---------- | ------ |  | Math | Done | 1.5 hrs | 11/29/2023 | 12/1/2023 |  | Géographie | Terminé | 30 min | 02/12/2023 | 04/12/2023 |  | Physique | En cours | 2 h | 03/12/2023 | 05/12/2023 |  | Biologie | Non commencé | 6 h | 02/11/2016 | 06/12/2023 | |

| **Prompt** (Requête) | **Réponse de modèle** |
| --- | --- |
| Fournissez la liste de tous les attributs suivants :  ingrédients, type de cuisine, végétarien ou non, au format JSON | ```` ```json ````  `{`  `"ingredients": [`  `"rice",`  `"shrimp",`  `"clams",`  `"mussels",`  `"peas",`  `"tomatoes",`  `"onions",`  `"garlic",`  `"olive oil",`  `"paprika",`  `"salt",`  `"pepper"`  `],`  `"type of cuisine": "Spanish",`  `"vegetarian": false`  `}`  ```` ``` ```` |

### Utilisez votre image en premier pour les requêtes liées à une seule image

Bien que Gemini puisse interpréter l'image et le texte dans n'importe quel ordre dans une requête, le fait de placer une seule image avant la requête de texte peut offrir de meilleurs résultats.
Dans les exemples suivants, vous remarquerez que l'image précède le texte dans chaque requête.

### Résoudre les problèmes liés à un prompt multimodal

Si vous n'obtenez pas de réponse utile, vous devrez peut-être résoudre les problèmes liés à votre requête. Voici quelques stratégies que vous pouvez essayer.

#### Si le modèle n'extrait pas d'informations de la partie pertinente de l'image

Pour obtenir une réponse plus spécifique, vous pouvez indiquer les aspects de l'image à partir desquels vous souhaitez que la requête extraie des informations pour éclairer sa réponse.

| Prompt | Réponse de modèle |
| --- | --- |
| Combien de jours ces couches vont-elles durer avec un bébé ? | Les couches vont durer 198 jours avant d'être épuisées. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Combien de temps vont durer ces couches avant d'être épuisées ?  Utilisez le poids indiqué sur la boîte pour déterminer l'âge de l'enfant et le nombre total de couches dans la boîte.  Divisez le nombre total par le nombre de couches utilisées par l'enfant chaque jour. | La boîte contient 198 couches. La boîte indique que les couches sont destinées à un enfant pesant entre 22 et 37 livres.  L'enfant correspondant à cette plage de poids a probablement 1 à 2 ans.  Un enfant de deux ans utilise généralement six couches par jour. Par conséquent, les couches vont durer environ 33 jours (198/6). |

#### Si les résultats du modèle sont trop génériques et ne sont pas suffisamment adaptés à l'entrée de type image

Pour aider le modèle à adapter sa réponse à l'image ou aux images, essayez de lui demander de les décrire avant d'effectuer sa tâche de raisonnement.

| Prompt | Réponse de modèle |
| --- | --- |
| Quel est le point commun entre ces images ? | Les quatre images sont des exemples de photographie de paysage. |

| **Prompt modifié** | **Réponse améliorée** |
| --- | --- |
| Commencez par décrire en détail le contenu de chaque image. Quel est le point commun entre ces images ? | La première image montre une personne préparant une valise. La deuxième image montre un couloir vide dans un centre commercial. La troisième image montre un rouleau de papier toilette. La quatrième image montre une mer sombre et orageuse.  Le point commun de ces images est qu'elles sont toutes des exemples d'espaces liminaux. Les espaces liminaux sont des lieux ou des situations situés entre deux autres lieux ou situations. Elles sont souvent caractérisées par un sentiment d'incertitude ou d'ambiguïté.  La première image montre une personne entre chez elle et en voyage. La deuxième image montre le couloir entre deux magasins. La troisième image montre du papier toilette, ce qui peut représenter une salle de bain. Une salle de bain est un espace de transition entre les domaines privé et public. C'est un endroit où nous nous préparons à pénétrer ou à quitter le monde extérieur.  La quatrième image montre une mer calme et orageuse.  Les espaces liminaux peuvent être à la fois intéressants et étranges. Ils peuvent constituer un début ou une fin. Ils peuvent représenter un lieu de réflexion ou d'action. |

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
| Peux-tu m'écrire un poème descriptif et théâtral sur cette image et y inclure le lieu ? | Petit lapin sur la pelouse,  Les oreilles sont si longues, si fines.  Que vois-tu là-bas,  Au loin, là où tu regardes ?  Est-ce le bleu de l'océan,  Étincelant dans la lumière du soleil ?  Ou les vagues qui s'écrasent et rugissent,  Un rythme que tu adores ?  Petit lapin, dis-moi la vérité,  Qu'est-ce qui retient tant ton attention ?  Est-ce la brise salée,  ou les cris des mouettes qui supplient ?  Peut-être est-ce toute cette immensité,  un monde si grand et si petit à la fois.  Un lieu où les rêves peuvent vagabonder  et où les aventures peuvent être créées.  Petit lapin, je me demande à quoi à quoi tu rêves,  Quand tu es assis sur l'herbe, si serein.  As-tu envie d'explorer les profondeurs,  ou de rester sur la terre ferme, là où tu peux sauter ?  Quoi qu'il en soit, petit lapin,  Garde cette étincelle qui brille en toi. Car dans tes rêves et tes aspirations,  se trouve un monde qui n'attend que d'être créé. |

#### Savoir quelle partie de la requête a échoué

Il peut être difficile de savoir si une requête a échoué car le modèle n'a pas **compris l'image** avec laquelle commencer, ou s'il a compris l'image, mais n'a pas effectué les bonnes **étapes de raisonnement**.
Pour faire la distinction entre les deux, demandez au modèle de décrire le contenu de l'image.

Dans l'exemple suivant, si le modèle répond avec un aliment qui ne semble pas correspondre au thé (par exemple, du pop-corn), vous pouvez d'abord chercher à déterminer si le modèle a correctement reconnu que l'image contient du thé.

| Prompt | Requête pour le dépannage |
| --- | --- |
| Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? | Décris ce que représente cette image. |

Une autre stratégie consiste à demander au modèle d'expliquer son raisonnement. Cela peut vous aider à déterminer la partie du raisonnement qui a échoué, le cas échéant.

| Prompt | Requête pour le dépannage |
| --- | --- |
| Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? | Quel aliment puis-je préparer en une minute qui pourrait être associé à cela ? Merci d'indiquer pour quelle raison. |

## Étape suivante

- Essayez d'écrire vos propres requêtes multimodales à l'aide de [Google AI Studio](http://aistudio.google.com?hl=fr).
- Pour savoir comment utiliser l'API Gemini Files pour importer des fichiers multimédias et les inclure dans vos requêtes, consultez les guides [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=fr), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr) et [Traitement de documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).
- Pour obtenir d'autres conseils sur la conception de requêtes, comme le réglage des paramètres d'échantillonnage, consultez la page [Stratégies de requête](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/07 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/07 (UTC)."],[],[]]
