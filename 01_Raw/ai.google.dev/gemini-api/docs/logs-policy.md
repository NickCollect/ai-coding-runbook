---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-BR
fetched_at: 2026-06-22T06:35:25.737513+00:00
title: "Registro e compartilhamento de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registro e compartilhamento de dados

Esta página descreve o armazenamento e o gerenciamento de
[registros da API Gemini](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br), que são dados de
API de propriedade do desenvolvedor de chamadas da API Gemini compatíveis para projetos com o faturamento ativado. Os registros abrangem todo o processo, desde a solicitação de um usuário até a resposta do modelo.

## 1. Dados que podem ser compartilhados

Como proprietário do projeto, você pode ativar o registro de chamadas da API Gemini para seu próprio uso ou para feedback e compartilhamento com o Google, ajudando a melhorar continuamente nossos modelos.

Com o registro ativado, você pode nos ajudar a criar sistemas de IA que continuam sendo valiosos para desenvolvedores em vários campos e casos de uso, contribuindo com os seguintes dados para melhorias de produtos e treinamento de modelos:

- **Conjuntos de dados**:use a interface de registros e conjuntos de dados do Google AI Studio para escolher registros (solicitações, respostas, metadados etc.) de chamadas da API Gemini compatíveis; contribuídos pela inclusão em conjuntos de dados, com a opção de desativar durante a criação do conjunto de dados.
- **Feedback**:ao analisar os registros, você pode fornecer feedback, incluindo classificações de positivo/negativo e comentários escritos.

Quando você compartilha um conjunto de dados com o Google, seus registros nesse conjunto, incluindo
solicitações e respostas, serão processados de acordo com nossos
[Termos](https://developers.google.com/terms?hl=pt-br) para
"[Serviços não pagos](https://ai.google.dev/gemini-api/terms?hl=pt-br#data-use-unpaid),"
o que significa que o conjunto de dados pode ser usado para desenvolver e melhorar produtos, serviços e tecnologias de aprendizado de máquina do Google,
incluindo aprimorar e
treinar nossos modelos. **Não inclua informações pessoais, sensíveis ou confidenciais**.

## 2. Como usamos seus dados

Os registros expiram após 55 dias por padrão. Eles ficam indisponíveis após esse período. Os conjuntos de dados podem ser criados para reter registros de interesse ou valor além desse período para casos de uso downstream e contribuição opcional para melhorias de modelos. Os registros armazenados em conjuntos de dados não têm datas de validade definidas, mas cada projeto tem um limite de armazenamento padrão de até 1.000 registros.

Por padrão, como o registro só está disponível para projetos com o faturamento ativado,
os comandos e as respostas nos registros não são usados para melhoria ou
desenvolvimento de produtos, de acordo com nossos [Termos](https://developers.google.com/terms?hl=pt-br)
de uso de dados.

Se você optar por compartilhar conjuntos de dados dos seus registros com o Google, esses conjuntos serão usados como dados de demonstração do mundo real para entender melhor a diversidade de domínios e contextos em que os sistemas e aplicativos de IA são usados. Esses dados podem ser usados para melhorar a qualidade do modelo e informar o treinamento e a avaliação de modelos e serviços futuros. Esses dados são tratados de acordo com nossos termos de uso de dados para [Serviços não pagos](https://ai.google.dev/gemini-api/terms?hl=pt-br#data-use-unpaid).
Assim, revisores humanos podem ler, fazer anotações e tratar as entradas e saídas da API que você compartilha. Antes que os dados sejam usados para melhorar o modelo, o Google toma medidas para proteger a privacidade do usuário como parte desse processo. Isso inclui desconectar esses dados da sua Conta do Google, da chave de API e do projeto na nuvem antes que os revisores os vejam ou façam anotações.

## 3. Permissões de dados

Ao ativar a contribuição de dados da API, você confirma que tem as permissões necessárias para que o Google trate e use os dados conforme descrito nesta documentação. **Não contribua com registros que contenham informações sensíveis, confidenciais ou proprietárias obtidas pelo serviço pago**.
A licença que você concede ao Google na seção "[Envio de conteúdo](https://developers.google.com/terms?hl=pt-br#b_submission_of_content)" nos Termos das APIs também se estende, na medida exigida pela legislação aplicável para nosso uso, a qualquer conteúdo (por exemplo, comandos, incluindo instruções de sistema associadas, conteúdo armazenado em cache e arquivos, como imagens, vídeos ou documentos) que você enviar aos Serviços e a quaisquer respostas geradas.

## 4. Compartilhamento de dados pessoais e feedback

Você pode nos ajudar a avançar na fronteira da pesquisa de IA, da API Gemini e do Google AI Studio ativando o compartilhamento de dados como exemplos, permitindo que melhoremos continuamente nossos modelos em vários contextos e criemos sistemas de IA que continuam sendo valiosos para desenvolvedores em vários campos e casos de uso.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-01 UTC."],[],[]]
