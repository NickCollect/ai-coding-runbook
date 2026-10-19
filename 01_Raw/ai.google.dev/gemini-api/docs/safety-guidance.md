---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-BR
fetched_at: 2026-10-19T05:43:10.606583+00:00
title: "Orienta\u00e7\u00f5es sobre seguran\u00e7a e veracidade \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Orientações sobre segurança e veracidade

Os modelos de inteligência artificial generativa são ferramentas poderosas, mas têm limitações. A versatilidade e a aplicabilidade delas podem levar a resultados inesperados, como respostas imprecisas, tendenciosas ou ofensivas. O pós-processamento e a avaliação manual rigorosa são essenciais para limitar o risco de danos causados por essas respostas.

Os modelos fornecidos pela API Gemini podem ser usados em uma ampla variedade de aplicativos de IA generativa e processamento de linguagem natural (PLN). O uso dessas funções só está disponível na API Gemini ou no web app Google AI Studio. O uso da API Gemini também está sujeito à [Política de uso proibido da IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br) e aos [Termos de Serviço da API Gemini](https://ai.google.dev/terms?hl=pt-br).

Parte do que torna os modelos de linguagem grandes (LLMs) tão úteis é que eles são ferramentas criativas que podem lidar com muitas tarefas de linguagem diferentes. No entanto, isso também significa que os LLMs podem gerar resultados inesperados, incluindo texto ofensivo, insensível ou incorreto. Além disso, a incrível versatilidade desses modelos também dificulta a previsão exata de quais tipos de resultados indesejáveis eles podem produzir. Embora a API Gemini tenha sido projetada com os [princípios de IA do Google](https://ai.google/principles/?hl=pt-br) em mente, a responsabilidade de aplicar esses modelos é dos desenvolvedores. Para ajudar os desenvolvedores a criar aplicativos seguros e responsáveis, a API Gemini tem uma filtragem de conteúdo integrada e configurações de segurança ajustáveis em quatro dimensões de danos. Consulte o guia de [configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br) para saber mais. Ela também oferece o recurso de embasamento com a Pesquisa Google ativada para melhorar a veracidade, mas isso pode ser desativado para desenvolvedores cujos casos de uso são mais criativos e não buscam informações.

Este documento apresenta alguns riscos de segurança que podem surgir ao usar LLMs e recomendações emergentes de design e desenvolvimento de segurança. As leis e regulamentações também podem impor restrições, mas essas considerações estão fora do escopo deste guia.

As etapas a seguir são recomendadas ao criar aplicativos com LLMs:

- Entender os riscos de segurança do seu aplicativo
- Considerando ajustes para evitar riscos de segurança
- Realizar testes de segurança de acordo com seu caso de uso
- Pedir feedback dos usuários e monitorar o uso

As fases de ajuste e teste devem ser iterativas até que você alcance
o desempenho adequado para seu aplicativo.

![Ciclo de implementação do modelo](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=pt-br)

## Entenda os riscos de segurança do seu aplicativo

Nesse contexto, a segurança é definida como a capacidade de um LLM evitar causar danos aos usuários, por exemplo, gerando linguagem ou conteúdo tóxico que promova estereótipos. Os modelos disponíveis na API Gemini foram projetados com os [princípios de IA do Google](https://ai.google/principles/?hl=pt-br) em mente, e seu uso está sujeito à [Política de uso proibido de IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br). A API oferece filtros de segurança integrados para ajudar a resolver alguns problemas comuns de modelos de linguagem, como linguagem tóxica e discurso de ódio, além de buscar a inclusão e evitar estereótipos. No entanto, cada aplicativo pode apresentar um conjunto diferente de riscos aos usuários. Portanto, como proprietário do aplicativo, você é responsável por conhecer seus usuários e os possíveis danos que seu aplicativo pode causar, além de garantir que ele use LLMs de maneira segura e responsável.

Como parte dessa avaliação, considere a probabilidade de ocorrência de danos e determine a gravidade e as etapas de mitigação. Por exemplo, um app que gera redações com base em eventos reais precisa ter mais cuidado para evitar desinformação do que um app que gera histórias fictícias para entretenimento. Uma boa maneira de começar a analisar possíveis riscos à segurança é pesquisar seus usuários finais e outras pessoas que possam ser afetadas pelos resultados do seu aplicativo. Isso pode assumir muitas formas, incluindo pesquisar estudos de ponta no domínio do seu app, observar como as pessoas estão usando apps semelhantes ou realizar um estudo de usuário, uma pesquisa ou entrevistas informais com usuários em potencial.

### Dicas avançadas

- Converse com um grupo diversificado de usuários em potencial dentro da população-alvo sobre seu aplicativo e a finalidade dele para ter uma perspectiva mais ampla sobre possíveis riscos e ajustar os critérios de diversidade conforme necessário.
- O [Framework de gerenciamento de riscos de IA](https://www.nist.gov/itl/ai-risk-management-framework) (em inglês) lançado pelo Instituto Nacional de Padrões e Tecnologia (NIST, na sigla em inglês) do governo dos EUA oferece orientações mais detalhadas e recursos de aprendizado adicionais para o gerenciamento de riscos de IA.
- A publicação do DeepMind sobre os [riscos éticos e sociais de danos causados por modelos de linguagem](https://arxiv.org/abs/2112.04359) descreve em detalhes as maneiras como os aplicativos de modelos de linguagem podem causar danos.

## Faça ajustes para evitar riscos de segurança e veracidade.

Agora que você entende os riscos, pode decidir como mitigá-los. Determinar quais riscos priorizar e o que fazer para tentar evitá-los é uma decisão crítica, semelhante à triagem de bugs em um projeto de software. Depois de determinar as prioridades, comece a pensar nos tipos de mitigação mais adequados. Muitas vezes, mudanças simples podem fazer a diferença e reduzir os riscos.

Por exemplo, ao criar um aplicativo, considere:

- **Ajustar a saída do modelo** para refletir melhor o que é aceitável no contexto do seu aplicativo. O ajuste pode tornar a saída do modelo mais previsível e consistente e, portanto, ajudar a mitigar determinados riscos.
- **Fornecer um método de entrada que facilite saídas mais seguras**: a entrada exata que você dá a um LLM pode fazer a diferença na qualidade da saída. Vale a pena testar comandos de entrada para encontrar o que funciona com mais segurança no seu caso de uso, já que você pode fornecer uma UX que facilite isso. Por exemplo, é possível restringir os usuários a escolher apenas em uma lista suspensa de comandos de entrada ou oferecer sugestões pop-up com frases descritivas que você descobriu que funcionam com segurança no contexto do seu aplicativo.
- **Bloqueio de entradas não seguras e filtragem da saída antes de ela ser mostrada ao usuário**.Em situações simples, as listas de bloqueio podem ser usadas para identificar e bloquear palavras ou frases não seguras em comandos ou respostas, ou exigir que revisores humanos alterem ou bloqueiem manualmente esse conteúdo.
- **Usar classificadores treinados para rotular cada comando com possíveis danos ou sinais adversários.** Diferentes estratégias podem ser usadas para lidar com a solicitação com base no tipo de dano detectado. Por exemplo, se a entrada for muito nociva ou abusiva por natureza, ela poderá ser bloqueada e, em vez disso, gerar uma resposta com roteiro pré-estruturado.
  **Dica avançada**:se os indicadores determinarem que a saída é prejudicial, o aplicativo poderá usar as seguintes opções:

  - Fornecer uma mensagem de erro ou uma saída com roteiro pré-estruturado.
  - Tente de novo, caso uma saída alternativa segura seja gerada, já que às vezes o mesmo comando gera respostas diferentes.
- **Implementar salvaguardas contra uso indevido intencional**, como atribuir a cada usuário um ID exclusivo e impor um limite ao volume de consultas que podem ser enviadas em um determinado período. Outra salvaguarda é tentar proteger contra possível injeção de comando. A injeção de comando, assim como a injeção de SQL, é uma maneira de usuários mal-intencionados criarem um comando de entrada que manipula a saída do modelo. Por exemplo, enviando um comando de entrada que instrui o modelo a ignorar exemplos anteriores. Consulte a [política de uso proibido da IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br) para mais detalhes sobre uso indevido intencional.
- **Ajustar a funcionalidade para algo que seja inerentemente de menor risco**. Tarefas de escopo mais restrito (por exemplo, extrair palavras-chave de trechos de texto) ou que têm maior supervisão humana (por exemplo, gerar conteúdo curto que será revisado por um humano) geralmente representam um risco menor. Por exemplo, em vez de criar um aplicativo para escrever uma resposta de e-mail do zero, você pode limitar a expansão de um esboço ou sugerir frases alternativas.
- **Ajustar as configurações de segurança de conteúdo nocivo para diminuir a probabilidade de
  receber respostas que possam ser prejudiciais**.A API Gemini oferece configurações de segurança
  que podem ser ajustadas durante a fase de prototipagem para determinar se o
  aplicativo requer uma configuração de segurança mais ou menos restritiva. É possível
  ajustar essas configurações em cinco categorias de filtro para restringir ou permitir
  determinados tipos de conteúdo. Consulte o [guia de configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br) para saber mais sobre
  as configurações de segurança ajustáveis disponíveis na API Gemini.
- **Diminua possíveis imprecisões factuais ou alucinações ativando o embasamento com a Pesquisa Google**. Muitos modelos de IA são experimentais
  e podem apresentar informações factualmente imprecisas, alucinar ou
  produzir resultados problemáticos. O recurso de embasamento com a Pesquisa Google conecta o modelo do Gemini ao conteúdo da web em tempo real e funciona com todos os idiomas disponíveis. Isso permite que o Gemini forneça respostas mais precisas e cite fontes verificáveis além do limite de conhecimento dos modelos.

## Realize testes de segurança de acordo com seu caso de uso.

Os testes são uma parte fundamental da criação de aplicativos robustos e seguros, mas a extensão, o escopo e as estratégias variam. Por exemplo, um gerador de haicai por diversão provavelmente apresenta riscos menos graves do que um aplicativo projetado para uso por escritórios de advocacia para resumir documentos jurídicos e ajudar a redigir contratos. Mas
o gerador de haicai pode ser usado por uma variedade maior de usuários, o que significa que o
potencial de tentativas adversárias ou até mesmo entradas prejudiciais não intencionais pode ser
maior. O contexto da implementação também é importante. Por exemplo, um aplicativo com saídas revisadas por especialistas humanos antes de qualquer ação ser tomada pode ser considerado menos propenso a produzir resultados prejudiciais do que o aplicativo idêntico sem essa supervisão.

É comum passar por várias iterações de mudanças e testes antes de se sentir confiante para lançar, mesmo para aplicativos de risco relativamente baixo. Dois tipos de testes são particularmente úteis para aplicativos de IA:

- O **benchmarking de segurança** envolve a criação de métricas que refletem as maneiras como seu aplicativo pode ser inseguro no contexto de como ele provavelmente será usado. Em seguida, é feito um teste para verificar o desempenho do aplicativo nas métricas usando conjuntos de dados de avaliação. É recomendável pensar nos níveis mínimos aceitáveis de métricas de segurança antes do teste para que 1) você possa avaliar os resultados do teste em relação a essas expectativas e 2) possa coletar o conjunto de dados de avaliação com base nos testes que avaliam as métricas mais importantes para você.

  **Dicas avançadas:**

  - Não confie demais em abordagens prontas, porque é provável que você precise criar seus próprios conjuntos de dados de teste usando avaliadores humanos para se adequar totalmente ao contexto do seu aplicativo.
  - Se você tiver mais de uma métrica, será necessário decidir como fazer a compensação se uma mudança levar a melhorias em uma métrica em detrimento de outra. Assim como em outras engenharias de performance, talvez seja melhor focar no desempenho do pior caso no conjunto de avaliação em vez do desempenho médio.
- O **teste adversário** envolve tentar quebrar seu aplicativo de maneira proativa. O objetivo é identificar pontos fracos para que você possa tomar medidas para corrigi-los, conforme necessário. O teste adversarial pode exigir muito tempo/esforço dos avaliadores com experiência no seu aplicativo, mas quanto mais você faz, maior é a chance de identificar problemas, principalmente aqueles que ocorrem raramente ou apenas após execuções repetidas do aplicativo.

  - O teste adversário é um método para avaliar sistematicamente um modelo de ML com a intenção de aprender como ele se comporta quando são fornecidas entradas acidentalmente nocivas ou maliciosas:
    - Uma entrada pode ser maliciosa quando é claramente projetada para produzir uma saída que não é segura ou é nociva. Por exemplo, pedir a um modelo de geração de texto para gerar um discurso de ódio sobre uma religião específica.
    - Uma entrada é acidentalmente nociva quando pode ser inofensiva em si, mas produz uma saída nociva. Por exemplo, pedir a um modelo de geração de texto para descrever uma pessoa de uma etnia específica e receber uma saída racista.
  - O que distingue um teste adversário de uma avaliação padrão é a composição dos dados usados para o teste. Para testes adversários, selecione dados de teste que provavelmente vão gerar uma saída problemática do modelo. Isso significa testar o comportamento do modelo para todos os tipos de danos possíveis, incluindo exemplos raros ou incomuns e casos extremos relevantes para as políticas de segurança. Ela também precisa incluir diversidade nas diferentes dimensões de uma frase, como estrutura, significado e extensão. Consulte as [práticas de IA responsável do Google em relação à justiça](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=pt-br) para mais detalhes sobre o que considerar ao criar um conjunto de dados de teste.
    **Dicas avançadas:**
  - Use [testes automatizados](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=pt-br) em vez do método tradicional de recrutar pessoas em "equipes vermelhas" para tentar quebrar seu aplicativo. Nos testes automatizados, a "equipe vermelha" é outro modelo de linguagem que encontra textos de entrada que geram saídas prejudiciais do modelo testado.

## Monitorar problemas

Não importa o quanto você teste e reduza os riscos, nunca é possível garantir a perfeição. Por isso, planeje com antecedência como identificar e lidar com os problemas que surgirem.As abordagens comuns incluem configurar um canal monitorado para que os usuários compartilhem feedback (por exemplo, classificação de positivo/negativo) e realizar um estudo com usuários para solicitar feedback de forma proativa de um grupo diversificado de pessoas. Isso é especialmente valioso se os padrões de uso forem diferentes das expectativas.

### Dicas avançadas

- Quando os usuários enviam feedback sobre produtos de IA, isso pode melhorar muito a performance da IA e a experiência do usuário ao longo do tempo. Por exemplo, isso ajuda você a escolher exemplos melhores para o ajuste de comandos. O [capítulo "Feedback e controle"](https://pair.withgoogle.com/chapter/feedback-controls/) do [Guia de pessoas e IA do Google](https://pair.withgoogle.com/guidebook/chapters) destaca considerações importantes a serem levadas em conta ao projetar mecanismos de feedback.

## Próximas etapas

- Consulte o guia de [configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br) para saber mais sobre as configurações ajustáveis disponíveis na API Gemini.
- Consulte a [introdução à criação de comandos](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pt-br) para começar a escrever seus primeiros comandos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-05 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-05 UTC."],[],[]]
