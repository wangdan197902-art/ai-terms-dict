---
title: "正則化"
term_id: "regularization"
category: "basic_concepts"
subcategory: ""
tags: ["ML Basics", "Optimization", "Statistics"]
difficulty: 2
weight: 1
slug: "regularization"
date: "2026-07-18T11:30:18.434901Z"
lastmod: "2026-07-18T11:44:45.138396Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "損失関数にペナルティを追加したりモデルの複雑さを制限したりすることで、過学習を防ぐためのトレーニング手法のセット。"
---
## Definition

正則化は、機械学習において一般化誤差を大幅に増加させることなく減少させるための重要な概念です。これは、モデルが過度に複雑なパターンやノイズを学習することを抑制することで機能します。

### Summary

損失関数にペナルティを追加したりモデルの複雑さを制限したりすることで、過学習を防ぐためのトレーニング手法のセット。

## Key Concepts

- 過学習
- バイアス・バリアンストレードオフ
- L1/L2ペナルティ
- ドロップアウト

## Use Cases

- ディープニューラルネットワークのトレーニング
- 線形回帰モデル
- 小規模データセットでの暗記（オーバーフィッティング）の防止

## Code Example

```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
```

## Related Terms

- [Overfitting (過学習)](/en/terms/overfitting-過学習/)
- [Underfitting (未学習)](/en/terms/underfitting-未学習/)
- [Cross-validation (交差検証)](/en/terms/cross-validation-交差検証/)
- [Hyperparameter tuning (ハイパーパラメータ調整)](/en/terms/hyperparameter-tuning-ハイパーパラメータ調整/)
