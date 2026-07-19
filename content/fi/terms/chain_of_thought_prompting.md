---
title: "Ketjuajatteluprompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:35:27.713754Z"
lastmod: "2026-07-18T17:15:09.368323Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Ketjuajatteluprompting on tekniikka, joka kannustaa suuria kielimalleja tuottamaan välisiä päättelyvaiheita ennen lopullisen vastauksen antamista."
---
## Definition

Ketjuajattelu (CoT) -prompting parantaa suurten kielimallien suorituskykyä monimutkaisissa päättelytehtävissä pyytämällä mallia nimenomaisesti hahmottamaan vaiheittaisen logiikkansa. Sen sijaan, että malli hyppäisi suoraan

### Summary

Ketjuajatteluprompting on tekniikka, joka kannustaa suuria kielimalleja tuottamaan välisiä päättelyvaiheita ennen lopullisen vastauksen antamista.

## Key Concepts

- Vaiheittainen päättely
- Harvoin esimerkillä oppiminen (Few-shot learning)
- Looginen deduktio
- Välivaiheet

## Use Cases

- Matemaattisten sanallisten ongelmien ratkaiseminen
- Monimutkaiset loogiset päättelytehtävät
- Koodintuotannon virheiden debuggaus

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Nollaesimerkki-prompting (Zero-shot prompting)](/en/terms/nollaesimerkki-prompting-zero-shot-prompting/)
- [Harvoin esimerkillä-prompting (Few-shot prompting)](/en/terms/harvoin-esimerkillä-prompting-few-shot-prompting/)
- [Itse-yhteensopivuus (Self-consistency)](/en/terms/itse-yhteensopivuus-self-consistency/)
- [Päättely (Reasoning)](/en/terms/päättely-reasoning/)
