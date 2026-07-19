---
title: 自监督
term_id: self_supervised
category: training_techniques
subcategory: ''
tags:
- Learning Paradigms
- NLP
- scalability
difficulty: 4
weight: 1
slug: self_supervised
date: '2026-07-18T10:57:22.743731Z'
lastmod: '2026-07-18T11:44:45.395310Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 自监督学习是一种技术，模型从输入数据中自动生成标签以学习表示，无需人工标注。
---
## Definition

自监督学习是机器学习的一个子集，其监督信号自动从数据本身派生，消除了手动标注的需求。模型通常通过解决预设的代理任务来学习数据的内在结构和表示。

### Summary

自监督学习是一种技术，模型从输入数据中自动生成标签以学习表示，无需人工标注。

## Key Concepts

-  pretext任务 (代理任务)
- 掩码建模
- 无标签数据
- 表示学习

## Use Cases

- 通过掩码语言建模训练BERT
- 用于图像嵌入的对比学习
- 预测大语言模型中的下一个词元

## Related Terms

- [unsupervised (无监督)](/en/terms/unsupervised-无监督/)
- [contrastive_learning (对比学习)](/en/terms/contrastive_learning-对比学习/)
- [masked_language_modeling (掩码语言建模)](/en/terms/masked_language_modeling-掩码语言建模/)
- [representation_learning (表示学习)](/en/terms/representation_learning-表示学习/)
