---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-BR
fetched_at: 2026-06-08T05:38:52.316448+00:00
title: "Guia de solu\u00e7\u00e3o de problemas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de solução de problemas

Use este guia para diagnosticar e resolver problemas comuns que surgem ao chamar a API Gemini. Você pode encontrar problemas no serviço de back-end da API Gemini ou nos SDKs do cliente. Nossos SDKs do cliente são de código aberto nos seguintes repositórios:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Se você tiver problemas com a chave de API, verifique se ela foi configurada
corretamente de acordo com o [guia de configuração da chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br).

## Códigos de erro do serviço de back-end da API Gemini

A tabela a seguir lista códigos de erro comuns de back-end que podem ocorrer, além de explicações sobre as causas e etapas de solução de problemas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Código HTTP** | **Status** | **Descrição** | **Exemplo** | **Solução** |
| 400 | INVALID\_ARGUMENT | O corpo da solicitação está malformado. | Há um erro de digitação ou um campo obrigatório ausente na sua solicitação. | Consulte a [referência da API](https://ai.google.dev/api?hl=pt-br) para ver o formato da solicitação, exemplos e versões compatíveis. O uso de recursos de uma versão mais recente da API com um endpoint mais antigo pode causar erros. |
| 400 | FAILED\_PRECONDITION | O nível sem custo financeiro da API Gemini não está disponível no seu país. Ative o faturamento no seu projeto no Google AI Studio. | Você está fazendo uma solicitação em uma região em que o nível sem custo financeiro não é compatível e não ativou o faturamento no seu projeto no Google AI Studio. | Para usar a API Gemini, você precisa configurar um plano pago usando [Google AI Studio](https://aistudio.google.com/app/apikey?hl=pt-br). |
| 403 | PERMISSION\_DENIED | Sua chave de API não tem as permissões necessárias. | Você está usando a chave de API errada ou você está tentando usar um modelo ajustado sem passar pela [autenticação adequada](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pt-br). | Verifique se a chave de API está definida e tem o acesso correto. E faça a autenticação adequada para usar modelos ajustados. |
| 404 | NOT\_FOUND | O recurso solicitado não foi encontrado. | Um arquivo de imagem, áudio ou vídeo referenciado na sua solicitação não foi encontrado. | Verifique se todos os [parâmetros na sua solicitação são válidos](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-br#check-api) para a versão da API. |
| 429 | RESOURCE\_EXHAUSTED | Você excedeu o limite de taxa. | Você está enviando muitas solicitações por minuto com a API Gemini de nível sem custo financeiro. | Verifique se você está dentro do [limite de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br) do modelo. [Solicite um aumento de cota](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br#request-rate-limit-increase), se necessário. |
| 499 | CANCELADO | A operação foi cancelada, geralmente pelo autor da chamada. | O cliente fechou a conexão antes que a API pudesse terminar de responder. | Verifique se o cliente ou a infraestrutura de rede está fechando a conexão prematuramente (por exemplo, devido a um tempo limite do lado do cliente). |
| 500 | INTERNAL | Ocorreu um erro inesperado do lado do Google. | O contexto de entrada é muito longo. | Confira a [página de status da API Gemini](https://aistudio.google.com/status?hl=pt-br) para ver se há incidentes em andamento. Reduza o contexto de entrada ou mude temporariamente para outro modelo (por exemplo, do Gemini 2.5 Pro para o Gemini 2.5 Flash) e veja se funciona. Ou aguarde um pouco e tente novamente. Se o problema persistir após a nova tentativa, informe-o usando o botão **Enviar feedback** no Google AI Studio. |
| 503 | INDISPONÍVEL | O serviço pode estar temporariamente sobrecarregado ou inativo. | O serviço está temporariamente sem capacidade. | Confira a [página de status da API Gemini](https://aistudio.google.com/status?hl=pt-br) para ver se há incidentes em andamento. Mude temporariamente para outro modelo (por exemplo, do Gemini 2.5 Pro para o Gemini 2.5 Flash) e veja se funciona. Ou aguarde um pouco e tente novamente. Se o problema persistir após a nova tentativa, informe-o usando o botão **Enviar feedback** no Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | O serviço não consegue concluir o processamento dentro do prazo. | Seu comando (ou contexto) é muito grande para ser processado a tempo. | Defina um "tempo limite" maior na solicitação do cliente para evitar esse erro. |

## Verificar erros de parâmetro do modelo nas chamadas de API

Verifique se os parâmetros do modelo estão dentro dos seguintes valores:

|  |  |
| --- | --- |
| **Parâmetro do modelo** | **Valores (intervalo)** |
| Contagem de candidatos | 1 a 8 (inteiro) |
| Temperatura | 0,0 a 1,0 |
| Máximo de tokens de saída | Use a [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br) para determinar o número máximo de tokens do modelo que você está usando. |
| TopP | 0,0 a 1,0 |

Além de verificar os valores dos parâmetros, confira se você está usando a
[versão correta da API](https://ai.google.dev/gemini-api/docs/api-versions?hl=pt-br) (por exemplo, `/v1` ou `/v1beta`) e o
modelo que oferece suporte aos recursos necessários. Por exemplo, se um recurso estiver na versão Beta, ele só estará disponível na versão `/v1beta` da API.

## Verificar se você tem o modelo certo

Verifique se você está usando um modelo compatível listado na nossa [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br).

## Maior latência ou uso de tokens com modelos 2.5

Se você estiver observando maior latência ou uso de tokens com os modelos 2.5 Flash e Pro, isso pode acontecer porque eles vêm com o **pensamento ativado por padrão** para melhorar a qualidade. Se você estiver priorizando a velocidade ou precisar minimizar os custos, ajuste ou desative o pensamento.

Consulte a [página de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#set-budget) para
orientações e exemplos de código.

## Problemas de segurança

Se você vir um comando bloqueado devido a uma configuração de segurança na chamada de API, revise o comando em relação aos filtros definidos na chamada de API.

Se você vir `BlockedReason.OTHER`, a consulta ou resposta poderá violar os [termos
de serviço](https://ai.google.dev/terms?hl=pt-br) ou não ter suporte.

## Problema de recitação

Se o modelo parar de gerar saída devido ao motivo RECITATION, isso significa que a saída do modelo pode se assemelhar a determinados dados. Para corrigir isso, tente tornar o comando / contexto o mais exclusivo possível e use uma temperatura mais alta.

## Problema de tokens repetitivos

Se você vir tokens de saída repetidos, tente as sugestões a seguir para ajudar a reduzir ou eliminar esses tokens.

| Descrição | Causa | Alternativa |
| --- | --- | --- |
| Hífens repetidos em tabelas Markdown | Isso pode ocorrer quando o conteúdo da tabela é longo, já que o modelo tenta criar uma tabela Markdown alinhada visualmente. No entanto, o alinhamento no Markdown não é necessário para a renderização correta. | Adicione instruções ao comando para dar ao modelo diretrizes específicas para gerar tabelas Markdown. Forneça exemplos que sigam essas diretrizes. Você também pode tentar ajustar a temperatura. Para gerar código ou saída muito estruturada, como tabelas Markdown, a temperatura alta funciona melhor (>= 0,8).  Confira a seguir um exemplo de diretrizes que você pode adicionar ao comando para evitar esse problema:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Tokens repetidos em tabelas Markdown | Semelhante aos hífens repetidos, isso ocorre quando o modelo tenta alinhar visualmente o conteúdo da tabela. O alinhamento no Markdown não é necessário para a renderização correta. | - Tente adicionar instruções como as seguintes ao comando do sistema:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Tente ajustar a temperatura. Temperaturas mais altas (>= 0,8)   geralmente ajudam a eliminar repetições ou duplicações na   saída. |
| Quebras de linha repetidas (`\n`) na saída estruturada | Quando a entrada do modelo contém sequências de caracteres Unicode ou de escape, como `\u` ou `\t`, isso pode levar a quebras de linha repetidas. | - Verifique e substitua sequências de escape proibidas por caracteres UTF-8   no comando. Por exemplo, a sequência de escape `\u`   nos exemplos JSON pode fazer com que o modelo também as use   na saída. - Instrua o modelo sobre escapes permitidos. Adicione uma instrução do sistema como   esta:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Texto repetido ao usar saída estruturada | Quando a saída do modelo tem uma ordem diferente para os campos do esquema estruturado definido, isso pode levar à repetição de texto. | - Não especifique a ordem dos campos no comando. - Torne todos os campos de saída obrigatórios. |
| Chamada de ferramenta repetitiva | Isso pode ocorrer se o modelo perder o contexto de pensamentos anteriores e/ou chamar um endpoint indisponível ao qual ele é forçado. | Instrua o modelo a manter o estado no processo de pensamento. Adicione isso ao final das instruções do sistema:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Texto repetitivo que não faz parte da saída estruturada | Isso pode ocorrer se o modelo ficar preso em uma solicitação que não pode resolver. | - Se o pensamento estiver ativado, evite dar ordens explícitas sobre como   pensar em um problema nas instruções. Basta pedir a saída final. - Tente uma temperatura mais alta >= 0,8. - Adicione instruções como "Seja conciso", "Não se repita" ou   "Forneça a resposta uma vez". |

## Chaves de API bloqueadas ou que não funcionam

Esta seção descreve como verificar se a chave da API Gemini está bloqueada e o que fazer a respeito.

### Entender por que as chaves são bloqueadas

Identificamos uma vulnerabilidade em que algumas chaves de API podem ter sido expostas publicamente. Para proteger seus dados e evitar acesso não autorizado, bloqueamos proativamente essas chaves vazadas conhecidas para impedir o acesso à API Gemini.

### Confirmar se as chaves foram afetadas

Se a chave for conhecida como vazada, não será mais possível usá-la com a API Gemini. Você pode usar [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pt-br) para verificar se alguma das
suas chaves de API está bloqueada para chamar a API Gemini e gerar novas
chaves. O seguinte erro também pode ser retornado ao tentar usar essas chaves:

```
Your API key was reported as leaked. Please use another API key.
```

### Ação para chaves de API bloqueadas

Gere novas chaves de API para suas integrações da API Gemini usando [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pt-br). Recomendamos revisar suas práticas de gerenciamento de chaves de API para garantir que as novas chaves sejam mantidas em segurança e não sejam expostas publicamente.

### Cobranças inesperadas devido à vulnerabilidade

[Envie um caso de suporte de faturamento](https://console.cloud.google.com/support/chat?hl=pt-br).
Nossa equipe de faturamento está trabalhando nisso e vamos comunicar as atualizações assim que possível.

### Medidas de segurança do Google para chaves vazadas

**Como o Google vai ajudar a proteger minha conta contra estouro de custos e abusos se minhas chaves de API forem vazadas?**

- Estamos avançando para emitir chaves de API quando você solicitar uma nova chave usando
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pt-br) que, por padrão, será
  limitada apenas ao Google AI Studio e não aceitará chaves de outros serviços.
  Isso ajudará a evitar o uso não intencional de chaves cruzadas.
- Estamos bloqueando por padrão as chaves de API vazadas e usadas com a API Gemini, ajudando a evitar abusos de custo e dados do aplicativo.
- Você poderá encontrar o status das suas chaves de API no [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pt-br), e vamos trabalhar para comunicar
  proativamente quando identificarmos que suas chaves de API foram vazadas para ação imediata.

## Melhorar a saída do modelo

Para saídas de modelo de maior qualidade, tente escrever comandos mais estruturados. A
[página do guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br)
apresenta alguns conceitos básicos, estratégias e práticas recomendadas para você
começar.

## Entender os limites de tokens

Leia nosso [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) para entender melhor como
contar tokens e os limites deles.

## Problemas conhecidos

- A API oferece suporte apenas a alguns idiomas selecionados. O envio de comandos em idiomas não compatíveis pode produzir respostas inesperadas ou até mesmo bloqueadas. Consulte
  [os idiomas disponíveis](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#supported-languages) para
  atualizações.

## Informar um bug

Participe da discussão no
[fórum de desenvolvedores da IA do Google](https://discuss.ai.google.dev?hl=pt-br)
se tiver dúvidas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
