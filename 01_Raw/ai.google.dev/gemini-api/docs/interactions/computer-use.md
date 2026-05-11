---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=pt-BR
fetched_at: 2026-05-11T05:03:23.673961+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Uso de computador

Com o Uso do computador, você pode criar agentes de controle do navegador que interagem e automatizam tarefas. Usando capturas de tela, o modelo pode "ver" uma tela de computador e "agir" gerando ações específicas da interface, como cliques do mouse e entradas de teclado. Assim como na chamada de função, você precisa escrever o código do aplicativo do lado do cliente para receber e executar as ações de uso do computador.

Com o uso do computador, é possível criar agentes que:

- Automatizar a entrada de dados repetitivos ou o preenchimento de formulários em sites.
- Realizar testes automatizados de aplicativos da Web e fluxos de usuários
- Fazer pesquisas em vários sites (por exemplo, coletar informações, preços e avaliações de produtos em sites de e-commerce para informar uma compra)

A maneira mais fácil de testar a capacidade de uso do computador é usando a [implementação de referência](https://github.com/google/computer-use-preview/) ou o [ambiente de demonstração do Browserbase](http://gemini.browserbase.com).

## Como o uso de computador funciona

Para criar um agente de controle do navegador com o modelo de uso do computador, implemente
um loop de agente que faça o seguinte:

1. [**Enviar uma solicitação para o modelo**](#send-request)

   - Adicione a ferramenta "Uso de computador" e, opcionalmente, qualquer função personalizada definida pelo usuário ou excluída à sua solicitação de API.
   - Envie o comando com a solicitação do usuário para o modelo de uso do computador.
2. [**Receber a resposta do modelo**](#model-response)

   - O modelo de uso do computador analisa a solicitação e a captura de tela do usuário e gera uma resposta que inclui um `function_call` sugerido representando uma ação da interface (por exemplo, "clique na coordenada (x,y)" ou "digite 'texto'"). Para uma descrição de todas as ações da interface compatíveis com o modelo de uso do computador, consulte [Ações compatíveis](#supported-actions).
   - A resposta da API também pode incluir um `safety_decision` de um sistema de segurança interno que verifica a ação proposta pelo modelo. Esse
     `safety_decision` classifica a ação como:
     - **Regular / permitida**:a ação é considerada segura. Isso também pode ser representado pela ausência de `safety_decision`.
     - **Requer confirmação (`require_confirmation`)**: o modelo está prestes a
       realizar uma ação
       que pode ser arriscada (por exemplo, clicar em um banner de cookie).
3. [**Executar a ação recebida**](#execute-actions)

   - Seu código do lado do cliente recebe o `function_call` e qualquer `safety_decision` acompanhante.
     - **Regular / permitido**:se o `safety_decision` indicar regular / permitido (ou se nenhum `safety_decision` estiver presente), seu código do lado do cliente poderá executar o `function_call` especificado no ambiente de destino (por exemplo, um navegador da Web).
     - **Requer confirmação**:se o `safety_decision` indicar
       que requer confirmação, o aplicativo precisa pedir ao usuário final
       que confirme antes de executar o `function_call`. Se o usuário
       confirmar, execute a ação. Se o usuário negar, não
       execute a ação.
4. [**Capturar o novo estado do ambiente**](#capture-state)

   - Se a ação tiver sido executada, o cliente vai capturar uma nova captura de tela
     da GUI e o URL atual para enviar de volta ao modelo de uso do computador como
     parte de um `function_result`.
   - Se uma ação foi bloqueada pelo sistema de segurança ou teve a confirmação negada pelo usuário, seu aplicativo poderá enviar um feedback diferente para o modelo ou encerrar a interação.

Esse processo se repete desde a etapa 2 com o modelo usando a nova captura de tela e a meta em andamento para sugerir a próxima ação. O loop continua até que a tarefa seja concluída, ocorra um erro ou o processo seja encerrado (por exemplo, devido a uma resposta de segurança de "bloqueio" ou uma decisão do usuário).

![Visão geral do uso de computadores](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=pt-br)

## Como implementar o uso do computador

Antes de criar com a ferramenta "Uso do computador", você precisa configurar o seguinte:

- **Ambiente de execução seguro**:por motivos de segurança, execute o agente de uso do computador em um ambiente seguro e controlado (por exemplo, uma máquina virtual em sandbox, um contêiner ou um perfil de navegador dedicado com permissões limitadas).
- **Gerenciador de ações do lado do cliente**:você precisa implementar uma lógica do lado do cliente para executar as ações geradas pelo modelo e capturar capturas de tela do ambiente após cada ação.

Os exemplos nesta seção usam um navegador como ambiente de execução
e o [Playwright](https://playwright.dev/) como o manipulador de ações do lado do cliente. Para
executar essas amostras, instale as dependências necessárias e inicialize uma
instância do navegador Playwright.

#### Instalar o Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### Inicializar a instância do navegador Playwright

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

O exemplo de código para extensão a um ambiente
Android está incluído na seção [Usar funções personalizadas definidas pelo
usuário](#custom-functions).

### 1. Enviar uma solicitação ao modelo

Adicione a ferramenta "Uso do computador" à solicitação de API e envie um comando ao modelo que inclua a meta do usuário. Você precisa usar um dos modelos compatíveis com o uso de computador ou vai receber um erro:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Também é possível adicionar os seguintes parâmetros opcionais:

- **Ações excluídas**:se houver ações da lista de [Ações da interface compatíveis](#supported-actions) que você não quer que o modelo execute, especifique-as como `excluded_predefined_functions`.
- **Funções definidas pelo usuário**:além da ferramenta "Uso do computador", talvez você queira incluir funções personalizadas definidas pelo usuário.

Observe que não é necessário especificar o tamanho de exibição ao fazer uma solicitação; o modelo prevê coordenadas de pixel dimensionadas para a altura e a largura da tela.

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

Para um exemplo com funções personalizadas, consulte [Usar funções personalizadas definidas pelo usuário](#custom-functions).

### 2. Receber a resposta do modelo

Quando a ferramenta "Uso do computador" está ativada, o modelo responde com uma ou mais etapas
`function_call` se determinar que ações da interface são necessárias para concluir a tarefa.
O uso de computadores é compatível com a chamada de função paralela, ou seja, o modelo pode retornar
várias ações em um único turno.

Confira um exemplo de resposta do modelo.

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

### 3. Executar as ações recebidas

O código do aplicativo precisa analisar a resposta do modelo, executar as ações e coletar os resultados.

O exemplo de código a seguir extrai chamadas de função da resposta do modelo de uso de computador
e as traduz em ações que podem ser executadas com o Playwright.
O modelo gera coordenadas normalizadas (0 a 999) independente das dimensões da imagem de entrada. Portanto, parte da etapa de tradução é converter essas coordenadas normalizadas de volta para valores de pixel reais.

O tamanho de tela recomendado para uso com o modelo de uso do computador é (1440, 900). O modelo funciona com qualquer resolução, mas a qualidade dos resultados pode ser afetada.

Este exemplo inclui apenas a implementação das três ações de interface mais comuns: `open_web_browser`, `click_at` e `type_text_at`. Para
casos de uso de produção, é necessário implementar todas as outras ações da interface da lista
[Ações compatíveis](#supported-actions), a menos que você as adicione explicitamente como
`excluded_predefined_functions`.

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

### 4. Capturar o estado do novo ambiente

Depois de executar as ações, envie o resultado da execução da função de volta ao modelo para que ele possa usar essas informações e gerar a próxima ação. Se várias ações (chamadas paralelas) foram executadas, envie um `function_result` para cada uma delas na próxima vez que o usuário falar.

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

## Criar um loop de agente

Para ativar interações de várias etapas, combine as quatro etapas da seção [Como implementar o uso do computador](#implement-computer-use) em um loop.
Não se esqueça de gerenciar o histórico de conversas corretamente anexando as respostas do modelo e da função.

Para executar este exemplo de código, você precisa:

- Instale as [dependências necessárias do Playwright](#implement-computer-use).
- Defina as funções auxiliares das etapas [(3) Executar as ações
  recebidas](#execute-actions) e [(4) Capturar o novo estado do
  ambiente](#capture-state).

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

## Usar funções personalizadas definidas pelo usuário

Você também pode incluir funções personalizadas definidas pelo usuário na solicitação para estender a funcionalidade do modelo. O exemplo a seguir adapta o modelo e a ferramenta de uso do computador para casos de uso em dispositivos móveis, incluindo ações personalizadas definidas pelo usuário, como `open_app`, `long_press_at` e `go_home`, e excluindo ações específicas do navegador. O modelo pode chamar de forma inteligente essas funções personalizadas junto com ações padrão da interface do usuário para concluir tarefas em ambientes que não são navegadores.

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

## Ações da interface compatíveis

O modelo pode solicitar as seguintes ações de interface usando um
`function_call`. O código do lado do cliente precisa implementar a lógica de execução dessas ações. Consulte a [implementação de referência](https://github.com/google/computer-use-preview) para exemplos.

| Nome do comando | Descrição | Argumentos (em "Chamada de função") | Exemplo de chamada de função |
| --- | --- | --- | --- |
| **open\_web\_browser** | Abre o navegador da Web. | Nenhum | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | Pausa a execução por 5 segundos para permitir que o conteúdo dinâmico seja carregado ou que as animações sejam concluídas. | Nenhum | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | Navega para a página anterior no histórico do navegador. | Nenhum | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | Navega para a próxima página no histórico do navegador. | Nenhum | `{"name": "go_forward", "arguments": {}}` |
| **search** | Navega até a página inicial do mecanismo de pesquisa padrão (por exemplo, o Google). Útil para iniciar uma nova tarefa de pesquisa. | Nenhum | `{"name": "search", "arguments": {}}` |
| **navigate** | Navega o navegador diretamente para o URL especificado. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Clica em uma coordenada específica na página da Web. Os valores x e y são baseados em uma grade de 1000 x 1000 e são dimensionados para as dimensões da tela. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | Passa o cursor do mouse em uma coordenada específica na página da Web. Útil para revelar submenus. x e y são baseados em uma grade de 1000 x 1000. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Digita texto em uma coordenada específica. Por padrão, limpa o campo primeiro e pressiona ENTER depois de digitar, mas isso pode ser desativado. x e y são baseados em uma grade de 1000 x 1000. | `y`: int (0 a 999), `x`: int (0 a 999), `text`: str, `press_enter`: bool (opcional, padrão é True), `clear_before_typing`: bool (opcional, padrão é True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Pressione teclas ou combinações de teclas do teclado, como "Control+C" ou "Enter". Útil para acionar ações (como enviar um formulário com "Enter") ou operações da área de transferência. | `keys`: str (por exemplo, "enter", "control+c"). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | Rola toda a página da Web para "cima", "baixo", "esquerda" ou "direita". | `direction`: str ("up", "down", "left" ou "right") | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | Rola um elemento ou área específica na coordenada (x, y) na direção especificada por uma determinada magnitude. As coordenadas e a magnitude (padrão 800) são baseadas em uma grade de 1000 x 1000. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, opcional, padrão 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Arrasta um elemento de uma coordenada inicial (x, y) e o solta em uma coordenada de destino (destination\_x, destination\_y). Todas as coordenadas são baseadas em uma grade de 1000 x 1000. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Segurança e proteção

### Confirmar decisão de segurança

Dependendo da ação, a resposta do modelo também pode incluir um
`safety_decision` de um sistema de segurança interno que verifica a ação
proposta pelo modelo.

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

Se o `safety_decision` for `require_confirmation`, peça ao usuário final para confirmar antes de executar a ação. De acordo com os [Termos de Serviço](https://ai.google.dev/gemini-api/terms?hl=pt-br), não é permitido ignorar solicitações de confirmação humana.

Este exemplo de código pede confirmação ao usuário final antes de executar a
ação. Se o usuário não confirmar a ação, o loop será encerrado. Se o usuário confirmar a ação, ela será executada e o campo `safety_acknowledgement` será marcado como `True`.

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

Se o usuário confirmar, inclua o reconhecimento de segurança no
seu `function_result`.

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

### Práticas recomendadas de segurança

O uso de computadores é uma ferramenta nova que apresenta riscos inéditos que os desenvolvedores precisam conhecer:

- **Conteúdo e golpes não confiáveis**:ao tentar alcançar o objetivo do usuário, o modelo pode usar fontes de informações e instruções não confiáveis na tela. Por exemplo, se o objetivo do usuário for comprar um smartphone Pixel e o modelo encontrar um golpe de "Pixel sem custo financeiro se você responder a uma pesquisa", há alguma chance de que o modelo responda à pesquisa.
- **Ações ocasionais não intencionais**:o modelo pode interpretar mal a meta de um usuário ou o conteúdo da página da Web, fazendo com que ele realize ações incorretas, como clicar no botão errado ou preencher o formulário errado. Isso pode levar a falhas nas tarefas ou exfiltração de dados.
- **Violações da política**:os recursos da API podem ser direcionados, intencionalmente ou não, a atividades que violam as políticas do Google ([Política de uso proibido da IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br) e os [Termos de Serviço adicionais da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br). Isso inclui ações que
  podem interferir na integridade de um sistema, comprometer a segurança, ignorar
  medidas de segurança,
  controlar dispositivos médicos etc.

Para lidar com esses riscos, implemente as seguintes medidas de segurança e práticas recomendadas:

1. **Human-in-the-Loop (HITL)**:

   - **Implemente a confirmação do usuário**:quando a resposta de segurança indicar
     `require_confirmation`, implemente a confirmação do usuário antes da
     execução. Consulte [Confirmar decisão de segurança](#safety-decisions) para
     um exemplo de código.
   - **Fornecer instruções de segurança personalizadas**:além das verificações de confirmação do usuário integradas, os desenvolvedores podem adicionar uma [instrução do sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#system-instructions) personalizada que aplique as próprias políticas de segurança, seja para bloquear determinadas ações do modelo ou exigir a confirmação do usuário antes que o modelo execute determinadas ações irreversíveis de alto risco. Confira um exemplo de instrução personalizada de segurança
     que você pode incluir ao interagir com o modelo.

     #### Exemplo de instruções de segurança

     Defina suas regras de segurança personalizadas como uma instrução do sistema:

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
2. **Ambiente de execução seguro**:execute o agente em um ambiente seguro e de sandbox para limitar o impacto potencial dele. Por exemplo, uma máquina virtual (VM) de sandbox, um contêiner (como o Docker) ou um perfil de navegador dedicado com permissões limitadas.
3. **Sanitização de entrada**:sanitizar todo o texto gerado pelo usuário em comandos para
   reduzir o risco de instruções não intencionais ou injeção de comandos. Essa é uma camada útil de segurança, mas não substitui um ambiente de execução seguro.
4. **Mecanismos de segurança de conteúdo**:use mecanismos de segurança e [APIs de segurança de conteúdo](https://ai.google.dev/gemma/docs/shieldgemma?hl=pt-br) para avaliar entradas do usuário, entradas e saídas de ferramentas, a adequação da resposta de um agente, a injeção de comandos e a detecção de jailbreak.
5. **Listas de permissões e de bloqueio**:implemente mecanismos de filtragem para controlar onde o modelo pode navegar e o que ele pode fazer. Uma lista de bloqueio de sites proibidos é um bom ponto de partida, mas uma lista de permissões mais restritiva é ainda mais segura.
6. **Observabilidade e geração de registros**:mantenha registros detalhados para depuração, auditoria e resposta a incidentes. O cliente precisa registrar comandos,
   capturas de tela, ações sugeridas pelo modelo (function\_call), respostas de segurança e
   todas as ações executadas pelo cliente.
7. **Gerenciamento de ambiente**:garanta que o ambiente da GUI seja consistente.
   Pop-ups, notificações ou mudanças inesperadas no layout podem confundir o modelo. Sempre que possível, comece de um estado limpo e conhecido para cada nova tarefa.

## Versões do modelo

O `gemini-3-flash-preview` tem suporte integrado para uso de computadores. Não é necessário um modelo separado para acessar a ferramenta.

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `gemini-2.5-computer-use-preview-10-2025` |
| saveTipos de dados aceitos | **Entrada**  Imagem, texto  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  128.000  **Limite de token de saída**  64.000 |
| Versões do 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthÚltima atualização | Outubro de 2025 |

## A seguir

- Teste o uso do computador no [ambiente de demonstração do Browserbase](http://gemini.browserbase.com).
- Confira a [implementação de referência](https://github.com/google/computer-use-preview) para exemplos de código.
- Conheça outras ferramentas da API Gemini:
  - [Chamadas de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br)
  - [Embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-07 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-07 UTC."],[],[]]
