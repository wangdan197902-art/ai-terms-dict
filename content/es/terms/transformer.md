---
title: Transformador
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T10:27:24.144441Z'
lastmod: '2026-07-18T11:44:44.753744Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una arquitectura de aprendizaje profundo basada en mecanismos de autoatención
  que procesa datos secuenciales en paralelo en lugar de secuencialmente.
---
## Definition

Introducido en el artículo 'Attention Is All You Need', la arquitectura Transformador revolucionó el procesamiento del lenguaje natural y más allá. Utiliza autoatención de múltiples cabezas para ponderar la importancia de

### Summary

Una arquitectura de aprendizaje profundo basada en mecanismos de autoatención que procesa datos secuenciales en paralelo en lugar de secuencialmente.

## Key Concepts

- Autoatención
- Atención de Múltiples Cabezas
- Codificación Posicional
- Estructura Codificador-Decodificador

## Use Cases

- Traducción automática
- Generación de texto
- Reconocimiento de imágenes (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (mecanismo de atención)](/en/terms/attention_mechanism-mecanismo-de-atención/)
- [bert (BERT)](/en/terms/bert-bert/)
- [gpt (GPT)](/en/terms/gpt-gpt/)
- [self_attention (autoatención)](/en/terms/self_attention-autoatención/)
