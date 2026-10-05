---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=fr
fetched_at: 2026-10-05T06:43:49.301238+00:00
title: "Journalisation et partage des donn\u00e9es \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Journalisation et partage des données

Cette page décrit le stockage et la gestion des
[journaux de l'API Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr), qui sont des données d'API appartenant aux développeurs et provenant d'appels d'API Gemini compatibles pour les projets pour lesquels la facturation est activée. Les journaux couvrent l'ensemble du processus, de la requête d'un utilisateur à la réponse du modèle.
Ces journaux, qui sont privés pour votre projet Google Cloud, sont distincts de tous les
journaux conservés uniquement à des fins de [surveillance des abus](https://ai.google.dev/gemini-api/docs/usage-policies?hl=fr).

## Données pouvant être partagées

En tant que propriétaire d'un projet, vous pouvez choisir d'activer la journalisation des appels d'API Gemini pour votre propre usage ou pour nous envoyer des commentaires et les partager avec Google afin de nous aider à améliorer continuellement nos modèles.

Si vous activez la journalisation, vous pouvez nous aider à créer des systèmes d'IA qui continuent d'être utiles aux développeurs dans divers domaines et cas d'utilisation en choisissant de fournir les données suivantes pour améliorer les produits et l'entraînement de modèle :

- **Ensembles de données** : utilisez l'interface "Journaux et ensembles de données" de Google AI Studio pour choisir les journaux (requêtes, réponses, métadonnées, etc.) qui vous intéressent parmi les appels d'API Gemini compatibles. Ils sont fournis par inclusion dans des ensembles de données, avec la possibilité de désactiver cette option lors de la création de l'ensemble de données.
- **Commentaires** : lorsque vous examinez les journaux, vous pouvez laisser des commentaires, y compris des évaluations positives ou négatives et des commentaires écrits.

Lorsque vous partagez un ensemble de données avec Google, vos journaux dans cet ensemble de données, y compris
les requêtes et les réponses, sont traités conformément à nos
[Conditions d'utilisation](https://developers.google.com/terms?hl=fr) des
"[Services non payants](https://ai.google.dev/gemini-api/terms?hl=fr#data-use-unpaid)".
Cela signifie que l'ensemble de données peut être utilisé pour développer et améliorer les
produits, services et technologies de machine learning de Google, y compris pour améliorer et
entraîner nos modèles. **N'incluez pas d'informations personnelles, sensibles ou confidentielles.**

## Comment vos données sont-elles utilisées ?

Les journaux sont conservés pendant une période maximale par défaut de 55 jours. Passé ce délai, ils sont automatiquement marqués pour suppression. La période de conservation du stockage d'un projet peut être mise à jour dans AI Studio pour marquer automatiquement les journaux pour suppression après 7, 14, 28 ou 55 jours.

[Des ensembles de données](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr) peuvent être créés pour conserver les journaux qui vous intéressent au-delà de la période de conservation définie pour les cas d'utilisation en aval et pour contribuer de manière facultative à l'amélioration des modèles. Les journaux stockés dans les ensembles de données n'ont pas de période de conservation définie.

Par défaut, étant donné que la journalisation n'est disponible que pour les projets pour lesquels la facturation est activée,
les requêtes et les réponses contenues dans les journaux ne sont pas utilisées pour améliorer ou
développer les produits, conformément à nos [conditions d'utilisation des données](https://developers.google.com/terms?hl=fr).

Si vous choisissez de partager des ensembles de données de vos journaux avec Google, ces ensembles de données seront utilisés comme données de démonstration réelles pour mieux comprendre la diversité des domaines et des contextes dans lesquels les systèmes et applications d'IA sont utilisés. Ces données peuvent être utilisées pour améliorer la qualité des modèles et pour informer l'entraînement et l'évaluation des futurs modèles et services. Ces données sont traitées conformément à nos conditions d'utilisation des données
pour les [services non payants](https://ai.google.dev/gemini-api/terms?hl=fr#data-use-unpaid).

Par conséquent, des réviseurs humains peuvent lire, annoter et traiter les entrées et sorties d'API que vous partagez. Avant que les données ne soient utilisées pour améliorer les modèles, Google prend les mesures nécessaires pour protéger la confidentialité des utilisateurs dans le cadre de ce processus. Entre autres, ces données sont dissociées de votre compte Google, de votre clé API et de votre projet Cloud avant que les réviseurs les voient ou les annotent.

## Data permissions

En choisissant de contribuer aux données d'API, vous confirmez que vous disposez des autorisations nécessaires pour que Google traite et utilise les données comme décrit dans cette documentation. **Veuillez ne pas fournir de journaux contenant des informations sensibles, confidentielles ou propriétaires obtenues via le service payant.**
La licence que vous accordez à Google en vertu de la section "[Envoi de contenu](https://developers.google.com/terms?hl=fr#b_submission_of_content)"
des Conditions des API englobe également, dans les limites autorisées par la loi applicable
pour leur utilisation par Google, tous les contenus que vous transmettez aux Services (par exemple, les requêtes, y compris les instructions système
associées, le contenu mis en cache et les fichiers tels que les images, les vidéos ou les documents)
et les réponses générées.

## Partage de données et commentaires

Vous pouvez nous aider à faire progresser la recherche sur l'IA, l'API Gemini et Google AI Studio en choisissant de partager vos données à titre d'exemples. Cela nous permettra d'améliorer continuellement nos modèles dans différents contextes et de créer des systèmes d'IA qui continueront d'être utiles aux développeurs dans divers domaines et cas d'utilisation.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/08 (UTC)."],[],[]]
