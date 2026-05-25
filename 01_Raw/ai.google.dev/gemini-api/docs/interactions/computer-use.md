---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=fr
fetched_at: 2026-05-25T05:28:27.925704+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Utilisation d'un ordinateur

L'utilisation de l'ordinateur vous permet de créer des agents de contrôle du navigateur qui interagissent avec les tâches et les automatisent. À l'aide de captures d'écran, le modèle peut "voir" un écran d'ordinateur et "agir" en générant des actions d'interface utilisateur spécifiques, comme des clics de souris et des saisies au clavier. Comme pour l'appel de fonction, vous devez écrire le code de l'application côté client pour recevoir et exécuter les actions d'utilisation de l'ordinateur.

Avec l'utilisation de l'ordinateur, vous pouvez créer des agents qui :

- Automatisez la saisie de données répétitives ou le remplissage de formulaires sur les sites Web.
- Effectuer des tests automatisés des applications Web et des parcours utilisateur
- Effectuer des recherches sur différents sites Web (par exemple, collecter des informations sur les produits, les prix et les avis sur les sites d'e-commerce pour prendre une décision d'achat)

Le moyen le plus simple de tester la fonctionnalité d'utilisation de l'ordinateur consiste à utiliser l'[implémentation de référence](https://github.com/google/computer-use-preview/) ou l'[environnement de démonstration Browserbase](http://gemini.browserbase.com).

## Fonctionnement de l'utilisation d'un ordinateur

Pour créer un agent de contrôle du navigateur avec le modèle d'utilisation de l'ordinateur, implémentez une boucle d'agent qui effectue les opérations suivantes :

1. [**Envoyer une requête au modèle**](#send-request)

   - Ajoutez l'outil d'utilisation de l'ordinateur et, éventuellement, des fonctions personnalisées ou exclues à votre requête API.
   - Envoyez la requête de l'utilisateur au modèle d'utilisation de l'ordinateur.
2. [**Recevoir la réponse du modèle**](#model-response)

   - Le modèle d'utilisation de l'ordinateur analyse la requête et la capture d'écran de l'utilisateur, et génère une réponse qui inclut une `function_call` suggérée représentant une action d'interface utilisateur (par exemple, "cliquer aux coordonnées (x,y)" ou "saisir 'texte'"). Pour obtenir la description de toutes les actions d'interface utilisateur compatibles avec le modèle Computer Use, consultez [Actions compatibles](#supported-actions).
   - La réponse de l'API peut également inclure un `safety_decision` provenant d'un système de sécurité interne qui vérifie l'action proposée par le modèle. Ce `safety_decision` classe l'action comme suit :
     - **Régulier / Autorisé** : l'action est considérée comme sûre. Cela peut également être représenté par l'absence de `safety_decision`.
     - **Nécessite une confirmation (`require_confirmation`)** : le modèle est sur le point d'effectuer une action potentiellement risquée (par exemple, cliquer sur une bannière de cookies).
3. [**Exécuter l'action reçue**](#execute-actions)

   - Votre code côté client reçoit le `function_call` et tout `safety_decision` associé.
     - **Régulier / Autorisé** : si `safety_decision` indique "régulier/autorisé" (ou si aucun `safety_decision` n'est présent), votre code côté client peut exécuter le `function_call` spécifié dans votre environnement cible (par exemple, un navigateur Web).
     - **Confirmation requise** : si `safety_decision` indique qu'une confirmation est requise, votre application doit demander à l'utilisateur final de confirmer avant d'exécuter `function_call`. Si l'utilisateur confirme, exécutez l'action. Si l'utilisateur refuse, n'exécutez pas l'action.
4. [**Capturer l'état du nouvel environnement**](#capture-state)

   - Si l'action a été exécutée, votre client capture une nouvelle capture d'écran de l'interface utilisateur graphique et l'URL actuelle pour les renvoyer au modèle d'utilisation de l'ordinateur dans le cadre d'un `function_result`.
   - Si une action a été bloquée par le système de sécurité ou si l'utilisateur a refusé de la confirmer, votre application peut envoyer une autre forme de commentaires au modèle ou mettre fin à l'interaction.

Ce processus se répète à partir de l'étape 2, le modèle utilisant la nouvelle capture d'écran et l'objectif en cours pour suggérer la prochaine action. La boucle se poursuit jusqu'à ce que la tâche soit terminée, qu'une erreur se produise ou que le processus soit arrêté (par exemple, en raison d'une réponse de sécurité "bloquer" ou d'une décision de l'utilisateur).

![Présentation de l&#39;utilisation d&#39;un ordinateur](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=fr)

## Implémenter l'utilisation de l'ordinateur

Avant de créer des applications avec l'outil Utilisation de l'ordinateur, vous devez configurer les éléments suivants :

- **Environnement d'exécution sécurisé** : pour des raisons de sécurité, vous devez exécuter votre agent d'utilisation de l'ordinateur dans un environnement sécurisé et contrôlé (par exemple, une machine virtuelle en bac à sable, un conteneur ou un profil de navigateur dédié avec des autorisations limitées).
- **Gestionnaire d'actions côté client** : vous devrez implémenter une logique côté client pour exécuter les actions générées par le modèle et capturer des captures d'écran de l'environnement après chaque action.

Les exemples de cette section utilisent un navigateur comme environnement d'exécution et [Playwright](https://playwright.dev/) comme gestionnaire d'actions côté client. Pour exécuter ces exemples, vous devez installer les dépendances nécessaires et initialiser une instance de navigateur Playwright.

#### Installer Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### Initialiser l'instance de navigateur Playwright

```
    from playwright.sync_api import sync_playwright

    # 1. Configure screen dimensions for the target environment
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900

    # 2. Start the Playwright browser
    # In production, utilize a sandboxed environment.
    playwright = sync_playwright().start()
    # Set headless=False to see the actions performed on your screen
    browser = playwright.chromium.launch(headless=False)

    # 3. Create a context and page with the specified dimensions
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
    )
    page = context.new_page()

    # 4. Navigate to an initial page to start the task
    page.goto("https://www.google.com")

    # The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
    # will be used in the steps below.
```

Un exemple de code pour l'extension à un environnement Android est inclus dans la section [Utiliser des fonctions personnalisées définies par l'utilisateur](#custom-functions).

### 1. Envoyer une requête au modèle

Ajoutez l'outil Computer Use à votre requête API et envoyez une invite au modèle qui inclut l'objectif de l'utilisateur. Vous devez utiliser l'un des modèles d'utilisation de l'ordinateur compatibles, sinon une erreur s'affichera :

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Vous pouvez également ajouter les paramètres facultatifs suivants :

- **Actions exclues** : si certaines actions de la liste des [actions d'interface utilisateur compatibles](#supported-actions) ne doivent pas être effectuées par le modèle, spécifiez-les comme `excluded_predefined_functions`.
- **Fonctions définies par l'utilisateur** : en plus de l'outil Utilisation de l'ordinateur, vous pouvez inclure des fonctions définies par l'utilisateur personnalisées.

Notez qu'il n'est pas nécessaire de spécifier la taille d'affichage lors de l'envoi d'une requête. Le modèle prédit les coordonnées en pixels mises à l'échelle de la hauteur et de la largeur de l'écran.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

Pour obtenir un exemple avec des fonctions personnalisées, consultez [Utiliser des fonctions définies par l'utilisateur personnalisées](#custom-functions).

### 2. Recevoir la réponse du modèle

Lorsque l'outil Utilisation de l'ordinateur est activé, le modèle répond avec une ou plusieurs étapes `function_call` s'il détermine que des actions d'interface utilisateur sont nécessaires pour accomplir la tâche.
L'utilisation de l'ordinateur est compatible avec l'appel de fonction parallèle, ce qui signifie que le modèle peut renvoyer plusieurs actions en un seul tour.

Voici un exemple de réponse du modèle.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3. Exécuter les actions reçues

Le code de votre application doit analyser la réponse du modèle, exécuter les actions et collecter les résultats.

L'exemple de code suivant extrait les appels de fonction de la réponse du modèle "Utilisation de l'ordinateur" et les traduit en actions pouvant être exécutées avec Playwright.
Le modèle génère des coordonnées normalisées (0 à 999), quelles que soient les dimensions de l'image d'entrée. Une partie de l'étape de traduction consiste donc à reconvertir ces coordonnées normalisées en valeurs de pixels réelles.

La taille d'écran recommandée pour une utilisation avec le modèle "Utilisation de l'ordinateur" est (1440, 900). Le modèle fonctionnera avec n'importe quelle résolution, mais la qualité des résultats peut être affectée.

Notez que cet exemple n'inclut que l'implémentation des trois actions d'UI les plus courantes : `open_web_browser`, `click_at` et `type_text_at`. Pour les cas d'utilisation en production, vous devrez implémenter toutes les autres actions d'UI de la liste [Actions acceptées](#supported-actions), sauf si vous les ajoutez explicitement en tant que `excluded_predefined_functions`.

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. Comprendre l'état du nouvel environnement

Après avoir exécuté les actions, renvoyez le résultat de l'exécution de la fonction au modèle afin qu'il puisse utiliser ces informations pour générer l'action suivante. Si plusieurs actions (appels parallèles) ont été exécutées, vous devez envoyer un `function_result` pour chacune d'elles lors du tour de l'utilisateur suivant.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

## Créer une boucle d'agent

Pour activer les interactions en plusieurs étapes, combinez les quatre étapes de la section [Implémenter l'utilisation de l'ordinateur](#implement-computer-use) dans une boucle.
N'oubliez pas de gérer correctement l'historique des conversations en ajoutant les réponses du modèle et vos réponses de fonction.

Pour exécuter cet exemple de code, vous devez :

- Installez les [dépendances Playwright nécessaires](#implement-computer-use).
- Définissez les fonctions d'assistance des étapes [(3) Exécuter les actions reçues](#execute-actions) et [(4) Capturer le nouvel état de l'environnement](#capture-state).

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## Utiliser des fonctions définies par l'utilisateur personnalisées

Vous pouvez éventuellement inclure des fonctions personnalisées définies par l'utilisateur dans votre requête pour étendre les fonctionnalités du modèle. L'exemple suivant adapte le modèle et l'outil d'utilisation de l'ordinateur aux cas d'utilisation mobiles en incluant des actions personnalisées définies par l'utilisateur, telles que `open_app`, `long_press_at` et `go_home`, tout en excluant les actions spécifiques au navigateur. Le modèle peut appeler intelligemment ces fonctions personnalisées en plus des actions d'interface utilisateur standards pour effectuer des tâches dans des environnements autres que le navigateur.

### Python

```
from typing import Optional, Dict, Any

from google import genai

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## Actions d'UI compatibles

Le modèle peut demander les actions d'UI suivantes à l'aide d'un `function_call`. Votre code côté client doit implémenter la logique d'exécution de ces actions. Pour obtenir des exemples, consultez l'[implémentation de référence](https://github.com/google/computer-use-preview).

| Nom de la commande | Description | Arguments (dans l'appel de fonction) | Exemple d'appel de fonction |
| --- | --- | --- | --- |
| **open\_web\_browser** | Ouvre le navigateur Web. | Aucun | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | Met en pause l'exécution pendant cinq secondes pour permettre au contenu dynamique de se charger ou aux animations de se terminer. | Aucun | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | Accède à la page précédente de l'historique du navigateur. | Aucun | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | Accède à la page suivante de l'historique du navigateur. | Aucun | `{"name": "go_forward", "arguments": {}}` |
| **search** | Accède à la page d'accueil du moteur de recherche par défaut (par exemple, Google). Utile pour lancer une nouvelle tâche de recherche. | Aucun | `{"name": "search", "arguments": {}}` |
| **navigate** | Dirige le navigateur directement vers l'URL spécifiée. | `url` : str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Clique sur une coordonnée spécifique de la page Web. Les valeurs x et y sont basées sur une grille de 1 000 x 1 000 et sont mises à l'échelle des dimensions de l'écran. | `y` : int (0-999), `x` : int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | Pointez sur une coordonnée spécifique de la page Web. Utile pour afficher les sous-menus. Les valeurs x et y sont basées sur une grille de 1 000 x 1 000. | `y` : int (0-999) `x` : int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Saisit du texte à une coordonnée spécifique. Par défaut, le champ est d'abord effacé, puis la touche ENTRÉE est enfoncée après la saisie, mais ces actions peuvent être désactivées. x et y sont basés sur une grille de 1 000 x 1 000. | `y` : int (0-999), `x` : int (0-999), `text` : str, `press_enter` : bool (facultatif, valeur par défaut : True), `clear_before_typing` : bool (facultatif, valeur par défaut : True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Appuyez sur des touches ou des combinaisons de touches du clavier, comme "Ctrl+C" ou "Entrée". Utile pour déclencher des actions (comme l'envoi d'un formulaire avec la touche Entrée) ou des opérations du presse-papiers. | `keys` : str (par exemple, "enter", "control+c"). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | Fait défiler l'intégralité de la page Web vers le haut, le bas, la gauche ou la droite. | `direction` : str ("up", "down", "left" ou "right") | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | Fait défiler un élément ou une zone spécifiques aux coordonnées (x, y) dans la direction spécifiée, selon une certaine amplitude. Les coordonnées et la magnitude (800 par défaut) sont basées sur une grille de 1 000 x 1 000. | `y` : int (0-999), `x` : int (0-999), `direction` : str ("up", "down", "left", "right"), `magnitude` : int (0-999, facultatif, valeur par défaut : 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Fait glisser un élément depuis une coordonnée de départ (x, y) et le dépose à une coordonnée de destination (destination\_x, destination\_y). Toutes les coordonnées sont basées sur une grille de 1 000 x 1 000. | `y` : int (0-999), `x` : int (0-999), `destination_y` : int (0-999), `destination_x` : int (0-999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Protection et sécurité

### Confirmer la décision de sécurité

Selon l'action, la réponse du modèle peut également inclure un `safety_decision` provenant d'un système de sécurité interne qui vérifie l'action proposée par le modèle.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

Si `safety_decision` est défini sur `require_confirmation`, vous devez demander à l'utilisateur final de confirmer avant d'exécuter l'action. Conformément aux [Conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr), vous n'êtes pas autorisé à contourner les demandes de confirmation humaine.

Cet exemple de code demande à l'utilisateur final de confirmer l'action avant de l'exécuter. Si l'utilisateur ne confirme pas l'action, la boucle se termine. Si l'utilisateur confirme l'action, celle-ci est exécutée et le champ `safety_acknowledgement` est marqué comme `True`.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

Si l'utilisateur confirme, vous devez inclure la confirmation de sécurité dans votre `function_result`.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### Bonnes pratiques concernant la sécurité

L'utilisation de l'ordinateur est un nouvel outil qui présente de nouveaux risques dont les développeurs doivent être conscients :

- **Contenus non fiables et escroqueries** : pour atteindre l'objectif de l'utilisateur, le modèle peut s'appuyer sur des sources d'informations et des instructions non fiables provenant de l'écran. Par exemple, si l'objectif de l'utilisateur est d'acheter un téléphone Pixel et que le modèle rencontre une arnaque "Pixel sans frais si vous répondez à une enquête", il y a une chance que le modèle réponde à l'enquête.
- **Actions involontaires occasionnelles** : le modèle peut mal interpréter l'objectif d'un utilisateur ou le contenu d'une page Web, ce qui l'amène à effectuer des actions incorrectes, comme cliquer sur le mauvais bouton ou remplir le mauvais formulaire. Cela peut entraîner l'échec des tâches ou l'exfiltration de données.
- **Non-respect des règles** : les fonctionnalités de l'API peuvent être orientées, intentionnellement ou non, vers des activités qui enfreignent les règles de Google ([Règlement sur les utilisations interdites de l'IA générative](https://policies.google.com/terms/generative-ai/use-policy?hl=fr) et les [Conditions d'utilisation supplémentaires de l'API Gemini](https://ai.google.dev/gemini-api/terms?hl=fr)). Cela inclut les actions qui pourraient nuire à l'intégrité d'un système, compromettre la sécurité, contourner les mesures de sécurité, contrôler des dispositifs médicaux, etc.

Pour faire face à ces risques, vous pouvez mettre en œuvre les mesures de sécurité et les bonnes pratiques suivantes :

1. **Human-in-the-loop (HITL)** :

   - **Implémenter la confirmation de l'utilisateur** : lorsque la réponse de sécurité indique `require_confirmation`, vous devez implémenter la confirmation de l'utilisateur avant l'exécution. Pour obtenir un exemple de code, consultez [Confirmer la décision de sécurité](#safety-decisions).
   - **Fournir des consignes de sécurité personnalisées** : en plus des vérifications de confirmation de l'utilisateur intégrées, les développeurs peuvent éventuellement ajouter une [instruction système](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#system-instructions) personnalisée qui applique leurs propres règles de sécurité, soit pour bloquer certaines actions du modèle, soit pour exiger la confirmation de l'utilisateur avant que le modèle n'effectue certaines actions irréversibles à fort enjeu. Voici un exemple d'instruction de système de sécurité personnalisé que vous pouvez inclure lorsque vous interagissez avec le modèle.

     #### Exemples d'instructions de sécurité

     Définissez vos règles de sécurité personnalisées comme instruction système :

     ```
         ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

         This is your first and most important check. If the next required action falls
         into any of the following categories, you MUST stop immediately, and seek the
         user's explicit permission.

         **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
         Perform all preparatory steps (e.g., navigating, filling out forms, typing a
         message). You will ask for confirmation **AFTER** all necessary information is
         entered on the screen, but **BEFORE** you perform the final, irreversible action
         (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
         Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
         terms, solving a CAPTCHA), you must first inform the user about the required
         action and ask for their confirmation to proceed.

         **USER_CONFIRMATION Categories:**

         *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
             agreeing to any of the following on the user's behalf. You must ask the
             user to confirm before performing these actions.
             *   Terms of Service
             *   Privacy Policies
             *   Cookie consent banners
             *   End User License Agreements (EULAs)
             *   Any other legally significant contracts or agreements.
         *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
             following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
             *   Any other anti-robot or human-verification mechanisms, even if you are
                 capable.
         *   **Financial Transactions:**
             *   Completing any purchase.
             *   Managing or moving money (e.g., transfers, payments).
             *   Purchasing regulated goods or participating in gambling.
         *   **Sending Communications:**
             *   Sending emails.
             *   Sending messages on any platform (e.g., social media, chat apps).
             *   Posting content on social media or forums.
         *   **Accessing or Modifying Sensitive Information:**
             *   Health, financial, or government records (e.g., medical history, tax
                 forms, passport status).
             *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
                 account number, credit card number).
         *   **User Data Management:**
             *   Accessing, downloading, or saving files from the web.
             *   Sharing or sending files/data to any third party.
             *   Transferring user data between systems.
         *   **Browser Data Usage:**
             *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
                 or saved passwords.
         *   **Security and Identity:**
             *   Logging into any user account.
             *   Any action that involves misrepresentation or impersonation (e.g.,
                 creating a fan account, posting as someone else).
         *   **Insurmountable Obstacles:** If you are technically unable to interact with
             a user interface element or are stuck in a loop you cannot resolve, ask the
             user to take over.
         ---

         ## **RULE 2: Default Behavior (ACTUATE)**

         If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
         your default behavior is to **Actuate**.

         **Actuation Means:**  You MUST proactively perform all necessary steps to move
         the user's request forward. Continue to actuate until you either complete the
         non-consequential task or encounter a condition defined in Rule 1.

         *   **Example 1:** If asked to send money, you will navigate to the payment
             portal, enter the recipient's details, and enter the amount. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Send" button.
         *   **Example 2:** If asked to post a message, you will navigate to the site,
             open the post composition window, and write the full message. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Post" button.

             After the user has confirmed, remember to get the user's latest screen
             before continuing to perform actions.

         # Final Response Guidelines:
         Write final response to the user in the following cases:
         - User confirmation
         - When the task is complete or you have enough information to respond to the user
     ```
2. **Environnement d'exécution sécurisé** : exécutez votre agent dans un environnement de bac à sable sécurisé pour limiter son impact potentiel (par exemple, une machine virtuelle (VM) en bac à sable, un conteneur (par exemple, Docker) ou un profil de navigateur dédié avec des autorisations limitées).
3. **Assainissement des entrées** : assainissez tout le texte généré par les utilisateurs dans les prompts pour réduire le risque d'instructions non souhaitées ou d'injection de prompts. Il s'agit d'une couche de sécurité utile, mais elle ne remplace pas un environnement d'exécution sécurisé.
4. **Garde-fous de contenu** : utilisez des garde-fous et des [API de sécurité du contenu](https://ai.google.dev/gemma/docs/shieldgemma?hl=fr) pour évaluer la pertinence des entrées utilisateur, des entrées et sorties d'outils, et des réponses d'un agent, ainsi que pour détecter l'injection de code et les tentatives de jailbreak.
5. **Listes d'autorisation et de blocage** : implémentez des mécanismes de filtrage pour contrôler les sites que le modèle peut consulter et les actions qu'il peut effectuer. Une liste de blocage des sites Web interdits est un bon point de départ, mais une liste d'autorisation plus restrictive est encore plus sécurisée.
6. **Observabilité et journalisation** : conservez des journaux détaillés pour le débogage, l'audit et la réponse aux incidents. Votre client doit consigner les requêtes, les captures d'écran, les actions suggérées par le modèle (function\_call), les réponses de sécurité et toutes les actions finalement exécutées par le client.
7. **Gestion de l'environnement** : assurez-vous que l'environnement de l'interface utilisateur graphique est cohérent.
   Les pop-ups, les notifications ou les modifications de mise en page inattendus peuvent dérouter le modèle. Si possible, commencez chaque nouvelle tâche à partir d'un état propre et connu.

## Versions de modèle

Notez que `gemini-3-flash-preview` est compatible avec l'utilisation de l'ordinateur. Vous n'avez pas besoin d'un modèle distinct pour accéder à l'outil.

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `gemini-2.5-computer-use-preview-10-2025` |
| Types de données acceptés pour save | **Entrée**  Image, texte  **Résultat**  Texte |
| token\_autoLimites de jetons[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | **Limite de jetons d'entrée**  128 000  **Limite de jetons de sortie**  64 000 |
| Versions 123 | Pour en savoir plus, consultez les [schémas de version de modèle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr#model-versions).  - Aperçu : `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthDernière mise à jour | Octobre 2025 |

## Étape suivante

- Testez l'utilisation de l'ordinateur dans l'[environnement de démonstration Browserbase](http://gemini.browserbase.com).
- Consultez l'[implémentation de référence](https://github.com/google/computer-use-preview) pour obtenir un exemple de code.
- Découvrez d'autres outils de l'API Gemini :
  - [Appel de fonction](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr)
  - [Ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/13 (UTC)."],[],[]]
