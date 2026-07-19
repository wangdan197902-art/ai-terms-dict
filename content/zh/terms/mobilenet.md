---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
date: "2026-07-18T11:26:24.857413Z"
lastmod: "2026-07-18T11:44:45.532439Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "MobileNet 是一系列专为移动端和嵌入式视觉应用设计的轻量级深度神经网络。"
---
## Definition

与标准卷积相比，MobileNet 利用深度可分离卷积大幅降低了计算成本和模型体积。这种架构使得在资源受限设备上高效提取特征成为可能。

### Summary

MobileNet 是一系列专为移动端和嵌入式视觉应用设计的轻量级深度神经网络。

## Key Concepts

- 深度可分离卷积
- 模型效率
- 边缘计算
- 迁移学习

## Use Cases

- 智能手机上的实时目标检测
- 物联网设备上的图像分类
- 移动应用中的面部识别

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (洗牌网络)](/en/terms/shufflenet-洗牌网络/)
- [SqueezeNet (挤压网络)](/en/terms/squeezenet-挤压网络/)
- [EfficientNet (高效网络)](/en/terms/efficientnet-高效网络/)
- [Convolutional Neural Network (卷积神经网络)](/en/terms/convolutional-neural-network-卷积神经网络/)
