---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko
fetched_at: 2026-09-07T05:43:22.082693+00:00
title: "\uc2a4\ud2b8\ub9ac\ubc0d\uc744 \uc0ac\uc6a9\ud55c \ub85c\ubd07 \uacf5\ud559 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 스트리밍을 사용한 로봇 공학

[`gemini-robotics-er-2-streaming-preview` 모델 엔드포인트는 Live API와 통합되는 전용 스트리밍 엔드포인트를 노출하여 애플리케이션과 로봇 간의 실시간 양방향 상호작용을 지원합니다.](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ko) 따라서 빠른 피드백 루프와 환경에 대한 반응형 응답이 필요한 에이전트에 적합합니다.

[Google AI Studio에서 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=ko)
[GitHub에서 샘플 앱 클론](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## 사용 사례

- **다중 로봇 조정**: 공유 세션을 통해 작업 상태를 전달하고
  하위 작업을 위임하는 여러 로봇입니다.
- **지속적 모니터링**: 장면을 관찰하고 컨테이너가 채우기 수준에 도달하는 등의 특정 이벤트가 발생하면 작업을 트리거하는 로봇입니다.
- **창고 및 물류**: 항목을 시각적으로 확인하고, 포장 진행 상황을 추적하고, 오류를 복구하는 출하 및 포장 에이전트입니다.

## 기술 사양

다음 표에는 Live API의 기술 사양이 나와 있습니다.

| 카테고리 | 세부정보 |
| --- | --- |
| 입력 모달리티 | 오디오 (원시 16비트 PCM 오디오, 16kHz, 리틀 엔디안), 이미지 (JPEG <= 1FPS), 텍스트 |
| 출력 모달리티 | 텍스트 |
| 프로토콜 | 스테이트풀 WebSocket 연결 (WSS) |

## 에이전트 설정 빌드

Live API를 기반으로 빌드된 모든 로봇 공학 에이전트는 다음 세 단계를 따릅니다.

1. **로봇 기능을 도구로 선언합니다.** 로봇이 실행할 수 있는 각 작업(탐색, 잡기, 말하기)은 이름, 설명, 매개변수 스키마가 있는 함수 선언이 됩니다. 모델이 다음 단계를 선택하기 전에 로봇이 완료될 때까지 기다리도록 하려면 실제 작업에서
   `"behavior": "BLOCKING"`을 사용해야 합니다.
2. **멀티모달 입력을 지속적 세션으로 스트리밍합니다.** `live.connect` 세션을 열고 작업 기간 동안 열어 둡니다. 로봇의 센서에서 도착하는 대로 동영상 프레임, 오디오 또는 텍스트를 전송합니다.
3. **수신 루프에서 도구 호출을 처리합니다.** 모델이 작업을 선택할 때마다 `tool_call` 메시지를 전송합니다. 수신 루프는 로봇 SDK에 대해 함수를 실행하고 `tool_response`를 다시 전송합니다. 세션은 열린 상태로 유지되고 모델은 결과에 따라 다음 작업을 선택합니다.

다음 섹션에서는 이러한 단계를 세 가지 일반적인 패턴(기준 에이전트 루프, 하트비트를 사용한 선제적 장면 모니터링, TTS를 도구로 사용한 음성 라우팅)에 적용하는 방법을 보여줍니다.

## 함수 호출을 통해 로봇 조정

다음 예에서는 세 단계를 모두 단일 Python 스크립트에 연결하는 방법을 보여줍니다.

1단계(도구 정의)에서는 로봇 기능을 함수 선언으로 선언합니다. `navigate` 함수는 `"behavior": "BLOCKING"`을 사용하므로
모델은 로봇이 경유지에 도달할 때까지 기다린 후 다른 도구를 호출합니다.
동일한 목록에 함수 선언을 더 추가하여 추가 로봇 기능을 노출합니다.

2단계(입력 도우미)에서는 다양한 모달리티 입력을 세션으로 스트리밍하는 세 가지 함수를 보여줍니다. 명령어의 경우 `send_text`, 선택적 텍스트 프롬프트가 있는 카메라 프레임의 경우 `send_image`, 마이크의 원시 PCM 오디오의 경우 `send_audio`입니다.

3단계(수신 루프)는 동시에 실행되며 두 가지 유형의 메시지(`server_content` 메시지(모델의 텍스트 출력) 및 `tool_call` 메시지(로봇 작업을 요청하는 모델))를 처리합니다. 도구 호출이 도착하면 루프는 실제 로봇 SDK로 대체하는 스텁인 `execute_tool`을 호출한 다음 모델이 다음 작업을 선택할 수 있도록 `tool_response`를 다시 전송합니다.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

수신 루프는 각 도구 응답 후에도 활성 상태를 유지합니다. 전체 작업 시퀀스를 미리 인코딩하지 않아도 모델이 장기 계획을 구성하고 수정합니다.

## 선제적 시공간 추론

Live API는 동영상을 스트리밍하지만 동영상 프레임만으로는 새로운 추론 차례가 트리거되지 않습니다. 모델 응답을 트리거하려면 동영상 프레임에 텍스트 또는 오디오 프롬프트가 함께 제공되어야 합니다. 자세한 내용은
[Live API 기능](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko)을
참고하세요.

선제적 추론을 사용 설정하려면 **하트비트**를 구현합니다. 모델이 장면을 검사하고 명시적 결정을 내리도록 하는 짧은 텍스트 프롬프트가 뒤따르는
최신 카메라 프레임을 주기적으로 전송합니다. 동영상 입력은 초당 1프레임으로 속도 제한됩니다.

이전 섹션의 수신 루프와 함께 이 코루틴을 추가합니다. 동일한 세션에서 별도의 `asyncio` 작업으로 실행됩니다.

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

로봇 작업 중에 하트비트를 일시중지할 필요는 없습니다.
**암시적 성공 감지기**로 사용하면 모델이 진행 중인 작업을 지속적으로
관찰 (잡기가 안전한지, 붓기가 목표에 있는지, 객체가 올바르게 정착되는지 추적)하고 결과가 명확해지는 순간에 반응할 수 있습니다.

하트비트 메시지는 사용자 차례로 작동하며 진행 중인 모델 생성을 중단합니다.
Live API가 이 동작을 처리하는 방법을 알아보려면 중단에 관한
[Live API 가이드](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko#interruptions)
를 참고하세요.

## 외부 TTS를 통한 오디오 출력

Gemini Robotics ER 2는 텍스트를 반환합니다. 애플리케이션은 삽입된 콜백을 통해 완료된 응답을
별도의 TTS 제공업체 (예:
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko))로 라우팅합니다.
이렇게 하면 음성 지연 시간, 음성 선택, 중단 동작을 제어할 수 있으며 에이전트 로직을 변경하지 않고도 TTS 백엔드를 교체할 수 있습니다.

TTS를 도구로 선언하여 모델이 '말하기'를 '팔 움직이기'와 동일하게 처리하도록 할 수도 있습니다. 첫 번째 섹션의 `tools` 목록에 다음 함수 선언을 추가합니다.

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

TTS를 함수 선언으로 래핑하면 모델은 다른 로봇 작업과 동일한 도구 호출 경로를 통해 음성을 처리합니다. 애플리케이션은 삽입된 콜백으로 호출을 처리합니다.

## GitHub의 예

Spot 로봇 스낵 가져오기 데모 및 Tinybot
팬틸트 Hello World를 비롯한 전체 작업 예시는
[로봇 공학 Live API 예시](https://github.com/google-gemini/robotics-samples/tree/main/live-api)를 참고하세요.

## 다음 단계

- [동영상 이해](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ko): 순간 찾기 및 진행률 분류
- [작업 조정](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ko): 스트리밍이 없는 장기 작업
- [Live API 개요](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ko): 전체 Live API 문서

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-31(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-31(UTC)"],[],[]]
