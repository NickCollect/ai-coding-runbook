# Model optimization and fine-tuning

<!-- source: https://platform.openai.com/docs/guides/fine-tuning -->

LLM output is non-deterministic, and model behavior changes between model snapshots and families. Developers must constantly measure and tune performance.

## Model optimization workflow

1. Write evals that measure model output, establishing a baseline
2. Prompt the model for output with relevant context and instructions
3. Optionally fine-tune a model for a specific task
4. Run evals using representative test data
5. Tweak your prompt or fine-tuning dataset based on eval feedback
6. Repeat continuously

## Fine-tuning methods

### Supervised Fine-Tuning (SFT)
Provide examples of correct responses to guide model behavior. Uses human-generated "ground truth" responses.

**Best for**: Classification, nuanced translation, generating content in a specific format, correcting instruction-following failures.

**Supported models**: `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`

### Vision Fine-Tuning
Provide image inputs for supervised fine-tuning to improve image understanding.

**Supported models**: `gpt-4o-2024-08-06`

### Direct Preference Optimization (DPO)
Provide both a correct and incorrect example response for a prompt. Indicate the correct response.

**Best for**: Summarizing text with right focus, generating chat messages with right tone/style.

**Supported models**: `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`

### Reinforcement Fine-Tuning (RFT)
Generate a response, provide an expert grade, and reinforce the model's chain-of-thought for higher-scored responses.

**Best for**: Complex domain-specific tasks requiring advanced reasoning, medical diagnoses, legal case law analysis.

**Supported models**: `o4-mini-2025-04-16`

## Fine-tuning process

1. Collect a dataset of examples for training data
2. Upload dataset to OpenAI, formatted in JSONL
3. Create a fine-tuning job (dashboard or API)
4. For RFT: define a grader to score model behavior
5. Evaluate results

## Benefits over prompting alone

- Provide more example inputs/outputs than fit in context window
- Use shorter prompts with fewer examples (saves token costs)
- Train on proprietary/sensitive data without including in every request
- Train a smaller, cheaper, faster model for a particular task

## Prompt engineering

Before fine-tuning, try prompt engineering first:
- Include relevant context in instructions
- Provide clear instructions with explicit goals
- Provide example outputs (few-shot learning)
