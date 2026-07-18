---
title: "TensorFlow Hub"
term_id: "tensorflow_hub"
category: "basic_concepts"
subcategory: ""
tags: ["tensorflow", "libraries", "transfer-learning"]
difficulty: 3
weight: 1
slug: "tensorflow_hub"
aliases:
  - /zh/terms/tensorflow_hub/
date: "2026-07-18T11:35:54.969714Z"
lastmod: "2026-07-18T11:44:45.561735Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一个用于可复用机器学习模块的仓库，支持使用预训练模型进行迁移学习。"
---

## Definition

TensorFlow Hub 是一个发布和复用机器学习组件的平台。它允许开发者访问针对图像分类、文本嵌入等各种任务预训练的模型。

### Summary

一个用于可复用机器学习模块的仓库，支持使用预训练模型进行迁移学习。

## Key Concepts

- 迁移学习
- 模块复用
- 预训练模型
- 效率

## Use Cases

- 快速模型原型开发
- 降低训练成本
- 实现最先进的自然语言处理/计算机视觉技术

## Code Example

```python
import tensorflow_hub as hub
module = hub.load('https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5')
```

## Related Terms

- [Hugging Face (Hugging Face平台)](/en/terms/hugging-face-hugging-face平台/)
- [Keras Applications (Keras应用库)](/en/terms/keras-applications-keras应用库/)
- [Transfer Learning (迁移学习)](/en/terms/transfer-learning-迁移学习/)
- [Model Zoo (模型动物园)](/en/terms/model-zoo-模型动物园/)
