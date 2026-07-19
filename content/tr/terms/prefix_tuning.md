---
title: Önek Ayarlama (Prefix Tuning)
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T16:09:34.574633Z'
lastmod: '2026-07-18T16:38:07.350369Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Dönüştürücü katmanlarının girişine eğitilebilir sürekli vektörler ekleyerek
  parametre verimliliği sağlayan ince ayar yöntemidir.
---
## Definition

Önek Ayarlama, önceden eğitilmiş dönüştürücüler için parametre verimli bir uyarlamadır. Tüm model ağırlıklarını güncellemek yerine, girişe eğitilebilir sürekli vektörlerden oluşan bir diziyi (öneki) ekler. Bu sayede modelin çekirdek ağırlıkları dondurulurken, sadece küçük bir önek parametre seti eğitilir; bu da hesaplama maliyetini önemli ölçüde düşürür.

### Summary

Dönüştürücü katmanlarının girişine eğitilebilir sürekli vektörler ekleyerek parametre verimliliği sağlayan ince ayar yöntemidir.

## Key Concepts

- Parametre verimli ayarlama
- Yumuşak ipuçları (Soft prompts)
- Dönüştürücü katmanları
- Dondurulmuş temel model

## Use Cases

- Az örnekli öğrenme adaptasyonu
- Sınırlı kaynaklarla çok görevli öğrenme
- Niş alanlar için LLM'lerin özelleştirilmesi

## Related Terms

- [prompt_tuning (ipucu ayarlama)](/en/terms/prompt_tuning-ipucu-ayarlama/)
- [p_tuning (P-Tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (uyarlayıcı modüller)](/en/terms/adapter_modules-uyarlayıcı-modüller/)
- [peft (parametre verimli ince ayarlama)](/en/terms/peft-parametre-verimli-ince-ayarlama/)
