---
title: "Prompt mérnökség"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T15:22:26.336457Z"
lastmod: "2026-07-18T17:15:09.712600Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A nagy nyelvi modelleket kívánt kimenetek felé terelő bemeneti szövegek tervezésének és optimalizálásának gyakorlata."
---
## Definition

A prompt mérnökség magában foglalja a specifikus bemenetek, az úgynevezett promptok (utasítások) megalkotását a generatív AI modellektől pontos, releváns és magas minőségű válaszok kiváltása érdekében. Megértést igényel, hogyan értelmezik a modellek a kontextust.

### Summary

A nagy nyelvi modelleket kívánt kimenetek felé terelő bemeneti szövegek tervezésének és optimalizálásának gyakorlata.

## Key Concepts

- Kontextuális keretezés
- Few-shot tanulás
- Utasítás-alapú finomhangolás
- Token-optimalizálás

## Use Cases

- Automatikus ügyfélszolgálati chatbotok
- Kódgeneráló asszisztensek
- Kreatív írási segédletek

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (Nagy Nyelvi Modell)](/en/terms/llm-nagy-nyelvi-modell/)
- [Chain-of-Thought (Gondolatmenet-lánc)](/en/terms/chain-of-thought-gondolatmenet-lánc/)
- [RAG (Retrieval-Augmented Generation / Visszakeresést fokozott generáció)](/en/terms/rag-retrieval-augmented-generation-visszakeresést-fokozott-generáció/)
- [Fine-tuning (Finomhangolás)](/en/terms/fine-tuning-finomhangolás/)
