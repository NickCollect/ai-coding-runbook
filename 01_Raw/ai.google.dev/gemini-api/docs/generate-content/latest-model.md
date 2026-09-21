---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=fr
fetched_at: 2026-09-21T05:54:01.350139+00:00
title: "Utiliser les derniers mod\u00e8les Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Utiliser les derniers modèles Gemini

[Cette page](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=fr)

Gemini 3.6 Flash (`gemini-3.6-flash`) et Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) sont disponibles pour tous les utilisateurs et prêts à être utilisés en production.

- **Gemini 3.6 Flash** : performances améliorées pour les tâches agentiques et multimodales complexes, tout en réduisant l'utilisation de jetons, à un prix inférieur à celui de 3.5 Flash.
- **Gemini 3.5 Flash-Lite** : le modèle le plus rapide et le moins coûteux de la famille 3.5. Surpasse les générations Flash-Lite précédentes pour l'exécution à haut débit.

Ce guide explique les nouveautés de chaque modèle, les modifications d'API qui affectent votre code et comment effectuer la migration.

### Gemini 3.6 Flash

1. Installez la compétence :

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Appliquez la compétence :

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Installez la compétence :

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Appliquez la compétence :

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Nouveaux modèles

| Modèle | ID du modèle | Niveau de réflexion par défaut | Tarifs | Description |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1,50 $/1 million de jetons d'entrée et 7,50 $/1 million de jetons de sortie | Équilibre la vitesse et l'intelligence pour les tâches agentiques et multimodales. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0,30 $/1 million de jetons d'entrée et 2,50 $/1 million de jetons de sortie | Le modèle 3.5 le plus rapide et le moins coûteux pour l'exécution à haut débit. |

Les deux modèles sont compatibles avec la fenêtre de contexte de 1 million de jetons, 64 000 jetons de sortie maximum, la réflexion et la suite complète d'outils intégrés, y compris [l'utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr).

Pour obtenir les spécifications complètes, consultez les pages des modèles :

- [Page du modèle Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr)
- [Page du modèle Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr)

Pour en savoir plus sur les tarifs, consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Guide de démarrage rapide

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Nouveautés de Gemini 3.6 Flash

- **Réduction des jetons et des tours** : exécute des workflows en plusieurs étapes avec moins d'étapes de raisonnement, de tours de conversation et d'appels d'outils que Gemini 3.5. Il réduit également la spirale de la boucle d'exécution.
- **Génération de code améliorée** : produit un code de qualité supérieure prêt pour la production avec moins de modifications indésirables et moins de boucles de débogage.
- **Meilleure application des instructions** : réduit les modifications de fichiers indésirables lors des tâches de diagnostic.
- **Raisonnement multimodal et spatial puissant** : amélioration des performances en matière d'interprétation de graphiques, de conversion de plans visuels et de génération de mises en page Web multi-éléments.
- **Inspection programmatique anticipée** : préfère exécuter des scripts de code de diagnostic avant d'apporter des modifications plus fréquemment que Gemini 3.5 Flash. Cela améliore la précision des tâches complexes, mais peut ajouter des étapes exploratoires supplémentaires pour les tâches frontend simples.
- **Compatibilité avec l'utilisation de l'ordinateur** : compatible en tant qu'outil natif pour l'automatisation de l'interface utilisateur agentique.
- **Préférence de style d'interface utilisateur** : meilleure création de code fonctionnel, bien que les évaluateurs humains aient préféré les modèles précédents pour la présentation visuelle et le style. Vous pouvez atténuer ce problème en fournissant des consignes de conception explicites.
- **Effort de réflexion par défaut (moyen)** : utilise le même niveau de réflexion par défaut `medium` que Gemini 3.5 Flash.
- **Prix réduit** : coûts des jetons de sortie inférieurs (7,50 $/1 million contre 9,00 $/1 million pour 3.5 Flash). Les jetons d'entrée restent à 1,50 $/1 million.

## Nouveautés de Gemini 3.5 Flash-Lite

- **Latence d'exécution des tâches réduite** : débit le plus élevé de la famille 3.5 pour l'analyse de données à fort volume et l'extraction de documents.
- **Performances de raisonnement et multimodales améliorées** : chemin de migration solide depuis Gemini 2.5 Flash, avec des scores plus élevés pour les tâches de raisonnement telles que HLE (18,0% contre 11,0%) et les benchmarks multimodaux tels que CharXIV (74,5% contre 63,7%).
- **Orchestration des sous-agents et fiabilité des outils** : améliore la fiabilité de l'exécution des outils pour l'exécution de code, la recherche et les workflows MCP. Augmentez le niveau de réflexion pour la planification autonome et les tâches complexes des sous-agents.
- **Compréhension améliorée des documents** : améliore la justesse de l'analyse des documents et de l'extraction des données structurées. Testez les niveaux de réflexion minimal et élevé en fonction de la complexité du document.
- **Codage Web interactif et traitement des données tabulaires** : excellentes performances pour le JavaScript frontend et le traitement des données tabulaires en planifiant via une exécution de code légère.
- **Chatbot et persistance du persona** : meilleure application des instructions multitours et cohérence du persona par rapport à Gemini 3.1 Flash-Lite.
- **Compatibilité avec l'utilisation de l'ordinateur** : compatible en tant qu'outil natif pour l'automatisation de l'interface utilisateur agentique.

## Choisir le bon modèle Flash ou Flash-Lite

Utilisez ce tableau pour sélectionner le bon modèle et le bon chemin de migration pour vos charges de travail.

