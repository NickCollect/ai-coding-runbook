---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=pt-BR
fetched_at: 2026-06-29T05:34:14.994665+00:00
title: "Contexto do URL \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Contexto do URL

[A ferramenta de contexto de URL permite fornecer contexto adicional aos modelos na forma de URLs. Ao incluir URLs na solicitação, o modelo acessa o conteúdo dessas páginas (desde que não seja um tipo de URL listado na seção de limitações) para informar e melhorar a resposta.](#limitations)

A ferramenta de contexto de URL é útil para tarefas como as seguintes:

- **Extrair dados**: extraia informações específicas, como preços, nomes ou principais
  descobertas de vários URLs.
- **Comparar documentos**: analise vários relatórios, artigos ou PDFs para
  identificar diferenças e acompanhar tendências.
- **Sintetizar e criar conteúdo**: combine informações de vários URLs de origem para gerar resumos, postagens de blog ou relatórios precisos.
- **Analisar código e documentos**: aponte para um repositório do GitHub ou documentação técnica para explicar o código, gerar instruções de configuração ou responder perguntas.

O exemplo a seguir mostra como comparar duas receitas de sites diferentes.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Como funciona

A ferramenta de contexto de URL usa um processo de recuperação de duas etapas para equilibrar velocidade, custo e acesso a dados atualizados. Quando você fornece um URL, a ferramenta primeiro tenta buscar o conteúdo de um cache de índice interno. Isso funciona como um cache altamente otimizado. Se um URL não estiver disponível no índice (por exemplo, se for uma página muito nova), a ferramenta fará um retorno automático para fazer uma busca ativa.
Isso acessa diretamente o URL para recuperar o conteúdo em tempo real.

## Como combinar com outras ferramentas

Você pode combinar a ferramenta de contexto de URL com outras ferramentas para criar fluxos de trabalho mais eficientes.

[Os modelos do Gemini 3](#supported-models) aceitam a combinação de ferramentas integradas
(como o contexto de URL) com ferramentas personalizadas (chamada de função). Saiba mais na
[página de combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

### Embasamento com pesquisa

Quando o contexto de URL e
[o embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pt-br) estão ativados,
o modelo pode usar os recursos de pesquisa para encontrar
informações relevantes on-line e usar a ferramenta de contexto de URL para entender melhor as páginas encontradas. Essa abordagem é útil para comandos que exigem pesquisa ampla e análise detalhada de páginas específicas.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Entender a resposta

Quando o modelo usa a ferramenta de contexto de URL, a resposta inclui um objeto `url_context_metadata`. Esse objeto lista os URLs de que o modelo recuperou conteúdo e o status de cada tentativa de recuperação, o que é útil para verificação e depuração.

Confira a seguir um exemplo dessa parte da resposta (algumas partes foram omitidas para maior brevidade):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Para detalhes completos sobre esse objeto , consulte a
[`UrlContextMetadata` referência da API](https://ai.google.dev/api/generate-content?hl=pt-br#UrlContextMetadata).

### Verificações de segurança

O sistema realiza uma verificação de moderação de conteúdo no URL para confirmar se ele atende aos padrões de segurança. Se o URL fornecido falhar nessa verificação, você receberá um `url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Contagem de tokens

O conteúdo recuperado dos URLs especificados no comando é contabilizado como parte dos tokens de entrada. Você pode conferir a contagem de tokens do comando e
o uso de ferramentas no [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=pt-br#UsageMetadata)
objeto da saída do modelo. Confira um exemplo de saída:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

O preço por token depende do modelo usado. Consulte a
[página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.

## Modelos compatíveis

| Modelo | Contexto do URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pt-br) | ✔️ |
| [Gemini 3.1 Pro (pré-lançamento)](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
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

- Chamada de função: o uso de ferramentas (contexto de URL, embasamento com a Pesquisa Google etc.) com a chamada de função não é aceito no momento.
- Limite de solicitações: a ferramenta pode processar até 20 URLs por solicitação.
- Tamanho do conteúdo do URL: o tamanho máximo do conteúdo recuperado de um único URL é de 34 MB.
- Acessibilidade pública: os URLs precisam estar acessíveis publicamente na Web.
  Endereços de localhost (por exemplo, localhost, 127.0.0.1), redes particulares e serviços de tunelamento (por exemplo, ngrok, pinggy) não são aceitos.
- Somente API Gemini: o contexto de URL está disponível apenas na API Gemini, não na Gemini Enterprise Agent Platform.

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
- Arquivos do Google Workspace, como Documentos Google ou Planilhas Google
- Arquivos de áudio e vídeo

## A seguir

- Confira o [manual de contexto de URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=pt-br#url-context)
  para mais exemplos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-23 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-23 UTC."],[],[]]
