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
  - /sv/terms/on_policy/
date: "2026-07-18T15:36:19.307380Z"
lastmod: "2026-07-18T17:15:08.958231Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En förstärkningsinlärningsansats där den policy som utvärderas och förbättras är densamma som den som används för att generera data."
---

## Definition

On-policy-algoritmer kräver att agenten lär sig direkt från de handlingar som tas av dess nuvarande policy. Detta innebär att data som samlas in under utforskning används omedelbart för att uppdatera policyn, vilket säkerställer...

### Summary

En förstärkningsinlärningsansats där den policy som utvärderas och förbättras är densamma som den som används för att generera data.

## Key Concepts

- förstärkningsinlärning
- policy gradient
- datakonsekvens
- provs effektivitet

## Use Cases

- Robotstyrning med säkerhetsbegränsningar
- Spelande agenter som kräver precisa uppdateringar
- System som anpassas i realtid

## Related Terms

- [off-policy (off-policy)](/en/terms/off-policy-off-policy/)
- [REINFORCE (REINFORCE)](/en/terms/reinforce-reinforce/)
- [PPO (proximal policy optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (aktör-kritiker)](/en/terms/actor-critic-aktör-kritiker/)
