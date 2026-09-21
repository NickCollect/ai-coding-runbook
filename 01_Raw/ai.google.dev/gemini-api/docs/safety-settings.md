---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-BR
fetched_at: 2026-09-21T05:50:34.723420+00:00
title: "Configura\u00e7\u00f5es de seguran\u00e7a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Configurações de segurança

A API Gemini oferece configurações de segurança que podem ser ajustadas durante o estágio de prototipagem para determinar se o aplicativo requer uma configuração de segurança mais ou menos restritiva. É possível ajustar essas configurações em quatro categorias de filtro para restringir ou permitir determinados tipos de conteúdo.

Este guia aborda como a API Gemini processa as configurações e a filtragem de segurança e como você pode mudar as configurações de segurança do seu aplicativo.

## Filtros de segurança

Os filtros de segurança ajustáveis da API Gemini abrangem as seguintes categorias:

| Categoria | Descrição |
| --- | --- |
| Assédio | Comentários negativos ou prejudiciais relacionados à identidade e/ou características protegidas atributos. |
| Discurso de ódio | Conteúdo grosseiro, desrespeitoso ou linguagem obscena. |
| Conteúdo sexualmente explícito | Contém referências a atos sexuais ou outro conteúdo obsceno. |
| Perigoso | Promove, facilita ou encoraja atos prejudiciais. |

Essas categorias são definidas em [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=pt-br). Use esses filtros para ajustar o que for necessário ao seu caso de uso. Por exemplo, se você estiver criando um diálogo de videogame, poderá considerar aceitável permitir mais conteúdo classificado como *Perigoso* devido à natureza do jogo.

Além dos filtros de segurança ajustáveis, a API Gemini tem proteções integradas contra danos principais, como conteúdo que coloca crianças em risco.
Esses tipos de danos são sempre bloqueados e não podem ser ajustados.

### Nível de filtragem de segurança do conteúdo

A API Gemini categoriza o nível de probabilidade de o conteúdo ser inseguro como `HIGH`, `MEDIUM`, `LOW` ou `NEGLIGIBLE`.

A API Gemini bloqueia o conteúdo com base na probabilidade de o conteúdo ser inseguro, não na gravidade. É importante ter isso em mente, porque alguns conteúdos podem apresentar uma probabilidade baixa de insegurança, mesmo que a gravidade dos danos seja alta. Por exemplo, comparando as frases:

1. O robô me bateu.
2. O robô me cortou.

A primeira frase pode resultar em uma probabilidade maior de ser insegura, mas a segunda frase pode ser considerada mais grave em termos de violência.
Por isso, é importante que você faça testes criteriosos e considere o nível apropriado de bloqueio necessário para oferecer suporte aos principais casos de uso e minimizar os danos aos usuários finais.

### Filtragem de segurança por solicitação

É possível ajustar as configurações de segurança de cada solicitação feita à API. Quando você faz uma solicitação, o conteúdo é analisado e recebe uma classificação de segurança. A classificação de segurança inclui a categoria e a probabilidade da classificação de dano. Por exemplo, se o conteúdo foi bloqueado porque a categoria de assédio tinha uma alta probabilidade, a classificação de segurança retornada teria a categoria igual a `HARASSMENT` e a probabilidade de dano definida como `HIGH`.

Devido à segurança inerente do modelo, outros filtros ficam **desativados** por padrão.
Se você optar por ativá-los, poderá configurar o sistema para bloquear o conteúdo com base na probabilidade de ele ser inseguro. O comportamento padrão do modelo abrange a maioria dos casos de uso. Portanto, só ajuste essas configurações se isso for consistentemente necessário para seu aplicativo.

A tabela a seguir descreve as configurações de bloqueio que você pode ajustar em cada categoria. Por exemplo, se você definir a configuração de bloqueio como **Bloquear poucos** na categoria **Discurso de ódio**, tudo com alta probabilidade de ser um conteúdo de discurso de ódio será bloqueado. No entanto, qualquer item com menor probabilidade de risco é permitido.

