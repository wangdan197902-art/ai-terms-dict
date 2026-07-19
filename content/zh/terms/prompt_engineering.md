---
title: "提示工程"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T07:43:58.206652Z"
lastmod: "2026-07-18T11:44:44.590070Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "设计和优化输入文本，以引导大型语言模型生成预期输出的实践。"
---
## Definition

提示工程涉及制作特定的输入（即提示），以从生成式 AI 模型中获取准确、相关且高质量的响应。它要求理解模型如何解释指令、上下文及约束条件，从而通过调整提示词的结构和措辞来最大化模型的表现。

### Summary

设计和优化输入文本，以引导大型语言模型生成预期输出的实践。

## Key Concepts

- 语境框架
- 少样本学习
- 指令微调
- 令牌优化

## Use Cases

- 自动化客户支持聊天机器人
- 代码生成助手
- 创意写作辅助工具

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (大型语言模型)](/en/terms/llm-大型语言模型/)
- [Chain-of-Thought (思维链)](/en/terms/chain-of-thought-思维链/)
- [RAG (检索增强生成)](/en/terms/rag-检索增强生成/)
- [Fine-tuning (微调)](/en/terms/fine-tuning-微调/)
