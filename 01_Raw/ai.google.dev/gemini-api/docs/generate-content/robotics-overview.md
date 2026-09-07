---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=pt-BR
fetched_at: 2026-09-07T05:49:46.288738+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Gemini Robotics ER

Os modelos de raciocínio incorporado (ER) do Gemini Robotics são modelos de visão-linguagem (VLMs) que permitem que os robôs percebam e interajam com o mundo físico. Eles interpretam dados visuais, fazem raciocínio espacial e temporal, planejam tarefas com várias etapas e orquestram robôs e ferramentas.

## Modelos

O modelo Gemini Robotics ER 2 é a versão mais recente do Gemini Robotics.
É nosso modelo de raciocínio atualizado que permite que os robôs entendam os ambientes com precisão. Ele é especializado em recursos de raciocínio incorporado, como orquestração agêntica de robôs (por exemplo, usando VLAs), compreensão de vídeo de robôs, incluindo compreensão de progresso e detecção de sucesso, leitura de instrumentos, apontamento e raciocínio espacial.

O modelo Gemini Robotics ER 2 apresenta dois endpoints de modelo:

- **`gemini-robotics-er-2-preview`**: o modelo padrão de ER 2. Baseado no Gemini 3.5 Flash com raciocínio espacial aprimorado, localização de descobertas em vídeo, classificação do progresso do vídeo, orquestração de vários robôs e uso de ferramentas em várias etapas.
- **`gemini-robotics-er-2-streaming-preview`**: otimizado para streaming em tempo real pela [API Live](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-br). Use este modelo para agentes robóticos de baixa latência que processam entrada contínua de áudio e vídeo.

