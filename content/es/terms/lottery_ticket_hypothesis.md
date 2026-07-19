---
title: Hipótesis del billete de lotería
term_id: lottery_ticket_hypothesis
category: basic_concepts
subcategory: ''
tags:
- Optimization
- pruning
- theory
difficulty: 4
weight: 1
slug: lottery_ticket_hypothesis
date: '2026-07-18T10:58:22.829879Z'
lastmod: '2026-07-18T11:44:44.827873Z'
draft: false
source: agnes_llm
status: published
language: es
description: La teoría que establece que las redes neuronales densas contienen subredes
  más pequeñas que, cuando se entrenan de forma aislada desde su inicialización, pueden
  igualar la precisión de la red original
---
## Definition

La Hipótesis del Billete de Lotería sugiere que dentro de una gran red neuronal inicializada aleatoriamente, existe una subred dispersa (el 'billete ganador') que está bien inicializada para el entrenamiento. Al podar sistemáticamente los pesos menos importantes y volver a entrenar la subred resultante desde su estado inicial, esta puede alcanzar una precisión comparable a la de la red densa original, demostrando que la redundancia en las redes densas es significativa y que es posible comprimir modelos sin pérdida sustancial de rendimiento.

### Summary

La teoría que establece que las redes neuronales densas contienen subredes más pequeñas que, cuando se entrenan de forma aislada desde su inicialización, pueden igualar la precisión de la red original.

## Key Concepts

- Podado de pesos
- Redes dispersas
- Compresión de modelos
- Sensibilidad de inicialización

## Use Cases

- Despliegue de modelos ligeros en dispositivos de borde
- Reducción de costes computacionales durante el entrenamiento
- Aceleración de las velocidades de inferencia

## Related Terms

- [Network Pruning (Podado de redes)](/en/terms/network-pruning-podado-de-redes/)
- [Model Distillation (Destilación de modelos)](/en/terms/model-distillation-destilación-de-modelos/)
- [Sparse Training (Entrenamiento disperso)](/en/terms/sparse-training-entrenamiento-disperso/)
- [Efficient AI (IA eficiente)](/en/terms/efficient-ai-ia-eficiente/)
