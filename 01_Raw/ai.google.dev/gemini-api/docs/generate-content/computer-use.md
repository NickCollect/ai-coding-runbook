---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=pt-BR
fetched_at: 2026-10-19T05:40:37.935717+00:00
title: "Uso do computador \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Uso do computador

Com a ferramenta Uso do computador, você cria agentes de controle para navegadores, dispositivos móveis e computadores desktop
que interagem e automatizam tarefas. Usando capturas de tela, o modelo pode "ver" uma
tela de computador e "agir" gerando ações específicas de interface, como cliques do mouse
e entradas de teclado. Assim como na chamada de função, você precisa implementar o ambiente de execução do lado do cliente para receber e executar as ações de uso do computador.

Para ver a lista de modelos compatíveis, consulte [Versões de modelo](#model-versions). Os modelos Gemini 3.x são compatíveis com vários recursos avançados:

- **Suporte a vários ambientes**:crie agentes para ambientes de [navegador, dispositivos móveis e computadores](#supported-environments).
- **Ações simplificadas com intents**:as ações incluem um campo `intent` que explica o raciocínio do modelo por trás de cada etapa.
- **Políticas de segurança configuráveis**:ajuste o [comportamento de segurança](#safety-policies) com categorias de políticas integradas e substituições.
- **Detecção de injeção de comandos**:ative a [verificação de capturas de tela](#prompt-injection) para detectar instruções adversárias ocultas.

Com o Computer Use, é possível criar agentes que:

- Automatizar a inserção de dados repetitivos ou o preenchimento de formulários em sites.
- Realizar testes automatizados de aplicativos da Web e fluxos do usuário
- Fazer pesquisas em vários sites (por exemplo, coletar informações de produtos, preços e avaliações de sites de e-commerce para informar uma compra)

Confira um exemplo mínimo de como ativar a ferramenta "Uso do computador":

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Search for 'Gemini API' on Google.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
            )
        )]
    )
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
  contents: "Search for 'Gemini API' on Google.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
      }
    }]
  }
});

