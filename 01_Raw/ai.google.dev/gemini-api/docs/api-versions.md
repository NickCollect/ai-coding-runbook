---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=pt-BR
fetched_at: 2026-05-11T05:07:02.411799+00:00
title: "Explica\u00e7\u00e3o sobre as vers\u00f5es da API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Referência da API](https://ai.google.dev/api?hl=pt-br)

Envie comentários

# Explicação sobre as versões da API

Este documento oferece uma visão geral das diferenças entre as versões `v1`
e `v1beta` da API Gemini.

- **v1**: versão estável da API. Os recursos na versão estável têm suporte total durante o ciclo de vida da versão principal. Se houver mudanças interruptivas, a próxima versão principal da API será criada, e a versão atual será descontinuada após um período razoável.
  Mudanças não interruptivas podem ser introduzidas na API sem alterar a versão principal.
- **v1beta**: essa versão inclui recursos iniciais que podem estar em desenvolvimento e sujeitos a mudanças interruptivas. Também não há garantia de que os recursos na versão Beta serão movidos para a versão estável. **Se você precisar de estabilidade no ambiente de produção e não puder correr o risco de mudanças interruptivas, não use essa versão na produção.**

| Recurso | v1 | v1beta |
| --- | --- | --- |
| Gerar conteúdo: entrada somente de texto |  |  |
| Gerar conteúdo: entrada de texto e imagem |  |  |
| Gerar conteúdo: saída de texto |  |  |
| Gerar conteúdo: conversas com várias interações (chat) |  |  |
| Gerar conteúdo: chamadas de função |  |  |
| Gerar conteúdo: streaming |  |  |
| Incorporar conteúdo: entrada somente de texto |  |  |
| Gerar resposta |  |  |
| Recuperador semântico |  |  |
| API Interactions |  |  |

- - Compatível
- - Nunca será compatível

## Configurar a versão da API em um SDK

Os SDKs da API Gemini são definidos como `v1beta`, mas você pode usar outras versões definindo a versão da API, conforme mostrado no exemplo de código a seguir:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
