---
title: 专家乘积
term_id: product_of_experts
category: basic_concepts
subcategory: ''
tags:
- Generative Models
- Probabilistic Graphical Models
- Deep Learning
difficulty: 4
weight: 1
slug: product_of_experts
date: '2026-07-18T11:30:38.310486Z'
lastmod: '2026-07-18T11:44:45.545690Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种概率建模框架，其联合分布由多个独立专家模型的输出相乘形成。
---
## Definition

专家乘积（PoE）是一种通过组合更简单的分布来构建复杂概率分布的方法。与平均概率的“混合专家”（MoE）不同，PoE通过乘法结合各个专家模型的输出。这意味着如果任何一个专家模型认为某个配置是不可能的（概率为零），整个联合分布的概率也将为零，从而能够更严格地满足约束条件。

### Summary

一种概率建模框架，其联合分布由多个独立专家模型的输出相乘形成。

## Key Concepts

- 基于能量的模型
- 联合分布
- 乘法组合
- 约束满足

## Use Cases

- 图像纹理合成与建模
- 深度玻尔兹曼机
- 生成模型中的复杂依赖关系建模

## Related Terms

- [mixture_of_experts (混合专家)](/en/terms/mixture_of_experts-混合专家/)
- [energy_based_model (基于能量的模型)](/en/terms/energy_based_model-基于能量的模型/)
- [deep_boltzmann_machine (深度玻尔兹曼机)](/en/terms/deep_boltzmann_machine-深度玻尔兹曼机/)
- [joint_probability (联合概率)](/en/terms/joint_probability-联合概率/)
