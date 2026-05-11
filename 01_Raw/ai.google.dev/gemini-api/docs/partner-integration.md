---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=fr
fetched_at: 2026-05-11T05:04:31.446343+00:00
title: "Int\u00e9grations de partenaires et de biblioth\u00e8ques \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Intégrations de partenaires et de bibliothèques

Ce guide décrit les stratégies architecturales permettant de créer des bibliothèques, des plates-formes et des passerelles sur l'API Gemini. Il décrit en détail les compromis techniques entre l'utilisation des SDK officiels d'IA générative, de l'API Direct (REST/gRPC) et de la couche de compatibilité OpenAI.

Utilisez ce guide si vous créez des outils pour d'autres développeurs, tels que des frameworks Open Source, des passerelles d'entreprise ou des agrégateurs SaaS, et que vous devez optimiser l'hygiène des dépendances, la taille du bundle ou la parité des fonctionnalités.

## Qu'est-ce que l'intégration de partenaires ?

Un partenaire est une personne qui crée une intégration entre l'API Gemini et les développeurs d'utilisateurs finaux. Nous classons les partenaires en quatre archétypes. Identifier celui qui vous correspond le mieux vous aidera à choisir la bonne voie d'intégration.

#### Framework d'écosystème

- **Votre profil** : vous êtes responsable d'un framework Open Source (par exemple, LangChain, LlamaIndex, Spring AI) ou de clients spécifiques à une langue.
- **Votre objectif** : une compatibilité étendue. Vous souhaitez que votre bibliothèque fonctionne dans n'importe quel environnement choisi par l'utilisateur, sans forcer les conflits.

#### Plate-forme d'exécution et de périphérie

- **Qui êtes-vous ?** Plates-formes SaaS, passerelles d'IA ou fournisseurs d'infrastructure cloud (par exemple, Vercel, Cloudflare, Zapier) où l'exécution du code a lieu dans des environnements restreints.
- **Votre objectif** : les performances. Vous avez besoin d'une faible latence, d'une taille de bundle minimale et de démarrages à froid rapides.

#### Agrégateur

- **Qui êtes-vous ?** Plates-formes, proxys ou "Model Gardens" internes qui normalisent l'accès à de nombreux fournisseurs de LLM différents (par exemple, OpenAI, Anthropic, Google) dans une seule interface.
- **Votre objectif** : portabilité et uniformité.

#### Passerelle Enterprise

- **Votre profil** : vous faites partie d'une équipe d'ingénierie des plates-formes internes dans une grande entreprise et vous créez des "voies optimales" pour des centaines de développeurs internes.
- **Votre objectif** : standardisation, gouvernance et authentification unifiée.

## Comparaison en un coup d'œil

