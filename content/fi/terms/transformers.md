---
title: "Transformers-kirjasto"
term_id: "transformers"
category: "training_techniques"
subcategory: ""
tags: ["library", "tools", "ecosystem"]
difficulty: 2
weight: 1
slug: "transformers"
date: "2026-07-18T15:32:15.090668Z"
lastmod: "2026-07-18T17:15:09.361885Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Tässä yhteydessä viittaa Hugging Facen Transformers-kirjastoon, suosittuun avoimen lähdekoodin työkalupakkiin huippuluokan luonnollisen kielen käsittelyn ja multimodaalisten mallien kehittämiseen."
---
## Definition

Termi 'Transformers' viittaa usein laajasti käytettyyn Python-kirjastoon, jota ylläpitää Hugging Face. Se tarjoaa helppokäyttöiset rajapinnat esikoulutettujen mallien lataamiseen, kouluttamiseen ja käyttöönottoon perustuen yhteisön tuottamaan infrastruktuuriin.

### Summary

Tässä yhteydessä viittaa Hugging Facen Transformers-kirjastoon, suosittuun avoimen lähdekoodin työkalupakkiin huippuluokan luonnollisen kielen käsittelyn ja multimodaalisten mallien kehittämiseen.

## Key Concepts

- Hugging Face Hub
- Putkisto-rajapinta (Pipeline API)
- Mallikortit (Model Cards)
- Tokenisoijan integrointi

## Use Cases

- Luonnollisen kielen sovellusten nopea prototyypitys
- Yhteisön esikouluttamien mallien hyödyntäminen
- Mallien käyttöönoton toimintatapojen standardointi

## Code Example

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
```

## Related Terms

- [hugging_face (Hugging Face -yhtiö/kirjasto)](/en/terms/hugging_face-hugging-face-yhtiö-kirjasto/)
- [pipeline (putkisto-rajapinta)](/en/terms/pipeline-putkisto-rajapinta/)
- [tokenizer (tekstin tokenisointityökalu)](/en/terms/tokenizer-tekstin-tokenisointityökalu/)
- [pytorch (syväoppimiskehyks)](/en/terms/pytorch-syväoppimiskehyks/)
