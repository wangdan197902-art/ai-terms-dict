---
title: "自洽性"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
aliases:
  - /zh/terms/self_consistency/
date: "2026-07-18T11:32:54.019434Z"
lastmod: "2026-07-18T11:44:45.552424Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "自洽性是一种解码策略，其中采样多个推理路径，并选择出现频率最高的答案作为最终输出。"
---

## Definition

该技术主要用于大型语言模型（LLM），通过采样生成针对同一提示的多个多样化响应来提高准确性。与依赖贪婪解码不同，它聚合

### Summary

自洽性是一种解码策略，其中采样多个推理路径，并选择出现频率最高的答案作为最终输出。

## Key Concepts

- 多数投票
- 解码策略
- LLM推理
- 减少幻觉

## Use Cases

- 数学应用题
- 复杂逻辑推导
- 代码合成任务

## Related Terms

- [思维链 (Chain-of-thought，引导模型逐步推理的技术)](/en/terms/思维链-chain-of-thought-引导模型逐步推理的技术/)
- [温度采样 (Temperature sampling，控制生成文本随机性的参数)](/en/terms/温度采样-temperature-sampling-控制生成文本随机性的参数/)
- [集成方法 (Ensemble methods，结合多个模型预测以提高准确性的技术)](/en/terms/集成方法-ensemble-methods-结合多个模型预测以提高准确性的技术/)
- [提示工程 (Prompt engineering，设计和优化输入提示以改善模型输出的技术)](/en/terms/提示工程-prompt-engineering-设计和优化输入提示以改善模型输出的技术/)
