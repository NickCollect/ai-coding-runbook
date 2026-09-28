---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=pt-BR
fetched_at: 2026-09-28T06:25:45.129019+00:00
title: "Erros da API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Erros da API

Esta página fornece uma referência para códigos de erro de back-end retornados pela API `GenerateContent`, descreve o formato de resposta de erro do gRPC e fornece etapas de solução de problemas.

## Códigos de erro HTTP

A tabela a seguir lista códigos de erro comuns do back-end, explicações sobre as causas e soluções recomendadas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Código HTTP** | **Status** | **Descrição** | **Exemplo** | **Solução** |
| 400 | INVALID\_ARGUMENT | O corpo da solicitação está incorreto. | Há um erro de digitação ou um campo obrigatório ausente na sua solicitação. | Consulte a [referência da API](https://ai.google.dev/api?hl=pt-br) para ver o formato da solicitação, exemplos e versões compatíveis. Usar recursos de uma versão mais recente da API com um endpoint mais antigo pode causar erros. |
| 400 | FAILED\_PRECONDITION | O nível sem custo financeiro da API Gemini não está disponível no seu país. Ative o faturamento no seu projeto no Google AI Studio. | Você está fazendo uma solicitação em uma região onde o nível sem custo financeiro não está disponível e não ativou o faturamento no seu projeto no Google AI Studio. | Para usar a API Gemini, você precisa configurar um plano pago usando o [Google AI Studio](https://aistudio.google.com/apikey?hl=pt-br). |
| 402 | RESOURCE\_EXHAUSTED | Seu saldo de crédito pré-pago acabou. | Sua conta de faturamento ficou sem créditos pré-pagos, então todas as chaves de API vinculadas a ela pararam de funcionar. | [Adicione créditos](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#buy-credits) à sua conta de faturamento ou ative a [recarga automática](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#auto-reload). Não tente de novo. A solicitação não vai ser concluída até que os créditos sejam adicionados. |
| 403 | PERMISSION\_DENIED | Sua chave de API não tem as permissões necessárias. | Você está usando a chave de API errada ou tentando usar um modelo ajustado sem passar pela [autenticação adequada](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pt-br). | Verifique se a chave de API está definida e tem o acesso correto. E faça a autenticação adequada para usar modelos ajustados. |
| 404 | NOT\_FOUND | O recurso solicitado não foi encontrado. | Não foi encontrado um arquivo de imagem, áudio ou vídeo referenciado na sua solicitação. | Verifique se todos os parâmetros na sua solicitação são válidos para a versão da API. |
| 429 | RESOURCE\_EXHAUSTED | Você excedeu um dos limites de taxa da API (RPM, TPM, RPD, gasto etc.). | Você está enviando muitas solicitações, usando muitos tokens ou excedendo os limites com base nos gastos do histórico de faturamento e do nível da sua conta. | Verifique se você está dentro dos [limites de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br) do modelo. Aguarde um pouco e tente de novo. Reduza a taxa ou o tamanho das solicitações. [Solicite um aumento no limite de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br#request-rate-limit-increase), se necessário. |
| 499 | CANCELADO | A operação foi cancelada, geralmente pelo autor da chamada. | O cliente encerrou a conexão antes que a API pudesse terminar de responder. | Verifique se o cliente ou a infraestrutura de rede está fechando a conexão prematuramente (por exemplo, devido a um tempo limite do lado do cliente). |
| 500 | INTERNAL | Ocorreu um erro inesperado no Google. | O contexto da sua entrada é muito longo. | Confira a [página de status da API Gemini](https://aistudio.google.com/status?hl=pt-br) para ver se há incidentes em andamento. Reduza o contexto de entrada ou mude temporariamente para outro modelo (por exemplo, do Gemini 2.5 Pro para o Gemini 2.5 Flash) e veja se funciona. Ou aguarde um pouco e tente de novo. Se o problema persistir depois de tentar novamente, informe usando o botão **Enviar feedback** no Google AI Studio. |
| 503 | INDISPONÍVEL | O serviço pode estar temporariamente sobrecarregado ou indisponível. | O serviço está temporariamente sem capacidade. | Confira a [página de status da API Gemini](https://aistudio.google.com/status?hl=pt-br) para ver se há incidentes em andamento. Mude temporariamente para outro modelo (por exemplo, do Gemini 2.5 Pro para o Gemini 2.5 Flash) e veja se funciona. Ou aguarde um pouco e tente de novo. Se o problema persistir depois de tentar novamente, informe usando o botão **Enviar feedback** no Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | O serviço não consegue concluir o processamento dentro do prazo. | Seu comando (ou contexto) é muito grande para ser processado a tempo. | Defina um "tempo limite" maior na solicitação do cliente para evitar esse erro. |

## Formato da resposta de erro

Quando uma solicitação `GenerateContent` falha, a API define o código de status HTTP (como `400 Bad Request`, `403 Forbidden` ou `429 Too Many Requests`) e retorna um corpo de resposta JSON com detalhes do status do gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `code` | número inteiro | O código de status HTTP. |
| `message` | string | Uma descrição legível do erro. |
| `status` | string | O código de status gRPC em `SCREAMING_CASE`. |
| `details` | matriz | Contexto adicional do erro, como `ErrorInfo` ou `LocalizedMessage`. |

## A seguir

- [Solução de problemas da API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-br): resolva problemas comuns e cenários de erro.
- [Limites de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br): saiba mais sobre limites de solicitação e processamento de cotas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-20 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-20 UTC."],[],[]]
