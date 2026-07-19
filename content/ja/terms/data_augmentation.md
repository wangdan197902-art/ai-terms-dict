---
title: データ拡張
term_id: data_augmentation
category: training_techniques
subcategory: ''
tags:
- Machine Learning
- preprocessing
- cv
difficulty: 2
weight: 1
slug: data_augmentation
date: '2026-07-18T11:09:46.134092Z'
lastmod: '2026-07-18T11:44:45.082742Z'
draft: false
source: agnes_llm
status: published
language: ja
description: データ拡張とは、既存のデータポイントに変換を適用することで、トレーニングデータの多様性と規模を増加させる手法です。
---
## Definition

この手法は、画像の回転、音声へのノイズ付加、テキストにおける同義語置換など、既存のサンプルを変形させたバージョンを作成することで、トレーニングデータを人為的に拡張します。これにより、モデルの過学習を防ぎ、汎化性能を向上させるのに役立ちます。

### Summary

データ拡張とは、既存のデータポイントに変換を適用することで、トレーニングデータの多様性と規模を増加させる手法です。

## Key Concepts

- 過学習の防止
- データセットの拡張
- 汎化性能
- 変換

## Use Cases

- コンピュータビジョンモデルの堅牢性の向上
- 限られたテキストデータでのNLPモデル性能の強化
- 不均衡なデータセットのバランス調整

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [正則化 (Regularization)](/en/terms/正則化-regularization/)
- [合成データ (Synthetic Data)](/en/terms/合成データ-synthetic-data/)
- [転移学習 (Transfer Learning)](/en/terms/転移学習-transfer-learning/)
- [過学習 (Overfitting)](/en/terms/過学習-overfitting/)
