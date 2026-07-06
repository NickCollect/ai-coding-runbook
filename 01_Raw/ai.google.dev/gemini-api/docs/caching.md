---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=pt-BR
fetched_at: 2026-07-06T05:21:33.650313+00:00
title: "O armazenamento em cache de contexto \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# O armazenamento em cache de contexto

Em um fluxo de trabalho de IA típico, é possível transmitir os mesmos tokens de entrada várias vezes para um modelo. A API Gemini oferece armazenamento em cache implícito para otimizar a performance e os custos.

## Armazenamento em cache implícito

O armazenamento em cache implícito é ativado por padrão para todos os modelos do Gemini 2.5 e mais recentes. Transferimos automaticamente a economia de custos se sua solicitação atingir os caches. Não é necessário fazer nada
para ativar esse recurso. A contagem mínima de tokens de entrada para o cache de contexto está listada na tabela a seguir para cada modelo:

| Modelo | Limite mínimo de tokens |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Pré-lançamento do Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Para aumentar a chance de uma ocorrência implícita em cache:

- Tente colocar conteúdos grandes e comuns no início do comando
- Tente enviar solicitações com prefixos semelhantes em um curto período

É possível conferir o número de tokens que foram acertos de cache no campo `usage_metadata` (Python) ou `usageMetadata` (JavaScript) do objeto de resposta.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-22 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-22 UTC."],[],[]]
