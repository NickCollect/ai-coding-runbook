---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=fr
fetched_at: 2026-08-17T02:23:05.747211+00:00
title: "Long contexte \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Long contexte

De nombreux modèles Gemini sont fournis avec de grandes fenêtres de contexte d'un million de jetons ou plus.
Auparavant, les grands modèles de langage (LLM) étaient considérablement limités par la quantité de texte (ou de jetons) pouvant être transmise au modèle en même temps.
La grande fenêtre de contexte de Gemini déverrouille de nombreux nouveaux cas d'utilisation et paradigmes pour les développeurs.

Le code que vous utilisez déjà pour des cas tels que la [génération de
texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr) ou les [entrées
multimodales](https://ai.google.dev/gemini-api/docs/vision?hl=fr) fonctionnera sans aucune modification avec un contexte long.

Ce document vous donne un aperçu de ce que vous pouvez réaliser à l'aide de modèles avec des fenêtres de contexte d'un million de jetons ou plus. Cette page présente brièvement une fenêtre de contexte et explique comment les développeurs doivent envisager le contexte long, divers cas d'utilisation réels pour le contexte long et les moyens d'optimiser l'utilisation de ce type de contexte.

Pour connaître la taille de la fenêtre de contexte de modèles spécifiques, consultez la
[page Modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).

## Qu'est-ce qu'une fenêtre de contexte ?

La méthode de base pour utiliser les modèles Gemini consiste à transmettre des informations (contexte) au modèle, qui générera ensuite une réponse. Une analogie pour cette fenêtre de contexte est la mémoire à court terme. Une quantité limitée d'informations peut être stockée dans la mémoire à court terme d'une personne, et il en va de même pour les modèles génératifs.

Pour en savoir plus sur le fonctionnement des modèles en coulisses, consultez notre [guide
sur les modèles génératifs](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr#under-the-hood).

## Premiers pas avec le contexte long

Les versions antérieures des modèles génératifs ne pouvaient traiter que 8 000 jetons à la fois. Les modèles plus récents ont permis d'aller plus loin en acceptant 32 000 ou même 128 000 jetons. Gemini est le premier modèle capable d'accepter un million de jetons.

En pratique, 1 million de jetons ressemblerait à ceci :

- 50 000 lignes de code (avec 80 caractères par ligne)
- Tous les SMS que vous avez envoyés au cours des cinq dernières années
- 8 romans anglais de longueur moyenne
- Transcriptions de plus de 200 épisodes de podcast de durée moyenne

Les fenêtres de contexte plus limitées courantes dans de nombreux autres modèles nécessitent souvent des stratégies telles que la suppression arbitraire d'anciens messages, la synthèse de contenu, l'utilisation de RAG avec des bases de données vectorielles ou le filtrage des requêtes pour économiser des jetons.

Bien que ces techniques restent utiles dans des scénarios spécifiques, la vaste fenêtre de contexte de Gemini invite à une approche plus directe : fournir toutes les informations pertinentes à l'avance. Étant donné que les modèles Gemini ont été conçus avec des capacités de contexte massives, ils démontrent un puissant apprentissage en contexte. Par
exemple, en utilisant uniquement des documents pédagogiques en contexte (une grammaire de référence de 500 pages,
un dictionnaire et environ 400 phrases parallèles), Gemini
[a appris à traduire](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
de l'anglais vers le kalamang (une langue papoue parlée par
moins de 200 personnes) avec une qualité semblable à celle d'un apprenant humain utilisant les mêmes
ressources. Cela illustre le changement de paradigme permis par le contexte long de Gemini, qui ouvre de nouvelles possibilités grâce à un apprentissage en contexte robuste.

## Cas d'utilisation du contexte long

Bien que le cas d'utilisation standard pour la plupart des modèles génératifs reste l'entrée textuelle, la famille de modèles Gemini permet un nouveau paradigme de cas d'utilisation multimodaux. Ces modèles peuvent comprendre nativement le texte, la vidéo, l'audio et les images. Ils sont
accompagnés de l'[API Gemini qui accepte les types de fichiers multimodaux
pour
plus de commodité.](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=fr)

### Texte long

Le texte s'est avéré être la couche d'intelligence qui sous-tend une grande partie de l'essor autour des LLM. Comme indiqué précédemment, la plupart des limites pratiques des LLM étaient dues à l'absence d'une fenêtre de contexte suffisamment grande pour effectuer certaines tâches. Cela a conduit à l'adoption rapide de la génération augmentée par récupération (RAG) et d'autres techniques qui fournissent au modèle des informations contextuelles pertinentes de manière dynamique. Désormais, avec des fenêtres de contexte de plus en plus grandes, de nouvelles techniques deviennent disponibles, ouvrant la voie à de nouveaux cas d'utilisation.

Voici quelques cas d'utilisation émergents et standards du contexte long basé sur du texte :

- Synthèse de grands corpus de texte
  - Les options de synthèse précédentes avec des modèles de contexte plus petits nécessitaient une fenêtre glissante ou une autre technique pour conserver l'état des sections précédentes lorsque de nouveaux jetons étaient transmis au modèle.
- Les questions et réponses
  - Auparavant, cela n'était possible qu'avec l'approche RAG, en raison de la quantité limitée de contexte et du faible rappel factuel des modèles.
- Workflows agentifs- Le texte est essentiel pour que les agents conservent un état de ce qu'ils ont accompli et de ce qu'ils doivent faire. Un manque d'informations sur le monde et sur les objectifs des agents limite leur fiabilité.

L'[apprentissage en contexte "multi-shot"](https://arxiv.org/pdf/2404.11018) est l'une des fonctionnalités les plus remarquables offertes par les modèles de contexte longs. Les recherches ont montré que l'utilisation du paradigme commun "one-shot" ou "multi-shot", où le modèle reçoit un ou plusieurs exemples d'une tâche, et les fait évoluer jusqu'à des centaines, des milliers, voire des centaines de milliers d'exemples, peut entraîner de nouvelles capacités pour le modèle. Cette approche "multi-shot" a également montré des performances comparables à celles des modèles qui ont été affinés pour une tâche spécifique. Pour les cas d'utilisation où les performances d'un modèle Gemini ne sont pas encore suffisantes pour un déploiement en production, vous pouvez essayer l'approche "multi-shot". Comme vous pourrez le découvrir plus tard dans la section sur l'optimisation du contexte long, la mise en cache de contexte rend ce type de charge de travail à jetons d'entrée élevés beaucoup plus économique et avec une latence encore plus faible dans certains cas.

### Vidéo longue

L'utilité du contenu vidéo a longtemps été limitée par le manque d'accessibilité du support lui-même. Il était difficile de parcourir le contenu, les transcriptions ne parviennent souvent pas à capturer les nuances d'une vidéo, et la plupart des outils ne traitent pas les images, le texte et l'audio simultanément. Avec Gemini, les fonctionnalités textuelles à contexte long se traduisent par la capacité à raisonner et à répondre aux questions sur les entrées multimodales avec des performances soutenues.

Voici quelques cas d'utilisation émergents et standards du contexte long basé sur de la vidéo :

- Questions et réponses sur la vidéo
- Mémoire vidéo, comme illustré par [le projet Astra de Google](https://deepmind.google/technologies/gemini/project-astra/?hl=fr)
- Sous-titrage vidéo
- Systèmes de recommandation vidéo, en enrichissant les métadonnées existantes grâce à une nouvelle compréhension multimodale
- Personnalisation des vidéos, en examinant un corpus de données et des métadonnées vidéo associées, puis en supprimant les parties des vidéos qui ne sont pas pertinentes pour le lecteur
- Modération de contenu vidéo
- Traitement vidéo en temps réel

Lorsque vous travaillez avec des vidéos, il est important de tenir compte de la façon dont les [vidéos sont
traitées en jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr#media-token), car cela affecte
la facturation et les limites d'utilisation. Pour en savoir plus sur les requêtes avec des fichiers vidéo, consultez
le [guide
sur les requêtes](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=fr#prompting-with-videos).

### Audio long

Les modèles Gemini étaient les premiers grands modèles de langage multimodaux natifs pouvant comprendre du contenu audio. Auparavant, le workflow de développeur classique impliquait l'association de plusieurs modèles spécifiques à un domaine, tels qu'un modèle de reconnaissance vocale et un modèle texte-vers-texte, afin de traiter le contenu audio. Cela entraînait une latence supplémentaire en raison des multiples requêtes aller-retour nécessaires, et une baisse des performances, généralement attribuée aux architectures déconnectées de la configuration à plusieurs modèles.

Voici quelques cas d'utilisation émergents et standards du contexte audio :

- Transcription et traduction en temps réel
- Questions et réponses sur un podcast/une vidéo
- Transcription et synthèse de réunions
- Assistants vocaux

Pour en savoir plus sur les requêtes avec des fichiers audio, consultez le [guide
sur les requêtes](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=fr#prompting-with-videos).

## Optimisations du contexte long

La principale optimisation lorsque vous travaillez avec un contexte long et les modèles Gemini
consiste à utiliser [la mise en cache
de contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr). Au-delà de l'impossibilité de traiter de nombreux jetons dans une seule requête auparavant, l'autre contrainte principale était le coût. Si vous disposez d'une application de type "discuter avec vos données" où un utilisateur importe 10 fichiers PDF, une vidéo et des documents de travail, vous auriez dû utiliser un outil/framework de génération augmentée par récupération (RAG) plus complexe afin de traiter ces requêtes et de payer un montant important pour les jetons déplacés dans la fenêtre de contexte. Vous pouvez désormais mettre en cache les fichiers importés par l'utilisateur et payer pour les stocker à l'heure. Le coût d'entrée / sortie par requête avec Gemini Flash, par exemple, est environ quatre fois inférieur au coût d'entrée / sortie standard. Par conséquent, si l'utilisateur discute suffisamment avec ses données, cela représente une économie considérable pour vous en tant que développeur.

## Limites de contexte long

Dans différentes sections de ce guide, nous avons expliqué comment les modèles Gemini obtiennent des performances élevées lors de différents tests de récupération de type "aiguille dans une botte de foin". Ces tests prennent en compte la configuration la plus élémentaire, dans laquelle vous recherchez une seule aiguille. Dans les cas où vous pouvez avoir plusieurs "aiguilles" ou informations spécifiques que vous recherchez, le modèle n'est pas aussi précis. Les performances peuvent varier considérablement en fonction du contexte. Il est important d'en tenir compte, car il existe un compromis inhérent entre l'obtention des bonnes informations et le coût. Vous pouvez obtenir des performances à hauteur de 99 % sur une seule requête, mais vous devez payer le coût du jeton d'entrée chaque fois que vous envoyez cette requête. Ainsi, pour récupérer 100 informations, si vous avez besoin de performances à 99 %, vous devrez probablement envoyer 100 requêtes. C'est un bon exemple de cas où la mise en cache du contexte peut réduire considérablement les coûts associés à l'utilisation des modèles Gemini tout en maintenant des performances élevées.

## Questions fréquentes

### Quel est le meilleur endroit pour placer ma requête dans la fenêtre de contexte ?

Dans la plupart des cas, en particulier si le contexte total est long, les performances du modèle seront meilleures si vous placez votre requête / question à la fin de l'invite (après tout le reste du contexte).

### Les performances du modèle sont-elles affectées lorsque j'ajoute des jetons à une requête ?

En général, si vous n'avez pas besoin que des jetons soient transmis au modèle, il est préférable d'éviter de les transmettre. Toutefois, si vous disposez d'un grand nombre de jetons contenant des informations et que vous souhaitez poser des questions à ce sujet, le modèle est tout à fait capable d'extraire ces informations (jusqu'à 99% de précision dans de nombreux cas).

### Comment puis-je réduire mes coûts avec des requêtes à contexte long ?

Si vous disposez d'un ensemble de jetons / contexte similaire que vous souhaitez réutiliser plusieurs
fois, [la mise en cache de contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) peut vous aider à réduire les coûts
associés aux questions sur ces informations.

### La longueur de contexte affecte-t-elle la latence du modèle ?

Il existe une certaine latence fixe dans toute requête, quelle que soit sa taille, mais en général, les requêtes plus longues auront une latence plus élevée (temps avant le premier jeton).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
