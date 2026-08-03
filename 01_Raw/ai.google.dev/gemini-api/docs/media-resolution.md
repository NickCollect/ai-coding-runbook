---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-BR
fetched_at: 2026-08-03T04:35:30.521727+00:00
title: "Resolu\u00e7\u00e3o da m\u00eddia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Resolução da mídia

O parâmetro `media_resolution` controla como a API Gemini processa entradas de mídia, como imagens, vídeos e documentos PDF, determinando o **número máximo de tokens** alocados para entradas de mídia, permitindo equilibrar a qualidade da resposta com a latência e o custo. Para diferentes configurações, valores padrão e como eles correspondem a tokens, consulte a seção [Contagens de tokens](#token-counts).

É possível configurar a resolução de mídia para objetos de mídia individuais (itens de conteúdo) na solicitação (somente no Gemini 3).

## Resolução de mídia por item de conteúdo (somente no Gemini 3)

O Gemini 3 permite definir a resolução de mídia para objetos de mídia individuais na solicitação, oferecendo otimização refinada do uso de tokens. É possível misturar níveis de resolução em uma única solicitação. Por exemplo, usando alta resolução para um diagrama complexo e baixa resolução para uma imagem contextual simples.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Valores de resolução disponíveis

A API Gemini define os seguintes níveis de resolução de mídia:

- `unspecified`: a configuração padrão. A contagem de tokens para esse nível varia significativamente entre o Gemini 3 e os modelos anteriores.
- `low`: contagem de tokens mais baixa, resultando em processamento mais rápido e custo menor, mas com menos detalhes.
- `medium`: um equilíbrio entre detalhes, custo e latência.
- `high`: contagem de tokens mais alta, fornecendo mais detalhes para o modelo trabalhar, à custa de maior latência e custo.
- `ultra_high` (somente por item de conteúdo): contagem de tokens mais alta, necessária para casos de uso específicos, como [uso de computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br).

O `high` oferece o desempenho ideal para a maioria dos casos de uso.

O número exato de tokens gerados para cada um desses níveis depende do **tipo de mídia** (imagem, vídeo, PDF) e da **versão do modelo**.

## Contagens de tokens

As tabelas abaixo resumem as contagens aproximadas de tokens para cada valor `media_resolution` e tipo de mídia por família de modelos.

**Modelos do Gemini 3**

| MediaResolution | Imagem | Vídeo | PDF |
| --- | --- | --- | --- |
| `unspecified` (padrão) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + texto nativo |
| `medium` | 560 | 70 | 560 + texto nativo |
| `high` | 1120 | 280 | 1120 + texto nativo |
| `ultra_high` | 2240 | N/A | N/A |

## Como escolher a resolução certa

- **Padrão (`unspecified`):** comece com o padrão. Ele é ajustado para um bom equilíbrio de qualidade, latência e custo para a maioria dos casos de uso comuns.
- **`low`:** use para cenários em que o custo e a latência são fundamentais e detalhes refinados são menos importantes.
- **`medium` / `high`:** aumente a resolução quando a tarefa exigir a compreensão de detalhes complexos na mídia. Isso geralmente é necessário para análises visuais complexas, leitura de gráficos ou compreensão de documentos densos.
- **`ultra_high`** : disponível apenas para a configuração por item de conteúdo. Recomendado para casos de uso específicos, como uso de computador ou quando os testes mostram uma melhoria clara em relação a `high`.
- **Controle por item de conteúdo (Gemini 3)** : otimiza o uso de tokens. Por exemplo, em um comando com várias imagens, use `high` para um diagrama complexo e `low` ou `medium` para imagens contextuais mais simples.

**Configurações recomendadas**

A seguir, listamos as configurações de resolução de mídia recomendadas para cada tipo de mídia compatível.

| Tipo de mídia | Configuração recomendada | Máximo de tokens | Orientação de uso |
| --- | --- | --- | --- |
| **Imagens** | `high` | 1120 | Recomendado para a maioria das tarefas de análise de imagens para garantir a máxima qualidade. |
| **PDFs** | `medium` | 560 | Ideal para compreensão de documentos. A qualidade normalmente satura em `medium`. Aumentar para `high` raramente melhora os resultados de OCR para documentos padrão. |
| **Vídeo** (geral) | `low` (ou `medium`) | 70 (por frame) | **Observação**:para vídeos, as configurações `low` e `medium` são tratadas de forma idêntica (70 tokens) para otimizar o uso do contexto. Isso é suficiente para a maioria das tarefas de reconhecimento e descrição de ações. |
| **Vídeo** (com muito texto) | `high` | 280 (por frame) | Necessário apenas quando o caso de uso envolve a leitura de texto denso (OCR) ou pequenos detalhes em frames de vídeo. |

Sempre teste e avalie o impacto de diferentes configurações de resolução no aplicativo para encontrar o melhor equilíbrio entre qualidade, latência e custo.

## Resumo da compatibilidade de versões

- A definição da `resolution` em itens de conteúdo individuais é **exclusiva dos modelos do Gemini 3**.

## Próximas etapas

- Saiba mais sobre os recursos multimodais da API Gemini nos guias de [compreensão de imagens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br), [compreensão de vídeos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br) e [compreensão de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
