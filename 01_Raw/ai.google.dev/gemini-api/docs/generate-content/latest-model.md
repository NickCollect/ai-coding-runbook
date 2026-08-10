---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=pt-BR
fetched_at: 2026-08-10T03:17:21.431477+00:00
title: "Como usar os modelos mais recentes do Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Como usar os modelos mais recentes do Gemini

[Esta página](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=pt-br)

O Gemini 3.6 Flash (`gemini-3.6-flash`) e o Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) estão em disponibilidade geral (GA) e prontos para uso na produção.

- **Gemini 3.6 Flash**: performance mais forte em tarefas complexas de agentes e multimodais, reduzindo o uso de tokens, com um preço mais baixo do que o 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: o modelo mais rápido e de menor custo da família 3.5. Supera as gerações anteriores do Flash-Lite para execução de alta capacidade.

Este guia explica as novidades de cada modelo, quais mudanças na API afetam seu código e como migrar.

### Gemini 3.6 Flash

1. Instale a habilidade:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Aplique a habilidade:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Instale a habilidade:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Aplique a habilidade:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Novos modelos

| Modelo | ID do modelo | Nível de pensamento padrão | Preços | Descrição |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | $1,50/1 milhão de tokens de entrada e $7,50/1 milhão de tokens de saída | Equilibra velocidade e inteligência para tarefas de agentes e multimodais. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | $0,30/1 milhão de tokens de entrada e $2,50/1 milhão de tokens de saída | O modelo 3.5 mais rápido e de menor custo para execução de alta capacidade. |

Os dois modelos oferecem suporte à janela de contexto de 1 milhão de tokens, 64 mil tokens de saída máximos, pensamento e o conjunto completo de ferramentas integradas, incluindo [Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br).

Para conferir as especificações completas, consulte as páginas do modelo:

- [Página do modelo Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br)
- [Página do modelo Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br)

Para conferir os preços detalhados, consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Guia de início rápido

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Novidades do Gemini 3.6 Flash

- **Redução de tokens e turnos**:conclui fluxos de trabalho de várias etapas com menos etapas de raciocínio, turnos de conversa e chamadas de ferramentas do que o Gemini 3.5. Ele também reduz a espiral do loop de execução.
- **Geração de código aprimorada**:produz código pronto para produção de maior qualidade, com menos edições indesejadas e menos loops de depuração.
- **Melhor acompanhamento de instruções**: reduz mudanças de arquivo indesejadas durante tarefas de diagnóstico.
- **Raciocínio multimodal e espacial forte**:performance aprimorada na interpretação de gráficos, conversão de projetos visuais e geração de layouts da Web com vários elementos.
- **Inspeção programática antecipada**:prefere executar scripts de código de diagnóstico antes de fazer mudanças com mais frequência do que o Gemini 3.5 Flash. Isso melhora a precisão em tarefas complexas, mas pode adicionar etapas exploratórias extras em trabalhos simples de front-end.
- **Suporte ao uso do computador**:com suporte como ferramenta nativa para automação de interface de agentes.
- **Preferência de estilo de interface**: melhor na criação de código funcional, embora os avaliadores humanos tenham preferido modelos anteriores para layout visual e estilo. É possível mitigar isso fornecendo diretrizes de design explícitas.
- **Esforço de pensamento padrão (médio)** : usa o mesmo nível de pensamento padrão `medium` do Gemini 3.5 Flash.
- **Preços reduzidos**: custos de token de saída mais baixos ($7,50/1 milhão em comparação com $9,00/1 milhão para o 3.5 Flash). Os tokens de entrada permanecem em $1,50/1 milhão.

## Novidades do Gemini 3.5 Flash-Lite

- **Latência de execução de tarefas reduzida**:maior capacidade de processamento na família 3.5 para análise de dados de alto volume e extração de documentos.
- **Raciocínio e performance multimodal aprimorados**:caminho de migração forte do Gemini 2.5 Flash, com pontuações mais altas em tarefas de raciocínio, como HLE (18,0% em comparação com 11,0%) e comparativos multimodais, como CharXIV (74,5% em comparação com 63,7%).
- **Orquestração de subagentes e confiabilidade de ferramentas**:melhora a confiabilidade da execução de ferramentas para execução de código, pesquisa e fluxos de trabalho de MCP. Aumente o nível de pensamento para planejamento autônomo e tarefas complexas de subagentes.
- **Melhor compreensão de documentos**:melhora a acurácia na análise de documentos e na extração de dados estruturados. Teste níveis de pensamento mínimos e altos, dependendo da complexidade do documento.
- **Programação interativa na Web e processamento de dados tabulares**:tem um bom desempenho no JavaScript de front-end e no processamento de dados tabulares, planejando a execução de código leve.
- **Chatbot e persistência de persona**:acompanhamento de instruções multiturno e consistência de persona mais fortes do que o Gemini 3.1 Flash-Lite.
- **Suporte ao uso do computador**:com suporte como ferramenta nativa para automação de interface de agentes.

## Como escolher o modelo Flash ou Flash-Lite certo

Use esta tabela para selecionar o modelo e o caminho de migração certos para suas cargas de trabalho.

