---
title: "Unsloth"
term_id: "unsloth"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "LLM", "training", "library"]
difficulty: 3
weight: 1
slug: "unsloth"
aliases:
  - /tr/terms/unsloth/
date: "2026-07-18T16:20:31.654994Z"
lastmod: "2026-07-18T16:38:07.375816Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Unsloth, büyük dil modellerinin (LLM) eğitimini ve çıkarımını optimize edilmiş bellek yönetimi ve çekirdek uygulamaları aracılığıyla %100'e kadar hızlandıran açık kaynaklı bir kütüphanedir."
---

## Definition

Unsloth, Büyük Dil Modellerinin (LLM) ince ayarını ve dağıtımını optimize etmek için tasarlanmış özel bir araçtır. Standart PyTorch işlemlerini değiştirerek önemli hız artışları ve bellek tasarrufu sağlar.

### Summary

Unsloth, büyük dil modellerinin (LLM) eğitimini ve çıkarımını optimize edilmiş bellek yönetimi ve çekirdek uygulamaları aracılığıyla %100'e kadar hızlandıran açık kaynaklı bir kütüphanedir.

## Key Concepts

- Bellek Optimizasyonu
- Özel Çekirdekler (Custom Kernels)
- LLM İnce Ayarı
- Hızlandırma

## Use Cases

- Sınırlı GPU kaynaklarında LLM'leri ince ayar yapmak
- Çıkarım hatlarını hızlandırmak
- Eğitim için bulut bilişim maliyetlerini azaltmak

## Code Example

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-2-7b-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)
```

## Related Terms

- [LoRA (Low-Rank Adaptation - Düşük Sıralı Uyarlanabilirlik)](/en/terms/lora-low-rank-adaptation-düşük-sıralı-uyarlanabilirlik/)
- [PyTorch (Derin Öğrenme Kütüphanesi)](/en/terms/pytorch-derin-öğrenme-kütüphanesi/)
- [Hugging Face (Açık Kaynak ML Topluluğu)](/en/terms/hugging-face-açık-kaynak-ml-topluluğu/)
- [Flash Attention (Hızlı Dikkat Mekanizması)](/en/terms/flash-attention-hızlı-dikkat-mekanizması/)
