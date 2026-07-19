---
title: 数据增强
term_id: data_augmentation
category: training_techniques
subcategory: ''
tags:
- Machine Learning
- preprocessing
- cv
difficulty: 2
weight: 1
slug: data_augmentation
date: '2026-07-18T11:12:24.479703Z'
lastmod: '2026-07-18T11:44:45.471065Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 数据增强是一种通过变换现有数据点来增加训练数据集多样性和规模的技术。
---
## Definition

这种方法通过创建现有样本的修改版本来人工扩展训练数据集，例如旋转图像、在音频中添加噪声或在文本中进行同义词替换。它有助于防止……

### Summary

数据增强是一种通过变换现有数据点来增加训练数据集多样性和规模的技术。

## Key Concepts

- 防止过拟合
- 数据集扩展
- 泛化能力
- 变换

## Use Cases

- 提高计算机视觉模型的鲁棒性
- 在有限文本下增强自然语言处理模型的性能
- 平衡不平衡的数据集

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (正则化)](/en/terms/regularization-正则化/)
- [Synthetic Data (合成数据)](/en/terms/synthetic-data-合成数据/)
- [Transfer Learning (迁移学习)](/en/terms/transfer-learning-迁移学习/)
- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
