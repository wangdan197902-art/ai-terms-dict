---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
aliases:
  - /ro/terms/on_policy/
date: "2026-07-18T15:33:06.879546Z"
lastmod: "2026-07-18T17:15:09.609895Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O abordare de învățare prin întărire în care politica evaluată și îmbunătățită este aceeași cu cea utilizată pentru generarea datelor."
---

## Definition

Algoritmii on-policy necesită ca agentul să învețe direct din acțiunile întreprinse de politica sa curentă. Acest lucru înseamnă că datele colectate în timpul explorării sunt utilizate imediat pentru a actualiza politica, asigurând coerența.

### Summary

O abordare de învățare prin întărire în care politica evaluată și îmbunătățită este aceeași cu cea utilizată pentru generarea datelor.

## Key Concepts

- învățare prin întărire
- gradient de politică
- consistența datelor
- eficiența eșantionării

## Use Cases

- Control robotic cu constrângeri de siguranță
- Agente de joc care necesită actualizări precise
- Sisteme adaptive în timp real

## Related Terms

- [off-policy (off-policy)](/en/terms/off-policy-off-policy/)
- [REINFORCE (algoritmul REINFORCE)](/en/terms/reinforce-algoritmul-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (arhitectura actor-critic)](/en/terms/actor-critic-arhitectura-actor-critic/)
