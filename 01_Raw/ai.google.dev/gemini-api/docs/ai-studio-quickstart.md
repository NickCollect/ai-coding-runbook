---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ko
fetched_at: 2026-06-08T05:33:31.013115+00:00
title: "Google AI \uc2a4\ud29c\ub514\uc624 \ube60\ub978 \uc2dc\uc791 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google AI 스튜디오 빠른 시작

[Google AI Studio](https://aistudio.google.com/?hl=ko)를 사용하면
모델을 바로 사용해 보고 다양한 프롬프트를 실험할 수 있습니다. 빌드할 준비가 되면
'코드 가져오기'와 원하는 프로그래밍 언어를 선택하여
[Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)를 사용할 수 있습니다.

## 프롬프트 및 설정

Google AI Studio는 다양한 사용 사례를 위해 설계된 여러 프롬프트 인터페이스를 제공합니다. 이 가이드에서는 **채팅 프롬프트**를 다룹니다. 이 프롬프트는
대화형 환경을 빌드하는 데 사용됩니다. 이 프롬프트 기법을 사용하면 여러 입력
및 응답 턴을 통해 출력을 생성할 수 있습니다. 아래의
[채팅 프롬프트 예시를 통해 자세히 알아보세요](#chat_example).
다른 옵션으로는 **실시간 스트리밍**, **동영상 생성** 등이 있습니다.

[[[[[[AI Studio는 모델 매개변수, 안전 설정, 구조화된 출력, 함수 호출, 코드 실행, 그라운딩과 같은 도구를 전환할 수 있는 **실행 설정** 패널도 제공합니다.](https://ai.google.dev/docs/prompting-strategies?hl=ko#model-parameters)](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko)](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)](https://ai.google.dev/gemini-api/docs/grounding?hl=ko)

## 채팅 프롬프트 예시: 맞춤 채팅 애플리케이션 빌드

[Gemini](https://gemini.google.com/?hl=ko) 이러한 범용 챗봇은 유용하지만 특정 사용 사례에 맞게 조정해야 하는 경우가 많습니다.

예를 들어 회사의 제품에 관해 이야기하는 대화만 지원하는 고객 서비스 챗봇을 빌드할 수 있습니다. 특정 어조나 스타일로 말하는 챗봇, 즉 농담을 많이 하거나 시인처럼 운율을 맞추거나 답변에 이모티콘을 많이 사용하는 봇을 빌드할 수 있습니다.

이 예시에서는 Google AI Studio를 사용하여 목성의 위성 중 하나인 유로파에 사는 외계인처럼 소통하는 친근한 챗봇을 빌드하는 방법을 보여줍니다.

### 1단계 - 채팅 프롬프트 만들기

챗봇을 빌드하려면 모델이 원하는 응답을 제공하도록 안내하기 위해 사용자와 챗봇 간의 상호작용 예시를 제공해야 합니다.

채팅 프롬프트를 만들려면 다음 단계를 따르세요.

1. [Google AI Studio](https://aistudio.google.com/?hl=ko)를 엽니다. 새 채팅 프롬프트와 함께 **Playground** 가 기본적으로 열립니다.
2. 오른쪽 상단에 있는 **실행 설정** tune을 클릭하여 패널을 펼치고 [**시스템 요청 사항**](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#system-instructions) 입력란을 찾습니다. 텍스트 입력란에 다음을 붙여넣습니다.

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

시스템 요청 사항을 추가한 후 모델과 채팅하여 애플리케이션 테스트를 시작합니다.

1. **무언가 입력하세요...**라는 텍스트 입력 상자에 사용자가 할 수 있는 질문이나 관찰 내용을 입력합니다. 예를 들면 다음과 같습니다.

   **사용자:**

   ```
   What's the weather like?
   ```
2. **실행** 버튼을 클릭하여 챗봇의 응답을 가져옵니다. 이 응답은 다음과 같이 표시될 수 있습니다.

   **모델:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### 2단계 - 봇이 더 잘 채팅하도록 학습시키기

단일 안내를 제공하여 기본적인 유로파 외계인 챗봇을 빌드할 수 있었습니다. 하지만 모델 응답의 일관성과 품질을 보장하기에는 단일 안내가 충분하지 않을 수 있습니다. 더 구체적인 안내가 없으면 날씨에 관한 질문에 대한 모델의 응답이 매우 길어지고 자체적으로 판단할 수 있습니다.

시스템 요청 사항에 추가하여 챗봇의 어조를 맞춤설정합니다.

1. 새 채팅 프롬프트를 시작하거나 동일한 프롬프트를 사용합니다. 채팅 세션이 시작된 후에는 시스템 요청 사항을 수정할 수 있습니다.
2. **시스템 요청 사항** 섹션에서 기존 안내를 다음과 같이 변경합니다.

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. 질문 (`What's the weather like?`)을 다시 입력하고 **실행**
   버튼을 클릭합니다. 새 채팅을 시작하지 않은 경우 응답이 다음과 같이 표시될 수 있습니다.

   **모델:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

이 접근 방식을 사용하여 챗봇에 추가적인 깊이를 더할 수 있습니다. 더 많은 질문을 하고, 답변을 수정하고, 챗봇의 품질을 개선합니다. 안내를 계속 추가하거나 수정하고 챗봇의 동작을 어떻게 변경하는지 테스트합니다.

### 3단계 - 다음 단계

다른 프롬프트 유형과 마찬가지로 프롬프트 프로토타입이 만족스러우면 **코드 가져오기** 버튼을 사용하여 코딩을 시작하거나 나중에 작업하고 다른 사용자와 공유할 수 있도록 프롬프트를 저장할 수 있습니다.

## 추가 자료

- 코드로 이동할 준비가 되었다면 [API
  빠른 시작](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)을 참고하세요.
- 더 나은 프롬프트를 작성하는 방법을 알아보려면 [프롬프트 디자인
  가이드라인](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)을 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-12(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-12(UTC)"],[],[]]
