---
title: Ajuste de Prompt
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T15:18:06.179164Z'
lastmod: '2026-07-18T15:51:59.524801Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um método de ajuste fino eficiente em parâmetros que otimiza embeddings
  contínuos de entrada em vez de atualizar todos os pesos do modelo.
---
## Definition

O ajuste de prompt envolve a adição de prompts treináveis suaves (vetores contínuos) à camada de entrada de um modelo de linguagem pré-treinado, mantendo os parâmetros subjacentes do modelo congelados. Essa abordagem permite

### Summary

Um método de ajuste fino eficiente em parâmetros que otimiza embeddings contínuos de entrada em vez de atualizar todos os pesos do modelo.

## Key Concepts

- prompts suaves
- eficiência de parâmetros
- pesos congelados
- aprendizado poucos exemplos

## Use Cases

- Adaptação de LLMs para domínios específicos
- Ajuste fino com poucos recursos
- Otimização de aprendizado multitarefa

## Related Terms

- [PEFT (Técnicas de Ajuste Fino Eficientes em Parâmetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficientes-em-parâmetros/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [in-context learning (Aprendizado no Contexto)](/en/terms/in-context-learning-aprendizado-no-contexto/)
- [fine-tuning (Ajuste Fino)](/en/terms/fine-tuning-ajuste-fino/)
