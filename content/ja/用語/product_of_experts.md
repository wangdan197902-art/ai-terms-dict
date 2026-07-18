---
title: "エキスパートの積（Product of Experts）"
term_id: "product_of_experts"
category: "basic_concepts"
subcategory: ""
tags: ["generative_models", "probabilistic_graphical_models", "deep_learning"]
difficulty: 4
weight: 1
slug: "product_of_experts"
aliases:
  - /ja/terms/product_of_experts/
date: "2026-07-18T11:28:42.914042Z"
lastmod: "2026-07-18T11:44:45.133930Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "複数の独立したエキスパートモデルの出力を乗算することで結合分布を形成する確率モデリングフレームワーク。"
---

## Definition

エキスパートの積（PoE）は、単純な確率分布を組み合わせて複雑な分布を構築する方法です。「エキスパートの混合（Mixture of Experts）」が確率を平均化するのに対し、PoEは各エキスパートの出力（またはエネルギー）を乗算します。これにより、すべてのエキスパートが合意する領域に確率質量が集まり、厳格な制約を満たす生成モデルを実現します。

### Summary

複数の独立したエキスパートモデルの出力を乗算することで結合分布を形成する確率モデリングフレームワーク。

## Key Concepts

- エネルギーベースモデル
- 結合分布
- 乗法的組み合わせ
- 制約充足

## Use Cases

- 画像テクスチャの合成とモデリング
- ディープボルツマンマシン
- 生成モデルにおける複雑な依存関係のモデリング

## Related Terms

- [mixture_of_experts (エキスパートの混合)](/en/terms/mixture_of_experts-エキスパートの混合/)
- [energy_based_model (エネルギーベースモデル)](/en/terms/energy_based_model-エネルギーベースモデル/)
- [deep_boltzmann_machine (ディープボルツマンマシン)](/en/terms/deep_boltzmann_machine-ディープボルツマンマシン/)
- [joint_probability (結合確率)](/en/terms/joint_probability-結合確率/)
