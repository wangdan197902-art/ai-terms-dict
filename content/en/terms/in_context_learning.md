---
title: "In-Context Learning"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T07:39:00.243208Z"
lastmod: "2026-07-18T11:44:44.579155Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A technique where models learn to perform tasks by observing examples provided in the prompt."
---
## Definition

In-context learning (ICL) allows large language models to adapt to new tasks without updating their weights. By providing input-output pairs within the prompt context, the model infers the pattern and applies it to new queries. This zero-shot or few-shot capability enables rapid prototyping and flexibility, serving as a powerful alternative to traditional fine-tuning for tasks requiring quick adaptation to novel domains.

### Summary

A technique where models learn to perform tasks by observing examples provided in the prompt.

## Key Concepts

- Few-Shot Learning
- Zero-Shot
- Prompt Design
- Weight-Free Adaptation

## Use Cases

- Quickly testing model capabilities on new datasets
- Dynamic task switching in conversational agents
- Prototyping AI applications without retraining

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering](/en/terms/prompt-engineering/)
- [Few-Shot](/en/terms/few-shot/)
- [Zero-Shot](/en/terms/zero-shot/)
- [Meta-Learning](/en/terms/meta-learning/)