Se você estiver usando o Gemini Robotics ER 1.6, faça upgrade para o Gemini Robotics ER 2 substituindo
`model="gemini-robotics-er-1.6-preview"` por
`model="gemini-robotics-er-2-preview"` ou
`model="gemini-robotics-er-2-streaming-preview"` nas suas chamadas de API. O modelo Gemini Robotics ER 1.6 será desativado no [fim de agosto](https://ai.google.dev/gemini-api/docs/deprecations?hl=pt-br#robotics-models).

[Teste o Gemini Robotics ER 2 no Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=pt-br)

## Recursos de robótica

O Gemini Robotics ER oferece suporte a uma variedade de recursos de raciocínio incorporado.
Selecione uma funcionalidade para saber mais:

| Capacidade | Descrição | Guia |
| --- | --- | --- |
| Raciocínio espacial | Aponte para objetos, rastreie-os em vídeos, detecte com caixas delimitadoras e planeje trajetórias. | [Raciocínio espacial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=pt-br) |
| Visão agêntica | Use a execução de código para melhorar outros recursos com ferramentas de manipulação de imagens. | [Visão agêntica](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=pt-br) |
| Orquestração de tarefas | Combine o raciocínio espacial com APIs de robôs personalizados para concluir tarefas de longo prazo. | [Orquestração de tarefas](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=pt-br) |
| Streaming (somente endpoint de streaming do Gemini Robotics ER 2) | Streaming bidirecional para agentes robóticos em tempo real com baixa latência e chamadas de função. | [Streaming para robótica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-br) |
| Andamento do vídeo (somente no Gemini Robotics ER 2) | Localização de momentos e classificação de progresso com base em feeds de vídeo contínuos. | [Compreensão do vídeo](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=pt-br) |

## Primeiros passos

O exemplo a seguir encontra objetos em uma imagem e retorna as coordenadas e os rótulos 2D normalizados deles. É possível transmitir essa saída diretamente para uma API de robótica ou um modelo de VLA para gerar ações de robôs.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

A saída será uma matriz JSON contendo objetos, cada um com um `point` (coordenadas `[y, x]` normalizadas) e um `label` que identifica o objeto.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

A imagem a seguir é um exemplo de como esses pontos podem ser mostrados:

![Um exemplo que mostra os pontos de objetos em uma imagem](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=pt-br)

## Como funciona

O Gemini Robotics ER usa entradas de imagem, vídeo ou áudio com comandos de linguagem natural. Ele identifica objetos, analisa o contexto da cena e as relações espaciais e retorna uma saída estruturada, como coordenadas ou caixas delimitadoras.

O Gemini Robotics ER também é agêntico: ele divide tarefas complexas em subtarefas e as executa chamando as funções do robô ou executando o código gerado. Por exemplo, "coloque a maçã na tigela" se torna uma sequência de etapas de localizar, pegar e colocar.

Consulte [Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=pt-br#how-it-works) para saber como o Gemini executa chamadas de ferramentas.

## Segurança

Embora o Gemini Robotics ER tenha sido criado pensando na segurança, é sua
responsabilidade manter um ambiente seguro ao redor do robô. Os modelos de IA generativa podem cometer erros, e os robôs físicos podem causar danos. Para saber mais, acesse a [página de segurança de robótica do Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=pt-br).

## Práticas recomendadas

1. Use uma linguagem simples e natural. Descreva o que você quer que o robô faça como se estivesse falando com uma pessoa. Se um termo não funcionar, tente um sinônimo comum.
2. Otimize a entrada visual. Corte ou faça zoom em objetos pequenos ou pouco claros antes de enviar a imagem. A iluminação e o baixo contraste de cores podem afetar a detecção.
3. Divida tarefas complexas em etapas. Envie cada etapa como um comando separado para manter o modelo focado e melhorar a precisão.
4. Consulte várias vezes e faça a média dos resultados para tarefas de alta precisão. Essa abordagem de consenso reduz a variância nas saídas espaciais.

## Limitações

Considere as seguintes limitações ao desenvolver com o Gemini Robotics ER:

- **Restrições de chave de API**:a API Gemini não aceita solicitações de chaves de API sem restrições e retorna um erro `403 Forbidden`. Proteja sua chave de API adicionando restrições no [AI Studio](https://aistudio.google.com/api-keys?hl=pt-br).
  Consulte [Proteger chaves de API irrestritas](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#secure-unrestricted-keys) para mais detalhes.
- **Latência x desempenho**:consultas complexas, entradas de alta resolução ou níveis de pensamento elevados podem aumentar os tempos de processamento. Para o nível de pensamento, use "médio" para um bom equilíbrio entre latência e desempenho.
- **Alucinações**:como todos os modelos de linguagem grandes, os modelos de resposta de emergência da Gemini Robotics podem ocasionalmente "alucinar" ou fornecer informações incorretas, especialmente para comandos ambíguos ou entradas fora da distribuição.
- **Dependência da qualidade do comando**:a qualidade da saída depende da clareza do comando de entrada. Use comandos específicos e bem estruturados.
- **Custo computacional**:executar o modelo, principalmente com entradas de vídeo ou `thinking_budget` alto, consome recursos computacionais e gera custos.
  Consulte a página [Pensamento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pt-br) para mais detalhes.
- **Tipos de entrada**:consulte os tópicos a seguir para saber mais sobre as limitações de cada modo.
  - [Entradas de imagem](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=pt-br#technical-details-image)
  - [Entradas de vídeo](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pt-br#supported-formats)
  - [Entradas de áudio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pt-br#supported-formats)

## Aviso de privacidade

Você reconhece que os modelos mencionados neste documento (os "Modelos de robótica") usam dados de vídeo e áudio para operar e mover seu hardware de acordo com suas instruções. Portanto, você pode operar os Modelos de robótica de forma que dados de pessoas identificáveis, como voz, imagens e dados de semelhança ("Dados pessoais"), sejam coletados por eles. Se você optar por operar os modelos de robótica de uma maneira que colete dados pessoais, concorda em não permitir que pessoas identificáveis interajam ou estejam presentes na área ao redor dos modelos de robótica, a menos que essas pessoas identificáveis tenham sido suficientemente notificadas e consentido com o fato de que seus dados pessoais podem ser fornecidos e usados pelo Google conforme descrito nos Termos Adicionais de Serviço da API Gemini, disponíveis em [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=pt-br) (os "Termos"), incluindo de acordo com a seção intitulada "Como o Google usa seus dados". Você vai garantir que esse aviso permita a coleta e o uso de dados pessoais conforme descrito nos Termos e vai usar esforços comercialmente razoáveis para minimizar a coleta e a distribuição de dados pessoais usando técnicas como desfoque de rosto e operando os modelos de robótica em áreas sem pessoas identificáveis, na medida do possível.

## Preços

Para informações detalhadas sobre preços e regiões disponíveis, consulte a página de [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Endpoints de modelos

### Pré-lançamento do Gemini Robotics ER 2

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-2-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  Compatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  Compatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  Compatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  Compatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  Compatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  incompatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  Compatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  Compatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  Compatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-2-preview` |
| calendar\_monthÚltima atualização | Julho de 2026 |
| id\_cardCard de modelo | [Card de modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pt-br) |

### Pré-lançamento do Gemini Robotics ER 2 Streaming

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  incompatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  incompatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  incompatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  incompatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  incompatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  Compatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  incompatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  incompatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  incompatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthÚltima atualização | Julho de 2026 |
| id\_cardCard de modelo | [Card de modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pt-br) |

### Pré-lançamento do Gemini Robotics ER 1.6

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-1.6-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  Compatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  Compatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  Compatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  Compatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  Compatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  incompatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  Compatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  Compatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  Compatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-1.6-preview` |
| calendar\_monthÚltima atualização | Dezembro de 2025 |
| cognition\_2Limite de conhecimento | Janeiro de 2025 |

## A seguir

- [Raciocínio espacial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=pt-br): apontamento, rastreamento, caixas delimitadoras, trajetórias.
- [Recursos agênticos](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=pt-br): execução de código, leitura de instrumentos, anotação de imagens.
- [Orquestração de tarefas](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=pt-br): tarefas de longo prazo com APIs de robôs personalizadas.
- [Robótica com streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-br): streaming bidirecional em tempo real (somente Gemini Robotics ER 2).
- [Compreensão de vídeo](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=pt-br): identificação de momentos e classificação de progresso (somente Gemini Robotics ER 2).
- [Segurança de robótica do Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=pt-br): pesquisa de segurança por trás da família de modelos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-04 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-04 UTC."],[],[]]
