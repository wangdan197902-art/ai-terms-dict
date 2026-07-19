---
title: 模型提取
term_id: model_extraction
category: ethics_safety
subcategory: ''
tags:
- security
- Adversarial ML
difficulty: 4
weight: 1
slug: model_extraction
date: '2026-07-18T11:38:39.318217Z'
lastmod: '2026-07-18T11:44:45.570672Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种攻击方式， adversaries 通过查询模型来重建其参数或创建代理副本。
---
## Definition

模型提取涉及查询目标机器学习模型的 API，以推断其内部结构、权重或决策边界。攻击者利用这些查询构建一个代理模型，从而窃取知识产权或绕过安全限制。

### Summary

一种攻击方式， adversaries 通过查询模型来重建其参数或创建代理副本。

## Key Concepts

- 代理建模
- API 查询
- 知识产权盗窃
- 对抗性攻击

## Use Cases

- 商业 AI API 的安全审计
- 保护专有算法免受克隆
- 研究针对模型提取的防御机制

## Related Terms

- [Membership Inference (成员推断)](/en/terms/membership-inference-成员推断/)
- [Adversarial Examples (对抗样本)](/en/terms/adversarial-examples-对抗样本/)
- [Model Watermarking (模型水印)](/en/terms/model-watermarking-模型水印/)
- [API Security (API 安全)](/en/terms/api-security-api-安全/)
