---
title: "基于流的生成模型"
term_id: "flow_based_generative_model"
category: "basic_concepts"
subcategory: ""
tags: ["generative", "probability", "invertible"]
difficulty: 4
weight: 1
slug: "flow_based_generative_model"
date: "2026-07-18T11:17:25.495551Z"
lastmod: "2026-07-18T11:44:45.500477Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一类利用可逆变换将简单分布映射到复杂数据分布的生成模型。"
---
## Definition

基于流的生成模型通过对简单的基分布（如高斯分布）应用一系列可逆且可微的变换来构建复杂的概率分布。由于变换是可逆的，模型可以精确计算似然值，便于密度估计和采样。

### Summary

一类利用可逆变换将简单分布映射到复杂数据分布的生成模型。

## Key Concepts

- 可逆变换
- 精确似然
- 归一化流
- 变量变换

## Use Cases

- 图像生成
- 密度估计
- 异常检测

## Related Terms

- [Normalizing Flow (归一化流)](/en/terms/normalizing-flow-归一化流/)
- [GAN (生成对抗网络)](/en/terms/gan-生成对抗网络/)
- [VAE (变分自编码器)](/en/terms/vae-变分自编码器/)
- [Coupling Layer (耦合层)](/en/terms/coupling-layer-耦合层/)
