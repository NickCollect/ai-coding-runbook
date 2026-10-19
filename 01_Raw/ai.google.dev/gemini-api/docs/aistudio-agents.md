---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=fr
fetched_at: 2026-10-19T05:56:30.793284+00:00
title: "Agents dans l'atelier AI\u00a0Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Agents dans l'atelier AI Studio

Google AI Studio Playground fournit une interface visuelle pour prototyper et apprendre à créer des agents gérés sans avoir à créer ni à écrire d'appels d'API.

Pour commencer, accédez à l'onglet **Playground** dans le panneau de navigation de Google AI Studio, puis activez le bouton **Agents**.

## Modèles prédéfinis

L'onglet **Agents** comporte une série de modèles qui préconfigurent l'agent Antigravity de base en définissant les configurations d'outil et d'environnement. Tous les modèles sont Open Source et publiés sous
le [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/) dépôt. L'exploration de ces modèles est un excellent moyen d'apprendre à créer et à structurer votre propre agent géré.

Par exemple, lorsque vous sélectionnez le modèle AI Radio, il active tous les outils autorisés et associe un fichier `AGENTS.md` spécialisé ainsi que des compétences pour la production d'émissions de radio. Vous pouvez afficher ces paramètres dans l'interface utilisateur de Playground, dans la section **Environnement** , en cliquant sur le bouton **Sources**.

.

## Configuration de l'outil

Dans les paramètres de l'agent de Playground, vous pouvez activer ou désactiver l'accès aux outils intégrés suivants :

- **Recherche Google** : accédez au Web ouvert pour l'ancrage d'informations en temps réel.
- **Contexte d'URL** : récupérez et analysez le contenu textuel d'URL de pages Web spécifiques.
- **Exécution de code** : exécutez des commandes Bash et Python directement dans l'environnement de bac à sable isolé.
- **Outils de système de fichiers** : lisez, écrivez, listez et supprimez des fichiers dans l'espace de travail.

## Configuration de l'environnement

Les agents gérés s'exécutent dans un bac à sable Linux éphémère et sécurisé (l'environnement) qui fournit l'espace de travail et les outils dont ils ont besoin pour fonctionner. Pour en savoir plus, consultez le guide de l'environnement d'agent [géré](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr).

### Contrôler le comportement de l'agent

Le comportement, la personnalité et les capacités de l'agent sont principalement déterminés par les fichiers présents dans son environnement. L'agent détecte et charge automatiquement les configurations à partir d'un dossier `.agents` spécial :

- **`AGENTS.md`**: préchargé dans le contexte de l'agent pour définir les instructions système et la personnalité.
- **`SKILL.md`** : situé dans les dossiers de compétences respectifs (par exemple, `.agents/skills/my-skill/SKILL.md`) pour définir des capacités et des workflows spécifiques.

### Provisionner l'environnement

Vous pouvez configurer l'environnement à utiliser par l'agent en montant des fichiers dans l'environnement avant de démarrer une session. Vous pouvez créer un environnement en montant des sources ou en restaurer un précédent :

- **Pour créer un environnement**, cliquez sur **Ajouter des sources** dans le panneau des paramètres d'environnement, puis choisissez parmi les types de sources suivants :

