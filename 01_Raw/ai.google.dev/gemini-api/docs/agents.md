---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=pt-BR
fetched_at: 2026-05-05T20:42:53.582176+00:00
title: "Vis\u00e3o geral dos agentes \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Visão geral dos agentes

Os agentes são sistemas que usam modelos do Gemini, um conjunto de ferramentas e recursos de raciocínio para realizar tarefas complexas de várias etapas e atingir metas específicas. Ao contrário de uma única chamada de modelo, um agente pode planejar, executar uma série de ações, interagir com sistemas externos e sintetizar informações para atender à solicitação de um usuário.

Com a API Gemini, é possível criar agentes eficientes usando recursos como:

- **[Modelos do Gemini](https://ai.google.dev/gemini-api/docs/models?hl=pt-br)**:a inteligência principal, que oferece raciocínio e compreensão de linguagem.
- **[Ferramentas](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)**:recursos que conectam o modelo a informações e ações do mundo real. Elas podem ser ferramentas integradas (como a Pesquisa Google, o Maps e a execução de código) ou personalizadas.
- **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**:o mecanismo para definir e conectar suas próprias ferramentas e APIs personalizadas ao modelo do Gemini.
- **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**:recursos que melhoram a capacidade do modelo de raciocinar e planejar tarefas complexas.
- **[Contexto longo](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br)**:permite que os agentes mantenham o estado e as informações em interações mais longas.

## Representantes disponíveis

- **[Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br)**:um agente autônomo que planeja, executa e sintetiza tarefas de pesquisa de várias etapas para casos de uso como análise de mercado, Deep Research e revisões de literatura.

## Como criar agentes

Os agentes usam modelos e ferramentas para concluir tarefas de várias etapas. Embora o Gemini ofereça os recursos de raciocínio (o "cérebro") e as ferramentas essenciais (as "mãos"), muitas vezes você precisa de uma estrutura de orquestração para gerenciar a memória do agente, planejar loops e realizar encadeamento de ferramentas complexo.

Para maximizar a confiabilidade em fluxos de trabalho de várias etapas, crie instruções que controlem explicitamente como o modelo raciocina e planeja. Embora o Gemini ofereça um raciocínio geral forte, agentes complexos se beneficiam de comandos que impõem comportamentos específicos, como persistência diante de problemas, avaliação de riscos e planejamento proativo.

Consulte os [fluxos de trabalho
de agente](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br#agentic-workflows) para
estratégias de design desses comandos. Confira um exemplo de uma [instrução do sistema](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br#agentic-si-template) que melhorou a performance em vários comparativos de agentes em cerca de 5%.

## Frameworks de agentes

O Gemini se integra aos principais frameworks de agentes de código aberto, como:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=pt-br): crie fluxos de aplicativos complexos e com estado e sistemas multiagentes usando estruturas de grafo.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=pt-br): conecte agentes do Gemini aos seus dados particulares para fluxos de trabalho aprimorados com RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=pt-br): orquestre agentes de IA autônomos colaborativos e de interpretação de papéis.
- [**SDK de IA da Vercel**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pt-br): crie
  interfaces e agentes de usuário com tecnologia de IA em JavaScript/TypeScript.
- [**ADK do Google**](https://google.github.io/adk-docs/get-started/python/): um framework de código aberto para criar e orquestrar agentes de IA interoperáveis.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
