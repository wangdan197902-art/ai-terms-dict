---
title: "On-Policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
aliases:
  - /de/terms/on_policy/
date: "2026-07-18T10:56:17.755742Z"
lastmod: "2026-07-18T11:44:44.890298Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein Ansatz des bestärkenden Lernens (Reinforcement Learning), bei dem die bewertete und verbesserte Policy dieselbe ist, die zur Datengenerierung verwendet wird."
---

## Definition

On-Policy-Algorithmen erfordern, dass der Agent direkt aus den Aktionen lernt, die von seiner aktuellen Policy unternommen werden. Das bedeutet, dass während der Exploration gesammelte Daten sofort verwendet werden, um die Policy zu aktualisieren, wodurch Konsistenz gewährleistet wird.

### Summary

Ein Ansatz des bestärkenden Lernens (Reinforcement Learning), bei dem die bewertete und verbesserte Policy dieselbe ist, die zur Datengenerierung verwendet wird.

## Key Concepts

- bestärkendes Lernen
- Policy Gradient
- Datenkonsistenz
- Sample Efficiency

## Use Cases

- Robotiksteuerung mit Sicherheitsbeschränkungen
- Spielagenten, die präzise Updates benötigen
- Echtzeit-Adaptive Systeme

## Related Terms

- [off-policy (Off-Policy)](/en/terms/off-policy-off-policy/)
- [REINFORCE (REINFORCE-Algorithmus)](/en/terms/reinforce-reinforce-algorithmus/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (Actor-Critic-Architektur)](/en/terms/actor-critic-actor-critic-architektur/)
