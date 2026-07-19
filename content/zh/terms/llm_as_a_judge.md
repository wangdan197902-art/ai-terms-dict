---
title: 大模型作为裁判
term_id: llm_as_a_judge
category: application_paradigms
subcategory: ''
tags:
- evaluation
- LLM Application
- NLP
difficulty: 3
weight: 1
slug: llm_as_a_judge
date: '2026-07-18T11:23:29.760163Z'
lastmod: '2026-07-18T11:44:45.522419Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种通过使用另一个大语言模型根据标准对响应进行评分或排名，从而评估大语言模型输出的方法。
---
## Definition

“大模型作为裁判”（LLM-as-a-Judge）是一种评估范式，其中大语言模型充当其他模型输出质量的自动化评估者。这种方法旨在减少对人工标注员或严格规则匹配的依赖，通过提示工程让LLM根据特定标准（如相关性、安全性、创造性等）对生成内容进行打分或排序，从而提高评估效率和一致性。

### Summary

一种通过使用另一个大语言模型根据标准对响应进行评分或排名，从而评估大语言模型输出的方法。

## Key Concepts

- 自动化评估
- 提示工程
- 模型对齐
- 质量指标

## Use Cases

- RLHF模型的基准测试
- 创意写作评估
- 安全性和偏见检测

## Related Terms

- [rlhf (基于人类反馈的强化学习)](/en/terms/rlhf-基于人类反馈的强化学习/)
- [evaluation_metrics (评估指标)](/en/terms/evaluation_metrics-评估指标/)
- [prompt_engineering (提示工程)](/en/terms/prompt_engineering-提示工程/)
- [model_alignment (模型对齐)](/en/terms/model_alignment-模型对齐/)
