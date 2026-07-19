---
title: スパイク・アンドスラブ回帰
term_id: spike_and_slab_regression
category: basic_concepts
subcategory: ''
tags:
- statistics
- bayesian
- Regression
difficulty: 4
weight: 1
slug: spike_and_slab_regression
date: '2026-07-18T11:33:20.376319Z'
lastmod: '2026-07-18T11:44:45.146877Z'
draft: false
source: agnes_llm
status: published
language: ja
description: ゼロと非ゼロの係数を区別するために混合事前分布を用いるベイズ変量選択手法。
---
## Definition

スパイク・アンドスラブ回帰は、変量選択やスパースモデリングに用いられるベイズ統計的手法です。この手法は、「スパイク（通常はゼロ付近に集中する分布）」と「スラブ（非ゼロの係数に対応する広範な分布）」という2つの成分からなる混合事前分布を採用しています。これにより、モデルがどの変数が重要かを確率的に判断し、不要な変数の係数をゼロに近づけることでスパースな解を得ます。

### Summary

ゼロと非ゼロの係数を区別するために混合事前分布を用いるベイズ変量選択手法。

## Key Concepts

- ベイズ推論
- スパースモデリング
- 混合事前分布
- 変量選択

## Use Cases

- 高次元ゲノムデータの解析
- 金融リスク要因の特定
- 予測モデリングにおける特徴量選択

## Related Terms

- [Lasso (L1正則化によるスパース回帰)](/en/terms/lasso-l1正則化によるスパース回帰/)
- [Ridge Regression (L2正則化によるリッジ回帰)](/en/terms/ridge-regression-l2正則化によるリッジ回帰/)
- [Bayesian Linear Regression (ベイズ線形回帰)](/en/terms/bayesian-linear-regression-ベイズ線形回帰/)
- [Sparsity (スパース性：パラメータの多くがゼロである性質)](/en/terms/sparsity-スパース性-パラメータの多くがゼロである性質/)
