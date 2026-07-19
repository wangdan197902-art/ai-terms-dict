---
title: "Auto-coerență"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
date: "2026-07-18T16:20:07.433211Z"
lastmod: "2026-07-18T17:15:09.700733Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Auto-coerența este o strategie de decodare în care sunt eșantionate mai multe căi de raționament, iar răspunsul cel mai frecvent este selectat ca ieșire finală."
---
## Definition

Utilizată în principal cu Modele Linguistice Mari (LLM), această tehnică îmbunătățește acuratețea generând mai multe răspunsuri diverse la un prompt prin eșantionare. În loc să se bazeze pe decodarea greșită (greedy decoding), aceasta agregă rezultatele multiple pentru a identifica consensul.

### Summary

Auto-coerența este o strategie de decodare în care sunt eșantionate mai multe căi de raționament, iar răspunsul cel mai frecvent este selectat ca ieșire finală.

## Key Concepts

- Vot majoritar
- Strategie de decodare
- Raționamentul LLM
- Reducerea halucinațiilor

## Use Cases

- Probleme matematice verbale
- Deducere logică complexă
- Sarcini de sinteză de cod

## Related Terms

- [Lanțul de gândire (Chain-of-thought)](/en/terms/lanțul-de-gândire-chain-of-thought/)
- [Eșantionarea temperaturii](/en/terms/eșantionarea-temperaturii/)
- [Metode de ansamblu](/en/terms/metode-de-ansamblu/)
- [Ingineria prompturilor](/en/terms/ingineria-prompturilor/)
