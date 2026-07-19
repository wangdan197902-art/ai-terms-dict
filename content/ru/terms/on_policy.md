---
title: "on-policy (он-полиси)"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T15:31:52.578283Z"
lastmod: "2026-07-18T16:38:07.096654Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Подход обучения с подкреплением, при котором политика, которая оценивается и улучшается, является той же самой, что используется для генерации данных."
---
## Definition

Алгоритмы on-policy требуют, чтобы агент учился непосредственно на действиях, совершаемых его текущей политикой. Это означает, что данные, собранные во время исследования среды, используются немедленно для обновления политики, обеспечивая согласованность выборки.

### Summary

Подход обучения с подкреплением, при котором политика, которая оценивается и улучшается, является той же самой, что используется для генерации данных.

## Key Concepts

- обучение с подкреплением
- градиент политики (policy gradient)
- согласованность данных
- эффективность выборки

## Use Cases

- Управление роботами с ограничениями безопасности
- Агенты для игр, требующие точных обновлений
- Системы адаптации в реальном времени

## Related Terms

- [off-policy (офф-полиси)](/en/terms/off-policy-офф-полиси/)
- [REINFORCE (алгоритм REINFORCE)](/en/terms/reinforce-алгоритм-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (архитектура актер-критик)](/en/terms/actor-critic-архитектура-актер-критик/)
