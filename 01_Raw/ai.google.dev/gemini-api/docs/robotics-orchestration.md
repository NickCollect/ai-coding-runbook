---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ko
fetched_at: 2026-09-07T05:46:04.916205+00:00
title: "\ud0dc\uc2a4\ud06c \uc870\uc815 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 태스크 조정

Gemini Robotics ER 모델은 작업을 계획하고 공간에 대해 추론하여 목표를 달성하기 위해 취할 작업과 이동할 객체를 추론할 수 있습니다. 이 페이지
에서는 맞춤 로봇 API를 통해 [선택 및 배치](https://ai.google.dev/gemini-api/docs/calling-custom-robot-api?hl=ko)
작업을 실행하여 항목을
그릇에 배치하는 작업을 오케스트레이션하는 예를 보여줍니다. 이 예에서는 표준 Gemini ER 2 모델을 사용합니다. 스트리밍
예는 [Gemini ER 2 스트리밍 가이드](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko)를 참고하세요.

실행 가능한 전체 코드는
[로봇공학 레시피](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)를 참고하세요.

## 맞춤 로봇 API 사용

이 예에서는 맞춤 로봇 API를 사용한 작업 오케스트레이션을 보여줍니다. 선택 및 배치 작업을 위해 설계된 모의 API를 소개합니다. 작업은 파란색 블록을 집어 주황색 그릇에 배치하는 것입니다.

![블록과 그릇의 이미지](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=ko)

이 예에서는 다음 모의 로봇 API를 사용합니다.

### Python

```
def move(x, y, high):
  print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
  print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_function = {
    "type": "function",
    "name": "move",
    "description": "Moves the arm to the given coordinates.",
    "parameters": {
        "type": "object",
        "properties": {
            "x": {"type": "integer", "description": "X coordinate relative to the origin"},
            "y": {"type": "integer", "description": "Y coordinate relative to the origin"},
            "high": {"type": "boolean", "description": "Set to True to lift the robot arm above the scene for avoiding obstacles. Set to False to place the gripper on the surface."}
        },
        "required": ["x", "y", "high"]
    }
}

set_gripper_state_function = {
    "type": "function",
    "name": "setGripperState",
    "description": "Opens or closes the robot's gripper.",
    "parameters": {
        "type": "object",
        "properties": {
            "opened": {"type": "boolean", "description": "True opens the gripper, False closes the gripper."}
        },
        "required": ["opened"]
    }
}
```

다음 예에서는 도구 정의와 함께 프롬프트와 이미지를 모델에 전송합니다. 그런 다음 에이전트 루프를 실행합니다. 각 모델 응답 후 요청된 함수 호출 (`move`, `setGripperState`)을 실행하고 `previous_interaction_id`를 사용하여 결과를 모델에 다시 반환하며 모델이 함수 호출을 중지하거나 단계 제한에 도달할 때까지 반복합니다.

### Python

```
prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

# 1. Initial Interaction
interaction = client.interactions.create(
    model=MODEL_ID,
    input=[{"type": "user_input", "content": [
        {"type": "image", "data": img_b64, "mime_type": "image/png"},
        {"type": "text", "text": prompt}
    ]}],
    tools=[move_function, set_gripper_state_function],
    generation_config={"thinking_level": "low"}
)

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15 # Safety limit to prevent infinite loops
step_count = 0

# 2. The Agentic Loop
while step_count < max_steps:
    step_count += 1

    # Check if the model wants to call any functions
    tool_calls = [step for step in interaction.steps if step.type == "function_call"]

    if not tool_calls:
        # If no tools were called, the model is finished with the sequence
        print("Sequence complete.")
        if interaction.output_text:
            print(f"Model Summary: {interaction.output_text}")
        break

    function_results = []

    for step in tool_calls:
        function_name = step.name
        arguments = step.arguments

        # Execute the mock function
        if function_name == "move":
            move(**arguments)
        elif function_name == "setGripperState":
            setGripperState(**arguments)
        else:
            print(f"Unknown function: {function_name}")

        # 3. Create a result object to tell the model the function succeeded
        function_results.append({
            "type": "function_result",
            "name": step.name,
            "call_id": step.id,
            "result": [{"type": "text", "text": '{"status": "success"}'}]
        })

    # 4. Send the results back to the model, passing previous_interaction_id
    # so it remembers the conversation history and generates the NEXT step
    interaction = client.interactions.create(
        model=MODEL_ID,
        previous_interaction_id=interaction.id,
        tools=[move_function, set_gripper_state_function],
        input=function_results
    )
```

다음은 프롬프트와 모의 로봇 API를 기반으로 모델의 가능한 출력을 보여줍니다. 출력에는 모델이 함께 시퀀싱한 로봇 함수 호출의 출력이 포함됩니다.

```
--- Executing Orchestrated Plan ---
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: 160, 440, down at table level
Mock Robot: Closing gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: -250, 60, high above table
Mock Robot: Moving to coordinates: -250, 60, down at table level
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: -250, 60, high above table
Sequence complete.
Model Summary: I have completed the task of picking up the blue block and placing it into the orange bowl.
```

## 다음 단계

- [스트리밍을 통한 로봇공학](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko) - 함수 호출을 통한 실시간 스트리밍 (Gemini Robotics ER 2만 해당)
- [동영상 이해](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ko) - 동영상에서 작업 진행률 추적 (ER 2만 해당)
- [공간 추론](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ko) - 가리키기, 추적, 경계 상자 예

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
