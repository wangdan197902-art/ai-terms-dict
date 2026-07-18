---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /hu/terms/relu/
date: "2026-07-18T15:39:25.490757Z"
lastmod: "2026-07-18T17:15:09.744274Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A Rectified Linear Unit (ReLU) egy aktivációs függvény, amely pozitív bemenet esetén közvetlenül visszaadja azt, ellenkező esetben nullát ad ki."
---

## Definition

A ReLU széles körben használt a mélytanuló neurális hálózatokban számítási hatékonysága és a „szűnő gradiens” (vanishing gradient) probléma enyhítése miatt. Matematikailag az f(x) = max(0, x) képlettel definiálják, így nemlineáris tulajdonságokat vezet be a hálózatba.

### Summary

A Rectified Linear Unit (ReLU) egy aktivációs függvény, amely pozitív bemenet esetén közvetlenül visszaadja azt, ellenkező esetben nullát ad ki.

## Key Concepts

- Nemlinearitás
- Aktivációs függvény
- Szűnő gradiens
- Darabonként lineáris

## Use Cases

- Rejtett rétegek konvolúciós neurális hálózatokban (CNN)
- Mély előrefelé irányuló hálózatok
- Képfelismerő modellek

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (aktivációs függvény)](/en/terms/sigmoid-aktivációs-függvény/)
- [Tanh (aktivációs függvény)](/en/terms/tanh-aktivációs-függvény/)
- [Leaky ReLU (variáns)](/en/terms/leaky-relu-variáns/)
- [Neurális hálózat](/en/terms/neurális-hálózat/)
