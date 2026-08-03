---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=pt-BR
fetched_at: 2026-08-03T04:33:47.892398+00:00
title: "Usar ferramentas com a API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Usar ferramentas com a API Gemini

As ferramentas ampliam as capacidades dos modelos do Gemini, permitindo que eles ajam no mundo real, acessem informações em tempo real e realizem tarefas computacionais complexas. Os modelos podem usar ferramentas em interações padrão de solicitação-resposta e em
sessões de streaming em tempo real usando a [API Live](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br).

As ferramentas são recursos específicos (como a Pesquisa Google ou a execução de código) que um modelo pode usar para responder a consultas. A API Gemini oferece um conjunto de ferramentas integradas totalmente
gerenciadas, ou você pode definir ferramentas personalizadas usando [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br).

Para criar sistemas orientados a metas e com várias etapas, consulte a [visão geral
dos agentes](https://ai.google.dev/gemini-api/docs/agents?hl=pt-br).

## Ferramentas integradas disponíveis

| Ferramenta | Descrição | Casos de uso |
| --- | --- | --- |
| [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) | Respostas baseadas em eventos e fatos atuais da Web para reduzir alucinações. | Responder a perguntas sobre eventos recentes, verificar fatos com diversas fontes. |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) | Crie assistentes com reconhecimento de localização que podem encontrar lugares, receber rotas e fornecer um contexto local avançado. | Planejar itinerários de viagem com várias paradas, encontrar empresas locais com base nos critérios do usuário. |
| [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) | Permita que o modelo escreva e execute código Python para resolver problemas de matemática ou processar dados com precisão. | Resolver equações matemáticas complexas, processar e analisar dados de texto com precisão. |
| [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) | Direcione o modelo para ler e analisar conteúdo de páginas ou documentos da Web específicos. | Responder a perguntas com base em URLs ou documentos específicos, recuperar informações em diferentes páginas da Web. |
| [Uso do computador (prévia)](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br) | Permita que o Gemini visualize uma tela e gere ações para interagir com interfaces do navegador da Web (execução do lado do cliente). | Automatizar fluxos de trabalho repetitivos baseados na Web, testar interfaces de usuário de aplicativos da Web. |
| [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br) | Indexe e pesquise seus próprios documentos para ativar a geração aumentada de recuperação (RAG). | Pesquisar manuais técnicos, responder a perguntas sobre dados próprios. |

Consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#pricing_for_tools) para detalhes
sobre os custos associados a ferramentas específicas.

## Como funciona a execução de ferramentas

As ferramentas permitem que o modelo solicite ações durante uma conversa. O fluxo varia dependendo se a ferramenta é integrada (gerenciada pelo Google) ou personalizada (gerenciada por você).

### Fluxo de ferramentas integradas

Para ferramentas integradas (Pesquisa Google, Google Maps, contexto de URL, pesquisa de arquivos, execução de código), todo o processo acontece em uma chamada de API:

1. **Você** envia um comando: "Qual é a raiz quadrada do preço mais recente das ações da GOOG?"
2. O **Gemini** decide que precisa de ferramentas e as executa nos servidores do Google (por exemplo, pesquisa o preço das ações e executa o código Python para calcular a raiz quadrada).
3. O **Gemini** envia a resposta final com base nos resultados da ferramenta.

### Fluxo de ferramentas personalizadas (chamada de função)

Para ferramentas personalizadas e uso do computador, o aplicativo processa a execução:

1. **Você** envia um comando com declarações de funções (ferramentas).
2. O **Gemini** pode enviar um JSON estruturado para chamar uma função específica
   (por exemplo, `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   sempre com um `id` exclusivo.
3. **Você** executa a função no aplicativo ou ambiente.
4. **Você** envia os resultados da função, com o mesmo `id` da chamada de função, de volta ao Gemini.
5. O **Gemini** usa os resultados para gerar uma resposta final ou outra chamada de ferramenta.

Saiba mais no [guia de chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br).

### Como combinar o fluxo de ferramentas integradas e personalizadas

Para solicitações que combinam ferramentas integradas e personalizadas (chamadas de função), o
modelo usa [circulação de contexto de ferramenta](https://ai.google.dev/gemini-api/docs/toold-combination?hl=pt-br) para
coordenar a execução em diferentes ambientes:

1. **Você** envia um comando e declara as ferramentas integradas e as funções personalizadas que quer ativar, definindo uma flag para ativar o suporte à combinação.
2. O **Gemini** executa ferramentas integradas e cede ao usuário se alguma chamada de função do lado do cliente for gerada (o que é executado primeiro depende do comando e do que o modelo decide). Ele envia uma resposta com:
   - Confirmação da chamada de ferramenta
   - Resultados da resposta da ferramenta (isso pode acontecer após o JSON se o modelo gerar duas chamadas de função paralelas)
   - JSON estruturado para chamar sua função
   - Assinaturas de pensamento criptografadas para preservar o contexto
3. **Você** executa a função no aplicativo ou ambiente.
4. **Você** retorna todas as partes da resposta do Gemini, além dos resultados da chamada de função.
5. O **Gemini** gera a resposta final usando todo o contexto combinado.

Leia o [guia de combinação de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br) para saber
como ativar o suporte à combinação de ferramentas integradas e personalizadas e exemplos de
circulação de contexto.

## Respostas estruturadas x chamada de função

O Gemini oferece dois métodos para gerar respostas estruturadas. Use [Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) quando o modelo precisar realizar uma
etapa intermediária conectando-se às suas próprias ferramentas ou sistemas de dados. Use
[respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) quando precisar que
a resposta final do modelo siga um esquema específico, como para renderizar
uma interface personalizada.

## Respostas estruturadas com ferramentas

É possível combinar [respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) com
ferramentas integradas para garantir que as respostas do modelo baseadas em dados ou
cálculos externos ainda sigam um esquema rigoroso.

Consulte [Respostas estruturadas com ferramentas](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=pt-br#structured_outputs_with_tools)
para exemplos de código.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-31 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-31 UTC."],[],[]]
