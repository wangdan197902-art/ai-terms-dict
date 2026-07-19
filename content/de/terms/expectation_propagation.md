---
title: Erwartungspropagation
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
date: '2026-07-18T11:13:48.471996Z'
lastmod: '2026-07-18T11:44:44.938349Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein approximativer Inferenzalgorithmus, der zur Schätzung von Posterior-Verteilungen
  in komplexen probabilistischen graphischen Modellen verwendet wird.
---
## Definition

Die Erwartungspropagation (EP) approximiert nicht handhabbare Integrale, indem sie iterativ Gaußsche Approximationen an die wahre Posterior-Verteilung verfeinert. Sie minimiert die Kullback-Leibler-Divergenz zwischen der approximativen und der wahren Verteilung, oft unter der Annahme, dass die Approximation in der Familie der Gaußschen Verteilungen liegt.

### Summary

Ein approximativer Inferenzalgorithmus, der zur Schätzung von Posterior-Verteilungen in komplexen probabilistischen graphischen Modellen verwendet wird.

## Key Concepts

- Posterior-Approximation
- Momentenanpassung
- Kullback-Leibler-Divergenz
- Gaußsche Prozesse

## Use Cases

- Sparse Gaußsche Prozesse
- Bayessche logistische Regression
- Probabilistische Matrixfaktorisierung

## Related Terms

- [variational_inference (Variationale Inferenz)](/en/terms/variational_inference-variationale-inferenz/)
- [gaussian_processes (Gaußsche Prozesse)](/en/terms/gaussian_processes-gaußsche-prozesse/)
- [bayesian_inference (Bayessche Inferenz)](/en/terms/bayesian_inference-bayessche-inferenz/)
- [mean_field_approximation (Mean-Field-Approximation)](/en/terms/mean_field_approximation-mean-field-approximation/)
