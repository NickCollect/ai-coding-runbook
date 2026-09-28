---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=hi
fetched_at: 2026-09-28T06:30:43.882332+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Hooks

हुक की मदद से, एजेंट के कोड को एक्ज़ीक्यूट करने या रिमोट सैंडबॉक्स में फ़ाइलों में बदलाव करने से ठीक पहले या बाद में, कस्टम स्क्रिप्ट या बाहरी एचटीटीपी अनुरोधों को चलाया जा सकता है. ऑटोमेटेड गार्डरेल और बैकग्राउंड वर्कफ़्लो के साथ एजेंट लूप को बढ़ाने के लिए, हुक का इस्तेमाल करें. जैसे:

- ज़्यादा जोखिम वाली शेल कमांड या फ़ाइल पढ़ने की पाबंदी लागू होने से पहले, **सुरक्षा और ऐक्सेस से जुड़े नियमों को लागू करना**.
- एजेंट के फ़ाइलें बनाने या उनमें बदलाव करने के तुरंत बाद, **डेटा पाइपलाइन में बदलावों को अपने-आप लागू करना**.
- टूल के इस्तेमाल के बाद, बाहरी मॉनिटरिंग सिस्टम को **स्ट्रीमिंग एंटरप्राइज़ ऑडिट टेलीमेट्री**.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## लाइफ़साइकल के इन इवेंट के लिए, यह सुविधा उपलब्ध है

सैंडबॉक्स में हुक, दो इवेंट के साथ काम करते हैं:

| इवेंट | यह कब ट्रिगर होता है | यह क्या करता है |
| --- | --- | --- |
| `pre_tool_execution` | किसी टूल के चलने से ठीक पहले | टूल को लागू करने से पहले, उसे अनुमति (`allow`) दी जा सकती है या ब्लॉक (`deny`) किया जा सकता है. ब्लॉक किए जाने पर, मॉडल को जवाब अस्वीकार करने की वजह पता चलती है और वह उसके हिसाब से काम करता है. |
| `post_tool_execution` | टूल का इस्तेमाल पूरा होने के तुरंत बाद | यह कोड को फ़ॉर्मैट करने, यूनिट टेस्ट चलाने या टेलीमेट्री लॉग करने जैसे फ़ॉलो-अप टास्क पूरे करता है. पूरी हो चुकी कार्रवाइयों को ब्लॉक नहीं किया जा सकता या पहले जैसा नहीं किया जा सकता. |

### `pre_tool_execution`

यह इवेंट, टूल के एक्ज़ीक्यूट होने से ठीक पहले ट्रिगर होता है. आपकी स्क्रिप्ट, `stdin` से टूल कॉल की जानकारी पढ़ती है और `stdout` को JSON (`allow` या `deny`) के तौर पर अपना फ़ैसला आउटपुट करती है.

