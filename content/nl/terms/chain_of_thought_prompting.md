---
title: "Chain-of-Thought Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /nl/terms/chain_of_thought_prompting/
date: "2026-07-18T15:35:24.860483Z"
lastmod: "2026-07-18T17:15:08.702478Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Chain-of-Thought Prompting is een techniek die grote taalmodellen (LLM's) aanmoedigt om tussenliggende redeneringsstappen te genereren voordat ze een eindantwoord produceren."
---

## Definition

Chain-of-Thought (CoT) prompting verbetert de prestaties van grote taalmodellen bij complexe redeneertaken door expliciet om de model te vragen zijn stap-voor-stap logica te articuleren. In plaats van direct naar

### Summary

Chain-of-Thought Prompting is een techniek die grote taalmodellen (LLM's) aanmoedigt om tussenliggende redeneringsstappen te genereren voordat ze een eindantwoord produceren.

## Key Concepts

- Stap-voor-stap redenering
- Few-Shot Learning (leren met weinig voorbeelden)
- Logische deductie
- Tussenliggende stappen

## Use Cases

- Het oplossen van wiskundige woordproblemen
- Taken met complexe logische redenering
- Het debuggen van fouten in gegenereerde code

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (prompting zonder voorbeelden)](/en/terms/zero-shot-prompting-prompting-zonder-voorbeelden/)
- [Few-Shot Prompting (prompting met enkele voorbeelden)](/en/terms/few-shot-prompting-prompting-met-enkele-voorbeelden/)
- [Zelfconsistentie (self-consistency)](/en/terms/zelfconsistentie-self-consistency/)
- [Redenering (reasoning)](/en/terms/redenering-reasoning/)
