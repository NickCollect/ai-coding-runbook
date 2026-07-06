---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr
fetched_at: 2026-07-06T05:20:07.777734+00:00
title: "M\u00e9thodes de saisie de fichiers \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Méthodes de saisie de fichiers

Ce guide explique les différentes manières d'inclure des fichiers multimédias tels que des images, des fichiers audio, des vidéos et des documents lorsque vous envoyez des requêtes à l'API Gemini.
Les nouvelles méthodes sont compatibles avec tous les points de terminaison de l'API Gemini, y compris les API Batch, Interactions et Live.
Le choix de la méthode appropriée dépend de la taille de votre fichier, de l'emplacement où vos données sont stockées et de la fréquence à laquelle vous prévoyez d'utiliser le fichier.

Le moyen le plus simple d'inclure un fichier comme entrée consiste à lire un fichier local et à l'inclure dans une requête. L'exemple suivant montre comment lire un fichier PDF local. Les fichiers PDF sont limités à 50 Mo pour cette méthode. Consultez le
[tableau comparatif des méthodes d'entrée](#method-comparison) pour obtenir la liste complète des types d'entrée de fichier
et des limites.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## Comparaison des méthodes d'entrée

Le tableau suivant compare chaque méthode d'entrée avec les limites de fichiers et les cas d'utilisation les plus adaptés. Notez que la limite de taille des fichiers peut varier en fonction du type de fichier et du modèle ou du tokenizer utilisé pour traiter le fichier.

| Méthode | Application idéale | Taille maximale du fichier | Persistance |
| --- | --- | --- | --- |
| **Données intégrées** | Tests rapides, petits fichiers, applications en temps réel. | 100 Mo par requête ou charge utile   (**50 Mo pour les fichiers PDF**) | Aucune (envoyée avec chaque requête) |
| **Importation de fichiers via l'API** | Fichiers volumineux, fichiers utilisés plusieurs fois. | 2 Go par fichier,   jusqu'à 20 Go par projet | 48 heures |
| **Enregistrement d'URI GCS via l'API Files** | Fichiers volumineux déjà présents dans Google Cloud Storage, fichiers utilisés plusieurs fois. | 2 Go par fichier, aucune limite de stockage globale | Aucune (récupérée par requête). L'enregistrement unique peut donner accès jusqu'à 30 jours. |
| **URL externes** | Données publiques ou données dans des buckets cloud (AWS, Azure, GCS) sans avoir à les importer à nouveau. | 100 Mo par requête/charge utile | Aucune (récupérée par requête) |

## Données intégrées

Pour les fichiers plus petits (moins de 100 Mo ou 50 Mo pour les fichiers PDF), vous pouvez transmettre les données directement dans la charge utile de la requête. Il s'agit de la méthode la plus simple pour les tests rapides ou les applications qui gèrent des données transitoires en temps réel. Vous pouvez fournir des données sous forme de chaînes encodées en base64 ou en lisant directement des fichiers locaux.

Pour obtenir un exemple de lecture à partir d'un fichier local, consultez l'exemple au début de cette page.

### Récupérer à partir d'une URL

Vous pouvez également récupérer un fichier à partir d'une URL, le convertir en octets et l'inclure dans l'entrée.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.5-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## API Gemini Files

L'API Files est conçue pour les fichiers plus volumineux (jusqu'à 2 Go) ou les fichiers que vous prévoyez d'utiliser dans plusieurs requêtes.

### Importation de fichiers standard

Importez un fichier local dans l'API Gemini. Les fichiers importés de cette manière sont stockés temporairement (48 heures) et traités pour être récupérés efficacement par le modèle.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Enregistrer des fichiers Google Cloud Storage

Si vos données se trouvent déjà dans Google Cloud Storage, vous n'avez pas besoin de les télécharger ni de les importer à nouveau. Vous pouvez les enregistrer directement avec l'API Files.

