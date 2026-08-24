---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=fr
fetched_at: 2026-08-24T02:22:02.504177+00:00
title: "Acc\u00e9l\u00e9rez la d\u00e9couverte avec Gemini pour la recherche \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)

# Accélérez la découverte avec Gemini pour la recherche

[Obtenir une clé API Gemini](https://aistudio.google.com/apikey?hl=fr)

Les modèles Gemini peuvent être utilisés pour faire progresser la recherche fondamentale dans différentes disciplines.
Voici quelques façons d'explorer Gemini pour vos recherches :

- **Analyser et contrôler les sorties du modèle** : pour une analyse plus approfondie, vous pouvez examiner un candidat de réponse généré par le modèle à l'aide d'outils tels que `CitationMetadata`. Vous pouvez également configurer des options pour la génération et les sorties de modèles, telles que `responseSchema`, `topP` et `topK`. [En savoir plus](https://ai.google.dev/api/generate-content?hl=fr)
- **Entrées multimodales** : Gemini peut traiter des images, de l'audio et des vidéos, ce qui ouvre la voie à une multitude de pistes de recherche passionnantes. [En savoir plus](https://ai.google.dev/gemini-api/docs/vision?hl=fr)
- **Capacités de contexte long** : Gemini 3.0 Flash et Pro sont fournis avec une fenêtre de contexte d'un million de jetons. [En savoir plus](https://ai.google.dev/gemini-api/docs/long-context?hl=fr)
- **Grow with Google** : accédez rapidement aux modèles Gemini via l'API et Google AI Studio pour les cas d'utilisation en production. Si vous recherchez une plate-forme basée sur Google Cloud, Gemini Enterprise Agent Platform peut fournir une infrastructure d'assistance supplémentaire.

Pour soutenir la recherche universitaire et faire progresser la recherche de pointe, Google fournit aux scientifiques et aux chercheurs universitaires des crédits pour l'API Gemini via le [programme Gemini Academic](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=fr#gemini-academic-program).

## Premiers pas avec Gemini

L'API Gemini et Google AI Studio vous aident à commencer à travailler avec les derniers modèles de Google et à transformer vos idées en applications évolutives.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Universitaires en vedette

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=fr)

"Nos recherches portent sur Gemini en tant que modèle de langage visuel (VLM) et sur ses comportements agentiques dans divers environnements, du point de vue de la robustesse et de la sécurité. Jusqu'à présent, nous avons évalué la robustesse de Gemini face aux distractions telles que les fenêtres pop-up lorsque les agents VLM effectuent des tâches informatiques, et nous avons utilisé Gemini pour analyser les interactions sociales, les événements temporels ainsi que les facteurs de risque en fonction des entrées vidéo."

[Site Web de Diyi Yang](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=fr)

"Gemini Pro et Flash, avec leur longue fenêtre de contexte, nous ont aidés dans OK-Robot, notre projet de manipulation mobile à vocabulaire ouvert. Gemini permet d'effectuer des requêtes et des commandes complexes en langage naturel sur la "mémoire" du robot, c'est-à-dire les observations précédentes effectuées par le robot pendant une longue durée de fonctionnement. Mahi Shafiullah et moi-même utilisons également Gemini pour décomposer les tâches en code que le robot peut exécuter dans le monde réel."

[Site Web de Lerrel Pinto](https://www.lerrelpinto.com/)

## Programme Gemini Academic

Les chercheurs universitaires qualifiés (tels que les enseignants, le personnel et les doctorants) dans les [pays acceptés](https://ai.google.dev/gemini-api/docs/available-regions?hl=fr) peuvent demander à recevoir des crédits pour l'API Gemini et des limites de débit plus élevées pour leurs projets de recherche. Cette prise en charge permet un débit plus élevé pour les expériences scientifiques et fait progresser la recherche.

Nous nous intéressons particulièrement aux domaines de recherche de la section suivante, mais nous acceptons les candidatures de diverses disciplines scientifiques :

- **Évaluations et benchmarks** : méthodes d'évaluation approuvées par la communauté qui peuvent fournir un signal de performance fort dans des domaines tels que la factualité, la sécurité, le respect des instructions, le raisonnement et la planification.
- **Accélérer les découvertes scientifiques au profit de l'humanité** : applications potentielles de l'IA dans la recherche scientifique interdisciplinaire, y compris dans des domaines tels que les maladies rares et négligées, la biologie expérimentale, la science des matériaux et le développement durable.
- **Incarnation et interactions** : utilisation de grands modèles de langage pour étudier de nouvelles interactions dans les domaines de l'IA incarnée, des interactions ambiantes, de la robotique et de l'interaction homme-machine.
- **Capacités émergentes** : exploration de nouvelles capacités agentiques nécessaires pour améliorer le raisonnement et la planification, et de la façon dont les capacités peuvent être étendues pendant l'inférence (par exemple, en utilisant Gemini Flash).
- **Interaction et compréhension multimodales** : identifier les lacunes et les opportunités pour les modèles de fondation multimodaux pour l'analyse, le raisonnement et la planification dans diverses tâches.

Éligibilité : seuls les particuliers (membres du corps enseignant, chercheurs ou équivalents) affiliés à un établissement d'enseignement ou à un organisme de recherche universitaire valides peuvent postuler. Notez que l'accès à l'API et les crédits seront accordés et supprimés à la discrétion de Google. Nous examinons les demandes tous les mois.

### Commencer à faire des recherches avec l'API Gemini

[S'inscrire](https://forms.gle/HMviQstU8PxC5iCt5)

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/01 (UTC).

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/01 (UTC)."],[],[]]
