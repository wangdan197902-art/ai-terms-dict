---
title: "Colapso de Representação"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /pt/terms/representation_collapse/
date: "2026-07-18T15:19:39.994259Z"
lastmod: "2026-07-18T15:51:59.528950Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um modo de falha no aprendizado auto-supervisionado onde o modelo produz representações idênticas para todas as entradas, perdendo poder discriminativo."
---

## Definition

O colapso de representação ocorre quando uma rede neural, particularmente em estruturas de aprendizado contrastivo auto-supervisionado, aprende a mapear todos os pontos de dados de entrada para o mesmo vetor de saída fixo. Essa solução trivial elimina a utilidade das representações aprendidas, pois elas não conseguem distinguir entre diferentes amostras de dados.

### Summary

Um modo de falha no aprendizado auto-supervisionado onde o modelo produz representações idênticas para todas as entradas, perdendo poder discriminativo.

## Key Concepts

- Aprendizado Auto-supervisionado
- Perda Contrastiva
- Soluções Triviais
- Aprendizado de Características

## Use Cases

- Depuração de modelos SimCLR ou MoCo
- Melhoria de Funções de Perda Contrastiva
- Análise de Convergência do Modelo

## Related Terms

- [Aprendizado Contrastivo](/en/terms/aprendizado-contrastivo/)
- [Normalização por Lote](/en/terms/normalização-por-lote/)
- [Codificador de Momento](/en/terms/codificador-de-momento/)
- [Extração de Características](/en/terms/extração-de-características/)
