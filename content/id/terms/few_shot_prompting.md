---
title: "Pemrograman Few-Shot"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /id/terms/few_shot_prompting/
date: "2026-07-18T15:34:29.559841Z"
lastmod: "2026-07-18T16:38:07.413648Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Pemrograman few-shot adalah teknik di mana LLM diberikan sejumlah kecil contoh input-output dalam prompt untuk membimbing perilakunya."
---

## Definition

Metode ini memanfaatkan kemampuan pembelajaran konteks dari model bahasa besar dengan memberikan beberapa contoh ilustratif langsung di dalam prompt. Berbeda dengan penyetelan halus (fine-tuning) yang memerlukan pembaruan bobot model, pendekatan ini hanya mengubah input teks untuk mengarahkan keluaran model.

### Summary

Pemrograman few-shot adalah teknik di mana LLM diberikan sejumlah kecil contoh input-output dalam prompt untuk membimbing perilakunya.

## Key Concepts

- Pembelajaran konteks
- Rekayasa prompt
- Bimbingan berbasis contoh
- Perbandingan nol-shot

## Use Cases

- Format analisis sentimen
- Adaptasi gaya kode
- Ekstraksi data terstruktur

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (nol-shot)](/en/terms/zero_shot-nol-shot/)
- [prompt_engineering (rekayasa prompt)](/en/terms/prompt_engineering-rekayasa-prompt/)
- [in_context_learning (pembelajaran dalam konteks)](/en/terms/in_context_learning-pembelajaran-dalam-konteks/)
- [llm (model bahasa besar)](/en/terms/llm-model-bahasa-besar/)