Les deux modèles nécessitent la suppression des paramètres d'échantillonnage obsolètes (`temperature`, `top_p`, `top_k`) et des tours de modèle préremplis. Pour en savoir plus, consultez la section [Modifications de l'API](#api-changes-and-parameter-updates).

| Modèle | Cas d'utilisation principaux | Cible de migration recommandée |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Génération de code, raisonnement spatial/multimodal, workflows agentiques en plusieurs étapes | **Gemini 3.5 Flash**, **Gemini 3 Flash (preview)** ou **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | Exécution autonome des sous-agents, analyse de données à fort volume et extraction de documents, analyse JSON structurée | **Gemini 3.1 Flash-Lite** ou **Gemini 2.5 Flash** |

## Agent Antigravity mis à jour

Grâce à ses performances améliorées, Gemini 3.6 Flash est désormais le nouveau modèle par défaut qui alimente l'agent [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=fr) dans Gemini Managed Agents. Vous pouvez modifier ce paramètre en définissant un nouveau champ dans l'API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Modifications de l'API et mises à jour des paramètres

À partir de Gemini 3.6 Flash et Gemini 3.5 Flash-Lite, les modifications d'API suivantes s'appliquent à ces modèles et à toutes les futures versions de modèles Gemini.

- **Abandon du paramètre d'échantillonnage** : `temperature`, `top_p` et `top_k` sont obsolètes. L'API ignore ces paramètres et renvoie une erreur dans les futures générations de modèles.
- **Validation du tour de modèle prérempli** : le préremplissage des tours de modèle n'est plus compatible. Si le dernier tour non vide de la requête est un tour `model`, l'API renvoie une erreur `400`.

Vous trouverez ci-dessous des explications détaillées et des exemples de code pour chaque modification de l'API.

### 1. Abandon du paramètre d'échantillonnage (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` et `top_k` sont obsolètes et ignorés. Dans les futures générations de modèles, la fourniture de ces paramètres renvoie une erreur HTTP 400. **Supprimez ces paramètres de toutes les requêtes.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Pour améliorer le déterminisme, définissez une instruction système avec des règles explicites pour votre cas d'utilisation spécifique.

### 2. Validation du tour de modèle prérempli

Les requêtes API se terminant par un tour de rôle de modèle non vide ne sont pas autorisées et renvoient une **erreur HTTP 400**.

#### ⚠️ À éviter

Dans les charges utiles REST brutes ou `generateContent` héritées, il n'est plus autorisé de terminer par un tour de rôle de modèle :

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Migration recommandée

Si votre application préremplissait auparavant un tour de modèle pour supprimer les préambules ou forcer la mise en forme JSON, utilisez plutôt `system_instruction` ou [des sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr).

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## Checklist de migration

### Gemini 3.6 Flash

1. Installez la compétence :

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Appliquez la compétence :

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Installez la compétence :

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Appliquez la compétence :

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Migrer vers gemini-3.6-flash

- **Mettre à jour l'ID du modèle** : remplacez la chaîne de votre modèle cible par `gemini-3.6-flash`.
- **Supprimer les paramètres d'échantillonnage obsolètes**
  - Supprimez `temperature`, `top_p` et `top_k` des configurations de génération.
  - Remplacez `thinking_budget` par l'énumération de chaîne `thinking_level` définie sur `"medium"` ou `"high"`.
  - Supprimez `candidate_count` (non compatible avec Gemini 3.x).
- **Appliquer les règles de validation des tours**
  - Supprimez les tours de modèle préremplis.
  - Assurez-vous que le tour final de l'utilisateur contient du texte non vide.
- **Auditer l'appel de fonction**
  - Assurez-vous que tous les objets `FunctionResponse` incluent `call_id` et `name`.
  - Placez les éléments multimodaux dans la charge utile de la réponse.
  - Mettez en forme les instructions intégrées à l'aide de `\\n\\n`.
  - Si vous voyez des erreurs `Malformed_Function_Call` liées au texte pré-outil, consultez [Solutions de contournement pour les exigences concernant le texte pré-outil](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=fr#workarounds-for-pre-tool-text-requirements).
- **Exigences de base pour Gemini 3.x** : pour les mises à jour du SDK et la préservation de la signature de pensée, consultez la [checklist de migration de Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=fr#migration).

### Migrer vers gemini-3.5-flash-lite

- **Mettre à jour l'ID du modèle** : remplacez la chaîne de votre modèle cible par `gemini-3.5-flash-lite`.
- **Configurer le niveau d'effort de réflexion**
  - Pour l'extraction, le routage ou la classification à fort volume, laissez `thinking_level` sur `"minimal"` (par défaut) pour un débit maximal.
  - Pour les sous-agents autonomes avec des appels d'outils, l'exécution de code ou le raisonnement en plusieurs étapes, définissez `thinking_level` sur `"medium"` ou `"high"` pour éviter l'arrêt prématuré de l'outil.
- **Supprimer les paramètres obsolètes et valider l'appel de fonction** : appliquez les [mêmes règles que pour 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **Exigences de base pour Gemini 3.x** : consultez la [checklist de migration de Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=fr#migration).

## Étapes suivantes

- Consultez les spécifications de l'API dans la [présentation des modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).
- Découvrez l'orchestration multi-agent dans le [guide de l'API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr).
- Testez et affinez les prompts dans [Google AI Studio](https://aistudio.google.com/?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/12 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/12 (UTC)."],[],[]]
