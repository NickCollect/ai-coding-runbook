---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=fr
fetched_at: 2026-05-18T05:16:01.372498+00:00
title: "Optimisation et inf\u00e9rence de l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Optimisation et inférence de l'API Gemini

L'API Gemini propose différents mécanismes d'optimisation pour vous aider à équilibrer la vitesse, le coût et la fiabilité en fonction des besoins spécifiques de vos charges de travail.
Que vous créiez des robots conversationnels en temps réel ou que vous exécutiez des pipelines de traitement de données hors connexion volumineux, le choix du bon paradigme peut réduire considérablement les coûts ou améliorer les performances.

| Fonctionnalité | Standard | Flex | Priorité | Lot | Mise en cache |
| --- | --- | --- | --- | --- | --- |
| **Tarifs** | Plein tarif | 50% de remise | 75% à 100% de plus que la valeur standard | 50% de remise | Remise de 90% + stockage des jetons au prorata |
| **Latence** | De secondes à minutes | Minutes (objectif de 1 à 15 min) | Secondes | Jusqu'à 24 heures | Délai d'émission du premier jeton plus rapide |
| **Fiabilité** | Élevée / Moyenne-haute | Optimisation limitée (désactivable) | Élevée (non amovible) | Élevée (pour le débit) | N/A |
| **Interface** | Synchrone | Synchrone | Synchrone | Asynchrone | État enregistré |
| **Cas d'utilisation idéal** | Workflows généraux des applications | Chaînes séquentielles non urgentes | Applications de production destinées aux utilisateurs | Ensembles de données volumineux, évaluations hors connexion | Requêtes récurrentes sur le même fichier |

## Niveaux de service d'inférence (synchrone)

Vous pouvez passer d'un trafic synchrone optimisé pour la fiabilité à un trafic synchrone optimisé pour les coûts en transmettant le paramètre `service_tier` dans vos appels de génération standards.

### Inférence standard (par défaut)

Le niveau standard est l'option par défaut pour la génération de contenu séquentiel.
Elle offre des temps de réponse normaux, sans frais supplémentaires ni longues files d'attente.

- **Fiabilité** : niveau de gravité standard
- **Prix** : tarifs standards.
- **Recommandé pour** : la plupart des applications interactives du quotidien.

### Inférence prioritaire (optimisée pour la latence)

Le traitement [prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr) achemine vos demandes vers des files d'attente de calcul de haute criticité.
Ce trafic ne peut en aucun cas être supprimé (il n'est jamais interrompu par d'autres niveaux) et offre la fiabilité la plus élevée. Si vous dépassez les limites de priorité dynamique, le système rétrogradera la requête vers un traitement standard au lieu d'échouer avec une erreur.

- **Fiabilité** : criticité la plus élevée
- **Prix** : 75% à 100% au-dessus des tarifs standards.
- **Idéal pour** : les chatbots clients, la détection de fraudes en temps réel et les copilotes essentiels pour l'entreprise.

### Inférence flexible (coût optimisé)

L'[inférence flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr) offre une remise de 50% par rapport aux tarifs standards en utilisant une capacité de calcul opportuniste hors pointe. Les requêtes sont traitées de manière synchrone, ce qui signifie que vous n'avez pas besoin de réécrire le code pour gérer les objets de lot.
Comme il s'agit d'un trafic "éliminable", les requêtes peuvent être préemptées si le système connaît des pics de trafic standards.

- **Fiabilité** : criticité non garantie et réductible
- **Prix** : 50% du prix standard (facturé par jeton).
- **Idéal pour** : les workflows agentiques en plusieurs étapes où l'appel N+1 dépend de la sortie de l'appel N, des mises à jour CRM en arrière-plan et des évaluations hors connexion.

## API Batch (par lot, asynchrone)

L'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) est conçue pour traiter de grands volumes de requêtes de manière asynchrone à 50% du coût standard. Vous pouvez envoyer des requêtes sous forme de dictionnaires intégrés ou à l'aide d'un fichier d'entrée JSONL (jusqu'à 2 Go). Il traite les demandes à l'aide de files d'attente de débit en arrière-plan avec un délai de traitement cible de 24 heures.

- **Fiabilité** : peut être supprimé, mais avec des tentatives automatiques de 24 heures et un système de mise en file d'attente
- **Prix** : 50% du prix standard.
- **Idéal pour** : le prétraitement d'ensembles de données volumineux, l'exécution de suites de tests de régression périodiques et la génération d'images ou d'embeddings à grand volume.

## Mise en cache du contexte (économies d'entrées)

La [mise en cache de contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) est utilisée lorsqu'un contexte initial important est référencé à plusieurs reprises par des requêtes plus courtes.

- **Mise en cache implicite** : activée automatiquement sur les modèles Gemini 2.5 et ultérieurs.
  Le système répercute les économies si votre demande touche des caches existants basés sur des préfixes d'invite courants.
- **Mise en cache explicite** : vous pouvez créer manuellement un objet cache avec une valeur TTL (Time-To-Live) spécifique. Une fois les jetons mis en cache, vous pouvez vous y référer pour les requêtes ultérieures afin d'éviter de transmettre plusieurs fois la même charge utile de corpus.
- **Prix** : facturé en fonction du nombre de jetons de cache et de la durée de stockage (TTL).
- **Idéal pour** : les chatbots avec des instructions système détaillées, l'analyse répétitive de fichiers vidéo longs ou les requêtes sur des ensembles de documents volumineux.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
