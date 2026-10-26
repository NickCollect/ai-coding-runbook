---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-BR
fetched_at: 2026-10-26T05:55:11.540543+00:00
title: "Criar apps Android no Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Criar apps Android no Google AI Studio

Com o Google AI Studio, você pode criar apps Android nativos usando um comando em linguagem natural. Descreva o app que você quer, e o
[agente do Antigravity](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-br#antigravity-agent)
vai gerar um projeto completo em Kotlin e
[Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=pt-br). No navegador, é possível visualizar o app em um Android Emulator baseado em navegador, instalá-lo em um dispositivo físico e publicá-lo para teste.

Os apps Android também são compatíveis com a [integração do Firebase](#firebase-integration) para
chamar modelos do Gemini com a Lógica de IA do Firebase e o App Check, armazenar dados no
Cloud Firestore e fazer login de usuários com o Firebase Authentication.

## Primeiros passos

Para começar a criar um app Android:

1. Acesse o [Modo de criação](https://aistudio.google.com/apps?hl=pt-br) no Google AI Studio usando o painel de navegação à esquerda.
2. Selecione **Android** no seletor de plataforma.
3. Insira um comando descrevendo o app que você quer criar (por exemplo, *"Crie um
   rastreador de tarefas diárias com armazenamento local"* ou *"Crie um app de receitas que use IA
   para sugerir refeições com base em ingredientes"*).
4. O agente gera o projeto e o inicia no Android Emulator baseado em navegador.

Em seguida, é possível iterar no app usando o painel de chat, assim como na experiência
da Web. O agente gerencia todos os arquivos no seu projeto do Android e propaga
as mudanças na base de código.

## Integração com o Firebase

O Google AI Studio se integra ao
[Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=pt-br)
para que seu app Android possa chamar modelos do Gemini com segurança, manter dados e
autenticar usuários sem um back-end personalizado do lado do servidor. Quando você pede ao
agente para criar recursos que exigem IA generativa, um banco de dados ou login, ele
pode provisionar e configurar automaticamente os seguintes serviços no seu
projeto do Firebase:

- **[Firebase AI Logic](https://firebase.google.com/docs/ai-logic?hl=pt-br) e
  [App Check do Firebase](https://firebase.google.com/docs/ai-logic/app-check?hl=pt-br)**:
  chame modelos do Gemini diretamente do seu app Android sem incorporar chaves de API
  brutas no APK. O AI Studio configura automaticamente o App Check para verificar se
  as solicitações são originadas de uma instância autêntica do seu app:
  - **Teste e compartilhamento (builds de depuração)**: usa um token de depuração do App Check
    gerenciado automaticamente pelo AI Studio ao visualizar no emulador baseado em navegador,
    instalar por USB ou compartilhar com testadores.
  - **Publicação no Google Play (builds de lançamento)**: muda automaticamente
    para o reCAPTCHA Enterprise usando uma chave de site pré-configurada ao criar uma
    versão de lançamento para o Google Play.
- **Cloud Firestore**: armazene e sincronize dados em um banco de dados NoSQL na nuvem,
  incluindo regras de segurança do Firestore geradas automaticamente
  (`firestore.rules`).
- **Firebase Authentication**: adicione fluxos de "Fazer login com o Google" para autenticar
  usuários.

É possível ativar o Firebase no card de configuração que aparece no chat quando você
solicita esses recursos ou a qualquer momento em **Configurações > Integrações**. Para
detalhes sobre a configuração do projeto, cotas compartilhadas e o ciclo de vida do App Check, consulte
[Adicionar o Firebase ao seu app do Google AI
Studio](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=pt-br).

## Android Emulator baseado em navegador

O Android Emulator é executado inteiramente na nuvem e transmitido para seu navegador.
Não é necessário instalar o SDK do Android, o Android Studio ou um emulador local.

O emulador oferece:

- **Simulação de dispositivo semelhante ao Pixel**: toque, role e interaja com o app
  como em um dispositivo real.
- **Suporte à rotação**: alterne entre as orientações retrato e paisagem.
- **Prévia em tempo real**: quando o agente faz mudanças no código, o app é recriado e
  o emulador é atualizado automaticamente.

### Limitações do emulador

O emulador baseado em navegador não é compatível com todos os recursos de hardware. Os seguintes
recursos não estão disponíveis no emulador:

- Captura de fotos e câmera
- NFC e Bluetooth
- GPS (localização simulada)
- Google Play Services (o Login do Google, o Maps e outros recursos do Google Play Services
  funcionam em um dispositivo real, mas não no emulador)

## Instalar em um dispositivo com ADB

É possível instalar o APK criado diretamente em um dispositivo Android físico conectado
ao computador por USB. Isso usa o
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=pt-br) para
se comunicar com o dispositivo pelo navegador. Não é necessário instalar o ADB localmente.

### Pré-requisitos

- Um navegador Chrome ou Edge compatível com WebUSB.
- Um dispositivo Android com as
  [Opções do desenvolvedor e a depuração USB](https://developer.android.com/studio/debug/dev-options?hl=pt-br)
  ativadas.
- Um cabo USB conectando o dispositivo ao computador.

### Instalar o app no dispositivo

1. Clique em **Instalar no dispositivo** no painel de visualização.
2. Selecione o dispositivo Android no seletor de dispositivos USB do navegador.
3. O APK será transferido e instalado no dispositivo.
4. O app é iniciado automaticamente.

## Publicar na Google Play Store

É possível publicar seu app Android na faixa de teste interno do [Google Play Console](https://play.google.com/console?hl=pt-br), que permite distribuir o app para até 100 testadores.

### Pré-requisitos

- Uma [conta de desenvolvedor do Google Play](https://play.google.com/console/signup?hl=pt-br)
  (requer uma taxa de registro única de US $25).
- Um perfil de desenvolvedor preenchido no Play Console.

### Publicar o app

1. Abra **Configurações > Publicar** no Google AI Studio.
2. Clique em **Publicar na Play Store**.
3. Autentique-se com sua conta de desenvolvedor do Google Play.
4. O AI Studio assina o APK, cria a página de detalhes do app (ou faz upload de uma nova versão)
   e publica na faixa de teste interno.
5. Você vai receber um link para compartilhar com os testadores.

O AI Studio gerencia a assinatura de APKs automaticamente usando um keystore gerenciado. É possível
personalizar a página de detalhes do app (ícone, capturas de tela, descrição) mais tarde no Play
Console.

## O que é gerado

Quando você cria um app Android, o agente gera um projeto padrão baseado no Gradle
com a seguinte estrutura:

- **Configuração do build**: arquivos `build.gradle.kts` (nível do projeto e do app)
  usando a DSL do Kotlin.
- **Camada de interface**: componentes do [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=pt-br)
  com temas do [Material 3](https://m3.material.io/).
- **Arquitetura**: arquitetura de atividade única com ViewModels e classes de dados.
- **Recursos**: `AndroidManifest.xml`, drawables, strings e outros recursos do Android.
- **Configuração do Firebase** (quando o Firebase está ativado):
  `google-services.json`, `firebase_applet_config.xml` e `firestore.rules`.

O agente gerencia automaticamente as dependências do Gradle, adicionando pacotes dos repositórios do Maven
e do Google conforme necessário.

É possível visualizar e editar o código gerado usando a guia **Código** no painel de
pré-lançamento. Para continuar o desenvolvimento no Android Studio, faça o download do projeto como um
**arquivo ZIP**.

## Limitações

A criação de apps Android no AI Studio tem as seguintes limitações:

### Limitações da plataforma

- **Somente do lado do cliente**: os apps Android não incluem um componente do lado do servidor.
  Os recursos que exigem um ambiente de execução do servidor (gerenciamento de secrets, multijogador,
  APIs do Google Workspace) não estão disponíveis.
- **Arquitetura de atividade única**: apenas projetos de atividade única e módulo único
  são compatíveis.
- **Somente Jetpack Compose**: os apps usam Kotlin e Jetpack Compose. Layouts Java e
  XML não são compatíveis.
- **Sem NDK ou código nativo**: não há suporte para código C e C++.
- **Sem Wear OS ou Android TV**: apenas os formatos de smartphone e tablet são
  compatíveis.

### Limitações de exportação

- **Somente download de ZIP**: é possível baixar o projeto como um arquivo ZIP. A exportação para o GitHub
  ainda não está disponível para projetos do Android.

## A seguir

- [Criar apps no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-br)
- [Desenvolvimento de apps de pilha completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br) (Web)
- Confira exemplos na [Galeria de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-20 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-20 UTC."],[],[]]
