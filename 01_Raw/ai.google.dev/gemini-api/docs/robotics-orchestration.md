---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th
fetched_at: 2026-08-10T03:15:51.058617+00:00
title: "\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e2a\u0e32\u0e19\u0e07\u0e32\u0e19\u0e07\u0e32\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การประสานงานงาน

โมเดล Gemini Robotics ER สามารถวางแผนงานและให้เหตุผลเกี่ยวกับพื้นที่ โดยอนุมานการดำเนินการที่จะทำและวัตถุที่จะย้ายเพื่อให้บรรลุเป้าหมาย หน้านี้
แสดงตัวอย่างสำหรับ [การขับเคลื่อนการดำเนินการหยิบและวาง](https://ai.google.dev/gemini-api/docs/calling-custom-robot-api?hl=th)
ผ่าน API ของหุ่นยนต์ที่กำหนดเองเพื่อจัดระเบียบงานในการวางสิ่งของ
ลงในชาม ตัวอย่างนี้ใช้โมเดล Gemini ER 2 มาตรฐาน หากต้องการดูตัวอย่างการสตรีม
โปรดดู[คู่มือการสตรีม Gemini ER 2](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th)

หากต้องการดูโค้ดที่เรียกใช้ได้ทั้งหมด โปรดดู
[คู่มือการใช้งาน Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)

## การใช้ API ของหุ่นยนต์ที่กำหนดเอง

ตัวอย่างนี้แสดงการจัดระเบียบงานด้วย API ของหุ่นยนต์ที่กำหนดเอง โดยจะแนะนำ API จำลองที่ออกแบบมาสำหรับการดำเนินการหยิบและวาง งานคือการหยิบบล็อกสีน้ำเงินและวางลงในชามสีส้ม ดังนี้

![รูปภาพบล็อกและชาม](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=th)

ตัวอย่างนี้ใช้ API ของหุ่นยนต์จำลองต่อไปนี้

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

ตัวอย่างต่อไปนี้จะส่งพรอมต์และรูปภาพไปยังโมเดลพร้อมคำจำกัดความของเครื่องมือ จากนั้นจะเรียกใช้ลูปของเอเจนต์ โดยหลังจากที่โมเดลตอบกลับแต่ละครั้ง ระบบจะเรียกใช้ฟังก์ชันที่ขอ (`move`, `setGripperState`), ส่งผลลัพธ์กลับไปยังโมเดลโดยใช้ `previous_interaction_id` และทำซ้ำจนกว่าโมเดลจะหยุดเรียกใช้ฟังก์ชันหรือถึงขีดจำกัดของขั้นตอน

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

ตัวอย่างต่อไปนี้แสดงเอาต์พุตที่เป็นไปได้ของโมเดลตามพรอมต์และ API ของหุ่นยนต์จำลอง เอาต์พุตประกอบด้วยเอาต์พุตของการเรียกใช้ฟังก์ชันของหุ่นยนต์ที่โมเดลจัดลำดับไว้ด้วยกัน

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

## ขั้นตอนถัดไป

- [Robotics พร้อมการสตรีม](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) - การสตรีมแบบเรียลไทม์พร้อมการเรียกใช้ฟังก์ชัน (Gemini Robotics ER 2 เท่านั้น)
- [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) - ติดตามความคืบหน้าของงานจากวิดีโอ (ER 2 เท่านั้น)
- [การให้เหตุผลเชิงพื้นที่](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=th) - ตัวอย่างการชี้ การติดตาม และกรอบล้อมรอบ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
