---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=pt-BR
fetched_at: 2026-10-05T06:50:45.554424+00:00
title: "Streaming do Gemini Robotics ER 2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Streaming do Gemini Robotics ER 2

O Gemini Robotics ER 2 Streaming é um modelo de visão-linguagem (VLM) para robótica
otimizado para streaming de texto em tempo real usando a API Live. Ele aceita entradas de texto, imagem, vídeo e áudio e oferece suporte a streaming bidirecional com chamadas de função.

[Testar no Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=pt-br)

## Documentação

Acesse a página [API Live para robótica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pt-br) para conferir a cobertura completa de recursos e funcionalidades.

## gemini-robotics-er-2-streaming-preview

### Pré-lançamento do Gemini Robotics ER 2

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-2-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  Compatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  Compatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  Compatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  Compatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  Compatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  incompatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  Compatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  Compatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  Compatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-2-preview` |
| calendar\_monthÚltima atualização | Julho de 2026 |
| id\_cardCard de modelo | [Card de modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pt-br) |

### Pré-lançamento do Gemini Robotics ER 2 Streaming

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  incompatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  incompatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  incompatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  incompatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  incompatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  Compatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  incompatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  incompatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  incompatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthÚltima atualização | Julho de 2026 |
| id\_cardCard de modelo | [Card de modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pt-br) |

### Pré-lançamento do Gemini Robotics ER 1.6

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | `gemini-robotics-er-1.6-preview` |
| saveTipos de dados aceitos | **Entradas** (link em inglês)  Texto, imagens, vídeo, áudio  **Saída**  Texto |
| token\_autoLimites de token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | **Limite de tokens de entrada**  131.072  **Limite de token de saída**  65.536 |
| handymanRecursos | **[Geração de áudio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br)**  incompatível  **[Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**  Compatível  **[Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)**  Compatível  **[Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br)**  Compatível  **[Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)**  Compatível  **[Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)**  Compatível  **[Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)**  Compatível  **[Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)**  incompatível  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)**  incompatível  **[Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)**  Compatível  **[Respostas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)**  Compatível  **[Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)**  Compatível  **[Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)**  Compatível |
| speedOpções de consumo | **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**  Compatível  **[Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)**  incompatível  **[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)**  incompatível |
| Versões 123 | Leia os [padrões de versão do modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br#model-versions) para mais detalhes.  - Visualização: `gemini-robotics-er-1.6-preview` |
| calendar\_monthÚltima atualização | Dezembro de 2025 |
| cognition\_2Limite de conhecimento | Janeiro de 2025 |

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-08-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-08-19 UTC."],[],[]]
