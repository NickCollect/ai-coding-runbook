---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=pt-BR
fetched_at: 2026-06-01T05:57:38.107756+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Embasamento com a Pesquisa Google

O embasamento com a Pesquisa Google conecta o modelo do Gemini ao conteúdo da Web em tempo real e funciona com todos os idiomas disponíveis. Isso permite que o Gemini forneça respostas mais precisas e cite fontes verificáveis além do limite de conhecimento.

O embasamento ajuda a criar aplicativos que podem:

- **Aumentar a precisão factual**:reduza as alucinações do modelo com base em informações do mundo real.
- **Acessar informações em tempo real**:responda a perguntas sobre eventos e tópicos recentes.
- **Fornecer citações**:crie confiança do usuário mostrando as fontes das declarações do modelo.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Saiba mais testando o [notebook da ferramenta de pesquisa](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=pt-br).

## Como funciona o embasamento com a Pesquisa Google

Quando você ativa a ferramenta `google_search`, o modelo processa todo o fluxo de trabalho de pesquisa, processamento e citação de informações automaticamente.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=pt-br)

1. **Comando do usuário**:seu aplicativo envia um comando do usuário para a API Gemini com a ferramenta `google_search` ativada.
2. **Análise de comandos**:o modelo analisa o comando e determina se uma Pesquisa Google pode melhorar a resposta.
3. **Pesquisa Google**:se necessário, o modelo gera automaticamente uma ou várias consultas de pesquisa e as executa.
4. **Processamento de resultados da pesquisa**:o modelo processa os resultados da pesquisa, sintetiza as informações e formula uma resposta.
5. **Resposta embasada**:a API retorna uma resposta final e fácil de usar que é baseada nos resultados da pesquisa. Essa resposta inclui a resposta de texto do modelo e `groundingMetadata` com as consultas de pesquisa, os resultados da Web e as citações.

## Entender a resposta de embasamento

Quando uma resposta é embasada, ela inclui um campo `groundingMetadata`. Esses dados estruturados são essenciais para verificar declarações e criar uma experiência de citação avançada no aplicativo.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

A API Gemini retorna as seguintes informações com `groundingMetadata`:

- `webSearchQueries` : matriz das consultas de pesquisa usadas. Isso é útil para depurar e entender o processo de raciocínio do modelo.
- `searchEntryPoint` : contém o HTML e o CSS para renderizar as sugestões de pesquisa necessárias. Os requisitos de uso completos estão detalhados nos [Termos de
  Serviço](https://ai.google.dev/gemini-api/terms?hl=pt-br#grounding-with-google-search).
- `groundingChunks` : matriz de objetos que contêm as fontes da Web (`uri` e `title`).
- `groundingSupports` : matriz de blocos para conectar a resposta do modelo `text` às fontes em `groundingChunks`. Cada bloco vincula um `segment` de texto (definido por `startIndex` e `endIndex`) a um ou mais `groundingChunkIndices`. Essa é a chave para criar citações inline.

O embasamento com a Pesquisa Google também pode ser usado em combinação com a ferramenta de contexto de [URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) para embasar respostas em dados da Web públicos
e nos URLs específicos que você fornece.

## Atribuir fontes com citações inline

A API retorna dados de citação estruturados, oferecendo controle total sobre como você mostra as fontes na interface do usuário. É possível usar os campos `groundingSupports` e `groundingChunks` para vincular as declarações do modelo diretamente às fontes. Confira um padrão comum para processar os metadados e criar uma resposta com citações inline clicáveis.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

A nova resposta com citações inline será assim:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Preços

Quando você usa o embasamento com a Pesquisa Google com o Gemini 3, seu projeto é cobrado por cada consulta de pesquisa que o modelo decide executar. Se o modelo decidir
executar várias consultas de pesquisa para responder a um único comando (por exemplo,
pesquisar `"UEFA Euro 2024 winner"` e `"Spain vs England Euro 2024 final
score"` na mesma chamada de API), isso será contabilizado como dois usos faturáveis da ferramenta
para essa solicitação. Para fins de faturamento, ignoramos as consultas de pesquisa na Web vazias ao contar consultas exclusivas. Esse modelo de faturamento só se aplica aos modelos do Gemini 3. Ao usar o embasamento de pesquisa com o Gemini 2.5 ou modelos mais antigos, seu projeto é cobrado por comando.

Para informações detalhadas sobre preços, consulte a [página de preços da API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Modelos compatíveis

Você pode encontrar recursos completos na página de visão geral do [modelo](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

| Modelo | Embasamento com a Pesquisa Google |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Pré-lançamento da imagem do Gemini 3.1 Flash | ✔️ |
| Pré-lançamento do Gemini 3.1 Pro | ✔️ |
| Pré-lançamento da imagem do Gemini 3 Pro | ✔️ |
| Pré-lançamento do Gemini 3 Flash | ✔️ |
| Pré-lançamento do Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinações de ferramentas compatíveis

Você pode usar o embasamento com a Pesquisa Google com outras ferramentas, como
[execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e
[contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br), para oferecer suporte a casos de uso mais complexos.

Os modelos do Gemini 3 oferecem suporte à combinação de ferramentas integradas (como o embasamento com a Pesquisa Google) com ferramentas personalizadas (chamada de função). Saiba mais na
[página de combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

## A seguir

- Teste o [embasamento com a Pesquisa Google no manual da API Gemini
  Gemini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=pt-br).
- Saiba mais sobre outras ferramentas disponíveis, como a [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br).
- Saiba como aumentar os comandos com URLs específicos usando a [ferramenta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-19 UTC."],[],[]]
