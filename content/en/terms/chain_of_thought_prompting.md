---
title: "Chain-of-Thought Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T09:40:12.571011Z"
lastmod: "2026-07-18T11:44:44.621438Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Chain-of-Thought Prompting is a technique that encourages LLMs to generate intermediate reasoning steps before producing a final answer."
---
## Definition

Chain-of-Thought (CoT) prompting improves the performance of large language models on complex reasoning tasks by explicitly asking the model to articulate its step-by-step logic. Instead of jumping directly to a conclusion, the model generates intermediate sentences that represent its thought process. This approach mimics human problem-solving strategies, significantly enhancing accuracy in mathematics, logic puzzles, and multi-step deductions. It can be implemented via few-shot examples or simple instructions like 'Let's think step by step.'

### Summary

Chain-of-Thought Prompting is a technique that encourages LLMs to generate intermediate reasoning steps before producing a final answer.

## Key Concepts

- Step-by-Step Reasoning
- Few-Shot Learning
- Logical Deduction
- Intermediate Steps

## Use Cases

- Solving mathematical word problems
- Complex logical reasoning tasks
- Debugging code generation errors

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting](/en/terms/zero-shot-prompting/)
- [Few-Shot Prompting](/en/terms/few-shot-prompting/)
- [Self-Consistency](/en/terms/self-consistency/)
- [Reasoning](/en/terms/reasoning/)
