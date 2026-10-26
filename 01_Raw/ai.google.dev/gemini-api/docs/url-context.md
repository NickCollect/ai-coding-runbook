---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=pt-BR
fetched_at: 2026-10-26T05:56:02.510795+00:00
title: "Contexto do URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Contexto do URL

A ferramenta de contexto de URL permite fornecer contexto adicional aos modelos na forma de URLs. Ao incluir URLs na solicitação, o modelo vai acessar o conteúdo dessas páginas (desde que não seja um tipo de URL listado na [seção de limitações](#limitations)) para informar e melhorar a resposta.

A ferramenta de contexto de URL é útil para tarefas como as seguintes:

- **Extrair dados**: extraia informações específicas, como preços, nomes ou principais
  descobertas de vários URLs.
- **Comparar documentos**: analise vários relatórios, artigos ou PDFs para
  identificar diferenças e acompanhar tendências.
- **Sintetizar e criar conteúdo**: combine informações de vários URLs de origem para gerar resumos, postagens de blog ou relatórios precisos.
- **Analisar código e documentos**: aponte para um repositório do GitHub ou documentação técnica para explicar o código, gerar instruções de configuração ou responder a perguntas.

O exemplo a seguir mostra como comparar duas receitas de sites diferentes.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
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

    url1 := "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
    url2 := "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                fmt.Sprintf("Compare the ingredients and cooking times from the recipes at %s and %s", url1, url2),
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and its source annotations
    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                    if len(contentBlock.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range contentBlock.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                fmt.Printf("  - %s: %s\n", annotation.URLCitation.GetTitle(), annotation.URLCitation.GetURL())
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Como funciona

A ferramenta de contexto de URL usa um processo de recuperação de duas etapas para equilibrar velocidade, custo e acesso a dados atualizados. Quando você fornece um URL, a ferramenta primeiro tenta buscar o conteúdo de um cache de índice interno. Isso funciona como um cache altamente otimizado. Se um URL não estiver disponível no índice (por exemplo, se for uma página muito nova), a ferramenta vai fazer uma busca em tempo real.
Isso acessa diretamente o URL para recuperar o conteúdo em tempo real.

## Como combinar com outras ferramentas

Você pode combinar a ferramenta de contexto de URL com outras para criar fluxos de trabalho mais eficientes.

[Os modelos do Gemini 3](#supported-models) oferecem suporte à combinação de ferramentas integradas
(como o contexto de URL) com ferramentas personalizadas (chamada de função). Saiba mais na
[página de combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

### Embasamento com a pesquisa

Quando o contexto de URL e
[o embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pt-br) estão ativados,
o modelo pode usar os recursos de pesquisa para encontrar
informações relevantes on-line e usar a ferramenta de contexto de URL para entender melhor as páginas encontradas. Essa abordagem é útil para comandos que exigem pesquisa ampla e análise detalhada de páginas específicas.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
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
            Input: interactions.NewInteractionsInput("Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Entender a resposta

Quando o modelo usa a ferramenta de contexto de URL, a resposta de texto inclui anotações `url_citation` inline no bloco de conteúdo de texto. Cada anotação vincula um segmento do texto de resposta (via `start_index` e `end_index`) ao URL de origem de que foi derivado. Essa é a principal maneira de mostrar citações no seu
aplicativo. Consulte o [exemplo principal acima](#get-started) para saber como extraí-las.

A resposta também inclui uma etapa `url_context_result` com metadados sobre cada tentativa de recuperação de URL (status, URL recuperado). Isso é útil principalmente para depuração.

### Verificações de segurança

O sistema realiza uma verificação de moderação de conteúdo nos URLs para confirmar se eles atendem aos padrões de segurança. Se um URL falhar nessa verificação, a etapa correspondente
`url_context_result` vai mostrar um `status` de `"unsafe"`.

### Contagem de tokens

O conteúdo recuperado dos URLs especificados no comando é contabilizado como parte dos tokens de entrada. É possível conferir a contagem de tokens no objeto `usage` da interação. Confira o seguinte exemplo:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

O preço por token depende do modelo usado. Consulte a
[página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.

## Modelos compatíveis

| Modelo | Contexto do URL |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pt-br) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br) | ✔️ |
| [Gemini 3.1 Pro (pré-lançamento)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Gemini 3 Flash (pré-lançamento)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## Práticas recomendadas

- **Forneça URLs específicos**: para melhores resultados, forneça URLs diretos para o
  conteúdo que você quer que o modelo analise. O modelo só vai recuperar conteúdo dos URLs fornecidos, não de links aninhados.
- **Verifique a acessibilidade**: verifique se os URLs fornecidos não levam a
  páginas que exigem login ou estão atrás de um paywall.
- **Use o URL completo**: forneça o URL completo, incluindo o protocolo
  (por exemplo, https://www.google.com em vez de apenas google.com).

## Limitações

- Limite de solicitações: a ferramenta pode processar até 20 URLs por solicitação.
- Tamanho do conteúdo do URL: o tamanho máximo do conteúdo recuperado de um único URL é de 34 MB.
- Acessibilidade pública: os URLs precisam estar acessíveis publicamente na Web.
  Endereços de localhost (por exemplo, localhost, 127.0.0.1), redes particulares e serviços de tunelamento (por exemplo, ngrok, pinggy) não são aceitos.

### Tipos de conteúdo aceitos e não aceitos

A ferramenta pode extrair conteúdo de URLs com os seguintes tipos de conteúdo:

- Texto (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Imagem (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Os seguintes tipos de conteúdo **não** são aceitos:

- Conteúdo com paywall
- Vídeos do YouTube (consulte
  [Entendimento de vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br#youtube) para saber
  como processar URLs do YouTube)
- Arquivos do Google Workspace, como documentos ou planilhas do Google
- Arquivos de áudio e vídeo

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
