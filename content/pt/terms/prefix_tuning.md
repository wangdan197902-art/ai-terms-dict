---
title: Prefix Tuning
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T15:17:36.878516Z'
lastmod: '2026-07-18T15:51:59.523364Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um método de ajuste fino eficiente em parâmetros que adiciona vetores
  contínuos treináveis à entrada das camadas do transformador.
---
## Definition

O Prefix Tuning é uma técnica de adaptação eficiente em parâmetros para transformadores pré-treinados. Em vez de atualizar todos os pesos do modelo, ele antecede uma sequência de vetores contínuos treináveis (o prefixo) às entradas das camadas do transformador.

### Summary

Um método de ajuste fino eficiente em parâmetros que adiciona vetores contínuos treináveis à entrada das camadas do transformador.

## Key Concepts

- Ajuste Fino Eficiente em Parâmetros
- Prompts Suaves
- Camadas do Transformador
- Backbone Congelado

## Use Cases

- Adaptação para aprendizado few-shot
- Aprendizado multi-tarefa com recursos limitados
- Personalização de LLMs para domínios específicos

## Related Terms

- [prompt_tuning (Ajuste de Prompts)](/en/terms/prompt_tuning-ajuste-de-prompts/)
- [p_tuning (Ajuste P-Tuning)](/en/terms/p_tuning-ajuste-p-tuning/)
- [adapter_modules (Módulos Adaptadores)](/en/terms/adapter_modules-módulos-adaptadores/)
- [peft (Técnicas de Ajuste Fino Eficientes em Parâmetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficientes-em-parâmetros/)
