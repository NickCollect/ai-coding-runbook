---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=fr
fetched_at: 2026-11-02T07:28:37.346908+00:00
title: "Pr\u00e9sentation de l'API Gemini\u00a0Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Présentation de l'API Gemini Live

L'API Live permet des interactions vocales et visuelles en temps réel et à faible latence avec Gemini. Il traite des flux continus d'audio, d'images et de texte pour fournir des réponses parlées immédiates et semblables à celles d'un humain, créant ainsi une expérience conversationnelle naturelle pour vos utilisateurs.

![Présentation de l'API Live](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=fr)

[Essayer l'API en direct dans Google AI Studiomic](https://aistudio.google.com/live?hl=fr)
[Cloner des exemples d'applications depuis GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Utiliser les compétences d'agent de codageterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr)

## Cas d'utilisation

L'API Live peut être utilisée pour créer des agents vocaux en temps réel pour divers secteurs, y compris :

- **E-commerce et vente au détail** : assistants d'achat qui proposent des recommandations personnalisées et agents d'assistance qui résolvent les problèmes des clients.
- **Jeux vidéo** : personnages non joueurs (PNJ) interactifs, assistants d'aide dans les jeux et traduction en temps réel du contenu des jeux.
- **Interfaces nouvelle génération** : expériences vocales et vidéo dans la robotique, les lunettes connectées et les véhicules.
- **Santé** : compagnons de santé pour l'assistance et l'éducation des patients.
- **Services financiers** : conseillers IA pour la gestion de patrimoine et les conseils d'investissement.
- **Éducation** : mentors et compagnons d'apprentissage basés sur l'IA qui fournissent des instructions et des commentaires personnalisés.
- **Traduction et localisation** : traduction en temps réel et à faible latence des conversations orales, permettant une communication multilingue fluide.
- **Transcription et sous-titrage instantanés** : flux de reconnaissance vocale en temps réel pour les sous-titres en direct, la transcription des réunions, la dictée vocale et la journalisation des appels clients.

## Principales fonctionnalités

L'API Live offre un ensemble complet de fonctionnalités permettant de créer des agents vocaux robustes :

- [**Compatibilité multilingue**](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#supported-languages) : discutez dans l'une des 70 langues disponibles.
- [**Interruption**](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#interruptions) : les utilisateurs peuvent interrompre le modèle à tout moment pour des interactions réactives.
- [**Utilisation d'outils**](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr) : intègre des outils tels que l'appel de fonction et la recherche Google pour des interactions dynamiques.
- [**Transcriptions audio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#audio-transcription) :
  Fournit des transcriptions textuelles des entrées utilisateur et des sorties du modèle.
- [**Audio proactif**](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#proactive-audio) : vous permet de contrôler quand et dans quels contextes le modèle répond.
- [**Dialogues affectifs**](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr#affective-dialog) : le style et le ton des réponses s'adaptent à l'expression de l'utilisateur.
- [**Transcription instantanée**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fr) : flux continu de conversion de la voix en texte en temps réel, avec détection automatique de la langue et vocabulaire personnalisé.
- [**Traduction instantanée**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=fr) :
  Traduction vocale en temps réel dans plus de 70 langues.

## Spécifications techniques

Le tableau suivant présente les spécifications techniques de l'API Live :

| Catégorie | Détails |
| --- | --- |
| Modes d'entrée | Audio (audio PCM 16 bits brut, 16 kHz, little-endian), images (JPEG <= 1 FPS), texte |
| Modes de sortie | Audio (audio PCM 16 bits brut, 24 kHz, little-endian) |
| Protocole | Connexion WebSocket avec état (WSS) |

## Choisir une approche d'implémentation

Lorsque vous intégrez l'API Live, vous devez choisir l'une des approches d'implémentation suivantes :

- **Serveur à serveur** : votre backend se connecte à l'API Live à l'aide de [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). En général, votre client envoie des données de flux (audio, vidéo, texte) à votre serveur, qui les transmet ensuite à l'API Live.
- **Client vers serveur** : votre code de frontend se connecte directement à l'API Live à l'aide de [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) pour diffuser des données, en contournant votre backend.

## Commencer

Sélectionnez le guide correspondant à votre environnement de développement :

Serveur à serveur

### [Tutoriel sur le SDK GenAI](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=fr)

Connectez-vous à l'API Gemini Live à l'aide du SDK GenAI pour créer une application multimodale en temps réel avec un backend Python.

Client-to-server

### [Tutoriel WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=fr)

Connectez-vous à l'API Gemini Live à l'aide de WebSockets pour créer une application multimodale en temps réel avec un frontend JavaScript et des jetons éphémères.

Agent development kit

### [Tutoriel ADK](https://google.github.io/adk-docs/streaming/)

Créez un agent et utilisez Agent Development Kit (ADK) Streaming pour activer la communication vocale et vidéo.

## Intégration de partenaires

Pour simplifier le développement d'applications audio et vidéo en temps réel, vous pouvez utiliser une intégration tierce compatible avec l'API Gemini Live via WebRTC ou WebSockets.

[LiveKit

Utilisez l'API Gemini Live avec les agents LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Créez un chatbot IA en temps réel à l'aide de Gemini Live et Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam par Software Mansion

Créez des applications de streaming vidéo et audio en direct avec Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Agents Vision de Stream

Créez des applications d'IA vocales et vidéo en temps réel avec les agents Vision.](https://visionagents.ai/integrations/gemini)
[Voximplant

Associez les appels entrants et sortants à l'API Live avec Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Créez des applications d'IA conversationnelle en temps réel avec Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[SDK Firebase AI

Faites vos premiers pas avec l'API Gemini Live à l'aide de Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/07 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/07 (UTC)."],[],[]]
