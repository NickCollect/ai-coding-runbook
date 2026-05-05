---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=fr
fetched_at: 2026-05-05T13:22:39.617935+00:00
title: "R\u00e9tention des donn\u00e9es nulle dans l'API Gemini\u00a0Developer \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/recherche approfondie Gemini) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

- [Accueil](https://ai.google.dev/gemini-api/docs/Accueil)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

Envoyer des commentaires

# Rétention des données nulle dans l'API Gemini Developer

Cette page décrit en détail ce que l'on appelle communément la "rétention zéro des données" dans l'API Gemini Developer.

## Restriction liée à l'entraînement

Comme indiqué dans les [Conditions d'utilisation de l'API Gemini](https://ai.google.dev/gemini-api/docs/Conditions d'utilisation de l'API Gemini), lorsque vous utilisez des Services payants, Google n'utilise pas vos requêtes (y compris les instructions système associées, le contenu mis en cache et les fichiers tels que les images, les vidéos ou les documents) ni les réponses pour améliorer ses produits. Les Services payants sont définis [ici](https://ai.google.dev/gemini-api/docs/ici).

## Conservation des données client et objectif de zéro conservation des données

Les données client sont généralement conservées pendant une durée limitée dans les scénarios et conditions suivants. Pour ne conserver aucune donnée, les clients doivent effectuer des actions spécifiques ou éviter certaines fonctionnalités dans chacun de ces domaines :

- **Journalisation des requêtes pour la surveillance des utilisations abusives** : comme indiqué dans les [Conditions d'utilisation supplémentaires de l'API Gemini](https://ai.google.dev/gemini-api/docs/Conditions d'utilisation supplémentaires de l'API Gemini), pour les Services payants, Google enregistre les requêtes et les réponses pendant une durée limitée uniquement pour détecter les cas de non-respect du [Règlement sur les utilisations interdites](https://ai.google.dev/gemini-api/docs/Règlement sur les utilisations interdites). Lorsque votre demande de ZDR pour un projet spécifique est approuvée, tous les contenus utilisateur (requêtes et réponses) et les métadonnées identifiables (telles que les adresses IP et les ID de compte Google) sont effacés avant la journalisation. L'enregistrement obtenu est marqué comme nettoyé et ne contient aucune donnée utilisateur permettant de l'identifier, ce qui garantit la parité avec la plate-forme Gemini Enterprise Agent Zero Data Retention.
- **Ancrage avec la recherche Google** : comme indiqué dans les [Conditions d'utilisation supplémentaires de l'API Gemini](https://ai.google.dev/gemini-api/docs/Conditions d'utilisation supplémentaires de l'API Gemini), Google stocke les requêtes, les informations contextuelles et les résultats générés pendant 30 jours afin de créer des résultats ancrés et des suggestions de recherche.
  Ces informations stockées peuvent être utilisées pour le débogage et le test des systèmes qui prennent en charge l'ancrage. **Il n'est pas possible de désactiver le stockage de ces informations si vous utilisez l'ancrage avec la recherche Google.**
- **Ancrage avec Google Maps** : comme indiqué dans les [Conditions d'utilisation supplémentaires de l'API Gemini](https://ai.google.dev/gemini-api/docs/Conditions d'utilisation supplémentaires de l'API Gemini), Google stocke les requêtes, les informations contextuelles et les résultats générés pendant 30 jours afin de créer des résultats ancrés. Ces informations stockées ne peuvent être utilisées que pour l'ingénierie de la fiabilité, par exemple pour le débogage en cas de problèmes de service.
  **Il n'est pas possible de désactiver le stockage de ces informations si vous utilisez l'ancrage avec Google Maps.**
- **API Interactions** : l'API Interactions gère l'état actif d'une conversation pour permettre les tours multitours. **Par défaut, l'API Interactions permet le stockage de l'état.** Pour garantir une empreinte de données nulle, vous devez définir explicitement le paramètre `store` sur `false` dans vos requêtes API afin de désactiver la conservation de l'état par défaut.
- **API Live** : cette API avec état permet une reconnexion en temps réel en stockant l'état de la conversation. Si vous ne souhaitez pas conserver de données, **ne configurez pas SessionResumptionConfig**. Si un identifiant de session est généré, l'état de la conversation (y compris le texte, l'audio et la vidéo) est conservé pendant 24 heures maximum.
- **Stockage de l'API File** : l'API File permet aux utilisateurs d'importer des composants volumineux.
  Les fichiers sont stockés au repos jusqu'à ce qu'ils soient supprimés par l'utilisateur ou qu'ils expirent.
  L'utilisation de l'API File est indépendante de la journalisation ZDR. Les utilisateurs doivent supprimer manuellement les fichiers pour s'assurer qu'il ne reste aucune trace de données.
- **Mise en cache explicite du contexte** : les utilisateurs peuvent mettre manuellement en cache de grands ensembles de données (par exemple, de longues vidéos ou des bibliothèques de documents) à l'aide du champ `cached_content`. Bien que les journaux de ces requêtes suivent les règles de suppression ZDR, le contexte mis en cache lui-même est stocké avec un `ttl` ou un `expire_time` défini par l'utilisateur. Pour obtenir une empreinte de données absolument nulle, n'utilisez pas la fonctionnalité cached\_content.
- **Mise en cache implicite en mémoire** : par défaut, les modèles Gemini mettent en cache les données en mémoire pour réduire la latence et les coûts pour les développeurs. Ces données sont strictement stockées dans la RAM (et non au repos), isolées au niveau du projet et ont une durée de vie de 24 heures.
  **Cela ne constitue pas une violation de la conservation zéro des données.**

## Étape suivante

- En savoir plus sur le [Règlement sur les utilisations interdites de l'IA générative](https://ai.google.dev/gemini-api/docs/Règlement sur les utilisations interdites de l'IA générative)
- Consultez les [Conditions d'utilisation supplémentaires de l'API Gemini](https://ai.google.dev/gemini-api/docs/Conditions d'utilisation supplémentaires de l'API Gemini).
- Si vous avez besoin de contrôles ZDR en libre-service de niveau entreprise, consultez le [guide Gemini Enterprise Agent Platform Zero Data Retention](https://ai.google.dev/gemini-api/docs/guide Gemini Enterprise Agent Platform Zero Data Retention).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0), et les échantillons de code sont régis par une licence [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://ai.google.dev/gemini-api/docs/Règles du site Google Developers). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?
