---
title: "Prompting Berpikir Bertahap"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:33:49.614429Z"
lastmod: "2026-07-18T16:38:07.411833Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Prompting Berpikir Bertahap adalah teknik yang mendorong Model Bahasa Besar (LLM) untuk menghasilkan langkah-langkah penalaran perantara sebelum menghasilkan jawaban akhir."
---
## Definition

Prompting Berpikir Bertahap (CoT) meningkatkan kinerja model bahasa besar pada tugas penalaran kompleks dengan secara eksplisit meminta model untuk mengartikulasikan logika langkah demi langkahnya. Alih-alih melompat langsung ke

### Summary

Prompting Berpikir Bertahap adalah teknik yang mendorong Model Bahasa Besar (LLM) untuk menghasilkan langkah-langkah penalaran perantara sebelum menghasilkan jawaban akhir.

## Key Concepts

- Penalaran Langkah demi Langkah
- Pembelajaran Few-Shot
- Deduksi Logis
- Langkah-Langkah Perantara

## Use Cases

- Memecahkan masalah matematika berbasis kata
- Tugas penalaran logis yang kompleks
- Men-debug kesalahan generasi kode

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (Prompting tanpa contoh)](/en/terms/zero-shot-prompting-prompting-tanpa-contoh/)
- [Few-Shot Prompting (Prompting dengan beberapa contoh)](/en/terms/few-shot-prompting-prompting-dengan-beberapa-contoh/)
- [Self-Consistency (Konsistensi Diri)](/en/terms/self-consistency-konsistensi-diri/)
- [Reasoning (Penalaran)](/en/terms/reasoning-penalaran/)