| Limite (Google AI Studio) | Limite (API) | Descrição |
| --- | --- | --- |
| Desativada | `OFF` | Desativar o filtro de segurança |
| Bloquear nenhum | `BLOCK_NONE` | Sempre mostrar, seja qual for a probabilidade do conteúdo não ser seguro |
| Bloquear poucos | `BLOCK_ONLY_HIGH` | Bloquear quando houver alta probabilidade do conteúdo não ser seguro |
| Bloquear alguns | `BLOCK_MEDIUM_AND_ABOVE` | Bloquear quando houver probabilidade média ou alta do conteúdo não ser seguro |
| Bloquear muitos | `BLOCK_LOW_AND_ABOVE` | Bloquear quando houver probabilidade baixa, média ou alta do conteúdo não ser seguro |
| N/A | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Como o limite não foi especificado, o bloqueio está usando o limite padrão |

Se o limite não estiver definido, o limite de bloqueio padrão será **Desativado** para os modelos Gemini 2.5 e 3.

Você pode definir essas configurações para cada solicitação feita ao serviço generativo.
Consulte a [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=pt-br#harmblockthreshold) referência da API
para mais detalhes.

### Feedback de segurança

[`generateContent`](https://ai.google.dev/api/generate-content?hl=pt-br#method:-models.generatecontent)
retorna um
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=pt-br#generatecontentresponse) que
inclui feedback de segurança.

O feedback do comando está incluído em
[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=pt-br#promptfeedback). Se `promptFeedback.blockReason` estiver definido, o conteúdo do comando será bloqueado.

O feedback do candidato de resposta está incluído em
[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=pt-br#candidate) e
[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=pt-br#candidate). Se o conteúdo da resposta foi bloqueado e o `finishReason` era `SAFETY`, inspecione `safetyRatings` para mais detalhes. O conteúdo bloqueado não é retornado.

## Ajustar configurações de segurança

Esta seção aborda como ajustar as configurações de segurança no Google AI Studio e no seu código.

### Google AI Studio

É possível ajustar as configurações de segurança no Google AI Studio.

Clique em **Configurações de segurança** em **Configurações avançadas** no painel **Executar configurações** para abrir o modal **Executar configurações de segurança**. No modal, use os controles deslizantes para ajustar o nível de filtragem de conteúdo por categoria de segurança:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=pt-br)

Quando você envia uma solicitação (por exemplo, fazendo uma pergunta ao modelo), uma warning
**Conteúdo bloqueado** mensagem aparece se o conteúdo da solicitação for bloqueado. Para mais detalhes, mantenha o ponteiro sobre o texto **Conteúdo bloqueado** para conferir a categoria e a probabilidade da classificação de dano.

### Exemplos de código

O snippet de código a seguir mostra como definir as configurações de segurança na chamada `GenerateContent`. Isso define o limite para a categoria de discurso de ódio (`HARM_CATEGORY_HATE_SPEECH`). Definir essa categoria como `BLOCK_LOW_AND_ABOVE` bloqueia qualquer conteúdo que tenha uma probabilidade baixa ou maior de ser um discurso de ódio. Para entender as configurações de limite, consulte [Filtragem de segurança
por solicitação](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
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

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
        .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(Arrays.asList(hateSpeechSafety))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Some potentially unsafe prompt.", config);

System.out.println(response.text());
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## Próximas etapas

- Consulte a [referência da API](https://ai.google.dev/api?hl=pt-br) para saber mais sobre a API completa.
- Analise as [orientações de segurança](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-br) para uma visão geral das considerações de segurança
  ao desenvolver com LLMs.
- Saiba mais sobre como avaliar a probabilidade em relação à gravidade da equipe do [Jigsaw
  team](https://developers.perspectiveapi.com/s/about-the-api-score)
- Saiba mais sobre os produtos que contribuem para soluções de segurança, como a
  [API
  Perspective](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).
  \* É possível usar essas configurações de segurança para criar um classificador de toxicidade. Consulte o [exemplo](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=pt-br) de
  classificação
  para começar.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
