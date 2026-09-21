---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=pt-BR
fetched_at: 2026-09-21T05:49:27.177771+00:00
title: "Reten\u00e7\u00e3o de dados zero na API Gemini Developer \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Retenção de dados zero na API Gemini Developer

Esta página descreve detalhes do que é comumente chamado de "retenção de dados zero"
na API Gemini Developer.

## Restrição de treinamento

Conforme descrito nos [Termos de Serviço da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br), quando você usa Serviços pagos, o Google não usa seus comandos (incluindo instruções do sistema associadas, conteúdo em cache e arquivos como imagens, vídeos ou documentos) nem respostas para melhorar nossos produtos. Os Serviços pagos são definidos [aqui](https://ai.google.dev/gemini-api/terms?hl=pt-br#paid-services).

## Retenção de dados do cliente e como alcançar a retenção zero de dados

Os dados dos clientes geralmente são retidos por períodos limitados nos seguintes cenários e condições. Para alcançar a retenção zero de dados, os clientes precisam tomar
ações específicas ou evitar recursos específicos em cada uma destas áreas:

- **Registro de comandos para monitoramento de abuso**: conforme descrito nos [Termos adicionais de serviço da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br), para Serviços Pagos, o Google registra comandos e respostas por um período limitado apenas para detectar violações da [Política de uso proibido](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br). Se sua
  carga de trabalho exigir retenção de dados zero garantida ou contratos de
  processamento de dados empresariais, use a Vertex AI. Para mais detalhes, consulte
  [Gemini Enterprise Agent Platform e retenção de dados zero](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=pt-br).
- **Embasamento com a Pesquisa Google**: conforme descrito nos [Termos de Serviço adicionais da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br#grounding-with-google-search), o Google armazena comandos, informações contextuais e resultados gerados por 30 dias para criar resultados embasados e sugestões de pesquisa.
  Essas informações armazenadas podem ser usadas para depuração e teste de sistemas
  que oferecem suporte ao embasamento. **Não é possível desativar o armazenamento dessas informações se você usa o Embasamento com a Pesquisa Google.**
- **Embasamento com o Google Maps**: conforme descrito nos [Termos de Serviço adicionais da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br), o Google armazena comandos, informações contextuais e resultados gerados por 30 dias para criar resultados embasados. Essas informações armazenadas só podem ser usadas para engenharia de confiabilidade, como depuração em caso de problemas no serviço.
  **Não é possível desativar o armazenamento dessas informações se você usa o embasamento com o Google Maps.**
- **API Interactions**: gerencia o estado ativo de uma conversa para permitir turnos multiturno. **Por padrão, a API Interactions
  ativa o armazenamento de estado**. Para garantir uma pegada de dados zero, defina explicitamente o parâmetro `store` como `false` nas solicitações de API para desativar a retenção de estado padrão.
- **API Live**: essa API com estado permite a reconexão em tempo real armazenando o estado da conversa. Para alcançar retenção de dados zero, **não configure
  SessionResumptionConfig**. Se um identificador de sessão for gerado, o estado da conversa (incluindo texto, áudio e vídeo) será retido por até 24 horas.
- **Armazenamento da API File**: a API File permite que os usuários façam upload de recursos grandes.
  Os arquivos são armazenados em repouso até serem excluídos pelo usuário ou expirarem.
  O uso da API File é independente do registro do ZDR. Os usuários precisam excluir arquivos manualmente para garantir uma pegada de dados zero.
- **Cache de contexto explícito**: os usuários podem armazenar em cache manualmente conjuntos de dados grandes (por exemplo,
  vídeos longos ou bibliotecas de documentos) usando o campo `cached_content`. Embora os registros dessas solicitações sigam as políticas de descarte de ZDR, o contexto armazenado em cache é armazenado com um `ttl` ou `expire_time` definido pelo usuário. Para alcançar uma pegada de dados zero absoluta, não use o recurso cached\_content.
- **Armazenamento em cache implícito na memória**: por padrão, os modelos do Gemini armazenam dados em cache na memória para reduzir a latência e o custo para os desenvolvedores. Esses dados ficam estritamente na RAM (não em repouso), são isolados no nível do projeto e têm um TTL de 24 horas.
  **Isso não viola a retenção de dados zero.**

## A seguir

- Saiba mais sobre a [Política de uso proibido da IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=pt-br).
- Leia os [Termos adicionais de serviço da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br).
- Se você precisar de controles de ZDR de nível empresarial e autoatendimento, consulte o [guia de retenção de dados zero da Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-16 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-16 UTC."],[],[]]
