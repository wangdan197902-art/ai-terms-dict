---
title: "上下文学习"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /zh/terms/in_context_learning/
date: "2026-07-18T07:44:46.533449Z"
lastmod: "2026-07-18T11:44:44.592217Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种模型通过观察提示中提供的示例来执行任务的技术。"
---

## Definition

上下文学习（ICL）允许大型语言模型在不更新权重的情况下适应新任务。通过在提示上下文中提供输入-输出对，模型可以推断出模式并执行相应任务。

### Summary

一种模型通过观察提示中提供的示例来执行任务的技术。

## Key Concepts

- 少样本学习
- 零样本
- 提示设计
- 无权重适配

## Use Cases

- 快速测试模型在新数据集上的能力
- 对话代理中的动态任务切换
- 无需重新训练即可原型化AI应用

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [提示工程](/en/terms/提示工程/)
- [少样本](/en/terms/少样本/)
- [零样本](/en/terms/零样本/)
- [元学习](/en/terms/元学习/)
