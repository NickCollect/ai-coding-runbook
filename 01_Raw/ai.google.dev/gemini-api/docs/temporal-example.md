---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=fr
fetched_at: 2026-08-03T04:28:12.152199+00:00
title: "Agent d'IA durable avec Gemini et Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Agent d'IA durable avec Gemini et Temporal

Ce tutoriel vous explique comment créer une
[boucle agentive de style ReAct](https://arxiv.org/abs/2210.03629) qui utilise l'
API Gemini pour le raisonnement et [Temporal](https://temporal.io/) pour la durabilité.
Le code source complet de ce tutoriel est disponible sur
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

L'agent peut appeler des outils, par exemple pour rechercher des alertes météo ou géolocaliser une adresse IP, et il effectue une boucle jusqu'à ce qu'il dispose de suffisamment d'informations pour répondre.

La différence avec une démonstration d'agent classique réside dans la **durabilité**. Chaque appel de LLM, chaque appel d'outil et chaque étape de la boucle agentive sont conservés par Temporal. En cas de plantage du processus, de perte de réseau ou d'expiration d'une API, Temporal effectue automatiquement une nouvelle tentative et reprend à partir de la dernière étape terminée. L'historique des conversations n'est pas perdu et aucun appel d'outil n'est répété par erreur.

## Architecture

L'architecture se compose de trois parties :

- **Workflow** : boucle agentive qui orchestre la logique d'exécution.
- **Activités** : unités de travail individuelles (appels de LLM, appels d'outils) que Temporal rend durables.
- **Nœud de calcul** : processus qui exécute les workflows et les activités.

Dans cet exemple, vous allez placer ces trois éléments dans un seul fichier (`durable_agent_worker.py`). Dans une implémentation réelle, vous les séparerez pour bénéficier de divers avantages en termes de déploiement et d'évolutivité. Vous placerez le code qui fournit un prompt à l'agent dans un deuxième fichier (`start_workflow.py`).

## Prérequis

Pour suivre ce guide, vous aurez besoin des éléments suivants :

- Une clé API Gemini. Vous pouvez en créer une sans frais dans
  [Google AI Studio](https://aistudio.google.com/apikey?hl=fr).
- [Python](https://www.python.org/downloads/) version 3.10 ou ultérieure.
- La [CLI Temporal](https://docs.temporal.io/cli) pour exécuter un serveur de développement
  local.

## Configuration

Avant de commencer, assurez-vous qu'un
[serveur de développement Temporal](https://docs.temporal.io/cli#start-dev-server)
est en cours d'exécution localement :

```
temporal server start-dev
```

Ensuite, installez les dépendances requises :

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Créez un fichier `.env` dans le répertoire de votre projet avec votre clé API Gemini. Vous
pouvez obtenir une clé API depuis
[Google AI Studio](https://aistudio.google.com/apikey?hl=fr).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implémentation

Le reste de ce tutoriel décrit le fichier `durable_agent_worker.py` de haut en bas, en créant l'agent pièce par pièce. Créez le fichier et suivez les instructions.

### Importations et configuration du bac à sable

Commencez par les importations qui doivent être définies à l'avance. Le bloc `workflow.unsafe.imports_passed_through()` indique au bac à sable de workflow de Temporal de laisser passer certains modules sans restriction. Cela est nécessaire, car plusieurs bibliothèques (notamment `httpx`, qui sous-classe `urllib.request.Request`) utilisent des modèles que le bac à sable bloquerait autrement.

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### Instructions système

Définissez ensuite la personnalité de l'agent. Les instructions système indiquent au modèle comment se comporter. Cet agent est invité à répondre en haïkus lorsqu'aucun outil n'est nécessaire.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Définitions d'outils

Définissez maintenant les outils que l'agent peut utiliser. Chaque outil est une fonction asynchrone avec une chaîne de documentation descriptive. Les outils qui acceptent des paramètres utilisent un modèle Pydantic comme argument unique. Il s'agit d'une bonne pratique Temporal qui permet de maintenir la stabilité des signatures d'activité lorsque vous ajoutez des champs facultatifs au fil du temps.

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

Définissez ensuite les outils de géolocalisation d'adresses IP :

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### Registre d'outils

Créez ensuite un registre qui mappe les noms d'outils aux fonctions de gestion. La fonction
`get_tools()` génère des objets `FunctionDeclaration` compatibles avec Gemini
à partir des appelables à l'aide de `FunctionDeclaration.from_callable_with_api_option()`.

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### Activité du LLM

Définissez maintenant l'activité qui appelle l'API Gemini. Les classes de données `GeminiChatRequest` et `GeminiChatResponse` définissent le contrat.

Vous allez désactiver l'appel de fonction automatique afin que l'appel de LLM et l'appel d'outil soient gérés comme des tâches distinctes, ce qui rendra votre agent plus durable. Vous allez également désactiver les nouvelles tentatives intégrées du SDK (`attempts=1`), car Temporal gère les nouvelles tentatives de manière durable.

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### Activité d'outil dynamique

Définissez ensuite l'activité qui exécute les outils. Cette fonctionnalité utilise la fonctionnalité d'activité dynamique de Temporal : le gestionnaire d'outils (un appelable) est obtenu à partir du registre d'outils via la fonction `get_handler`. Cela permet de définir différents agents en fournissant simplement un ensemble d'outils et d'instructions système différents. Le workflow qui implémente la boucle agentive ne nécessite aucune modification.

L'activité inspecte la signature du gestionnaire pour déterminer comment transmettre les arguments. Si le gestionnaire attend un modèle Pydantic, il gère le format de sortie imbriqué généré par Gemini (par exemple, `{"request": {"state": "CA"}}` au lieu d'un format plat `{"state": "CA"}`).

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### Workflow de boucle agentive

Vous disposez maintenant de tous les éléments nécessaires pour terminer la création de l'agent. La classe `AgentWorkflow` implémente un workflow contenant la boucle de l'agent. Dans cette boucle, le LLM est appelé via une activité (ce qui le rend durable), la sortie est inspectée et, si un outil a été choisi par le LLM, il est appelé via `dynamic_tool_activity`.

Dans cet agent simple de style ReAct, une fois que le LLM choisit de ne pas utiliser d'outil, la boucle est considérée comme terminée et le résultat final du LLM est renvoyé.

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3.5-flash",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

La boucle agentive est entièrement durable. Si le nœud de calcul de l'agent plante après plusieurs itérations dans la boucle, Temporal reprendra exactement là où il s'est arrêté sans avoir à appeler de nouveau les appels de LLM ou d'outils déjà exécutés.

### Démarrage du nœud de calcul

Enfin, connectez tous les éléments. Bien que le code implémente la logique métier nécessaire de manière à ce qu'il semble s'exécuter dans un seul processus, l'utilisation de Temporal en fait un système basé sur les événements (plus précisément, basé sur la source d'événements) où la communication entre le workflow et les activités se fait via la messagerie fournie par Temporal.

Le nœud de calcul Temporal se connecte au service Temporal et sert de planificateur pour les tâches de workflow et d'activité. Le nœud de calcul enregistre le workflow et les deux activités, puis commence à écouter les tâches.

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## Script client

Créez le script client (`start_workflow.py`). Il envoie une requête et attend le résultat. Notez qu'il se connecte à la même file d'attente de tâches que celle référencée dans le nœud de calcul de l'agent. Le script `start_workflow` distribue une tâche de workflow avec le prompt utilisateur à cette file d'attente de tâches, ce qui lance l'exécution de l'agent.

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Exécuter l'agent

Si ce n'est pas déjà fait, démarrez le serveur de développement Temporal :

```
temporal server start-dev
```

Dans une nouvelle fenêtre de terminal, démarrez le nœud de calcul de l'agent :

```
python -m durable_agent_worker
```

Dans une troisième fenêtre de terminal, envoyez une requête à votre agent :

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Notez la sortie dans le terminal de `durable_agent_worker` qui affiche les actions qui se produisent à chaque itération de la boucle agentique. Le LLM est en mesure de répondre à la requête de l'utilisateur en appelant une série d'outils à sa disposition. Vous pouvez voir les étapes qui ont été exécutées via l'interface utilisateur Temporal à l'adresse `http://localhost:8233/namespaces/default/workflows`.

Essayez quelques prompts différents pour voir le raisonnement de l'agent et les outils d'appel :

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Le dernier prompt ne nécessite aucun outil. L'agent répond donc en haïku en fonction de `SYSTEM_INSTRUCTIONS`.

## Tester la durabilité (facultatif)

La création sur Temporal garantit que votre agent survit aux échecs de manière transparente. Vous pouvez tester cela à l'aide de deux expériences distinctes.

### Simuler une panne de réseau

Dans ce test, vous allez désactiver temporairement la connexion Internet de votre ordinateur, envoyer un workflow, regarder Temporal réessayer automatiquement, puis restaurer le réseau pour voir s'il récupère.

1. Déconnectez votre machine d'Internet (par exemple, désactivez le Wi-Fi).
2. Envoyez un workflow :

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Consultez l'interface utilisateur Temporal (`http://localhost:8233`). Vous verrez l'activité du LLM échouer et Temporal gérer automatiquement les nouvelles tentatives en arrière-plan.
4. Reconnectez-vous à Internet.
5. La prochaine nouvelle tentative automatisée atteindra l'API Gemini, et votre terminal affichera le résultat final.

### Survivre à un plantage du nœud de calcul

Dans ce test, vous arrêtez le nœud de calcul en cours d'exécution et le redémarrez. Temporal relit l'historique du workflow (source d'événements) et reprend à partir de la dernière activité terminée. Les appels de LLM et d'outils déjà terminés ne sont pas répétés.

1. Pour vous donner le temps d'arrêter le Worker, ouvrez `durable_agent_worker.py` et annulez temporairement la mise en commentaire de `await asyncio.sleep(10)` dans la boucle `run` de `AgentWorkflow`.
2. Redémarrez le nœud de calcul :

   ```
   python -m durable_agent_worker
   ```
3. Envoyez une requête qui déclenche plusieurs outils :

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Arrêtez le processus de nœud de calcul à tout moment avant la fin (`Ctrl-C` dans le terminal du nœud de calcul ou à l'aide de `kill %1` si vous l'exécutez en arrière-plan).
5. Redémarrez le nœud de calcul :

   ```
   python -m durable_agent_worker
   ```

Temporal relit l'historique du workflow. Les appels de LLM et les appels d'outils déjà terminés ne sont **pas** réexécutés. Leurs résultats sont immédiatement relus à partir de l'historique (le journal des événements). Le workflow se termine correctement.

## Autres ressources

- [Documentation Temporal](https://docs.temporal.io/)
- [SDK Python Temporal](https://docs.temporal.io/develop/python)
- [SDK Google GenAI](https://googleapis.github.io/python-genai/)
- [Code source de ce tutoriel](https://github.com/temporal-community/durable-react-agent-gemini)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
