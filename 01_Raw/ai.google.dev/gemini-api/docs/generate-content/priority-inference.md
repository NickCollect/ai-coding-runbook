---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=pt-BR
fetched_at: 2026-08-24T02:33:18.506229+00:00
title: "Infer\u00eancia de prioridade \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Inferência de prioridade

Descrição: saiba como otimizar a latência com o nível de inferência de prioridade

A API Gemini Priority é um nível de inferência premium projetado para cargas de trabalho essenciais aos negócios que exigem menor latência e maior confiabilidade a um preço premium. O tráfego do nível de prioridade tem prioridade sobre o tráfego da API padrão e do nível Flex.

A inferência de prioridade está disponível para usuários [dos níveis 2 e 3](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#about-billing) nos endpoints da API GenerateContent
e da API Interactions.

## Como usar a prioridade

Para usar o nível de prioridade, defina o campo `service_tier` no corpo da solicitação como `priority`. O nível padrão será usado se o campo for omitido.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Como funciona a inferência de prioridade

A inferência de prioridade encaminha solicitações para filas de computação de alta criticidade, oferecendo desempenho rápido e previsível para aplicativos voltados ao usuário. O mecanismo principal é um downgrade suave do lado do servidor para o processamento padrão de tráfego que excede os limites dinâmicos, garantindo a estabilidade do aplicativo em vez de falhar na solicitação.

| Recurso | Prioridade | Padrão | Flex | Lote |
| --- | --- | --- | --- | --- |
| **Preços** | 75 a 100% mais caro que o padrão | Preço total | 50% de desconto | 50% de desconto |
| **Latência** | Segundos | Segundos a minutos | Minutos (meta de 1 a 15 minutos) | Até 24 horas |
| **Confiabilidade** | Alta (não descartável) | Alta / média-alta | Melhor esforço (descartável) | Alta (para capacidade de processamento) |
| **Interface** | Síncrona | Síncrona | Síncrona | Assíncrona |

### Principais benefícios

- **Baixa latência**: projetado para tempos de resposta de segundos para ferramentas de IA interativas,
  voltadas ao usuário.
- **Alta confiabilidade**: o tráfego é tratado com a maior criticidade e é
  estritamente não descartável.
- **Degradação suave**: picos de tráfego que excedem os limites dinâmicos são
  automaticamente rebaixados para o nível padrão para processamento em vez de falhar,
  evitando interrupções de serviço.
- **Baixa fricção**: usa o mesmo método síncrono `generateContent` que os
  níveis padrão e Flex.

### Casos de uso

O processamento de prioridade é ideal para fluxos de trabalho essenciais aos negócios em que o desempenho e a confiabilidade são fundamentais.

- **Aplicativos de IA interativos**: chatbots de atendimento ao cliente e copilotos em que
  os usuários pagam um valor premium e esperam respostas rápidas e consistentes.
- **Mecanismos de decisão em tempo real**: sistemas que exigem resultados altamente confiáveis e de baixa latência
  como triagem de tickets ao vivo ou detecção de fraudes.
- **Recursos premium para clientes**: desenvolvedores que precisam garantir objetivos de nível de serviço (SLOs) mais altos para clientes pagantes.

### Limites de taxas

O consumo de prioridade tem limites de taxa próprios, mesmo que o consumo seja
contabilizado nos [limites gerais de taxa de tráfego interativo](https://aistudio.google.com/rate-limit?hl=pt-br). Os limites de taxa padrão para inferência de prioridade são **0,3 vezes o limite de taxa padrão para modelo / nível**.

### Lógica de downgrade suave

Se os limites de prioridade forem excedidos devido ao congestionamento, as solicitações de estouro serão **rebaixadas automaticamente e de maneira suave** para o processamento padrão em vez de falhar com um erro 503 ou 429. As solicitações rebaixadas são cobradas na taxa padrão, não na taxa premium de prioridade.

### Responsabilidade do cliente

- **Monitoramento de respostas**: os desenvolvedores precisam monitorar o `x-gemini-service-tier`
  cabeçalho na resposta da API para detectar se as solicitações estão sendo rebaixadas com frequência para
  `standard`.
- **Nova tentativa**: os clientes precisam implementar a lógica de nova tentativa/espera exponencial para
  erros padrão, como `DEADLINE_EXCEEDED`.

## Preços

A inferência de prioridade custa de 75 a 100% mais do que a [API padrão](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) e é cobrada por token.

## Modelos compatíveis

Os modelos a seguir oferecem suporte à inferência de prioridade:

| Modelo | Inferência de prioridade |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## A seguir

Leia sobre outras opções de [inferência e otimização](https://ai.google.dev/gemini-api/docs/optimization?hl=pt-br) do Gemini:

- [Inferência flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br) para redução de custos de 50%.
- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br) para processamento assíncrono em até 24 horas.
- [Armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) para reduzir os custos de token de entrada.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
