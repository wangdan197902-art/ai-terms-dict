---
title: "QLoRA"
term_id: "qlora"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "fine-tuning", "efficiency"]
difficulty: 4
weight: 1
slug: "qlora"
aliases:
  - /tr/terms/qlora/
date: "2026-07-18T15:36:47.227528Z"
lastmod: "2026-07-18T16:38:07.261795Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "4-bit nicelleme ve düşük ranklı adaptörler kullanarak büyük dil modellerini verimli bir şekilde ince ayar yapmak için kullanılan Nicellenmiş Düşük Ranklı Uyarlamadır."
---

## Definition

QLoRA, Düşük Ranklı Uyarlamayı (LoRA) 4-bit nicelleme ile birleştirerek devasa modelleri ince ayarlamak için gereken bellek kullanımını önemli ölçüde azaltır. Ağırlıkları 4-bit formatta saklayarak ve üçüncül adaptörler ekleyerek, yüksek bellek gereksinimini minimuma indirir.

### Summary

4-bit nicelleme ve düşük ranklı adaptörler kullanarak büyük dil modellerini verimli bir şekilde ince ayar yapmak için kullanılan Nicellenmiş Düşük Ranklı Uyarlamadır.

## Key Concepts

- Düşük Ranklı Uyarlama
- 4-Bit Nicelleme
- Bellek Verimliliği
- İnce Ayar

## Use Cases

- Tüketici GPU'ları ile İnce Ayar
- Kaynak Kısıtlı Ortamlar
- Hızlı Model Yinelmesi

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base_model, config)
```

## Related Terms

- [LoRA](/en/terms/lora/)
- [PEFT (Parametre Verimli İnce Ayar Tekniği)](/en/terms/peft-parametre-verimli-i-nce-ayar-tekniği/)
- [Nicelleme](/en/terms/nicelleme/)
- [Parametre Verimli İnce Ayar](/en/terms/parametre-verimli-i-nce-ayar/)
