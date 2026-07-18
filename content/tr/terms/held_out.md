---
title: "ayrılmış (held-out)"
term_id: "held_out"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "data_splitting", "validation"]
difficulty: 2
weight: 1
slug: "held_out"
aliases:
  - /tr/terms/held_out/
date: "2026-07-18T15:31:33.833532Z"
lastmod: "2026-07-18T16:38:07.249516Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Model performansını değerlendirmek ve geliştirme sırasında aşırı öğrenmeyi önlemek için eğitim kümesinden ayrılan veri örnekleri."
---

## Definition

'Ayrılmış' (held-out) bir veri kümesi, makine öğrenimi modelinin eğitim aşamasından kasıtlı olarak hariç tutulan örneklerden oluşur. Bu alt küme, modelin görünmeyen verilere ne kadar iyi genelleme yaptığını değerlendirmek için kullanılır ve modelin geliştirme sürecindeki gerçek performansını objektif bir şekilde ölçmeye olanak tanır. Genellikle eğitim ve test verisi arasında bir ara aşama olarak kullanılır, böylece hiperparametre ayarlaması sırasında test verisinin sızması (data leakage) engellenir.

### Summary

Model performansını değerlendirmek ve geliştirme sırasında aşırı öğrenmeyi önlemek için eğitim kümesinden ayrılan veri örnekleri.

## Key Concepts

- Genelleme
- Aşırı öğrenme
- Doğrulama kümesi
- Önyargısız değerlendirme

## Use Cases

- Hiperparametreleri ayarlama
- Farklı model mimarilerini karşılaştırma
- Üretime geçmeden önce nihai performans tahmini

## Related Terms

- [training_set (eğitim kümesi)](/en/terms/training_set-eğitim-kümesi/)
- [test_set (test kümesi)](/en/terms/test_set-test-kümesi/)
- [cross_validation (çapraz doğrulama)](/en/terms/cross_validation-çapraz-doğrulama/)
- [generalization (genelleme)](/en/terms/generalization-genelleme/)
