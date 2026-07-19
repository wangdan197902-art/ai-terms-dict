---
title: Few-Shot Prompting
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T09:40:59.277390Z'
lastmod: '2026-07-18T11:44:44.624944Z'
draft: false
source: agnes_llm
status: published
language: en
description: Few-shot prompting is a technique where LLMs are provided with a small
  number of input-output examples within the prompt to guide their behavior.
---
## Definition

This method leverages the in-context learning capabilities of large language models by providing a few illustrative examples directly in the prompt. Unlike fine-tuning, which requires updating model weights, few-shot prompting allows users to steer the model's output format, tone, or logic dynamically. It is highly effective for tasks like classification, translation, or code generation where specific patterns need to be demonstrated to the model before generating the final response.

### Summary

Few-shot prompting is a technique where LLMs are provided with a small number of input-output examples within the prompt to guide their behavior.

## Key Concepts

- In-context learning
- Prompt engineering
- Example-based guidance
- Zero-shot comparison

## Use Cases

- Sentiment analysis formatting
- Code style adaptation
- Structured data extraction

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot](/en/terms/zero_shot/)
- [prompt_engineering](/en/terms/prompt_engineering/)
- [in_context_learning](/en/terms/in_context_learning/)
- [llm](/en/terms/llm/)
