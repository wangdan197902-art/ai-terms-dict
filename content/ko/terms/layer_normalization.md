---
title: レイヤー正規化
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T16:01:50.719537Z'
lastmod: '2026-07-18T16:38:06.859605Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 個々のサンプルごとに、ニューラルネットワークの層の活性化値を特徴量次元に対して正規化する手法。
---
## Definition

レイヤー正規化は、内部共変量シフトを軽減することでトレーニングの安定化を図ります。特にリカレントニューラルネットワークやトランスフォーマーアーキテクチャで効果的です。バッチ統計量に依存するバッチ正規化とは異なり、バッチサイズが小さい場合でも安定して動作します。

### Summary

個々のサンプルごとに、ニューラルネットワークの層の活性化値を特徴量次元に対して正規化する手法。

## Key Concepts

- 正規化
- 内部共変量シフト
- トランスフォーマーモデル
- RNN

## Use Cases

- BERTなどのトランスフォーマーモデルのトレーニング
- RNN/LSTMのトレーニング安定化
- 小バッチサイズでのディープラーニング

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (バッチ正規化)](/en/terms/batch_normalization-バッチ正規化/)
- [transformer (トランスフォーマー)](/en/terms/transformer-トランスフォーマー/)
- [normalization (正規化)](/en/terms/normalization-正規化/)
- [deep_learning (ディープラーニング)](/en/terms/deep_learning-ディープラーニング/)
