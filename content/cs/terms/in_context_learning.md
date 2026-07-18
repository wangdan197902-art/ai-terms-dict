---
title: "Učení v kontextu (In-Context Learning)"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /cs/terms/in_context_learning/
date: "2026-07-18T15:23:01.660691Z"
lastmod: "2026-07-18T17:15:09.063067Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Technika, při které se modely učí plnit úkoly pozorováním příkladů poskytnutých v zadání."
---

## Definition

Učení v kontextu (ICL) umožňuje velkým jazykovým modelům přizpůsobit se novým úkolům bez aktualizace jejich vah. Poskytováním párů vstup-výstup přímo v kontextu zadání model odvodí vzorec a dokáže na základě něj reagovat, aniž by došlo k jakékoli změně parametrů modelu.

### Summary

Technika, při které se modely učí plnit úkoly pozorováním příkladů poskytnutých v zadání.

## Key Concepts

- Učení s několika příklady (Few-Shot Learning)
- Nulový zásah (Zero-Shot)
- Návrh zadání (Prompt Design)
- Adaptace bez změn vah

## Use Cases

- Rychlé testování schopností modelu na nových datech
- Dynamické přepínání úkolů v konverzačních agentech
- Prototypování AI aplikací bez nutnosti opětovného trénování

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Inženýrství promptů (Prompt Engineering)](/en/terms/inženýrství-promptů-prompt-engineering/)
- [Few-Shot (učení z několika málo příkladů)](/en/terms/few-shot-učení-z-několika-málo-příkladů/)
- [Zero-Shot (učení bez příkladů)](/en/terms/zero-shot-učení-bez-příkladů/)
- [Meta-učení (Meta-Learning)](/en/terms/meta-učení-meta-learning/)
