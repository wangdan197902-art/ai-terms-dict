---
title: "on-policy (basado en la política actual)"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T10:28:41.323375Z"
lastmod: "2026-07-18T11:44:44.757901Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un enfoque de aprendizaje por refuerzo donde la política que se evalúa y mejora es la misma que se utiliza para generar los datos."
---
## Definition

Los algoritmos on-policy requieren que el agente aprenda directamente de las acciones tomadas por su política actual. Esto significa que los datos recopilados durante la exploración se utilizan inmediatamente para actualizar la política, asegurando la consistencia.

### Summary

Un enfoque de aprendizaje por refuerzo donde la política que se evalúa y mejora es la misma que se utiliza para generar los datos.

## Key Concepts

- aprendizaje por refuerzo
- gradiente de política (policy gradient)
- consistencia de datos
- eficiencia de muestras

## Use Cases

- Control de robótica con restricciones de seguridad
- Agentes de juego que requieren actualizaciones precisas
- Sistemas adaptativos en tiempo real

## Related Terms

- [off-policy (fuera de la política)](/en/terms/off-policy-fuera-de-la-política/)
- [REINFORCE (algoritmo REINFORCE)](/en/terms/reinforce-algoritmo-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (arquitectura actor-crítico)](/en/terms/actor-critic-arquitectura-actor-crítico/)
