---
title: "急切学习"
term_id: "eager_learning"
category: "training_techniques"
subcategory: ""
tags: ["learning_paradigms", "training", "inference"]
difficulty: 2
weight: 1
slug: "eager_learning"
aliases:
  - /zh/terms/eager_learning/
date: "2026-07-18T11:15:46.560737Z"
lastmod: "2026-07-18T11:44:45.492611Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "急切学习是一种机器学习方法，其泛化函数在训练阶段就被学习完成，因此在训练结束后能够实现快速的预测时间。"
---

## Definition

在急切学习中，系统在遇到新实例之前，会根据训练数据构建一个通用的目标函数或模型。这与延迟学习形成对比，后者将泛化过程推迟到查询阶段，即直到需要预测时才进行计算。

### Summary

急切学习是一种机器学习方法，其泛化函数在训练阶段就被学习完成，因此在训练结束后能够实现快速的预测时间。

## Key Concepts

- 训练阶段泛化
- 快速推理
- 模型复杂度
- 过拟合风险

## Use Cases

- 实时图像分类
- 欺诈检测系统
- 推荐引擎

## Related Terms

- [延迟学习 (将泛化推迟到测试阶段的策略)](/en/terms/延迟学习-将泛化推迟到测试阶段的策略/)
- [基于实例的学习 (如KNN，属于延迟学习)](/en/terms/基于实例的学习-如knn-属于延迟学习/)
- [监督学习 (从标注数据中学习的方法)](/en/terms/监督学习-从标注数据中学习的方法/)
- [模型训练 (调整模型参数的过程)](/en/terms/模型训练-调整模型参数的过程/)
