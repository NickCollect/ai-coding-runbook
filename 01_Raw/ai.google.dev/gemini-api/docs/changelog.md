---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=fr
fetched_at: 2026-10-12T07:06:40.380815+00:00
title: "Notes de version \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Notes de version

Cette page décrit les mises à jour apportées à l'API Gemini.

## 8 octobre 2026

- **Obsolescence de Gemini 3.7 Flash** :
  [`gemini-3.7-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.7?hl=fr) est obsolète
  et a été remplacé par [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr).
  Toutes les demandes adressées à `gemini-3.7-flash` sont automatiquement redirigées vers `gemini-3.8-flash`. Mettez à jour votre chaîne de modèle sur `gemini-3.8-flash` et consultez le [guide Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr).
- **Obsolescence de Gemini 3.5 Flash** :
  [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=fr) est obsolète et a été remplacé par [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=fr).
  Toutes les demandes adressées à `gemini-3.5-flash` sont automatiquement redirigées vers `gemini-3.6-flash`. Mettez à jour votre chaîne de modèle sur `gemini-3.6-flash` (ou [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr)) et consultez le [guide Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=fr).
- **Arrêt de l'agent Deep Research `deep-research-pro-preview-12-2025`** :
  L'agent `deep-research-pro-preview-12-2025` est obsolète et sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr#managed-agents) le **23 octobre 2026**.

  Migrez vos requêtes vers l'une des versions plus récentes de l'agent [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) :

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=fr) : conçu pour la rapidité et l'efficacité, idéal pour être rediffusé sur une UI client.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=fr) : exhaustivité maximale pour la collecte et la synthèse automatiques du contexte.

  Pour migrer, remplacez le paramètre `agent` dans vos requêtes `interactions.create`
  par `deep-research-pro-preview-12-2025`
  `deep-research-preview-04-2026` (ou `deep-research-max-preview-04-2026`).

## 6 octobre 2026

- **Disponibilité générale de Gemini Nano Banana 2.1** : sortie de [Gemini Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=fr) (`gemini-nano-banana-2.1`), le dernier modèle de génération d'images et de retouche conversationnelle à haute efficacité. Nano Banana 2 ([`gemini-3.1-flash-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=fr)) a été mis à jour. Il conserve la vitesse et la rentabilité de Flash, tout en offrant des améliorations significatives en termes de qualité visuelle, de respect des consignes, de cohérence du personnage multitour, de rendu du texte et de génération de formats panoramiques et larges (`1:4`, `4:1`, `1:8`, `8:1`) pour les résolutions `1K`, `2K` et `4K`.

  Pour commencer, consultez le [guide de génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).
- **Annonce d'abandon** : le modèle `gemini-3.1-flash-image` est abandonné (aucune date d'arrêt n'a été annoncée). Migrez vers [`gemini-nano-banana-2.1`](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=fr).

## 22 septembre 2026

- **Disponibilité générale de Gemini 3.8 Flash TTS et Gemini 3.8 Flash-Lite TTS (DG)** : nous avons lancé nos modèles audio de synthèse vocale (TTS) de nouvelle génération et le point de terminaison API Gemini Voices (`/v1beta/voices`) :

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr)
    (`gemini-3.8-flash-tts`)** : modèle TTS créatif phare conçu pour une fidélité vocale de qualité studio, un jeu d'acteur nuancé, des dialectes régionaux et une stabilité multi-tours de longue durée.
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr)
    (`gemini-3.8-flash-lite-tts`)** : modèle TTS rapide et économique conçu pour remplacer `gemini-3.1-flash-tts-preview` pour la production à haut débit et les cascades d'agents vocaux en temps réel.
  - **[Conception de voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr), [réplication de voix](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fr) et [bibliothèque vocale étendue](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#voice-library)** : créez des personas vocaux personnalisés persistants à partir de requêtes textuelles, répliquez des voix avec vérification du consentement et interrogez plus de 150 voix prédéfinies et personnalisées.

  Pour commencer, consultez le [guide Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).

## 18 septembre 2026

- **Mise à jour de l'accès aux modèles Gemini 2.5** : pour garantir des performances fiables à tous les utilisateurs, nous limitons l'accès aux modèles 2.5 aux utilisateurs qui les ont utilisés activement par le passé. Ces modèles ne sont pas obsolètes et continueront d'être proposés via l'API jusqu'à nouvel ordre. Pour tout nouveau projet, utilisez nos derniers modèles : 3.5 Flash-Lite ou 3.8 Flash. Cela nous aide à maintenir une capacité suffisante pour les workflows anciens en cours et les nouvelles applications.

## 17 septembre 2026

- **Agent Antigravity 09-2026** : `antigravity-preview-09-2026` a été publié, ce qui remplace et abandonne `antigravity-preview-05-2026`.

  Si vous exécutez une sandbox à distance (`environment: "remote"`) et que vous lisez uniquement les étapes `output_text` ou `model_output`, mettez à jour la chaîne de l'agent. Aucune autre modification n'est nécessaire.

  Si vous exécutez des outils en local (`local_environment`) ou analysez les étapes `function_call`, les outils intégrés ont changé. Les paramètres utilisent PascalCase au lieu de snake\_case, et les modifications de fichiers utilisent des remplacements de plages de lignes au lieu de réécritures complètes.

  | Capacité | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | Création de fichiers | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | Modification de fichiers | `write_file(path, content)`, réécriture complète | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | Lecture des fichiers | `read_file(path, offset, limit)`, décalages d'octets | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | Annuaire | `list_files(path)` | `list_dir(DirectoryPath)` |
  | Recherche de fichiers et de code | Aucun, les agents ont utilisé des commandes shell | `find_by_name(SearchDirectory, Pattern, MaxDepth)` et `grep_search(SearchPath, Query, IsRegex)` |
  | Exécution du shell | `code_execution(command, timeout_seconds)` | Non modifié |
  | Recherche sur le Web | `google_search(queries)` | Non modifié |

  Consultez le guide [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr).
  `antigravity-preview-05-2026` sera arrêté le 5 octobre 2026. Vous trouverez plus d'informations sur la page [Obsolète](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr#managed-agents).

## 15 septembre 2026

- **Disponibilité générale de Gemini 3.8 Live et Gemini 3.8 Live Extended Thinking** : deux nouveaux modèles audio-vers-audio ont été lancés pour les applications vocales en temps réel utilisant l'API Live :

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=fr)) : option par défaut pour la plupart des expériences d'agent vocal à faible latence et des dialogues en temps réel sans délai de raisonnement. Il inclut le raisonnement entrelacé, l'appel de fonction asynchrone par défaut et les mises à jour complètes du contenu client de la session.
  - **Gemini 3.8 Live Extended Thinking**
    ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=fr)) : modèle audio-vers-audio à haut niveau de raisonnement qui prend en charge le raisonnement en arrière-plan lors des interactions audio en direct. Il est recommandé lorsque le niveau de raisonnement en arrière-plan doit être plus élevé.

  Pour commencer, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr), le [guide des fonctionnalités](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=fr) et le [guide de réflexion](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=fr).

