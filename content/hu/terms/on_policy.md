---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T15:35:57.639829Z"
lastmod: "2026-07-18T17:15:09.736418Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy megerősítéses tanuló megközelítés, ahol az értéelt és fejlesztett politika ugyanaz, mint amelyiket az adatok generálásához használnak."
---
## Definition

Az on-policy algoritmusok azt követelik meg, hogy az ügynök közvetlenül a jelenlegi politikája által tett cselekvésekből tanuljon. Ez azt jelenti, hogy a felfedezés során gyűjtött adatokat azonnal felhasználják a politika frissítésére, biztosítva az adatok konzisztenciáját.

### Summary

Egy megerősítéses tanuló megközelítés, ahol az értéelt és fejlesztett politika ugyanaz, mint amelyiket az adatok generálásához használnak.

## Key Concepts

- megerősítéses tanulás
- politika gradiens
- adat konzisztencia
- mintahatékonyság

## Use Cases

- Robotika vezérlés biztonsági korlátokkal
- Pontos frissítéseket igénylő játékos ügynökök
- Valós idejű adaptív rendszerek

## Related Terms

- [off-policy (nem a jelenlegi politika alapján tanuló)](/en/terms/off-policy-nem-a-jelenlegi-politika-alapján-tanuló/)
- [REINFORCE (alapvető on-policy algoritmus)](/en/terms/reinforce-alapvető-on-policy-algoritmus/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (színész-kritikus architektúra)](/en/terms/actor-critic-színész-kritikus-architektúra/)
