---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T15:33:07.548831Z"
lastmod: "2026-07-18T17:15:08.580927Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un approccio di apprendimento per rinforzo in cui la politica valutata e migliorata è la stessa utilizzata per generare i dati."
---
## Definition

Gli algoritmi on-policy richiedono che l'agente impari direttamente dalle azioni intraprese dalla sua politica corrente. Ciò significa che i dati raccolti durante l'esplorazione vengono utilizzati immediatamente per aggiornare la politica, garantendo coerenza.

### Summary

Un approccio di apprendimento per rinforzo in cui la politica valutata e migliorata è la stessa utilizzata per generare i dati.

## Key Concepts

- apprendimento per rinforzo
- policy gradient (gradiente della politica)
- coerenza dei dati
- efficienza campionaria

## Use Cases

- Controllo robotico con vincoli di sicurezza
- Agenti per giochi che richiedono aggiornamenti precisi
- Sistemi adattivi in tempo reale

## Related Terms

- [off-policy (fuori-policy)](/en/terms/off-policy-fuori-policy/)
- [REINFORCE (algoritmo REINFORCE)](/en/terms/reinforce-algoritmo-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (attore-critico)](/en/terms/actor-critic-attore-critico/)
