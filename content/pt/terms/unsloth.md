---
title: Unsloth
term_id: unsloth
category: basic_concepts
subcategory: ''
tags:
- Optimization
- LLM
- training
- library
difficulty: 3
weight: 1
slug: unsloth
date: '2026-07-18T15:26:24.969108Z'
lastmod: '2026-07-18T15:51:59.540922Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Unsloth é uma biblioteca de código aberto que acelera o treinamento e
  a inferência de Grandes Modelos de Linguagem (LLMs) em até 2x por meio de gerenciamento
  de memória otimizado e implementações de k
---
## Definition

Unsloth é uma ferramenta especializada projetada para otimizar o ajuste fino (fine-tuning) e a implantação de Grandes Modelos de Linguagem (LLMs). Ela alcança aumentos significativos de velocidade e reduções de memória substituindo os kernels padrão do PyTorch por versões otimizadas.

### Summary

Unsloth é uma biblioteca de código aberto que acelera o treinamento e a inferência de Grandes Modelos de Linguagem (LLMs) em até 2x por meio de gerenciamento de memória otimizado e implementações de kernels.

## Key Concepts

- Otimização de Memória
- Kernels Personalizados
- Ajuste Fino de LLMs
- Aceleração de Velocidade

## Use Cases

- Ajuste fino de LLMs com recursos limitados de GPU
- Aceleração de pipelines de inferência
- Redução de custos de computação em nuvem para treinamento

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

- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [PyTorch](/en/terms/pytorch/)
- [Hugging Face](/en/terms/hugging-face/)
- [Flash Attention](/en/terms/flash-attention/)
