---
title: "Алгоритм «актор-критик»"
term_id: "actor_critic_algorithm"
category: "basic_concepts"
subcategory: ""
tags: ["reinforcement_learning", "neural_networks", "algorithms"]
difficulty: 4
weight: 1
slug: "actor_critic_algorithm"
aliases:
  - /ru/terms/actor_critic_algorithm/
date: "2026-07-18T15:39:26.569243Z"
lastmod: "2026-07-18T16:38:07.116330Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Фреймворк обучения с подкреплением, сочетающий методы, основанные на ценности и политике, с использованием двух нейронных сетей: актора и критика."
---

## Definition

Алгоритм «актор-критик» состоит из двух компонентов: актора, который обновляет политику для выбора действий, и критика, который оценивает качество этих действий путём оценки функции ценности.

### Summary

Фреймворк обучения с подкреплением, сочетающий методы, основанные на ценности и политике, с использованием двух нейронных сетей: актора и критика.

## Key Concepts

- Градиент политики
- Функция ценности
- Ошибка временной разницы
- Гибридное обучение с подкреплением

## Use Cases

- Манипулирование роботизированным манипулятором
- Игровые агенты (например, AlphaStar)
- Системы непрерывного управления в автономных транспортных средствах

## Related Terms

- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [A3C (Asynchronous Advantage Actor-Critic)](/en/terms/a3c-asynchronous-advantage-actor-critic/)
- [policy_gradient (Градиент политики)](/en/terms/policy_gradient-градиент-политики/)
- [value_function (Функция ценности)](/en/terms/value_function-функция-ценности/)
