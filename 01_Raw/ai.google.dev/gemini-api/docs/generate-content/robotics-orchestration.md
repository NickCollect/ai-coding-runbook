---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=de
fetched_at: 2026-09-07T05:41:43.376208+00:00
title: "Aufgabenorchestrierung \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Aufgabenorchestrierung

Gemini Robotics ER-Modelle können Aufgaben planen und räumliche Zusammenhänge berücksichtigen. Sie leiten ab, welche Aktionen ausgeführt und welche Objekte bewegt werden müssen, um ein Ziel zu erreichen. Auf dieser Seite
wird ein Beispiel für die Ausführung eines [Pick-and-Place](#calling-custom-robot-api)
Vorgangs über eine benutzerdefinierte Roboter-API gezeigt, um die Aufgabe zu orchestrieren, einen Gegenstand
in eine Schüssel zu legen.

Vollständiger ausführbarer Code ist im
[Robotics-Cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) verfügbar.

## Benutzerdefinierte Roboter-API verwenden

In diesem Beispiel wird die Aufgabenorchestrierung mit einer benutzerdefinierten Roboter-API veranschaulicht. Es wird eine Mock-API für einen Pick-and-Place-Vorgang eingeführt. Die Aufgabe besteht darin, einen blauen Block aufzunehmen und in eine orangefarbene Schüssel zu legen:

![Bild des Blocks und der Schale](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=de)

In diesem Beispiel werden die folgenden Mock-Roboter-API- und Tool-Definitionen verwendet:

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

Im folgenden Beispiel werden der Prompt und das Bild mit den Tool-Definitionen an das Modell gesendet. Anschließend wird eine Agenten-Schleife ausgeführt: Nach jeder Modellantwort werden alle angeforderten Funktionsaufrufe (`move`, `setGripperState`) ausgeführt, die Ergebnisse an das Modell zurückgegeben und der Vorgang wiederholt, bis das Modell keine Funktionen mehr aufruft oder das Schrittlimit erreicht ist.

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

Im Folgenden sehen Sie eine mögliche Ausgabe des Modells basierend auf dem Prompt und der Mock-Roboter-API. Die Ausgabe enthält die Ausgabe der Roboter-Funktionsaufrufe, die das Modell sequenziell ausgeführt hat.

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

## Nächste Schritte

- [Robotik mit Streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de): Echtzeit-Streaming mit Funktionsaufrufen (nur Gemini Robotics ER 2)
- [Videoanalyse](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de): Aufgabenfortschritt anhand von Videos verfolgen (nur ER 2)
- [Räumliches Denken](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=de): Beispiele für Zeigen, Tracking und Begrenzungsrahmen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-04 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-04 (UTC)."],[],[]]