1. Accorder l'accès à l'**agent de service** à chaque bucket

   1. Activez l'API Gemini dans votre projet Google Cloud.
   2. Créez l'agent de service :

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Accordez à l'agent de service de l'API Gemini les autorisations** nécessaires pour lire vos buckets de stockage.

      L'utilisateur doit attribuer le `Storage Object Viewer`
      [rôle IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=fr#storage.objectViewer)
      à cet agent de service sur les buckets de stockage spécifiques qu'il prévoit d'utiliser.

   Cet accès n'expire pas par défaut, mais peut être modifié à tout moment. Vous pouvez
   également utiliser les
   [commandes du SDK IAM Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=fr)
   pour accorder des autorisations.
2. Authentifier votre service

   **Prérequis**

   - Activer l'API
   - Créez un compte de service ou un agent avec les autorisations appropriées.

   Vous devez d'abord vous authentifier en tant que service disposant des autorisations de lecteur d'objets de stockage. La manière dont cela se produit dépend de l'environnement dans lequel votre code de gestion des fichiers s'exécutera.

   **En dehors de Google Cloud**

   Si votre code s'exécute en dehors de Google Cloud, par exemple sur votre ordinateur, téléchargez les identifiants du compte à partir de la console Google Cloud en procédant comme suit :

   1. Accédez à la console [Comptes de service](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=fr).
   2. Sélectionnez le compte de service concerné.
   3. Sélectionnez l'onglet **Clés, puis **Ajouter une clé** > Créer une clé**.
   4. Choisissez le type de clé **JSON** et notez l'emplacement où le fichier a été téléchargé sur votre ordinateur.

   Pour en savoir plus, consultez la documentation officielle de Google Cloud sur
   [la gestion des clés de compte de service](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=fr).

   Utilisez ensuite les commandes suivantes pour vous authentifier. Ces commandes supposent que votre fichier de compte de service se trouve dans le répertoire actuel et qu'il est nommé `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### Javascript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Sur Google Cloud**

   Si vous exécutez directement dans Google Cloud, par exemple à l'aide de [fonctions Cloud Run](https://cloud.google.com/functions?hl=fr) ou d'une [instance Compute Engine](https://cloud.google.com/products/compute?hl=fr), vous disposerez d'identifiants implicites, mais vous devrez vous réauthentifier pour accorder les champs d'application appropriés.

   ### Python

   Ce code s'attend à ce que le service s'exécute dans un environnement où
   [les identifiants par défaut de l'application](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=fr)
   peuvent être obtenus automatiquement, comme Cloud Run ou Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Ce code s'attend à ce que le service s'exécute dans un environnement où
   [les identifiants par défaut de l'application](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=fr)
   peuvent être obtenus automatiquement, comme Cloud Run ou Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   Il s'agit d'une commande interactive. Pour les services tels que Compute Engine, vous pouvez associer des champs d'application au service en cours d'exécution au niveau de la configuration. [Pour obtenir un exemple, consultez la documentation sur les services gérés par l'utilisateur.](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=fr#using)

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Enregistrement de fichiers (API Files)

   Utilisez l'API Files pour enregistrer des fichiers et générer un chemin d'accès à l'API Files qui peut être utilisé directement dans l'API Gemini.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.5-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.5-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## URL HTTP externes / signées

Vous pouvez transmettre directement des URL HTTPS accessibles au public ou des URL pré-signées dans votre requête. L'API Gemini récupérera le contenu de manière sécurisée lors du traitement.
Cette méthode est idéale pour les fichiers de moins de 100 Mo que vous ne souhaitez pas importer à nouveau.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.5-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### Accessibilité

Vérifiez que les URL que vous fournissez ne mènent pas à des pages qui nécessitent des identifiants de connexion ou qui sont soumises à un paywall. Pour les bases de données privées, assurez-vous de créer une URL signée avec les autorisations d'accès et la date d'expiration appropriées.

### Vérifications de sécurité

Le système effectue une vérification de modération du contenu sur l'URL pour s'assurer qu'elle respecte les normes de sécurité et les règles. Si l'URL échoue à cette vérification, vous recevrez un `url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Types de contenu compatibles

Cette liste des types de fichiers et des limites compatibles est fournie à titre indicatif et n'est pas exhaustive. L'ensemble effectif des types compatibles est susceptible d'être modifié et peut varier en fonction du modèle spécifique et de la version du tokenizer utilisés. Les types non compatibles entraîneront une erreur.
De plus, la récupération de contenu pour ces types de fichiers n'est compatible qu'avec les URL accessibles au public.

#### Types de fichiers texte

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Types de fichiers d'application

- `application/json`
- `application/pdf`

#### Types de fichiers image

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Types de fichiers vidéo

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Bonnes pratiques

- **Choisissez la bonne méthode** : utilisez des données intégrées pour les petits fichiers transitoires.
  Utilisez l'API Files pour les fichiers plus volumineux ou fréquemment utilisés. Utilisez des URL externes pour les données déjà hébergées en ligne.
- **Spécifiez les types MIME** : fournissez toujours le type MIME correct pour les données de fichier afin de garantir un traitement approprié.
- **Gérez les erreurs** : implémentez la gestion des erreurs dans votre code pour gérer les problèmes potentiels tels que les pannes de réseau, les problèmes d'accès aux fichiers ou les erreurs d'API.

## Limites

- Les limites de taille des fichiers varient en fonction de la méthode (voir le [tableau comparatif](#method-comparison))
  et du type de fichier.
- Les données intégrées augmentent la taille de la charge utile de la requête.
- Les importations de fichiers via l'API sont temporaires et expirent au bout de 48 heures.
- La récupération d'URL externes est limitée à 100 Mo par charge utile et est compatible avec des types de contenu spécifiques.

## Étape suivante

- Essayez d'écrire vos propres requêtes multimodales à l'aide de
  [Google AI Studio](http://aistudio.google.com/?hl=fr).
- Pour savoir comment inclure des fichiers dans vos requêtes, consultez les
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=fr),
  [de l'audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr)et des
  [documents](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