console.log(response.text);
```

## Como o Uso de Computador funciona

Para criar um agente com o modelo de uso do computador, é necessário configurar um
loop contínuo entre o aplicativo e a API. Confira o que seu código
vai fazer em cada etapa:

1. [**Enviar uma solicitação ao modelo**](#send-request)
   - O aplicativo envia uma solicitação de API que contém a ferramenta Uso do computador,
     as configurações de configuração (como o ambiente de destino), o comando do
     usuário e uma captura de tela da tela atual.
2. [**Receber a resposta do modelo**](#model-response)
   - O modelo analisa a tela e o comando, retornando uma resposta que inclui um `function_call` sugerido representando uma ação da interface (como um clique, rolagem ou pressionamento de tecla).
   - Para os **modelos do Gemini 3.x**, a resposta também inclui uma justificativa `intent`
     explicando por que o modelo escolheu essa ação.
   - A resposta também pode incluir um `safety_decision` de um sistema de segurança interno que classifica a ação como regular/permitida, `require_confirmation` (exige aprovação do usuário) ou bloqueada.
3. [**Executar a ação recebida**](#execute-actions)
   - Se a ação for permitida (ou o usuário confirmar), o código do lado do cliente
     analisará o `function_call`, dimensionará as coordenadas normalizadas para corresponder
     à sua janela de visualização e executará a ação no ambiente de destino usando
     ferramentas de automação (como o Playwright). Se a ação for bloqueada, o
     cliente precisará interromper a execução ou lidar com a interrupção.
4. [**Capturar o novo estado do ambiente**](#capture-state)
   - Depois que a ação é executada, o aplicativo captura uma nova
     captura de tela e a envia de volta ao modelo em um `function_result` para
     solicitar a próxima etapa.

Esse processo se repete desde a etapa 2, solicitando continuamente a próxima ação
do modelo até que a tarefa seja concluída ou encerrada.

![Visão geral do Uso de Computador](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=pt-br)

## Como implementar o uso do computador

Antes de criar com a ferramenta de uso do computador, você precisa configurar:

- **Ambiente de execução seguro**:execute o agente em uma VM ou um contêiner em sandbox para isolá-lo do sistema host e limitar o impacto potencial.
  A [implementação de referência](https://github.com/google/computer-use-preview/)
  inclui um sandbox pronto para uso baseado no Docker que você pode usar como ponto de partida.
- **Gerenciador de ações do lado do cliente**:implemente a lógica do lado do cliente para executar coordenadas, digitar texto e fazer capturas de tela.

Os exemplos abaixo usam um navegador da Web como ambiente de execução e o
[Playwright](https://playwright.dev/) como gerenciador do lado do cliente.

### 0. Configurar o Playwright

Primeiro, instale os pacotes necessários:

```
pip install google-genai playwright
playwright install chromium
```

Em seguida, inicialize uma instância do navegador Playwright para usar na execução:

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

### 1. Enviar uma solicitação ao modelo

Inicialize a biblioteca de cliente e configure a ferramenta de uso do computador. Não é necessário especificar o tamanho da tela ao emitir uma solicitação. O modelo prevê coordenadas de pixel dimensionadas para a altura e a largura da tela.

### Python

Use o SDK do Python `google-genai` (versão `2.7.0` ou mais recente) para configurar uma solicitação direcionada ao ambiente do navegador:

```
from google import genai
from google.genai.types import (
    Content,
    Part,
    GenerateContentConfig,
    Tool,
    ComputerUse,
    Environment,
    ThinkingConfig,
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        Content(
            role="user",
            parts=[
                Part(text="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            ],
        )
    ],
    config=GenerateContentConfig(
        tools=[
            Tool(
                computer_use=ComputerUse(
                    environment=Environment.ENVIRONMENT_BROWSER,
                    enable_prompt_injection_detection=True,
                ),
            ),
        ],
        thinking_config=ThinkingConfig(
            include_thoughts=True
        ),
    )
)

print(response.text)
```

### JavaScript

Use o SDK do Node.js do `@google/genai` para configurar uma solicitação direcionada ao ambiente do navegador:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
  contents: [
    {
      role: 'user',
      parts: [{ text: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th" }]
    }
  ],
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
        enable_prompt_injection_detection: true
      }
    }],
    thinkingConfig: {
      includeThoughts: true
    }
  }
});

console.log(response.text);
```

### REST

Use curl para enviar uma solicitação:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": {
          "text": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com"
        }
      }
    ],
    "tools": [
      {
        "computer_use": {
          "environment": "ENVIRONMENT_BROWSER",
          "enable_prompt_injection_detection": true
        }
      }
    ]
  }'
```

### 2. Receber a resposta do modelo

A resposta do modelo sugere uma chamada de função com coordenadas e uma
intenção de raciocínio personalizada explicando a ação:

```
{
  "function_call": {
    "name": "click",
    "args": {
      "x": 450,
      "y": 120,
      "intent": "Click the search box to type the destination."
    }
  }
}
```

### 3. Executar as ações recebidas

O código do aplicativo precisa analisar a resposta do modelo, executar as ações
e coletar os resultados.

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
    function_calls = []

    # Parse function calls from candidate response
    parts = candidate.content.parts if hasattr(candidate, 'content') else []
    if not parts and hasattr(candidate, 'function_calls'):
        function_calls = candidate.function_calls
    else:
        for part in parts:
            if part.function_call:
                function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname == "open_app":
                pass # Handled / already open
            elif fname in ("click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname == "click":
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname == "type":
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(candidate, page, screenWidth, screenHeight) {
    const results = [];
    let functionCalls = [];

    // Parse function calls from candidate response
    const parts = candidate.content?.parts || [];
    if (parts.length === 0 && candidate.functionCalls) {
        functionCalls = candidate.functionCalls;
    } else {
        for (const part of parts) {
            if (part.functionCall) {
                functionCalls.push(part.functionCall);
            }
        }
    }

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.args;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_app") {
                // Handled / already open
            } else if (["click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### 4. Capturar o novo estado do ambiente

Capture uma representação da tela e retorne ao modelo.

### Python

```
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

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

