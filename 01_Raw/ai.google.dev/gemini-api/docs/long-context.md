---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=pt-BR
fetched_at: 2026-05-18T05:12:50.915597+00:00
title: "Contexto longo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Contexto longo

Muitos modelos do Gemini vêm com janelas de contexto grandes de 1 milhão ou mais tokens.
Historicamente, os modelos de linguagem grandes (LLMs) estavam significativamente limitados pela quantidade de texto (ou tokens) que poderiam ser transmitidos ao modelo de uma só vez.
A janela de contexto longo do Gemini libera muitos novos casos de uso e paradigmas de desenvolvedor.

O código que você já usa para casos como [text
generation](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br) ou [multimodal
inputs](https://ai.google.dev/gemini-api/docs/vision?hl=pt-br) vai funcionar sem mudanças com contexto longo.

Este documento oferece uma visão geral do que você pode alcançar usando modelos com janelas de contexto de 1 milhão ou mais tokens. A página oferece uma breve visão geral de uma janela de contexto e explica como os desenvolvedores devem pensar sobre o contexto longo, vários casos de uso reais para contexto longo e maneiras de otimizar o uso do contexto longo.

Para os tamanhos da janela de contexto de modelos específicos, consulte a
[página Modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

## O que é uma janela de contexto?

A maneira básica de usar os modelos do Gemini é transmitindo informações (contexto) ao modelo, que vai gerar uma resposta. Uma analogia com a janela de contexto é a memória de curto prazo. Há uma quantidade limitada de informações
que podem ser armazenadas na memória de curto prazo, e o mesmo vale para
modelos generativos.

Leia mais sobre como os modelos funcionam no nosso [guia de modelos
generativos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br#under-the-hood).

## Introdução ao contexto longo

As versões anteriores de modelos generativos só conseguiam processar 8.000 tokens de uma vez. Os modelos mais recentes avançaram ainda mais, aceitando 32.000 ou até 128.000 tokens. O Gemini é o primeiro modelo capaz de aceitar 1 milhão de tokens.

Na prática, 1 milhão de tokens seria:

- 50.000 linhas de código (com o padrão de 80 caracteres por linha)
- Todas as mensagens de texto que você enviou nos últimos cinco anos
- 8 romances ingleses de tamanho médio
- Transcrição de mais de 200 episódios de podcast de duração média

As janelas de contexto mais limitadas comuns em muitos outros modelos geralmente exigem estratégias como descartar arbitrariamente mensagens antigas, resumir conteúdo, usar RAG com bancos de dados vetoriais ou filtrar comandos para salvar tokens.

Embora essas técnicas continuem valiosas em cenários específicos, a extensa janela de contexto do Gemini convida a uma abordagem mais direta: fornecer todas as informações relevantes antecipadamente. Como os modelos do Gemini foram criados especificamente com recursos de contexto enormes, eles demonstram um aprendizado poderoso no contexto. Por
exemplo, usando apenas materiais instrucionais no contexto (uma gramática de referência de 500 páginas, um dicionário e cerca de 400 frases paralelas), o Gemini
[aprendeu a traduzir](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
do inglês para o Kalamang (um idioma papuano com menos de 200 falantes) com qualidade semelhante a um aluno humano usando os mesmos
materiais. Isso ilustra a mudança de paradigma possibilitada pelo contexto longo do Gemini, capacitando novas possibilidades por meio de um aprendizado robusto no contexto.

## Casos de uso de contexto longo

Embora o caso de uso padrão para a maioria dos modelos generativos ainda seja a entrada de texto, a família de modelos do Gemini possibilita um novo paradigma de casos de uso multimodais. Eles podem entender textos, vídeos, áudios e imagens de maneira nativa. Eles são
acompanhados pela [API Gemini, que aceita tipos de arquivos multimodais
por
questões de comodidade.](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=pt-br)

### Texto longo

O texto provou ser a camada de inteligência que sustenta grande parte do
impulso em torno dos LLMs. Como mencionado anteriormente, grande parte da limitação prática dos
LLMs se deve à falta de uma janela de contexto grande o suficiente para realizar determinadas
tarefas. Isso levou à rápida adoção da geração aumentada de recuperação (RAG, na sigla em inglês) e outras técnicas que fornecem dinamicamente ao modelo informações contextuais. Agora, com janelas de contexto cada vez maiores, novas técnicas são disponibilizadas, o que possibilita novos casos de uso.

Alguns casos de uso emergentes e padrão para contexto longo baseado em texto incluem o seguinte:

- Resumir grandes corpus de texto
  - As opções de resumo anteriores com modelos de contexto menores exigiam
    uma janela deslizante ou outra técnica para manter o estado das seções anteriores
    à medida que novos tokens eram transmitidos para o modelo.
- Perguntas e respostas
  - Historicamente, isso só era possível com o RAG, devido à quantidade limitada de
    contexto e à baixa recuperação de fatos dos modelos.
- Fluxos de trabalho agente
  - O texto é a base de como os agentes mantêm o estado do que fizeram
    e o que eles precisam fazer. Não ter informações suficientes sobre o mundo
    e o objetivo do agente é uma limitação na confiabilidade dos agentes

A [aprendizagem em contexto com muitas tentativas](https://arxiv.org/pdf/2404.11018) é um dos
recursos mais exclusivos liberados pelos modelos de contexto longo. As pesquisas mostram
que usar o exemplo de paradigma de "tentativa única" comum ou "muitas tentativas", em que
o modelo é apresentado com um ou alguns exemplos de uma tarefa e escalonando-o até
centenas, milhares ou mesmo centenas de milhares de exemplos, pode levar a
novos recursos do modelo. Essa abordagem de várias fotos também apresentou um desempenho
semelhante ao de modelos ajustados para uma tarefa específica. Para casos de uso
em que a performance de um modelo do Gemini ainda não é suficiente para um lançamento
em produção, tente a abordagem de várias tentativas. Como você pode explorar mais tarde
na seção de otimização de contexto longo, o armazenamento em cache de contexto torna esse tipo de
alta carga de trabalho de token de entrada muito mais viável e com latência ainda menor em alguns
casos.

### Vídeo mais longo

A utilidade do conteúdo de vídeo é, há muito tempo, limitada pela falta de acessibilidade
da própria mídia. Era difícil ler o conteúdo, as transcrições muitas vezes não conseguiam capturar as nuances de um vídeo e a maioria das ferramentas não processava imagem, texto e áudio juntos. Com o Gemini, os recursos de texto de contexto longo se traduzem na capacidade de raciocinar e responder a perguntas sobre entradas multimodais com desempenho sustentável.

Alguns casos de uso emergentes e padrão para contexto de vídeo longo incluem:

- Perguntas e respostas sobre vídeos
- Memória de vídeo, como mostrado com o [Project Astra do Google](https://deepmind.google/technologies/gemini/project-astra/?hl=pt-br)
- Legendas em vídeos
- Sistemas de recomendação de vídeo, enriquecendo os metadados com nova
  compreensão multimodal
- Personalização de vídeo, analisando um conjunto de dados e metadados de vídeos associados e, em seguida, removendo partes dos vídeos que não são relevantes para o
  leitor
- Moderação de conteúdo em vídeo
- Processamento de vídeo em tempo real

Ao trabalhar com vídeos, é importante considerar como os [vídeos são
processados em tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br#media-token), o que afeta
os limites de faturamento e uso. Saiba mais sobre comandos com arquivos de vídeo em
o [Guia de comandos](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=pt-br#prompting-with-videos).

### Áudio de longa duração

Os modelos do Gemini foram os primeiros modelos de linguagem grandes multimodais nativos que pudesse entender áudio. Historicamente, o fluxo de trabalho típico de um desenvolvedor envolveria unir vários modelos específicos de domínio, como um modelo de conversão de voz em texto e um modelo de texto para texto, a fim de processar o áudio. Isso levou a uma latência adicional necessária ao realizar várias solicitações de ida e volta e reduziu o desempenho, geralmente atribuído a arquiteturas desconexas da configuração de vários modelos.

Alguns casos de uso emergentes e padrão para contexto de áudio incluem o seguinte:

- Transcrição e tradução em tempo real
- Perguntas e respostas sobre podcasts / vídeos
- Transcrição e resumo de reuniões
- Assistentes por voz

Saiba mais sobre comandos com arquivos de áudio em [Guia de comandos](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=pt-br#prompting-with-videos).

## Otimizações de contexto longo

A otimização principal ao trabalhar com contexto longo e os modelos do Gemini
é usar o armazenamento em cache de [contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br). Além da impossibilidade anterior de processar muitos tokens em uma única solicitação, a outra restrição principal era o custo. Se você tiver um app de "conversa com seus dados" em que um usuário
carrega 10 PDFs, um vídeo e alguns documentos de trabalho, historicamente, você teria
que trabalhar com uma ferramenta / framework de geração aumentada de recuperação (RAG) mais complexa para processar essas solicitações e pagar um valor significativo por
tokens que foram movidos para a janela de contexto. Agora, é possível armazenar em cache os arquivos que o usuário envia e pagar para armazená-los por hora. O custo de entrada / saída por solicitação com o Gemini Flash, por exemplo, é cerca de 4 vezes menor do que o custo de entrada / saída padrão. Portanto, se o usuário conversar bastante com os dados, isso vai gerar uma grande economia de custos para você como desenvolvedor.

## Limitações de contexto longo

Em várias seções deste guia, falamos sobre como os modelos do Gemini alcançam alta performance em várias avaliações de recuperação de agulha no palheiro. Esses testes consideram a configuração mais básica, em que há apenas uma agulha que você está procurando. Nos casos em que você pode ter várias "agulhas" ou partes específicas de informações que está procurando, o modelo não tem o mesmo desempenho. A performance pode variar bastante dependendo do contexto. É importante considerar isso, pois há uma compensação inerente entre obter
a recuperação de informações e custos corretos. Você pode receber cerca de 99% em uma única consulta, mas
precisa pagar o custo do token de entrada sempre que enviar essa consulta. Portanto, para que 100 pedaços
de informações sejam recuperadas, se você precisar de 99% de performance, provavelmente
terá que enviar 100 solicitações. Este é um bom exemplo de quando o armazenamento em cache do contexto pode reduzir significativamente o custo associado ao uso de modelos do Gemini mantendo o alto desempenho.

## Perguntas frequentes

### Qual é o melhor lugar para colocar minha consulta na janela de contexto?

Na maioria dos casos, especialmente se o contexto total for longo, a performance do modelo será melhor se você colocar sua consulta / pergunta no final do comando (depois de todo o contexto).

### Perco a performance do modelo quando adiciono mais tokens a uma consulta?

Em geral, se você não precisar que os tokens sejam transmitidos ao modelo, é melhor evitar a transmissão. No entanto, se você tiver um grande bloco de tokens com algumas informações e quiser fazer perguntas sobre essas informações, o modelo será altamente capaz de extrair essas informações (até 99% de precisão em muitos casos).

### Como posso reduzir meu custo com consultas de contexto longo?

Se você tiver um conjunto semelhante de tokens / contexto que queira reutilizar muitas
vezes, [o armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) poderá ajudar a reduzir os custos
associados a perguntas sobre essas informações.

### O tamanho do contexto afeta a latência do modelo?

Há uma quantidade fixa de latência em qualquer solicitação, independentemente do tamanho, mas geralmente consultas mais longas têm maior latência (tempo para o primeiro token).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
