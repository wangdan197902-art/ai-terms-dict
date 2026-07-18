---
title: "Bağlam İçi Öğrenme"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /tr/terms/in_context_learning/
date: "2026-07-18T15:23:00.947087Z"
lastmod: "2026-07-18T16:38:07.226074Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Modellerin, istem içinde sağlanan örnekleri gözlemleyerek görevleri öğrenmesini sağlayan bir teknik."
---

## Definition

Bağlam içi öğrenme (ICL), büyük dil modellerinin ağırlıklarını güncellemeden yeni görevlere uyum sağlamasına olanak tanır. İstem bağlamı içindeki girdi-çıktı çiftlerini sağlayarak model

### Summary

Modellerin, istem içinde sağlanan örnekleri gözlemleyerek görevleri öğrenmesini sağlayan bir teknik.

## Key Concepts

- Az Örnekli Öğrenme
- Sıfır Örnekli
- İstem Tasarımı
- Ağırlıksız Uyarlanabilirlik

## Use Cases

- Yeni veri setlerinde model yeteneklerini hızlıca test etmek
- Sohbet ajanlarında dinamik görev değiştirme
- Yeniden eğitim yapmadan yapay zeka uygulamalarını prototiplemek

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (İstem Mühendisliği)](/en/terms/prompt-engineering-i-stem-mühendisliği/)
- [Few-Shot (Az Örnekli)](/en/terms/few-shot-az-örnekli/)
- [Zero-Shot (Sıfır Örnekli)](/en/terms/zero-shot-sıfır-örnekli/)
- [Meta-Learning (Meta Öğrenme)](/en/terms/meta-learning-meta-öğrenme/)
