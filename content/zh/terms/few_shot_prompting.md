---
title: 少样本提示
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
date: '2026-07-18T11:00:03.938758Z'
lastmod: '2026-07-18T11:44:45.400282Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 少样本提示是一种技术，通过在提示词中提供少量输入-输出示例来引导大型语言模型的行为。
---
## Definition

这种方法利用大型语言模型的上下文学习能力，直接在提示词中提供几个说明性示例。与需要更新模型权重的微调不同，少样本提示通过展示期望的输出格式或逻辑，让模型在不重新训练的情况下适应新任务。

### Summary

少样本提示是一种技术，通过在提示词中提供少量输入-输出示例来引导大型语言模型的行为。

## Key Concepts

- 上下文学习
- 提示工程
- 基于示例的引导
- 零样本对比

## Use Cases

- 情感分析格式化
- 代码风格适配
- 结构化数据提取

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

- [zero_shot (零样本)](/en/terms/zero_shot-零样本/)
- [prompt_engineering (提示工程)](/en/terms/prompt_engineering-提示工程/)
- [in_context_learning (上下文学习)](/en/terms/in_context_learning-上下文学习/)
- [llm (大型语言模型)](/en/terms/llm-大型语言模型/)
