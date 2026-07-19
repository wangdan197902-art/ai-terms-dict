---
title: 残差接続
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T11:00:34.091819Z'
lastmod: '2026-07-18T11:44:45.057241Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 勾配の伝播を促進するため、層の入力を直接出力に追加するメカニズム。
---
## Definition

スキップ接続とも呼ばれる残差接続は、入力を後の層の出力に直接加えることで、ネットワーク内を勾配が流れることを可能にします。このアーキテクチャは、深いネットワークにおける勾配消失問題を解決します。

### Summary

勾配の伝播を促進するため、層の入力を直接出力に追加するメカニズム。

## Key Concepts

- スキップ接続
- 勾配消失問題
- 深層残差学習
- 勾配フロー

## Use Cases

- 深層畳み込みニューラルネットワークのトレーニング
- トランスフォーマーアーキテクチャ
- 画像分類モデル

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (スキップ接続)](/en/terms/skip_connection-スキップ接続/)
- [vanishing_gradient (勾配消失)](/en/terms/vanishing_gradient-勾配消失/)
- [deep_learning (深層学習)](/en/terms/deep_learning-深層学習/)
- [resnet (ResNet)](/en/terms/resnet-resnet/)
