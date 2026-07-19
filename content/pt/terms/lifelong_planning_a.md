---
title: Planejamento Vitalício A*
term_id: lifelong_planning_a
category: application_paradigms
subcategory: ''
tags:
- algorithms
- robotics
- Graph Theory
difficulty: 4
weight: 1
slug: lifelong_planning_a
date: '2026-07-18T15:08:20.668441Z'
lastmod: '2026-07-18T15:51:59.507561Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um algoritmo incremental de busca de caminhos que atualiza eficientemente
  os caminhos mais curtos em grafos dinâmicos sem recalcular do zero após mudanças
  nos pesos das arestas.
---
## Definition

O Planejamento Vitalício A* (LPA*) é uma extensão do algoritmo de busca A* projetada para ambientes onde os custos mudam ao longo do tempo. Em vez de reiniciar a busca, o LPA* mantém uma fila de prioridade e atualiza apenas as partes afetadas do caminho.

### Summary

Um algoritmo incremental de busca de caminhos que atualiza eficientemente os caminhos mais curtos em grafos dinâmicos sem recalcular do zero após mudanças nos pesos das arestas.

## Key Concepts

- Busca Incremental
- Busca de Caminhos
- Grafos Dinâmicos
- Navegação Robótica

## Use Cases

- Roteamento de veículos autônomos no tráfego
- Navegação de robôs em armazéns em mudança
- Movimento de IA em jogos de estratégia em tempo real

## Related Terms

- [a_star (algoritmo A*)](/en/terms/a_star-algoritmo-a/)
- [d_star (algoritmo D*)](/en/terms/d_star-algoritmo-d/)
- [incremental_search (busca incremental)](/en/terms/incremental_search-busca-incremental/)
- [path_planning (planejamento de caminhos)](/en/terms/path_planning-planejamento-de-caminhos/)
