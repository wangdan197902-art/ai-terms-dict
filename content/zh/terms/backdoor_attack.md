---
title: "后门攻击"
term_id: "backdoor_attack"
category: "ethics_safety"
subcategory: ""
tags: ["AI Security", "Ethics", "Adversarial ML"]
difficulty: 4
weight: 1
slug: "backdoor_attack"
date: "2026-07-18T11:38:27.568103Z"
lastmod: "2026-07-18T11:44:45.570248Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种安全威胁，恶意行为者在训练期间将隐藏触发器嵌入 AI 模型，导致特定错误分类。"
---
## Definition

后门攻击涉及使用特定的模式（称为触发器）对机器学习模型的训练数据进行投毒。虽然模型在干净数据上表现正常，但在检测到触发器时会激活错误的行为，例如将特定图像错误分类为指定标签，

### Summary

一种安全威胁，恶意行为者在训练期间将隐藏触发器嵌入 AI 模型，导致特定错误分类。

## Key Concepts

- 数据投毒
- 模型完整性
- 对抗性机器学习
- 触发模式

## Use Cases

- ML 流水线的安全测试
- 开发防御过滤器
- 审计第三方模型

## Related Terms

- [Adversarial Examples (对抗样本)](/en/terms/adversarial-examples-对抗样本/)
- [Data Poisoning (数据投毒)](/en/terms/data-poisoning-数据投毒/)
- [Model Robustness (模型鲁棒性)](/en/terms/model-robustness-模型鲁棒性/)
- [Clean Label Attacks (干净标签攻击)](/en/terms/clean-label-attacks-干净标签攻击/)
