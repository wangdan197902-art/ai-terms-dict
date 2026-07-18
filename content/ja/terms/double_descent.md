---
title: "ダブルデセント（二重下降）"
term_id: "double_descent"
category: "basic_concepts"
subcategory: ""
tags: ["Theory", "Deep Learning", "Generalization"]
difficulty: 5
weight: 1
slug: "double_descent"
aliases:
  - /ja/terms/double_descent/
date: "2026-07-18T11:12:52.607861Z"
lastmod: "2026-07-18T11:44:45.092936Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "モデルの複雑さが補間閾値を超えて増加するにつれて、テスト誤差が減少し、増加し、その後再び減少する現象。"
---

## Definition

ダブルデセントは、トレーニングデータを完全に補間しているにもかかわらず、高度に過剰パラメータ化されたモデルが低いテスト誤差を実現できることを示すことで、従来のバイアス・バリアンストレードオフに挑戦します。初期段階では誤差が増加しますが、モデルが複雑になりすぎると誤差が再び低下するという二つの下降局面が見られます。

### Summary

モデルの複雑さが補間閾値を超えて増加するにつれて、テスト誤差が減少し、増加し、その後再び減少する現象。

## Key Concepts

- 補間閾値
- 過剰パラメータ化
- バイアス・バリアンストレードオフ
- テスト誤差

## Use Cases

- ニューラルネットワークのスケーリング則の分析
- ディープラーニングにおける汎化の理解
- 大規模AIシステムにおけるモデル選択

## Related Terms

- [Overfitting (過学習)](/en/terms/overfitting-過学習/)
- [Underfitting (未学習)](/en/terms/underfitting-未学習/)
- [Neural Tangent Kernel (ニューラルタンジェントカーネル)](/en/terms/neural-tangent-kernel-ニューラルタンジェントカーネル/)
- [Regularization (正則化)](/en/terms/regularization-正則化/)