Os dois modelos exigem a remoção de parâmetros de amostragem descontinuados (`temperature`, `top_p`, `top_k`) e turnos de modelo pré-preenchidos. Consulte [Mudanças na API](#api-changes-and-parameter-updates) para mais detalhes.

| Modelo | Principais casos de uso | Destino de migração recomendado |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Geração de código, raciocínio espacial/multimodal, fluxos de trabalho de agentes de várias etapas | **Gemini 3.5 Flash**, **Gemini 3 Flash (pré-lançamento)** ou **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | Execução autônoma de subagentes, análise de dados de alto volume e extração de documentos, análise JSON estruturada | **Gemini 3.1 Flash-Lite** ou **Gemini 2.5 Flash** |

## Agente do Antigravity atualizado

Devido à performance aprimorada, o Gemini 3.6 Flash agora é o novo modelo padrão que alimenta o [agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=pt-br) nos agentes gerenciados do Gemini. Isso pode ser alterado definindo um novo campo na API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Mudanças na API e atualizações de parâmetros

A partir do Gemini 3.6 Flash e do Gemini 3.5 Flash-Lite, as seguintes mudanças na API se aplicam a esses modelos e a todos os lançamentos futuros de modelos do Gemini.

- **Descontinuação do parâmetro de amostragem**: `temperature`, `top_p` e `top_k` foram descontinuados. A API ignora esses parâmetros e retorna um erro em gerações futuras de modelos.
- **Validação de turnos de modelo pré-preenchidos**: o pré-preenchimento de turnos de modelo não é mais aceito. Se o último turno não vazio na solicitação for um turno `model`, a API vai retornar um erro `400`.

Confira abaixo explicações detalhadas e exemplos de código para cada mudança na API.

### 1. Descontinuação do parâmetro de amostragem (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` e `top_k` foram descontinuados e ignorados. Em gerações futuras de modelos, o fornecimento desses parâmetros retorna um erro HTTP 400. **Remova esses parâmetros de todas as solicitações.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Para melhorar o determinismo, defina uma instrução de sistema com regras explícitas para seu caso de uso específico.

### 2. Validação de turnos de modelo pré-preenchidos

As solicitações de API que terminam com um turno de função de modelo não vazio não são permitidas e retornam um **erro HTTP 400**.

#### ⚠️ Evite

Em payloads REST brutos ou `generateContent` legados, o encerramento com um turno de função de modelo não é mais permitido:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Migração recomendada

Se o aplicativo tiver pré-preenchido um turno de modelo para suprimir preâmbulos ou forçar a formatação JSON, use `system_instruction` ou [saídas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) em vez disso.

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## Lista de verificação de migração

### Gemini 3.6 Flash

1. Instale a habilidade:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Aplique a habilidade:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Instale a habilidade:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Aplique a habilidade:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Migrar para o gemini-3.6-flash

- **Atualizar o ID do modelo**:mude a string do modelo de destino para `gemini-3.6-flash`.
- **Remover parâmetros de amostragem descontinuados:**
  - Remova `temperature`, `top_p` e `top_k` das configurações de geração.
  - Substitua `thinking_budget` pela enumeração de string `thinking_level` definida como `"medium"` ou `"high"`.
  - Remova `candidate_count` (não aceito no Gemini 3.x).
- **Aplicar regras de validação de turnos:**
  - Remova os turnos de modelo pré-preenchidos.
  - Verifique se o turno final do usuário contém texto não vazio.
- **Auditoria de chamadas de função**
  - Verifique se todos os objetos `FunctionResponse` incluem `call_id` e `name`.
  - Coloque recursos multimodais no payload da resposta.
  - Formate as instruções inline usando `\\n\\n`.
  - Se você encontrar erros `Malformed_Function_Call` vinculados a texto pré-ferramenta, consulte [Soluções alternativas para requisitos de texto pré-ferramenta](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=pt-br#workarounds-for-pre-tool-text-requirements).
- **Requisitos básicos do Gemini 3.x**:para atualizações do SDK e preservação da assinatura de pensamento, consulte a [lista de verificação de migração do Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=pt-br#migration).

### Migrar para o gemini-3.5-flash-lite

- **Atualizar o ID do modelo**:mude a string do modelo de destino para `gemini-3.5-flash-lite`.
- **Configurar o nível de esforço de pensamento:**
  - Para extração, roteamento ou classificação de alto volume: deixe `thinking_level` como `"minimal"` (padrão) para capacidade máxima.
  - Para subagentes autônomos com chamadas de ferramentas, execução de código ou raciocínio em várias etapas: defina `thinking_level` como `"medium"` ou `"high"` para evitar o encerramento prematuro da ferramenta.
- **Remover parâmetros descontinuados e validar chamadas de função:** aplique as [mesmas regras do 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **Requisitos básicos do Gemini 3.x**:consulte a [lista de verificação de migração do Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=pt-br#migration).

## Próximas etapas

- Revise as especificações da API na [visão geral dos modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).
- Conheça a orquestração multiagente no [guia da API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br).
- Teste e refine comandos no [Google AI Studio](https://aistudio.google.com/?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
