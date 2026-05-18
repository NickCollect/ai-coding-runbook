---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=fr
fetched_at: 2026-05-18T05:19:31.985909+00:00
title: "Pr\u00e9sentation des agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Présentation des agents

Les agents sont des systèmes qui exploitent les modèles Gemini, un ensemble d'outils et des capacités de raisonnement pour effectuer des tâches complexes en plusieurs étapes et atteindre des objectifs spécifiques. Contrairement à un simple appel de modèle, un agent peut planifier et exécuter une série d'actions, interagir avec des systèmes externes et synthétiser des informations pour répondre à la demande d'un utilisateur.

L'API Gemini vous permet de créer des agents puissants en utilisant des fonctionnalités telles que :

- **[Modèles Gemini](https://ai.google.dev/gemini-api/docs/models?hl=fr)** : l'intelligence de base, qui permet le raisonnement et la compréhension du langage.
- **[Outils](https://ai.google.dev/gemini-api/docs/tools?hl=fr)** : capacités qui connectent le modèle à des informations et des actions réelles. Il peut s'agir d'outils intégrés (comme la recherche Google, Maps ou l'exécution de code) ou d'outils personnalisés.
- **[Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)** : mécanisme permettant de définir et de connecter vos propres outils et API personnalisés au modèle Gemini.
- [**Raisonnement** : fonctionnalités qui améliorent la capacité du modèle à raisonner et à planifier des tâches complexes.](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)
- **[Contexte long](https://ai.google.dev/gemini-api/docs/long-context?hl=fr)** : permet aux agents de conserver l'état et les informations lors d'interactions prolongées.

## Agents disponibles

- **[Agent Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr)** : agent autonome qui planifie, exécute et synthétise des tâches de recherche en plusieurs étapes pour des cas d'utilisation tels que l'analyse de marché, la diligence raisonnable et les revues de la littérature.

## Créer des agents

Les agents utilisent des modèles et des outils pour effectuer des tâches en plusieurs étapes. Bien que Gemini fournisse les capacités de raisonnement (le "cerveau") et les outils essentiels (les "mains"), vous avez souvent besoin d'un framework d'orchestration pour gérer la mémoire de l'agent, planifier les boucles et effectuer un chaînage d'outils complexe.

Pour maximiser la fiabilité des workflows en plusieurs étapes, vous devez rédiger des instructions qui contrôlent explicitement la façon dont le modèle raisonne et planifie. Bien que Gemini offre un raisonnement général solide, les agents complexes bénéficient de requêtes qui imposent des comportements spécifiques tels que la persévérance face aux problèmes, l'évaluation des risques et la planification proactive.

Consultez les [workflows agentiques](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr#agentic-workflows) pour obtenir des stratégies de conception de ces requêtes. Voici un exemple d'[instruction système](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr#agentic-si-template) qui a amélioré les performances sur plusieurs benchmarks d'environ 5%.

## Frameworks d'agents

Gemini s'intègre aux principaux frameworks d'agents Open Source, tels que :

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=fr) : créez des flux d'application complexes avec état et des systèmes multi-agents à l'aide de structures de graphiques.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=fr) : connectez les agents Gemini à vos données privées pour des workflows RAG améliorés.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=fr) : orchestrez des agents d'IA autonomes et collaboratifs qui jouent un rôle.
- [**SDK Vercel AI**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=fr) : créez des interfaces utilisateur et des agents optimisés par l'IA en JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/) : framework Open Source permettant de créer et d'orchestrer des agents d'IA interopérables.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
