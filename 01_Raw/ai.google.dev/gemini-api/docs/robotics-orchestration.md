---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=hi
fetched_at: 2026-08-31T06:40:34.237170+00:00
title: "\u091f\u093e\u0938\u094d\u0915 \u0911\u0930\u094d\u0915\u0947\u0938\u094d\u091f\u094d\u0930\u0947\u0936\u0928 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# टास्क ऑर्केस्ट्रेशन

Gemini Robotics ER मॉडल, टास्क प्लान कर सकते हैं. साथ ही, यह अनुमान लगा सकते हैं कि किसी लक्ष्य को पूरा करने के लिए, कौनसे ऑब्जेक्ट को कहाँ ले जाना है और कौनसे ऐक्शन लेने हैं. इस पेज पर, [पिक-एंड-प्लेस की प्रोसेस को कंट्रोल करने](https://ai.google.dev/gemini-api/docs/calling-custom-robot-api?hl=hi) का उदाहरण दिखाया गया है. इसके लिए, कस्टम रोबोट एपीआई का इस्तेमाल किया गया है, ताकि किसी आइटम को कटोरे में रखने के टास्क को मैनेज किया जा सके. इस उदाहरण में, Gemini ER 2 के स्टैंडर्ड मॉडल का इस्तेमाल किया गया है. स्ट्रीमिंग के उदाहरण के लिए, [Gemini ER 2 की स्ट्रीमिंग से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) देखें.

पूरे रन करने लायक कोड के लिए, [रोबोटिक्स कुकबुक](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) देखें.

## कस्टम रोबोट एपीआई का इस्तेमाल करना

इस उदाहरण में, कस्टम रोबोट एपीआई की मदद से टास्क ऑर्केस्ट्रेशन के बारे में बताया गया है. इसमें पिक-एंड-प्लेस ऑपरेशन के लिए डिज़ाइन किया गया मॉक एपीआई शामिल है. टास्क में, नीले रंग के ब्लॉक को उठाकर नारंगी रंग के कटोरे में रखना है:

![ब्लॉक और कटोरे की इमेज](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=hi)

इस उदाहरण में, रोबोट के एपीआई के इस मॉक का इस्तेमाल किया गया है:

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

यहां दिए गए उदाहरण में, टूल की परिभाषाओं के साथ मॉडल को प्रॉम्प्ट और इमेज भेजी जाती है. इसके बाद, यह एजेंटिक लूप चलाता है: हर मॉडल रिस्पॉन्स के बाद, यह अनुरोध किए गए किसी भी फ़ंक्शन कॉल (`move`, `setGripperState`) को एक्ज़ीक्यूट करता है. साथ ही, `previous_interaction_id` का इस्तेमाल करके, नतीजों को मॉडल पर वापस भेजता है. यह प्रोसेस तब तक दोहराई जाती है, जब तक मॉडल फ़ंक्शन कॉल करना बंद नहीं कर देता या चरण की सीमा पूरी नहीं हो जाती.

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

यहां प्रॉम्प्ट और मॉक रोबोट एपीआई के आधार पर, मॉडल का संभावित आउटपुट दिखाया गया है. आउटपुट में, रोबोट फ़ंक्शन कॉल का आउटपुट शामिल होता है. मॉडल ने इन फ़ंक्शन कॉल को एक साथ क्रम से लगाया है.

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

## आगे क्या करना है

- [स्ट्रीमिंग के साथ रोबोटिक्स](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) — फ़ंक्शन कॉलिंग के साथ रीयल-टाइम स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2).
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=hi) — वीडियो से टास्क की प्रोग्रेस को ट्रैक करना (सिर्फ़ ER 2).
- [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=hi) — पॉइंटिंग, ट्रैकिंग, और बाउंडिंग बॉक्स के उदाहरण.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
