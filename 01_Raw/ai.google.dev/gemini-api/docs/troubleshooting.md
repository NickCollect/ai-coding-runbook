---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-BR
fetched_at: 2026-10-05T06:48:35.804243+00:00
title: "Guia de solu\u00e7\u00e3o de problemas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de solução de problemas

Use este guia para diagnosticar e resolver problemas comuns que surgem ao
chamar a API Gemini. Você pode encontrar problemas no serviço de back-end da API Gemini ou nos SDKs do cliente. Nossos SDKs de cliente são
de código aberto nos seguintes repositórios:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Se você tiver problemas com a chave de API, verifique se ela foi configurada corretamente de acordo com o [guia de configuração da chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br).

## Códigos de erro

Para uma referência completa de todos os códigos de erro, incluindo códigos de status HTTP, códigos de geração bloqueada e códigos de erro de conteúdo, consulte a página [Erros da API](https://ai.google.dev/gemini-api/docs/api-errors?hl=pt-br).

## Repetir estratégia

Se você receber um erro indicando que precisa tentar novamente a solicitação (como `429 RESOURCE_EXHAUSTED` ou `503 UNAVAILABLE`), recomendamos implementar uma estratégia de espera exponencial. Isso significa que você espera um pouco antes da primeira nova tentativa e aumenta gradualmente o tempo de espera entre as tentativas subsequentes.

Os SDKs de cliente oficiais da API Gemini, como o [SDK do Python](https://github.com/googleapis/python-genai), incluem por padrão uma lógica de nova tentativa automática com espera exponencial para lidar com erros temporários, como tempos limite, problemas de rede e limites de taxa (códigos de status `429` e `5xx`). Por exemplo, o SDK para Python repete automaticamente erros transitórios até quatro vezes com um atraso inicial de aproximadamente 1 segundo e um atraso máximo de 60 segundos.

Se você estiver fazendo solicitações diretas da API REST ou personalizando sua lógica de novas tentativas, siga estas práticas recomendadas para aumentar a probabilidade de uma solicitação bem-sucedida e evitar sobrecarregar o serviço:

- **Use a espera exponencial**:aguarde um pouco antes da primeira nova tentativa (por exemplo, 1 segundo) e aumente o atraso exponencialmente (por exemplo, 2s, 4s, 8s).
- **Adicione instabilidade**:adicione uma instabilidade aleatória ao atraso para evitar que todos os clientes tentem novamente exatamente ao mesmo tempo.
- **Repetir em erros específicos**:repita apenas em erros transitórios (como `429`, `408` ou `5xx`). Não repita em erros do cliente (como `400`, `402` ou `403`), porque eles indicam problemas como chaves de API inválidas, créditos de pré-pagamento esgotados ou sintaxe incorreta.
- **Defina o número máximo de novas tentativas**:defina um número máximo de tentativas para evitar loops infinitos.

## Verificar se há erros de parâmetro do modelo nas chamadas de API

Verifique se os parâmetros do modelo estão dentro dos seguintes valores:

|  |  |
| --- | --- |
| **Parâmetro do modelo** | **Valores (intervalo)** |
| Contagem de candidatos | 1 a 8 (número inteiro) |
| Temperatura | 0.0-1.0 |
| Máximo de tokens de saída | Use a [página "Modelos"](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br) para determinar o número máximo de tokens do modelo que você está usando. |
| TopP | 0.0-1.0 |

Além de verificar os valores dos parâmetros, confira se você está usando a [versão da API](https://ai.google.dev/gemini-api/docs/api-versions?hl=pt-br) correta (por exemplo, `/v1` ou `/v1beta`) e o modelo que oferece suporte aos recursos necessários. Por exemplo, se um recurso estiver na versão Beta, ele só vai estar disponível na versão `/v1beta` da API.

## Verificar se você tem o modelo certo

Verifique se você está usando um modelo compatível listado na nossa [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br).

## Maior latência ou uso de tokens com modelos de raciocínio

A latência ou o uso de tokens mais altos geralmente ocorrem porque os modelos do Gemini 3.x têm
o recurso de pensamento ativado por padrão. Os modelos Gemini 2.5 descontinuados também usam o raciocínio padrão.

Os modelos de pensamento geram tokens de raciocínio interno para melhorar a qualidade. Esse processo de raciocínio aumenta a latência da resposta e o consumo total de tokens.

Se você prioriza uma latência menor ou precisa minimizar os custos, pode diminuir o nível de pensamento ou desativar o recurso.

Para detalhes de configuração e exemplos de código, consulte o
[guia de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#thinking-levels).

## Problemas de segurança

Se uma solicitação for bloqueada devido a uma configuração de segurança na chamada de API,
analise a solicitação em relação aos filtros definidos na chamada de API.

Se você vir `BlockedReason.OTHER`, a consulta ou resposta pode violar os [termos de serviço](https://ai.google.dev/terms?hl=pt-br) ou não ser compatível.

## Problema de recitação

Se o modelo parar de gerar saída devido ao motivo RECITATION, isso significa que a saída do modelo pode se assemelhar a determinados dados. Para corrigir isso, tente tornar o
comando / contexto o mais exclusivo possível e use uma temperatura mais alta.

## Problema com tokens repetitivos

Se você notar tokens de saída repetidos, siga estas sugestões para reduzir ou eliminar esse problema.

| Descrição | Causa | Solução alternativa sugerida |
| --- | --- | --- |
| Hífenes repetidos em tabelas Markdown | Isso pode acontecer quando o conteúdo da tabela é longo, já que o modelo tenta criar uma tabela Markdown visualmente alinhada. No entanto, o alinhamento em Markdown não é necessário para a renderização correta. | Adicione instruções ao comando para dar ao modelo diretrizes específicas para gerar tabelas em Markdown. Forneça exemplos que sigam essas diretrizes. Você também pode tentar ajustar a temperatura. Para gerar código ou resultados muito estruturados, como tabelas Markdown, uma temperatura alta funciona melhor (>= 0,8).  Confira um exemplo de diretrizes que você pode adicionar ao seu comando para evitar esse problema:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Tokens repetidos em tabelas Markdown | Assim como os hífens repetidos, isso acontece quando o modelo tenta alinhar visualmente o conteúdo da tabela. O alinhamento em Markdown não é necessário para a renderização correta. | - Tente adicionar instruções como as seguintes ao seu comando do sistema:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Tente ajustar a temperatura. Temperaturas mais altas (>= 0,8) geralmente ajudam a eliminar repetições ou duplicações na saída. |
| Quebras de linha repetidas (`\n`) na saída estruturada | Quando a entrada do modelo contém Unicode ou sequências de escape como `\u` ou `\t`, isso pode resultar em novas linhas repetidas. | - Verifique e substitua as sequências de escape proibidas por caracteres UTF-8   no seu comando. Por exemplo, a sequência de escape `\u` nos exemplos de JSON pode fazer com que o modelo também a use na saída. - Instrua o modelo sobre as opções de escape permitidas. Adicione uma instrução do sistema como esta:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Texto repetido usando saída estruturada | Quando a saída do modelo tem uma ordem diferente para os campos do esquema estruturado definido, isso pode levar à repetição de texto. | - Não especifique a ordem dos campos no comando. - Tornar todos os campos de saída obrigatórios. |
| Chamadas de ferramentas repetitivas | Isso pode acontecer se o modelo perder o contexto de ideias anteriores e/ou chamar um endpoint indisponível a que ele é forçado. | Instrua o modelo a manter o estado no processo de pensamento. Adicione isso ao final das instruções do sistema:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Texto repetitivo que não faz parte da saída estruturada | Isso pode acontecer se o modelo ficar preso em uma solicitação que não consegue resolver. | - Se o pensamento estiver ativado, evite dar ordens explícitas sobre como   pensar em um problema nas instruções. Basta pedir o resultado final. - Tente uma temperatura mais alta >= 0,8. - Adicione instruções como "Seja conciso", "Não se repita" ou "Dê a resposta uma vez". |

## Chaves de API bloqueadas ou que não funcionam

Esta seção descreve como verificar se sua chave de API Gemini está bloqueada e o que fazer nesse caso.

### Entenda por que as chaves são bloqueadas

Identificamos uma vulnerabilidade em que algumas chaves de API podem ter sido expostas publicamente. Para proteger seus dados e evitar o acesso não autorizado, bloqueamos proativamente essas chaves vazadas conhecidas para que não possam acessar a API Gemini.

### Confirmar se as chaves foram afetadas

Se você souber que sua chave foi vazada, não poderá mais usá-la com a
API Gemini. Use o [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br) para verificar se alguma das suas chaves de API está bloqueada para chamar a API Gemini e gerar novas chaves. O seguinte erro também pode ser retornado ao tentar usar essas chaves:

```
Your API key was reported as leaked. Please use another API key.
```

### Ação para chaves de API bloqueadas

Gere novas chaves de API para suas integrações da API Gemini usando o [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br). Recomendamos revisar suas práticas de gerenciamento de chaves de API para garantir que as novas chaves sejam mantidas em segurança e não sejam expostas publicamente.

### Cobranças inesperadas devido a vulnerabilidade

[Envie um caso de suporte de faturamento](https://console.cloud.google.com/support/chat?hl=pt-br).
Nossa equipe de faturamento está trabalhando nisso e vamos comunicar as atualizações assim que
possível.

### Medidas de segurança do Google para chaves vazadas

**Como o Google vai ajudar a proteger minha conta contra estouro de custos e abuso se minhas chaves de API forem vazadas?**

- Estamos caminhando para emitir chaves de API quando você solicita uma nova chave usando o
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br), que por padrão será
  limitado apenas ao Google AI Studio e não aceitará chaves de outros serviços.
  Isso ajuda a evitar o uso não intencional de teclas cruzadas.
- Por padrão, bloqueamos as chaves de API que são vazadas e usadas com a
  API Gemini, ajudando a evitar o abuso de custos e dos dados do seu aplicativo.
- Você poderá encontrar o status das suas chaves de API no [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br). Além disso, vamos comunicar
  de forma proativa quando identificarmos que suas chaves de API foram vazadas para que você tome medidas imediatas.

## Melhorar a saída do modelo

Para saídas de modelo de maior qualidade, tente escrever comandos mais estruturados. A página do [guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br) apresenta alguns conceitos básicos, estratégias e práticas recomendadas para você começar.

## Entender os limites de token

Leia nosso [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) para entender melhor como contar tokens e quais são os limites deles.

## Problemas conhecidos

- A API é compatível apenas com alguns idiomas. Enviar comandos em idiomas não aceitos pode gerar respostas inesperadas ou até mesmo bloqueadas. Confira os [idiomas disponíveis](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#supported-languages) para atualizações.

## Informar um bug

Participe da discussão no
[fórum de desenvolvedores da IA do Google](https://discuss.ai.google.dev?hl=pt-br)
se tiver dúvidas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-01 UTC."],[],[]]
