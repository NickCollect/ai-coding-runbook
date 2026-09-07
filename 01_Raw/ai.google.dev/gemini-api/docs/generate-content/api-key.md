---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=fr
fetched_at: 2026-09-07T05:46:59.296749+00:00
title: "Utiliser des cl\u00e9s API Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Utiliser des clés API Gemini

Pour utiliser l'API Gemini, vous devez authentifier vos requêtes. Vous pouvez vous authentifier à l'aide d'une clé API standard ou d'une clé API d'autorisation.

[Créer ou afficher une clé API Gemini](https://aistudio.google.com/apikey?hl=fr)

## Types de clés API : standard ou d'autorisation

Les clés API permettent d'accéder à l'API Gemini, mais leurs caractéristiques de sécurité diffèrent. L'API Gemini passe des clés API standard aux clés d'autorisation pour améliorer la sécurité :

- **Les clés API standard** associent les requêtes à un projet Google Cloud à des fins de
  facturation et de quota. Les clés standard n'identifient pas l'appelant, ce qui limite la granularité des autorisations et du contrôle des accès qu'elles peuvent prendre en charge.
- Les **clés d'autorisation** sont directement liées à un compte de service Google Cloud. Lorsque vous utilisez une clé d'autorisation, vos requêtes sont traitées sous l'identité de ce compte de service lié, ce qui permet un contrôle d'accès précis. Les clés d'autorisation sont limitées à l'API Generative Language (API Gemini) par défaut et permettent d'appliquer rapidement les clés divulguées, ce qui arrête rapidement l'utilisation des clés divulguées détectées par nos systèmes.

Pour garantir une utilisation sécurisée, l'API Gemini passera des clés standard aux clés d'autorisation :

- **Clés d'autorisation par défaut** : toutes les nouvelles clés API créées dans Google AI Studio
  sont automatiquement créées en tant que clés d'autorisation.
- **Clés sans restriction refusées** : l'API Gemini refuse les requêtes
  provenant de **clés standard sans restriction**. Les clés API standard auxquelles des restrictions explicites sont appliquées continuent de fonctionner. Cette restriction empêche l'utilisation non autorisée de clés qui pourraient être partagées publiquement ou liées à d'autres services.
- **En septembre 2026** : l'API Gemini refusera les requêtes provenant de **clés
  standard**. Vous devez [migrer vers des clés d'autorisation](#migrate-to-auth-key)
  avant cette date pour éviter toute interruption de service. Veillez à migrer vers des clés d'autorisation avant septembre 2026.

## Gérer les clés API dans Google AI Studio

Vous pouvez gérer vos projets et vos clés directement dans [Google AI Studio](https://aistudio.google.com/apikey?hl=fr).

### Projets Google Cloud

Chaque clé API Gemini est associée à un [projet Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=fr).
Les projets Google Cloud gèrent la facturation, les collaborateurs et les autorisations. Google AI Studio fournit une interface légère pour accéder à ces projets.

- **Projet par défaut** : si vous êtes un nouvel utilisateur, Google AI Studio crée automatiquement
  un projet Google Cloud et une clé API par défaut après que vous avez accepté les
  Conditions d'utilisation. Vous pouvez renommer ce projet en accédant à la vue **Projects** (Projets) de votre tableau de bord.
- **Projets existants** : si vous possédez déjà un compte Google Cloud, AI
  Studio ne crée pas de projet par défaut. Vous devez plutôt importer vos projets existants.

### Importer des projets

Par défaut, Google AI Studio n'affiche pas tous vos projets Google Cloud. Vous devez importer les projets que vous souhaitez utiliser :

1. Accédez à [Google AI Studio](https://aistudio.google.com?hl=fr).
2. Ouvrez le **Dashboard** (Tableau de bord) dans le panneau de gauche, puis sélectionnez **Projects** (Projets).
3. Cliquez sur le bouton **Import projects** (Importer des projets).
4. Recherchez et sélectionnez le projet Google Cloud que vous souhaitez importer, puis cliquez sur **Import** (Importer).
5. Une fois l'importation terminée, accédez à la page **API Keys** (Clés API) du tableau de bord pour créer une clé dans ce projet.

### Résoudre les problèmes d'autorisations de création de clés

Si le bouton **Create API key** n'est pas disponible et affiche le message :
*"Vous ne disposez pas des autorisations nécessaires pour créer une clé dans ce projet"*, vous ne disposez pas des
autorisations IAM requises.

Demandez à l'administrateur de votre projet ou de votre organisation Google Cloud de vous accorder un rôle contenant les autorisations suivantes (par exemple, Éditeur de projet) :

- `resourcemanager.projects.get` : permet à AI Studio de vérifier le projet.
- `apikeys.keys.create` : permet la génération de clés.
- `serviceusage.services.enable`: garantit que l'API Generative Language est activée.
- `iam.serviceAccounts.create` : obligatoire pour créer le compte de service lié.
- `iam.serviceAccountApiKeyBindings.create`: lie le compte de service à la clé API.

Si vous ne parvenez pas à obtenir un accès administrateur, vous pouvez créer un projet Google Cloud qui n'est pas associé à une organisation pour générer vos clés.

## Configurer votre environnement

Une fois que vous disposez d'une clé, configurez votre environnement pour l'utiliser de manière sécurisée dans vos applications.

### Utiliser des variables d'environnement (recommandé)

Définissez la variable d'environnement `GEMINI_API_KEY` ou `GOOGLE_API_KEY`. Les bibliothèques clientes de l'API Gemini détectent et utilisent automatiquement ces variables. Si les deux sont définies, `GOOGLE_API_KEY` est prioritaire.

Sélectionnez votre système d'exploitation pour définir la variable :

### Linux/macOS – Bash

Vérifiez si vous disposez d'un fichier de configuration bash :

```
~/.bashrc
```

Si ce n'est pas le cas, créez-en un et ouvrez-le :

```
touch ~/.bashrc && open ~/.bashrc
```

Ajoutez la commande d'exportation à la fin du fichier :

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Enregistrez le fichier, puis appliquez les modifications :

```
source ~/.bashrc
```

### macOS – Zsh

Vérifiez si vous disposez d'un fichier de configuration zsh :

```
~/.zshrc
```

Si ce n'est pas le cas, créez-en un et ouvrez-le :

```
touch ~/.zshrc && open ~/.zshrc
```

Ajoutez la commande d'exportation :

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Enregistrez le fichier, puis appliquez les modifications :

```
source ~/.zshrc
```

### Windows

1. Recherchez "Variables d'environnement" dans la barre de recherche Windows.
2. Cliquez sur **Variables d'environnement** dans la boîte de dialogue "Propriétés système".
3. Sous **Variables utilisateur** ou **Variables système**, cliquez sur **Nouveau...**.
4. Définissez le nom de la variable sur `GEMINI_API_KEY` et la valeur sur votre clé API.
5. Cliquez sur **OK** pour enregistrer vos paramètres. Ouvrez une nouvelle session de terminal pour charger la variable.

### Fournir explicitement la clé API dans le code

Vous pouvez transmettre explicitement la clé API lors de l'initialisation du client. Ne le faites que si vous ne pouvez pas utiliser de variables d'environnement.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
            "gemini-3.6-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
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

## Sécurité et gestion des secrets

Traitez votre clé API Gemini comme un mot de passe. Si elle est compromise, d'autres personnes peuvent consommer le quota de votre projet, entraîner des frais de facturation inattendus et accéder à des ressources privées.

### Règles de sécurité critiques

- **Gardez les clés confidentielles** : n'enregistrez jamais de clés API dans des systèmes de contrôle des sources
  tels que Git.
- **N'exposez jamais les clés côté client en production** : ne codez pas en dur les clés API
  directement dans les applications Web ou mobiles. Les clés compilées dans le code côté client peuvent être extraites par les utilisateurs. Pour sécuriser les applications côté client, exécutez un serveur proxy de backend pour effectuer les appels d'API réels.

### Bonnes pratiques concernant la gestion des secrets

- **Variables d'environnement** : lisez les clés à partir de variables d'environnement plutôt que de fichiers de
  configuration.
- **Secret Manager** : pour la production, stockez vos clés dans un magasin de secrets sécurisé
  tel que [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=fr).
- **Alertes de facturation** : configurez des alertes de facturation dans la console Google Cloud pour
  être averti en cas de pic d'utilisation ou de coûts.

### Checklist de réponse en cas de fuite

Si vous pensez que votre clé API a été divulguée :

1. **Générez une nouvelle clé** : créez une clé de remplacement dans Google AI Studio ou
   Cloud Console.
2. **Mettez à jour votre application** : déployez votre code à l'aide de la nouvelle clé.
3. **Désactivez ou supprimez la clé compromise** : désactivez la clé divulguée dans
   Cloud Console une fois la nouvelle clé validée. Ne supprimez pas l'ancienne clé tant que la nouvelle n'est pas entièrement active pour éviter les temps d'arrêt de l'application.
4. **Auditez l'utilisation** : vérifiez les journaux de facturation et l'utilisation de l'API dans la console Google Cloud
   pour identifier toute activité non autorisée.

## Restreindre et sécuriser vos clés

L'ajout de restrictions à vos clés API minimise les dommages potentiels en cas de compromission d'une clé.

### Appliquer des restrictions d'origine des requêtes

Les restrictions d'origine limitent les adresses IP, les sites Web ou les applications qui peuvent utiliser votre clé.

1. Accédez à la page "[Identifiants](https://console.cloud.google.com/apis/credentials?hl=fr)" de la console Google Cloud.
2. Sélectionnez votre projet, puis cliquez sur le nom de la clé API que vous souhaitez restreindre.
3. Sous **Application restrictions** (Restrictions liées aux applications), sélectionnez **IP addresses** (Adresses IP) (ou le
   type de restriction approprié pour votre environnement).
4. Spécifiez les adresses IP ou les plages autorisées, puis cliquez sur **Save** (Enregistrer).

### Sécuriser les clés API standard sans restriction

Pour continuer à utiliser l'API Gemini, vous devez sécuriser toutes les clés sans restriction.

#### Restreindre la clé à l'API Gemini uniquement via AI Studio

Si vous n'utilisez la clé que pour l'API Gemini, sécurisez-la directement dans AI Studio :

1. Sur la page **API Keys** (Clés API) de [Google AI Studio](https://aistudio.google.com/api-keys?hl=fr), recherchez les clés marquées du libellé
   **Unrestricted** (Sans restriction).
2. Pointez sur le libellé, puis cliquez sur **Add restrictions** (Ajouter des restrictions) dans la boîte de dialogue.
3. Sélectionnez **Restrict to Gemini API only** (Restreindre à l'API Gemini uniquement).
4. Cliquez sur **Restrict key** (Restreindre la clé) pour confirmer.

#### Restreindre la clé pour d'autres services via la console Google Cloud

Si la clé est partagée avec d'autres API Google (non recommandé), limitez-la dans Cloud Console. **Remarque : Les requêtes de l'API Gemini utilisant cette clé échoueront une fois ces restrictions appliquées.**

1. Accédez à la page "[Identifiants](https://console.cloud.google.com/apis/credentials?hl=fr)" de la console Google Cloud.
2. Sélectionnez le projet et la clé API.
3. Sous **API restrictions** (Restrictions liées à l'API), sélectionnez **Restrict key** (Restreindre la clé).
4. Dans la liste déroulante, sélectionnez les API auxquelles vous souhaitez que cette clé accède. Ne sélectionnez pas l'**API Generative Language**.
5. Cliquez sur **Save** (Enregistrer). Créez une clé distincte et limitée dans AI Studio pour continuer à utiliser l'API Gemini.

### Clés inactives bloquées

À partir du 7 mai 2026, l'API Gemini bloquera les clés API sans restriction qui sont inactives depuis une période prolongée. Ces clés affichent un tag **Blocked** (Bloqué) dans AI Studio. Vous devez générer une nouvelle clé ou utiliser une clé limitée existante pour continuer.

## Migrer vers une clé d'autorisation

Suivez ces étapes pour créer une clé API d'autorisation et mettre à jour vos applications :

1. Accédez à la page "[Clés API](https://aistudio.google.com/api-keys?hl=fr)" d'AI Studio.
2. Cochez la colonne **Key Type** (Type de clé) pour identifier les clés listées comme **Standard**.
3. Cliquez sur **Create API key** (Créer une clé API) pour générer une nouvelle clé. Toutes les nouvelles clés créées dans AI Studio sont automatiquement créées en tant que clés d'autorisation.
4. Copiez la nouvelle clé API d'autorisation.
5. Mettez à jour le code de votre application, les variables d'environnement et toutes les configurations de déploiement pour utiliser la nouvelle clé API d'autorisation.
6. Testez votre application pour vérifier qu'elle fonctionne correctement avec la nouvelle clé.
7. Une fois la validation effectuée, supprimez ou révoquez votre ancienne clé de trafic pour éviter toute utilisation abusive.

## Limites

Google AI Studio impose les limites suivantes en matière de gestion des projets et des clés :

- Vous pouvez créer au maximum 10 projets à la fois à partir de la page **Projects** (Projets) de Google AI Studio.
- Les pages **API keys** (Clés API) et **Projects** (Projets) affichent au maximum 100 clés et 50 projets.
- Seules les clés API sans restriction ou limitées spécifiquement à l'API Generative Language (API Gemini) sont affichées.

Pour une gestion avancée des projets ou pour modifier des clés avec d'autres restrictions, utilisez
la page "[Identifiants](https://console.cloud.google.com/apis/credentials?hl=fr)" de la console Google Cloud.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
