---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-BR
fetched_at: 2026-05-18T05:06:41.656106+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Embasamento com a Pesquisa Google

O embasamento com a Pesquisa Google conecta o modelo do Gemini a conteúdo da Web em tempo real e funciona com todos os idiomas disponíveis. Isso permite que o Gemini forneça respostas mais precisas e cite fontes verificáveis além do limite de conhecimento.

O embasamento ajuda você a criar aplicativos que podem:

- **Aumentar a acurácia factual**:reduza as alucinações do modelo embasando as respostas em informações do mundo real.
- **Acessar informações em tempo real**:responda a perguntas sobre eventos e temas recentes.
- **Forneça citações**:aumente a confiança do usuário mostrando as fontes das declarações do modelo.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

# Print the model's text response
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

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

const modelStep = interaction.steps.find(s => s.type === 'model_output');
if (modelStep) {
  for (const contentBlock of modelStep.content) {
    if (contentBlock.type === 'text') console.log(contentBlock.text);
  }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Como funciona o embasamento com a Pesquisa Google

Quando você ativa a ferramenta `google_search`, o modelo processa todo o fluxo de trabalho de pesquisa, tratamento e citação de informações automaticamente.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=pt-br)

1. **Comando do usuário**:seu aplicativo envia um comando do usuário para a API Gemini
   com a ferramenta `google_search` ativada.
2. **Análise do comando**:o modelo analisa o comando e determina se uma
   Pesquisa Google pode melhorar a resposta.
3. **Pesquisa Google**:se necessário, o modelo gera e executa automaticamente uma ou várias consultas de pesquisa.
4. **Processamento de resultados da pesquisa**:o modelo processa os resultados da pesquisa, sintetiza as informações e formula uma resposta.
5. **Resposta embasada**:a API retorna uma resposta final e fácil de usar que
   é baseada nos resultados da pesquisa. Essa resposta inclui o texto do modelo
   com `annotations` inline contendo as citações, bem como
   etapas `google_search_call` e `google_search_result` com as consultas
   de pesquisa e sugestões de pesquisa.

## Entender a resposta de embasamento

Quando uma resposta é fundamentada, a saída de texto do modelo inclui `annotations` inline diretamente no bloco de conteúdo de texto. Essas anotações
fornecem informações de citação que vinculam partes da resposta às fontes.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Os campos principais na resposta:

- `google_search_call` : contém a pesquisa `queries` executada pelo modelo.
- `google_search_result` : contém `search_suggestions`, um snippet HTML
  para renderizar sugestões de pesquisa na sua interface. Os requisitos de uso completos estão detalhados nos [Termos de Serviço](https://ai.google.dev/gemini-api/terms?hl=pt-br#grounding-with-google-search).
- `text` com `annotations` : a resposta sintetizada do modelo com citações
  inline. Cada anotação `url_citation` vincula um segmento de texto (definido por `start_index` e `end_index`) a um URL de origem. Essa é a chave para
  criar citações inline.

O embasamento com a Pesquisa Google também pode ser usado em combinação com a [ferramenta de contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br) para embasar respostas em dados públicos da Web e nos URLs específicos que você fornece.

## Atribuição de fontes com citações inline

A API retorna anotações `url_citation` inline no bloco de conteúdo de texto, controle total sobre como você mostra as fontes na interface do usuário.
Cada anotação inclui `start_index` e `end_index` para identificar a parte do texto que ela cita. Veja como extrair e mostrar esses dados.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

A saída vai mostrar o texto seguido das citações:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Preços

Quando você usa o Embasamento com a Pesquisa Google com o Gemini 3, seu projeto é cobrado
por cada consulta de pesquisa que o modelo decide executar. Se o modelo decidir executar várias consultas de pesquisa para responder a um único comando (por exemplo, pesquisar `"UEFA Euro 2024 winner"` e `"Spain vs England Euro 2024 final
score"` na mesma chamada de API), isso será contabilizado como dois usos faturáveis da ferramenta para essa solicitação. Para fins de faturamento, ignoramos as consultas de pesquisa na Web vazias ao contar as consultas únicas. Esse modelo de faturamento se aplica apenas aos modelos do Gemini 3. Ao usar o embasamento da pesquisa com o Gemini 2.5 ou modelos mais antigos, seu projeto é faturado por comando.

Para informações detalhadas sobre preços, consulte a [página de preços da API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Modelos compatíveis

Confira todos os recursos na página [Visão geral do modelo](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

| Modelo | Embasamento com a Pesquisa Google |
| --- | --- |
| Pré-lançamento da imagem do Gemini 3.1 Flash | ✔️ |
| Pré-lançamento do Gemini 3.1 Pro | ✔️ |
| Pré-lançamento do Gemini 3 Pro Image | ✔️ |
| Pré-lançamento do Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinações de ferramentas compatíveis

Você pode usar o embasamento com a Pesquisa Google com outras ferramentas, como [execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) e [contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br), para casos de uso mais complexos.

Os modelos do Gemini 3 permitem combinar ferramentas integradas (como o embasamento com a Pesquisa Google) e personalizadas (chamada de função). Saiba mais na página de
[combinações de ferramentas](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br).

## A seguir

- Saiba mais sobre outras ferramentas disponíveis, como a [chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br).
- Saiba como aumentar os comandos com URLs específicos usando a [ferramenta de contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-12 UTC."],[],[]]
