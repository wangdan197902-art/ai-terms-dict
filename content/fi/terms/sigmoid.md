---
title: "Sigmoidi"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:20:10.813770Z"
lastmod: "2026-07-18T17:15:09.459129Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Matemaattinen funktio, joka kuvaa minkä tahansa reaaliluvun arvoksi välille nolla ja yksi, muodostaen S-kirjaimen muotoisen käyrän."
---
## Definition

Sigmoidifunktio, määriteltynä σ(z) = 1 / (1 + e^-z), on laajalti käytetty koneoppimisessa todennäköisyyksien mallintamiseen. Se puristaa syötearvot välille (0, 1), mikä tekee siitä sopivan binääriluokitteluun.

### Summary

Matemaattinen funktio, joka kuvaa minkä tahansa reaaliluvun arvoksi välille nolla ja yksi, muodostaen S-kirjaimen muotoisen käyrän.

## Key Concepts

- Logistinen funktio
- Todennäköisyyksien kuvaaminen
- Häviävä gradientti
- Ei-lineaarisuus

## Use Cases

- Binääriluokittelun lähtöarvo
- Logistinen regressio
- Aktivaatio matalissa neuroverkoissa

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression (Logistinen regressio)](/en/terms/logistic-regression-logistinen-regressio/)
- [Activation Function (Aktivaatiofunktio)](/en/terms/activation-function-aktivaatiofunktio/)
