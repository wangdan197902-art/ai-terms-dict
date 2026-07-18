---
title: "再パラメータ化トリック"
term_id: "reparameterization_trick"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "probabilistic_models", "optimization"]
difficulty: 4
weight: 1
slug: "reparameterization_trick"
aliases:
  - /ja/terms/reparameterization_trick/
date: "2026-07-18T11:30:33.410927Z"
lastmod: "2026-07-18T11:44:45.138743Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "確率変数と学習可能なパラメータを分離し、変分推論における勾配ベースの最適化を可能にする手法。"
---

## Definition

再パラメータ化トリックは、変分オートエンコーダーや他の確率的モデルで使用される基本的な手法です。これは、確率変数を外部のパラメータ（通常は正規分布からのサンプリング）と決定論的な関数の組み合わせとして表現することで、確率的ノードを通って勾配を流すことを可能にします。これにより、逆伝播アルゴリズムを用いてモデルのパラメータを効率的に最適化できます。

### Summary

確率変数と学習可能なパラメータを分離し、変分推論における勾配ベースの最適化を可能にする手法。

## Key Concepts

- 変分推論
- 勾配推定
- 確率的ノード
- 微分可能シミュレーション

## Use Cases

- 変分オートエンコーダー（VAE）の学習
- ベイズニューラルネットワーク
- 確率的グラフィカルモデル

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO (Evidence Lower Bound: 証拠の下界)](/en/terms/elbo-evidence-lower-bound-証拠の下界/)
- [Latent Variables (潜在変数)](/en/terms/latent-variables-潜在変数/)
- [Backpropagation (逆伝播)](/en/terms/backpropagation-逆伝播/)
- [Monte Carlo Estimation (モンテカルロ推定)](/en/terms/monte-carlo-estimation-モンテカルロ推定/)
