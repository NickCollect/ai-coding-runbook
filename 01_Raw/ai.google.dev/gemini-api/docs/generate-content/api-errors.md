---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=fr
fetched_at: 2026-10-05T06:30:00.610526+00:00
title: "Erreurs d'API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Erreurs d'API

Cette page fournit une référence pour les codes d'erreur de backend renvoyés par l'API `GenerateContent`, décrit le format de réponse aux erreurs gRPC et fournit des étapes de dépannage.

## Codes d'erreur HTTP

Le tableau suivant répertorie les codes d'erreur de backend courants, explique leurs causes et fournit des solutions recommandées :

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Code HTTP** | **État** | **Description** | **Exemple** | **Solution** |
| 400 | INVALID\_ARGUMENT | Le corps de la requête est mal formé. | Votre demande contient une faute de frappe ou un champ obligatoire manquant. | Consultez la [documentation de référence de l'API](https://ai.google.dev/api?hl=fr) pour connaître le format des requêtes, des exemples et les versions compatibles. L'utilisation de fonctionnalités d'une version d'API plus récente avec un point de terminaison plus ancien peut entraîner des erreurs. |
| 400 | FAILED\_PRECONDITION | Le niveau sans frais de l'API Gemini n'est pas disponible dans votre pays. Veuillez activer la facturation pour votre projet dans Google AI Studio. | Vous effectuez une requête dans une région où le niveau sans frais n'est pas disponible et vous n'avez pas activé la facturation pour votre projet dans Google AI Studio. | Pour utiliser l'API Gemini, vous devez configurer un forfait payant à l'aide de [Google AI Studio](https://aistudio.google.com/apikey?hl=fr). |
| 402 | RESOURCE\_EXHAUSTED | Votre solde de crédits prépayés est épuisé. | Votre compte de facturation n'a plus de crédits prépayés. Par conséquent, toutes les clés API associées à ce compte de facturation cessent de fonctionner. | [Ajoutez des crédits](https://ai.google.dev/gemini-api/docs/billing?hl=fr#buy-credits) à votre compte de facturation ou activez la [recharge automatique](https://ai.google.dev/gemini-api/docs/billing?hl=fr#auto-reload). Ne réessayez pas cette requête : elle n'aboutira pas tant que des crédits n'auront pas été ajoutés. |
| 403 | PERMISSION\_DENIED | Votre clé API ne dispose pas des autorisations requises. | Vous utilisez une clé API incorrecte ou vous essayez d'utiliser un modèle ajusté sans [authentification appropriée](https://ai.google.dev/gemini-api/docs/model-tuning?hl=fr). | Vérifiez que votre clé API est définie et qu'elle dispose des droits d'accès appropriés. Assurez-vous également de passer par une authentification appropriée pour utiliser les modèles ajustés. |
| 404 | NOT\_FOUND | La ressource demandée est introuvable. | Un fichier image, audio ou vidéo référencé dans votre demande est introuvable. | Vérifiez que tous les paramètres de votre requête sont valides pour votre version de l'API. |
| 429 | RESOURCE\_EXHAUSTED | Vous avez dépassé l'une des limites de débit de l'API (RPM, TPM, RPD, dépenses, etc.). | Vous envoyez trop de requêtes, utilisez trop de jetons ou dépassez les limites basées sur les dépenses pour l'historique de facturation et le niveau de votre compte. | Vérifiez que vous respectez les [limites de fréquence](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr) du modèle. Patientez un peu, puis réessayez. Réduisez la fréquence ou la taille de vos requêtes. [Demandez une augmentation de la limite de fréquence](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr#request-rate-limit-increase) si nécessaire. |
| 499 | ANNULÉ | L'opération a été annulée, généralement par l'appelant. | Le client a fermé la connexion avant que l'API n'ait pu terminer de répondre. | Vérifiez si votre client ou votre infrastructure réseau ferme prématurément la connexion (par exemple, en raison d'un délai d'expiration côté client). |
| 500 | INTERNE | Une erreur inattendue s'est produite du côté de Google. | Le contexte de votre saisie est trop long. | Consultez la [page d'état de l'API Gemini](https://aistudio.google.com/status?hl=fr) pour connaître les éventuels incidents en cours. Réduisez le contexte d'entrée ou passez temporairement à un autre modèle (par exemple, de Gemini 2.5 Pro à Gemini 2.5 Flash) pour voir si cela fonctionne. Vous pouvez également patienter un instant, puis réessayer. Si le problème persiste après plusieurs tentatives, veuillez le signaler à l'aide du bouton **Envoyer des commentaires** dans Google AI Studio. |
| 503 | UNAVAILABLE | Il est possible que le service soit temporairement surchargé ou indisponible. | Le service est temporairement saturé. | Consultez la [page d'état de l'API Gemini](https://aistudio.google.com/status?hl=fr) pour connaître les éventuels incidents en cours. Passez temporairement à un autre modèle (par exemple, de Gemini 2.5 Pro à Gemini 2.5 Flash) et vérifiez si cela fonctionne. Vous pouvez également patienter un instant, puis réessayer. Si le problème persiste après plusieurs tentatives, veuillez le signaler à l'aide du bouton **Envoyer des commentaires** dans Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Le service n'est pas en mesure de terminer le traitement dans les délais. | Votre requête (ou contexte) est trop volumineuse pour être traitée à temps. | Définissez un délai d'attente plus long dans votre requête client pour éviter cette erreur. |

## Format de la réponse d'erreur

Lorsqu'une requête `GenerateContent` échoue, l'API définit le code d'état HTTP (tel que `400 Bad Request`, `403 Forbidden` ou `429 Too Many Requests`) et renvoie un corps de réponse JSON contenant les détails de l'état gRPC :

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Champ | Type | Description |
| --- | --- | --- |
| `code` | entier | Code d'état HTTP. |
| `message` | chaîne | Description de l'erreur lisible par l'utilisateur. |
| `status` | chaîne | Code d'état gRPC dans `SCREAMING_CASE`. |
| `details` | tableau | Contexte d'erreur supplémentaire, tel que `ErrorInfo` ou `LocalizedMessage`. |

## Étape suivante

- [Dépannage de l'API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=fr) : résolvez les problèmes et les scénarios d'erreur courants.
- [Limites de débit](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr) : découvrez les limites de requêtes et la gestion des quotas.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/20 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/20 (UTC)."],[],[]]
