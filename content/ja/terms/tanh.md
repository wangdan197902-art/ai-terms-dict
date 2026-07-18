---
title: "Tanh"
term_id: "tanh"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "mathematics"]
difficulty: 2
weight: 1
slug: "tanh"
aliases:
  - /ja/terms/tanh/
date: "2026-07-18T11:34:00.783247Z"
lastmod: "2026-07-18T11:44:45.149374Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "Tanh（双曲線正接）は、入力値を-1から1の範囲にマッピングする活性化関数です。"
---

## Definition

双曲線正接（Tanh）関数は、ニューラルネットワークで一般的に使用される非線形活性化関数です。入力値を区間(-1, 1)に圧縮し、ゼロ中心化された出力を提供することで、

### Summary

Tanh（双曲線正接）は、入力値を-1から1の範囲にマッピングする活性化関数です。

## Key Concepts

- 活性化関数
- 非線形性
- ゼロ中心化出力
- 逆伝播

## Use Cases

- 再帰型ニューラルネットワーク
- LSTMセルゲート
- MLPの隠れ層

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (シグモイド)](/en/terms/sigmoid-シグモイド/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (ニューラルネットワーク)](/en/terms/neural_networks-ニューラルネットワーク/)
