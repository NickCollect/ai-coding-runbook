---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-TW
fetched_at: 2026-08-24T02:29:01.900285+00:00
title: "\u5de5\u4f5c\u81ea\u52d5\u5316\u8abf\u5ea6\u7ba1\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 工作自動化調度管理

Gemini Robotics ER 模型可以規劃工作和推論空間，推斷要採取哪些動作和移動哪些物體，才能達成目標。本頁提供範例，說明如何透過自訂機器人 API 驅動取放作業，協調將物品放入碗中的工作。這個範例使用標準 Gemini ER 2 模型。如需串流範例，請參閱 [Gemini ER 2 串流指南](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw)。

如需完整的可執行程式碼，請參閱「[機器人食譜](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)」。

## 使用自訂機器人 API

這個範例說明如何使用自訂機器人 API 編排工作。這個 API 專為取放作業設計，這項工作的目標是拿起藍色積木，然後放入橘色碗中：

![木塊和碗的圖片](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=zh-tw)

本範例使用下列模擬機器人 API：

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

以下範例會將提示和圖片連同工具定義傳送給模型。接著執行代理程式迴圈：在每次模型回覆後，執行任何要求的函式呼叫 (`move`、`setGripperState`)，使用 `previous_interaction_id` 將結果傳回模型，並重複執行，直到模型停止呼叫函式或達到步驟限制為止。

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

以下是根據提示和模擬機器人 API，模型可能產生的輸出內容。輸出內容包含模型依序執行的機器人函式呼叫輸出內容。

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

## 後續步驟

- [串流機器人](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw)：透過函式呼叫進行即時串流 (僅限 Gemini Robotics ER 2)。
- [影片理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-tw)：追蹤影片中的工作進度 (僅限 ER 2)。
- [空間推論](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=zh-tw)：指向、追蹤和定界框範例。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
