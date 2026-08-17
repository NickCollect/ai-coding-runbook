---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=pt-BR
fetched_at: 2026-08-17T02:29:50.072083+00:00
title: "Explica\u00e7\u00e3o sobre as vers\u00f5es da API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Referência da API](https://ai.google.dev/api?hl=pt-br)

Envie comentários

# Explicação sobre as versões da API

Este documento oferece uma visão geral das diferenças entre as versões `v1`
e `v1beta` da API Gemini.

- **v1**: versão estável da API. Os recursos na versão estável têm suporte completo durante o ciclo de vida da versão principal. Se houver mudanças significativas, uma nova versão principal da API será criada, e a versão atual será descontinuada após um período razoável.
  Mudanças não significativas podem ser introduzidas na API sem alterar a versão principal. A **API Interactions** e os principais recursos dela estão disponíveis na versão `v1`.
- **v1beta**: essa versão inclui recursos e funcionalidades iniciais que estão sendo desenvolvidos ativamente. Embora os recursos na versão `v1beta` possam estar sujeitos a mudanças à medida que os refinamos com base no feedback, ela permite que você teste novos recursos antes que sejam promovidos à versão estável.

## Suporte a recursos e funcionalidades

A tabela a seguir detalha a disponibilidade de recursos nas versões `v1` (GA)
e `v1beta` (Beta). Os principais recursos e ferramentas da API se aplicam à API Interactions e à `generateContent`, a menos que especificado de outra forma:

| Recurso | v1 | v1beta |
| --- | --- | --- |
| **Principais recursos da API** |  |  |
| [API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br) |  |  |
| [Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) |  |  |
| [Saída estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) |  |  |
| [Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br) |  |  |
| [Instruções do sistema](https://ai.google.dev/gemini-api/docs/system-instructions?hl=pt-br) |  |  |
| [Saída de áudio (configuração de fala)](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br) |  |  |
| [Nível de serviço (prioridade / flexível)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br) |  |  |
| **Ferramentas** |  |  |
| [Ferramenta de execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) |  |  |
| [Embasamento da Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) |  |  |
| [Embasamento do Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) |  |  |
| [Ferramenta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) |  |  |
| [Ferramenta de pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br) |  |  |
| [Ferramenta de uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br) |  |  |
| [Ferramenta de servidores MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=pt-br) |  |  |
| **APIs em tempo real** |  |  |
| [API Live (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br) |  |  |
| [API Live Music](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-br) |  |  |
| [Tokens temporários (API Live)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pt-br) |  |  |
| **APIs da plataforma** |  |  |
| [API Models](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) |  |  |
| [Rota do serviço de arquivos](https://ai.google.dev/gemini-api/docs/files?hl=pt-br) |  |  |
| [Rota de lojas de pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br) |  |  |
| [API Agents](https://ai.google.dev/gemini-api/docs/agents?hl=pt-br) |  |  |
| [API Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=pt-br) |  |  |
| [Armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) |  |  |

- - Compatível

## Configurar a versão da API em um SDK

Os SDKs da API Gemini são definidos como `v1beta` por padrão, mas é possível especificar versões definindo a versão da API, conforme mostrado no exemplo de código a seguir:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
  }'
```

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-28 UTC."],[],[]]
