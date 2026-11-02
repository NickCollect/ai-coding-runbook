---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=fr
fetched_at: 2026-11-02T07:03:47.948230+00:00
title: "Guide de d\u00e9pannage \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Guide de dépannage

Utilisez ce guide pour diagnostiquer et résoudre les problèmes courants qui surviennent lorsque vous appelez l'API Gemini. Vous pouvez rencontrer des problèmes liés au service de backend de l'API Gemini ou aux SDK client. Nos SDK clients sont disponibles en Open Source dans les dépôts suivants :

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Si vous rencontrez des problèmes de clé API, vérifiez que vous l'avez configurée correctement en suivant le [guide de configuration de la clé API](https://ai.google.dev/gemini-api/docs/api-key?hl=fr).

## Codes d'erreur

Pour obtenir une documentation de référence complète sur tous les codes d'erreur, y compris les codes d'état HTTP, les codes bloquants de génération et les codes d'erreur de contenu, consultez la page [Erreurs d'API](https://ai.google.dev/gemini-api/docs/api-errors?hl=fr).

## Stratégie de nouvelle tentative

Si vous recevez une erreur indiquant que vous devez réessayer d'envoyer votre requête (par exemple, `429 RESOURCE_EXHAUSTED` ou `503 UNAVAILABLE`), nous vous recommandons d'implémenter une stratégie de temporisation de retransmission. Cela signifie que vous attendez un court instant avant la première nouvelle tentative, puis que vous augmentez progressivement le temps d'attente entre les tentatives suivantes.

Les SDK client officiels de l'API Gemini, tels que le [SDK Python](https://github.com/googleapis/python-genai), incluent par défaut une logique de nouvelle tentative automatique avec intervalle exponentiel entre les tentatives pour gérer les erreurs temporaires telles que les délais d'expiration, les problèmes de réseau et les limites de débit (codes d'état `429` et `5xx`). Par exemple, le SDK Python relance automatiquement les erreurs temporaires jusqu'à quatre fois, avec un délai initial d'environ une seconde et un délai maximal de 60 secondes.

Si vous effectuez des requêtes API REST directes ou si vous personnalisez votre logique de nouvelle tentative, suivez ces bonnes pratiques pour augmenter les chances de réussite d'une requête et éviter de surcharger le service :

- **Utilisez un intervalle exponentiel entre les tentatives** : attendez un court instant avant la première tentative (par exemple, une seconde), puis augmentez le délai de manière exponentielle (par exemple, 2 s, 4 s, 8 s).
- **Ajouter de la gigue** : ajoutez une "gigue" aléatoire au délai pour éviter que tous les clients ne réessayent exactement au même moment.
- **Réessayer en cas d'erreurs spécifiques** : ne réessayez qu'en cas d'erreurs temporaires (comme `429`, `408` ou `5xx`). Ne réessayez pas en cas d'erreurs client (comme `400`, `402` ou `403`), car elles indiquent des problèmes tels que des clés API non valides, des crédits prépayés épuisés ou une syntaxe incorrecte.
- **Définir un nombre maximal de tentatives** : définissez un nombre maximal de tentatives pour éviter les boucles infinies.

## Vérifier si vos appels d'API contiennent des erreurs de paramètres de modèle

Vérifiez que les paramètres de votre modèle se situent dans les valeurs suivantes :

|  |  |
| --- | --- |
| **Paramètre du modèle** | **Valeurs (plage)** |
| Nombre de candidats | 1-8 (entier, non compatible avec Gemini 3 et 4) |
| Température | 0,0-1,0 (ignoré sur Gemini 3.6+ et 4 ; conserver la valeur par défaut sur les modèles Gemini 3 antérieurs) |
| Nombre maximal de jetons de sortie | Utilisez la [page des modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr) pour déterminer le nombre maximal de jetons pour le modèle que vous utilisez. |
| TopP | 0,0-1,0 (ignoré sur Gemini 3.6+ et 4 ; conserver la valeur par défaut sur les modèles Gemini 3 antérieurs) |

En plus de vérifier les valeurs des paramètres, assurez-vous d'utiliser la bonne [version de l'API](https://ai.google.dev/gemini-api/docs/api-versions?hl=fr) (par exemple, `/v1` ou `/v1beta`) et le modèle qui prend en charge les fonctionnalités dont vous avez besoin. Par exemple, si une fonctionnalité est en version bêta, elle ne sera disponible que dans la version `/v1beta` de l'API.

## Vérifier si vous disposez du bon modèle

Vérifiez que vous utilisez un modèle compatible listé sur notre [page des modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).

## Latence ou utilisation de jetons plus élevées avec les modèles de raisonnement

Une latence ou une utilisation de jetons plus élevée se produit souvent, car les modèles Gemini 3.x ont la réflexion activée par défaut. Les modèles Gemini 2.5 obsolètes utilisent également le raisonnement par défaut.

Les modèles de raisonnement génèrent des jetons de raisonnement internes pour améliorer la qualité. Ce processus de raisonnement augmente à la fois la latence de réponse et la consommation totale de jetons.

Si vous privilégiez une latence plus faible ou si vous devez minimiser les coûts, vous pouvez réduire le niveau de réflexion ou désactiver la réflexion.

Pour obtenir des détails de configuration et des exemples de code, consultez le [guide sur le raisonnement](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#thinking-levels).

## Problèmes de sécurité

Si vous voyez qu'un prompt a été bloqué en raison d'un paramètre de sécurité dans votre appel d'API, examinez le prompt par rapport aux filtres que vous avez définis dans l'appel d'API.

Si vous voyez `BlockedReason.OTHER`, cela signifie que la requête ou la réponse peut enfreindre les [Conditions d'utilisation](https://ai.google.dev/terms?hl=fr) ou ne pas être acceptée pour une autre raison.

## Problème de récitation

Si vous constatez que le modèle cesse de générer des sorties pour la raison RECITATION, cela signifie que la sortie du modèle peut ressembler à certaines données. Pour résoudre ce problème, essayez de rendre la requête/le contexte aussi uniques que possible. Pour les modèles plus anciens qui acceptent les paramètres d'échantillonnage, vous pouvez également utiliser une température plus élevée.

## Problème de jetons répétitifs

Si vous voyez des jetons de sortie répétés, essayez les suggestions suivantes pour les réduire ou les éliminer. Les ajustements de température ne s'appliquent qu'aux modèles antérieurs compatibles avec les paramètres d'échantillonnage. Pour les modèles Gemini 3 et Gemini 4, utilisez plutôt les solutions de contournement des requêtes et des instructions système.

| Description | Cause | Solution de contournement suggérée |
| --- | --- | --- |
| Tirets répétés dans les tableaux Markdown | Cela peut se produire lorsque le contenu de la table est long, car le modèle tente de créer une table Markdown visuellement alignée. Toutefois, l'alignement dans Markdown n'est pas nécessaire pour un rendu correct. | Ajoutez des instructions à votre prompt pour donner au modèle des consignes spécifiques pour générer des tableaux Markdown. Fournissez des exemples qui respectent ces consignes. Pour les modèles antérieurs compatibles avec les paramètres d'échantillonnage, vous pouvez également essayer d'ajuster la température (>= 0,8).  Voici un exemple de consignes que vous pouvez ajouter à votre prompt pour éviter ce problème :     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Jetons répétés dans les tableaux Markdown | Comme pour les traits d'union répétés, cela se produit lorsque le modèle tente d'aligner visuellement le contenu du tableau. L'alignement dans Markdown n'est pas requis pour un rendu correct. | - Essayez d'ajouter des instructions comme celles-ci à votre prompt système :      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Pour les modèles plus anciens qui acceptent les paramètres d'échantillonnage, essayez une température plus élevée (>= 0,8) pour réduire les répétitions dans la sortie. |
| Sauts de ligne répétés (`\n`) dans la sortie structurée | Lorsque l'entrée du modèle contient des séquences Unicode ou d'échappement telles que `\u` ou `\t`, cela peut entraîner des sauts de ligne répétés. | - Recherchez et remplacez les séquences d'échappement interdites par des caractères UTF-8 dans votre requête. Par exemple, la séquence d'échappement `\u` dans vos exemples JSON peut amener le modèle à les utiliser également dans sa sortie. - Indiquez au modèle les échappements autorisés. Ajoutez une instruction système comme celle-ci :      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Texte répété lors de l'utilisation d'une sortie structurée | Lorsque l'ordre des champs dans la sortie du modèle est différent de celui du schéma structuré défini, cela peut entraîner une répétition du texte. | - Ne spécifiez pas l'ordre des champs dans votre prompt. - Rendre tous les champs de sortie obligatoires. |
| Appel d'outils répétitif | Cela peut se produire si le modèle perd le contexte des pensées précédentes et/ou appelle un point de terminaison indisponible auquel il est forcé. | Demandez au modèle de conserver l'état dans son processus de réflexion. Ajoutez ceci à la fin de vos instructions système :    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Texte répétitif qui ne fait pas partie d'une sortie structurée | Cela peut se produire si le modèle se bloque sur une requête qu'il ne peut pas résoudre. | - Si la réflexion est activée, évitez de donner des ordres explicites sur la façon de réfléchir à un problème dans les instructions. Demandez simplement le résultat final. - Pour les modèles plus anciens qui acceptent les paramètres d'échantillonnage, essayez une température plus élevée >= 0,8. - Ajoutez des instructions telles que "Sois concis", "Ne te répète pas" ou "Fournis la réponse une seule fois". |

## Projet limité ou indisponible

Si vos requêtes API renvoient `403 PERMISSION_DENIED` ("L'accès a été refusé à votre projet") ou si l'état de votre projet indique **Limité**, **Niveau sans frais indisponible**, **Paiement requis** ou **Indisponible** dans [Google AI Studio](https://aistudio.google.com/?hl=fr), vérifiez laquelle des sections suivantes s'applique à votre projet :

### Indisponibilité du niveau sans frais de l'API Gemini

Tous les projets ou comptes Google Cloud ne sont pas éligibles au niveau sans frais de l'API Gemini. Si votre projet n'est pas autorisé à utiliser le niveau sans frais :

- **La création d'une clé API dans le même projet ne résoudra pas l'erreur.**
  Google évalue l'éligibilité au niveau du projet Google Cloud.
- **Pour utiliser l'API Gemini avec ce projet, vous devez passer au niveau payant** en associant un [compte de facturation Cloud](https://aistudio.google.com/billing?hl=fr) actif.
- Remarque : Passer un projet au niveau payant ne débloque pas le quota du niveau sans frais.
  Google facture l'utilisation du niveau payant conformément aux [tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr) ou la déduit des crédits Google Cloud éligibles.

### Paiement du compte de facturation Cloud requis

Si votre projet est déjà associé à un compte de facturation Cloud et qu'il indique **Paiement requis** (ou renvoie `403 PERMISSION_DENIED` en indiquant un solde dû) :

- Accédez à la [page "Facturation" d'AI Studio](https://aistudio.google.com/billing?hl=fr) ou à la [console Cloud Billing de Google Cloud](https://console.cloud.google.com/billing?hl=fr) pour régler un solde impayé ou mettre à jour votre mode de paiement.
- Une fois que votre compte de facturation est de nouveau en règle, votre projet retrouve automatiquement l'accès à l'API.

### Clés API divulguées ou bloquées

Si l'erreur `403 PERMISSION_DENIED` indique que votre clé API a été signalée comme ayant fuité ou étant bloquée :

- Accédez à la [page des clés API AI Studio](https://aistudio.google.com/apikeys?hl=fr) pour générer une nouvelle clé API et mettre à jour les identifiants de votre application.
- N'intégrez jamais de clés API directement dans le code côté client ou dans des dépôts publics.

### Suspension d'un projet ou d'un compte de facturation pour non-respect des règles

Si Google suspend votre projet Google Cloud ou votre compte de facturation Cloud pour non-respect des règles, vérifiez l'adresse e-mail associée. Accédez à la [console Google Cloud](https://console.cloud.google.com/?hl=fr) pour consulter les avis de suspension et suivez les [consignes de suspension de projet](https://cloud.google.com/resource-manager/docs/project-suspension-guidelines?hl=fr).

## Clés API bloquées ou non fonctionnelles

Cette section explique comment vérifier si votre clé API Gemini est bloquée et comment résoudre ce problème.

### Comprendre pourquoi des clés sont bloquées

Nous avons identifié une faille qui a pu exposer publiquement certaines clés API. Pour protéger vos données et empêcher tout accès non autorisé, nous avons bloqué de manière proactive l'accès à l'API Gemini pour ces clés divulguées connues.

### Vérifier si vos clés sont concernées

Si votre clé a été divulguée, vous ne pouvez plus l'utiliser avec l'API Gemini. Vous pouvez utiliser [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=fr) pour vérifier si l'une de vos clés API est bloquée et ne peut pas appeler l'API Gemini, et générer de nouvelles clés. L'erreur suivante peut également s'afficher lorsque vous tentez d'utiliser ces clés :

```
Your API key was reported as leaked. Please use another API key.
```

### Action pour les clés API bloquées

Vous devez générer de nouvelles clés API pour vos intégrations de l'API Gemini à l'aide de [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=fr). Nous vous recommandons vivement de revoir vos pratiques de gestion des clés API pour vous assurer que vos nouvelles clés sont sécurisées et ne sont pas exposées publiquement.

### Frais inattendus dus à une faille

[Envoyez une demande d'assistance concernant la facturation.](https://console.cloud.google.com/support/chat?hl=fr)
Notre équipe chargée de la facturation s'en occupe, et nous vous tiendrons informé dès que possible.

### Mesures de sécurité de Google pour les clés divulguées

**Comment Google va-t-il m'aider à protéger mon compte contre les dépassements de coûts et les utilisations abusives en cas de fuite de mes clés API ?**

- Nous allons désormais émettre des clés API lorsque vous demandez une nouvelle clé à l'aide de [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=fr). Par défaut, ces clés seront limitées à Google AI Studio et n'accepteront pas les clés d'autres services.
  Cela permettra d'éviter toute utilisation involontaire de clés croisées.
- Par défaut, nous bloquons les clés API qui ont fuité et qui sont utilisées avec l'API Gemini, ce qui permet d'éviter l'utilisation abusive des coûts et des données de votre application.
- Vous pourrez trouver l'état de vos clés API dans [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=fr). Nous vous contacterons de manière proactive lorsque nous identifierons une fuite de vos clés API afin que vous puissiez prendre des mesures immédiates.

## Améliorer la sortie du modèle

Pour obtenir des sorties de modèle de meilleure qualité, essayez d'écrire des prompts plus structurés. La page du [guide de prompt engineering](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr) présente des concepts, des stratégies et des bonnes pratiques de base pour vous aider à vous lancer.

## Comprendre les limites de jetons

Consultez notre [guide sur les jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) pour mieux comprendre comment compter les jetons et leurs limites.

## Problèmes connus

- L'API n'est compatible qu'avec un certain nombre de langues. L'envoi de requêtes dans des langues non acceptées peut produire des réponses inattendues, voire bloquées. Consultez les [pages d'informations sur les modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr) pour connaître les mises à jour.

## Signaler un bug

Si vous avez des questions, participez à la discussion sur le [forum des développeurs Google AI](https://discuss.ai.google.dev?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/27 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/27 (UTC)."],[],[]]
