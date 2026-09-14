---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=pt-BR
fetched_at: 2026-09-14T05:47:28.079918+00:00
title: "O armazenamento em cache de contexto \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# O armazenamento em cache de contexto

Em um fluxo de trabalho de IA típico, você pode transmitir os mesmos tokens de entrada várias vezes para um modelo. A API Gemini oferece armazenamento em cache implícito para otimizar a performance e os custos.

## Armazenamento em cache implícito

O armazenamento em cache implícito é ativado por padrão para todos os modelos do Gemini 2.5 e mais recentes. Ele é
compatível com modos de conversa com [estado](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#multi-turn-conversations) (usando `previous_interaction_id`)
e sem [estado](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#stateless-conversations).
Transmitimos automaticamente a economia de custos se a solicitação atingir os caches. Não é necessário fazer nada para ativar esse recurso. A contagem mínima de tokens de entrada para o armazenamento em cache de contexto está listada na tabela a seguir para cada modelo:

| Modelo | Limite mínimo de tokens |
| --- | --- |
| Gemini 3.8 Flash | 4.096 |
| Gemini 3.7 Flash | 4.096 |
| Gemini 3.6 Flash | 4.096 |
| Gemini 3.5 Flash | 4.096 |
| Pré-lançamento do Gemini 3.1 Pro | 4.096 |
| Gemini 2.5 Flash | 2.048 |
| Gemini 2.5 Pro | 2.048 |

Para aumentar a chance de um acerto de cache implícito:

- Tente colocar conteúdos grandes e comuns no início do prompt.
- Tente enviar solicitações com prefixo semelhante em um curto período.

Você pode conferir o número de tokens que foram acertos de cache no campo `usage.total_cached_tokens` do objeto de resposta (Python e JavaScript).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-10 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-10 UTC."],[],[]]
