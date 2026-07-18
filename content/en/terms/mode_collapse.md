---
title: "Mode Collapse"
term_id: "mode_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["GANs", "Deep Learning", "Failure Modes"]
difficulty: 4
weight: 1
slug: "mode_collapse"
aliases:
  - /en/terms/mode_collapse/
date: "2026-07-18T10:07:39.942986Z"
lastmod: "2026-07-18T11:44:44.700345Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Mode collapse is a failure mode in Generative Adversarial Networks where the generator produces limited varieties of outputs."
---

## Definition

In GANs, mode collapse occurs when the generator learns to exploit weaknesses in the discriminator by producing a narrow range of plausible samples, ignoring other modes of the data distribution. This results in a lack of diversity in generated content, such as generating only one specific digit in MNIST despite training on all digits, severely limiting the utility of the generative model.

### Summary

Mode collapse is a failure mode in Generative Adversarial Networks where the generator produces limited varieties of outputs.

## Key Concepts

- GAN Stability
- Distribution Diversity
- Generator Failure
- Discriminator Feedback

## Use Cases

- Diagnosing GAN training instability
- Improving image generation diversity
- Analyzing latent space coverage

## Related Terms

- [Generative Adversarial Networks](/en/terms/generative-adversarial-networks/)
- [Latent Space](/en/terms/latent-space/)
- [Training Instability](/en/terms/training-instability/)
- [Wasserstein Distance](/en/terms/wasserstein-distance/)
