---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=pt-BR
fetched_at: 2026-09-21T05:47:19.873001+00:00
title: "Gerar imagens usando o Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)

Envie comentários

# Gerar imagens usando o Imagen

O Imagen é o modelo legado de geração de imagens do Google. Ele foi desativado e não está mais disponível na API Gemini.

## Migrar para o Nano Banana

Migre para o Nano Banana para geração de imagens:

- **Nome do modelo**: use `gemini-2.5-flash-image` (ou modelos do Nano Banana 2, como `gemini-3.1-flash-image`) em vez dos nomes de modelos do Imagen.
- **Método**: use `client.models.generate_content` em vez de
  `client.models.generate_images`.
- **Processamento de respostas**: o Nano Banana retorna partes de conteúdo com dados de imagem
  em vez de um objeto de resposta de imagem específico.

Consulte o [guia de geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) para mais detalhes e exemplos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
