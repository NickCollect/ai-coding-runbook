---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=pt-BR
fetched_at: 2026-06-15T06:26:41.661764+00:00
title: "Pr\u00e1ticas recomendadas da API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Práticas recomendadas da API Live

Este guia aborda as práticas recomendadas que você pode seguir para otimizar o uso da API Live.
Consulte a página [Introdução à API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br)
para conferir uma visão geral e exemplos de código para casos de uso comuns.

## Criar instruções claras do sistema

Para ter o melhor desempenho da API Live, recomendamos ter um conjunto de instruções do sistema (SIs, na sigla em inglês) bem definido que defina o perfil do agente, as regras de conversação e as barreiras de proteção, nessa ordem.

Para melhores resultados, separe cada agente em uma SI distinta.

1. **Especificar o perfil do agente**:forneça detalhes sobre o nome, a função e as características preferidas do agente. Se você quiser especificar o sotaque, também especifique o idioma de saída preferido (por exemplo, um sotaque britânico para um falante de inglês).
2. **Especificar as regras de conversação**:coloque essas regras na ordem em que você espera que o modelo siga. Delimite entre elementos únicos da conversa e loops de conversação. Por exemplo:

   - **Elemento único**:colete os detalhes de um cliente uma vez (como nome, local, número do cartão fidelidade).
   - **Loop de conversação**:o usuário pode discutir recomendações, preços, devoluções e entrega, e pode querer passar de um tópico para outro. Informe ao modelo que ele pode participar desse loop de conversação pelo tempo que o usuário quiser.
3. **Especificar chamadas de ferramentas em um fluxo em frases distintas**:por exemplo, se uma etapa única para coletar os detalhes de um cliente exigir a invocação de uma função `get_user_info`, você poderá dizer: *Sua primeira etapa é coletar informações do usuário. Primeiro, peça ao usuário que forneça o nome, o local e o número do cartão fidelidade. Em seguida,
   invoque `get_user_info` com esses detalhes.*
4. **Adicionar as barreiras de proteção necessárias**:forneça as barreiras de proteção conversacionais gerais que você não quer que o modelo faça. Você pode fornecer exemplos específicos de se *x* acontecer, você quer que o modelo faça *y*. Se você ainda não estiver recebendo o nível de precisão preferido, use a palavra *inequivocamente* para orientar o modelo a ser preciso.

## Definir ferramentas com precisão

