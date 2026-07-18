---
title: "知識蒸留"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /ja/terms/knowledge_distillation/
date: "2026-07-18T11:20:35.953125Z"
lastmod: "2026-07-18T11:44:45.112391Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "知識蒸留は、小さな学生モデルが大きな教師モデルの動作を模倣するように学習させるモデル圧縮技術です。"
---

## Definition

知識蒸留は、大規模で複雑なニューラルネットワーク（教師）を、より小さく効率的なネットワーク（学生）に圧縮するために使用される機械学習手法です。学生モデルは教師の出力分布を学習します。

### Summary

知識蒸留は、小さな学生モデルが大きな教師モデルの動作を模倣するように学習させるモデル圧縮技術です。

## Key Concepts

- 教師-学生モデル
- モデル圧縮
- ソフトターゲット
- 効率性

## Use Cases

- エッジデバイスへのモデル展開
- 推論レイテンシの削減
- クラウドコンピューティングコストの低減

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (モデル圧縮)](/en/terms/model-compression-モデル圧縮/)
- [Pruning (プルーニング)](/en/terms/pruning-プルーニング/)
- [Quantization (量子化)](/en/terms/quantization-量子化/)
- [Neural Networks (ニューラルネットワーク)](/en/terms/neural-networks-ニューラルネットワーク/)
