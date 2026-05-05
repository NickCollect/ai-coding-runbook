---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-BR
fetched_at: 2026-05-05T19:48:54.174423+00:00
title: "Registros e conjuntos de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registros e conjuntos de dados

Este guia contém tudo o que você precisa para começar a ativar o registro em
log nos seus aplicativos da API Gemini. Neste guia, você vai aprender a
visualizar registros de um aplicativo novo ou atual no painel do Google AI Studio
para entender melhor o comportamento do modelo e como os usuários interagem com seus
aplicativos. Use o registro para observar, depurar e *compartilhar feedback de uso com o Google para ajudar a melhorar o Gemini em vários casos de uso de desenvolvedores*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-br)

Todas as chamadas de API `GenerateContent` e `StreamGenerateContent` são compatíveis, incluindo as feitas pelos endpoints de [compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

## 1. Ativar a geração de registros no Google AI Studio

Antes de começar, verifique se você tem um projeto ativado para faturamento.

1. Abra a página de registros no [AI Studio](https://aistudio.google.com/logs?hl=pt-br) do Google.
2. Escolha seu projeto no menu suspenso e pressione o botão "Ativar" para ativar o registro em log de todas as solicitações por padrão.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=pt-br)

É possível ativar ou desativar a geração de registros para todos os projetos ou para projetos específicos, e mudar essas preferências a qualquer momento no Google AI Studio.

## 2. Ver registros no AI Studio

1. Acesse o [AI Studio](https://aistudio.google.com/logs?hl=pt-br).
2. Selecione o projeto em que você ativou o registro em registros.
3. Seus registros vão aparecer na tabela em ordem cronológica inversa.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Clique em uma entrada para ver a visualização de página inteira do par de solicitação e resposta. Você pode inspecionar o comando completo, a resposta completa do Gemini e o contexto da troca anterior. Cada projeto tem um limite de armazenamento padrão de até 1.000 registros, e os registros não salvos em conjuntos de dados expiram após 55 dias. Se o projeto atingir o limite de armazenamento, você vai receber uma solicitação para excluir registros.

## 3. Selecionar e compartilhar conjuntos de dados

- Na tabela de registros, encontre a barra de filtro na parte de cima para selecionar uma propriedade e filtrar.
- Na visualização filtrada de registros, use as caixas de seleção para selecionar todos ou alguns deles.
- Clique no botão "Criar conjunto de dados" que aparece na parte de cima da lista.
- Dê um nome descritivo e uma descrição opcional ao novo conjunto de dados.
- Você vai encontrar o conjunto de dados que acabou de criar com o conjunto selecionado de registros.
- Exporte seu conjunto de dados para análise posterior como arquivos CSV, JSONL ou para o Google Planilhas.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Os conjuntos de dados podem ser úteis para vários casos de uso diferentes.

- **Organize conjuntos de desafios**:impulsione melhorias futuras em áreas que você quer que a IA melhore.
- **Organize conjuntos de amostras**:por exemplo, uma amostra de uso real para gerar respostas de outro modelo ou uma coleção de casos extremos para verificações de rotina antes da implantação.
- **Conjuntos de avaliação**:conjuntos representativos do uso real em recursos importantes, para comparação entre outros modelos ou iterações de instruções do sistema.

Você pode ajudar a impulsionar o progresso na pesquisa de IA, na API Gemini e no Google AI Studio
compartilhando seus conjuntos de dados como exemplos de demonstração. Isso nos permite refinar nossos modelos em diversos contextos e criar sistemas de IA que continuam sendo úteis para desenvolvedores em vários campos e aplicativos.

## Próximas etapas e o que testar

Agora que você ativou o registro em log, veja algumas coisas que você pode fazer:

- **Criar protótipos com o histórico de sessões**:use o [AI Studio Build](https://aistudio.google.com/apps?hl=pt-br) para programar apps e adicione sua chave de API para ativar um histórico de registros do usuário.
- **Executar novamente os registros com a API Gemini Batch**:use conjuntos de dados para amostragem de respostas e avaliação de modelos ou lógica de aplicativos executando novamente os registros pela [API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Compatibilidade

No momento, não há suporte para o registro em log nos seguintes casos:

- Modelos do Imagen e do Veo
- Modelo de embedding do Gemini
- Entradas com vídeos, GIFs ou PDFs

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
