---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr
fetched_at: 2026-10-05T06:28:15.170786+00:00
title: "Configurer votre assistant de codage avec Gemini\u00a0MCP et Skills \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Configurer votre assistant de codage avec Gemini MCP et Skills

Les assistants de programmation basés sur l'IA sont puissants, mais ils ont des limites : les données d'entraînement s'arrêtent à une date spécifique et ne tiennent pas compte des nouvelles fonctionnalités et modifications des API. Sans accès à la documentation spécifique à Gemini, les agents peuvent suggérer des schémas génériques au lieu d'approches optimisées.

Pour que votre assistant de programmation reste à jour avec l'évolution de l'API Gemini et son utilisation recommandée, nous vous conseillons de configurer le **MCP Gemini Docs** et d'améliorer votre environnement avec les **compétences de l'API Gemini**. Bien que ces outils puissent être utilisés indépendamment, ils sont conçus pour fonctionner ensemble et offrir une couverture complète.

## Connecter le MCP Gemini Docs

Gemini héberge un serveur MCP (Model Context Protocol) public à l'adresse `https://gemini-api-docs-mcp.dev`. En connectant votre agent de codage à ce serveur, vous vous assurez que toutes les requêtes ont accès aux dernières API, aux mises à jour du code et aux exemples de configuration optimale.

Exécutez la commande suivante dans le terminal ou la racine du projet de votre agent pour installer le serveur :

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Ce serveur ajoute une fonction `search_documentation` que votre agent peut utiliser pour récupérer les définitions d'API et les modèles d'intégration en temps réel à partir des fichiers de documentation Gemini officiels.

## Ajouter des compétences en développement d'API

Les compétences fournissent des **règles et des bonnes pratiques intégrées** (comme l'application des versions correctes du SDK et du modèle actuel) directement dans le contexte de votre assistant. La compétence fonctionne avec le service MCP Gemini Docs : si vous avez installé les deux, la compétence utilise le service MCP pour la documentation. Toutefois, même sans le service MCP installé, elle récupère [`/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=fr) à partir de `ai.google.dev` en tant que solution de secours (où les pages individuelles peuvent également être récupérées au format Markdown brut en ajoutant `.md.txt`, par exemple `https://ai.google.dev/gemini-api/docs/speech-generation.md.txt`).

Pour installer ces skills, vous pouvez utiliser l'un des outils compatibles suivants. Vous trouverez les instructions d'installation pour les deux modules de compétences sous chacun d'eux :

- **[skills.sh](https://skills.sh)** : recommandé. Norme ouverte pour les comportements d'agent portables.
- **[Context7](https://context7.com)** : disponible pour les utilisateurs qui utilisent déjà l'écosystème Context7.

### gemini-api-dev

Compétence pour créer des applications avec l'[API Gemini](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) (API Interactions). L'API Interactions est le moyen le plus simple et le plus efficace de créer des applications avec les modèles et les agents Gemini. Cette compétence couvre les points suivants :

- Génération de texte, chat multitour et streaming
- Appel de fonction, sortie structurée et génération d'images
- Exécution en arrière-plan et agents Deep Research
- Gestion de l'état de la conversation côté serveur
- Routage des requêtes vers les modèles actuels et évitement des modèles obsolètes
- Modèles de SDK Python et TypeScript

#### Installer avec skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Installer avec Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Compétence pour créer des applications d'IA conversationnelle en temps réel avec l'API Gemini Live. Cette compétence fournit de la documentation et des bonnes pratiques pour :

- Connexions WebSocket pour le streaming à faible latence
- Streaming audio, vidéo et texte
- Détection de l'activité vocale et prise en charge de l'interruption

#### Installer avec skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Installer avec Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

## Vérifier l'installation

Après l'installation, vérifiez que votre assistant de codage peut se connecter au serveur MCP Gemini Docs et utiliser les compétences installées.

### 1. Vérifier le comportement de l'agent

Le moyen le plus fiable de le vérifier est de poser une question technique à votre agent sur l'API Gemini.

**Requête** : "Comment utiliser la mise en cache du contexte avec l'API Gemini ?"

Une configuration réussie :

- **Fournissez du code précis** : référencez des méthodes Gemini spécifiques telles que `cacheContent` ou `cachedContents.create` à partir des derniers points de terminaison.
- **Utiliser l'outil MCP** : montrer qu'il est connecté au **serveur MCP Gemini Docs** ou qu'il utilise l'outil `search_documentation` pour récupérer des données.
- **Invoquer les compétences chargées** : afficher un indicateur "Utilisation de la compétence : gemini-api-dev" (si vous vous appuyez sur un wrapper secondaire).

### 2. Valider les manifestations et les outils

Si l'agent fournit une réponse générale ou générique, utilisez les commandes spécifiques "Discovery" ou "Status" pour votre environnement afin de vérifier que le MCP ou la skill Docs sont chargés en mémoire.

| Environnement | Validation MCP | Validation des compétences |
| --- | --- | --- |
| **Claude Code** | Saisissez `/mcp` dans le terminal pour afficher les serveurs actifs et les outils `search_documentation`. | Saisissez `/skills` dans le terminal pour lister tous les fichiers manifestes actifs. |
| **Cursor** | Accédez à **Paramètres > Fonctionnalités > MCP**. Assurez-vous que le serveur est "Connecté". | Ouvrez **Paramètres > Règles**. Vérifiez que la compétence apparaît sous "L'agent décide". |
| **Antigravity** | Consultez la barre latérale **Personnalisations > Connexions** pour connaître l'état du MCP. | Saisissez `/skills list` ou cochez la barre latérale **Personnalisations > Règles**. |
| **Gemini CLI** | Exécutez `gemini mcp list` ou utilisez `/mcp list`. | Exécutez `gemini skills list` ou utilisez la commande à barre oblique `/skills` en cours de session. |
| **Copilot** | Saisissez `@gemini /mcp` pour lister les connecteurs de données actifs. | Saisissez `@gemini /skills` (ou `/skills`) pour afficher les extensions actives. |

## Dépannage

Si votre agent ne fournit que des informations générales ou ne reconnaît pas les méthodes spécifiques à Gemini, vérifiez les points suivants :

### L'agent n'a pas découvert la compétence

La plupart des agents n'indexent les compétences qu'au démarrage.

**Correction** : redémarrez complètement votre IDE (Cursor/VS Code) ou quittez et rouvrez votre agent basé sur un terminal (Claude Code).

### Conflits globaux et locaux

Si vous avez installé l'agent avec l'indicateur `--global`, il est possible qu'il l'ignore au profit de règles spécifiques au projet.

**Solution** : essayez d'installer la skill directement à la racine de votre projet, sans l'indicateur global :

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Ressources

- [Compétences de l'API Gemini sur GitHub](https://github.com/google-gemini/gemini-skills)
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr)
- [Commencer](https://ai.google.dev/gemini-api/docs/get-started?hl=fr)
- [Bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
