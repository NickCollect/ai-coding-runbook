# Safety best practices

<!-- source: https://platform.openai.com/docs/guides/safety-best-practices -->

## Use the free Moderation API

OpenAI's Moderation API is free-to-use and can help reduce the frequency of unsafe content in completions. Alternatively, develop your own content filtration system tailored to your use case.

## Adversarial testing ("red-teaming")

Test your product over a wide range of inputs and user behaviors:
- Representative inputs
- Inputs from someone trying to "break" the application
- Prompt injection attempts ("ignore the previous instructions and do this instead")

## Human in the loop (HITL)

Have a human review outputs before they are used in practice — especially critical for:
- High-stakes domains
- Code generation

Humans should be aware of system limitations and have access to information needed to verify outputs.

## Prompt engineering

Constraining the topic and tone via prompt reduces the chance of producing undesired content. Provide additional context (few-shot examples of desired behavior) to steer outputs.

## "Know your customer" (KYC)

Require user registration/login. Consider linking to existing accounts (Gmail, LinkedIn). Credit card or ID verification reduces risk further.

## Constrain user input and limit output tokens

- Limit text a user can input to prevent prompt injection
- Limit output tokens to reduce chance of misuse
- Use dropdown fields instead of open-ended text where possible
- Return outputs from a validated set of materials when possible (e.g., route to existing support articles rather than generating from scratch)

## Allow users to report issues

Provide an easily available method for reporting improper functionality. Monitor and respond appropriately.

## Safety identifiers

Send `safety_identifier` in API requests to help OpenAI detect abuse. Should be a unique, hashed string (hash username/email to avoid sending PII). Use session ID for non-logged-in users.

## Report security issues

Submit through OpenAI's Coordinated Vulnerability Disclosure Program: https://openai.com/security/disclosure/
