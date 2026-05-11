---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=fr
fetched_at: 2026-05-11T05:05:36.544023+00:00
title: "Utiliser des cl\u00e9s API Gemini \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Utiliser des clés API Gemini

Pour utiliser l'API Gemini, vous avez besoin d'une clé API. Cette page explique comment créer et gérer vos clés dans Google AI Studio, et comment configurer votre environnement pour les utiliser dans votre code.

[Créer ou afficher une clé API Gemini](https://aistudio.google.com/app/apikey?hl=fr)

## Clés API

Vous pouvez créer et gérer toutes vos clés API Gemini sur la page [Clés API](https://aistudio.google.com/app/apikey?hl=fr) de **Google AI Studio**.

Une fois que vous disposez d'une clé API, vous avez les options suivantes pour vous connecter à l'API Gemini :

- [Définir votre clé API comme variable d'environnement](#set-api-env-var)
- [Fournir explicitement votre clé API](#provide-api-key-explicitly)

Pour les tests initiaux, vous pouvez coder en dur une clé API, mais cela ne doit être que temporaire, car ce n'est pas sécurisé. Vous trouverez des exemples d'intégration en dur de la clé API dans la section [Fournir explicitement la clé API](#provide-api-key-explicitly).

## Projets Google Cloud

Les [projets Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=fr) sont essentiels pour utiliser les services Google Cloud (tels que l'API Gemini), gérer la facturation et contrôler les collaborateurs et les autorisations. Google AI Studio fournit une interface légère pour vos projets Google Cloud.

Si vous n'avez pas encore créé de projets, vous devez en créer un ou en importer un depuis Google Cloud dans Google AI Studio. La page **Projets** de Google AI Studio affiche toutes les clés disposant des autorisations suffisantes pour utiliser l'API Gemini. Pour obtenir des instructions, consultez la section [Importer des projets](#import-projects).

### Projet par défaut

Pour les nouveaux utilisateurs, Google AI Studio crée un projet Google Cloud et une clé API par défaut après l'acceptation des conditions d'utilisation, pour faciliter l'utilisation. Vous pouvez renommer ce projet dans Google AI Studio en accédant à la vue **Projets** du **tableau de bord**, en cliquant sur le bouton des paramètres à trois points à côté d'un projet et en sélectionnant **Renommer le projet**. Aucun projet par défaut ne sera créé pour les utilisateurs existants ou ceux qui possèdent déjà des comptes Google Cloud.

## Importer des projets

Chaque clé API Gemini est associée à un projet Google Cloud. Par défaut, Google AI Studio n'affiche pas tous vos projets Cloud. Vous devez importer les projets souhaités en recherchant leur nom ou leur ID dans la boîte de dialogue **Importer des projets**. Pour afficher la liste complète des projets auxquels vous avez accès, consultez la console Cloud.

Si vous n'avez pas encore importé de projets, suivez ces étapes pour importer un projet Google Cloud et créer une clé :

1. Accédez à [Google AI Studio](https://aistudio.google.com?hl=fr).
2. Ouvrez le **tableau de bord** dans le panneau latéral de gauche.
3. Sélectionnez **Projets**.
4. Sélectionnez le bouton **Importer des projets** sur la page **Projets**.
5. Recherchez et sélectionnez le projet Google Cloud que vous souhaitez importer, puis cliquez sur le bouton **Importer**.

Une fois le projet importé, accédez à la page **Clés API** depuis le menu **Tableau de bord** et créez une clé API dans le projet que vous venez d'importer.

## Limites

Voici les limites liées à la gestion des clés API et des projets Google Cloud dans Google AI Studio.

- Vous pouvez créer jusqu'à 10 projets à la fois sur la page **Projets** de Google AI Studio.
- Vous pouvez nommer et renommer des projets et des clés.
- Les pages **Clés API** et **Projets** affichent un maximum de 100 clés et 50 projets.
- Seules les clés API sans restriction ou limitées à l'API Generative Language s'affichent.

Pour bénéficier d'un accès supplémentaire à la gestion de vos projets, y compris pour modifier et restreindre les clés API, accédez à la [page des identifiants de la console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=fr).
Dans la console Cloud, vous pouvez sélectionner votre projet, cliquer sur une clé API existante, puis la limiter à l'**API Generative Language**.

## Définir la clé API comme variable d'environnement

Si vous définissez la variable d'environnement `GEMINI_API_KEY` ou `GOOGLE_API_KEY`, la clé API sera automatiquement récupérée par le client lors de l'utilisation de l'une des [bibliothèques de l'API Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=fr). Il est recommandé de ne définir qu'une seule de ces variables, mais si les deux sont définies, `GOOGLE_API_KEY` est prioritaire.

Si vous utilisez l'API REST ou JavaScript sur le navigateur, vous devrez fournir la clé API de manière explicite.

Voici comment définir votre clé API localement en tant que variable d'environnement `GEMINI_API_KEY` avec différents systèmes d'exploitation.

### Linux/macOS : Bash

Bash est une configuration de terminal Linux et macOS courante. Pour vérifier si vous disposez d'un fichier de configuration, exécutez la commande suivante :

```
~/.bashrc
```

Si la réponse est "No such file or directory" (Aucun fichier ni répertoire de ce type), vous devrez créer ce fichier et l'ouvrir en exécutant les commandes suivantes, ou utiliser `zsh` :

```
touch ~/.bashrc
open ~/.bashrc
```

Ensuite, vous devez définir votre clé API en ajoutant la commande d'exportation suivante :

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Après avoir enregistré le fichier, appliquez les modifications en exécutant la commande suivante :

```
source ~/.bashrc
```

### macOS – Zsh

Zsh est une configuration de terminal Linux et macOS courante. Pour vérifier si vous disposez d'un fichier de configuration, exécutez la commande suivante :

```
~/.zshrc
```

Si la réponse est "No such file or directory" (Aucun fichier ni répertoire de ce type), vous devrez créer ce fichier et l'ouvrir en exécutant les commandes suivantes, ou utiliser `bash` :

```
touch ~/.zshrc
open ~/.zshrc
```

Ensuite, vous devez définir votre clé API en ajoutant la commande d'exportation suivante :

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Après avoir enregistré le fichier, appliquez les modifications en exécutant la commande suivante :

```
source ~/.zshrc
```

### Windows

1. Recherchez "Variables d'environnement" dans la barre de recherche.
2. Choisissez de modifier les **paramètres système**. Vous devrez peut-être confirmer que vous souhaitez effectuer cette action.
3. Dans la boîte de dialogue des paramètres système, cliquez sur le bouton **Variables d'environnement**.
4. Sous **Variables utilisateur** (pour l'utilisateur actuel) ou **Variables système** (s'applique à tous les utilisateurs de la machine), cliquez sur **Nouveau…**.
5. Spécifiez le nom de la variable sous la forme `GEMINI_API_KEY`. Spécifiez votre clé API Gemini comme valeur de la variable.
6. Cliquez sur **OK** pour appliquer les modifications.
7. Ouvrez une nouvelle session de terminal (cmd ou PowerShell) pour obtenir la nouvelle variable.

## Fournir explicitement la clé API

Dans certains cas, vous pouvez fournir explicitement une clé API. Exemple :

- Vous effectuez un appel d'API simple et préférez coder en dur la clé API.
- Vous souhaitez un contrôle explicite sans avoir à vous fier à la découverte automatique des variables d'environnement par les bibliothèques de l'API Gemini.
- Vous utilisez un environnement dans lequel les variables d'environnement ne sont pas prises en charge (par exemple, le Web) ou vous effectuez des appels REST.

Vous trouverez ci-dessous des exemples de la façon dont vous pouvez fournir une clé API de manière explicite :

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Sécuriser votre clé API

Traitez votre clé API Gemini comme un mot de passe. S'il est compromis, d'autres utilisateurs peuvent utiliser le quota de votre projet, générer des frais (si la facturation est activée) et accéder à vos données privées, comme vos fichiers.

### Règles de sécurité critiques

- **Gardez vos clés confidentielles** : les clés API pour Gemini peuvent accéder à des données sensibles dont votre application dépend.

  - **N'effectuez jamais de commit de clés API vers le contrôle de source.** Ne vérifiez pas votre clé API dans les systèmes de contrôle des versions tels que Git.
  - **N'exposez jamais les clés API côté client.** N'utilisez pas votre clé API directement dans les applications Web ou mobiles en production. Les clés dans le code côté client (y compris nos bibliothèques JavaScript/TypeScript et les appels REST) peuvent être extraites.
- **Restreignez l'accès** : si possible, limitez l'utilisation des clés API à des adresses IP, des URL de provenance HTTP ou des applications Android/iOS spécifiques.
- **Restreignez l'utilisation** : n'activez que les API nécessaires pour chaque clé.
- **Effectuez des audits réguliers** : auditez régulièrement vos clés API et faites-les tourner périodiquement.

### Bonnes pratiques

- **Utiliser des appels côté serveur avec des clés API** : la méthode la plus sécurisée pour utiliser votre clé API consiste à appeler l'API Gemini à partir d'une application côté serveur où la clé peut rester confidentielle.
- **Utilisez des jetons éphémères pour l'accès côté client (API Live uniquement)** : pour un accès direct côté client à l'API Live, vous pouvez utiliser des jetons éphémères. Ils présentent moins de risques de sécurité et peuvent être utilisés en production. Pour en savoir plus, consultez le guide sur les [jetons éphémères](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=fr).
- **Envisagez d'ajouter des restrictions à votre clé** : vous pouvez limiter les autorisations d'une clé en ajoutant des [restrictions de clé API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=fr#add-api-restrictions).
  Cela permet de minimiser les dommages potentiels si la clé est divulguée.

Pour obtenir des bonnes pratiques générales, vous pouvez également consulter [cet article d'aide](https://support.google.com/googleapi/answer/6310037?hl=fr).

## Sécuriser les clés API sans restriction

Les clés API sans restriction sont vulnérables aux acteurs malveillants et aux utilisations non autorisées. À partir du 19 juin 2026, pour améliorer la sécurité, l'API Gemini ne sera plus compatible avec les clés de trafic non restreint.

**Cela signifie que vos requêtes API Gemini échoueront si vous ne prenez pas de mesures.**

Pour continuer à utiliser l'API Gemini sans interruption, sécurisez vos clés de trafic en ajoutant des restrictions dans [AI Studio](https://aistudio.google.com/api-keys?hl=fr).

Sur [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=fr), une bannière s'affiche pour vous informer lorsque les clés API sont sans restriction. Vous pouvez voir quelles clés sont sans restriction et l'utilisation des services au cours des 90 derniers jours.

Pour les clés sans restriction, vous devez choisir l'une des options suivantes :

- Utilisez la clé uniquement pour l'API Gemini.
- Utilisez la clé pour une API autre que Gemini.

### Limiter la clé à l'API Gemini uniquement

Si vous souhaitez limiter la clé à l'API Gemini uniquement, sécurisez-la dans [AI Studio](https://aistudio.google.com/api-keys?hl=fr) en cliquant sur le bouton **Restreindre à l'API Gemini**.

### Restreindre la clé pour une utilisation autre que l'API Gemini

Si vous souhaitez restreindre la clé pour une utilisation autre que l'API Gemini :

1. Accédez à la [page "Identifiants" de la console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=fr).
2. Assurez-vous que le projet est correctement sélectionné.
3. Sélectionnez une clé API.
4. Développez le menu déroulant **Restrictions d'API** et appliquez des restrictions de service à la clé API.

Si vous souhaitez modifier des clés avec des restrictions existantes ou nouvellement ajoutées, accédez à la [console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=fr).

## Résoudre les problèmes de création de clés API

Dans Google AI Studio, le bouton **Créer une clé API** peut sembler indisponible et le message suivant peut s'afficher : *Vous n'avez pas l'autorisation de créer une clé dans ce projet*.

Cela se produit lorsque vous ne disposez pas des autorisations nécessaires dans le projet pour générer une clé :

- **`resourcemanager.projects.get`** : permet à AI Studio de vérifier l'existence du projet.
- **`apikeys.keys.create`** : permet de générer la clé API elle-même.
- **`serviceusage.services.enable`** : obligatoire pour s'assurer que l'API Gemini est active dans le projet.

Pour corriger vos autorisations, demandez à l'administrateur de votre projet ou de votre organisation (si le projet appartient à une [organisation](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=fr)) de vous attribuer un rôle disposant des autorisations listées ci-dessus (par exemple, le rôle "Éditeur de projet" ou un rôle personnalisé).

Si vous n'avez pas accès à un projet en tant qu'administrateur, vous pouvez en créer un qui n'est pas associé à une organisation pour générer vos clés.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/07 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/07 (UTC)."],[],[]]
