---
title: "Verborgen laag"
term_id: "hidden_layer"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture", "deep_learning"]
difficulty: 3
weight: 1
slug: "hidden_layer"
aliases:
  - /nl/terms/hidden_layer/
date: "2026-07-18T15:58:35.202666Z"
lastmod: "2026-07-18T17:15:08.751768Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een tussenliggende laag in een neurale netwerk tussen de invoer- en uitvoerlagen die kenmerken verwerkt."
---

## Definition

Een verborgen laag bestaat uit neuronen die invoer ontvangen van vorige lagen, gewichten en bias toepassen en getransformeerde gegevens doorgeven via een activatiefunctie. Deze lagen stellen neurale netwerken in staat complexe patronen en niet-lineaire relaties te leren.

### Summary

Een tussenliggende laag in een neurale netwerk tussen de invoer- en uitvoerlagen die kenmerken verwerkt.

## Key Concepts

- Neurale netwerken
- Kenmerkextractie
- Activatiefuncties
- Diep leren

## Use Cases

- Systeem voor beeldherkenning
- Modellen voor natuurlijke taalverwerking
- Predictieve analyses

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neurone (basiseenheid van een neuraal netwerk)](/en/terms/neurone-basiseenheid-van-een-neuraal-netwerk/)
- [backpropagatie (algoritme voor training)](/en/terms/backpropagatie-algoritme-voor-training/)
- [activatiefunctie (functie die signaal doorgeeft)](/en/terms/activatiefunctie-functie-die-signaal-doorgeeft/)
- [diep leren (subveld van machine learning met veel lagen)](/en/terms/diep-leren-subveld-van-machine-learning-met-veel-lagen/)
