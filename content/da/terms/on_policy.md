---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T15:32:39.006774Z"
lastmod: "2026-07-18T17:15:09.240042Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En tilgang inden for forstærkningslæring, hvor den politik, der evalueres og forbedres, er den samme som den, der bruges til at generere data."
---
## Definition

On-policy-algoritmer kræver, at agenten lærer direkte fra de handlinger, den aktuelle politik tager. Dette betyder, at data, der indsamles under udforskning, straks bruges til at opdatere politikken, hvilket sikrer konsistens.

### Summary

En tilgang inden for forstærkningslæring, hvor den politik, der evalueres og forbedres, er den samme som den, der bruges til at generere data.

## Key Concepts

- forstærkningslæring
- policy gradient (politikgradient)
- datakonsistens
- prøveeffektivitet

## Use Cases

- Robotstyring med sikkerhedsbegrænsninger
- Spillende agenter, der kræver præcise opdateringer
- Systemer, der tilpasser sig i realtid

## Related Terms

- [off-policy (off-policy)](/en/terms/off-policy-off-policy/)
- [REINFORCE (REINFORCE)](/en/terms/reinforce-reinforce/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (aktør-kritiker)](/en/terms/actor-critic-aktør-kritiker/)
