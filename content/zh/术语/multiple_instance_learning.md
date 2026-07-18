---
title: "多示例学习"
term_id: "multiple_instance_learning"
category: "training_techniques"
subcategory: ""
tags: ["supervised_learning", "weak_labeling", "ml_paradigm"]
difficulty: 4
weight: 1
slug: "multiple_instance_learning"
aliases:
  - /zh/terms/multiple_instance_learning/
date: "2026-07-18T11:01:16.765817Z"
lastmod: "2026-07-18T11:44:45.403166Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种弱监督学习范式，标签被分配给实例集合（包），而非单个实例。"
---

## Definition

多示例学习（MIL）解决的是数据被分组为具有单一标签的“包”，而包内的各个实例未标记的场景。通常，如果一个包中包含至少一个正例实例，则该包被标记为正例；否则为负例。

### Summary

一种弱监督学习范式，标签被分配给实例集合（包），而非单个实例。

## Key Concepts

- 包级标注
- 实例级不确定性
- 弱监督
- 正/负包逻辑

## Use Cases

- 药物活性预测
- 基于边界框的图像分类
- 基于内容的图像检索

## Related Terms

- [weak_supervision (弱监督)](/en/terms/weak_supervision-弱监督/)
- [bagging (装袋法)](/en/terms/bagging-装袋法/)
- [instance_classification (实例分类)](/en/terms/instance_classification-实例分类/)
- [label_noise (标签噪声)](/en/terms/label_noise-标签噪声/)
