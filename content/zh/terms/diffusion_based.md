---
title: "基于扩散的"
term_id: "diffusion_based"
category: "application_paradigms"
subcategory: ""
tags: ["generative_ai", "deep_learning", "image_synthesis"]
difficulty: 4
weight: 1
slug: "diffusion_based"
aliases:
  - /zh/terms/diffusion_based/
date: "2026-07-18T10:56:23.618178Z"
lastmod: "2026-07-18T11:44:45.390229Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种生成建模方法，通过学习去噪步骤逆转逐渐添加噪声的过程来创建数据。"
---

## Definition

基于扩散的模型是一类生成式AI，它们通过从随机分布中迭代去除噪声来创建新的数据样本。该过程始于一个前向阶段，即缓慢地向数据中添加高斯噪声，直到数据变为纯噪声；随后通过训练神经网络学习逆向过程，从而从噪声中恢复出有意义的结构。

### Summary

一种生成建模方法，通过学习去噪步骤逆转逐渐添加噪声的过程来创建数据。

## Key Concepts

- 前向过程
- 逆向过程
- 去噪
- 潜在空间

## Use Cases

- 高分辨率图像合成
- 文生图生成
- 医学影像的数据增强

## Related Terms

- [stable_diffusion (稳定扩散)](/en/terms/stable_diffusion-稳定扩散/)
- [generative_models (生成模型)](/en/terms/generative_models-生成模型/)
- [denoising_autoencoder (去噪自编码器)](/en/terms/denoising_autoencoder-去噪自编码器/)
- [latent_diffusion (潜在扩散)](/en/terms/latent_diffusion-潜在扩散/)
