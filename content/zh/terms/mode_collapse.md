---
title: "模式崩溃"
term_id: "mode_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["GANs", "Deep Learning", "Failure Modes"]
difficulty: 4
weight: 1
slug: "mode_collapse"
date: "2026-07-18T11:26:24.857431Z"
lastmod: "2026-07-18T11:44:45.532624Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "模式崩溃是生成对抗网络（GAN）中的一种失效模式，指生成器产生的输出种类有限。"
---
## Definition

在 GAN 中，当生成器学会利用判别器的弱点，仅产生少量看似合理的样本，而忽略数据分布的其他模式时，就会发生模式崩溃。这种现象会导致生成多样性严重不足。

### Summary

模式崩溃是生成对抗网络（GAN）中的一种失效模式，指生成器产生的输出种类有限。

## Key Concepts

- GAN 稳定性
- 分布多样性
- 生成器失效
- 判别器反馈

## Use Cases

- 诊断 GAN 训练的不稳定性
- 提高图像生成的多样性
- 分析潜在空间覆盖率

## Related Terms

- [Generative Adversarial Networks (生成对抗网络)](/en/terms/generative-adversarial-networks-生成对抗网络/)
- [Latent Space (潜在空间)](/en/terms/latent-space-潜在空间/)
- [Training Instability (训练不稳定性)](/en/terms/training-instability-训练不稳定性/)
- [Wasserstein Distance (Wasserstein 距离)](/en/terms/wasserstein-distance-wasserstein-距离/)
