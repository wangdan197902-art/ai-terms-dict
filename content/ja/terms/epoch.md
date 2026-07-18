---
title: "エポック"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /ja/terms/epoch/
date: "2026-07-18T11:13:45.750708Z"
lastmod: "2026-07-18T11:44:45.095377Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "モデル訓練中に、訓練データセット全体を機械学習アルゴリズムが1回完全に通過すること。"
---

## Definition

機械学習において、エポックは訓練データセット全体に対する単一の反復（イテレーション）を表します。各エポックの間、モデルはすべての訓練例を処理し、逆伝播を通じて重みを更新します。適切なエポック数の選択は、モデルの収束と過学習の防止において重要な役割を果たします。

### Summary

モデル訓練中に、訓練データセット全体を機械学習アルゴリズムが1回完全に通過すること。

## Key Concepts

- 訓練反復
- 逆伝播
- 収束
- ハイパーパラメータ調整

## Use Cases

- ニューラルネットワークの訓練ループの設定
- サイクルごとの検証損失のモニタリング
- 早期終了戦略の実装

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (バッチサイズ)](/en/terms/batch-size-バッチサイズ/)
- [Iteration (イテレーション)](/en/terms/iteration-イテレーション/)
- [Learning Rate (学習率)](/en/terms/learning-rate-学習率/)
- [Overfitting (過学習)](/en/terms/overfitting-過学習/)
