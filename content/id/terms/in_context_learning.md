---
title: "Pembelajaran Dalam Konteks"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /id/terms/in_context_learning/
date: "2026-07-18T15:23:01.511884Z"
lastmod: "2026-07-18T16:38:07.387896Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sebuah teknik di mana model belajar melakukan tugas dengan mengamati contoh yang disediakan dalam prompt."
---

## Definition

Pembelajaran dalam konteks (ICL) memungkinkan model bahasa besar beradaptasi dengan tugas baru tanpa memperbarui bobotnya. Dengan menyediakan pasangan input-output dalam konteks prompt, model menyimpulkan pola dan

### Summary

Sebuah teknik di mana model belajar melakukan tugas dengan mengamati contoh yang disediakan dalam prompt.

## Key Concepts

- Pembelajaran Few-Shot
- Zero-Shot
- Desain Prompt
- Adaptasi Tanpa Bobot

## Use Cases

- Menguji kemampuan model dengan cepat pada dataset baru
- Pergantian tugas dinamis dalam agen percakapan
- Prototipe aplikasi AI tanpa pelatihan ulang

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Rekayasa Prompt (Prompt Engineering)](/en/terms/rekayasa-prompt-prompt-engineering/)
- [Few-Shot (Beberapa Contoh)](/en/terms/few-shot-beberapa-contoh/)
- [Zero-Shot (Tanpa Contoh)](/en/terms/zero-shot-tanpa-contoh/)
- [Meta-Pembelajaran (Meta-Learning)](/en/terms/meta-pembelajaran-meta-learning/)
