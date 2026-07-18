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
  - /es/terms/lora/
date: "2026-07-18T10:24:12.554801Z"
lastmod: "2026-07-18T11:44:44.744315Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "La Adaptación de Bajo Rango es un método de ajuste fino eficiente en parámetros que inyecta matrices de descomposición de rango entrenables en los pesos existentes del modelo."
---

## Definition

LoRA congela los pesos del modelo preentrenado e inserta matrices de descomposición entrenables en cada capa de la arquitectura de Transformador. Al optimizar solo estas matrices de bajo rango, LoRA reduce significativamente

### Summary

La Adaptación de Bajo Rango es un método de ajuste fino eficiente en parámetros que inyecta matrices de descomposición de rango entrenables en los pesos existentes del modelo.

## Key Concepts

- Ajuste Fino Eficiente en Parámetros
- Descomposición de Rango
- Congelamiento de Pesos
- Módulos Adaptadores

## Use Cases

- Personalización de LLMs
- Adaptación Específica por Dominio
- Entrenamiento con Recursos Limitados

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Técnicas de Ajuste Fino Eficiente en Parámetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficiente-en-parámetros/)
- [Ajuste Fino (Fine-Tuning)](/en/terms/ajuste-fino-fine-tuning/)
- [Cuantización](/en/terms/cuantización/)
