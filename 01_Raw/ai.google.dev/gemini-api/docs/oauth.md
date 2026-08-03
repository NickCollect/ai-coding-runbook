---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=fr
fetched_at: 2026-08-03T04:40:28.276068+00:00
title: "Guide de d\u00e9marrage\u00a0rapide de l'authentification avec OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Guide de démarrage rapide de l'authentification avec OAuth

Le moyen le plus simple de s'authentifier auprès de l'API Gemini consiste à configurer une clé API, comme décrit dans le [guide de démarrage de l'API Gemini](https://ai.google.dev/gemini-api/docs/get-started?hl=fr). Si vous avez besoin de contrôles d'accès plus stricts, vous pouvez utiliser OAuth à la place. Ce guide vous aidera à configurer l'authentification avec OAuth.

Ce guide utilise une approche d'authentification simplifiée qui convient à un environnement de test. Pour un environnement de production, renseignez-vous sur l'[authentification et l'autorisation](https://developers.google.com/workspace/guides/auth-overview?hl=fr) avant de [choisir les identifiants d'accès](https://developers.google.com/workspace/guides/create-credentials?hl=fr#choose_the_access_credential_that_is_right_for_you) qui conviennent à votre application.

## Objectifs

- Configurer votre projet cloud pour OAuth
- Configurer les identifiants par défaut de l'application
- Gérer les identifiants dans votre programme au lieu d'utiliser `gcloud auth`

## Prérequis

Pour exécuter ce guide de démarrage rapide, vous avez besoin des éléments suivants :

- [Un projet Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=fr)
- [Installation locale de la gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=fr)

## Configurer votre projet Cloud

Pour suivre ce guide de démarrage rapide, vous devez d'abord configurer votre projet Cloud.

### 1. Activer l'API

Avant d'utiliser les API Google, vous devez les activer dans un projet Google Cloud.

- Dans la console Google Cloud, activez l'API Generative Language de Google.

  [Activer l'API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=fr)

### 2. Configurer l'écran d'autorisation OAuth

Ensuite, configurez l'écran de consentement OAuth du projet et ajoutez-vous en tant qu'utilisateur test. Si vous avez déjà effectué cette étape pour votre projet Cloud, passez à la section suivante.

1. Dans la console Google Cloud, accédez à **Menu** > **Plate-forme Google Auth** > **Présentation**.

   [Accéder à la plate-forme Google Auth](https://console.developers.google.com/auth/overview?hl=fr)
2. Remplissez le formulaire de configuration du projet et définissez le type d'utilisateur sur **Externe** dans la section **Audience**.
3. Remplissez le reste du formulaire, acceptez les conditions du règlement sur les données utilisateur, puis cliquez sur **Créer**.
4. Pour l'instant, vous pouvez ignorer l'ajout de niveaux d'accès et cliquer sur **Enregistrer et continuer**. À l'avenir, lorsque vous créerez une application à utiliser en dehors de votre organisation Google Workspace, vous devrez ajouter et valider les niveaux d'autorisation requis par votre application.
5. Ajoutez des utilisateurs de test :

   1. Accédez à la [page "Audience"](https://console.developers.google.com/auth/audience?hl=fr) de la plate-forme Google Auth.
   2. Sous **Utilisateurs de test**, cliquez sur **Ajouter des utilisateurs**.
   3. Saisissez votre adresse e-mail et celles des autres utilisateurs de test autorisés, puis cliquez sur **Enregistrer**.

### 3. Autoriser les identifiants pour une application de bureau

Pour vous authentifier en tant qu'utilisateur final et accéder aux données utilisateur dans votre application, vous devez créer un ou plusieurs ID client OAuth 2.0. Un ID client sert à identifier une application unique auprès des serveurs OAuth de Google. Si votre application s'exécute sur plusieurs plates-formes, vous devez créer un ID client distinct pour chacune d'elles.

1. Dans la console Google Cloud, accédez à **Menu** > **Plate-forme Google Auth** > **Clients**.

   [Accéder à "Identifiants"](https://console.developers.google.com/auth/clients?hl=fr)
2. Cliquez sur **Créer un client**.
3. Cliquez sur **Type d'application** > **Application de bureau**.
4. Dans le champ **Nom**, saisissez un nom pour l'identifiant. Ce nom n'apparaît que dans la console Google Cloud.
5. Cliquez sur **Créer**. L'écran "Client OAuth créé" s'affiche, indiquant votre nouvel ID client et votre nouveau code secret de client.
6. Cliquez sur **OK**. Les identifiants que vous venez de créer s'affichent sous **ID client OAuth 2.0**.
7. Cliquez sur le bouton de téléchargement pour enregistrer le fichier JSON. Il sera enregistré sous le nom `client_secret_<identifier>.json`. Renommez-le `client_secret.json` et déplacez-le dans votre répertoire de travail.

## Configurer les identifiants par défaut de l'application

Pour convertir le fichier `client_secret.json` en identifiants utilisables, transmettez son emplacement à l'argument `--client-id-file` de la commande `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

La configuration simplifiée du projet dans ce tutoriel déclenche une boîte de dialogue **Google n'a pas validé cette application**. C'est normal. Sélectionnez **Continuer**.

Le jeton obtenu est placé dans un emplacement connu afin qu'il puisse être accessible par `gcloud` ou les bibliothèques clientes.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Une fois que vous avez défini les identifiants par défaut de l'application (ADC), les bibliothèques clientes dans la plupart des langages ont besoin d'une aide minimale, voire aucune, pour les trouver.

### Curl

Le moyen le plus rapide de vérifier que cela fonctionne consiste à l'utiliser pour accéder à l'API REST à l'aide de curl :

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

En Python, les bibliothèques clientes devraient les trouver automatiquement :

```
pip install google-genai
```

Voici un script minimal pour le tester :

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Étapes suivantes

Si cela fonctionne, vous pouvez essayer la [récupération sémantique sur vos données textuelles](https://ai.google.dev/docs/semantic_retriever?hl=fr).

## Gérer vous-même les identifiants [Python]

Dans de nombreux cas, vous ne disposerez pas de la commande `gcloud` pour créer le jeton d'accès à partir de l'ID client (`client_secret.json`). Google fournit des bibliothèques dans de nombreux langages pour vous permettre de gérer ce processus dans votre application. Cette section illustre le processus en Python. Des exemples équivalents de ce type de procédure sont disponibles pour d'autres langages dans la [documentation de l'API Drive](https://developers.google.com/drive/api/quickstart/python?hl=fr).

### 1. Installer les bibliothèques nécessaires

Installez la bibliothèque cliente Google pour Python et la bibliothèque cliente Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Écrire le gestionnaire d'identifiants

Pour minimiser le nombre de clics nécessaires pour parcourir les écrans d'autorisation, créez un fichier appelé `load_creds.py` dans votre répertoire de travail pour mettre en cache un fichier `token.json` qu'il pourra réutiliser ultérieurement ou actualiser s'il expire.

Commencez par le code suivant pour convertir le fichier `client_secret.json` en jeton utilisable avec `genai.configure` :

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Écrire votre programme

Créez maintenant votre `script.py` :

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Exécuter votre programme

Dans votre répertoire de travail, exécutez l'exemple :

```
python script.py
```

La première fois que vous exécutez le script, il ouvre une fenêtre de navigateur et vous invite à autoriser l'accès.

1. Si vous n'êtes pas encore connecté à votre compte Google, vous êtes invité à le faire. Si vous êtes connecté à plusieurs comptes, **assurez-vous de sélectionner celui que vous avez défini comme "Compte de test" lors de la configuration de votre projet**.
2. Les informations d'autorisation sont stockées dans le système de fichiers. La prochaine fois que vous exécuterez l'exemple de code, vous ne serez pas invité à fournir une autorisation.

Vous avez configuré l'authentification.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/01 (UTC)."],[],[]]
