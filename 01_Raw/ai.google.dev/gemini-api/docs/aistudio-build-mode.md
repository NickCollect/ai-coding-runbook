---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-BR
fetched_at: 2026-06-29T05:39:42.991570+00:00
title: "Criar apps no Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Criar apps no Google AI Studio

Esta página descreve como usar o Google AI Studio para criar (ou "vibe
code") e implantar rapidamente apps que testam os recursos mais recentes do Gemini, como o
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) e a [API
Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br). O Google AI Studio permite criar **apps da Web** com ambientes de execução full stack e **apps Android nativos** com Kotlin e Jetpack Compose, tudo isso usando comandos em linguagem natural.

## Primeiros passos

Comece a programar no [modo de criação](https://aistudio.google.com/apps?hl=pt-br) do Google AI Studio. Você pode
começar a criar de algumas maneiras:

- **Comece com um comando**: no modo de criação, use a caixa de entrada para inserir uma descrição do que você quer criar. Selecione "Chips de IA" para adicionar recursos específicos, como geração de imagens ou dados do Google Maps, ao seu comando. Você pode
  até dizer o que quer usando o botão de conversão de voz em texto.
- **Botão "Estou com sorte"**: se você precisar de uma faísca de criatividade, use o botão "Estou com sorte". O Gemini vai gerar um comando com uma ideia de projeto para você começar.
- **Remixar um projeto da galeria**: abra um projeto na [Galeria de
  apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br) e selecione **Copiar app**.

Depois de executar o comando, o código e os arquivos necessários serão gerados, com uma prévia em tempo real do seu app aparecendo no lado direito.

## O que é criado?

Quando você executa o comando, o AI Studio cria um aplicativo completo. Você pode
criar um **app da Web** ou um **app Android nativo** usando o seletor
de plataforma.

Para **apps da Web** (padrão), o AI Studio cria um ambiente full stack que inclui:

- **Do lado do cliente**: um front-end da Web (o React é o padrão).
- **Do lado do servidor**: um ambiente de execução do Node.js que permite chamadas de API seguras, conexões de banco de dados e uso de pacotes npm.

Para **apps Android**, o AI Studio gera um projeto em Kotlin e Jetpack Compose que pode ser visualizado em um emulador baseado em navegador, instalado em um dispositivo físico e publicado na Google Play Store para testes. [Saiba mais sobre como criar apps
Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br).

Para ver o código gerado, selecione a guia **Código** no painel de visualização à direita. O **Antigravity Agent** gerencia de forma inteligente
vários arquivos em toda a sua pilha, garantindo que as mudanças sejam propagadas
corretamente.

### O agente do Antigravity

O **Agente Antigravity** é a principal funcionalidade de IA no [Google Antigravity](https://antigravity.google?hl=pt-br). Agora, os componentes principais do conector do agente estão alimentando a experiência do modo de criação no Google AI Studio. Ele vai além da simples geração de código, mantendo o contexto de todo o projeto, gerenciando vários arquivos e entendendo instruções complexas para criar aplicativos full-stack robustos.

As principais capacidades incluem:

- **Consciência de contexto**: mantém o contexto de comandos e estados de arquivos anteriores.
- **Gerenciamento de vários arquivos**: processa dependências em vários arquivos.
- **Execução verificada**: verifica atualizações de código para reduzir alucinações.

## Recursos de pilha completa

O Google AI Studio libera o poder do ecossistema da Web moderna, permitindo que você crie mais do que apenas protótipos do lado do cliente.

- **Tempo de execução do lado do servidor e npm**: use a vasta biblioteca de pacotes npm. O
  agente vai identificar e instalar automaticamente os pacotes conforme necessário para seu
  app (por exemplo, bibliotecas específicas para visualização de dados ou clientes de API). Você
  também pode solicitar pacotes específicos, se quiser.
- **Gerenciamento de secrets**: armazene chaves de API e secrets com segurança no menu **Configurações**. Eles ficam acessíveis no código do lado do servidor, protegendo-os contra exposição do lado do cliente.
- **Multiplayer**: crie experiências colaborativas em tempo real diretamente no AI Studio. O ambiente de execução do lado do servidor gerencia o estado e as conexões necessárias
  para que os usuários interajam entre si.
- **Firebase Firestore e Authentication**: provisiona e configura automaticamente o Firebase,
  incluindo o banco de dados do Firestore (armazenamento de dados persistentes) e
  o Firebase Authentication (fluxos de login, especificamente "Fazer login com o Google").
  O agente gerencia todo o processo de configuração e até mesmo escreve o código no seu
  app para esses serviços.
- **Integrações com o Google Workspace**: conecte seu app às APIs do Google Workspace, como Gmail, Planilhas, Documentos, Drive, Agenda e muito mais. O AI Studio processa
  toda a configuração do OAuth automaticamente.

[Saiba mais sobre o desenvolvimento de apps full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br)

### Apps Android

Você também pode criar apps Android nativos usando Kotlin e Jetpack Compose.
Visualize o app em um emulador do Android baseado em navegador, instale-o em um dispositivo físico usando o adb no navegador e publique na Google Play Store para testes internos.

[Saiba mais sobre como criar apps Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br)

## Continuar criando

Depois que o Google AI Studio gerar o código inicial do seu aplicativo, você poderá continuar refinando-o:

### Crie no Google AI Studio

- **Iterar com o Gemini**: use o painel de chat no **Modo de criação** para pedir ao Gemini
  que faça modificações, adicione novos recursos ou mude o estilo.
- **Edite o código diretamente**: abra a **guia "Código"** no painel de visualização para
  fazer edições em tempo real.

### Desenvolver externamente

Para fluxos de trabalho mais avançados, exporte o código e trabalhe no ambiente de sua preferência:

- **Baixar e desenvolver localmente**: exporte o código gerado como um **arquivo
  ZIP** e importe-o para seu editor de código.
- **Enviar para o GitHub**: integre o código aos seus processos de desenvolvimento e
  implantação atuais enviando-o para um **repositório do GitHub**.

## Principais recursos

O Google AI Studio inclui vários recursos para tornar o processo de criação
intuitivo e visual:

- **Crie e itere em apps de pilha completa**: crie apps de pilha completa com apenas um comando e itere no chat ou no **modo de anotação**. O modo de anotação
  permite destacar qualquer parte da interface do app e descrever a
  mudança desejada.
- **Compartilhe e implante seu app**: você pode compartilhar suas criações com outras pessoas para
  colaborar ou mostrar seu trabalho. Ao compartilhar, as chamadas de API são contabilizadas nos seus limites de uso. Se você usar modelos pagos, poderão ser aplicadas cobranças. Depois, quando o app estiver
  pronto, implante no Cloud Run.
- **Galeria de apps**: a galeria de apps oferece uma biblioteca visual de ideias de projetos.
  Você pode navegar pelas possibilidades do Gemini, testar aplicativos instantaneamente e
  fazer remix para criar algo seu.

## Implantar ou arquivar o app

Quando o aplicativo estiver pronto, você poderá implantá-lo:

- **Cloud Run**: implante seu aplicativo como um serviço escalonável.
  Os preços do [Google Cloud Run](https://cloud.google.com/run?hl=pt-br) podem ser aplicados com base no uso. Para saber mais sobre a implantação, consulte
  [Implantar no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br).
- **GitHub**: exporte seu projeto para um repositório do GitHub.

## Limitações

Esta seção lista as limitações atuais do modo de criação no Google AI Studio.

### Gerenciamento de chaves de API

Quando você cria um app que usa a API Gemini, o AI Studio configura automaticamente
sua chave de API Gemini como um segredo no ambiente do lado do servidor do app.
Você pode ver e gerenciar essa chave no painel **Secrets**.

- **Configuração automática**: seu `GEMINI_API_KEY` é configurado para você. Não é necessário fazer configurações manuais para começar a criar.
- **Somente do lado do servidor**: as chaves de API são injetadas no tempo de execução do lado do servidor e nunca são incluídas no código do lado do cliente.
- **Apps atuais**: para apps criados antes de 14 de maio de 2026, o agente vai
  atualizar automaticamente a integração da API Gemini para a abordagem
  recomendada do lado do servidor na próxima vez que você modificar os recursos do Gemini no app.

### Implantação fora do Google AI Studio

- **Cloud Run**: quando você implanta no Cloud Run pelo AI Studio, a chave de API é
  incluída com segurança no ambiente do lado do servidor. O app implantado vai usar
  sua chave de API para todas as chamadas da API Gemini dos usuários.
- **Download do ZIP**: se você baixar o app como um arquivo ZIP para executá-lo
  em outro lugar, será necessário configurar a variável de ambiente `GEMINI_API_KEY`
  no ambiente de hospedagem. Como as chamadas da API Gemini do seu app são feitas com
  código do lado do servidor, a chave não é exposta aos usuários finais.

### Erro ao compartilhar apps

Se você compartilhar o app e o usuário final encontrar um erro **403 Acesso restrito**
ao usar o URL compartilhado, isso pode ser devido a um dos seguintes motivos:

- **Extensões do navegador**: extensões de privacidade, como o Privacy Badger, podem estar bloqueando o app. Desative a extensão para evitar o erro.
- **Problemas de build**: pode haver problemas com o código atual. Peça ao
  agente para "corrigir problemas de build com o código atual" e compartilhe o
  URL novamente.

## Perguntas frequentes

### O que é o recurso "Criar no AI Studio"?

O AI Studio Build é uma plataforma criada para transformar um comando simples em um aplicativo pronto para produção e com tecnologia de IA usando o Gemini. Descreva o que você quer criar com um comando, e o Gemini vai gerar um app para você. Você também pode acessar nossa galeria para conferir o que é possível fazer com a API Gemini e remixar apps para personalizar.

### Como o Build trata minha chave da API Gemini?

Quando você cria um app que usa a API Gemini, o AI Studio configura automaticamente
sua chave de API Gemini como um segredo do lado do servidor. As chamadas da API Gemini do seu app são feitas com código do lado do servidor usando essa chave. Portanto, ela nunca é exposta no navegador. É possível conferir sua chave de API no painel **Secrets** em
Configurações.

### Minha chave de API fica exposta ao compartilhar apps?

Não. Sua chave de API é armazenada como um secret do lado do servidor e nunca é incluída no código do lado do cliente. Quando você compartilha seu app, outros usuários podem usá-lo, mas não podem ver sua chave de API.

Ao compartilhar seus apps com outras pessoas, as chamadas de API contam para seus limites de uso.
Se você usar modelos pagos, poderão ser aplicadas cobranças. O AI Studio vai avisar durante a configuração e antes do compartilhamento se o app pode gerar custos.

### Quem pode ver meus apps?

Por padrão, seu app é particular. Você pode compartilhar seu app com outros usuários para
que eles possam usá-lo. Os usuários com quem você compartilha seu app podem ver e bifurcar o código
para fins próprios. Se você compartilhar seu app com permissão de edição, os
outros usuários poderão editar o código dele.

### Posso executar apps fora do AI Studio?

Sim. É possível implantar seu app no
[Cloud Run](https://cloud.google.com/run?hl=pt-br) pelo AI Studio, o que
dá ao app um URL público com sua chave de API configurada com segurança no
ambiente do lado do servidor. Você também pode baixar o app como um arquivo ZIP e
hospedá-lo em outro lugar. Para isso, defina a variável de ambiente `GEMINI_API_KEY` no ambiente
de hospedagem. Como as chamadas da API Gemini são feitas no código do lado do servidor, sua chave permanece segura.

Para saber mais sobre as opções de implantação, consulte [Implantar do Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br).

### Posso desenvolver apps localmente com minhas próprias ferramentas e depois compartilhá-los aqui?

Essa funcionalidade ainda não está disponível. Estamos animados para oferecer suporte a mais casos de uso de apps no futuro. Envie feedback se tiver algo específico em mente.

### Como posso usar um banco de dados ou outro armazenamento com meus apps?

Os apps do AI Studio são apps padrão executados em um contêiner do Cloud Run. Você pode usar qualquer solução de armazenamento que possa ser conectada por uma rede, desde que não haja um firewall impedindo o acesso de um intervalo de IP dinâmico.

Estamos trabalhando para adicionar suporte direto ao armazenamento no futuro, que você poderá configurar diretamente no AI Studio.

### Como posso acessar o microfone, a webcam e outras APIs do navegador?

Para garantir que os espectadores estejam cientes do uso da webcam ou de outros dispositivos por um app, exigimos uma confirmação extra antes que o app possa acessar essas [APIs Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Os criadores de apps podem adicionar essas solicitações de permissão ao arquivo
`metadata.json` do app. Exemplo:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Os valores aceitos para `requestFramePermissions` são um subconjunto dos [recursos padrão controlados por política](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Como posso usar o GitHub com meus apps?

Com a integração do GitHub no AI Studio, você pode criar um repositório para seu
trabalho e confirmar as mudanças mais recentes. No momento, não é possível extrair mudanças remotas.

### Posso dar acesso de edição do meu app a outros usuários?

Ainda não há suporte para isso, mas o recurso será lançado em breve.

### Por que meu app foi sinalizado por violação da política?

Temos sistemas que analisam automaticamente os apps para garantir que eles obedeçam às nossas políticas. Se descobrirmos que um app viola nossas políticas, ele será removido do AI Studio. As violações de política podem incluir, entre outros:

- Apps que contêm malware, phishing ou falsificação de identidade
- Apps que mostram ou distribuem conteúdo que viola a política sobre imagens de abuso sexual infantil
- Apps que mostram ou distribuem conteúdo que viola a política contra assédio
- Apps que mostram ou distribuem conteúdo que viola a política contra discurso de ódio
- Apps que mostram ou distribuem conteúdo que viola a política contra tráfico de pessoas
- Apps que mostram ou distribuem conteúdo que viola a política contra conteúdo sexualmente explícito
- Apps que mostram ou distribuem conteúdo que viola a política contra violência e imagens sangrentas
- Apps que mostram ou distribuem conteúdo que viola a política contra conteúdo nocivo ou perigoso

Se o app foi sinalizado por violação de política e você acredita que houve um erro, envie uma contestação. Violações recorrentes das nossas políticas podem resultar no encerramento do seu acesso ao AI Studio.

### Quais são minhas responsabilidades como desenvolvedor de apps?

Como proprietário do aplicativo, você é responsável pelo comportamento dele e por todos os dados que ele processa. Isso inclui:

- **Conformidade legal e direitos de terceiros**:garantir que seu app esteja em conformidade com todas as leis e regulamentações aplicáveis e não viole os direitos de outras pessoas, incluindo direitos de propriedade intelectual e direitos de privacidade.
- **Monitoramento de conteúdo**:a conformidade com termos adicionais pode se aplicar a outros serviços usados pelo seu app. Por exemplo, os [Termos de Serviço do Google Cloud](https://cloud.google.com/terms?hl=pt-br), aplicáveis ao Firestore, exigem que os clientes que hospedam conteúdo de terceiros publiquem políticas que definam o que é proibido (por exemplo, conteúdo ilegal) e monitorem a presença desse conteúdo.
- **Implementação segura**:implemente as proteções e ferramentas de moderação necessárias para evitar o uso indevido do aplicativo.

Conheça as [restrições de uso](https://ai.google.dev/gemini-api/terms?hl=pt-br#use-restrictions) nos Termos de Serviço.

### Quais termos se aplicam aos apps na galeria de apps do AI Studio?

Os [Termos Adicionais de Serviço da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br)
se aplicam ao uso dos apps mostrados na Galeria de Apps do AI Studio, a menos que
indicado de outra forma.

## A seguir

- [Desenvolvimento de apps de pilha completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br) (Web)
- [Criar apps Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br)
- Confira exemplos na [Galeria de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-19 UTC."],[],[]]
