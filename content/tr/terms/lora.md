---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:23.723866Z"
lastmod: "2026-07-18T16:38:07.236340Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Düşük Sıralı Uyarlanım, mevcut model ağırlıklarına eğitilebilir düşük sıralı ayrışım matrisleri enjekte eden, parametre verimliliğine odaklanan ince ayar yöntemidir."
---
## Definition

LoRA, önceden eğitilmiş model ağırlıklarını dondurur ve Dönüştürücü mimarisinin her katmanına eğitilebilir ayrışım matrisleri ekler. Yalnızca bu düşük sıralı matrislerin optimize edilmesiyle LoRA, önemli ölçüde azaltır

### Summary

Düşük Sıralı Uyarlanım, mevcut model ağırlıklarına eğitilebilir düşük sıralı ayrışım matrisleri enjekte eden, parametre verimliliğine odaklanan ince ayar yöntemidir.

## Key Concepts

- Parametre Verimli İnce Ayar
- Sıralı Ayrışım
- Ağırlıkları Dondurma
- Adaptör Modülleri

## Use Cases

- LLM'leri Özelleştirme
- Alana Özgü Uyarlanım
- Kaynak Kısıtlı Eğitim

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT](/en/terms/peft/)
- [İnce Ayar](/en/terms/i-nce-ayar/)
- [Nicelleştirme (Quantization)](/en/terms/nicelleştirme-quantization/)
