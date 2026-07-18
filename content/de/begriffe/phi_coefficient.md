---
title: "Phi-Koeffizient"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /de/terms/phi_coefficient/
date: "2026-07-18T11:27:47.612348Z"
lastmod: "2026-07-18T11:44:44.975345Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein statistisches Maß für den Zusammenhang zwischen zwei binären Variablen."
---

## Definition

Der Phi-Koeffizient (φ) ist ein Maß für den Zusammenhang zwischen zwei binären Variablen und dient als Pearson-Korrelationskoeffizient für dichotome Variablen. Er reicht von -1 bis +1, wobei 0 keinen Zusammenhang anzeigt.

### Summary

Ein statistisches Maß für den Zusammenhang zwischen zwei binären Variablen.

## Key Concepts

- Binäre Variablen
- Korrelation
- Kontingenztabelle
- Assoziationsstärke

## Use Cases

- Bewertung der Leistung eines binären Klassifizierers über die Genauigkeit hinaus
- Analyse von Zusammenhängen in Umfragedaten mit Ja/Nein-Antworten
- Merkmalsauswahl in Datensätzen mit kategorialen Eingaben

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramers V (Maß für den Zusammenhang zwischen zwei nominalen Variablen)](/en/terms/cramers-v-maß-für-den-zusammenhang-zwischen-zwei-nominalen-variablen/)
- [Pearson-Korrelation (Maß für den linearen Zusammenhang)](/en/terms/pearson-korrelation-maß-für-den-linearen-zusammenhang/)
- [Konfusionsmatrix (Tabelle zur Beschreibung der Leistung eines Klassifikators)](/en/terms/konfusionsmatrix-tabelle-zur-beschreibung-der-leistung-eines-klassifikators/)
- [Gegenseitige Information (Maß für die Abhängigkeit zwischen Zufallsvariablen)](/en/terms/gegenseitige-information-maß-für-die-abhängigkeit-zwischen-zufallsvariablen/)