Depois de definir como capturar e formatar o estado do ambiente, você pode combinar todas essas etapas em um loop de execução contínua.

## Criar um loop de agente

Para permitir interações em várias etapas, combine as quatro etapas da seção [Como implementar o uso do computador](#implement-computer-use) em um único loop. Esse ciclo continua solicitando ações e enviando os resultados de volta ao modelo até que a tarefa seja concluída.

Não se esqueça de gerenciar o histórico da conversa corretamente, adicionando as respostas do modelo e da função ao histórico em cada etapa.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright
from google import genai
from google.genai import types

client = genai.Client()

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Paste helper functions execute_function_calls and get_function_responses here

try:
    page.goto("https://ai.google.dev/gemini-api/docs")

    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER,
            enable_prompt_injection_detection=True
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        types.Content(role="user", parts=[
            types.Part(text=USER_PROMPT),
            types.Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join(
                part.text for part in candidate.content.parts if hasattr(part, 'text')
            )
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            types.Content(role="user", parts=[types.Part(function_response=fr) for fr in function_responses])
        )

finally:
    print("Closing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    await page.goto("https://ai.google.dev/gemini-api/docs");

    const config = {
        tools: [{
            computerUse: {
                environment: "ENVIRONMENT_BROWSER",
                enable_prompt_injection_detection: true
            }
        }],
        thinkingConfig: { includeThoughts: true }
    };

    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    const contents = [
        {
            role: "user",
            parts: [
                { text: USER_PROMPT },
                {
                    inlineData: {
                        data: initialScreenshotBase64,
                        mimeType: "image/png"
                    }
                }
            ]
        }
    ];

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);
        console.log("Thinking...");
        const response = await ai.models.generateContent({
            model: 'gemini-3.8-flash',
            contents: contents,
            config: config
        });

        const candidate = response.candidates[0];
        contents.push(candidate.content);

        const hasFunctionCalls = candidate.content.parts.some(part => part.functionCall);
        if (!hasFunctionCalls) {
            const textResponse = candidate.content.parts
                .filter(part => part.text)
                .map(part => part.text)
                .join(" ");
            console.log("Agent finished:", textResponse);
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        contents.push({
            role: "user",
            parts: functionResponses.map(fr => ({
                ...fr
            }))
        });
    }
} finally {
    console.log("Closing browser...");
    await browser.close();
}
```

## Ambientes compatíveis

Os modelos do Gemini 3.x são compatíveis com três ambientes especificados nas configurações de `computer_use`:

### Ambiente do navegador (`ENVIRONMENT_BROWSER`)

Ações na ferramenta do navegador:

| Nome do comando | Descrição | Argumentos (na chamada de função) |
| --- | --- | --- |
| **click** | Clica com o botão esquerdo na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Clica duas vezes na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Clica três vezes na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Clica com o botão do meio na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Clica com o botão direito do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Toca e mantém pressionado o botão do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Solta o botão do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Move o cursor para a posição especificada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Digita texto. | `text`: str `press_enter`: bool (opcional, padrão `false`) `intent`: str |
| **drag\_and\_drop** | Arrasta um item da coordenada inicial até a coordenada final. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Pausa a execução por um número especificado de segundos. | `seconds`: int (opcional, padrão `1`) `intent`: str |
| **press\_key** | Pressiona e solta a tecla especificada. | `key`: str `intent`: str |
| **key\_down** | Toca e pressiona a tecla especificada. | `key`: str `intent`: str |
| **key\_up** | Libera a chave especificada. | `key`: str `intent`: str |
| **hotkey** | Pressiona a combinação de teclas especificada. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Retorna uma captura da tela atual. | `intent`: str |
| **scroll** | Rola para cima, para baixo, para a esquerda ou para a direita em uma coordenada por uma distância de pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, opcional, padrão `300`) `intent`: str |
| **go\_back** | Volta para a página da Web anterior no histórico de navegação do navegador. | `intent`: str |
| **navigate** | Navega diretamente para um URL especificado. | `url`: str `intent`: str |
| **go\_forward** | Navega para a próxima página da Web no histórico de navegação. | `intent`: str |

### Ambiente para dispositivos móveis (`ENVIRONMENT_MOBILE`)

Ações de ambiente otimizado para Android:

| Nome do comando | Descrição | Argumentos (na chamada de função) |
| --- | --- | --- |
| **open\_app** | Abre um aplicativo pelo nome. | `app_name`: str `intent`: str |
| **click** | Clica com o botão esquerdo na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | Lista os aplicativos disponíveis no dispositivo, retornando os nomes e nomes de pacotes. | `intent`: str |
| **wait** | Pausa a execução por um número especificado de segundos. | `seconds`: int (opcional, padrão `1`) `intent`: str |
| **go\_back** | Volta para a tela ou página da Web anterior. | `intent`: str |
| **type** | Digita texto. | `text`: str `press_enter`: bool (opcional, padrão `false`) `intent`: str |
| **drag\_and\_drop** | Arrasta um item da coordenada inicial até a coordenada final. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | Toca e mantém pressionada uma coordenada na tela. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (opcional, padrão `2`) `intent`: str |
| **press\_key** | Pressiona e solta a tecla especificada. | `key`: str `intent`: str |
| **take\_screenshot** | Retorna uma captura da tela atual. | `intent`: str |

### Ambiente de computador (`ENVIRONMENT_DESKTOP`)

Comandos de cursor no nível do SO para ambientes de área de trabalho:

| Nome do comando | Descrição | Argumentos (na chamada de função) |
| --- | --- | --- |
| **click** | Clica com o botão esquerdo na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Clica duas vezes na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Clica três vezes na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Clica com o botão do meio na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Clica com o botão direito do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Toca e mantém pressionado o botão do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Solta o botão do mouse na coordenada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Move o cursor para a posição especificada. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Digita texto. | `text`: str `press_enter`: bool (opcional, padrão `false`) `intent`: str |
| **drag\_and\_drop** | Arrasta um item da coordenada inicial até a coordenada final. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Pausa a execução por um número especificado de segundos. | `seconds`: int (opcional, padrão `1`) `intent`: str |
| **press\_key** | Pressiona e solta a tecla especificada. | `key`: str `intent`: str |
| **key\_down** | Toca e pressiona a tecla especificada. | `key`: str `intent`: str |
| **key\_up** | Libera a chave especificada. | `key`: str `intent`: str |
| **hotkey** | Pressiona a combinação de teclas especificada. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Retorna uma captura da tela atual. | `intent`: str |
| **scroll** | Rola para cima, para baixo, para a esquerda ou para a direita em uma coordenada por uma distância de pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, opcional, padrão `300`) `intent`: str |

## Funções definidas pelo usuário personalizadas

É possível estender a funcionalidade do modelo incluindo funções definidas pelo usuário. Por exemplo, em cenários de human-in-the-loop (HITL), é possível excluir ações predefinidas padrão e registrar ações personalizadas.

### Python

Exclua as ações padrão predefinidas do navegador (como `click`) e registre uma ferramenta `yield_to_user` personalizada:

```
from google import genai
from google.genai import types

client = genai.Client()

yield_to_user_tool = types.FunctionDeclaration(
    name="yield_to_user",
    description="Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "reason": types.Schema(
                type="STRING",
                description="The reason why the agent is yielding control to the human."
            )
        },
        required=["reason"]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Click the submit button. If you need a second factor authentication code, ask me.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment="ENVIRONMENT_MOBILE",
                    excluded_predefined_functions=["click"]
                )
            ),
            yield_to_user_tool
        ]
    )
)
```

## Como gerenciar os níveis de raciocínio

Para agentes de uso de computador, é possível configurar diferentes níveis de pensamento para equilibrar a qualidade da ação e a velocidade de execução. Os níveis de pensamento mais baixos geralmente alcançam um bom equilíbrio para tarefas de automação padrão.

## Segurança e proteção

### Configurar políticas de segurança

Os modelos do Gemini 3.x incluem categorias de serviços de segurança integradas que ajudam a determinar se a confirmação do usuário é necessária.

| Categoria da política de segurança | Descrição |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | Bloqueia ou aciona a confirmação de ações que envolvem pagamentos, finalização de compras no varejo ou produtos regulamentados. |
| `SENSITIVE_DATA_MODIFICATION` | Protege registros de saúde, financeiros ou governamentais contra modificações não autorizadas. |
| `COMMUNICATION_TOOL` | Impede que o agente envie e-mails, mensagens de chat ou rascunhos de forma autônoma. |
| `ACCOUNT_CREATION` | Restringe o agente de registrar novas contas em sites de forma autônoma. |
| `DATA_MODIFICATION` | Regula as modificações gerais do sistema de arquivos, o compartilhamento de dados e a exclusão do armazenamento. |
| `USER_CONSENT_MANAGEMENT` | Exige que o usuário assuma o controle dos banners de consentimento de cookies e das solicitações de privacidade. |
| `LEGAL_TERMS_AND_AGREEMENTS` | Impede que o modelo aceite de forma autônoma os Termos de Serviço ou contratos juridicamente vinculativos. |

#### Substituições de segurança

É possível modificar algumas políticas transmitindo substituições:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Clean up the local folder by archiving old logs.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_DESKTOP,
                    disabled_safety_policies=[
                        types.SafetyPolicy.DATA_MODIFICATION
                    ]
                )
            )
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
  contents: "Clean up the local folder by archiving old logs.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_DESKTOP",
        disabledSafetyPolicies: [
          "DATA_MODIFICATION"
        ]
      }
    }]
  }
});
```

