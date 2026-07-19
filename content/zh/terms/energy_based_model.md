---
title: 基于能量的模型
term_id: energy_based_model
category: basic_concepts
subcategory: ''
tags:
- Generative Models
- probability
- Deep Learning
difficulty: 4
weight: 1
slug: energy_based_model
date: '2026-07-18T11:16:12.975025Z'
lastmod: '2026-07-18T11:44:45.494647Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种概率模型，为合理的配置分配低能量值，为不合理的配置分配高能量值。
---
## Definition

基于能量的模型（EBM）使用源自能量函数的未归一化密度函数来定义输入数据的概率分布。能量函数将数据点映射到实数，合理的配置具有较低的能量，而不合理的配置具有较高的能量。模型通常通过马尔可夫链蒙特卡洛方法进行采样和训练。

### Summary

一种概率模型，为合理的配置分配低能量值，为不合理的配置分配高能量值。

## Key Concepts

- 未归一化概率
- 配分函数
- 能量函数
- 马尔可夫链蒙特卡洛

## Use Cases

- 图像生成与修复
- 密度估计
- 异常检测

## Related Terms

- [Boltzmann machine (玻尔兹曼机)](/en/terms/boltzmann-machine-玻尔兹曼机/)
- [Deep Boltzmann machine (深度玻尔兹曼机)](/en/terms/deep-boltzmann-machine-深度玻尔兹曼机/)
- [Variational inference (变分推断)](/en/terms/variational-inference-变分推断/)
- [Probabilistic graphical models (概率图模型)](/en/terms/probabilistic-graphical-models-概率图模型/)
