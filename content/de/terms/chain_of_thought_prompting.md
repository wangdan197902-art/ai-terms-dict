---
title: "Chain-of-Thought-Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /de/terms/chain_of_thought_prompting/
date: "2026-07-18T10:57:35.607299Z"
lastmod: "2026-07-18T11:44:44.893082Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Chain-of-Thought-Prompting ist eine Technik, die große Sprachmodelle (LLMs) dazu anregt, vor der Erzeugung einer endgültigen Antwort Zwischenschritte der Argumentation zu generieren."
---

## Definition

Chain-of-Thought (CoT)-Prompting verbessert die Leistung großer Sprachmodelle bei komplexen Aufgaben zur logischen Schlussfolgerung, indem das Modell explizit aufgefordert wird, seine schrittweise Logik darzulegen. Anstatt direkt zu

### Summary

Chain-of-Thought-Prompting ist eine Technik, die große Sprachmodelle (LLMs) dazu anregt, vor der Erzeugung einer endgültigen Antwort Zwischenschritte der Argumentation zu generieren.

## Key Concepts

- Schritt-für-Schritt-Argumentation
- Few-Shot-Lernen
- Logische Deduktion
- Zwischenschritte

## Use Cases

- Lösung mathematischer Textaufgaben
- Komplexe Aufgaben zur logischen Schlussfolgerung
- Fehlerbehebung bei Codegenerierungsfehlern

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot-Prompting (Prompting ohne Beispiele)](/en/terms/zero-shot-prompting-prompting-ohne-beispiele/)
- [Few-Shot-Prompting (Prompting mit wenigen Beispielen)](/en/terms/few-shot-prompting-prompting-mit-wenigen-beispielen/)
- [Selbstkonsistenz (Konsistenzprüfung der Antworten)](/en/terms/selbstkonsistenz-konsistenzprüfung-der-antworten/)
- [Schlussfolgerung (logisches Ableiten)](/en/terms/schlussfolgerung-logisches-ableiten/)
