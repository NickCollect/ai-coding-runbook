---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr
fetched_at: 2026-10-12T06:49:53.608187+00:00
title: "Limites de d\u00e9bit \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Limites de débit

Les limites de débit régissent le nombre de requêtes que vous pouvez envoyer à l'API Gemini au cours d'une période donnée. Ces limites permettent de maintenir une utilisation équitable, de protéger contre les utilisations abusives et de préserver les performances du système pour tous les utilisateurs.

[Afficher vos limites de fréquence actives dans AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=fr)

## Fonctionnement des limites de fréquence

Les limites de débit sont généralement mesurées selon trois dimensions :

- Requêtes par minute (**RPM**)
- Jetons par minute (entrée) (**TPM**)
- Requêtes par jour (**RPD**)

Votre utilisation est évaluée par rapport à chaque limite. Si vous dépassez l'une d'elles, une erreur de limitation du débit se déclenchera. Par exemple, si votre limite de requêtes par minute est de 20, vous recevrez un message d'erreur si vous envoyez 21 requêtes en une minute, même si vous n'avez pas dépassé votre limite de requêtes par minute ni d'autres limites.

Les limites de débit sont appliquées par projet, et non par clé API. Les quotas de **RPD** sont réinitialisés à minuit (heure du Pacifique).

Les limites varient en fonction du modèle spécifique utilisé, et certaines limites ne s'appliquent qu'à certains modèles. Par exemple, les images par minute (IPM) ne sont calculées que pour les modèles capables de générer des images (Nano Banana), mais sont conceptuellement similaires aux TPM. D'autres modèles peuvent avoir une limite de jetons par jour.

Les limites de débit sont plus restreintes pour les modèles expérimentaux et en version preview.

### Limites de débit basées sur les dépenses

