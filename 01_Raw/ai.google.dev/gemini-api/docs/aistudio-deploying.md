---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=fr
fetched_at: 2026-05-25T05:22:44.756024+00:00
title: "D\u00e9ployer depuis Google AI\u00a0Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Déployer depuis Google AI Studio

Google AI Studio vous permet de déployer vos applications Full Stack directement depuis le mode Création. Vous pouvez ainsi passer rapidement d'un prototype à un environnement de production géré et évolutif.

## Options de déploiement

Pour déployer votre application à partir du mode Création d'AI Studio, les exigences dépendent du niveau que vous utilisez :

- [**Niveau Starter de Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=fr):
  vous permet de publier jusqu'à deux applications Full Stack sans configurer de
  projet Google Cloud ni de compte de facturation.
- **Déploiement standard** : nécessite un projet Google Cloud associé à votre
  compte AI Studio et la facturation activée pour ce projet.

## À propos du niveau Starter

Le niveau Starter de Google Cloud vous permet de déployer des applications sur Google Cloud directement depuis Google AI Studio sans configurer d'environnement Google Cloud complet ni de compte de facturation.

Chaque déploiement Google AI Studio crée un service correspondant dans Cloud Run. Pour les services déployés dans Google AI Studio avec le niveau Starter, les limites suivantes s'appliquent :

- Vous pouvez déployer jusqu'à deux services.
- Vos services sont déployés dans une
  [seule région Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=fr).

## Étapes de déploiement du niveau Starter

Après avoir conçu votre application en mode Création, déployez-la avec le niveau Starter :

1. Cliquez sur le bouton **Publier** en haut à droite.
2. Cliquez sur **Commencer**.
3. Cliquez sur **Publier l'application**.

Une fois le déploiement terminé, AI Studio fournit une URL Cloud Run vous permettant d'accéder à votre application en direct.

## Déploiement standard

À mesure que vos applications évoluent, vous pouvez avoir besoin de fonctionnalités allant au-delà du niveau Starter, telles que des quotas plus élevés, des ressources de calcul accrues ou d'autres produits Google Cloud non disponibles dans le niveau Starter. Pour déverrouiller ces fonctionnalités, vous pouvez convertir votre projet entièrement géré de niveau Starter en projet Google Cloud standard.

Vous pouvez ainsi effectuer une mise à l'échelle sans difficulté et sans perdre votre progression. Suivez les étapes pour
[créer un compte de facturation Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=fr#create-new-billing-account),
accepter formellement les conditions d'utilisation standards de Google Cloud et
[passer à un projet Google Cloud standard](https://docs.cloud.google.com/docs/starter-tier?hl=fr#upgradee).
Pour en savoir plus, consultez
[Configuration des comptes payants](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=fr#paid-setup).

Pour en savoir plus sur les niveaux de facturation, consultez [Facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr).

## Supprimer votre application

Si vous n'avez plus besoin de votre application, vous pouvez la supprimer dans Google AI Studio en suivant ces instructions :

1. Dans Google AI Studio, accédez à la page "
   [Applications](https://aistudio.google.com/app/apps?hl=fr)".
2. Dans le menu de gauche, sélectionnez **Applications**.
3. Pointez sur l'application que vous souhaitez supprimer.
4. Cliquez sur l'icône en forme de corbeille à droite de la ligne pour supprimer l'application.

## Étape suivante

- En savoir plus sur le
  [niveau Starter de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=fr).
- En savoir plus sur [la facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr) dans l'API Gemini

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/16 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/16 (UTC)."],[],[]]
