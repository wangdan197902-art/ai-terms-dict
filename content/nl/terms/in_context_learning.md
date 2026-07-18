---
title: "In-Context Learning"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /nl/terms/in_context_learning/
date: "2026-07-18T15:22:56.815828Z"
lastmod: "2026-07-18T17:15:08.679392Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een techniek waarbij modellen taken leren uitvoeren door voorbeelden te observeren die in de prompt zijn gegeven."
---

## Definition

In-context learning (ICL) stelt grote taalmodellen in staat zich aan te passen aan nieuwe taken zonder hun gewichten bij te werken. Door input-outputparen binnen de promptcontext te bieden, inferert het model het patroon en

### Summary

Een techniek waarbij modellen taken leren uitvoeren door voorbeelden te observeren die in de prompt zijn gegeven.

## Key Concepts

- Few-shot learning (leren met weinig voorbeelden)
- Zero-shot (leren zonder voorbeelden)
- Promptontwerp
- Gewichtloze aanpassing

## Use Cases

- Snel testen van modelcapaciteiten op nieuwe datasets
- Dynamisch wisselen van taken in conversational agents
- Prototypen van AI-toepassingen zonder hertraining

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt engineering (het ontwerpen van invoeropdrachten)](/en/terms/prompt-engineering-het-ontwerpen-van-invoeropdrachten/)
- [Few-shot (met enkele voorbeelden)](/en/terms/few-shot-met-enkele-voorbeelden/)
- [Zero-shot (zonder voorbeelden)](/en/terms/zero-shot-zonder-voorbeelden/)
- [Meta-learning (leren over leren)](/en/terms/meta-learning-leren-over-leren/)
