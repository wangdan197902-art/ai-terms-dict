---
title: "前缀微调"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /zh/terms/prefix_tuning/
date: "2026-07-18T11:30:18.063193Z"
lastmod: "2026-07-18T11:44:45.544372Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种参数高效的微调方法，通过在变换器层的输入端添加可训练的连续向量来实现适配。"
---

## Definition

前缀微调是一种用于预训练变换器的参数高效适应技术。与更新所有模型权重不同，它在输入序列前prepend（前置）一系列可训练的连续向量（即前缀），从而冻结主干网络并仅优化少量参数以适应新任务。

### Summary

一种参数高效的微调方法，通过在变换器层的输入端添加可训练的连续向量来实现适配。

## Key Concepts

- 参数高效微调
- 软提示
- 变换器层
- 冻结主干

## Use Cases

- 少样本学习适配
- 资源受限下的多任务学习
- 为利基领域定制大型语言模型

## Related Terms

- [prompt_tuning (提示微调)](/en/terms/prompt_tuning-提示微调/)
- [p_tuning (P-Tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (适配器模块)](/en/terms/adapter_modules-适配器模块/)
- [peft (参数高效微调技术)](/en/terms/peft-参数高效微调技术/)
