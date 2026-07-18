---
title: "彩票假设"
term_id: "lottery_ticket_hypothesis"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "pruning", "theory"]
difficulty: 4
weight: 1
slug: "lottery_ticket_hypothesis"
aliases:
  - /zh/terms/lottery_ticket_hypothesis/
date: "2026-07-18T11:24:46.268053Z"
lastmod: "2026-07-18T11:44:45.527174Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "该理论认为密集神经网络中包含较小的子网络，若从初始状态单独训练，其准确率可与原始网络相匹配。"
---

## Definition

彩票假设指出，在一个大型随机初始化的神经网络中，存在一个稀疏的子网络（即“中奖彩票”），其初始化状态非常适合训练。通过剪枝掉不重要的权重，仅保留并训练这个子网络，可以在不损失性能的前提下大幅减少模型规模。

### Summary

该理论认为密集神经网络中包含较小的子网络，若从初始状态单独训练，其准确率可与原始网络相匹配。

## Key Concepts

- 权重剪枝
- 稀疏网络
- 模型压缩
- 初始化敏感性

## Use Cases

- 在边缘设备上部署轻量级模型
- 降低训练期间的计算成本
- 加速推理速度

## Related Terms

- [Network Pruning (网络剪枝)](/en/terms/network-pruning-网络剪枝/)
- [Model Distillation (模型蒸馏)](/en/terms/model-distillation-模型蒸馏/)
- [Sparse Training (稀疏训练)](/en/terms/sparse-training-稀疏训练/)
- [Efficient AI (高效人工智能)](/en/terms/efficient-ai-高效人工智能/)
