---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=fr
fetched_at: 2026-06-01T06:02:56.184926+00:00
title: "Notes de version \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Notes de version

Cette page répertorie les mises à jour de l'API Gemini.

## 28 mai 2026

- Sortie des versions disponibles pour tous (GA) de nos modèles visuels natifs [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=fr) et [Gemini 3.1 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=fr), `gemini-3.1-flash-image` (Nano Banana 2) et `gemini-3-pro-image` (Nano Banana Pro).
- **Prise en charge de la génération d'images à partir de vidéos** : vous pouvez désormais transmettre un fichier vidéo (par importation directe ou en tant qu'URL YouTube publique) en tant que contexte multimodal avec une requête textuelle pour générer des miniatures de haute qualité, des affiches de films cinématographiques ou des infographies récapitulatives. Cette fonctionnalité n'est disponible que sur le modèle `gemini-3.1-flash-image`. Pour en savoir plus, consultez le guide [Génération d'images à partir de vidéos](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#video-to-image).
- Annonce d'abandon : les modèles `gemini-3.1-flash-image-preview` et `gemini-3-pro-image-preview` sont abandonnés et seront [arrêtés](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 25 juin 2026.

## 25 mai 2026

- Le modèle `gemini-3.1-flash-lite-preview` a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr). Utilisez plutôt [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr).

## 19 mai 2026

- La version en disponibilité générale (DG) de [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr), notre modèle le plus intelligent pour des performances de pointe soutenues sur les tâches agentiques et de codage, est sortie le `gemini-3.5-flash`.
- Lancement de la **version Preview publique des agents gérés dans l'API Gemini**. Les développeurs peuvent ainsi créer et déployer des agents autonomes avec état qui s'exécutent dans des environnements Linux sécurisés et isolés hébergés par Google. Pour en savoir plus, consultez la page [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) et le [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr).
- Publication de l'agent géré **Antigravity Agent** à usage général, [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=fr), en version Preview publique.
  L'agent Antigravity peut planifier, raisonner, écrire et exécuter du code de manière autonome, gérer des fichiers et naviguer sur le Web dans son conteneur bac à sable. Pour obtenir des exemples de code et des spécifications, consultez le guide [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr).

## 7 mai 2026

- Sortie de la version en disponibilité générale (DG) de [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr), optimisée pour la rapidité, l'évolutivité et la rentabilité.`gemini-3.1-flash-lite`
- Annonce d'abandon : le modèle `gemini-3.1-flash-lite-preview` sera abandonné le 11/05/2026 et [éteint](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 25/05/2026.

## 6 mai 2026

- **Changement incompatible à venir** : le schéma de requête et de réponse de l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr) (`outputs` → `steps`) et la configuration du format de sortie (`response_format`) vont changer. Le nouveau schéma deviendra celui par défaut le **26 mai** et l'ancien schéma sera supprimé le **8 juin**.
  Pour en savoir plus, consultez le [guide de migration](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=fr).

## 5 mai 2026

- Mise à jour de la **recherche de fichiers** pour prendre en charge la recherche multimodale. Vous pouvez désormais intégrer et rechercher des images de manière native à l'aide du modèle `gemini-embedding-2`.
  Les métadonnées d'ancrage incluent désormais `media_id` pour les citations visuelles et `page_numbers` qui indiquent où trouver les informations. Pour en savoir plus, consultez le guide [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

## 4 mai 2026

- Lancement de la compatibilité avec les [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=fr) basés sur des événements dans l'API Gemini pour remplacer les workflows d'interrogation pour l'API Batch et les opérations de longue durée.

## 30 avril 2026

- Le modèle `gemini-robotics-er-1.5-preview` a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr). Utilisez plutôt [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=fr).

## 22 avril 2026

- `gemini-embedding-2` est désormais disponible pour tous les utilisateurs. Pour en savoir plus, consultez la page [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr).

## 21 avril 2026

- Nouvelles versions de l'agent [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) avec planification collaborative, prise en charge de la visualisation, intégration du serveur MCP et recherche de fichiers :

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=fr) : conçu pour la rapidité et l'efficacité, idéal pour être diffusé en streaming vers une UI client.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=fr) : exhaustivité maximale pour la collecte et la synthèse automatiques du contexte.

## 15 avril 2026

- Lancement de la [version Preview de Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=fr), notre modèle de synthèse vocale économique, expressif et orientable. Pour en savoir plus, consultez la documentation [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).

## 14 avril 2026

- Sortie de `gemini-robotics-er-1.6-preview`, notre modèle de robotique mis à jour.
  Il dispose désormais de nouvelles fonctionnalités, comme la lecture d'instruments et des capacités de raisonnement spatial et physique améliorées. Pour en savoir plus, consultez la page [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) et le [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=fr).
- Annonce d'arrêt : le modèle `gemini-robotics-er-1.5-preview` sera [mis hors service](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 30 avril 2026 à 9h (heure du Pacifique).

## 2 avril 2026

- Sorti le `gemma-4-26b-a4b-it` et le `gemma-4-31b-it`, disponible sur [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=fr).

## 1er avril 2026