### Detecção de injeção de comandos

O uso do computador para o Gemini 3.5 Flash-Lite ou posterior oferece suporte a um mecanismo de segurança avançado
para detectar ataques de injeção de comandos. Quando ativado, esse recurso
verifica se uma captura de tela incluída contém instruções adversárias
ocultas (por exemplo, "Ignorar comandos anteriores") e bloqueia
a execução quando detectado.

A detecção de injeção de comandos é um recurso de ativação. O padrão é `false`.

Os exemplos a seguir mostram como ativar a detecção de injeção de comandos
na configuração da ferramenta de uso do computador:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Search for flight deals and summarize top results.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment="ENVIRONMENT_DESKTOP",
                    enable_prompt_injection_detection=True,
                )
            )
        ]
    ),
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Search for flight deals and summarize top results.",
    config: {
        tools: [{
            computerUse: {
                environment: "ENVIRONMENT_DESKTOP",
                enablePromptInjectionDetection: true,
            }
        }]
    }
});
```

### cURL

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${GEMINI_API_KEY}" \
-H 'Content-Type: application/json' \
-d '{
  "contents": [{
    "parts": [{"text": "Search for flight deals and summarize top results."}]
  }],
  "tools": [{
    "computer_use": {
      "environment": "ENVIRONMENT_DESKTOP",
      "enable_prompt_injection_detection": true
    }
  }]
}'
```