**Bonne pratique à l'échelle mondiale** : tous les partenaires doivent envoyer l'[en-tête `x-goog-api-client`](#client-id), quel que soit le chemin choisi.

| Si vous êtes : | Chemin recommandé | Principal avantage | Compromis clé | Bonne pratique |
| --- | --- | --- | --- | --- |
| **Passerelle d'entreprise, framework d'écosystème** | **[SDK Google GenAI](#genai-sdk)** | **Parité et vitesse de Gemini Enterprise Agent Platform.** Gestion intégrée des types, de l'authentification et des fonctionnalités complexes (par exemple, l'importation de fichiers). Migration transparente vers Google Cloud. | **Poids de la dépendance** Les dépendances transitives peuvent être complexes et hors de votre contrôle. Limité aux langages compatibles (Python/Node/Go/Java). | **Verrouillez les versions.** Épinglez les versions du SDK dans vos images de base internes pour assurer la stabilité entre les équipes. |
| **Framework d'écosystème, plates-formes Edge et agrégateurs** | **[API directe](#rest)**  *(REST / gRPC)* | **Aucune dépendance.** Vous contrôlez le client HTTP et la taille exacte du bundle. Accès complet à toutes les fonctionnalités des API et des modèles. | **Frais de développement élevés** : Les structures JSON peuvent être profondément imbriquées et nécessitent une validation manuelle et une vérification des types strictes. | **Utilisez les spécifications OpenAPI.** Automatisez la génération de types à l'aide de nos spécifications officielles au lieu de les écrire à la main. |
| **Agrégateur utilisant les SDK OpenAI qui ne nécessitent que des workflows basés sur du texte**  *(Optimisation pour la portabilité des anciens systèmes)* | **[Compatibilité avec OpenAI](#openai)** | **Portabilité instantanée** : Réutiliser du code ou des bibliothèques existants compatibles avec OpenAI | **Plafond de caractéristiques** : Il est possible que les fonctionnalités spécifiques au modèle (vidéo native, mise en cache) ne soient pas disponibles. | **Plan de migration.** Utilisez-le pour une validation rapide, mais prévoyez de passer à l'API Direct pour bénéficier de toutes les fonctionnalités de l'API. |

## Intégration du SDK Google GenAI

Pour les frameworks, l'implémentation du [SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) est souvent la méthode la plus simple, car elle nécessite le moins de lignes de code dans les langages compatibles.

Pour les équipes de plate-forme internes, votre principal livrable est souvent un "chemin d'or" qui permet aux ingénieurs produit d'avancer rapidement tout en respectant les règles de sécurité.

**Avantages :**

- **Interface unifiée pour la migration de Gemini Enterprise Agent Platform** : les développeurs internes créent souvent des prototypes à l'aide de clés API (API Gemini) et les déploient sur Gemini Enterprise Agent Platform (IAM) pour la conformité en production. Le SDK fait abstraction de ces différences d'authentification.
  De même, pour les frameworks, vous pouvez implémenter un chemin de code et prendre en charge deux ensembles d'utilisateurs.
- **Assistance côté client** : le SDK inclut des utilitaires idiomatiques qui réduisent le code passe-partout pour les tâches complexes.
  - *Exemples* : prise en charge des objets image `PIL` directement dans les requêtes, appel de fonction automatique et types complets.
- **Accès aux fonctionnalités dès le premier jour** : les nouvelles fonctionnalités de l'API sont disponibles au moment du lancement via les SDK.
- **Prise en charge améliorée de la génération de code** : l'installation locale du SDK expose les définitions de type et les chaînes de documentation aux assistants de codage (par exemple, Cursor et Copilot).
  Ce contexte améliore la précision de la génération de code par rapport à la génération de requêtes REST brutes.

**Le compromis :**

- **Poids et complexité des dépendances** : les SDK ont leurs propres dépendances, ce qui peut augmenter la taille du bundle et potentiellement le risque lié à la chaîne d'approvisionnement.
- **Gestion des versions** : les nouvelles fonctionnalités de l'API sont souvent associées à des versions minimales du SDK.
  Vous devrez peut-être envoyer des mises à jour aux utilisateurs pour qu'ils puissent accéder aux nouvelles fonctionnalités ou aux nouveaux modèles. Dans certains cas, cela peut nécessiter des modifications des dépendances transitives qui affectent vos utilisateurs.
- **Limites de protocole** : les SDK ne sont compatibles qu'avec HTTPS pour l'API principale et WebSockets (WSS) pour l'API Live. gRPC n'est pas compatible avec les clients SDK de haut niveau.
- **Langues acceptées** : les SDK sont compatibles avec les versions linguistiques *actuelles*. Si vous devez prendre en charge les versions en fin de vie (par exemple, Python 3.9), vous devrez gérer un fork.

**Bonnes pratiques :**

- **Verrouillez les versions** : épinglez la version du SDK dans vos images de base internes pour assurer la stabilité entre les équipes.

## Intégration directe à l'aide de l'API

Si vous distribuez une bibliothèque à des milliers de développeurs, que vous l'exécutez dans un environnement contraint ou que vous créez un agrégateur qui nécessite les fonctionnalités de pointe de Gemini, vous devrez peut-être l'intégrer directement à l'API à l'aide de REST ou de gRPC.

**Avantages :**

- **Accès complet aux fonctionnalités** : contrairement à la couche de compatibilité OpenAI, l'utilisation directe de l'API permet d'accéder à des fonctionnalités spécifiques à Gemini, telles que l'importation dans l'API File, la création de mise en cache de contenu et l'utilisation de l'API Live bidirectionnelle.
- **Dépendances minimales** : dans un environnement où les dépendances sont sensibles en raison de la taille ou des coûts d'audit. L'utilisation de l'API directement via une bibliothèque standard comme `fetch` ou via un wrapper comme `httpx` garantit que votre bibliothèque reste légère.
- **Indépendant du langage** : il s'agit de la seule option pour les langages non couverts par les SDK, tels que Rust, PHP et Ruby, car il n'y a aucune restriction de langage.
- **Performances** : l'API Direct n'a aucun coût d'initialisation, ce qui minimise les démarrages à froid dans les fonctions sans serveur.

**Le compromis :**

- **Implémentation manuelle de la plate-forme d'agents Gemini Enterprise** : contrairement au SDK, l'utilisation directe de l'API ne gère pas automatiquement les différences d'authentification entre AI Studio (clé API) et la plate-forme d'agents Gemini Enterprise (IAM). Vous devez implémenter des gestionnaires d'authentification distincts si vous souhaitez prendre en charge les deux environnements.
- **Pas de types ni d'assistants natifs** : vous n'obtenez pas de complétion de code ni de vérifications au moment de la compilation pour les objets de requête, sauf si vous les implémentez vous-même. Il n'existe pas d'assistants clients (par exemple, des convertisseurs de fonction en schéma). Vous devez donc écrire cette logique manuellement.

**Bonne pratique**

Nous exposons une spécification lisible par machine que vous pouvez utiliser pour générer des définitions de type pour votre bibliothèque, ce qui vous évite de les écrire à la main. Téléchargez la spécification lors du processus de compilation, générez les types et distribuez le code compilé.

- **Point de terminaison** : `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Intégration du SDK OpenAI

Si vous êtes une plate-forme qui privilégie un schéma unifié (OpenAI Chat Completions) plutôt que des fonctionnalités spécifiques à un modèle, il s'agit de la méthode la plus rapide.

**Avantages :**

- **Faible friction** : vous pouvez souvent ajouter la prise en charge de Gemini en modifiant `baseURL` et `apiKey`. Il s'agit d'un moyen rapide d'intégrer les implémentations "Bring Your Own Key" (Apportez votre propre clé), en ajoutant la prise en charge de Gemini sans écrire de nouveau code.
- **Contraintes** : Ce chemin n'est recommandé que si vous êtes limité au SDK OpenAI et que vous n'avez pas besoin de fonctionnalités Gemini avancées comme l'API File, ou d'ajouter manuellement la prise en charge d'outils comme l'ancrage avec la recherche Google.

**Le compromis :**

- **Limites des fonctionnalités** : la couche de compatibilité impose des limites aux capacités Gemini de base. Les outils côté serveur disponibles diffèrent selon les plates-formes et peuvent nécessiter une gestion manuelle pour fonctionner avec les outils de l'API Gemini.
- **Surcharge de traduction** : comme le schéma OpenAI ne correspond pas exactement à l'architecture de Gemini, le recours à la couche de compatibilité introduit certaines complexités qui nécessitent un travail d'implémentation supplémentaire pour être résolues, comme le mappage d'un outil de "recherche" utilisateur à l'outil de plate-forme approprié.
  Si vous avez besoin d'un grand nombre de cas particuliers, il peut être plus intéressant d'utiliser un SDK ou une API dédiés pour chaque plate-forme.

**Bonne pratique**

Si possible, intégrez directement l'API Gemini. Toutefois, pour une compatibilité maximale, envisagez d'utiliser une bibliothèque qui connaît les différents fournisseurs et qui peut gérer le mappage des outils et des messages pour vous.

## Bonne pratique pour tous les partenaires : identification du client

Lorsque vous appelez l'API Gemini en tant que plate-forme ou bibliothèque, vous devez identifier votre client à l'aide de l'en-tête `x-goog-api-client`.

Cela permet à Google d'identifier vos segments de trafic spécifiques. Si votre bibliothèque produit un modèle d'erreur spécifique, nous pouvons vous contacter pour vous aider à le déboguer.

Utilisez le format `company-product/version` (par exemple, `acme-framework/1.2.0`).

### Exemples d'intégration

### SDK GenAI

En fournissant le client API, le SDK ajoute automatiquement votre en-tête personnalisé à ses en-têtes internes.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### API directe (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### SDK OpenAI

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Étapes suivantes

- Consultez la [présentation de la bibliothèque](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) pour en savoir plus sur les SDK GenAI.
- Parcourir la [documentation de référence de l'API](https://ai.google.dev/api?hl=fr)
- Consultez le [guide de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
