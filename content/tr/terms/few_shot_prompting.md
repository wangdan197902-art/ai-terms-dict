---
title: Az Örnekli İstem (Few-Shot Prompting)
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:34:34.239923Z'
lastmod: '2026-07-18T16:38:07.257744Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Az örnekli istem, büyük dil modellerinin (LLM) davranışlarını yönlendirmek
  için istem içinde küçük sayıda giriş-çıkış örneği sunulduğu bir tekniktir.
---
## Definition

Bu yöntem, doğrudan istem içinde birkaç açıklayıcı örnek sağlayarak büyük dil modellerinin bağlam içi öğrenme yeteneklerinden yararlanır. Model ağırlıklarını güncellemeyi gerektiren ince ayarın aksine,

### Summary

Az örnekli istem, büyük dil modellerinin (LLM) davranışlarını yönlendirmek için istem içinde küçük sayıda giriş-çıkış örneği sunulduğu bir tekniktir.

## Key Concepts

- Bağlam içi öğrenme
- İstem mühendisliği
- Örnek tabanlı rehberlik
- Sıfır örnekli karşılaştırma

## Use Cases

- Duygu analizi formatlama
- Kod stili uyarlaması
- Yapılandırılmış veri çıkarma

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

- [zero_shot (sıfır örnekli)](/en/terms/zero_shot-sıfır-örnekli/)
- [prompt_engineering (istem mühendisliği)](/en/terms/prompt_engineering-istem-mühendisliği/)
- [in_context_learning (bağlam içi öğrenme)](/en/terms/in_context_learning-bağlam-içi-öğrenme/)
- [llm (büyük dil modeli)](/en/terms/llm-büyük-dil-modeli/)
