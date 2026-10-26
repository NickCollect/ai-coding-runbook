---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=fr
fetched_at: 2026-10-26T05:46:29.559768+00:00
title: "Erreurs d'API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Erreurs d'API

Cette page fournit une documentation de référence pour tous les codes d'erreur de l'API Interactions, décrit le format de réponse d'erreur et explique comment l'API renvoie les erreurs pour différents types de requêtes.

## Codes d'erreur de l'API Standard

Ces codes d'erreur généraux au niveau de la requête correspondent aux codes d'état HTTP standards.
Utilisez le champ `code` dans la logique de votre application pour gérer les erreurs de manière programmatique.

| Code | État HTTP | Description | Action recommandée |
| --- | --- | --- | --- |
| `invalid_request` | 400 Requête erronée | La charge utile de la requête est incorrecte ou contient des paramètres non valides. | Vérifiez la syntaxe et les paramètres de votre requête par rapport à la [documentation de référence de l'API](https://ai.google.dev/api/interactions-api?hl=fr). |
| `failed_precondition` | 400 Requête erronée | La requête ne peut pas être traitée, car une condition préalable n'est pas remplie (par exemple, la facturation est désactivée). | Vérifiez l'état de facturation du projet ou les conditions préalables du compte. |
| `out_of_range` | 416 Requested Range Not Satisfiable | Le paramètre de requête est en dehors de la plage valide. | Vérifiez les valeurs et les limites des paramètres. |
| `parameter_unknown` | 400 Requête erronée | La requête contient un paramètre inconnu. | Supprimez le paramètre non reconnu, puis réessayez. |
| `authentication` | 401 Non autorisé | La clé API est manquante, non valide ou arrivée à expiration. | Vérifiez votre [clé API](https://ai.google.dev/gemini-api/docs/api-key?hl=fr). |
| `payment_required` | 402 Paiement requis | Votre solde de crédit prépayé est épuisé. | [Ajoutez des crédits](https://ai.google.dev/gemini-api/docs/billing?hl=fr#buy-credits) à votre compte de facturation ou activez la [recharge automatique](https://ai.google.dev/gemini-api/docs/billing?hl=fr#auto-reload). Ne réessayez pas : la requête n'aboutira pas tant que des crédits n'auront pas été ajoutés. |
| `permission_denied` | 403 Interdit | Votre clé API ne dispose pas des autorisations nécessaires pour cette ressource, ou l'accès à l'API de votre projet est limité. | Vérifiez les autorisations de votre clé API, l'éligibilité de votre niveau de projet et l'état de facturation. Consultez [Résoudre les problèmes liés à un projet restreint ou indisponible](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=fr#project-unavailable). |
| `not_found` | 404 Not Found | Impossible de trouver la ressource demandée. | Vérifiez le chemin d'accès et les paramètres de la ressource. |
| `model_not_found` | 404 Not Found | Le modèle spécifié est introuvable. | Vérifiez le nom du modèle ou utilisez un autre modèle. |
| `already_exists` | 409 Conflit | L'entité que vous avez tenté de créer existe déjà. | Vérifiez si la ressource existe déjà avant de la recréer. |
| `aborted` | 409 Conflit | L'opération a été annulée en raison d'un conflit ou d'un échec de vérification de simultanéité. | Réessayez la requête à un niveau d'application plus élevé. |
| `rate_limit_exceeded` | 429 Trop de requêtes | Vous avez dépassé la limite de requêtes ou de jetons par minute ou par seconde. | Attendez et réessayez avec un intervalle exponentiel entre les tentatives. |
| `quota_exceeded` | 429 Trop de requêtes | Vous avez dépassé votre quota quotidien. | Attendez que le quota soit réinitialisé ou demandez une augmentation de quota. |
| `too_many_requests` | 429 Trop de requêtes | Vous avez effectué trop de requêtes en peu de temps. | Attendez et réessayez avec un intervalle exponentiel entre les tentatives. |
| `cancelled` | 499 Client Closed Request | Le client a annulé la requête avant qu'elle ne soit terminée. | Aucune action requise. Cela signifie généralement que le client s'est déconnecté. |
| `api_error` | 500 Erreur interne du serveur. | Une erreur inattendue s'est produite sur le serveur. | Réessayez d'envoyer la requête. Si le problème persiste, contactez l'assistance. |
| `unimplemented` | 501 Non implémenté | L'opération ou la fonctionnalité n'est pas implémentée ou n'est pas prise en charge. | Vérifiez les fonctionnalités de l'API ou passez à une fonctionnalité compatible. |
| `service_unavailable` | 503 Service indisponible. | Le service est temporairement surchargé ou indisponible. | Attendez et réessayez avec un intervalle exponentiel entre les tentatives. |
| `deadline_exceeded` | 504 Expiration du délai de la passerelle | La requête n'a pas abouti dans le délai imparti. | Supprimez ou augmentez le paramètre de délai client pour utiliser la valeur par défaut du serveur. |

## Codes bloquants de la génération

Ces codes d'erreur indiquent que des restrictions de règles, de sécurité ou de contenu ont bloqué la sortie du modèle. Lorsque vous recevez l'un de ces codes, modifiez votre saisie et réessayez.

| Code | Description |
| --- | --- |
| `safety` | Des violations des règles de sécurité (contenu nuisible) ont bloqué la requête. |
| `recitation` | La demande a été bloquée en raison de restrictions liées aux droits d'auteur ou à la récitation. |
| `language` | Une langue non acceptée a bloqué la requête. |
| `prohibited_content` | Les consignes relatives au contenu interdit ont bloqué la requête. |
| `spii` | Les restrictions concernant les informations personnelles sensibles ont bloqué la requête. |
| `blocklist` | Des termes interdits figurant sur une liste de blocage ont bloqué la requête. |
| `image_safety` | La génération d'images a été bloquée en raison d'un non-respect des règles de sécurité. |
| `image_prohibited_content` | Les consignes relatives au contenu interdit ont bloqué la génération d'images. |
| `image_recitation` | La génération d'images a été bloquée en raison de restrictions liées aux droits d'auteur ou à la récitation. |
| `image_other` | La génération d'images a été bloquée pour des raisons non spécifiées. |
| `content_blocked` | Une raison non spécifiée liée aux règles a bloqué la requête. |

## Codes d'erreur de génération

Ces codes d'erreur indiquent un problème structurel avec la sortie générée par le modèle (par exemple, un appel de fonction incorrect ou un appel d'outil non déclaré).

| Code | Description |
| --- | --- |
| `malformed_function_call` | Le modèle a produit un appel de fonction qui n'a pas pu être analysé. |
| `malformed_tool_call` | Le modèle a produit un appel d'outil qui n'a pas pu être analysé. |
| `unexpected_tool_call` | Le modèle a appelé un outil qui n'a pas été déclaré dans la requête. |
| `no_image` | Le modèle n'a pas pu générer d'image. |
| `too_many_tool_calls` | Le modèle a généré plus d'appels d'outils que le nombre autorisé. |
| `missing_thought_signature` | La réponse ne contient pas la signature de pensée requise. |

## Format de réponse d'erreur

Toutes les erreurs de l'API Interactions renvoient un objet `error` contenant un `code` et un `message`. Par exemple, si vous transmettez un type d'outil non compatible, vous obtenez le résultat suivant :

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Champ | Type | Description |
| --- | --- | --- |
| `code` | chaîne | Code d'erreur lisible par machine dans `snake_case`. |
| `message` | chaîne | Description lisible par l'humain du problème. |

## Comment les erreurs sont-elles transmises ?

L'API renvoie les erreurs différemment selon que vous effectuez une requête HTTP standard ou une requête de streaming (SSE).

### Requêtes HTTP standards

Pour les requêtes standards (non diffusées en streaming), l'API définit le code d'état de la réponse HTTP (par exemple, `400 Bad Request`, `401 Unauthorized` ou `429 Too Many Requests`) et renvoie un objet `error` dans le corps de la réponse JSON :

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Requêtes de streaming (SSE)

Pour les requêtes de streaming (`stream: true`), l'API envoie des événements d'erreur via le flux d'événements envoyés par le serveur (SSE) avec `event_type` défini sur `"error"`. Le champ `error` contient la même structure `code` et `message` :

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Pour obtenir le schéma d'événement SSE complet, consultez la [documentation de référence de l'API Interactions](https://ai.google.dev/api/interactions-api?hl=fr).

## Étape suivante

- [Résoudre les problèmes liés aux API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=fr) : résolvez les problèmes et les scénarios d'erreur courants.
- [Limites de débit](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr) : découvrez les limites de requêtes et la gestion des quotas.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/23 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/23 (UTC)."],[],[]]