- Nous avons lancé les nouveaux niveaux d'inférence [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr) et [Priorité](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr), qui offrent plus d'options pour optimiser les coûts ou la latence.

## 31 mars 2026

- Lancement de la version Preview de Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=fr), notre modèle de [génération de vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr) le plus économique, conçu pour une itération rapide et la création d'applications à fort volume.
- Le modèle `gemini-2.5-flash-lite-preview-09-2025` a été arrêté. Utilisez plutôt [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=fr).

## 26 mars 2026

- Sorti le [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=fr), il s'agit du dernier modèle audio-to-audio (A2A) conçu pour les applications d'IA axées sur la voix et le dialogue en temps réel. Pour commencer, consultez la documentation de l'[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr).

## 25 mars 2026

- Lancement des modèles de génération de musique [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) : [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=fr) (extraits de 30 secondes) et [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=fr) (titres complets). Les deux modèles acceptent les entrées de texte et d'image, et génèrent un son stéréo de haute qualité à 48 kHz. Pour en savoir plus et obtenir des exemples de code, consultez le guide [Génération de musique](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr).

## 23 mars 2026

- Déploiement des [forfaits de facturation prépayés et postpayés](https://ai.google.dev/gemini-api/docs/billing?hl=fr) dans AI Studio. Les comptes existants peuvent être concernés. Pour en savoir plus, consultez la documentation sur la [facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr).

## 18 mars 2026

- Lancement de la nouvelle fonctionnalité [Combinaison d'outils intégrés et d'appels de fonction](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr), qui permet d'utiliser les outils intégrés de Gemini en même temps que les outils d'appel de fonction personnalisés dans un seul appel d'API.
- L'[ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr#supported_models) est désormais compatible avec les modèles Gemini 3.

## 16 mars 2026

- Nous avons repensé les [niveaux d'utilisation](https://ai.google.dev/gemini-api/docs/billing?hl=fr#about-billing) et les [plafonds de dépenses des comptes de facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr#tier-spend-caps) pour améliorer l'expérience utilisateur en matière de facturation.

## 12 mars 2026

- Ajout de [plafonds de dépenses au niveau du projet](https://ai.google.dev/gemini-api/docs/billing?hl=fr#project-spend-caps) à la facturation dans AI Studio.

## 10 mars 2026

- Sortie de `gemini-embedding-2-preview`, notre premier modèle d'embedding multimodal.
  Il accepte les entrées de texte, d'image, de vidéo, d'audio et de PDF, en mappant toutes les modalités dans un espace d'embedding unifié. Pour en savoir plus, consultez [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr).
- Annonce d'abandon : le modèle `gemini-2.5-flash-lite-preview-09-2025` sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 31 mars 2026.

## 9 mars 2026

- Le modèle Gemini 3 Pro Preview a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr). `gemini-3-pro-preview` pointe désormais vers [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr).

## 3 mars 2026

- Lancement de la version Preview de Gemini 3.1 Flash-Lite, le premier modèle Flash-Lite de la série Gemini 3. Consultez la [page du modèle](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=fr) pour connaître les spécifications, les mises à jour spécifiques et les conseils pour les développeurs.

## 26 février 2026

- Lancement de Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=fr), un modèle à haute efficacité optimisé pour la vitesse et les cas d'utilisation à volume élevé.
- Annonce d'arrêt : la preview de Gemini 3 Pro (`gemini-3-pro-preview`) sera [arrêtée](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 9 mars 2026.

## 19 février 2026

- Lancement de [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr), notre dernière itération de la nouvelle famille Gemini 3.
- Lancement d'un point de terminaison distinct `gemini-3.1-pro-preview-customtools`, qui est plus efficace pour hiérarchiser les outils personnalisés, pour les utilisateurs qui créent des applications avec un mélange de bash et d'outils.

## 18 février 2026

- Annonce d'arrêt : les modèles suivants seront [mis hors service](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 1er juin 2026 :

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 février 2026

- Les modèles suivants sont [éteints](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) :

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 janvier 2026

- Ajout de la compatibilité avec l'outil d'utilisation de l'ordinateur dans `gemini-3-pro-preview` et `gemini-3-flash-preview`.

## 21 janvier 2026

- Modification des alias de `latest` :

  - `gemini-pro-latest` est passé à `gemini-3-pro-preview`
  - `gemini-flash-latest` est passé à `gemini-3-flash-preview`

## 15 janvier 2026

- Annonce d'abandon : les modèles suivants seront [arrêtés](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 17 février 2026 :

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Le modèle `gemini-2.5-flash-image-preview` a été arrêté.

## 14 janvier 2026

- Le modèle `text-embedding-004` a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

## 13 janvier 2026

- Ajout de résolutions de sortie 4K pour [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr) et prise en charge améliorée des vidéos au format portrait dans toutes les résolutions.

## 12 janvier 2026

- Lancement de la fonctionnalité de cycle de vie des modèles. Certains modèles spécifieront désormais l'étape du cycle de vie et le calendrier d'abandon. Pour en savoir plus, consultez la documentation suivante :

  - [Étapes du modèle](https://ai.google.dev/api/generate-content?hl=fr#ModelStatus)

## 8 janvier 2026

- Prise en charge des buckets Cloud Storage et de toute URL pré-signée de base de données publique et privée en tant que source d'entrée de données pour l'API Gemini. La taille limite des fichiers est également passée de 20 Mo à 100 Mo. Pour en savoir plus, consultez le [guide sur les méthodes de saisie de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

## 19 décembre 2025

- Modification destructive apportée à la version bêta publique de l'API Interactions dans la version v1beta. Le champ `total_reasoning_tokens` a été renommé `total_thought_tokens` pour mieux correspondre au concept de "pensées" dans les modèles de réflexion.

## 17 décembre 2025

- Lancement de la preview Gemini 3 Flash, `gemini-3-flash-preview`, qui offre des performances rapides de pointe comparables à celles de modèles plus grands, pour un coût bien inférieur. Avec des capacités de raisonnement visuel et spatial améliorées, et des fonctionnalités de codage agentique. Consultez la documentation sur certaines nouvelles fonctionnalités, y compris :

  - [Réponses de fonctions multimodales](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#multimodal)
  - [Exécution de code avec des images](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#images)

## 12 décembre 2025

- Sortie de `gemini-2.5-flash-native-audio-preview-12-2025`, un nouveau modèle audio natif pour l'API Live. Cette mise à jour améliore la capacité du modèle à gérer les workflows complexes. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr) et [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=fr).

## 11 décembre 2025

- Lancement de l'API Interactions en version bêta. Cette API fournit une interface unifiée pour interagir avec les modèles et les agents Gemini. Pour en savoir plus, consultez le guide de l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr).
- Lancement de l'agent Gemini Deep Research en preview. Il peut planifier, exécuter et synthétiser de manière autonome les résultats des tâches de recherche en plusieurs étapes. Pour en savoir plus, consultez le guide [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr).

## 10 décembre 2025

- Nous avons lancé des améliorations pour nos [modèles de synthèse vocale](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr), Gemini 2.5 Flash TTS (aperçu, optimisé pour une faible latence) et Gemini 2.5 Pro TTS (aperçu, optimisé pour la qualité), y compris une expressivité améliorée, un rythme précis et un dialogue fluide.

## 9 Décembre 2025

- Les modèles d'API Gemini Live suivants sont désormais arrêtés :
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 décembre 2025

- La facturation de Gemini 3 pour l'[ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) commencera le 5 janvier 2026.

## 4 décembre 2025

- Annonce d'arrêt : le modèle `gemini-2.5-flash-image-preview` sera arrêté le 15 janvier 2026.

## 3 décembre 2025

- Annonce d'arrêt : le modèle `text-embedding-004` sera mis hors service le 14 janvier 2026.

## 20 novembre 2025

- Sortie de la version Preview de Gemini 3 Pro Image, `gemini-3-pro-image-preview`, la prochaine itération du modèle Nano Banana. Pour en savoir plus, consultez la page [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

## 18 Novembre 2025

- Lancement du premier modèle de la série Gemini 3, `gemini-3-pro-preview`, notre modèle de compréhension multimodale et de raisonnement de pointe, doté de puissantes capacités de codage et agentiques.

  En plus d'améliorer l'intelligence et les performances, l'aperçu de Gemini 3 Pro introduit de nouveaux comportements concernant :

  - [Résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr)
  - [Signatures de pensée](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr)
  - [Niveaux de réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#thinking-levels)

  Consultez le [Guide du développeur Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=fr) pour en savoir plus sur la migration, les nouvelles fonctionnalités et les spécifications.

## 11 novembre 2025

- Annonce d'arrêt : les modèles suivants seront arrêtés :

  - 12 novembre :

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 novembre :

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 novembre 2025

- Le modèle suivant est arrêté :

  - `imagen-3.0-generate-002`

  Utilisez plutôt [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=fr#imagen-4). Pour en savoir plus, consultez le [tableau sur l'arrêt des fonctionnalités Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

## 6 novembre 2025

- Nous avons lancé l'API File Search en version Preview publique, ce qui permet aux développeurs d'ancrer les réponses dans leurs propres données. Pour en savoir plus, consultez la nouvelle page [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

## November 4, 2025

- Pour [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr), le nombre de jetons d'entrée pour les images a été réduit de 1 290 à 258, ce qui diminue le coût de la retouche d'images.
- Annonce d'arrêt : les modèles suivants seront arrêtés :

  - 18 novembre :

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 décembre :

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 décembre :

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 octobre 2025

- Lancement du nouvel outil [journalisation et ensembles de données](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr) pour l'API Gemini.

## 20 octobre 2025

- Les modèles d'API Gemini Live suivants sont désormais arrêtés :

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Vous pouvez utiliser `gemini-2.5-flash-native-audio-preview-09-2025` à la place.
- Annonce d'arrêt : `gemini-2.0-flash-live-001` et `gemini-live-2.5-flash-preview` seront arrêtés le 9 décembre 2025.

## 17 octobre 2025

- L'**ancrage avec Google Maps** est désormais en phase de disponibilité générale. Pour en savoir plus, consultez la documentation [Ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr).

## 15 octobre 2025

- Publication des modèles [Veo 3.1 et 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=fr#veo-3.1) en version Preview publique, avec de nouvelles fonctionnalités, y compris :

  - Prolonger les vidéos créées par Veo
  - Faire référence à un maximum de trois images pour générer une vidéo.
  - Fournir les images de la première et de la dernière image pour générer des vidéos

  Nous avons également ajouté des options de durée pour les vidéos générées par Veo 3 : 4, 6 et 8 secondes.
- Annonce d'arrêt : `veo-3.0-generate-preview` et `veo-3.0-fast-generate-preview` seront arrêtés le 12 novembre 2025.

## 7 octobre 2025

- Lancement de la [version Preview de Gemini 2.5 Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)

## 2 octobre 2025

- Lancement de Gemini 2.5 Flash Image en disponibilité générale : [Génération d'images avec Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)

## 29 septembre 2025

- Les modèles Gemini 1.5 suivants sont désormais arrêtés :
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 septembre 2025

- Sortie du modèle Gemini Robotics-ER 1.5 en preview. Consultez la [présentation de la robotique](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) pour découvrir comment utiliser le modèle pour votre application de robotique.
- Lancement des modèles d'aperçu suivants :

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Pour en savoir plus, consultez la page [Modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).

## 23 septembre 2025

- Sortie de `gemini-2.5-flash-native-audio-preview-09-2025`, un nouveau modèle audio natif pour l'API Live avec une gestion améliorée de l'appel de fonction et de la coupure de la parole. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr) et [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-native-audio).

## 16 septembre 2025

- Annonce d'arrêt : les modèles suivants seront arrêtés en octobre 2025 :

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Pour en savoir plus sur le dernier modèle d'embedding, consultez la page [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr).

## 10 septembre 2025

- Ajout de la compatibilité avec le [modèle Embeddings dans l'API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr#batch-embedding) et de l'API Batch à la [bibliothèque de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr#batch) pour faciliter encore plus la prise en main des requêtes par lot.

## 9 septembre 2025

- Lancement de Veo 3 et Veo 3 Fast en disponibilité générale, avec des prix plus bas et de nouvelles options pour les formats, la résolution et le seeding. Pour en savoir plus, consultez la [documentation Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr#model-features).

## 26 août 2025

- Lancement de [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-image-preview), notre dernier modèle de génération d'images natif.

## 18 août 2025

- L'[outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) est désormais disponible en disponibilité générale. Il permet de fournir des URL comme contexte supplémentaire aux requêtes. L'assistance pour l'utilisation du contexte d'URL avec le modèle `gemini-2.0-flash` (disponible en version expérimentale) sera interrompue dans une semaine.

## 14 août 2025

- Les modèles Imagen 4 Ultra, Standard et Fast sont désormais en disponibilité générale (DG). Pour en savoir plus, consultez la page [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=fr).

## 7 août 2025

- Le paramètre `allow_adult` de la génération d'images en vidéos est désormais disponible dans les régions soumises à des restrictions. Pour en savoir plus, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=fr#veo-model-parameters).

## 31 juillet 2025

- Lancement de la génération de vidéos à partir d'images pour le modèle Veo 3 (preview).
- Publication du modèle Veo 3 Fast Preview.
- Pour en savoir plus sur Veo 3, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).

## 22 juillet 2025

- Sortie de `gemini-2.5-flash-lite`, notre modèle Gemini 2.5 rapide, économique et performant. Pour en savoir plus, consultez [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-lite).

## July 17, 2025

- Lancement de `veo-3.0-generate-preview`, la dernière mise à jour de Veo qui permet de générer des vidéos avec de l'audio. Pour en savoir plus sur Veo 3, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Augmentation des limites de débit pour Imagen 4 Standard et Ultra. Pour en savoir plus, consultez la page [Limites de fréquence](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr).

## 14 juillet 2025

- Sortie de `gemini-embedding-001`, la version stable de notre modèle d'embedding textuel. Pour en savoir plus, consultez [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr). Le modèle `gemini-embedding-exp-03-07`
  sera obsolète le 14 août 2025.

## 7 juillet 2025

- Lancement du mode par lot de l'API Gemini. Regroupez les requêtes et envoyez-les pour traitement asynchrone. Pour en savoir plus, consultez [Mode Batch](https://ai.google.dev/gemini-api/docs/batch-mode?hl=fr).

## 26 juin 2025

- Les modèles preview `gemini-2.5-pro-preview-05-06` et `gemini-2.5-pro-preview-03-25` redirigent désormais vers la dernière version stable `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` est éteint.

## 24 juin 2025

- Lancement des modèles Imagen 4 Ultra et Standard en preview. Pour en savoir plus, consultez la page [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

## 17 juin 2025

- Sortie le `gemini-2.5-pro`, la version stable de notre modèle le plus puissant, désormais doté d'une capacité de réflexion adaptative. Pour en savoir plus, consultez [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr). `gemini-2.5-pro-preview-05-06` sera redirigé vers `gemini-2.5-pro` le 26 juin 2025.
- Sortie de `gemini-2.5-flash`, notre premier modèle 2.5 Flash stable. Pour en savoir plus, consultez [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` sera obsolète le 15 juillet 2025.
- Lancement de `gemini-2.5-flash-lite-preview-06-17`, un modèle Gemini 2.5 à faible coût et hautes performances. Pour en savoir plus, consultez [Aperçu de Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-lite).

## 5 juin 2025

- Nous avons lancé `gemini-2.5-pro-preview-06-05`, une nouvelle version de notre modèle le plus puissant, désormais doté d'une capacité de réflexion adaptative. Pour en savoir plus, consultez [Preview de Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-06-05) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).
  `gemini-2.5-pro-preview-05-06` sera redirigé vers `gemini-2.5-pro` le 26 juin 2025.

## 27 mai 2025

- Le dernier modèle d'affinage disponible, Gemini 1.5 Flash 001, a été arrêté.
  Le réglage n'est plus disponible pour aucun modèle.
  Consultez [Affiner avec l'API Gemini](https://ai.google.dev/gemini-api/docs/model-tuning?hl=fr).

## 20 mai 2025

**Mises à jour de l'API :**

- Ajout de la prise en charge du [prétraitement vidéo personnalisé](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#customize-video-processing) à l'aide d'intervalles de découpage et d'un échantillonnage de la fréquence d'images configurable.
- Lancement de l'utilisation de plusieurs outils, qui permet de configurer l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et l'[ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) dans la même requête `generateContent`.
- Prise en charge des [appels de fonction asynchrones](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr#async-function-calling) dans l'API Live.
- Lancement d'un [outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) expérimental permettant de fournir des URL comme contexte supplémentaire aux requêtes.

**Mises à jour des modèles** :

- Sortie de `gemini-2.5-flash-preview-05-20`, un modèle [preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions) Gemini optimisé pour le rapport prix/performances et la pensée adaptative. Pour en savoir plus, consultez [Aperçu de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).
- Sortie des modèles [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-tts) et [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview-tts), qui sont capables de [générer de la parole](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr) avec un ou deux locuteurs.
- Sortie du modèle `lyria-realtime-exp`, qui [génère de la musique](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) en temps réel.
- Sortie de `gemini-2.5-flash-preview-native-audio-dialog` et `gemini-2.5-flash-exp-native-audio-thinking-dialog`, nouveaux modèles Gemini pour l'API Live avec des fonctionnalités de sortie audio native. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#native-audio-output) et [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-native-audio).
- Version Preview `gemma-3n-e4b-it` disponible dans [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=fr).

## 7 mai 2025

- Sortie de `gemini-2.0-flash-preview-image-generation`, un modèle en aperçu pour générer et modifier des images. Pour en savoir plus, consultez [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) et [Génération d'images avec Gemini 2.0 Flash (preview)](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.0-flash-preview-image-generation).

## 6 mai 2025

- Nous avons lancé `gemini-2.5-pro-preview-05-06`, une nouvelle version de notre modèle le plus puissant, avec des améliorations concernant le code et les appels de fonction. `gemini-2.5-pro-preview-03-25` pointera automatiquement vers la nouvelle version du modèle.

## 17 avril 2025

- Sortie de `gemini-2.5-flash-preview-04-17`, un modèle [preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions) Gemini optimisé pour le rapport prix/performances et la pensée adaptative. Pour en savoir plus, consultez [Aperçu de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

## 16 avril 2025

- Lancement de la mise en cache du contexte pour [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.0-flash).

## 9 avril 2025

**Mises à jour des modèles** :

- Lancement de `veo-2.0-generate-001`, un modèle de texte et d'image à vidéo en disponibilité générale (DG), capable de générer des vidéos détaillées et artistiquement nuancées. Pour en savoir plus, consultez la [documentation Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Le `gemini-2.0-flash-live-001`, une version Preview publique du modèle [Live API](https://ai.google.dev/gemini-api/docs/live?hl=fr) avec la facturation activée a été publiée.

  - **Gestion et fiabilité des sessions améliorées**

    - **Reprise de session** : permet de maintenir les sessions actives en cas de perturbations temporaires du réseau. L'API est désormais compatible avec le stockage de l'état de la session côté serveur (pendant 24 heures maximum) et fournit des identifiants (session\_resumption) pour se reconnecter et reprendre là où vous vous étiez arrêté.
    - **Sessions plus longues grâce à la compression du contexte** : permet des interactions plus longues que les limites de temps précédentes. Configurez la compression de la fenêtre de contexte avec un mécanisme de fenêtre glissante pour gérer automatiquement la longueur de contexte, ce qui évite les arrêts brusques dus aux limites de contexte.
    - **Notification de déconnexion progressive** : recevez un message du serveur `GoAway` indiquant quand une connexion est sur le point d'être fermée, ce qui permet une gestion progressive avant la fin de la connexion.
  - **Plus de contrôle sur la dynamique des interactions**
  - **Détection d'activité vocale (VAD) configurable** : choisissez des niveaux de sensibilité ou désactivez complètement la VAD automatique et utilisez de nouveaux événements client (`activityStart`, `activityEnd`) pour le contrôle manuel du tour de parole.
  - **Gestion configurable des interruptions** : décidez si l'entrée utilisateur doit interrompre la réponse du modèle.
  - **Couverture de tour configurable** : choisissez si l'API traite toutes les entrées audio et vidéo en continu ou ne les capture que lorsque l'utilisateur final est détecté en train de parler.
  - **Résolution média configurable** : optimisez la qualité ou l'utilisation de jetons en sélectionnant la résolution des médias d'entrée.
  - **Des fonctionnalités et des résultats plus riches**
  - **Options vocales et linguistiques étendues** : choisissez parmi deux nouvelles voix et 30 nouvelles langues pour la sortie audio. La langue de sortie est désormais configurable dans `speechConfig`.
  - **Streaming de texte** : recevez les réponses textuelles de manière incrémentielle au fur et à mesure de leur génération, ce qui permet de les afficher plus rapidement à l'utilisateur.
  - **Rapports sur l'utilisation des jetons** : obtenez des insights sur l'utilisation grâce à des décomptes détaillés des jetons fournis dans le champ `usageMetadata` des messages du serveur, ventilés par modalité et par phase de requête ou de réponse.

## 4 avril 2025

- Publication de la version Preview publique de Gemini 2.5 Pro, `gemini-2.5-pro-preview-03-25`, avec la facturation activée. Vous pouvez continuer à utiliser `gemini-2.5-pro-exp-03-25` avec le forfait sans frais.

## 25 mars 2025

- Sortie de `gemini-2.5-pro-exp-03-25`, un modèle Gemini expérimental public avec le mode Pensée toujours activé par défaut.
  Pour en savoir plus, consultez [Gemini 2.5 Pro (expérimental)](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-03-25).

## 12 mars 2025

**Mises à jour des modèles** :

- Lancement d'un modèle expérimental [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#gemini) capable de générer et de retoucher des images.
- Sorti le `gemma-3-27b-it`, disponible sur [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=fr).

**Mises à jour de l'API :**

- Ajout de la compatibilité avec les [URL YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=fr#youtube) en tant que source multimédia.
- Ajout de la possibilité d'inclure une [vidéo intégrée](https://ai.google.dev/gemini-api/docs/vision?hl=fr#inline-video) de moins de 20 Mo.

## 11 mars 2025

**Mises à jour du SDK :**

- Publication de la [version Preview publique du SDK Google Gen AI pour TypeScript et JavaScript](https://googleapis.github.io/js-genai).

## 7 mars 2025

**Mises à jour des modèles** :

- Publication `gemini-embedding-exp-03-07` d'un modèle d'embeddings [expérimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=fr) basé sur Gemini en version Preview publique.

## 28 février 2025

**Mises à jour de l'API :**

- Ajout de la compatibilité avec la [recherche en tant qu'outil](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) à `gemini-2.0-pro-exp-02-05`, un modèle expérimental basé sur Gemini 2.0 Pro.

## 25 février 2025

**Mises à jour des modèles** :

- Sortie de la version en disponibilité générale (DG) de [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash-lite), optimisée pour la vitesse, l'évolutivité et la rentabilité.`gemini-2.0-flash-lite`

## 19 février 2025

**Nouveautés d'AI Studio** :

- Prise en charge de [régions supplémentaires](https://ai.google.dev/gemini-api/docs/available-regions?hl=fr) (Kosovo, Groenland et Îles Féroé).

**Mises à jour de l'API :**

- Prise en charge de [régions supplémentaires](https://ai.google.dev/gemini-api/docs/available-regions?hl=fr) (Kosovo, Groenland et Îles Féroé).

## 18 février 2025

**Mises à jour des modèles** :

- Gemini 1.0 Pro n'est plus disponible. Pour obtenir la liste des modèles compatibles, consultez [Modèles Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr).

## 11 février 2025

**Mises à jour de l'API :**

- Mises à jour concernant la [compatibilité des bibliothèques OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

## 6 février 2025

**Mises à jour des modèles** :

- Sortie de la version en disponibilité générale (DG) d'[Imagen 3 dans l'API Gemini](https://ai.google.dev/gemini-api/docs/imagen?hl=fr) le `imagen-3.0-generate-002`.

**Mises à jour du SDK :**

- Publication du [SDK Google Gen AI pour Java](https://github.com/googleapis/java-genai) en version Preview publique.

## 5 février 2025

**Mises à jour des modèles** :

- Nous avons lancé `gemini-2.0-flash-001`, une version en disponibilité générale (DG) de [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash) qui n'accepte que les sorties textuelles.
- Version publique [expérimentale](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=fr) de Gemini 2.0 Pro publiée le `gemini-2.0-pro-exp-02-05`.
- Sortie de `gemini-2.0-flash-lite-preview-02-05`, un [modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash-lite) expérimental en aperçu public optimisé pour la rentabilité.

**Mises à jour de l'API :**

- Ajout de la prise en charge de l'[entrée de fichier et de la sortie de graphique](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#input-output) à l'exécution de code.

**Mises à jour du SDK :**

- Le [SDK Google Gen AI pour Python](https://googleapis.github.io/python-genai/) est désormais disponible en disponibilité générale (DG).

## 21 janvier 2025

**Mises à jour des modèles** :

- Sortie le `gemini-2.0-flash-thinking-exp-01-21`, dernière version Preview du modèle qui alimente le [modèle Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

## 19 décembre 2024

**Mises à jour des modèles** :

- Lancement du mode Gemini 2.0 Flash Thinking en version Preview publique. Le mode Réflexion est un modèle de calcul au moment du test qui vous permet de voir le processus de réflexion du modèle lorsqu'il génère une réponse. Il produit des réponses avec de meilleures capacités de raisonnement.

  Pour en savoir plus sur le modèle Gemini 2.0 Flash Thinking, consultez notre [page de présentation](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=fr).

## 11 décembre 2024

**Mises à jour des modèles** :

- Lancement de [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash) en version Preview publique. Voici une liste partielle des fonctionnalités de Gemini 2.0 Flash Experimental :
  - Deux fois plus rapide que Gemini 1.5 Pro
  - Streaming bidirectionnel avec notre API Live
  - Génération de réponses multimodales sous forme de texte, d'images et de parole
  - Utilisation d'outils intégrés avec un raisonnement multitour pour utiliser des fonctionnalités telles que l'exécution de code, la recherche, l'appel de fonction, etc.

Pour en savoir plus sur Gemini 2.0 Flash, consultez notre [page de présentation](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=fr).

## 21 novembre 2024

**Mises à jour des modèles** :

- Sortie de `gemini-exp-1121`, un modèle d'API Gemini expérimental encore plus puissant.

**Mises à jour des modèles** :

- Mise à jour des alias de modèle `gemini-1.5-flash-latest` et `gemini-1.5-flash` pour utiliser `gemini-1.5-flash-002`.
  - Modification du paramètre `top_k` : le modèle `gemini-1.5-flash-002` accepte les valeurs `top_k` comprises entre 1 et 41 (exclus).
    Les valeurs supérieures à 40 seront remplacées par 40.

## 14 novembre 2024

**Mises à jour des modèles** :

- Sortie de `gemini-exp-1114`, un modèle d'API Gemini expérimental et puissant.

## 8 novembre 2024

**Mises à jour de l'API :**

- Ajout de la [prise en charge de Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=fr) dans les bibliothèques OpenAI et l'API REST.

## 31 octobre 2024

**Mises à jour de l'API :**

- Ajout de la [compatibilité avec l'ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/grounding?hl=fr).

## 3 octobre 2024

**Mises à jour des modèles** :

- Sortie de `gemini-1.5-flash-8b-001`, une version stable de notre plus petit modèle d'API Gemini.

## 24 septembre 2024

**Mises à jour des modèles** :

- Sortie des versions stables `gemini-1.5-pro-002` et `gemini-1.5-flash-002` de Gemini 1.5 Pro et 1.5 Flash, désormais disponibles en disponibilité générale.
- Mise à jour du code du modèle `gemini-1.5-pro-latest` pour utiliser `gemini-1.5-pro-002` et du code du modèle `gemini-1.5-flash-latest` pour utiliser `gemini-1.5-flash-002`.
- `gemini-1.5-flash-8b-exp-0924` a été publié pour remplacer `gemini-1.5-flash-8b-exp-0827`.
- Ajout du [filtre de sécurité pour l'intégrité civique](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr#safety-filters) pour l'API Gemini et AI Studio.
- Ajout de la compatibilité avec deux nouveaux paramètres pour Gemini 1.5 Pro et 1.5 Flash dans Python et NodeJS : [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=fr#FIELDS.frequency_penalty) et [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=fr#FIELDS.presence_penalty).

## 19 septembre 2024

**Nouveautés d'AI Studio** :

- Ajout de boutons "J'aime" et "Je n'aime pas" aux réponses du modèle pour permettre aux utilisateurs de donner leur avis sur la qualité d'une réponse.

**Mises à jour de l'API :**

- Ajout de la compatibilité avec les crédits Google Cloud, qui peuvent désormais être utilisés pour l'utilisation de l'API Gemini.

## 17 septembre 2024

**Nouveautés d'AI Studio** :

- Ajout d'un bouton **Ouvrir dans Colab** qui exporte une requête (et le code permettant de l'exécuter) vers un notebook Colab. Cette fonctionnalité n'est pas encore compatible avec les requêtes utilisant des outils (mode JSON, appel de fonction ou exécution de code).

## 13 septembre 2024

**Nouveautés d'AI Studio** :

- Ajout de la compatibilité avec le mode Comparaison, qui vous permet de comparer les réponses de différents modèles et requêtes pour trouver la solution la mieux adaptée à votre cas d'utilisation.

## 30 août 2024

**Mises à jour des modèles** :

- Gemini 1.5 Flash permet de [fournir un schéma JSON via la configuration du modèle](https://ai.google.dev/gemini-api/docs/json-mode?hl=fr#supply-schema-in-config).

## 27 août 2024

**Mises à jour des modèles** :

- Sortie des [modèles expérimentaux](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=fr) suivants :
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 août 2024

**Mises à jour de l'API :**

- Ajout de la prise en charge du [traitement des PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr).

## 5 août 2024

**Mises à jour des modèles** :

- L'optimisation est désormais disponible pour Gemini 1.5 Flash.

## 1er août 2024

**Mises à jour des modèles** :

- Sortie le `gemini-1.5-pro-exp-0801`, une nouvelle version expérimentale de [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro).

## 12 juillet 2024

**Mises à jour des modèles** :

- La prise en charge de Gemini 1.0 Pro Vision a été supprimée des services et outils Google AI.

## 27 juin 2024

**Mises à jour des modèles** :

- Disponibilité générale de la fenêtre de contexte de deux millions de jetons de Gemini 1.5 Pro.

**Mises à jour de l'API :**

- Ajout de la compatibilité avec l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr).

## 18 juin 2024

**Mises à jour de l'API :**

- Ajout de la compatibilité avec la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr).

## 12 juin 2024

**Mises à jour des modèles** :

- Gemini 1.0 Pro Vision est obsolète.

## 23 mai 2024

**Mises à jour des modèles** :

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro) (`gemini-1.5-pro-001`) est en disponibilité générale.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-flash) (`gemini-1.5-flash-001`) est disponible pour tous les utilisateurs.

## 14 mai 2024

**Mises à jour de l'API :**

- Nous avons lancé une fenêtre de contexte de deux millions de jetons pour Gemini 1.5 Pro (liste d'attente).
- Nous avons lancé la [facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr) au paiement à l'usage pour Gemini 1.0 Pro. La facturation pour Gemini 1.5 Pro et Gemini 1.5 Flash sera bientôt disponible.
- Augmentation des limites de débit pour le prochain niveau payant de Gemini 1.5 Pro.
- Ajout de la prise en charge vidéo intégrée à l'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=fr).
- Ajout de la prise en charge du texte brut à l'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=fr).
- Ajout de la prise en charge de l'appel de fonction parallèle, qui renvoie plusieurs appels à la fois.

## 10 mai 2024

**Mises à jour des modèles** :

- Sortie de [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-flash) (`gemini-1.5-flash-latest`) en preview.

## 09 avril 2024

**Mises à jour des modèles** :

- Sortie de [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro) (`gemini-1.5-pro-latest`) en preview.
- Lancement d'un nouveau modèle d'embedding textuel, `text-embeddings-004`, qui est compatible avec les tailles d'[embedding élastique](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr#elastic-embedding) inférieures à 768.

**Mises à jour de l'API :**

- L'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=fr) a été publiée pour stocker temporairement les fichiers multimédias à utiliser dans les requêtes.
- Ajout de la prise en charge des requêtes avec des données textuelles, d'image et audio, également appelées requêtes *multimodales*. Pour en savoir plus, consultez [Utiliser des éléments multimédias dans les requêtes](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=fr).
- Lancement des [instructions système](https://ai.google.dev/gemini-api/docs/system-instructions?hl=fr) en version bêta.
- Ajout du [mode d'appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#function_calling_mode), qui définit le comportement d'exécution pour l'appel de fonction.
- Ajout de la compatibilité avec l'option de configuration `response_mime_type`, qui vous permet de demander des réponses au [format JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=fr#json).

## 19 mars 2024

**Mises à jour des modèles** :

- Ajout de la prise en charge du [réglage de Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) dans Google AI Studio ou avec l'API Gemini.

## 13 décembre 2023

**Mises à jour des modèles** :

- gemini-pro : nouveau modèle de texte pour une grande variété de tâches. Équilibre entre capacité et efficacité.
- gemini-pro-vision : nouveau modèle multimodal pour un large éventail de tâches.
  Équilibre entre capacité et efficacité.
- embedding-001 : nouveau modèle d'embedding.
- aqa : nouveau modèle spécialement adapté et entraîné pour répondre aux questions à l'aide de passages de texte permettant d'ancrer les réponses générées.

Pour en savoir plus, consultez [Modèles Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr).

**Mises à jour des versions de l'API :**

- v1 : canal d'API stable.
- v1beta : version bêta. Cette chaîne propose des fonctionnalités qui peuvent être en cours de développement.

Pour en savoir plus, consultez la section [Versions de l'API](https://ai.google.dev/gemini-api/docs/api-versions?hl=fr).

**Mises à jour de l'API :**

- `GenerateContent` est un point de terminaison unifié unique pour le chat et le texte.
- L'insertion de données en flux continu est disponible avec la méthode `StreamGenerateContent`.
- Fonctionnalité multimodale : l'image est une nouvelle modalité acceptée
- Nouvelles fonctionnalités bêta :
  - [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
  - [Récupérateur sémantique](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=fr)
  - Attributed Question Answering (AQA)
- Nombre de candidats mis à jour : les modèles Gemini ne renvoient qu'un seul candidat.
- Différentes catégories de paramètres de sécurité et de classification de sécurité. Pour en savoir plus, consultez [Paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr).
- L'ajustement des modèles n'est pas encore disponible pour les modèles Gemini (en cours de développement).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/28 (UTC)."],[],[]]
