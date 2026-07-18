---
title: "密結合層"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /ja/terms/dense/
date: "2026-07-18T11:11:57.692583Z"
lastmod: "2026-07-18T11:44:45.090097Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "前のレイヤーまたは次元のすべての要素と、現在のすべての要素が接続されているレイヤーまたはテンソル。"
---

## Definition

ニューラルネットワークにおいて、「密結合（Dense）」とは、各ニューロンが前のレイヤーのすべてのニューロンから入力を受ける全結合層を指します。これは、畳み込み層やスパース接続に見られる疎な接続とは対照的です。

### Summary

前のレイヤーまたは次元のすべての要素と、現在のすべての要素が接続されているレイヤーまたはテンソル。

## Key Concepts

- 全結合
- 重み行列
- 活性化関数
- 特徴量統合

## Use Cases

- 多層パーセプトロン（MLP）における最終分類層
- ハイブリッドモデルにおける特徴量融合
- 単純な回帰タスク

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [順伝播型ニューラルネットワーク (フィードフォワードNN)](/en/terms/順伝播型ニューラルネットワーク-フィードフォワードnn/)
- [逆伝播法 (バックプロパゲーション)](/en/terms/逆伝播法-バックプロパゲーション/)
- [ReLU (整流線形ユニット)](/en/terms/relu-整流線形ユニット/)
- [バイアス項](/en/terms/バイアス項/)
