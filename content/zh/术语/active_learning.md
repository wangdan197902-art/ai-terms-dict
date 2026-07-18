---
title: "主动学习"
term_id: "active_learning"
category: "training_techniques"
subcategory: ""
tags: ["supervised_learning", "efficiency", "annotation"]
difficulty: 3
weight: 1
slug: "active_learning"
aliases:
  - /zh/terms/active_learning/
date: "2026-07-18T11:04:13.788381Z"
lastmod: "2026-07-18T11:44:45.438398Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种机器学习策略，算法选择性地查询用户或专家来标记新数据点，从而优化训练过程。"
---

## Definition

主动学习通过允许模型选择最具信息量的实例进行人工标记，减少了所需标记数据的数量。与被动接收随机样本不同，算法会主动识别那些最能提升模型性能的数据点进行查询。

### Summary

一种机器学习策略，算法选择性地查询用户或专家来标记新数据点，从而优化训练过程。

## Key Concepts

- 查询策略
- 标记效率
- 不确定性采样
- 人在回路

## Use Cases

- 由放射科专家进行医学图像标注
- 稀有方言的情感分析标记
- 自动驾驶场景的选择

## Related Terms

- [semi-supervised learning (半监督学习)](/en/terms/semi-supervised-learning-半监督学习/)
- [query strategies (查询策略)](/en/terms/query-strategies-查询策略/)
- [data annotation (数据标注)](/en/terms/data-annotation-数据标注/)
- [label efficiency (标记效率)](/en/terms/label-efficiency-标记效率/)
