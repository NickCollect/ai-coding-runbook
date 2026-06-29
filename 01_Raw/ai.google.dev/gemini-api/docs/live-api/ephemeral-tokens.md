---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-CN
fetched_at: 2026-06-29T05:34:34.675120+00:00
title: "\u4e34\u65f6\u4ee4\u724c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 临时令牌

临时令牌是短期有效的身份验证令牌，用于通过 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 访问 Gemini API。它们旨在增强从用户设备直接连接到 API（[客户端到服务器](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn#implementation-approach)的实现）时的安全性。与标准 API 密钥一样，临时令牌可以从 Web 浏览器或移动应用等客户端应用中提取。不过，由于临时令牌会快速过期且可以受到限制，因此它们可显著降低生产环境中的安全风险。当您直接从客户端应用访问 Live API 时，应使用它们来增强 API 密钥安全性。

## 临时令牌的工作原理

临时令牌的大致运作方式如下：

1. 您的客户端（例如 Web 应用）向后端进行身份验证。
2. 您的后端向 Gemini API 的配置服务请求临时令牌。
3. Gemini API 会签发短期有效的令牌。
4. 您的后端会将令牌发送给客户端，以用于与 Live API 的 WebSocket 连接。您可以通过将 API 密钥替换为临时令牌来实现此目的。
5. 然后，客户端会像使用 API 密钥一样使用该令牌。

![临时令牌概览](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=zh-cn)

这有助于提高安全性，因为即使令牌被提取，其有效期也很短，不像部署在客户端的长效 API 密钥。由于客户端直接向 Gemini 发送数据，因此这还可以缩短延迟时间，并避免后端需要代理实时数据。

## 创建临时令牌

以下是一个简化示例，展示了如何从 Gemini 获取临时令牌。
默认情况下，您将有 1 分钟的时间来使用此请求 (`newSessionExpireTime`) 中的令牌启动新的 Live API 会话，并有 30 分钟的时间通过该连接发送消息 (`expireTime`)。

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

有关 `expireTime` 值限制、默认值和其他字段规范，请参阅 [API 参考](https://ai.google.dev/api/live?hl=zh-cn#ephemeral-auth-tokens)。
在 `expireTime` 时间范围内，您需要每 10 分钟重新连接一次通话（即使 `uses: 1`，也可以使用同一令牌完成此操作）。[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn#session-resumption)

还可以将临时令牌锁定到一组配置。这可能有助于进一步提高应用的安全性，并将系统指令保留在服务器端。

### Python

```
from google import genai

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

您还可以锁定部分字段，如需了解详情，请参阅 [SDK 文档](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)。

## 使用临时令牌连接到 Live API

获得临时令牌后，您可以使用它，就像使用 API 密钥一样（但请注意，它仅适用于实时 API，并且仅适用于 `v1alpha` 版本的 API）。

仅当部署遵循[客户端到服务器实现](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn#implementation-approach)方法的应用时，使用临时令牌才有意义。

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

如需查看更多示例，请参阅 [Live API 使用入门](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)。

## 最佳做法

- 使用 `expire_time` 参数设置较短的过期时长。
- 令牌会过期，需要重新启动配置流程。
- 验证您自己的后端的安全身份验证。临时令牌的安全性仅取决于您的后端身份验证方法。
- 一般来说，应避免使用临时令牌进行后端到 Gemini 的连接，因为此路径通常被认为是安全的。

## 限制

临时令牌目前仅与 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 兼容。

## 后续步骤

- 如需了解详情，请参阅 Live API [参考文档](https://ai.google.dev/api/live?hl=zh-cn#ephemeral-auth-tokens)中的临时令牌。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-12。"],[],[]]
