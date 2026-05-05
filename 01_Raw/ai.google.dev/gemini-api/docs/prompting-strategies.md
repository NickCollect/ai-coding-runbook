---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko
fetched_at: 2026-05-05T20:42:12.912662+00:00
title: "\ud504\ub86c\ud504\ud2b8 \uc124\uacc4 \uc804\ub7b5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 프롬프트 설계 전략

*프롬프트 설계*는 언어 모델에서 정확하고 고품질의 응답을 유도하는 프롬프트 또는 자연어 요청을 만드는 프로세스입니다.

이 페이지에서는 Gemini AI 모델을 최대한 활용하기 위한 프롬프트 설계를 시작하는 데 필요한 기본 개념, 전략, 권장사항을 소개합니다.

## 주제별 프롬프트 가이드

더 구체적인 프롬프트 전략을 찾고 계신가요? 다음 주제에 관한 다른 프롬프트 작성 가이드를 확인하세요.

- [미디어 파일로 프롬프트하기](https://ai.google.dev/gemini-api/docs/files?hl=ko#prompt-guide)
- [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ko#imagen-prompt-guide) 및 [Gemini 네이티브 이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko#prompt-guide)을 사용한 이미지 생성 프롬프트
- [동영상 생성을 위한 프롬프트](https://ai.google.dev/gemini-api/docs/video?hl=ko#prompt-guide)

이 가이드에서 공유된 여러 개념을 대화형으로 보여주기 위한 [프롬프트 갤러리](https://ai.google.dev/gemini-api/prompts?hl=ko)에서 다른 샘플 프롬프트를 확인할 수 있습니다.

## 명확하고 구체적인 요청 사항

모델 동작을 효과적이고 효율적으로 맞춤설정하는 방법은 명확하고 구체적인 요청 사항을 제공하는 것입니다. 요청 사항은 질문, 단계별 작업 또는 사용자 경험과 사고방식을 매핑하는 것만큼 복잡한 형태로 제공될 수 있습니다.

### 입력

입력은 모델에서 응답을 제공하려는 프롬프트의 필수 텍스트입니다. 입력은 모델에서 답하는 질문(질문 입력), 모델에서 수행하는 태스크(태스크 입력), 모델에서 작업하는 항목(항목 입력) 또는 모델에서 완료하거나 계속하는 부분 입력(완료 입력)일 수 있습니다.

| **입력 유형** | **프롬프트** | **생성된 출력** |
| --- | --- | --- |
| 질문 | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| 작업 | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| 항목 | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### 부분 입력 완료

생성형 언어 모델은 고급 자동 완성 도구처럼 작동합니다. 부분 콘텐츠를 제공하면 모델은 나머지 콘텐츠나 해당 콘텐츠의 연속이라고 생각하는 것을 응답으로 제공할 수 있습니다. 이 경우 예시 또는 컨텍스트를 포함하면 모델이 이러한 예시 또는 컨텍스트를 고려할 수 있습니다.

다음 예시에서는 안내 및 항목 입력과 함께 프롬프트를 제공합니다.

|  |
| --- |
| **프롬프트:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **응답:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

모델이 예측한 대로 작동하지만 자연어로 안내를 작성하는 것이 어려울 수 있으며 모델의 해석에 많은 영향을 미칩니다.
예를 들어 레스토랑 메뉴에는 많은 항목이 포함되어 있을 수 있습니다. JSON 응답의 크기를 줄이기 위해 정렬되지 않은 항목을 생략하고 싶을 수 있습니다. 이 경우 예시 및 응답 프리픽스를 제공하여 모델이 이를 완료하게 할 수 있습니다.

|  |
| --- |
| **프롬프트:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **응답:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

'치즈버거'가 주문의 일부가 아니었기 때문에 출력에서 어떻게 제외되었는지 확인하세요.

프롬프트를 사용하여 간단한 JSON 응답 객체의 형식을 지정할 수 있지만, 대답에 더 복잡한 JSON 스키마를 지정할 때는 Gemini API의 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko) 기능을 사용하는 것이 좋습니다.

### 제약조건

프롬프트 읽기 또는 응답 생성에 대한 제약조건을 지정합니다. 모델에게 해야 할 일과 하지 말아야 할 일을 지시할 수 있습니다. 예를 들어 프롬프트에서 요약의 길이에 대한 제약 조건을 지정할 수 있습니다.

|  |
| --- |
| **프롬프트:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **응답:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### 대답 형식

응답 형식을 지정하는 요청 사항을 제공할 수 있습니다. 예를 들어 대답 형식을 표, 글머리기호 목록, 엘리베이터 피치, 키워드, 문장 또는 단락 형식으로 요청할 수 있습니다. 다음 시스템 요청 사항은 모델에 대답 시 더 대화형으로 작성하도록 지시합니다.

|  |
| --- |
| **시스템 요청 사항**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **프롬프트**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **응답:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### 완료 전략으로 대답 형식 지정

[완료 전략](#completion)은 응답의 형식을 지정하는 데 도움이 될 수도 있습니다.
다음 예시에서는 모델에 에세이 개요를 만들라는 프롬프트를 표시합니다.

|  |
| --- |
| **프롬프트:**    ``` Create an outline for an essay about hummingbirds. ```  **응답:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

프롬프트에 개요의 형식이 지정되지 않았고 모델이 자동으로 형식을 선택했습니다. 모델이 특정 형식으로 개요를 반환하기 위해서는 개요의 시작을 나타내는 텍스트를 추가하고, 시작한 패턴에 따라 모델이 이를 완료하도록 할 수 있습니다.

|  |
| --- |
| **프롬프트:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **응답:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## 제로샷 또는 퓨샷 프롬프트

프롬프트에 올바른 예시 모델을 보여주는 예시를 포함할 수 있습니다. 모델은 예시의 패턴과 관계를 식별한 후 응답을 생성할 때 이를 적용합니다. 몇 가지 예시가 포함된 프롬프트를 *퓨샷* 프롬프트라고 하며, 예시를 제공하지 않는 프롬프트를 *제로샷* 프롬프트라고 합니다. 퓨샷 프롬프트는 모델 응답의 형식 지정, 문구, 범위 지정 또는 일반적인 패턴을 규제하는 데 자주 사용됩니다. 모델이 초점을 좁히고 더 정확한 결과를 생성할 수 있도록 구체적이고 다양한 예시를 사용합니다.

프롬프트에는 항상 퓨샷 예시를 포함하는 것이 좋습니다. 퓨샷 예시가 없는 프롬프트는 효과적이지 않을 수 있습니다. 실제로 태스크를 보여주는 예시가 충분히 명확하다면 프롬프트에서 요청 사항을 삭제해도 됩니다.

다음 제로샷 프롬프트는 모델에 가장 적합한 설명을 선택하라고 요청합니다.

|  |
| --- |
| **프롬프트:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **응답:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

모델이 간결한 응답을 생성해야 하는 사용 사례의 경우 간결한 응답을 선호할 수 있도록 프롬프트에 예시를 포함할 수 있습니다.

다음 프롬프트는 간략한 설명을 선호하는 두 가지 예시를 제공합니다. 응답에서 모델은 이전과 마찬가지로 더 긴 설명 (`Explanation1`)이 아닌 더 짧은 설명 (`Explanation2`)을 선택하도록 모델에 예시를 통해 안내가 제공된 것을 볼 수 있습니다.

|  |
| --- |
| **프롬프트:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **응답:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### 최적의 예시 수

Gemini와 같은 모델은 종종 몇 가지 예시를 사용하여 패턴을 선택하지만, 최상의 결과를 얻기 위해 프롬프트에 제공할 예시 수에 대해 실험해야 할 수 있습니다. 하지만 너무 많은 예시를 포함하면 모델이 예시에 대한 응답에 [과적합](https://developers.google.com/machine-learning/glossary?hl=ko#overfitting)하게 될 수 있습니다.

### 일관된 형식

원치 않는 형식의 응답을 방지하기 위해 퓨샷 예시의 구조와 형식이 동일해야 합니다. 프롬프트에 퓨샷 예시를 추가하는 기본 목표 중 하나는 모델에 응답 형식을 보여주는 것입니다. 따라서 모든 예시에서 일관된 형식을 보장하는 것이 중요합니다. 특히 XML 태그, 공백, 줄바꿈, 예시 분할기에 주의해야 합니다.

## 컨텍스트 추가

모델에 필요한 모든 정보가 있다고 가정하는 대신 모델이 문제를 해결하는 데 필요한 프롬프트 안내와 정보를 포함할 수 있습니다. 이 컨텍스트 정보는 모델이 요청된 작업의 제약조건과 세부정보를 이해하는 데 도움이 됩니다.

다음 예시에서는 모델에 라우터에 대한 문제 해결 안내를 제공하도록 요청합니다.

|  |
| --- |
| **프롬프트:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **응답:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

이 응답은 라우터 또는 LED 표시기 표시등의 상태와 관련이 없는 일반적인 문제 해결 정보처럼 보입니다.

특정 라우터의 응답을 맞춤설정하려면 응답을 제공할 때 참조할 컨텍스트로 라우터의 문제 해결 가이드를 프롬프트에 추가할 수 있습니다.

|  |
| --- |
| **프롬프트:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **응답:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## 프롬프트를 구성요소로 세분화

복잡한 프롬프트가 필요한 사용 사례의 경우 항목을 더 간단한 구성요소로 나누면 모델이 이러한 복잡성을 관리하도록 도울 수 있습니다.

1. **요청 사항 세분화:** 하나의 프롬프트에 여러 요청 사항을 포함하는 대신 요청 사항당 하나의 프롬프트를 만듭니다. 사용자의 입력에 따라 처리할 프롬프트를 선택할 수 있습니다.
2. **프롬프트 연결:** 여러 순차적 단계가 포함된 복잡한 태스크의 경우 각 단계를 프롬프트로 만들고 프롬프트를 순서대로 연결합니다. 이 순차적인 프롬프트 체인에서 시퀀스의 한 프롬프트 출력이 다음 프롬프트의 입력이 됩니다. 시퀀스에서 마지막 프롬프트의 출력이 최종 출력입니다.
3. **응답 집계:** 집계는 데이터의 서로 다른 부분에서 서로 다른 병렬 태스크를 수행하고 결과를 집계하여 최종 출력을 생성하는 경우에 사용됩니다. 예를 들어 데이터의 첫 번째 부분에 대해 하나의 작업을 수행하고 나머지 데이터에서 다른 작업을 수행한 후 결과를 집계하도록 모델에 지시할 수 있습니다.

## 모델 파라미터 실험

모델에 보낸 각 셀에는 모델의 응답 생성 방식을 제어하는 매개변수 값이 포함되어 있습니다. 모델은 서로 다른 매개변수 값에 대해 서로 다른 결과를 생성할 수 있습니다. 이 작업에서는 최상의 값을 얻을 수 있도록 다양한 매개변수 값으로 실험해 봅니다. 모델별로 사용 가능한 파라미터가 다를 수 있습니다. 가장 일반적인 파라미터는 다음과 같습니다.

1. **최대 출력 토큰:** 응답에서 생성될 수 있는 최대 토큰 수를 지정합니다. 토큰 1개는 약 4자(영문 기준)입니다. 100개의 토큰은 대략 60~80개의 단어에 해당합니다.
2. **온도:** 온도는 토큰 선택의 무작위성 수준을 제어합니다. 온도는 응답 생성 중 샘플링에 사용되며 `topP` 및 `topK`가 적용될 때 발생합니다. 온도가 낮을수록 자유롭거나 창의적인 답변과 거리가 먼 확정적인 응답이 필요한 프롬프트에 적합하고, 온도가 높을수록 보다 다양하거나 창의적인 결과로 이어질 수 있습니다. 온도가 0이면 결정론적입니다. 즉, 확률이 가장 높은 응답이 항상 선택됩니다.
3. **`topK`:** `topK` 매개변수는 모델이 출력용 토큰을 선택하는 방식을 변경합니다. `topK`이 1이면 선택된 토큰이 모델의 어휘에 포함된 모든 토큰 중에서 가장 확률이 높다는 의미입니다 (그리디 디코딩이라고도 함). 반면에 `topK`이 3이면 온도를 사용하여 가장 확률이 높은 토큰 3개 중에서 다음 토큰이 선택된다는 의미입니다. 각 토큰 선택 단계에서 확률이 가장 높은 `topK` 토큰이 샘플링됩니다. 그런 다음 `topP`을 기준으로 토큰을 추가로 필터링하고 온도 샘플링을 사용하여 최종 토큰을 선택합니다.
4. **`topP`:** `topP` 매개변수는 모델이 출력용 토큰을 선택하는 방식을 변경합니다. 토큰은 확률의 합이 `topP` 값과 같아질 때까지 확률이 가장 높은 것부터 가장 낮은 것까지 선택됩니다. 예를 들어 토큰 A, B, C의 확률이 0.3, 0.2, 0.1이고 `topP` 값이 0.5이면 모델이 온도를 사용해서 다음 토큰으로 A 또는 B를 선택하고 C는 후보에서 제외합니다. 기본 `topP` 값은 0.95입니다.
5. **`stop_sequences`:** 모델에 콘텐츠 생성을 중지하도록 지시하는 중지 시퀀스를 설정합니다. 중지 시퀀스는 모든 문자 시퀀스일 수 있습니다. 생성된 콘텐츠에 표시될 수 있는 문자 시퀀스를 사용하지 마세요.

## 프롬프트 반복 전략

프롬프트 설계 시 원하는 응답을 일관성 있게 얻으려면 몇 번의 반복 작업이 필요한 경우가 있습니다. 이 섹션에서는 프롬프트에서 반복할 때 시도할 수 있는 몇 가지 사항에 대한 안내를 제공합니다.

1. **다른 문구 사용:** 프롬프트에서 다른 단어나 문구를 사용하면 의미가 동일하더라도 모델마다 다른 응답이 출력되는 경우가 많습니다. 프롬프트에서 예상한 결과를 얻지 못했다면 다른 문구를 사용해 보세요.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **유사한 작업으로 전환:** 모델이 작업 안내를 따르게 할 수 없으면 동일한 결과를 얻는 유사한 작업에 대한 안내를 제공해 보세요.

   이 프롬프트는 사전 정의된 카테고리를 사용하여 도서를 분류하도록 모델에 지시합니다.

   |  |
   | --- |
   | **프롬프트:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **응답:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   응답은 올바르지만 모델이 옵션의 경계 내에 있지 않았습니다. 또한 전체 문장 대신 옵션 중 하나에만 응답하도록 모델을 만들 수 있습니다. 이 경우 안내를 객관식 질문으로 변경하고 모델이 옵션을 선택하도록 요청할 수 있습니다.

   |  |
   | --- |
   | **프롬프트:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **응답:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **프롬프트 콘텐츠 순서 변경:** 프롬프트에서 콘텐츠 순서는 응답에 영향을 줄 수 있습니다. 콘텐츠 순서를 변경하여 응답에 미치는 영향을 확인하세요.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## 대체 응답

대체 응답은 프롬프트 또는 응답이 안전 필터를 트리거할 때 모델에서 반환하는 응답입니다. 대체 응답의 예로는 '저는 언어 모델일 뿐이기 때문에 지원할 수 없습니다.'가 있습니다.

모델이 대체 응답을 제공할 경우에는 강도를 높여보세요.

## 그라운딩 및 코드 실행

Gemini는 그렇지 않으면 잘못된 대답을 생성할 수 있는 시나리오에서 할루시네이션을 방지하기 위해 도구를 사용할 수 있습니다.

[Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)은 Gemini 모델을 실시간 웹 콘텐츠에 연결하며, 모델이 잘 알려지지 않은 사실이나 최근 사실을 알아야 할 수 있는 경우에 사용 설정해야 합니다.

Gemini의 [코드 실행 도구](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)를 사용하면 모델이 Python 코드를 생성하고 실행할 수 있으며, 모델이 산술, 계산, 계산을 수행해야 할 때마다 사용 설정해야 합니다.

## Gemini 3

[Gemini 3 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko#gemini-3)은 고급 추론 및 요청 사항 준수를 위해 설계되었습니다.
직접적이고 구조화되어 있으며 작업과 제약 조건을 명확하게 정의하는 프롬프트에 가장 잘 응답합니다. Gemini 3로 최적의 결과를 얻으려면 다음 권장사항을 따르세요.

### 핵심 프롬프팅 원칙

- **정확하고 직접적으로 표현:** 목표를 명확하고 간결하게 설명합니다. 불필요하거나 지나치게 설득적인 표현은 피하세요.
- **일관된 구조 사용:** 명확한 구분자를 사용하여 프롬프트의 여러 부분을 구분합니다. XML 스타일 태그 (예: `<context>`, `<task>`) 또는 마크다운 헤더가 효과적입니다. 하나의 형식을 선택하고 단일 프롬프트 내에서 일관되게 사용하세요.
- **매개변수 정의:** 모호한 용어나 매개변수를 명시적으로 설명합니다.
- **출력 장황도 제어:** 기본적으로 Gemini 3 모델은 직접적이고 효율적인 답변을 제공합니다. 더 대화형이거나 자세한 대답이 필요한 경우 요청 사항에 명시적으로 요청해야 합니다.
- **멀티모달 입력을 일관되게 처리:** 텍스트, 이미지, 오디오 또는 동영상을 사용할 때 이를 동등한 클래스 입력으로 취급합니다. 필요에 따라 각 모달리티를 명확하게 참조하도록 안내합니다.
- **중요한 안내에 우선순위 지정:** 필수 행동 제약 조건, 역할 정의 (페르소나), 출력 형식 요구사항을 시스템 안내 또는 사용자 프롬프트의 맨 처음에 배치합니다.
- **긴 컨텍스트의 구조:** 많은 양의 컨텍스트(예: 문서, 코드)를 제공할 때는 먼저 모든 컨텍스트를 제공하세요. 구체적인 요청 사항이나 질문을 프롬프트의 가장 *끝*에 배치합니다.
- **앵커 컨텍스트:** 대량의 데이터 블록 후에는 컨텍스트와 질문을 연결하는 명확한 전환 문구를 사용하세요(예: '위의 정보를 바탕으로...').

### Gemini 3 Flash 전략

- **현재 날짜 정확성:** 모델이 2026년의 현재 날짜에 주의하도록 시스템 안내에 다음 절을 추가합니다.

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **지식 단절 정확성:** 모델이 지식 단절을 인식하도록 시스템 안내에 다음 절을 추가합니다.

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **그라운딩 성능:** 제공된 컨텍스트에서 대답을 그라운딩하는 모델의 능력을 개선하려면 시스템 안내에 다음 조항을 추가하세요 (적절한 경우 수정).

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### 추론 및 계획 개선

Gemini 2.5 및 3 시리즈 모델은 추론 성능을 개선하기 위해 내부 '사고' 텍스트를 자동으로 생성합니다. 따라서 일반적으로 모델이 반환된 대답 자체에서 추론 단계를 간략하게 설명하거나 계획하거나 자세히 설명할 필요는 없습니다. 추론이 많이 필요한 문제의 경우 '대답하기 전에 매우 신중하게 생각하세요'와 같은 간단한 요청이 성능을 개선할 수 있지만, 추가 사고 토큰이 필요합니다.

자세한 내용은 [Gemini 사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko) 문서를 참고하세요.

### 구조화된 프롬프트 예시

태그나 마크다운을 사용하면 모델이 안내, 컨텍스트, 작업을 구분하는 데 도움이 됩니다.

**XML 예:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**마크다운 예:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### 권장사항을 결합한 템플릿 예시

이 템플릿은 Gemini 3로 프롬프트를 작성하기 위한 핵심 원칙을 포착합니다. 항상 특정 사용 사례에 맞게 반복하고 수정해야 합니다.

**시스템 안내:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**사용자 프롬프트:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## 에이전트형 워크플로

심층적인 에이전트 워크플로의 경우 모델이 추론하고, 계획하고, 작업을 실행하는 방식을 제어하기 위해 구체적인 안내가 필요한 경우가 많습니다. Gemini는 강력한 일반 성능을 제공하지만 복잡한 에이전트의 경우 컴퓨팅 비용 (지연 시간 및 토큰)과 작업 정확도 간의 균형을 구성해야 하는 경우가 많습니다.

에이전트의 프롬프트를 설계할 때는 에이전트에서 조종할 수 있는 다음과 같은 행동의 측면을 고려하세요.

### 추론 및 전략

모델이 행동하기 전에 생각하고 계획하는 방식에 관한 구성입니다.

- **논리적 분해:** 모델이 제약 조건, 사전 요구사항, 작업 순서를 얼마나 철저하게 분석해야 하는지 정의합니다.
- **문제 진단**: 원인을 식별할 때 분석의 깊이와 모델의 귀추법적 추론 사용을 제어합니다. 모델이 가장 명확한 대답을 수락해야 하는지 아니면 복잡하고 가능성이 낮은 설명을 탐색해야 하는지 결정합니다.
- **정보 완전성:** 사용 가능한 모든 정책과 문서를 분석하는 것과 효율성과 속도를 우선시하는 것 사이의 절충안입니다.

### 실행 및 안정성

에이전트가 자율적으로 작동하고 장애물을 처리하는 방식에 관한 구성입니다.

- **적응성:** 모델이 새 데이터에 반응하는 방식입니다. 관찰 결과가 가정과 모순될 때 초기 계획을 엄격하게 준수해야 하는지 아니면 즉시 전환해야 하는지 결정합니다.
- **지속성 및 복구:** 모델이 오류를 자체 수정하려고 시도하는 정도입니다. 지속성이 높을수록 성공률이 높아지지만 토큰 비용이 높아지거나 루프가 발생할 위험이 있습니다.
- **위험 평가:** 결과를 평가하는 논리입니다. 위험도가 낮은 탐색 작업 (읽기)과 위험도가 높은 상태 변경 (쓰기)을 명시적으로 구분합니다.

### 상호작용 및 출력

에이전트가 사용자와 소통하고 결과를 포맷하는 방식에 관한 구성입니다.

- **모호성 및 권한 처리:** 모델이 가정을 해도 되는 경우와 사용자에게 명확한 설명이나 권한을 요청하기 위해 실행을 일시중지해야 하는 경우를 정의합니다.
- **장황성:** 도구 호출과 함께 생성되는 텍스트의 볼륨을 제어합니다. 이는 모델이 실행 중에 사용자에게 작업을 설명하는지 아니면 침묵을 유지하는지를 결정합니다.
- **정확성 및 완전성:** 출력에 필요한 충실도입니다. 모델이 모든 특이 사례를 해결하고 정확한 수치를 제공해야 하는지 아니면 대략적인 추정치가 허용되는지 지정합니다.

### 시스템 요청 사항 템플릿

다음 시스템 안내는 모델이 복잡한 규칙을 준수하고 사용자와 상호작용해야 하는 에이전트 벤치마크에서 성능을 개선하기 위해 연구자가 평가한 예입니다. 에이전트가 강력한 추론자이자 계획자로서 행동하도록 장려하고, 위에 나열된 여러 차원에서 특정 행동을 강제하며, 모델이 행동을 취하기 전에 사전 계획을 세우도록 요구합니다.

이 템플릿을 특정 사용 사례 제약 조건에 맞게 조정할 수 있습니다.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## 다음 단계

- 프롬프트 설계에 대해 자세히 알아봤으니 이제 [Google AI Studio](http://aistudio.google.com?hl=ko)를 사용하여 나만의 프롬프트를 작성해 보세요.
- 멀티모달 프롬프트 사용에 대한 자세한 내용은 [미디어 파일로 프롬프트 입력](https://ai.google.dev/gemini-api/docs/files?hl=ko#prompt-guide)을 참고하세요.
- 이미지 프롬프트에 대해 알아보려면 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko#prompt-guide) 및 [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ko#imagen-prompt-guide) 프롬프트 가이드를 참고하세요.
- 동영상 프롬프트에 대해 알아보려면 [Veo 프롬프트 가이드](https://ai.google.dev/gemini-api/docs/video?hl=ko#prompt-guide)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
