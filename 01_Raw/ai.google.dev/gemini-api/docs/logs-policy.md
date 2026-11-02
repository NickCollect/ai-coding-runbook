---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-BR
fetched_at: 2026-11-02T07:28:23.553601+00:00
title: "Registro e compartilhamento de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registro e compartilhamento de dados

Nesta página, descrevemos o armazenamento e o gerenciamento dos
[registros da API Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br), que são dados de API
de propriedade do desenvolvedor de chamadas de API Gemini compatíveis para projetos com o faturamento ativado. Os registros
abrangem todo o processo, desde a solicitação do usuário até a resposta do modelo.
Esses registros, que são particulares do seu projeto do Google Cloud, são separados de todos os
registros mantidos exclusivamente para fins de [monitoramento de abuso](https://ai.google.dev/gemini-api/docs/usage-policies?hl=pt-br).

## Dados que podem ser compartilhados

A geração de registros é ativada por padrão para chamadas da API Interactions e da API Generate Content
em projetos criados a partir de 26 de outubro de 2026. Como proprietário do projeto,
é possível ativar ou desativar a geração de registros a qualquer momento na página
[Registros e conjuntos de dados](https://aistudio.google.com/logs?hl=pt-br) no AI Studio. Os registros
são para seu próprio uso, e você pode optar por compartilhá-los com o Google como feedback
para nos ajudar a melhorar continuamente nossos modelos.

Com a geração de registros ativada, você pode nos ajudar a criar sistemas de IA que continuam sendo
valiosos para desenvolvedores em vários campos e casos de uso, optando por
contribuir com os seguintes dados para melhorias de produtos e treinamento de modelos:

- **Conjuntos de dados**: use a interface de registros e conjuntos de dados do Google AI Studio para
  escolher registros (solicitações, respostas, metadados etc.) de interesse de
  chamadas da API Gemini compatíveis, contribuídos por inclusão em conjuntos de dados, com a
  opção de desativação durante a criação do conjunto de dados.
- **Feedback**: ao analisar os registros, você pode enviar feedback, incluindo avaliações com Gostei e Não gostei e comentários escritos.

Quando você compartilha um conjunto de dados com o Google, os registros dele, incluindo
solicitações e respostas, são processados de acordo com nossos
[Termos](https://developers.google.com/terms?hl=pt-br) para
[Serviços não pagos](https://ai.google.dev/gemini-api/terms?hl=pt-br#data-use-unpaid).
Isso significa que o conjunto de dados pode ser usado para desenvolver e melhorar produtos,
serviços e tecnologias de aprendizado de máquina do Google, incluindo a melhoria e
o treinamento dos nossos modelos. **Não inclua informações pessoais, sensíveis ou confidenciais.**

## Como usamos seus dados

Os registros são retidos por um período máximo padrão de 55 dias. Após esse período,
os registros são marcados automaticamente para exclusão. A janela de retenção de armazenamento de um
projeto pode ser atualizada no AI Studio para marcar automaticamente os registros para exclusão
após 7, 14, 28 ou 55 dias.

É possível criar [conjuntos de dados](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br) para reter registros de interesse além do período de retenção definido para casos de uso downstream e contribuição opcional para melhorias de modelo. Os registros armazenados em conjuntos de dados
não têm períodos de retenção definidos.

Por padrão, como a geração de registros só está disponível para projetos com faturamento ativado,
os comandos e as respostas nos registros não são usados para melhoria ou desenvolvimento de produtos, de acordo com nossos [Termos](https://developers.google.com/terms?hl=pt-br)
sobre o uso de dados.

Se você optar por compartilhar conjuntos de dados dos seus registros com o Google, eles serão
usados como dados de demonstração do mundo real para entender melhor a diversidade de
domínios e contextos em que os sistemas e aplicativos de IA são usados. Esses dados podem ser usados para melhorar a qualidade do modelo e informar o treinamento e a avaliação de futuros modelos e serviços. Esses dados são tratados de acordo com nossos termos de uso de dados para [Serviços Não Pagos](https://ai.google.dev/gemini-api/terms?hl=pt-br#data-use-unpaid).

Por isso, revisores humanos podem ler, fazer anotações e processar as entradas e saídas de API que você compartilha. Antes de usar os dados para melhorar o modelo, o Google toma medidas
para proteger a privacidade do usuário como parte desse processo. Isso inclui desconectar
esses dados da sua Conta do Google, da chave de API e do projeto na nuvem antes que os revisores
os vejam ou façam anotações.

## Permissões de dados

Ao aceitar contribuir com dados da API, você confirma que tem as permissões necessárias para que o Google processe e use os dados conforme descrito nesta documentação. **Não envie registros que contenham informações sensíveis,
confidenciais ou reservadas obtidas pelo serviço pago**.
A licença que você concede ao Google de acordo com a seção "[Envio de
conteúdo](https://developers.google.com/terms?hl=pt-br#b_submission_of_content)"
nos Termos da API também se estende, na medida exigida pela legislação
aplicável para nosso uso, a qualquer conteúdo (por exemplo, comandos, incluindo instruções do sistema
associadas, conteúdo em cache e arquivos como imagens, vídeos ou documentos)
que você enviar aos Serviços e a todas as respostas geradas.

## Compartilhamento de dados pessoais e feedback

Você pode nos ajudar a avançar na fronteira da pesquisa de IA, da API Gemini e do Google
AI Studio ao compartilhar seus dados como exemplos, o que nos permite
melhorar continuamente nossos modelos em vários contextos e criar sistemas de IA que
continuam sendo valiosos para desenvolvedores em vários campos e casos de uso.

### Nível de colaborador da API Gemini

O nível de colaborador do Gemini permite que os desenvolvedores recebam descontos nos custos de tokens em
determinados modelos em troca da permissão para usar dados desses modelos para
fornecer, melhorar e desenvolver produtos e serviços do Google e tecnologias de aprendizado de
máquina.

Os desenvolvedores recebem até 50% de desconto nos custos de token para modelos selecionados, com o mesmo
desempenho em tempo real da [API padrão](https://ai.google.dev/gemini-api/docs/optimization?hl=pt-br). Os
seguintes modelos são compatíveis:

| Modelo | Nível "Colaborador" |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-3.8-flash) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-3.5-flash-lite) | ✔️ |

**Uso de dados:**

- Ao ativar o nível de colaborador em um projeto, os dados do uso do modelo participante no projeto serão usados de acordo com nossos termos para "[Serviços não pagos](https://ai.google.dev/gemini-api/terms?hl=pt-br#unpaid-services)".
  Como seus dados serão usados para melhorar os produtos e as tecnologias de aprendizado de máquina do Google, não envie informações sensíveis ou pessoais.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-26 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-26 UTC."],[],[]]
