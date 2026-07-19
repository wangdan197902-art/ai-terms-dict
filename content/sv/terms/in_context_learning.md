---
title: "In-context learning"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:23:00.635122Z"
lastmod: "2026-07-18T17:15:08.936549Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En teknik där modeller lär sig utföra uppgifter genom att observera exempel som tillhandahålls i prompten."
---
## Definition

In-context learning (ICL) gör att stora språkmodeller kan anpassa sig till nya uppgifter utan att uppdatera sina vikter. Genom att tillhandahålla indata-och-utdata-par inom promptkontexten, drar modellen slutsatser om mönstret och utför uppgiften.

### Summary

En teknik där modeller lär sig utföra uppgifter genom att observera exempel som tillhandahålls i prompten.

## Key Concepts

- Few-shot learning
- Zero-shot
- Promptdesign
- Vikt-fri anpassning

## Use Cases

- Snabbtestning av modellkapacitet på nya datamängder
- Dynamisk uppgiftsbyte i konversationella agenter
- Prototypframtagning av AI-applikationer utan omträning

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt-engineering](/en/terms/prompt-engineering/)
- [Few-shot (få-exempel)](/en/terms/few-shot-få-exempel/)
- [Zero-shot (noll-exempel)](/en/terms/zero-shot-noll-exempel/)
- [Meta-inlärning](/en/terms/meta-inlärning/)