## 3 septembre 2026

- **Lyria 3.5 en disponibilité générale** : nous avons lancé la nouvelle génération du modèle de génération de musique de Google :

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=fr) : génération de titres complets avec une meilleure cohérence musicale, des voix naturelles et un contrôle précis de la durée et de la structure.

  Le modèle accepte les entrées de texte et d'image, et génère un son stéréo haute fidélité de 44,1 kHz. Pour en savoir plus et obtenir des exemples de code, consultez le guide [Génération de musique](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr).

## 2 septembre 2026

- **Disponibilité générale de Gemini 3.8 Flash** : sortie de `gemini-3.8-flash`, notre modèle Flash le plus intelligent, conçu pour l'ingénierie logicielle à long terme, les agents autonomes et les workflows d'entreprise complexes.

  Pour commencer, consultez la page du modèle [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fr) et le [guide des derniers modèles](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr).

## 1 septembre 2026

- **Compréhension agentique des vidéos** : la compréhension agentique des vidéos est désormais disponible pour Gemini 3.7 Flash, 3.6 Flash et 3.5 Flash-Lite dans les API Interactions et GenerateContent. Le modèle parcourt de manière dynamique les chronologies vidéo, en demandant des transcriptions, des images ou des pistes audio à la demande. Cette approche utilise jusqu'à 88% de jetons en moins pour les contenus longs par rapport au traitement statique.

  Pour commencer, consultez le guide [Compréhension agentique des vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#agentic-video-understanding).

## 27 août 2026

- **Disponibilité générale (DG) de Gemini Omni Flash** : version DG de notre modèle rapide et conversationnel de génération et de montage vidéo, disponible depuis le `gemini-omni-1.1-flash`. Cette version inclut de nouvelles fonctionnalités importantes :

  - **Extension de vidéo** : étendez facilement des vidéos existantes en générant des continuations à la fin d'un extrait à l'aide de la tâche `extend` ou directement avec une requête.
  - **Interpolation (première et dernière images)** : générez une vidéo de transition entre deux images à l'aide de la tâche `image_to_video` avec un maximum de deux images.
  - **Contrôle de la résolution** : le nouveau paramètre `resolution` dans `video_config` est compatible avec les sorties `360p`, `720p` (par défaut), `1080p` et `4k`.
    Les sorties 1080p et 4K sont générées à l'aide du scaling à la hausse.

  Le point de terminaison `gemini-omni-flash-preview` existant sera obsolète le 30 septembre 2026.

  Pour commencer, consultez la page du modèle [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=fr) et le [guide Omni](https://ai.google.dev/gemini-api/docs/omni?hl=fr).

## 26 août 2026

- **Disponibilité générale de Gemini 3.5 Transcribe** : deux modèles de reconnaissance vocale dédiés basés sur la compréhension audio de Gemini ont été lancés :

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`) : transcription non continue de haute précision et à faible latence avec détection de la langue basée sur les énoncés dans plus de 85 langues, identification des locuteurs, codes temporels au niveau des mots et pondération du vocabulaire personnalisé (jusqu'à 1 000 termes).
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`) :
    Transcription vocale en streaming bidirectionnel à faible latence sur WebSockets à l'aide de l'API Live, avec prise en charge des événements de transcription provisoires et définitifs, du mode de transcription intelligente et de plusieurs stratégies de détection d'activité vocale (VAD).

  Pour commencer, consultez le [guide de transcription audio](https://ai.google.dev/gemini-api/docs/transcribe?hl=fr), le [guide de transcription instantanée](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fr) et la [page du modèle Gemini 3.5 Transcribe](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=fr).

## 13 août 2026

- **Disponibilité générale de Gemini 3.7 Flash** : nous avons lancé notre modèle de travail le plus intelligent à ce jour pour le codage et les agents :

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`) : améliorations importantes pour l'ingénierie logicielle, le développement Web et les workflows agentiques, disponibles à un prix découverte jusqu'au 31 décembre 2026.

  Pour commencer, consultez la page du modèle [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=fr) et le [guide des derniers modèles](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr).

## 30 juillet 2026

- **Gemini Robotics ER2 en version bêta publique** : deux nouveaux points de terminaison de modèle de raisonnement ancré ont été publiés pour la robotique :

  - `gemini-robotics-er-2-preview` : raisonnement spatial avancé, exécution de code par l'agent, orchestration d'outils en plusieurs étapes, recherche de moments vidéo, classification de la progression et coordination de plusieurs robots.
  - `gemini-robotics-er-2-streaming-preview` : optimisé pour le streaming de texte en temps réel à l'aide de l'API Live, ce qui permet aux agents robotiques à faible latence d'utiliser des entrées audio et vidéo bidirectionnelles.

  Les deux points de terminaison de modèle acceptent les entrées de texte, d'image, de vidéo et d'audio, et sont compatibles avec les appels de fonction avec un comportement de blocage pour les actions physiques des robots.
  Pour commencer, consultez la [présentation de Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr). Pour les cas d'utilisation de flux en temps réel, consultez [Robotique avec flux](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr).
- **Annonce d'abandon** : le modèle `gemini-robotics-er-1.6-preview` sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 31 août 2026.

## 21 juillet 2026

- **Disponibilité générale de Gemini 3.6 Flash et Gemini 3.5 Flash-Lite** :
  Nous avons publié des versions stables et prêtes pour la production de nos derniers modèles Flash 3.x :

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`) : offre une efficacité améliorée des jetons et des capacités de planification de code/agentique à un prix inférieur à celui de 3.5 Flash, répondant ainsi aux commentaires des développeurs concernant la verbosité des résultats.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`) : option de sous-agent à faible latence et très économique, conçue pour l'automatisation à volume élevé.

  Pour en savoir plus, consultez le guide [Dernier modèle Gemini](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr).
- **Paramètres obsolètes** : les paramètres d'échantillonnage `temperature`, `top_p` et `top_k` sont désormais obsolètes. Pour en savoir plus, consultez [Dernier modèle Gemini](https://ai.google.dev/gemini-api/docs/latest-model?hl=fr#sampling-parameter-deprecation).

## 6 juillet 2026

- Prise en charge des [journaux de développeur](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr) pour l'API Interactions : les journaux des appels d'API Interactions compatibles sont désormais visibles dans le [tableau de bord AI Studio](https://aistudio.google.com/logs?hl=fr).

## 30 juin 2026

- **Gemini Omni Flash en aperçu public** : lancé le `gemini-omni-flash-preview`, ce modèle multimodal haute performance est conçu pour générer des vidéos à grande vitesse et pour la retouche vidéo conversationnelle. L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) vous permet de générer des vidéos de 3 à 10 secondes en 720p à partir de descriptions textuelles ou d'animer des images fixes, puis de modifier et d'affiner les résultats de manière conversationnelle. Pour commencer, consultez le guide [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=fr) et la fiche de modèle [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=fr).
- Mise à disposition générale de `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite), notre modèle multimodal intégré optimisé pour la génération et la retouche d'images à très faible latence et à faible coût. Consultez la fiche du modèle [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=fr) et le guide [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

