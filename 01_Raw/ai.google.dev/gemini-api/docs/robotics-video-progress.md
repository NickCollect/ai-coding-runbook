---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ko
fetched_at: 2026-08-03T04:32:34.376473+00:00
title: "\ub3d9\uc601\uc0c1 \uc774\ud574 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 동영상 이해

Gemini Robotics ER 2는 두 가지 기능을 사용하여 연속 동영상 피드에서 작업 진행 상황을 추적할 수 있습니다.

- 순간 찾기: 주요 이벤트가 발생하는 정확한 타임스탬프를 식별합니다.
- 진행 상황 분류: 각 동영상을 5개의 완료 구간 (0~20%, 20~40%, 40~60%, 60~80%, 80~100%) 중 하나에 할당합니다.

## 순간 찾기

순간 찾기는 컵이 가득 차거나 매듭이 묶이는 등 중요한 이벤트가 발생하는 정확한 동영상 프레임을 식별합니다. 로봇은 이를 사용하여 성공 여부를 확인하고, 단계를 순서대로 진행하고, 수정을 트리거합니다.

다음 예시 프롬프트는 모델에 동영상에서 지정된 작업의 완료 순간을 식별하도록 요청합니다.

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

다음은 모델이 작업 완료 타임스탬프를 식별하는 순간 찾기 동영상의 프레임 예시를 보여줍니다.

![타임스탬프 오버레이가 있는 순간 찾기 출력을 보여주는 동영상 프레임의 예](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=ko)

## 진행 상황 분류

진행 상황 분류는 동영상을 5개의 완료 구간(0~20%, 20~40%, 40~60%, 60~80%, 80~100%) 중 하나에 할당합니다. 이를 통해 로봇은 실시간으로 상황을 인식하여 전체 워크플로를 다시 시작하지 않고도 작업을 조정하거나 실패한 단계를 다시 시도할 수 있습니다.

다음 예시 프롬프트는 모델에 동영상의 현재 진행 상황 수준을 분류하도록 요청합니다.

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

다음은 모델이 진행 상황 구간을 할당하는 진행 상황 분류 동영상의 프레임 예시를 보여줍니다.

![진행률 괄호 라벨이 있는 진행률 분류 출력을 보여주는 동영상 프레임 예시](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=ko)

## 예

다단계 작업 추적을 비롯한 실행 가능한 전체 예시는
[로봇공학 레시피](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)를 참고하세요.

## 다음 단계

- [로봇공학용 Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko) - 실시간 양방향 스트리밍
- [작업 오케스트레이션](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ko) - 공간 추론을 사용하는 장기 작업
- [Gemini Robotics ER 개요](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ko) - 모델 비교 및 기능

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
