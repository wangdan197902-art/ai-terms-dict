---
title: "机器遗忘"
term_id: "machine_unlearning"
category: "training_techniques"
subcategory: ""
tags: ["privacy", "ethics", "maintenance"]
difficulty: 4
weight: 1
slug: "machine_unlearning"
aliases:
  - /zh/terms/machine_unlearning/
date: "2026-07-18T11:25:23.018243Z"
lastmod: "2026-07-18T11:44:45.529170Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "机器遗忘是指在不从头重新训练模型的情况下，从已训练模型中移除特定数据点或其影响的过程。"
---

## Definition

这项技术通过允许模型在保留通用知识的同时“忘记”特定用户数据，来解决如GDPR“被遗忘权”等隐私法规问题。其目标是近似于从头重新训...

### Summary

机器遗忘是指在不从头重新训练模型的情况下，从已训练模型中移除特定数据点或其影响的过程。

## Key Concepts

- 被遗忘权
- 模型重训练近似
- 数据隐私
- 梯度更新

## Use Cases

- 遵守数据删除请求
- 从模型中移除有偏见或错误的数据
- 减轻数据投毒攻击的影响

## Related Terms

- [Data Privacy (数据隐私)](/en/terms/data-privacy-数据隐私/)
- [Federated Learning (联邦学习)](/en/terms/federated-learning-联邦学习/)
- [Model Retraining (模型重训练)](/en/terms/model-retraining-模型重训练/)
- [GDPR (通用数据保护条例)](/en/terms/gdpr-通用数据保护条例/)
