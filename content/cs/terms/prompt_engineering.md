---
title: "Inženýrství promptů"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
aliases:
  - /cs/terms/prompt_engineering/
date: "2026-07-18T15:22:18.954363Z"
lastmod: "2026-07-18T17:15:09.060996Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Praxe navrhování a optimalizace vstupních textů k řízení velkých jazykových modelů k požadovaným výstupům."
---

## Definition

Inženýrství promptů zahrnuje vytváření specifických vstupů, známých jako prompty, aby se od generativních AI modelů vyvolaly přesné, relevantní a kvalitní odpovědi. Vyžaduje pochopení toho, jak modely interpretují kontext a instrukce.

### Summary

Praxe navrhování a optimalizace vstupních textů k řízení velkých jazykových modelů k požadovaným výstupům.

## Key Concepts

- Kontextové rámování
- Učení s několika příklady (few-shot learning)
- Ladění instrukcí (instruction tuning)
- Optimalizace tokenů

## Use Cases

- Automatizované zákaznické podpůrné chatboty
- Asistenti pro generování kódu
- Nástroje pro kreativní psaní

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (Velký jazykový model)](/en/terms/llm-velký-jazykový-model/)
- [Chain-of-Thought (Řetězec myšlenek)](/en/terms/chain-of-thought-řetězec-myšlenek/)
- [RAG (Retrieval-Augmented Generation)](/en/terms/rag-retrieval-augmented-generation/)
- [Fine-tuning (Doladění modelu)](/en/terms/fine-tuning-doladění-modelu/)