| Type de source | Description | Chemin de montage |
| --- | --- | --- |
| **Fichiers intégrés** | Écrivez ou collez des fichiers de configuration, des ensembles de données fictifs ou des scripts utilitaires (jusqu'à 100 Ko) directement dans l'interface utilisateur de Playground. | Chemin de destination défini par l'utilisateur (par exemple, `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Montez un bucket Cloud Storage public ou privé.  Les buckets privés nécessitent un jeton porteur OAuth 2.0 standard. Pour en savoir plus, consultez la section [Sources privées](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#private-sources). | Mappe un chemin d'accès à un bucket GCS (par exemple, `gs://your-bucket-name/data/`) vers un répertoire d'espace de travail (par exemple, `/workspace/data/`). |
| **Dépôts GitHub** | Clonez des bases de code publiques ou privées.  Les dépôts privés nécessitent une authentification de base avec votre jeton d'accès personnel (PAT) GitHub. Pour en savoir plus, consultez la section [Sources privées](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#private-sources). | Cloné directement dans `/workspace/` (généralement sous `/workspace/<repo-name>`). |

- **Pour restaurer un environnement précédent**, vous pouvez [réutiliser un ID d'environnement existant](#reusing-an-existing-environment-id) pour cloner et dupliquer son état exact.

### Réutiliser un ID d'environnement existant

Si vous avez déjà configuré un environnement de bac à sable, vous n'avez pas besoin de recommencer à zéro. Pour utiliser un environnement existant :

1. Accédez au panneau "Environnements" dans AI Studio, puis activez le bouton **Type** sur **Existant**.
2. Saisissez l'**ID d'environnement** (par exemple, `env_abc123`).

Pour en savoir plus, consultez la section [Configurer un environnement](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#configure-an-environment). Vous pouvez également récupérer l'ID d'environnement de la session en cours à partir de l'onglet "Environnement" de l'interface utilisateur.

Une fois que vous avez envoyé votre premier message à l'agent, la configuration de l'environnement est fixe pour cette session. Vous ne pouvez pas monter de nouvelles sources ni modifier la liste d'autorisation du réseau pendant que l'interaction est en cours d'exécution.

## Télécharger l'environnement

Une fois un environnement créé, vous pouvez télécharger son instantané à tout moment à l'aide du bouton **Télécharger** dans les paramètres d'environnement d'AI Studio Playground pour récupérer les fichiers d'environnement sous forme de fichier tar.

## Sécurité et gestion des coûts

### Gérer la consommation de jetons

Contrairement à une requête de chat standard qui produit une seule sortie, l'agent Antigravity exécute un workflow autonome. Il planifie, exécute du code, observe les résultats et itère. Cela signifie qu'un seul prompt peut entraîner une consommation illimitée de jetons.

Pour gérer les coûts, **fournissez des critères d'arrêt clairs dans vos prompts et limitez les tâches de l'agent**. Un bon exemple pourrait être une invite de commande telle que *Vérifiez la demande d'extraction et arrêtez-vous une fois que vous avez généré le résumé Markdown.
N'essayez pas d'écrire le correctif vous-même*.

### Coûts supplémentaires

Par défaut, tous les modèles d'agent de Playground ont accès au service de l'API Gemini et peuvent effectuer des appels d'API à partir de l'environnement pour répondre aux requêtes. Cela peut entraîner des coûts supplémentaires qui ne seront pas reflétés dans la consommation de jetons.

De même, si vous ajoutez d'autres services externes, l'agent peut entraîner des coûts supplémentaires en appelant ces services en votre nom.

### Liste d'autorisation du réseau

Par défaut, dans AI Studio, toutes les requêtes réseau sortantes de l'environnement de bac à sable de votre agent sont étroitement contrôlées et limitées pour garantir la sécurité. Pour autoriser votre agent à accéder à des API externes, à des services Web ou à des gestionnaires de paquets, vous devez les déclarer explicitement :

1. Accédez au panneau "Environnements" dans AI Studio.
2. Sélectionnez le bouton **Règles** à côté de **Réseau**.
3. Dans le panneau **Configuration réseau** , cliquez sur **Ajouter à la liste d'autorisation** , puis saisissez les informations pertinentes :
   - **Restriction de domaine** : seule la machine virtuelle de l'agent peut accéder aux domaines spécifiques ou aux modèles de caractères génériques ajoutés à la liste. Par exemple, vous pouvez saisir des domaines exacts tels que `api.github.com` ou des modèles généraux tels que `*.googleapis.com`.
   - **Ajouter un en-tête HTTP et une injection de jeton** : utilisez l'option **Ajouter un en-tête HTTP** pour injecter de manière sécurisée les identifiants requis (tels qu'un jeton d'API) pour un domaine spécifique. Ces identifiants passent en toute sécurité par un proxy de sortie et ne sont jamais exposés directement sous forme de texte brut dans le bac à sable de l'agent.

Soyez toujours prudent lorsque vous ajoutez des domaines à votre liste d'autorisation. Accorder à l'agent l'accès à des services authentifiés signifie qu'il peut agir en votre nom, ce qui peut entraîner des actions involontaires si vous ne le surveillez pas attentivement.

### Bonnes pratiques concernant les identifiants

Si votre workflow nécessite que l'agent s'authentifie auprès de services externes, vous êtes responsable du provisionnement et de la définition du champ d'application de ces identifiants. Suivez ces consignes pour réduire les risques :

- **Utilisez des identifiants avec le principe du moindre privilège** : créez des comptes de service ou des clés API avec uniquement les autorisations dont votre agent a besoin. Évitez de transmettre des identifiants avec un accès étendu ou administratif.
- **Privilégiez les jetons de courte durée** : dans la mesure du possible, utilisez des identifiants ou des jetons à durée limitée qui expirent plutôt que des clés API à longue durée de vie.
- **Partez du principe que l'accès est complet** : l'agent peut utiliser n'importe quel identifiant auquel il a accès pour effectuer la tâche que vous lui avez confiée. Ne fournissez que les identifiants dont vous êtes prêt à accorder l'accès complet.
- **Effectuez régulièrement une rotation des identifiants** : traitez les identifiants partagés avec l'agent de la même manière que vous le feriez pour n'importe quel identifiant programmatique. Effectuez une rotation régulière.

### Connecter des outils et des API externes

Vous pouvez connecter des outils et des API externes (tels que des serveurs MCP [Model Context Protocol]) pour étendre les capacités de l'agent. Dans ce cas :

- Ne connectez que des outils provenant de sources fiables. Un outil malveillant ou mal écrit peut exposer des données ou effectuer des actions involontaires.
- Configurez les outils avec les autorisations minimales requises pour votre cas d'utilisation. Si un outil est compatible avec le mode lecture seule, préférez-le, sauf si des écritures sont strictement nécessaires.
- Avant de connecter un outil à une source de données de production, testez-le sur des exemples de données ou des données synthétiques pour vérifier que l'agent l'utilise comme prévu.

### Supervision humaine

Les agents peuvent raisonner, planifier et exécuter des workflows en plusieurs étapes avec un degré d'autonomie élevé. Bien que cela soit puissant, vous devez également appliquer une supervision appropriée, en particulier pour les tâches qui modifient des données ou interagissent avec des systèmes externes.

Vérifiez toujours les sorties critiques telles que le code généré, les transformations de données ou les modifications de configuration avant de les déployer.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/08/19 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/08/19 (UTC)."],[],[]]
