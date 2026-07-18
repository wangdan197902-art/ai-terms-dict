---
title: "Învățare în Context"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /ro/terms/in_context_learning/
date: "2026-07-18T15:23:10.069385Z"
lastmod: "2026-07-18T17:15:09.588509Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O tehnică prin care modelele învață să execute sarcini observând exemplele furnizate în prompt."
---

## Definition

Învățarea în context (ICL) permite modelelor lingvistice mari să se adapteze la sarcini noi fără a actualiza ponderile acestora. Prin furnizarea perechilor intrare-ieșire în contextul promptului, modelul inferă modelul și execută sarcina corespunzătoare.

### Summary

O tehnică prin care modelele învață să execute sarcini observând exemplele furnizate în prompt.

## Key Concepts

- Învățare Few-Shot
- Zero-Shot
- Designul Promptului
- Adaptare Fără Ponderi

## Use Cases

- Testarea rapidă a capacităților modelului pe seturi de date noi
- Comutarea dinamică a sarcinilor în agenții conversaționali
- Prototiparea aplicațiilor AI fără reantrenare

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Ingineria Prompturilor (Prompt Engineering)](/en/terms/ingineria-prompturilor-prompt-engineering/)
- [Few-Shot (cu puține exemple)](/en/terms/few-shot-cu-puține-exemple/)
- [Zero-Shot (fără exemple)](/en/terms/zero-shot-fără-exemple/)
- [Meta-Învățare (Meta-Learning)](/en/terms/meta-învățare-meta-learning/)