### Confirmar decisão de segurança

A resposta pode incluir um parâmetro `safety_decision` nos argumentos da chamada de função:

```
{
  "function_call": {
    "name": "click",
    "args": {
      "x": 60,
      "y": 100,
      "safety_decision": {
        "explanation": "Must check check-box",
        "decision": "require_confirmation"
      }
    }
  }
}
```

Se o `safety_decision` for `require_confirmation`, mostre uma solicitação ao usuário final. Se o
usuário confirmar, defina `safety_acknowledgement` em `FunctionResponse`.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.args:
    decision = get_safety_confirmation(function_call.args['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### Práticas recomendadas de segurança

O uso de computadores apresenta riscos operacionais e de segurança exclusivos, já que um modelo que age em nome de um usuário pode encontrar conteúdo não confiável nas telas ou cometer erros ao executar ações. Implemente as seguintes práticas recomendadas para proteger os dados e sistemas dos usuários:

1. **Human-in-the-loop (HITL)**:

   - **Exigir confirmação do usuário**:quando a resposta de segurança indicar
     `require_confirmation`, peça aprovação do usuário.
   - **Forneça instruções de segurança personalizadas**:implemente uma instrução do sistema personalizada para definir e aplicar seus próprios limites de segurança. Exemplo:

     ### Python

     ```
     from google import genai
     from google.genai import types

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

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
     """

     client = genai.Client()
     response = client.models.generate_content(
         model="gemini-3.8-flash",
         contents="Prepare a draft but do not send.",
         config=types.GenerateContentConfig(
             system_instruction=system_instruction,
             tools=[types.Tool(computer_use=types.ComputerUse(environment="ENVIRONMENT_BROWSER"))]
         )
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

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
         *   Compleying any purchase.
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

     If an action does **NOT** fall under the conditions for \`USER_CONFIRMATION\`,
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
     `;

     const response = await ai.models.generateContent({
       model: 'gemini-3.8-flash',
       contents: "Prepare a draft but do not send.",
       config: {
         systemInstruction: systemInstruction,
         tools: [{
           computerUse: {
             environment: "ENVIRONMENT_BROWSER"
           }
         }]
       }
     });
     ```
2. **Ambiente de execução seguro**:execute o agente em um ambiente seguro e em sandbox
   para limitar o impacto potencial. Pode ser uma máquina virtual (VM) em sandbox, um contêiner (por exemplo, Docker) ou um perfil de navegador dedicado com permissões limitadas. Consulte a
   [implementação de referência do GitHub](https://github.com/google/computer-use-preview/)
   para orientações de configuração do sandbox usando o Docker.
3. **Sanitização de entrada**:limpe todo o texto gerado pelo usuário nos comandos para
   mitigar o risco de instruções não intencionais ou injeção de comandos. Essa é uma
   camada de segurança útil, mas não substitui um ambiente de execução
   seguro.
4. **Proteções de conteúdo**:use proteções e APIs de segurança de conteúdo para avaliar
   as entradas do usuário, as entradas e saídas de ferramentas e as respostas do agente quanto à adequação,
   injeção de comandos e detecção de jailbreak.
5. **Listas de permissões e de bloqueio**:implemente mecanismos de filtragem para controlar onde o modelo pode navegar e o que ele pode fazer. Uma lista de bloqueio de sites proibidos é um bom ponto de partida, enquanto uma lista de permissões mais restritiva é ainda mais segura.
6. **Observabilidade e geração de registros**:mantenha registros detalhados para depuração, auditoria e resposta a incidentes. Seu cliente precisa registrar comandos,
   capturas de tela, ações sugeridas pelo modelo (`function_call`), respostas de segurança e
   todas as ações executadas pelo cliente.
7. **Gerenciamento de ambiente**:garanta que o ambiente da GUI seja consistente.
   Pop-ups, notificações ou mudanças inesperadas no layout podem confundir o
   modelo. Se possível, comece cada nova tarefa com um estado conhecido e limpo.

## Versões do modelo

É possível usar o recurso Uso do Computador com os seguintes modelos:

- [**Gemini 4 Argon**](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br) (`gemini-4-argon`): nosso modelo mais avançado, que permite o uso do computador para raciocínio complexo e fluxos de trabalho de interface agênticos.
- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pt-br) (`gemini-3.8-flash`): o modelo recomendado para uso em computadores, com interação de alta precisão na interface e chamadas de ferramentas confiáveis.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br) (`gemini-3.5-flash-lite`): um modelo de baixa latência e econômico que oferece suporte ao
  uso do computador.
- [**Pré-lançamento do Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) (`gemini-3-flash-preview`): modelo de pré-lançamento
  com suporte ao uso do computador.

## A seguir

- Teste o uso do computador no [ambiente de demonstração do Browserbase](http://gemini.browserbase.com).
- Confira o exemplo de código na [implementação de referência](https://github.com/google/computer-use-preview).
- Aprenda mais sobre outras ferramentas da API Gemini:
  - [Chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
  - [Embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
