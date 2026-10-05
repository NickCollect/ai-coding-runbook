---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=pt-BR
fetched_at: 2026-10-05T06:39:34.072004+00:00
title: "Erros da API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Erros da API

Esta página fornece uma referência para todos os códigos de erro da API Interactions, descreve o formato da resposta de erro e explica como a API entrega erros para diferentes tipos de solicitação.

## Códigos de erro da API padrão

Esses códigos de erro gerais no nível da solicitação correspondem aos códigos de status HTTP padrão.
Use o campo `code` na lógica do aplicativo para processar erros de maneira programática.

| Código | Status do HTTP | Descrição | Ação recomendada |
| --- | --- | --- | --- |
| `invalid_request` | 400 Solicitação inválida | O payload da solicitação está incorreto ou contém parâmetros inválidos. | Verifique a sintaxe e os parâmetros da solicitação na [referência da API](https://ai.google.dev/api/interactions-api?hl=pt-br). |
| `failed_precondition` | 400 Solicitação inválida | Não é possível processar a solicitação porque um pré-requisito não foi atendido (por exemplo, faturamento desativado). | Verifique o status de faturamento do projeto ou os pré-requisitos da conta. |
| `out_of_range` | 416 Intervalo solicitado não satisfatório | O parâmetro da solicitação está fora do intervalo válido. | Verifique os valores e limites de parâmetros. |
| `parameter_unknown` | 400 Solicitação inválida | A solicitação contém um parâmetro desconhecido. | Remova o parâmetro não reconhecido e tente de novo. |
| `authentication` | 401 Não autorizado | A chave de API está ausente, é inválida ou expirou. | Verifique sua [chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br). |
| `payment_required` | 402 Pagamento necessário | Seu saldo de crédito pré-pago acabou. | [Adicione créditos](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#buy-credits) à sua conta de faturamento ou ative a [recarga automática](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#auto-reload). Não tente de novo: a solicitação não será concluída até que os créditos sejam adicionados. |
| `permission_denied` | 403 Proibido | Sua chave de API não tem permissão para esse recurso. | Verifique as permissões da chave de API e o acesso ao projeto. |
| `not_found` | 404 Não encontrado | O recurso solicitado não foi encontrado. | Verifique o caminho e os parâmetros do recurso. |
| `model_not_found` | 404 Não encontrado | O modelo especificado não foi encontrado. | Verifique o nome do modelo ou use outro. |
| `already_exists` | 409 Conflito | A entidade que você tentou criar já existe. | Verifique se o recurso já existe antes de recriar. |
| `aborted` | 409 Conflito | A operação foi cancelada devido a um conflito ou falha na verificação de simultaneidade. | Tente fazer a solicitação novamente em um nível de aplicativo mais alto. |
| `rate_limit_exceeded` | 429 número excessivo de solicitações | Você excedeu o limite de solicitações ou tokens por minuto ou por segundo. | Aguarde e tente de novo com uma espera exponencial. |
| `quota_exceeded` | 429 número excessivo de solicitações | Você excedeu sua cota diária. | Aguarde até que a cota seja redefinida ou peça um aumento. |
| `too_many_requests` | 429 número excessivo de solicitações | Você fez muitas solicitações em pouco tempo. | Aguarde e tente de novo com uma espera exponencial. |
| `cancelled` | 499 Solicitação fechada pelo cliente | O cliente cancelou a solicitação antes da conclusão. | Nenhuma ação é necessária. Isso geralmente significa que o cliente se desconectou. |
| `api_error` | 500 Internal Server Error | Ocorreu um erro inesperado no servidor. | Tente fazer a solicitação novamente. Se o problema persistir, entre em contato com o suporte. |
| `unimplemented` | 501 Não implementado | A operação ou o recurso não foi implementado ou não é compatível. | Verifique os recursos da API ou mude para um recurso compatível. |
| `service_unavailable` | 503 Serviço indisponível | O serviço está temporariamente sobrecarregado ou fora do ar. | Aguarde e tente de novo com uma espera exponencial. |
| `deadline_exceeded` | 504 Gateway Timeout | A solicitação não foi concluída dentro do prazo. | Remova ou aumente a configuração de prazo do cliente para usar o padrão do servidor. |

## Códigos de geração bloqueados

Esses códigos de erro indicam que restrições de política, segurança ou conteúdo bloquearam a saída do modelo. Quando você receber um desses códigos, modifique a entrada e tente de novo.

| Código | Descrição |
| --- | --- |
| `safety` | Violações de segurança (conteúdo prejudicial) bloquearam a solicitação. |
| `recitation` | Restrições de direitos autorais ou recitação bloquearam a solicitação. |
| `language` | Um idioma sem suporte bloqueou a solicitação. |
| `prohibited_content` | As diretrizes de conteúdo proibido bloquearam a solicitação. |
| `spii` | As restrições de informações sensíveis de identificação pessoal bloquearam a solicitação. |
| `blocklist` | Termos proibidos em uma lista de bloqueio impediram a solicitação. |
| `image_safety` | Violações de segurança bloquearam a geração de imagens. |
| `image_prohibited_content` | As diretrizes de conteúdo proibido bloquearam a geração de imagens. |
| `image_recitation` | As restrições de direitos autorais ou recitação bloquearam a geração de imagens. |
| `image_other` | Motivos não especificados bloquearam a geração de imagens. |
| `content_blocked` | Um motivo não especificado da política bloqueou a solicitação. |

## Códigos de erro de geração

Esses códigos de erro indicam um problema estrutural com a saída gerada do modelo, como uma chamada de função malformada ou uma chamada de ferramenta não declarada.

| Código | Descrição |
| --- | --- |
| `malformed_function_call` | O modelo gerou uma chamada de função que não pôde ser analisada. |
| `malformed_tool_call` | O modelo gerou uma chamada de ferramenta que não pôde ser analisada. |
| `unexpected_tool_call` | O modelo chamou uma ferramenta que não foi declarada na solicitação. |
| `no_image` | O modelo não conseguiu gerar uma imagem. |
| `too_many_tool_calls` | O modelo gerou mais chamadas de função do que o permitido. |
| `missing_thought_signature` | A resposta não tem uma assinatura de pensamento obrigatória. |

## Formato da resposta de erro

Todos os erros da API Interactions retornam um objeto `error` que contém um `code` e um `message`. Por exemplo, transmitir um tipo de ferramenta incompatível retorna:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `code` | string | Um código de erro legível por máquina em `snake_case`. |
| `message` | string | Uma descrição legível por humanos do que deu errado. |

## Como os erros são entregues

A API entrega erros de maneira diferente, dependendo se você faz uma solicitação HTTP padrão ou uma solicitação de streaming (SSE).

### Solicitações HTTP padrão

Para solicitações padrão (não de streaming), a API define o código de status da resposta HTTP (como `400 Bad Request`, `401 Unauthorized` ou `429 Too Many Requests`) e retorna um objeto `error` no corpo da resposta JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Solicitações de streaming (SSE)

Para solicitações de streaming (`stream: true`), a API envia eventos de erro pelo fluxo de eventos enviados pelo servidor (SSE) com `event_type` definido como `"error"`. O campo `error` contém a mesma estrutura `code` e `message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Para conferir o esquema completo de eventos SSE, consulte a [Referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br).

## A seguir

- [Solução de problemas da API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-br): resolva problemas comuns e cenários de erro.
- [Limites de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br): saiba mais sobre limites de solicitação e processamento de cotas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-20 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-20 UTC."],[],[]]
