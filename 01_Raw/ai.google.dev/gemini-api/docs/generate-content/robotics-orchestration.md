---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=fr
fetched_at: 2026-10-12T07:03:19.489205+00:00
title: "Orchestration des t\u00e2ches \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Orchestration des tâches

Les modèles Gemini Robotics ER peuvent planifier des tâches et raisonner sur l'espace, en déduisant les actions à entreprendre et les objets à déplacer pour atteindre un objectif. Cette page
présente un exemple de pilotage d'une opération de [prise et de dépose](#calling-custom-robot-api)
via une API de robot personnalisée pour orchestrer la tâche consistant à placer un élément
dans un bol.

Pour obtenir le code exécutable complet, consultez le
[livre de recettes sur la robotique](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Utiliser une API de robot personnalisée

Cet exemple illustre l'orchestration des tâches avec une API de robot personnalisée. Il présente une API fictive conçue pour une opération de prise et de dépose. La tâche consiste à prendre un bloc bleu et à le placer dans un bol orange :

![Image du bloc et du bol](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=fr)

Cet exemple utilise les définitions d'API et d'outil de robot fictifs suivantes :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

def move(x, y, high):
    print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
    print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_declaration = types.FunctionDeclaration(
    name="move",
    description="Moves the arm to the given coordinates.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "x": types.Schema(type=types.Type.INTEGER, description="X coordinate relative to the origin"),
            "y": types.Schema(type=types.Type.INTEGER, description="Y coordinate relative to the origin"),
            "high": types.Schema(type=types.Type.BOOLEAN, description="Set to True to lift the robot arm above the scene. Set to False to place the gripper on the surface."),
        },
        required=["x", "y", "high"],
    ),
)

set_gripper_state_declaration = types.FunctionDeclaration(
    name="setGripperState",
    description="Opens or closes the robot's gripper.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "opened": types.Schema(type=types.Type.BOOLEAN, description="True opens the gripper, False closes the gripper."),
        },
        required=["opened"],
    ),
)

robot_tools = types.Tool(function_declarations=[move_declaration, set_gripper_state_declaration])
```

L'exemple suivant envoie le prompt et l'image au modèle avec les définitions d'outil. Il exécute ensuite une boucle d'agent : après chaque réponse du modèle, il exécute tous les appels de fonction demandés (`move`, `setGripperState`), renvoie les résultats au modèle et répète l'opération jusqu'à ce que le modèle cesse d'appeler des fonctions ou que la limite d'étapes soit atteinte.

### Python

```
with open("robot-api-example.png", "rb") as f:
    img_bytes = f.read()

prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

contents = [
    types.Content(role="user", parts=[
        types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
        types.Part(text=prompt),
    ])
]

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15  # Safety limit to prevent infinite loops
step_count = 0

# The Agentic Loop
while step_count < max_steps:
    step_count += 1

    response = client.models.generate_content(
        model="gemini-robotics-er-2-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[robot_tools],
            thinking_config=types.ThinkingConfig(thinking_level="low"),
        ),
    )

    # Add model response to conversation history
    contents.append(response.candidates[0].content)

    # Check for function calls
    function_calls = [part for part in response.candidates[0].content.parts if part.function_call]

    if not function_calls:
        # Model is done calling functions
        print("Sequence complete.")
        print(f"Model Summary: {response.text}")
        break

    # Execute function calls and collect results
    function_response_parts = []
    for part in function_calls:
        fc = part.function_call
        if fc.name == "move":
            move(**fc.args)
        elif fc.name == "setGripperState":
            setGripperState(**fc.args)

        function_response_parts.append(
            types.Part.from_function_response(
                name=fc.name,
                response={"status": "success"},
            )
        )

    # Send function results back to model
    contents.append(types.Content(role="user", parts=function_response_parts))
```

L'exemple suivant montre une sortie possible du modèle en fonction du prompt et de l'API de robot fictive. La sortie inclut la sortie des appels de fonction de robot que le modèle a séquencés ensemble.

```
--- Executing Orchestrated Plan ---
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: 160, 440, down at table level
Mock Robot: Closing gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: -250, 60, high above table
Mock Robot: Moving to coordinates: -250, 60, down at table level
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: -250, 60, high above table
Sequence complete.
Model Summary: I have completed the task of picking up the blue block and placing it into the orange bowl.
```

## Étape suivante

- [Robotique avec streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr) : streaming en temps réel avec appel de fonction (Gemini Robotics ER 2 uniquement)
- [Compréhension vidéo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fr) : suivi de la progression des tâches à partir de la vidéo (ER 2 uniquement)
- [Raisonnement spatial](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=fr) : exemples de pointage, de suivi et de cadre de délimitation

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/08 (UTC)."],[],[]]
