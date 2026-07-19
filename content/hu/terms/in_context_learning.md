---
title: "Kontextuson belüli tanulás"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:23:10.444315Z"
lastmod: "2026-07-18T17:15:09.714526Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy technika, ahol a modellek a promptban megadott példák megfigyelésével tanulnak meg feladatokat elvégezni."
---
## Definition

A kontextuson belüli tanulás (ICL) lehetővé teszi a nagy nyelvi modellek számára, hogy új feladatokhoz igazodjanak súlyaik frissítése nélkül. Bemenet-kimenet párok biztosítása a prompt kontextusán belül lehetővé teszi a modell számára, hogy...

### Summary

Egy technika, ahol a modellek a promptban megadott példák megfigyelésével tanulnak meg feladatokat elvégezni.

## Key Concepts

- Few-Shot Learning (keveset látó tanulás)
- Zero-Shot (nulla látásos)
- Prompt tervezés
- Súly nélküli alkalmazkodás

## Use Cases

- A modell képességeinek gyors tesztelése új adathalmazokon
- Dinamikus feladványváltás beszélgetési ügynököknél
- AI alkalmazások prototípuskészítése újratanítás nélkül

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (utasítás-mérnökség)](/en/terms/prompt-engineering-utasítás-mérnökség/)
- [Few-Shot (keveset látásos)](/en/terms/few-shot-keveset-látásos/)
- [Zero-Shot (nulla látásos)](/en/terms/zero-shot-nulla-látásos/)
- [Meta-Learning (meta-tanulás)](/en/terms/meta-learning-meta-tanulás/)
