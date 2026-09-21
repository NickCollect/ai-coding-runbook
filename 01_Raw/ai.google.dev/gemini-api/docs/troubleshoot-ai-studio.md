---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=fr
fetched_at: 2026-09-21T05:46:13.080922+00:00
title: "R\u00e9soudre les probl\u00e8mes li\u00e9s \u00e0 Google\u00a0AI\u00a0Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Résoudre les problèmes liés à Google AI Studio

Cette page fournit des suggestions pour résoudre les problèmes liés à Google AI Studio.

## Comprendre les erreurs 403 "Accès limité"

Si le message d'erreur "403 Accès limité" s'affiche, cela signifie que vous utilisez Google AI Studio d'une manière qui ne respecte pas les [Conditions d'utilisation](https://ai.google.dev/terms?hl=fr). Une raison fréquente est que vous ne vous trouvez pas dans une [région où le VPN est disponible](https://ai.google.dev/available_regions?hl=fr).

## Résoudre les réponses "Aucun contenu" dans Google AI Studio

Un message warning **Aucun contenu** s'affiche dans Google AI Studio si le contenu est bloqué pour une raison quelconque. Pour en savoir plus, pointez sur **Aucun contenu**, puis cliquez sur warning **Sécurité**.

Si la réponse a été bloquée en raison des [paramètres de sécurité](https://ai.google.dev/docs/safety_setting?hl=fr) et que vous avez tenu compte des [risques de sécurité](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr) pour votre cas d'utilisation, vous pouvez modifier les [paramètres de sécurité](https://ai.google.dev/docs/safety_setting?hl=fr#safety_settings_in_makersuite) pour influencer la réponse renvoyée.

Si la réponse a été bloquée, mais pas en raison des paramètres de sécurité, il est possible que la requête ou la réponse ne respecte pas les [Conditions d'utilisation](https://ai.google.dev/terms?hl=fr) ou ne soit pas prise en charge.

## Vérifier l'utilisation et les limites des jetons

Lorsqu'une requête est ouverte, le bouton **Aperçu du texte** en bas de l'écran indique le nombre de jetons actuellement utilisés pour le contenu de votre requête et le nombre maximal de jetons pour le modèle utilisé.

## Autorisations Google Cloud IAM pour AI Studio

Les membres d'un projet Google Cloud ont besoin d'autorisations Identity and Access Management (IAM) spécifiques pour effectuer des actions dans Google AI Studio. Pour en savoir plus sur ces identités, consultez la [présentation des comptes principaux IAM](https://docs.cloud.google.com/iam/docs/principals-overview?hl=fr).

Les utilisateurs disposant des rôles **Éditeur** ou **Propriétaire** dans le projet Google Cloud associé disposent de toutes les autorisations pour afficher les tableaux de bord et gérer les clés API Gemini. Les utilisateurs disposant du rôle **Lecteur** peuvent afficher les tableaux de bord et les clés API, mais pas les créer, les modifier ni les supprimer.

Pour un contrôle plus précis, consultez le tableau suivant pour connaître les autorisations spécifiques requises pour chaque fonctionnalité AI Studio. Pour savoir comment accorder ces autorisations, consultez [Accorder, modifier et révoquer les accès à des ressources](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=fr) dans la documentation Google Cloud.

| Fonctionnalité AI Studio | Autorisations IAM requises | Exigences supplémentaires |
| --- | --- | --- |
| **Rechercher un projet** (importer des projets) | `resourcemanager.projects.get` |  |
| **Renommer le projet** | `resourcemanager.projects.update` |  |
| **Afficher le niveau de quota** | N/A |  |
| **Créer une clé API** | Disposer de l'autorisation **Rechercher dans le projet** et :  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Lister les clés API** | Disposer de l'autorisation **Rechercher dans le projet** et :  `apikeys.keys.list` `serviceusage.services.get` | L'[API Generative Language](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=fr) doit être activée pour le projet Google Cloud. |
| **Renommer des clés API** | `apikeys.keys.update` |  |
| **Supprimer des clés API** | `apikeys.keys.delete` |  |
| **Tableau de bord "Utilisation"** | Disposer de l'autorisation **Rechercher dans le projet**, et :  `monitoring.timeSeries.list` |  |
| **Tableau de bord des limites de taux** | Disposer des autorisations **Tableau de bord "Utilisation"** et :  `cloudquotas.quotas.get` |  |
| **Dépenses (plafond de facturation)** | `billing.resourceCosts.get` (pour afficher les dépenses) `billing.resourcebudgets.read` (pour afficher le plafond) `billing.resourcebudgets.write` (pour définir le plafond) |  |
| **Tableau de bord "Facturation"** | `billing.accounts.get` |  |

### Autres vérifications de l'accès

En plus des autorisations Google Cloud IAM, AI Studio effectue également des vérifications de sécurité et de conformité. Vous pouvez rencontrer une erreur `PERMISSION_DENIED` ou une erreur de restriction d'accès dans l'interface AI Studio ou dans les réponses de l'API si vous ne remplissez pas les conditions suivantes :

- **Contrôles de sécurité** : votre demande doit passer les contrôles de sécurité automatisés.
- **Conditions d'utilisation** : vous devez accepter les conditions d'utilisation de Google et les conditions d'utilisation supplémentaires de l'IA générative.
- **Région acceptée** : vous devez vous trouver dans une [région acceptée](https://ai.google.dev/gemini-api/docs/available-regions?hl=fr).
- **Confiance et sécurité** : le projet Google Cloud ne doit pas avoir été signalé pour utilisation abusive.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/12 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/12 (UTC)."],[],[]]
