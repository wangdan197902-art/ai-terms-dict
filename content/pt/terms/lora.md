---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /pt/terms/lora/
date: "2026-07-18T14:36:36.094683Z"
lastmod: "2026-07-18T15:51:59.433198Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Adaptação de Baixo Ranque é um método de ajuste fino eficiente em parâmetros que injeta matrizes de decomposição de ranque treináveis nos pesos existentes do modelo."
---

## Definition

O LoRA congela os pesos do modelo pré-treinado e insere matrizes de decomposição treináveis em cada camada da arquitetura Transformer. Ao otimizar apenas essas matrizes de baixo ranque, o LoRA reduz significativamente o custo computacional.

### Summary

Adaptação de Baixo Ranque é um método de ajuste fino eficiente em parâmetros que injeta matrizes de decomposição de ranque treináveis nos pesos existentes do modelo.

## Key Concepts

- Ajuste Fino Eficiente em Parâmetros
- Decomposição de Ranque
- Congelamento de Pesos
- Módulos Adaptadores

## Use Cases

- Personalização de LLMs
- Adaptação Específica por Domínio
- Treinamento com Recursos Limitados

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Técnicas de Ajuste Fino Eficientes em Parâmetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficientes-em-parâmetros/)
- [Fine-Tuning (Ajuste Fino)](/en/terms/fine-tuning-ajuste-fino/)
- [Quantização](/en/terms/quantização/)
