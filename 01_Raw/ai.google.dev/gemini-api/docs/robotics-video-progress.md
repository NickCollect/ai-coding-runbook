---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pt-BR
fetched_at: 2026-09-28T06:17:09.189454+00:00
title: "Compreens\u00e3o do v\u00eddeo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Compreensão do vídeo

O Gemini Robotics ER 2 pode acompanhar o progresso da tarefa em feeds de vídeo contínuos usando dois recursos:

- Localização de momentos: identifica o carimbo de data/hora exato em que um evento principal ocorre.
- Classificação de progresso: atribui cada vídeo a um dos cinco intervalos de conclusão (0 a 20%, 20 a 40%, 40 a 60%, 60 a 80%, 80 a 100%).

## Localização de momentos

A localização de momentos identifica o frame de vídeo exato em que um evento crítico ocorre, por exemplo, quando um copo está cheio ou um nó é amarrado. Os robôs usam isso para verificar o sucesso, sequenciar etapas e acionar correções.

O exemplo de comando a seguir pede ao modelo para identificar o momento de conclusão de uma determinada tarefa em um vídeo:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

A seguir, mostramos exemplos de frames de um vídeo de localização de momentos, com o modelo identificando o carimbo de data/hora de conclusão da tarefa:

![Exemplo de frames de vídeo mostrando o resultado da descoberta de momentos com uma sobreposição de carimbo de data/hora](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=pt-br)

## Classificação de progresso

A classificação de progresso atribui um vídeo a um dos cinco intervalos de conclusão: 0 a 20%, 20 a 40%, 40 a 60%, 60 a 80% ou 80 a 100%. Isso oferece aos robôs reconhecimento situacional em tempo real para que eles possam ajustar ações ou repetir etapas com falha sem reiniciar todo um fluxo de trabalho.

O exemplo de comando a seguir pede ao modelo para classificar o nível de progresso atual de um vídeo:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

A seguir, mostramos exemplos de frames de um vídeo de classificação de progresso, com o modelo atribuindo um intervalo de progresso:

![Exemplo de frames de vídeo mostrando a saída da classificação de progresso com um rótulo de intervalo de progresso](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=pt-br)

## Exemplos

Para exemplos executáveis completos, incluindo o acompanhamento de tarefas de várias etapas, consulte o
[cookbook de robótica](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## A seguir

- [API Live para robótica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-br): streaming bidirecional em tempo real.
- [Orquestração de tarefas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pt-br): tarefas de longo prazo com raciocínio espacial.
- [Visão geral do Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pt-br): comparação e recursos do modelo.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-08 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-08 UTC."],[],[]]
