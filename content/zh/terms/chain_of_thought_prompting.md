---
title: "思维链提示 (Chain-of-Thought Prompting)"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T10:59:27.500291Z"
lastmod: "2026-07-18T11:44:45.397750Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "思维链提示是一种鼓励大语言模型在生成最终答案之前，先生成中间推理步骤的技术。"
---
## Definition

思维链（CoT）提示通过明确要求模型阐述其逐步逻辑，从而提升大型语言模型在复杂推理任务上的表现。与直接跳跃到最终答案不同，CoT引导模型展示其思考过程，这有助于解决需要多步逻辑推导的问题，如数学应用题或复杂的逻辑推理任务。

### Summary

思维链提示是一种鼓励大语言模型在生成最终答案之前，先生成中间推理步骤的技术。

## Key Concepts

- 逐步推理
- 少样本学习
- 逻辑演绎
- 中间步骤

## Use Cases

- 解决数学应用题
- 复杂逻辑推理任务
- 调试代码生成错误

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (零样本提示)](/en/terms/zero-shot-prompting-零样本提示/)
- [Few-Shot Prompting (少样本提示)](/en/terms/few-shot-prompting-少样本提示/)
- [Self-Consistency (自洽性)](/en/terms/self-consistency-自洽性/)
- [Reasoning (推理)](/en/terms/reasoning-推理/)
