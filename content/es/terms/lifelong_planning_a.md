---
title: Planificación A* de por vida
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
date: '2026-07-18T10:57:37.952598Z'
lastmod: '2026-07-18T11:44:44.825973Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un algoritmo de búsqueda de caminos incremental que actualiza eficientemente
  las rutas más cortas en grafos dinámicos sin recalcular desde cero tras cambios
  en el peso de las aristas.
---
## Definition

La Planificación A* de por vida (LPA*, por sus siglas en inglés) es una extensión del algoritmo de búsqueda A* diseñada para entornos donde los costes cambian con el tiempo. En lugar de reiniciar la búsqueda desde el principio, LPA* mantiene una cola de prioridad y actualiza selectivamente solo las partes del grafo afectadas por los cambios, lo que resulta en una eficiencia computacional significativamente mayor en escenarios dinámicos.

### Summary

Un algoritmo de búsqueda de caminos incremental que actualiza eficientemente las rutas más cortas en grafos dinámicos sin recalcular desde cero tras cambios en el peso de las aristas.

## Key Concepts

- Búsqueda incremental
- Búsqueda de caminos
- Grafos dinámicos
- Navegación robótica

## Use Cases

- Enrutamiento de vehículos autónomos en tráfico cambiante
- Navegación de robots en almacenes con configuración variable
- Movimiento de IA en juegos de estrategia en tiempo real

## Related Terms

- [A* (algoritmo de búsqueda heurística estándar)](/en/terms/a-algoritmo-de-búsqueda-heurística-estándar/)
- [D* (algoritmo de planificación dinámica relacionado)](/en/terms/d-algoritmo-de-planificación-dinámica-relacionado/)
- [búsqueda incremental (actualización parcial de soluciones)](/en/terms/búsqueda-incremental-actualización-parcial-de-soluciones/)
- [planificación de rutas (proceso de encontrar un camino óptimo)](/en/terms/planificación-de-rutas-proceso-de-encontrar-un-camino-óptimo/)
