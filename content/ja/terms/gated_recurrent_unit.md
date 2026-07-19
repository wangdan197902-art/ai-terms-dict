---
title: "ゲート付き再帰型ユニット（GRU）"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T11:15:40.207723Z"
lastmod: "2026-07-18T11:44:45.100133Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "情報の流れを制御するためにゲート機構を使用する再帰型ニューラルネットワーク（RNN）の一種で、LSTMの簡略化された代替版として機能する。"
---
## Definition

ゲート付き再帰型ユニット（GRU）は、系列データにおける長期依存関係を捉えるように設計された特殊な再帰型ニューラルネットワーク（RNN）セルです。長短期記憶（LSTM）アーキテクチャを簡素化しており、更新ゲートとリセットゲートの2つのゲートを使用して、過去の情報を保持するか捨てるかを制御します。これにより、計算効率が高く、パラメータ数が少ないという利点があります。

### Summary

情報の流れを制御するためにゲート機構を使用する再帰型ニューラルネットワーク（RNN）の一種で、LSTMの簡略化された代替版として機能する。

## Key Concepts

- 再帰型ニューラルネットワーク
- 更新ゲート
- リセットゲート
- 系列モデリング

## Use Cases

- 自然言語処理
- 時系列予測
- 音声認識

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM (長短期記憶：GRUの前身となるRNNアーキテクチャ)](/en/terms/lstm-長短期記憶-gruの前身となるrnnアーキテクチャ/)
- [RNN (再帰型ニューラルネットワーク)](/en/terms/rnn-再帰型ニューラルネットワーク/)
- [ディープラーニング (多層ニューラルネットワークを用いた機械学習)](/en/terms/ディープラーニング-多層ニューラルネットワークを用いた機械学習/)
- [シーケンスツーシーケンス (系列データを別の系列に変換するモデル)](/en/terms/シーケンスツーシーケンス-系列データを別の系列に変換するモデル/)
