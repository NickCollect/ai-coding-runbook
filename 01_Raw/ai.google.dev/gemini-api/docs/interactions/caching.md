---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=fr
fetched_at: 2026-06-15T06:31:51.436795+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# mise en cache du contexte

Dans un workflow d'IA typique, vous pouvez transmettre les mêmes jetons d'entrée à un modèle à plusieurs reprises. L'API Gemini propose une mise en cache implicite pour optimiser les performances et les coûts.

## Mise en cache implicite

La mise en cache implicite est activée par défaut pour tous les modèles Gemini 2.5 et ultérieurs. Nous répercutons automatiquement les économies de coûts si votre requête atteint les caches. Aucune action n'est requise de votre part pour activer cette fonctionnalité. Le nombre minimal de jetons d'entrée pour la mise en cache du contexte est indiqué dans le tableau suivant pour chaque modèle :

| Modèle | Limite minimale de jetons |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Preview Gemini 3.1 Pro | 4096 |
| Gemini 2.0 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Pour augmenter les chances d'un succès de cache implicite :

- Essayez de placer les contenus volumineux et courants au début de votre requête.
- Essayer d'envoyer des requêtes avec un préfixe similaire en peu de temps

Vous pouvez voir le nombre de jetons qui ont été des accès au cache dans le champ `usage_metadata` (Python) ou `usageMetadata` (JavaScript) de l'objet de réponse.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/02 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/02 (UTC)."],[],[]]