**इनपुट पेलोड (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**आउटपुट रिस्पॉन्स (`stdout`):**

टूल को कॉल करने की अनुमति देने के लिए:

```
{
  "decision": "allow"
}
```

टूल कॉल को ब्लॉक करने और मॉडल को सुझाव/राय देने या शिकायत करने के लिए:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

जब कोई हुक किसी निर्देश को अस्वीकार करता है, तो टूल कॉल को तुरंत स्किप कर दिया जाता है. एजेंट को, मौजूदा बातचीत में ही गड़बड़ी का नतीजा दिखता है. इसमें अनुरोध अस्वीकार करने की वजह शामिल होती है. इसके बाद, मॉडल किसी दूसरी कमांड को चुनकर या उपयोगकर्ता को ब्लॉक करने की वजह बताकर, अपनी गलती को ठीक कर सकता है.

अगर आपकी स्क्रिप्ट से, पहचाना नहीं गया JSON, सादा टेक्स्ट या `{"decision": "deny"}` के अलावा कोई और आउटपुट मिलता है, तो रनटाइम, रिस्पॉन्स को मंज़ूरी (`allow`) के तौर पर मानता है.

### `post_tool_execution`

यह टूल के पूरा होने के तुरंत बाद ट्रिगर होता है. आपकी स्क्रिप्ट, `stdin` से एक्ज़ीक्यूशन की जानकारी और गड़बड़ी की स्थिति को पढ़ती है.

**इनपुट पेलोड (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

अगर कोई शेल कमांड, स्टैंडर्ड गड़बड़ी (`stderr`) में गड़बड़ियां प्रिंट करती है या फ़ाइल सिस्टम का कोई ऑपरेशन पूरा नहीं होता है, तो गड़बड़ी के टेक्स्ट वाला `"error"` फ़ील्ड, पेलोड में शामिल किया जाता है. जब कमांड बिना किसी गड़बड़ी के पूरी हो जाती है, तो `"error"` फ़ील्ड को पूरी तरह से हटा दिया जाता है.

**आउटपुट रिस्पॉन्स (`stdout`):**

```
{}
```

टूल के बाद चलने वाले हुक, सिर्फ़ बैकग्राउंड टास्क के लिए काम करते हैं. जैसे, कोड फ़ॉर्मैट करना या लॉग करना. इसलिए, रनटाइम `stdout` पर दिखाई गई किसी भी फ़ैसले की वैल्यू को अनदेखा कर देता है.

## कॉन्फ़िगरेशन की जानकारी

रनटाइम, सैंडबॉक्स एनवायरमेंट में मौजूद `.agents/hooks.json` या `/.agents/hooks.json` से हुक की परिभाषाओं का अपने-आप पता लगाता है. [एनवायरमेंट सोर्स](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi#mount_from_a_source) के साथ काम करने वाले किसी भी सोर्स का इस्तेमाल करके, अपनी कस्टम स्क्रिप्ट के साथ `hooks.json` दिया जा सकता है:

- **डेटा स्टोर करने की जगह को माउंट करना**: यह एक Git डेटा स्टोर करने की जगह होती है, जिसमें `AGENTS.md` के साथ-साथ `.agents/hooks.json` भी शामिल होता है.
- **Cloud Storage (`gcs`)**: यह GCS बकेट है, जिसमें `hooks.json` को एनवायरमेंट में कॉपी किया गया है.
- **इनलाइन सोर्स**: `client.interactions.create` को कॉल करते समय, `environment.sources` में पास की गई रॉ JSON स्ट्रिंग और स्क्रिप्ट का कॉन्टेंट.

### `hooks.json` स्कीमा

`hooks.json` फ़ाइल, कस्टम नामों के तहत इवेंट डेफ़िनिशन (`pre_tool_execution` या `post_tool_execution`) को ग्रुप करती है. हर ग्रुप के लिए, इस सुविधा को अलग-अलग चालू या बंद किया जा सकता है:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### मैचर का सिंटैक्स और नियम

`hooks.json` में मौजूद हर नियम ग्रुप यह तय करता है कि `matcher` और `hooks` प्रॉपर्टी का इस्तेमाल करके, हैंडलर कब और कैसे ट्रिगर होंगे:

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `enabled` | `boolean` | ज़रूरी नहीं. ग्रुप को बंद करने के लिए, इसे `false` पर सेट करें (डिफ़ॉल्ट रूप से `true` पर सेट होता है). |
| `matcher` | `string` | कंटेनर में मौजूद टारगेट टूल के नामों से मेल खाने वाला रेगुलर एक्सप्रेशन पैटर्न. |
| `hooks` | `array` | हैंडलर की परिभाषाओं की क्रम वाली सूची (`command` या `http`). हैंडलर, क्रम से लागू होते हैं. |

#### रेगुलर एक्सप्रेशन के आकलन का तरीका

जब एजेंट, सैंडबॉक्स में किसी टूल को शुरू करता है, तो रनटाइम, टूल के कंटेनर के नाम की तुलना आपके `matcher` पैटर्न से करता है. इसके लिए, स्टैंडर्ड RE2 रेगुलर एक्सप्रेशन का इस्तेमाल किया जाता है. अगर रेगुलर एक्सप्रेशन, टूल के नाम से मेल खाता है, तो `hooks` ऐरे में मौजूद सभी हैंडलर क्रम से काम करते हैं. अगर एक से ज़्यादा नियम ग्रुप, एक ही टूल से मैच करते हैं, तो उनसे जुड़े सभी हैंडलर ऐरे चलते हैं.

आपके पास किसी भी बिल्ट-इन कंटेनर टूल के नाम को टारगेट करने का विकल्प होता है: कोड एक्ज़ीक्यूशन (`code_execution`) या फ़ाइल सिस्टम ऑपरेशन (`view_file`, `write_to_file`, `replace_file_content`, `list_dir`, और `delete_file`).

#### मैचर के सामान्य एक्सप्रेशन

- `"code_execution"`: शेल कमांड और स्क्रिप्ट को चलाने के लिए, स्ट्रिंग का सटीक मिलान.
- `"write_to_file"`: फ़ाइल सिस्टम में फ़ाइल बनाने और डिस्क पर डेटा लिखने के लिए, पूरी तरह से मेल खाने वाला पैटर्न.
- `"view_file|write_to_file"`: पाइप से अलग किए गए टूल के नाम, एक ही नियम में कई टूल के नामों से मेल खाते हैं.
- `".*_file"`: रेगुलर एक्सप्रेशन वाइल्डकार्ड, `_file` पर खत्म होने वाले किसी भी टूल से मैच करता है. जैसे, `view_file`, `write_to_file` या `delete_file`. इसमें फ़ाइल सिस्टम टूलसेट का सिर्फ़ एक हिस्सा शामिल होता है. `replace_file_content` और `list_dir`, `_file` पर खत्म नहीं होते हैं. इसलिए, जब आपको इनकी ज़रूरत हो, तब इनके नाम साफ़ तौर पर बताएं. स्टैंडर्ड RE2 रेगुलर एक्सप्रेशन के लिए `.*` की ज़रूरत होती है; `*_file` जैसे सामान्य शेल ग्लोब, रेगुलर एक्सप्रेशन के अमान्य सिंटैक्स होते हैं और इनसे कोई मैच नहीं मिलेगा.
- `".*"` या `"*"` या `""`: यह एक ऐसा पैटर्न है जो कंटेनर में मौजूद हर टूल कॉल को इंटरसेप्ट करता है.

## हैंडलर के टाइप

### कमांड हुक

कमांड हुक, सैंडबॉक्स में शेल कमांड या स्क्रिप्ट को एक्ज़ीक्यूट करते हैं. स्क्रिप्ट को `stdin` पर इवेंट JSON मिलता है और वह `stdout` पर फ़ैसले का JSON आउटपुट करती है.

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `type` | `string` | `"command"` होना चाहिए. |
| `command` | `string` | सैंडबॉक्स में चलाने के लिए कमांड लाइन (उदाहरण के लिए, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | टाइम आउट होने का समय, सेकंड में. डिफ़ॉल्ट: `30`. |

### एचटीटीपी हुक

एचटीटीपी हुक, इवेंट JSON को POST अनुरोध के तौर पर, सैंडबॉक्स नेटवर्क से सीधे किसी बाहरी एचटीटीपीएस यूआरएल पर भेजते हैं. टारगेट सर्वर, एचटीटीपी रिस्पॉन्स बॉडी में अपना फ़ैसला दिखाता है. इसके लिए, वह ठीक उसी JSON फ़ॉर्मैट (`{"decision": "allow"}` या `{"decision": "deny", "reason": "..."}`) का इस्तेमाल करता है.

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `type` | `string` | `"http"` होना चाहिए. |
| `url` | `string` | इवेंट पेलोड को पोस्ट करने के लिए, एक्सटर्नल एचटीटीपीएस एंडपॉइंट. |
| `headers` | `object` | गैर-संवेदनशील कस्टम हेडर (जैसे, `{"X-Event-Source": "agent-sandbox"}`) के लिए, वैकल्पिक की-वैल्यू पेयर. पुष्टि करने के लिए, नेटवर्क की अनुमति वाली सूची में मौजूद [क्रेडेंशियल](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=hi) का इस्तेमाल करें. |
| `timeout` | `integer` | टाइम आउट होने का समय, सेकंड में. डिफ़ॉल्ट: `30`. |

#### ईग्रैस प्रॉक्सी और टोकन ट्रांसफ़ॉर्मेशन

एचटीटीपी हुक, सैंडबॉक्स नेटवर्क नेमस्पेस के अंदर से सीधे तौर पर एक्ज़ीक्यूट होते हैं. इसलिए, आउटगोइंग अनुरोध, ट्रांसपैरंट इग्रेस प्रॉक्सी से होकर गुज़रते हैं. इस आर्किटेक्चर से, आपको सुरक्षा से जुड़े दो अहम फ़ायदे मिलते हैं:

- **नेटवर्क की अनुमति वाली सूची:** टारगेट एंडपॉइंट को आपके एनवायरमेंट के `network.allowlist` में साफ़ तौर पर अनुमति दी जानी चाहिए. लूपबैक ट्रैफ़िक (`127.0.0.1` या `localhost`) को प्रॉक्सी ब्लॉक करती है. इसलिए, हमेशा उन बाहरी एंडपॉइंट को टारगेट करें जिन्हें अनुमति दी गई है.
- **क्रेडेंशियल इंजेक्ट करना:** आपको एपीआई पासकोड या सीक्रेट बियरर टोकन को `.agents/hooks.json` में सेव करने या उन्हें कंटेनर में माउंट करने की ज़रूरत नहीं है. सीक्रेट को एक बार [क्रेडेंशियल](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=hi) के तौर पर सेव करें. इसके बाद, अपने एनवायरमेंट के `network.allowlist` से आईडी के ज़रिए इसे रेफ़रंस करें. ईग्रैस प्रॉक्सी, आउटगोइंग एचटीटीपी हुक ट्रैफ़िक को अपने-आप इंटरसेप्ट कर लेता है. साथ ही, सैंडबॉक्स छोड़ने से पहले वायर पर असली पुष्टि करने वाला हेडर डाल देता है. इनलाइन `transform` नियम, वायर पर हेडर को उसी तरह सेट करते हैं. क्रेडेंशियल का इस्तेमाल तब किया जाता है, जब आपको पूरे प्रोजेक्ट में सीक्रेट का फिर से इस्तेमाल करना हो और उसे एक ही जगह पर रोटेट करना हो. [नेटवर्क कॉन्फ़िगरेशन](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi#network-configuration) देखें.

## रनटाइम, फ़ैसलों और गड़बड़ियों को कैसे मैनेज करता है

- **सिंक्रोनस वेटिंग:** एजेंट, आपके हुक के पूरा होने तक रुक जाता है. इसके बाद ही, वह आगे बढ़ता है.
- **टूल के इस्तेमाल को रोकना:** अगर आपका प्री-टूल हुक `{"decision": "deny", "reason": "<your reason>"}` दिखाता है, तो रनटाइम तुरंत टूल कॉल को रद्द कर देता है. मॉडल, बातचीत के इतिहास में जवाब अस्वीकार करने की वजह देखता है. इसके बाद, वह सुरक्षित विकल्प चुनकर या उपयोगकर्ता को ब्लॉक करने की वजह बताकर, जवाब को अडैप्ट करता है.
- **स्क्रिप्ट क्रैश, एचटीटीपी गड़बड़ियों, और टाइमआउट को मैनेज करना:** अगर कोई कमांड स्क्रिप्ट क्रैश हो जाती है (नॉन-ज़ीरो एक्ज़िट स्टेटस), कोई एचटीटीपी हुक नॉन-2xx स्टेटस कोड दिखाता है (जैसे कि 4xx या 5xx सर्वर गड़बड़ी), कोई ऑपरेशन टाइम आउट हो जाता है या अपरिचित JSON दिखाता है, तो रनटाइम इसे मंज़ूरी (`allow`) के तौर पर मानता है. टूल का इस्तेमाल सामान्य तरीके से जारी रहता है, ताकि खराब स्क्रिप्ट या टेलीमेट्री सर्वर तक न पहुंच पाने की वजह से आपका ऐप्लिकेशन कभी भी लॉक न हो.

## इस्तेमाल के सामान्य उदाहरण

### डेटा की निजता और नियमों का पालन करने के लिए, कई बार में डेटा वापस पाने की सुविधा

जब कोई हुक, पाबंदी वाले संसाधनों का ऐक्सेस ब्लॉक करता है, तब `previous_interaction_id` को अगले कॉल पर पास किया जा सकता है, ताकि उसी एनवायरमेंट में टर्न जारी रखा जा सके. पाबंदी वाले संसाधनों में, व्यक्तिगत पहचान से जुड़ी जानकारी (पीआईआई) या गोपनीय वित्तीय रिकॉर्ड वाली डायरेक्ट्री शामिल होती हैं. एजेंट, अनुरोध अस्वीकार किए जाने की वजह पढ़ता है. इसके बाद, वह मंज़ूरी वाली सार्वजनिक टेबल से क्वेरी करके, अपने-आप ठीक हो जाता है.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "view_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### बाहरी ऑडिट लॉगिंग और टेलीमेट्री

जब भी फ़ाइलें पढ़ी या बदली जाती हैं, तब सैंडबॉक्स से रीयल-टाइम ऑडिट इवेंट को किसी बाहरी मॉनिटरिंग सर्वर पर भेजें.

- **एक से ज़्यादा टूल को मैच करना:** मैच करने वाले टूल, स्टैंडर्ड रेगुलर एक्सप्रेशन का इस्तेमाल करते हैं. इसलिए, पाइप (`view_file|write_to_file|replace_file_content`) या वाइल्डकार्ड (`.*_file`) का इस्तेमाल करके, एक ही नियम में कई टूल को जोड़ा जा सकता है.
- **अपने कॉन्फ़िगरेशन में सीक्रेट न रखें:** पुष्टि करने वाले टोकन को [क्रेडेंशियल](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=hi) के तौर पर सेव करें. साथ ही, इसे अपने एनवायरमेंट के [नेटवर्क कॉन्फ़िगरेशन](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi#network-configuration) (`network.allowlist.credential`) से आईडी के हिसाब से रेफ़रंस करें. इग्रेस प्रॉक्सी, आउटगोइंग अनुरोधों पर असली बियरर टोकन इंजेक्ट करता है. इस उदाहरण में, हेडर को `transform` के साथ इनलाइन सेट किया गया है. इसे उसी प्रॉक्सी से सुरक्षित किया जाता है. साथ ही, यह तब काम करता है, जब टोकन इस कॉन्फ़िगरेशन से जुड़ा हो.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "view_file|write_to_file|replace_file_content",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "view_file|write_to_file|replace_file_content",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## सीमाएं

- **सैंडबॉक्स टूल का दायरा:** हुक, सैंडबॉक्स में मौजूद बिल्ट-इन टूल को इंटरसेप्ट करते हैं: कोड एक्ज़ीक्यूशन (`code_execution`) और फ़ाइल सिस्टम के ऑपरेशन (`view_file`, `write_to_file`, `replace_file_content`, `list_dir`, और `delete_file`). ये कस्टम फ़ंक्शन कॉलिंग (`function`) या बाहरी मॉडल कॉन्टेक्स्ट प्रोटोकॉल (`mcp_server`) टूल के लिए ट्रिगर नहीं होते हैं. इन टूल को कंटेनर के बाहर मैनेज किया जाता है.
- **नेटवर्क की अनुमति वाली सूचियां:** एचटीटीपी हुक, कंटेनर नेटवर्क में चलते हैं. आपको अपने एनवायरमेंट के `network.allowlist` में टारगेट किए गए यूआरएल को साफ़ तौर पर अनुमति देनी होगी. लूपबैक पतों (`localhost`, `127.0.0.1`) को प्रॉक्सी ने ब्लॉक किया है.
- **गड़बड़ियों पर अपने-आप मंज़ूरी मिलना:** अगर कोई हुक स्क्रिप्ट क्रैश हो जाती है (शून्य से अलग एक्ज़िट स्टेटस), उसका समय खत्म हो जाता है या वह काम नहीं करती है, तो रनटाइम गड़बड़ी को लॉग करता है और टूल कॉल को जारी रखने की अनुमति देता है. इससे यह पक्का होता है कि लिंटर स्क्रिप्ट या हैंगिंग प्रोसेस में गड़बड़ी होने पर, आपके ऐप्लिकेशन कभी भी डेडलॉक न हों.
- **सैंडबॉक्स कॉन्फ़िगरेशन की सुरक्षा:** हुक, कंटेनर सैंडबॉक्स में एक्ज़ीक्यूट होते हैं. इसलिए, फ़ाइल सिस्टम में डेटा सेव करने वाले टूल या शेल कोड को एक्ज़ीक्यूट करने की अनुमतियां रखने वाले एजेंट, लिखने की अनुमति वाले वर्कस्पेस में मौजूद लोकल `.agents/hooks.json` या स्क्रिप्ट में बदलाव कर सकते हैं. नीति से जुड़ी जानकारी और ऑपरेशनल गार्डरेल के तौर पर, कंटेनर हुक का इस्तेमाल करें. अगर गैर-भरोसेमंद मॉडल के एक्ज़ीक्यूशन के ख़िलाफ़, छेड़छाड़ को रोकने के लिए सख्त सुरक्षा की ज़रूरत है, तो रीड-ओनली रिपॉज़िटरी से कॉन्फ़िगरेशन सोर्स माउंट करें.

## आगे क्या करना है

- परसिस्टेंट [रिमोट सैंडबॉक्स और एनवायरमेंट](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi) को कॉन्फ़िगर करने का तरीका जानें.
- [Antigravity एजेंट](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi) की क्षमताओं और पहले से मौजूद टूल के बारे में जानें.
- सिलसिलेवार बातचीत वाले सेशन और स्ट्रीमिंग के लिए, [Interactions API की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया."],[],[]]