Ao usar ferramentas com a API Live, seja específico nas definições de ferramentas.
Informe ao Gemini em quais condições uma chamada de ferramenta deve ser invocada. Para mais detalhes, consulte [Definições de ferramentas](#tool-definitions-example) em
a seção de exemplos.

## Criar comandos eficazes

- **Usar comandos claros**:forneça exemplos do que os modelos devem e não devem fazer nos comandos e tente limitar os comandos a um por perfil ou função por vez. Em vez de comandos longos e de várias páginas, considere usar o encadeamento de comandos. O modelo tem melhor desempenho em tarefas com chamadas de função única.
- **Fornecer comandos e informações iniciais**:a API Live espera a entrada do usuário antes de responder. Para que a API Live inicie a conversa, inclua um comando pedindo que ela cumprimente o usuário ou inicie a conversa. Inclua informações sobre o usuário para que a API Live personalize essa saudação.

## Especificar idioma

Para um desempenho ideal na `gemini-live-2.5-flash` em cascata da API Live, verifique se o `language_code` da API corresponde ao idioma falado pelo usuário.

Se a expectativa for que o modelo responda em um idioma diferente do inglês, inclua o seguinte como parte das instruções do sistema:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Streaming

Ao implementar áudio em tempo real, siga estas práticas recomendadas:

- **Tamanho do bloco e latência**: envie áudio em blocos de 20 ms a 40 ms.
- **Processamento de interrupção**: quando o usuário fala enquanto o modelo está respondendo,
  o servidor envia uma mensagem `server_content` com `"interrupted": true`. Você precisa descartar imediatamente o buffer de áudio do lado do cliente para evitar que o agente continue falando com o usuário.

## Gerenciamento de contexto

Use `ContextWindowCompressionConfig` para sessões longas, já que os tokens de áudio nativos se acumulam rapidamente (aproximadamente 25 tokens por segundo de áudio).

## Armazenamento em buffer do cliente

Não armazene em buffer o áudio de entrada significativamente (como 1 segundo) antes de enviar. Envie pequenos blocos (20 ms a 100 ms) para minimizar a latência.

## Reamostragem

Verifique se o aplicativo cliente reamostra a entrada do microfone (geralmente 44,1 kHz ou 48 kHz) para 16 kHz antes da transmissão.

## Gerenciamento de sessões

Siga estas diretrizes para processar o ciclo de vida da sessão e garantir uma experiência do usuário confiável:

- **Ativar a compactação da janela de contexto**:os tokens de áudio se acumulam a aproximadamente 25 tokens por segundo. Sem compactação, as sessões somente de áudio são limitadas a 15 minutos e as sessões de áudio e vídeo a 2 minutos. Ative
  [a compactação da janela de contexto](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-br#context-window-compression)
  para estender as sessões a uma duração ilimitada.
- **Implementar a retomada da sessão**:o servidor pode redefinir periodicamente a conexão WebSocket. Use
  [a retomada da sessão](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-br#session-resumption)
  para se reconectar sem perder o contexto. Mantenha o token de retomada mais recente das mensagens `SessionResumptionUpdate` e transmita-o como o identificador ao se reconectar. Os tokens de retomada são válidos por 2 horas após o término da última sessão.
- **Processar mensagens GoAway:** o servidor envia uma
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-br#goaway-message)
  antes de encerrar uma conexão. Ouça essa mensagem e use o campo `timeLeft` para concluir ou se reconectar antes que a conexão seja fechada.
- **Processar sinais generationComplete**:use a
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-br#generation-complete-message)
  mensagem para saber quando o modelo terminou de gerar uma resposta, para que o
  aplicativo possa atualizar a interface ou continuar com a próxima ação.

Para detalhes da implementação, consulte
[Gerenciamento de sessões](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=pt-br).

## Exemplos

Este exemplo combina as práticas recomendadas e
[as diretrizes para o design de instruções do sistema](#system-instruction-guidelines) para
orientar o desempenho do modelo como um coach de carreira.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Definições de ferramentas

Este JSON define as funções relevantes chamadas no exemplo de coach de carreira.
Para melhores resultados ao definir funções, inclua os nomes, as descrições, os parâmetros e as condições de invocação.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Preços e faturamento

A API Gemini Live é faturada estritamente pelo uso de tokens. Como a API Live mantém uma sessão WebSocket persistente, o faturamento segue um modelo de composição com base na janela de contexto ativa.

### A janela de contexto da sessão (custos compostos)

A API cobra por turno todos os tokens presentes na janela de contexto da sessão. Um "turno" é definido como uma entrada do usuário e a resposta correspondente do modelo.

- **Acúmulo**:a janela de contexto inclui novos tokens do turno atual e todos os tokens acumulados de turnos anteriores.
- **Refaturamento**:os tokens anteriores são reprocessados e contabilizados em cada novo turno, até o tamanho da janela de contexto configurada. À medida que uma sessão se estende, o custo por turno aumenta porque o histórico de conversas é reprocessado.

### Tokens de áudio e transcrições

A API Live é multimodal nativamente. Ela retém o histórico de conversas como tokens de áudio brutos para preservar a nuance e o tom acústico.

- **Faturamento de áudio**:a API cobra pelos tokens de áudio nativos acumulados na taxa de entrada de áudio padrão em cada turno.
- **Taxa extra de transcrição**:quando a transcrição de áudio para texto está ativada (`inputAudioTranscription` ou `outputAudioTranscription`), a API cobra por todos os tokens de texto gerados para transcrição na taxa de saída de token de texto, além dos custos padrão de token de áudio.

### Gerenciar custos com limites de contexto

Para evitar o crescimento ilimitado de custos em sessões longas, configure o tamanho da janela de contexto usando `contextWindowCompression`.

Ao definir um acionador de compactação (por exemplo, 25.000 tokens) e uma janela deslizante (por exemplo, 8.000 tokens), a API remove automaticamente os tokens mais antigos quando o limite é atingido. Em seguida, a API fatura os turnos subsequentes apenas pelo histórico retido e por novos tokens.

### Modo de áudio proativo

Quando o modo de áudio proativo está ativado, os tokens de entrada são cobrados durante todo o tempo em que a API Live está ouvindo, enquanto os tokens de saída só são cobrados quando a API responde.

- **Observação para o Gemini 3.1**:o modo de áudio proativo não é compatível com `gemini-3.1-flash-live-preview`. Para esse modelo, você só será cobrado pelo áudio quando estiver transmitindo a entrada ativamente.

Para informações detalhadas sobre preços, consulte a [página de preços da API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-01 UTC."],[],[]]