## 24 juin 2026

- **Utilisation de l'ordinateur** : nous avons lancé la version bêta publique de l'outil [Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr) dans Gemini 3.5 Flash. Cette version inclut des actions simplifiées avec des intents, une prise en charge intégrée des environnements de navigateur, mobile et de bureau, des règles de sécurité configurables et une détection avancée de l'injection de requêtes.

## 17 juin 2026

- **Compatibilité du streaming pour la génération de la parole** : le streaming via `streamGenerateContent` (et `stream: true` dans l'API Interactions) est désormais compatible avec le modèle `gemini-3.1-flash-tts-preview`. Pour en savoir plus, consultez le guide [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#streaming).

## 15 juin 2026

- **Annonce d'abandon** : les modèles de génération d'images suivants sont abandonnés et seront [arrêtés](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le **17 août 2026** :

  - **Modèles Imagen 4 et Gemini 3 Image** :
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  Pour migrer votre code vers des points de terminaison stables ou d'aperçu plus récents, consultez la page [Obsolescences de Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr#imagen-models).
- **Annonce d'abandon** : les modèles de génération de vidéos suivants sont en cours d'abandon et seront [arrêtés](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le **30 juin 2026** :

  - **Modèles Veo** :
    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

  Mettez à jour votre intégration pour utiliser les ID de modèle d'aperçu Veo 3.1 (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) ou les modèles 3.1 GA disponibles sur la [plate-forme Gemini Enterprise Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=fr) afin d'éviter toute interruption de service.
- **Annonce de l'arrêt** : l'outil expérimental GMP Contextual View (interface fixe pour les résultats de l'ancrage avec Google Maps) sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le **15 juin 2026** :

## 1er juin 2026

- Les modèles Gemini 2.0 suivants sont désormais [arrêtés](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) :

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Utilisez plutôt [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) ou
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr).

## 28 mai 2026

- Sortie des versions disponibles dans le commerce (GA) de nos modèles visuels natifs `gemini-3.1-flash-image` (Nano Banana 2) et `gemini-3-pro-image` (Nano Banana Pro), [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=fr) et [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=fr).
- **Prise en charge de la génération d'images à partir de vidéos** : vous pouvez désormais transmettre un fichier vidéo (par importation directe ou sous forme d'URL YouTube publique) en tant que contexte multimodal, en plus d'un prompt textuel, pour générer des miniatures de haute qualité, des affiches de films cinématographiques ou des infographies récapitulatives. Cette fonctionnalité n'est disponible que sur le modèle `gemini-3.1-flash-image`. Pour en savoir plus, consultez le guide [Génération d'images à partir de vidéos](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#video-to-image).
- Annonce d'obsolescence : les modèles `gemini-3.1-flash-image-preview` et `gemini-3-pro-image-preview` sont obsolètes et seront [mis hors service](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 25 juin 2026.

## 25 mai 2026

- Le modèle `gemini-3.1-flash-lite-preview` a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr). Utilisez plutôt [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr).

## 19 mai 2026

- Sortie `gemini-3.5-flash`de la version en disponibilité générale (DG) de [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr), notre modèle le plus intelligent pour des performances de pointe constantes dans les tâches agentiques et de codage. Il s'agit désormais du modèle qui alimente `gemini-flash-latest`.
- Lancement de **Managed Agents dans l'API Gemini** en version Preview publique. Les développeurs peuvent ainsi créer et déployer des agents autonomes avec état qui s'exécutent dans des environnements de bac à sable Linux sécurisés et isolés hébergés par Google. Pour en savoir plus, consultez la page [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) et le [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr).
- L'agent géré **Antigravity Agent** à usage général, [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=fr), est disponible en version Preview publique.
  L'agent Antigravity peut planifier, raisonner, écrire et exécuter du code de manière autonome, gérer des fichiers et naviguer sur le Web dans son conteneur bac à sable. Pour obtenir des exemples de code et des spécifications, consultez le guide [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr).

## 7 mai 2026

- Sortie le `gemini-3.1-flash-lite`, la version en disponibilité générale (DG) de [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) est optimisée pour la rapidité, l'évolutivité et la rentabilité.
- Annonce d'arrêt : le modèle `gemini-3.1-flash-lite-preview` sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 25 mai 2026. Il ne sera plus disponible à partir du 11 mai 2026.

## 6 mai 2026

- **Modification incompatible à venir** : le schéma de requête et de réponse de l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) (`outputs` → `steps`) et la configuration du format de sortie (`response_format`) vont changer. Le nouveau schéma deviendra le schéma par défaut le **26 mai** et l'ancien schéma sera supprimé le **8 juin**.
  Pour en savoir plus, consultez le [guide de migration](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=fr).

## 5 mai 2026

- Mise à jour de la **recherche de fichiers** pour prendre en charge la recherche multimodale. Vous pouvez désormais intégrer des images et les rechercher de manière native à l'aide du modèle `gemini-embedding-2`.
  Les métadonnées d'ancrage incluent désormais `media_id` pour les citations visuelles et `page_numbers` qui indiquent où trouver les informations. Pour en savoir plus, consultez le guide [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

## 4 mai 2026

- Lancement de la prise en charge des [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=fr) basés sur des événements dans l'API Gemini pour remplacer les workflows d'interrogation pour l'API Batch et les opérations de longue durée.

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
  Il dispose désormais de nouvelles capacités, comme la lecture d'instruments et des capacités de raisonnement spatial et physique améliorées. Pour en savoir plus, consultez la page [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) et le [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=fr).
- Annonce d'arrêt : le modèle `gemini-robotics-er-1.5-preview` sera [mis hors service](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 30 avril 2026 à 9h (PST).

## 2 avril 2026

- Sorti le `gemma-4-26b-a4b-it` et le `gemma-4-31b-it`, disponible sur [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=fr).

## 1er avril 2026

- Nous avons lancé les nouveaux niveaux d'inférence [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr) et [Priorité](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr), qui offrent plus d'options pour optimiser les coûts ou la latence.

## 31 mars 2026

- Lancement de l'aperçu de Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=fr), notre modèle de [génération de vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr) le plus économique, conçu pour une itération rapide et la création d'applications à volume élevé.
- Le modèle `gemini-2.5-flash-lite-preview-09-2025` a été arrêté. Utilisez plutôt [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=fr).

## 26 mars 2026

- Sorti le [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=fr), il s'agit du dernier modèle audio à audio (A2A) conçu pour les applications d'IA axées sur la voix et les dialogues en temps réel. Consultez la documentation de l'[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=fr) pour commencer.

## 25 mars 2026

- Lancement des modèles de génération de musique [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) : [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=fr) (extraits de 30 secondes) et [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=fr) (morceaux complets). Les deux modèles acceptent les entrées de texte et d'image, et génèrent un son stéréo de haute qualité à 48 kHz. Pour en savoir plus et obtenir des exemples de code, consultez le guide [Génération de musique](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr).

## 23 mars 2026

- Déploiement des [forfaits avec prépaiement et post-paiement](https://ai.google.dev/gemini-api/docs/billing?hl=fr) dans AI Studio. Les comptes existants peuvent être concernés. Pour en savoir plus, consultez la documentation sur la [facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr).

## 18 mars 2026

- Lancement de la nouvelle fonctionnalité [Combinaison d'outils intégrés et d'appels de fonction](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr), qui permet d'utiliser les outils intégrés de Gemini en même temps que les outils d'appels de fonction personnalisés dans un seul appel d'API.
- L'[ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr#supported_models) est désormais compatible avec les modèles Gemini 3.

## 16 mars 2026

- Nous avons repensé les [niveaux d'utilisation](https://ai.google.dev/gemini-api/docs/billing?hl=fr#about-billing) et les [plafonds de dépenses des comptes de facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr#tier-spend-caps) pour améliorer l'expérience utilisateur en matière de facturation.

## 12 mars 2026

- Nous avons introduit des [plafonds de dépenses au niveau du projet](https://ai.google.dev/gemini-api/docs/billing?hl=fr#project-spend-caps) dans la facturation d'AI Studio.

## 10 mars 2026

- Lancement de `gemini-embedding-2-preview`, notre premier modèle d'embedding multimodal.
  Il accepte les entrées de texte, d'image, de vidéo, d'audio et de PDF, en mappant toutes les modalités dans un espace d'embedding unifié. Pour en savoir plus, consultez [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr).
- Annonce d'abandon : le modèle `gemini-2.5-flash-lite-preview-09-2025` sera [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 31 mars 2026.

## 9 mars 2026

- Le modèle Gemini 3 Pro Preview a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr). `gemini-3-pro-preview` pointe désormais vers [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr).

## 3 mars 2026

- Lancement de la preview Gemini 3.1 Flash-Lite, le premier modèle Flash-Lite de la série Gemini 3. Consultez la [page du modèle](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=fr) pour connaître les caractéristiques, les mises à jour spécifiques et les conseils pour les développeurs.

## 26 février 2026

- Lancement de Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=fr), un modèle à haute efficacité optimisé pour la vitesse et les cas d'utilisation à volume élevé.
- Annonce d'arrêt : la version Preview de Gemini 3 Pro (`gemini-3-pro-preview`) sera [arrêtée](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 9 mars 2026.

## 19 février 2026

- Lancement de [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr), notre dernière itération de la nouvelle famille Gemini 3.
- Lancement d'un point de terminaison distinct `gemini-3.1-pro-preview-customtools`, qui est plus efficace pour hiérarchiser les outils personnalisés, pour les utilisateurs qui créent des applications avec un mélange de bash et d'outils.

## 18 février 2025

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

- Lancement de la compatibilité avec l'outil Utilisation de l'ordinateur dans `gemini-3-pro-preview` et `gemini-3-flash-preview`.

## 21 janvier 2026

- Modification des alias `latest` :

  - `gemini-pro-latest` a été remplacé par `gemini-3-pro-preview`
  - `gemini-flash-latest` a été remplacé par `gemini-3-flash-preview`

## 15 janvier 2026

- Annonce d'arrêt : les modèles suivants seront [mis hors service](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr) le 17 février 2026 :

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Le modèle `gemini-2.5-flash-image-preview` a été arrêté.

## 14 janvier 2026

- Le modèle `text-embedding-004` a été [arrêté](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

## 13 janvier 2026

- Ajout de résolutions de sortie 4K pour [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr) et prise en charge des vidéos au format portrait dans toutes les résolutions.

## 12 janvier 2026

- Lancement de la fonctionnalité de cycle de vie des modèles. Certains modèles spécifient désormais l'étape du cycle de vie et le calendrier d'abandon. Pour en savoir plus, consultez la documentation suivante :

  - [Étapes du modèle](https://ai.google.dev/api/generate-content?hl=fr#ModelStatus)

## 8 janvier 2026

- Prise en charge des buckets Cloud Storage et de toute URL pré-signée DB publique et privée en tant que source d'entrée de données pour l'API Gemini. La limite de taille des fichiers est également passée de 20 Mo à 100 Mo. Pour en savoir plus, consultez le [guide sur les méthodes de saisie de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

## 19 décembre 2025

- Modification destructive apportée à l'API Interactions dans la version v1beta. Le champ `total_reasoning_tokens` a été renommé `total_thought_tokens` pour mieux correspondre au concept de "pensées" dans les modèles de réflexion.

## 17 décembre 2025

- Lancement de l'aperçu de Gemini 3 Flash, `gemini-3-flash-preview`, qui offre des performances rapides de pointe comparables à celles des modèles plus grands, pour un coût bien inférieur. Avec des capacités de raisonnement visuel et spatial améliorées, et des fonctionnalités de codage agentique. Consultez la documentation sur certaines nouvelles fonctionnalités, y compris :

  - [Réponses de fonction multimodales](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#multimodal)
  - [Exécution de code avec des images](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#images)

## 12 décembre 2025

- Sortie de `gemini-2.5-flash-native-audio-preview-12-2025`, un nouveau modèle audio natif pour l'API Live. Cette mise à jour améliore la capacité du modèle à gérer les workflows complexes. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr) et [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=fr).

## 11 décembre 2025

- Lancement de l'API Interactions. Cette API fournit une interface unifiée pour interagir avec les modèles et les agents Gemini. Pour en savoir plus, consultez le guide de l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr).
- Lancement de l'agent Gemini Deep Research en preview. Il peut planifier, exécuter et synthétiser de manière autonome les résultats des tâches de recherche en plusieurs étapes. Pour en savoir plus, consultez le guide [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr).

## 10 décembre 2025

- Nous avons lancé des améliorations pour nos [modèles de synthèse vocale](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr), les aperçus Gemini 2.5 Flash TTS (optimisé pour la faible latence) et Gemini 2.5 Pro TTS (optimisé pour la qualité), y compris une expressivité améliorée, un rythme précis et un dialogue fluide.

## 9 Décembre 2025

- Les modèles d'API Gemini Live suivants sont désormais arrêtés :
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 décembre 2025

- La facturation de Gemini 3 pour l'[ancrage avec la Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) commencera le 5 janvier 2026.

## 4 décembre 2025

- Annonce d'arrêt : le modèle `gemini-2.5-flash-image-preview` sera arrêté le 15 janvier 2026.

## 3 décembre 2025

- Annonce d'abandon : le modèle `text-embedding-004` sera arrêté le 14 janvier 2026.

## 20 novembre 2025

- Sortie de Gemini 3 Pro Image Preview, `gemini-3-pro-image-preview`, la prochaine itération du modèle Nano Banana. Pour en savoir plus, consultez la page [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

## 18 Novembre 2025

- Lancement du premier modèle de la série Gemini 3, `gemini-3-pro-preview`, notre modèle de raisonnement et de compréhension multimodale de pointe, doté de puissantes capacités agentiques et de codage.

  En plus d'améliorer l'intelligence et les performances, l'aperçu de Gemini 3 Pro introduit de nouveaux comportements concernant :

  - [Résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr)
  - [Signatures de réflexion](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr)
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

  Utilisez plutôt [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=fr#imagen-4). Pour en savoir plus, consultez le [tableau des abandons de Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=fr).

## 6 novembre 2025

- Lancement de l'API File Search en version Preview publique, permettant aux développeurs d'ancrer les réponses dans leurs propres données. Pour en savoir plus, consultez la nouvelle page [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

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
- Annonce d'arrêt : arrêt de `gemini-2.0-flash-live-001` et `gemini-live-2.5-flash-preview` le 9 décembre 2025.

## 17 octobre 2025

- L'**ancrage avec Google Maps** est désormais en phase de disponibilité générale. Pour en savoir plus, consultez la documentation sur l'[ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr).

## 15 octobre 2025

- Publication des modèles [Veo 3.1 et 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=fr#veo-3.1) en version bêta publique, avec de nouvelles fonctionnalités, y compris :

  - Prolonger des vidéos créées par Veo
  - Faites référence à un maximum de trois images pour générer une vidéo.
  - Fournir les images de la première et de la dernière image pour générer des vidéos

  Nous avons également ajouté des options de durée pour les vidéos générées par Veo 3 : 4, 6 et 8 secondes.
- Annonce d'arrêt : `veo-3.0-generate-preview` et `veo-3.0-fast-generate-preview` seront arrêtés le 12 novembre 2025.

## 7 octobre 2025

- Lancement de la [version Preview de Gemini 2.5 Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)

## 2 octobre 2025

- Lancement de Gemini 2.5 Flash Image en disponibilité générale : [Génération d'images avec Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)

## 29 septembre 2025

- Les modèles Gemini 1.5 suivants sont désormais arrêtés :
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 septembre 2025

- Sortie du modèle Gemini Robotics ER 1.5 en preview. Consultez la [présentation de la robotique](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) pour découvrir comment utiliser le modèle pour votre application de robotique.
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

- Prise en charge du [modèle Embeddings dans l'API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr#batch-embedding) et ajout de l'API Batch à la [bibliothèque de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr#batch) pour faciliter encore plus la prise en main des requêtes par lot.

## 9 septembre 2025

- Lancement de Veo 3 et Veo 3 Fast en disponibilité générale, avec des prix plus bas et de nouvelles options pour les formats, la résolution et le seeding. Pour en savoir plus, consultez la [documentation Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr#model-features).

## 26 août 2025

- Lancement de [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-image-preview), notre dernier modèle de génération d'images natif.

## 18 août 2025

- Lancement de l'[outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) en disponibilité générale (DG). Cet outil permet de fournir des URL comme contexte supplémentaire aux requêtes. L'assistance pour l'utilisation du contexte d'URL avec le modèle `gemini-2.0-flash` (disponible en version expérimentale) sera interrompue dans une semaine.

## 14 août 2025

- Les modèles Imagen 4 Ultra, Standard et Fast sont désormais en disponibilité générale (DG). Pour en savoir plus, consultez la page [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=fr).

## 7 août 2025

- Le paramètre `allow_adult` de la génération d'images en vidéos est désormais disponible dans les régions soumises à restriction. Pour en savoir plus, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=fr#veo-model-parameters).

## 31 juillet 2025

- Lancement de la génération de vidéos à partir d'images pour le modèle Veo 3 (preview).
- Publication du modèle Veo 3 Fast Preview.
- Pour en savoir plus sur Veo 3, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).

## 22 juillet 2025

- Sortie de `gemini-2.5-flash-lite`, notre modèle Gemini 2.5 rapide, économique et performant. Pour en savoir plus, consultez [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-lite).

## July 17, 2025

- Lancement de `veo-3.0-generate-preview`, la dernière mise à jour de Veo qui permet de générer des vidéos avec de l'audio. Pour en savoir plus sur Veo 3, consultez la page [Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Augmentation des limites de débit pour Imagen 4 Standard et Ultra. Pour en savoir plus, consultez la page [Limites de débit](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr).

## 14 juillet 2025

- Sortie de `gemini-embedding-001`, la version stable de notre modèle d'embedding textuel. Pour en savoir plus, consultez [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr). Le modèle `gemini-embedding-exp-03-07`
  sera obsolète le 14 août 2025.

## 7 juillet 2025

- Lancement du mode par lot de l'API Gemini. Regroupez les requêtes et envoyez-les pour traitement de manière asynchrone. Pour en savoir plus, consultez [Mode Batch](https://ai.google.dev/gemini-api/docs/batch-mode?hl=fr).

## 26 juin 2025

- Les modèles preview `gemini-2.5-pro-preview-05-06` et `gemini-2.5-pro-preview-03-25` redirigent désormais vers la dernière version stable `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` est éteint.

## 24 juin 2025

- Publication des modèles Imagen 4 Ultra et Standard en preview. Pour en savoir plus, consultez la page [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

## 17 juin 2025

- Sortie le `gemini-2.5-pro`, la version stable de notre modèle le plus puissant, désormais doté d'une capacité de réflexion adaptative. Pour en savoir plus, consultez [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr). `gemini-2.5-pro-preview-05-06`
  sera redirigé vers `gemini-2.5-pro` le 26 juin 2025.
- Sortie de `gemini-2.5-flash`, notre premier modèle 2.5 Flash stable. Pour en savoir plus, consultez [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` sera obsolète le 15 juillet 2025.
- Lancement de `gemini-2.5-flash-lite-preview-06-17`, un modèle Gemini 2.5 à faible coût et hautes performances. Pour en savoir plus, consultez [Preview Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-lite).

## 5 juin 2025

- Nous avons lancé `gemini-2.5-pro-preview-06-05`, une nouvelle version de notre modèle le plus puissant, qui intègre désormais la pensée adaptative. Pour en savoir plus, consultez [Preview de Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-06-05) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).
  `gemini-2.5-pro-preview-05-06` sera redirigé vers `gemini-2.5-pro` le 26 juin 2025.

## 27 mai 2025

- Le dernier modèle d'affinage disponible, Gemini 1.5 Flash 001, a été arrêté.
  Le réglage n'est plus pris en charge sur aucun modèle.
  Consultez [Finetuning avec l'API Gemini](https://ai.google.dev/gemini-api/docs/model-tuning?hl=fr).

## 20 mai 2025

**Mises à jour de l'API :**

- Ajout de la prise en charge du [prétraitement vidéo personnalisé](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#customize-video-processing) à l'aide d'intervalles de découpage et d'un échantillonnage de la fréquence d'images configurable.
- Lancement de l'utilisation de plusieurs outils, qui permet de configurer l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et l'[ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) sur la même requête `generateContent`.
- Lancement de la prise en charge des [appels de fonction asynchrones](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr#async-function-calling) dans l'API Live.
- Lancement d'un [outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) expérimental permettant de fournir des URL comme contexte supplémentaire aux requêtes.

**Mises à jour des modèles** :

- Sortie de `gemini-2.5-flash-preview-05-20`, un modèle [preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions) Gemini optimisé pour le rapport prix/performances et la pensée adaptative. Pour en savoir plus, consultez [Aperçu de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).
- Publication des modèles [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-tts) et [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview-tts), qui sont capables de [générer de la parole](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr) avec un ou deux locuteurs.
- Sortie du modèle `lyria-realtime-exp`, qui [génère de la musique](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) en temps réel.
- Sortie des `gemini-2.5-flash-preview-native-audio-dialog` et `gemini-2.5-flash-exp-native-audio-thinking-dialog`, de nouveaux modèles Gemini pour l'API Live avec des fonctionnalités de sortie audio native. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#native-audio-output) et [Audio natif Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-native-audio).
- Version Preview `gemma-3n-e4b-it` disponible sur [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=fr).

## 7 mai 2025

- Sortie de `gemini-2.0-flash-preview-image-generation`, un modèle d'aperçu pour générer et modifier des images. Pour en savoir plus, consultez [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) et [Génération d'images avec Gemini 2.0 Flash (preview)](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.0-flash-preview-image-generation).

## 6 mai 2025

- Nous avons lancé `gemini-2.5-pro-preview-05-06`, une nouvelle version de notre modèle le plus puissant, avec des améliorations au niveau du code et des appels de fonction. `gemini-2.5-pro-preview-03-25` pointera automatiquement vers la nouvelle version du modèle.

## 17 avril 2025

- Sortie de `gemini-2.5-flash-preview-04-17`, un modèle [preview](https://ai.google.dev/gemini-api/docs/models?hl=fr#model-versions) Gemini optimisé pour le rapport prix/performances et la pensée adaptative. Pour en savoir plus, consultez [Aperçu de Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-flash-preview) et [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

## 16 avril 2025

- Lancement de la mise en cache du contexte pour [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.0-flash).

## 9 avril 2025

**Mises à jour des modèles** :

- Lancement de `veo-2.0-generate-001`, un modèle de texte et d'image à vidéo en disponibilité générale (DG), capable de générer des vidéos détaillées et artistiquement nuancées. Pour en savoir plus, consultez la [documentation Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Publication de `gemini-2.0-flash-live-001`, une version Preview publique du modèle [Live API](https://ai.google.dev/gemini-api/docs/live?hl=fr) avec la facturation activée.

  - **Fiabilité et gestion des sessions améliorées**

    - **Reprise de session** : permet de maintenir les sessions actives en cas de perturbations temporaires du réseau. L'API est désormais compatible avec le stockage de l'état de la session côté serveur (pendant 24 heures maximum) et fournit des identifiants (session\_resumption) pour se reconnecter et reprendre là où vous vous étiez arrêté.
    - **Sessions plus longues grâce à la compression du contexte** : permet des interactions plus longues que les limites de temps précédentes. Configurez la compression de la fenêtre de contexte avec un mécanisme de fenêtre glissante pour gérer automatiquement la longueur de contexte, ce qui évite les arrêts brusques dus aux limites de contexte.
    - **Notification de déconnexion progressive** : recevez un message du serveur `GoAway` indiquant quand une connexion est sur le point d'être fermée, ce qui permet une gestion progressive avant la fin de la connexion.
  - **Plus de contrôle sur la dynamique des interactions**
  - **Détection d'activité vocale (VAD) configurable** : choisissez des niveaux de sensibilité ou désactivez complètement la VAD automatique et utilisez de nouveaux événements client (`activityStart`, `activityEnd`) pour le contrôle manuel du tour de parole.
  - **Gestion configurable des interruptions** : décidez si l'entrée utilisateur doit interrompre la réponse du modèle.
  - **Couverture TURN configurable** : choisissez si l'API traite toutes les entrées audio et vidéo en continu ou ne les capture que lorsque l'utilisateur final est détecté en train de parler.
  - **Résolution média configurable** : optimisez la qualité ou l'utilisation de jetons en sélectionnant la résolution des médias d'entrée.
  - **Des résultats et des fonctionnalités plus riches**
  - **Options de voix et de langue étendues** : choisissez parmi deux nouvelles voix et 30 nouvelles langues pour la sortie audio. La langue de sortie est désormais configurable dans `speechConfig`.
  - **Streaming de texte** : recevez les réponses textuelles de manière incrémentielle au fur et à mesure de leur génération, ce qui permet de les afficher plus rapidement à l'utilisateur.
  - **Rapports sur l'utilisation des jetons** : obtenez des insights sur l'utilisation grâce à des décomptes détaillés des jetons fournis dans le champ `usageMetadata` des messages du serveur, ventilés par modalité et par phase de requête ou de réponse.

## 4 avril 2025

- Publication de la version Preview publique de Gemini 2.5 Pro le `gemini-2.5-pro-preview-03-25`, avec la facturation activée. Vous pouvez continuer à utiliser `gemini-2.5-pro-exp-03-25` avec le forfait sans frais.

## 25 mars 2025

- Publication de `gemini-2.5-pro-exp-03-25`, un modèle Gemini expérimental public avec le mode de réflexion toujours activé par défaut.
  Pour en savoir plus, consultez [Gemini 2.5 Pro (expérimental)](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-2.5-pro-preview-03-25).

## 12 mars 2025

**Mises à jour des modèles** :

- Lancement d'un modèle expérimental [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#gemini) capable de générer et de retoucher des images.
- Sorti le `gemma-3-27b-it`, disponible sur [AI Studio](https://aistudio.google.com?hl=fr) et via l'API Gemini, dans le cadre du lancement de [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=fr).

**Mises à jour de l'API :**

- Ajout de la compatibilité avec les [URL YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=fr#youtube) en tant que source multimédia.
- Ajout de la possibilité d'inclure une [vidéo intégrée](https://ai.google.dev/gemini-api/docs/vision?hl=fr#inline-video) de moins de 20 Mo.

## 11 mars 2025

**Mises à jour du SDK :**

- Publication de la version Preview publique du [SDK Google Gen AI pour TypeScript et JavaScript](https://googleapis.github.io/js-genai).

## 7 mars 2025

**Mises à jour des modèles** :

- Publication `gemini-embedding-exp-03-07` d'un modèle d'embeddings [expérimental](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=fr) basé sur Gemini en version Preview publique.

## 28 février 2025

**Mises à jour de l'API :**

- Ajout de la [recherche en tant qu'outil](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) à `gemini-2.0-pro-exp-02-05`, un modèle expérimental basé sur Gemini 2.0 Pro.

## 25 février 2025

**Mises à jour des modèles** :

- Sortie de la version en disponibilité générale (DG) de [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash-lite), le `gemini-2.0-flash-lite`, qui est optimisée pour la vitesse, l'évolutivité et la rentabilité.

## 19 février 2025

**Nouveautés d'AI Studio :**

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

- Sortie de `imagen-3.0-generate-002`, une version en disponibilité générale (DG) d'[Imagen 3 dans l'API Gemini](https://ai.google.dev/gemini-api/docs/imagen?hl=fr).

**Mises à jour du SDK :**

- Publication du [SDK Google Gen AI pour Java](https://github.com/googleapis/java-genai) en version Preview publique.

## 5 février 2025

**Mises à jour des modèles** :

- Nous avons lancé `gemini-2.0-flash-001`, une version en disponibilité générale (DG) de [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash) qui prend en charge les sorties textuelles uniquement.
- Version publique [expérimentale](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=fr) de Gemini 2.0 Pro publiée le `gemini-2.0-pro-exp-02-05`.
- Lancement de `gemini-2.0-flash-lite-preview-02-05`, un [modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash-lite) expérimental en aperçu public optimisé pour la rentabilité.

**Mises à jour de l'API :**

- Ajout de la prise en charge de l'[entrée de fichier et de la sortie de graphique](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#input-output) à l'exécution de code.

**Mises à jour du SDK :**

- Mise à disposition générale du [SDK Google Gen AI pour Python](https://googleapis.github.io/python-genai/).

## 21 janvier 2025

**Mises à jour des modèles** :

- Sortie le `gemini-2.0-flash-thinking-exp-01-21`, dernière version Preview du modèle qui alimente le [modèle Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

## 19 décembre 2024

**Mises à jour des modèles** :

- Lancement du mode Gemini 2.0 Flash Thinking en version Preview publique. Le mode Réflexion est un modèle de calcul au moment du test qui vous permet de voir le processus de réflexion du modèle lorsqu'il génère une réponse. Il produit des réponses avec de meilleures capacités de raisonnement.

  Pour en savoir plus sur le mode Gemini 2.0 Flash Thinking, consultez notre [page de présentation](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=fr).

## 11 décembre 2024

**Mises à jour des modèles** :

- Lancement de [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-2.0-flash) en version Preview publique. Voici une liste partielle des fonctionnalités de Gemini 2.0 Flash Experimental :
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
    Les valeurs supérieures à 40 seront remplacées par 40.

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

**Nouveautés d'AI Studio :**

- Ajout de boutons "J'aime" et "Je n'aime pas" aux réponses du modèle pour permettre aux utilisateurs de donner leur avis sur la qualité d'une réponse.

**Mises à jour de l'API :**

- Ajout de la compatibilité avec les crédits Google Cloud, qui peuvent désormais être utilisés pour l'utilisation de l'API Gemini.

## 17 septembre 2024

**Nouveautés d'AI Studio :**

- Ajout d'un bouton **Ouvrir dans Colab** qui exporte une requête (et le code pour l'exécuter) vers un notebook Colab. Cette fonctionnalité n'est pas encore compatible avec les requêtes utilisant des outils (mode JSON, appel de fonction ou exécution de code).

## 13 septembre 2024

**Nouveautés d'AI Studio :**

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

- Sortie le `gemini-1.5-pro-exp-0801`, une nouvelle version expérimentale de [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro).

## 12 juillet 2024

**Mises à jour des modèles** :

- La prise en charge de Gemini 1.0 Pro Vision a été supprimée des services et outils Google AI.

## 27 juin 2024

**Mises à jour des modèles** :

- Sortie de la disponibilité générale de la fenêtre de contexte de deux millions de jetons de Gemini 1.5 Pro.

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

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro) (`gemini-1.5-pro-001`) est en disponibilité générale (DG).
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

## 9 avril 2024

**Mises à jour des modèles** :

- Sortie de [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#gemini-1.5-pro) (`gemini-1.5-pro-latest`) en preview.
- Lancement d'un nouveau modèle d'embedding textuel, `text-embeddings-004`, qui est compatible avec les tailles d'[embedding élastique](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr#elastic-embedding) inférieures à 768.

**Mises à jour de l'API :**

- L'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=fr) a été publiée pour stocker temporairement les fichiers multimédias à utiliser dans les requêtes.
- Ajout de la prise en charge des requêtes avec des données textuelles, d'image et audio, également appelées requêtes *multimodales*. Pour en savoir plus, consultez [Requêtes avec des éléments multimédias](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=fr).
- Lancement des [instructions système](https://ai.google.dev/gemini-api/docs/system-instructions?hl=fr) en version bêta.
- Ajout du [mode d'appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#function_calling_mode), qui définit le comportement d'exécution pour l'appel de fonction.
- Ajout de la compatibilité avec l'option de configuration `response_mime_type`, qui vous permet de demander des réponses au [format JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=fr#json).

## 19 mars 2024

**Mises à jour des modèles** :

- Ajout de la prise en charge de la [configuration de Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) dans Google AI Studio ou avec l'API Gemini.

## 13 décembre 2023

**Mises à jour des modèles** :

- gemini-pro : nouveau modèle de texte pour une grande variété de tâches. Équilibre les capacités et l'efficacité.
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
- Le streaming est disponible via la méthode `StreamGenerateContent`.
- Fonctionnalité multimodale : l'image est une nouvelle modalité acceptée
- Nouvelles fonctionnalités bêta :
  - [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
  - Attributed Question Answering (AQA)
- Nombre de candidats mis à jour : les modèles Gemini ne renvoient qu'un seul candidat.
- Différentes catégories de paramètres de sécurité et de classification de sécurité. Pour en savoir plus, consultez [Paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr).
- L'ajustement des modèles n'est pas encore disponible pour les modèles Gemini (en cours de développement).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/09 (UTC)."],[],[]]
