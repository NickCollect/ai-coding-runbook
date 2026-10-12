---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fr
fetched_at: 2026-10-12T06:52:25.247464+00:00
title: "Compr\u00e9hension des vid\u00e9os \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Compréhension des vidéos

Gemini Robotics ER 2 peut suivre la progression des tâches à partir de flux vidéo continus à l'aide de deux fonctionnalités :

- Recherche de moments : identifie l'horodatage précis auquel un événement clé se produit.
- Classification de la progression : attribue chaque vidéo à l'une des cinq catégories de progression (0-20%, 20-40%, 40-60%, 60-80%, 80-100%).

## Recherche de moments

La recherche de moments identifie l'image vidéo exacte où un événement critique se produit, par exemple lorsqu'une tasse est pleine ou qu'un nœud est fait. Les robots l'utilisent pour vérifier la réussite, séquencer les étapes et déclencher des corrections.

L'exemple de prompt suivant demande au modèle d'identifier le moment d'achèvement d'une tâche donnée dans une vidéo :

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

L'exemple suivant montre des images d'une vidéo de recherche de moments, le modèle identifiant l'horodatage d'achèvement de la tâche :

![Exemple d'images vidéo montrant le résultat de la recherche de moments avec un code temporel en superposition](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=fr)

## Classification de la progression

La classification de la progression attribue une vidéo à l'une des cinq catégories de progression : 0-20%, 20-40%, 40-60%, 60-80 % ou 80-100%. Cela permet aux robots d'avoir une conscience de la situation en temps réel afin qu'ils puissent ajuster leurs actions ou réessayer les étapes qui ont échoué sans redémarrer l'ensemble du workflow.

L'exemple de prompt suivant demande au modèle de classer le niveau de progression actuel à partir d'une vidéo :

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

L'exemple suivant montre des images d'une vidéo de classification de la progression, le modèle attribuant une catégorie de progression :

![Exemple de frames vidéo montrant le résultat de la classification de la progression avec un libellé de tranche de progression](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=fr)

## Exemples

Pour obtenir des exemples exécutables complets, y compris le suivi des tâches en plusieurs étapes, consultez le
[livre de recettes sur la robotique](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Étape suivante

- [API Live pour la robotique](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr) : streaming bidirectionnel en temps réel.
- [Orchestration des tâches](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=fr) : tâches à long terme avec raisonnement spatial.
- [Présentation de Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr) : comparaison des modèles et fonctionnalités.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/08 (UTC)."],[],[]]
