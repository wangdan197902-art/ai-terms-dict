---
title: "类激活映射"
term_id: "class_activation_mapping"
category: "training_techniques"
subcategory: ""
tags: ["visualization", "interpretability", "computer_vision"]
difficulty: 4
weight: 1
slug: "class_activation_mapping"
aliases:
  - /zh/terms/class_activation_mapping/
date: "2026-07-18T11:10:07.300942Z"
lastmod: "2026-07-18T11:44:45.456602Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "类激活映射（CAM）是一种可视化技术，用于高亮显示输入图像中对特定预测类别贡献最大的区域。"
---

## Definition

CAM 在输入图像上叠加热力图，以显示哪些像素对模型针对特定类别标签的决策贡献最大。它通过对最终卷积层应用全局平均池化来工作，从而定位关键特征区域。

### Summary

类激活映射（CAM）是一种可视化技术，用于高亮显示输入图像中对特定预测类别贡献最大的区域。

## Key Concepts

- 热力图可视化
- 可解释性
- 特征重要性
- 全局平均池化

## Use Cases

- 医学影像诊断验证
- 自动驾驶物体检测调试
- 可解释 AI 报告

## Related Terms

- [Grad-CAM (梯度加权类激活映射)](/en/terms/grad-cam-梯度加权类激活映射/)
- [Saliency Maps (显著性图)](/en/terms/saliency-maps-显著性图/)
- [Explainable AI (可解释人工智能)](/en/terms/explainable-ai-可解释人工智能/)
- [Convolutional Neural Networks (卷积神经网络)](/en/terms/convolutional-neural-networks-卷积神经网络/)
