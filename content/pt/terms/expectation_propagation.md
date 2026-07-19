---
title: Propagação de Expectativa
term_id: expectation_propagation
category: basic_concepts
subcategory: ''
tags:
- Bayesian Methods
- inference
- Probabilistic Models
difficulty: 5
weight: 1
slug: expectation_propagation
date: '2026-07-18T14:59:29.148788Z'
lastmod: '2026-07-18T15:51:59.489688Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um algoritmo de inferência aproximada usado para estimar distribuições
  posteriores em modelos gráficos probabilísticos complexos.
---
## Definition

A Propagação de Expectativa (EP) aproxima integrais intratáveis refinando iterativamente aproximações gaussianas da verdadeira distribuição posterior. Ela minimiza a divergência de Kullback-Leibler entre a distribuição aproximada e a verdadeira, permitindo uma inferência mais precisa em modelos bayesianos complexos.

### Summary

Um algoritmo de inferência aproximada usado para estimar distribuições posteriores em modelos gráficos probabilísticos complexos.

## Key Concepts

- Aproximação Posterior
- Correspondência de Momentos
- Divergência de Kullback-Leibler
- Processos Gaussianos

## Use Cases

- Processos Gaussianos esparsos
- Regressão logística bayesiana
- Fatoração matricial probabilística

## Related Terms

- [variational_inference (inferência variacional)](/en/terms/variational_inference-inferência-variacional/)
- [gaussian_processes (processos gaussianos)](/en/terms/gaussian_processes-processos-gaussianos/)
- [bayesian_inference (inferência bayesiana)](/en/terms/bayesian_inference-inferência-bayesiana/)
- [mean_field_approximation (aproximação de campo médio)](/en/terms/mean_field_approximation-aproximação-de-campo-médio/)