En plus des limites de requêtes par minute (RPM) et de jetons par minute (TPM), l'API Gemini applique des limites de débit basées sur les dépenses pour se protéger contre les frais inattendus. L'application de ces limites à votre compte dépend de votre historique de facturation et de votre [niveau d'utilisation](#usage-tiers).

Le tableau suivant indique les limites de débit basées sur les dépenses pour chaque [niveau d'utilisation](#usage-tiers). Ces limites sont évaluées sur une période de 10 minutes. L'application de ces limites à votre compte dépend de votre historique de facturation et de l'état de votre compte.

| Niveau d'utilisation | Limite du taux de dépenses (par tranche de 10 minutes) |
| --- | --- |
| **Free** | N/A |
| **Niveau 1** | 10 $ |
| **Niveau 2** | 50 $ |
| **Niveau 3** | 200 $ |

Si vous atteignez une limite de débit basée sur les dépenses, l'API renvoie une erreur `429 RESOURCE_EXHAUSTED`. Pour remédier à ce problème, procédez comme suit :

- **Patientez quelques instants, puis réessayez.**
- **Réduisez le taux de requêtes coûteuses**, par exemple en utilisant des fenêtres de contexte plus petites ou des sorties plus courtes.
- Si vous atteignez régulièrement cette limite lors d'une utilisation normale, [demandez une augmentation de la limite de débit](#request-rate-limit-increase).

## Niveaux d'utilisation

Les limites de débit sont liées au niveau d'utilisation du projet. À mesure que votre utilisation et vos dépenses d'API augmentent, vous passez automatiquement à un niveau supérieur avec des limites de débit plus élevées.

Les critères d'éligibilité aux niveaux 2 et 3 sont basés sur les dépenses cumulées totales pour les services Google Cloud (y compris, mais sans s'y limiter, l'API Gemini) pour le compte de facturation associé à votre projet.

| Niveau d'utilisation | Qualification | [Plafond du niveau de facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr#tier-spend-caps) |
| --- | --- | --- |
| **Free** | [Projet actif](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) ou essai sans frais | N/A |
| **Niveau 1** | [Configurer et associer un compte de facturation actif](https://ai.google.dev/gemini-api/docs/billing?hl=fr#setup-billing) | 250 $ |
| **Niveau 2** | Paiement de 100 $ + 3 jours après le premier paiement réussi | 2 000 $ |
| **Niveau 3** | Paiement de 1 000 $ + 30 jours à compter du premier paiement réussi | 20 000 $ – 100 000 $ et plus |

Bien que le respect des critères d'éligibilité indiqués soit généralement suffisant pour l'approbation, il peut arriver, dans de rares cas, qu'une demande de mise à niveau soit refusée en fonction d'autres facteurs identifiés lors de la procédure d'examen.

Ce système permet de préserver la sécurité et l'intégrité de la plate-forme de l'API Gemini pour tous les utilisateurs.

## Limites de débit de l'API Gemini

Les limites de débit dépendent de différents facteurs (comme votre niveau d'utilisation) et peuvent être consultées dans Google AI Studio. Vos limites de débit seront automatiquement mises à jour en fonction de votre niveau et de l'état de votre compte.

[Afficher vos limites de fréquence actives dans AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=fr)

Les limites de débit spécifiées ne sont pas garanties et la capacité réelle peut varier.

## Limites de débit pour l'inférence de priorité

La consommation [prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr) conserve ses propres limites de débit, même si la consommation est comptabilisée dans les limites de débit globales du trafic interactif. **Les limites de débit par défaut sont les suivantes : 0,3 fois la [limite de débit standard](https://aistudio.google.com/rate-limit?hl=fr) pour chaque modèle et niveau**

## Limites de débit de l'API Batch

Les requêtes [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) sont soumises à leurs propres limites de débit, distinctes de celles des appels d'API non par lot.

- **Requêtes par lot simultanées** : 100
- **Taille maximale du fichier d'entrée** : 2 Go
- **Limite de stockage de fichiers** : 20 Go
- **Jetons mis en file d'attente par modèle** : le tableau **Jetons mis en file d'attente par lot** indique le nombre maximal de jetons pouvant être mis en file d'attente pour le traitement par lot dans tous vos jobs par lot actifs pour un modèle donné.

### Niveau 1

| Modèle | Jetons en file d'attente par lot |
| --- | --- |
| Modèles de sortie de texte | | | | |
| --- | --- | --- | --- | --- |
| Preview Gemini 3.1 Pro | 5 000 000 |
| Gemini 3.5 Flash-Lite | 10 000 000 |
| Gemini 3.8 Flash | 3 000 000 |
| Gemini 3.1 Flash-Lite | 10 000 000 |
| Preview Gemini 3.1 Flash-Lite | 10 000 000 |
| Gemini 3.6 Flash | 3 000 000 |
| Gemini 2.5 Pro | 5 000 000 |
| Gemini 2.5 Pro TTS | 25 000 |
| Gemini 2.5 Flash | 3 000 000 |
| Preview Gemini 2.5 Flash | 3 000 000 |
| Preview Gemini 2.5 Flash Image | 3 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash-Lite | 10 000 000 |
| Preview Gemini 2.5 Flash-Lite | 10 000 000 |
| Gemini 2.0 Flash | 10 000 000 |
| Image Gemini 2.0 Flash | 3 000 000 |
| Gemini 2.0 Flash-Lite | 10 000 000 |
| Modèles de génération multimodale | | | | |
| Preview de l'image Gemini 3.1 Flash 🍌 | 1 000 000 |
| Image Gemini 3.1 Flash Lite 🍌 | 2 000 000 |
| Preview Gemini 3 Pro Image 🍌 | 2 000 000 |
| Modèles d'embeddings | | | | |
| Embedding Gemini | 500 000 |

### Niveau 2

| Modèle | Jetons en file d'attente par lot |
| --- | --- |
| Modèles de sortie de texte | | | | |
| --- | --- | --- | --- | --- |
| Preview Gemini 3.1 Pro | 500 000 000 |
| Gemini 3.5 Flash-Lite | 500 000 000 |
| Gemini 3.1 Flash-Lite | 500 000 000 |
| Preview Gemini 3.1 Flash-Lite | 500 000 000 |
| Gemini 3.8 Flash | 400 000 000 |
| Gemini 3.6 Flash | 400 000 000 |
| Gemini 2.5 Pro | 500 000 000 |
| Gemini 2.5 Pro TTS | 100 000 |
| Gemini 2.5 Flash | 400 000 000 |
| Preview Gemini 2.5 Flash | 400 000 000 |
| Preview Gemini 2.5 Flash Image | 400 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash-Lite | 500 000 000 |
| Preview Gemini 2.5 Flash-Lite | 500 000 000 |
| Gemini 2.0 Flash | 1 000 000 000 |
| Image Gemini 2.0 Flash | 400 000 000 |
| Gemini 2.0 Flash-Lite | 1 000 000 000 |
| Modèles de génération multimodale | | | | |
| Preview de l'image Gemini 3.1 Flash 🍌 | 250 000 000 |
| Image Gemini 3.1 Flash Lite 🍌 | 270 000 000 |
| Preview Gemini 3 Pro Image 🍌 | 270 000 000 |
| Modèles d'embeddings | | | | |
| Embedding Gemini | 5 000 000 |

### Niveau 3

| Modèle | Jetons en file d'attente par lot |
| --- | --- |
| Modèles de sortie de texte | | | | |
| --- | --- | --- | --- | --- |
| Preview Gemini 3.1 Pro | 1 000 000 000 |
| Gemini 3.5 Flash-Lite | 1 000 000 000 |
| Gemini 3.1 Flash-Lite | 1 000 000 000 |
| Preview Gemini 3.1 Flash-Lite | 1 000 000 000 |
| Gemini 3.8 Flash | 1 000 000 000 |
| Gemini 3.6 Flash | 1 000 000 000 |
| Gemini 2.5 Pro | 1 000 000 000 |
| Gemini 2.5 Pro TTS | 1 000 000 |
| Gemini 2.5 Flash | 1 000 000 000 |
| Preview Gemini 2.5 Flash | 1 000 000 000 |
| Preview Gemini 2.5 Flash Image | 1 000 000 000 |
| Gemini 2.5 Flash TTS | 4 000 000 |
| Gemini 2.5 Flash-Lite | 1 000 000 000 |
| Preview Gemini 2.5 Flash-Lite | 1 000 000 000 |
| Gemini 2.0 Flash | 5 000 000 000 |
| Image Gemini 2.0 Flash | 1 000 000 000 |
| Gemini 2.0 Flash-Lite | 5 000 000 000 |
| Modèles de génération multimodale | | | | |
| Preview de l'image Gemini 3.1 Flash 🍌 | 750 000 000 |
| Image Gemini 3.1 Flash Lite 🍌 | 1 000 000 000 |
| Preview Gemini 3 Pro Image 🍌 | 1 000 000 000 |
| Modèles d'embeddings | | | | |
| Embedding Gemini | 10 000 000 |

## Passer au niveau supérieur

Pour passer du niveau sans frais à un niveau payant, vous devez d'abord [configurer la facturation dans AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=fr).

Une fois que votre projet répond aux [critères spécifiés](#usage-tiers), il est automatiquement mis à niveau vers le niveau supérieur. Les mises à niveau du niveau sans frais vers le niveau 1 prennent généralement effet instantanément, et les mises à niveau vers les niveaux suivants prennent effet dans les 10 minutes. Accédez à la [page "Projets"](https://aistudio.google.com/projects?hl=fr) dans AI Studio pour vérifier vos niveaux.

## Demander une augmentation de la limite de débit

Chaque variante de modèle est associée à une limite de fréquence (requêtes par minute, RPM).
Pour en savoir plus sur ces limites de débit, consultez la page [Limites de débit d'AI Studio](https://aistudio.google.com/rate-limit?hl=fr).

[Demander une augmentation de la limite de débit du niveau payant](https://forms.gle/ETzX94k8jf7iSotH9)

Nous ne pouvons pas vous garantir que nous augmenterons votre limite de fréquence, mais nous ferons de notre mieux pour examiner votre demande.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/09 (UTC)."],[],[]]
