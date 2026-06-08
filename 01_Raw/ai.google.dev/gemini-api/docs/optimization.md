---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=pt-BR
fetched_at: 2026-06-08T05:33:49.792492+00:00
title: "Otimiza\u00e7\u00e3o e infer\u00eancia da API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Otimização e inferência da API Gemini

A API Gemini oferece vários mecanismos de otimização para ajudar você a equilibrar velocidade, custo e confiabilidade com base nas necessidades específicas da carga de trabalho.
Se você estiver criando bots conversacionais em tempo real ou executando pipelines de processamento de dados off-line pesados, escolher o paradigma certo pode reduzir significativamente os custos ou aumentar a performance.

| Recurso | Padrão | Flex | Prioridade | Lote | Armazenamento em cache |
| --- | --- | --- | --- | --- | --- |
| **Preços** | Preço total | 50% de desconto | 75% a 100% a mais do que o padrão | 50% de desconto | 90% de desconto + armazenamento de tokens proporcional |
| **Latência** | Segundos a minutos | Minutos (1 a 15 min de destino) | Segundos | Até 24 horas | Tempo até o primeiro token mais rápido |
| **Confiabilidade** | Alta / média-alta | Melhor esforço (descartável) | Alta (não descartável) | Alta (para capacidade de processamento) | N/A |
| **Interface** | Síncrona | Síncrona | Síncrona | Assíncrona | Estado salvo |
| **Melhor caso de uso** | Fluxos de trabalho de aplicativos gerais | Cadeias sequenciais não urgentes | Apps de produção voltados ao usuário | Conjuntos de dados massivos, avaliações off-line | Consultas recorrentes no mesmo arquivo |

## Níveis de serviço de inferência (síncrono)

É possível alternar entre o tráfego síncrono otimizado para confiabilidade e o otimizado para custos transmitindo o parâmetro `service_tier` nas chamadas de geração padrão.

### Inferência padrão (padrão)

O nível padrão é a opção padrão para geração de conteúdo sequencial.
Ele oferece tempos de resposta normais sem prêmios extras ou filas pesadas.

- **Confiabilidade**:criticidade padrão
- **Preço**:preços padrão.
- **Ideal para**:a maioria dos aplicativos interativos do dia a dia.

### Inferência de prioridade (otimizada para latência)

[O processamento de](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)prioridade encaminha suas solicitações
para filas de computação de alta criticidade.
Esse tráfego é estritamente não descartável (nunca substituído por outros níveis) e oferece a maior confiabilidade. Se você exceder os limites de prioridade dinâmica, o sistema vai fazer o downgrade da solicitação para o processamento padrão em vez de falhar com um erro.

- **Confiabilidade**:maior criticidade
- **Preço**:75% a 100% acima das taxas padrão.
- **Ideal para**:chatbots de clientes, detecção de fraudes em tempo real e copilotos essenciais para os negócios.

### Inferência flexível (otimizada para custos)

[A inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br) oferece um desconto de 50% em comparação com as taxas padrão, utilizando
capacidade de computação oportunista fora do horário de pico. As solicitações são processadas de forma síncrona, o que significa que não é necessário reescrever o código para gerenciar objetos em lote.
Como é um tráfego "descartável", as solicitações podem ser substituídas se o sistema tiver picos de tráfego padrão.

- **Confiabilidade**:criticidade não garantida e descartável
- **Preço**:50% do preço padrão (cobrado por token).
- **Ideal para**:fluxos de trabalho de agentes de várias etapas em que a chamada N+1 depende da saída da chamada N, atualizações de CRM em segundo plano e avaliações off-line.

## API Batch (em massa, assíncrona)

[A API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br) foi projetada para processar grandes volumes
de solicitações de forma assíncrona a
50% do custo padrão. É possível enviar solicitações como dicionários inline ou usando um arquivo de entrada JSONL (até 2 GB). Ele processa solicitações usando filas de capacidade de processamento em segundo plano com um tempo de resposta de 24 horas.

- **Confiabilidade**:descartável, mas com novas tentativas automatizadas de 24 horas e sistema de filas
- **Preço**:50% do preço padrão.
- **Ideal para**:pré-processamento de conjuntos de dados massivos, execução de conjuntos de testes de regressão periódicos e gerações de imagens ou incorporações de alto volume.

## Armazenamento em cache de contexto (economia de entrada)

[O armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) é usado quando um contexto inicial substancial
é referenciado repetidamente por solicitações mais curtas.

- **Armazenamento em cache implícito**:ativado automaticamente no Gemini 2.5 e em modelos mais recentes.
  O sistema transmite economias de custos se a solicitação atingir caches atuais com base em prefixos de comandos comuns.
- **Armazenamento em cache explícito**:é possível criar manualmente um objeto de cache com um tempo de vida (TTL) específico. Depois de criado, você se refere aos tokens armazenados em cache para solicitações subsequentes para evitar a transmissão repetida do mesmo payload do corpus.
- **Preço**:cobrado com base na contagem de tokens de cache e na duração do armazenamento (TTL).
- **Ideal para**:chatbots com instruções abrangentes do sistema, análise repetitiva de arquivos de vídeo longos ou consultas em grandes conjuntos de documentos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
