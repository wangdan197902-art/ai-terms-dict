---
title: "学習のための近接勾配法"
term_id: "proximal_gradient_methods_for_learning"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "mathematics", "regression"]
difficulty: 4
weight: 1
slug: "proximal_gradient_methods_for_learning"
aliases:
  - /ja/terms/proximal_gradient_methods_for_learning/
date: "2026-07-18T11:28:57.680423Z"
lastmod: "2026-07-18T11:44:45.134552Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "滑らかな成分と非滑らかな成分の両方を含む合成目的関数を最小化するために設計された最適化アルゴリズム。"
---

## Definition

近接勾配法は、損失関数に微分可能な滑らかな項と、L1ノルムのような微分不可能な正則化項が含まれている場合に使用される反復最適化技法です。このアルゴリズムは、勾配降下ステップと近接演算子（プロキシマル演算子）による正則化ステップを組み合わせて、非滑らかな項を持つ関数の最適解を探ります。

### Summary

滑らかな成分と非滑らかな成分の両方を含む合成目的関数を最小化するために設計された最適化アルゴリズム。

## Key Concepts

- 合成最適化
- 近接演算子
- L1正則化
- 非滑らかな凸性

## Use Cases

- スパース特徴選択
- ラッソ回帰
- 構造化予測モデル

## Related Terms

- [gradient descent (勾配降下法)](/en/terms/gradient-descent-勾配降下法/)
- [Lasso (ラッソ回帰)](/en/terms/lasso-ラッソ回帰/)
- [convex optimization (凸最適化)](/en/terms/convex-optimization-凸最適化/)
- [regularization (正則化)](/en/terms/regularization-正則化/)
