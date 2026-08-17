---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-preview?hl=fr
fetched_at: 2026-08-17T02:24:36.441230+00:00
title: "Gemini Robotics ER\u00a02 Preview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Gemini Robotics ER 2 Preview

Gemini Robotics ER2 est un modèle de vision-langage (VLM) pour la robotique qui accepte les entrées de texte, d'image, de vidéo et d'audio. Il prend en charge le raisonnement spatial, la compréhension des vidéos, l'exécution de code agentique, l'orchestration d'outils en plusieurs étapes et la coordination de plusieurs robots.

[Essayer dans Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=fr)

## Documentation

Consultez la page [Robotique](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) pour obtenir une couverture complète des fonctionnalités.

## gemini-robotics-er-2-preview

### Gemini Robotics ER 2 Preview

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | `gemini-robotics-er-2-preview` |
| Types de données acceptés pour save | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handyman Fonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Compatible  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Compatible  **[Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Compatible  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Compatible  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Compatible  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Not supported  **[Ancrage de recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Compatible  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Compatible |
| speed Options de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Compatible  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Aperçu : `gemini-robotics-er-2-preview` |
| calendar\_monthDernière mise à jour | Juillet 2026 |
| Fiche de modèle id\_card | [fiche de modèle](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fr) |

### Aperçu du streaming Gemini Robotics ER 2

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | `gemini-robotics-er-2-streaming-preview` |
| Types de données acceptés pour save | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handyman Fonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Not supported  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Not supported  **[Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Not supported  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Not supported  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Not supported  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Compatible  **[Ancrage de recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Not supported  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Not supported |
| speed Options de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Not supported  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Aperçu : `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthDernière mise à jour | Juillet 2026 |
| Fiche de modèle id\_card | [fiche de modèle](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fr) |

### Gemini Robotics ER 1.6 (preview)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | `gemini-robotics-er-1.6-preview` |
| Types de données acceptés pour save | **Entrées**  Texte, images, vidéo, audio  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  131 072  **Limite de jetons de sortie**  65 536 |
| handyman Fonctionnalités | **[Génération d'audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)**  Not supported  **[Mise en cache](https://ai.google.dev/gemini-api/docs/caching?hl=fr)**  Compatible  **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**  Compatible  **[Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)**  Compatible  **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)**  Compatible  **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)**  Compatible  **[Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)**  Compatible  **[Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)**  Not supported  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr)**  Not supported  **[Ancrage de recherche](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)**  Compatible  **[Sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr)**  Compatible  **[Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)**  Compatible  **[Contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)**  Compatible |
| speed Options de consommation | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr)**  Compatible  **[Inférence Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr)**  Not supported  **[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)**  Not supported |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Aperçu : `gemini-robotics-er-1.6-preview` |
| calendar\_monthDernière mise à jour | Décembre 2025 |
| cognition\_2Date limite des connaissances | Janvier 2025 |

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
