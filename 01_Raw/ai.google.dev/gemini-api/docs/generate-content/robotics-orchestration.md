---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=hi
fetched_at: 2026-10-26T05:41:56.409233+00:00
title: "\u091f\u093e\u0938\u094d\u0915 \u0911\u0930\u094d\u0915\u0947\u0938\u094d\u091f\u094d\u0930\u0947\u0936\u0928 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# टास्क ऑर्केस्ट्रेशन

Gemini Robotics ER मॉडल, टास्क की योजना बना सकते हैं और जगह के बारे में जानकारी दे सकते हैं. साथ ही, यह भी बता सकते हैं कि किसी लक्ष्य को पूरा करने के लिए, कौनसी कार्रवाइयां करनी हैं और किन ऑब्जेक्ट को मूव करना है. इस पेज पर, किसी आइटम को कटोरे में रखने के टास्क को पूरा करने के लिए, कस्टम रोबोट एपीआई की मदद से [पिक-ऐंड-प्लेस](#calling-custom-robot-api) ऑपरेशन चलाने का उदाहरण दिया गया है.

पूरा कोड देखने के लिए, [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) देखें.

## कस्टम रोबोट एपीआई का इस्तेमाल करना

इस उदाहरण में, कस्टम रोबोट एपीआई की मदद से टास्क ऑर्केस्ट्रेशन करने का तरीका दिखाया गया है. इसमें, पिक-ऐंड-प्लेस ऑपरेशन के लिए डिज़ाइन किया गया मॉक एपीआई दिखाया गया है. इस टास्क में, नीले रंग के ब्लॉक को उठाकर, नारंगी रंग के कटोरे में रखना है:

![ब्लॉक और कटोरे की इमेज](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=hi)

इस उदाहरण में, मॉक रोबोट एपीआई और टूल की इन परिभाषाओं का इस्तेमाल किया गया है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

def move(x, y, high):
    print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
    print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_declaration = types.FunctionDeclaration(
    name="move",
    description="Moves the arm to the given coordinates.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "x": types.Schema(type=types.Type.INTEGER, description="X coordinate relative to the origin"),
            "y": types.Schema(type=types.Type.INTEGER, description="Y coordinate relative to the origin"),
            "high": types.Schema(type=types.Type.BOOLEAN, description="Set to True to lift the robot arm above the scene. Set to False to place the gripper on the surface."),
        },
        required=["x", "y", "high"],
    ),
)

set_gripper_state_declaration = types.FunctionDeclaration(
    name="setGripperState",
    description="Opens or closes the robot's gripper.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "opened": types.Schema(type=types.Type.BOOLEAN, description="True opens the gripper, False closes the gripper."),
        },
        required=["opened"],
    ),
)

robot_tools = types.Tool(function_declarations=[move_declaration, set_gripper_state_declaration])
```

इस उदाहरण में, टूल की परिभाषाओं के साथ प्रॉम्प्ट और इमेज को मॉडल को भेजा जाता है. इसके बाद, एजेंटिक लूप चलता है. हर मॉडल के जवाब के बाद, अनुरोध किए गए फ़ंक्शन कॉल (`move`, `setGripperState`) को लागू किया जाता है. इसके बाद, नतीजों को वापस मॉडल को भेजा जाता है. यह प्रोसेस तब तक चलती है, जब तक मॉडल फ़ंक्शन कॉल करना बंद नहीं कर देता या चरण की सीमा पूरी नहीं हो जाती.

### Python

```
with open("robot-api-example.png", "rb") as f:
    img_bytes = f.read()

prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

contents = [
    types.Content(role="user", parts=[
        types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
        types.Part(text=prompt),
    ])
]

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15  # Safety limit to prevent infinite loops
step_count = 0

# The Agentic Loop
while step_count < max_steps:
    step_count += 1

    response = client.models.generate_content(
        model="gemini-robotics-er-2-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[robot_tools],
            thinking_config=types.ThinkingConfig(thinking_level="low"),
        ),
    )

    # Add model response to conversation history
    contents.append(response.candidates[0].content)

    # Check for function calls
    function_calls = [part for part in response.candidates[0].content.parts if part.function_call]

    if not function_calls:
        # Model is done calling functions
        print("Sequence complete.")
        print(f"Model Summary: {response.text}")
        break

    # Execute function calls and collect results
    function_response_parts = []
    for part in function_calls:
        fc = part.function_call
        if fc.name == "move":
            move(**fc.args)
        elif fc.name == "setGripperState":
            setGripperState(**fc.args)

        function_response_parts.append(
            types.Part.from_function_response(
                name=fc.name,
                response={"status": "success"},
            )
        )

    # Send function results back to model
    contents.append(types.Content(role="user", parts=function_response_parts))
```

यहां, प्रॉम्प्ट और मॉक रोबोट एपीआई के आधार पर, मॉडल का संभावित आउटपुट दिखाया गया है. आउटपुट में, रोबोट के फ़ंक्शन कॉल का आउटपुट शामिल होता है. इन्हें मॉडल ने एक साथ क्रम से लगाया है.

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
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=hi) — वीडियो से टास्क की प्रोग्रेस ट्रैक करना (सिर्फ़ ER 2).
- [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=hi) — पॉइंटिंग, ट्रैकिंग, और बाउंडिंग बॉक्स के उदाहरण.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-08 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-08 (UTC) को अपडेट किया गया."],[],[]]
