---
title: "Johtopäätösten tekeminen (Inferenssi)"
term_id: "inference"
category: "engineering_practice"
subcategory: ""
tags: ["Deployment", "Production", "Performance"]
difficulty: 2
weight: 1
slug: "inference"
date: "2026-07-18T15:22:52.575556Z"
lastmod: "2026-07-18T17:15:09.345306Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Vaihe, jossa koulutettu malli käsittelee uutta dataa tuottaakseen ennusteita tai tuloksia."
---
## Definition

Inferenssi viittaa käyttöönottovaiheeseen, jossa valmis mallia käytetään tekemään päätelmiä tai ennusteita näkemättömälle datalle. Toisin kuin koulutus, joka päivittää painoarvoja, inferenssi kuluttaa laskentaresursseja tulosten tuottamiseen.

### Summary

Vaihe, jossa koulutettu malli käsittelee uutta dataa tuottaakseen ennusteita tai tuloksia.

## Key Concepts

- Ennuste
- Viive (Latency)
- Läpäisykyky (Throughput)
- Käyttöönotto

## Use Cases

- Reaaliaikainen petosten tunnistaminen pankkitapahtumissa
- Vastauksien generointi elävissä chatbot-keskusteluissa
- Kuvien luokittelu autonomisissa ajoneuvojärjestelmissä

## Code Example

```python
import torch
model.eval()
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1)
```

## Related Terms

- [Koulutus](/en/terms/koulutus/)
- [Viiveen optimointi](/en/terms/viiveen-optimointi/)
- [Paketointi (Batching)](/en/terms/paketointi-batching/)
- [Mallin tarjoaminen (Model Serving)](/en/terms/mallin-tarjoaminen-model-serving/)
