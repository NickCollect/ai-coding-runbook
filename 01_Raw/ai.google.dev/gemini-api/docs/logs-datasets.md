---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr
fetched_at: 2026-10-12T06:59:49.840108+00:00
title: "Journaux et ensembles de donn\u00e9es \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Journaux et ensembles de données

Ce guide vous explique comment afficher les journaux d'utilisation de l'API Gemini dans le tableau de bord Google AI Studio pour mieux comprendre le comportement des modèles et la façon dont les utilisateurs interagissent avec vos applications. Utilisez la journalisation pour observer, déboguer et *partager éventuellement des commentaires sur l'utilisation avec Google afin d'améliorer Gemini pour les cas d'utilisation des développeurs*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=fr)

Tous les appels d'API `GenerateContent`, `BatchGenerateContent` et `StreamGenerateContent`, ainsi que les appels d'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr) (à l'exception des Managed Agents) sont acceptés. Cela inclut les appels effectués via les points de terminaison [compatibles avec OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

## Configurer la journalisation du projet

Par défaut, l'API stocke tous les objets d'interaction (`store=true`) afin de simplifier l'utilisation des fonctionnalités de gestion de l'état côté serveur. En revanche, l'API Generate Content ne stocke pas les requêtes par défaut. Le stockage doit être activé pour chaque requête ou au niveau du projet dans AI Studio.

Dans Google [AI Studio](https://aistudio.google.com/logs?hl=fr), vous pouvez activer ou désactiver la journalisation pour tous les projets ou pour des projets spécifiques. Vous pouvez modifier ces préférences à tout moment dans le panneau **Paramètres** de la page [Journaux et ensembles de données](https://aistudio.google.com/logs?hl=fr). Vous pouvez activer ou désactiver la journalisation indépendamment pour l'API `generateContent` et l'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr) afin de modifier le comportement de stockage par défaut d'un projet.

### Journalisation au niveau de la requête

Le comportement de stockage et de journalisation diffère selon l'API :

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr)** : stocke les requêtes par défaut (`store=true`) pour simplifier la gestion de l'état côté serveur.
- **Generate Content API (`generateContent`)** : ne stocke pas les requêtes par défaut (`store=false`).

Voici comment définir la propriété `store` :

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

// The GenerateContent API does not store requests by default
GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder().build());

System.out.println(response.text());
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // The GenerateContent API does not store requests by default
    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{},
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**API Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

## Afficher les journaux du projet dans AI Studio

1. Accédez à la page "Journaux" dans [AI Studio](https://aistudio.google.com/logs?hl=fr).
2. Sélectionnez un projet dans le menu déroulant.
3. Si des journaux existent pour l'API Interactions, ils s'affichent dans le tableau dans l'ordre chronologique inverse.
4. Pour observer les journaux du projet pour l'API Generate Content, commencez par l'activer dans le [panneau des paramètres](#configure-logging).

Cliquez sur une entrée pour obtenir un aperçu de la charge utile. Vous pouvez inspecter l'intégralité du prompt et de la réponse de Gemini, ainsi que le contexte des tours précédents. Pour les requêtes de l'**API Interactions**, les journaux incluent également un lien direct vers le `previous_interaction_id`.

## Configurer la durée de conservation du stockage d'un projet

Les journaux expirent et sont marqués pour suppression après une période de conservation par défaut de 55 jours (sauf s'ils sont [enregistrés dans un ensemble de données](#create), auquel cas ils n'expirent pas).
Vous pouvez configurer la période de conservation des journaux d'un projet sur 7, 14, 28 ou 55 jours maximum.

## Créer et partager des ensembles de données

Vous pouvez enregistrer les journaux dans des ensembles de données pour les organiser et les exporter plus efficacement.

- Sur la [page "Journaux"](https://aistudio.google.com/logs?hl=fr), localisez la barre de filtres en haut de la page et sélectionnez une propriété à filtrer.
- Dans votre vue filtrée, utilisez les cases à cocher pour sélectionner tous les journaux ou certains d'entre eux.
- Cliquez sur le bouton **Créer un ensemble de données** qui s'affiche en haut de la liste.
- Attribuez un nom et éventuellement une description à votre nouvel ensemble de données.
- L'ensemble de données que vous venez de créer s'affiche avec l'ensemble de journaux sélectionnés.
- Exportez votre ensemble de données pour une analyse plus approfondie au format CSV ou JSONL, ou vers Google Sheets.

Les ensembles de données peuvent être utiles pour différents cas d'utilisation.

- **Créez des ensembles de défis** : favorisez les futures améliorations dans les domaines où vous souhaitez que votre IA progresse.
- **Organisez des ensembles d'échantillons** : par exemple, un échantillon d'utilisation réelle pour générer des réponses à partir d'un autre modèle, ou une collection de cas extrêmes pour les vérifications de routine avant le déploiement.
- **Ensembles d'évaluation** : ensembles représentatifs de l'utilisation réelle des fonctionnalités importantes, pour la comparaison avec d'autres modèles ou itérations d'instructions système.

Vous pouvez contribuer à la recherche et au développement de Gemini en choisissant de partager vos ensembles de données avec Google à titre d'exemples.

## Limites

La journalisation n'est actuellement pas disponible pour les éléments suivants :

- Modèles Imagen et Veo
- Modèles d'embedding Gemini
- Modèle Gemini Robotics
- Entrées contenant des vidéos, des GIF ou des PDF
- Agents en version Preview publique dans l'API Gemini

## Étape suivante

- **Prototyper avec l'historique des sessions** : utilisez [AI Studio Build](https://aistudio.google.com/apps?hl=fr) pour coder des applications et ajoutez votre clé API afin d'activer un historique des journaux de l'API Gemini pour les fonctionnalités d'IA.
- **Réexécuter les journaux avec l'API Gemini Batch** : utilisez des ensembles de données pour l'échantillonnage des réponses et l'évaluation des modèles ou de la logique d'application en réexécutant les journaux avec l'[API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
