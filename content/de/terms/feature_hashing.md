---
title: "Feature Hashing"
term_id: "feature_hashing"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "text-mining", "optimization"]
difficulty: 3
weight: 1
slug: "feature_hashing"
aliases:
  - /de/terms/feature_hashing/
date: "2026-07-18T11:14:30.485294Z"
lastmod: "2026-07-18T11:44:44.940030Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Technik, die hochdimensionale, spärliche Merkmale mit einer Hash-Funktion auf einen Vektor fester Größe abbildet."
---

## Definition

Feature Hashing, auch als Hashing-Trick bekannt, ermöglicht es Machine-Learning-Modellen, große, spärliche Merkmalsräume zu verarbeiten, ohne eine explizite Zuordnung zwischen Merkmalen und Indizes aufrechterhalten zu müssen. Durch die Anwendung einer Hash-Funktion wird die Dimensionalität reduziert, was den Speicherbedarf erheblich verringert und die Effizienz bei der Verarbeitung großer Datenmengen steigert.

### Summary

Eine Technik, die hochdimensionale, spärliche Merkmale mit einer Hash-Funktion auf einen Vektor fester Größe abbildet.

## Key Concepts

- Hash-Funktion
- Spärliche Vektoren
- Dimensionsreduktion
- Speichereffizienz

## Use Cases

- Textklassifizierung mit großen Vokabularen
- Empfehlungssysteme mit riesigen Artikelgruppen
- Echtzeit-Verarbeitung von Streaming-Daten

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-Hot-Encoding (Binäre Kodierung einzelner Kategorien)](/en/terms/one-hot-encoding-binäre-kodierung-einzelner-kategorien/)
- [Bag of Words (Wortbeutel-Modell)](/en/terms/bag-of-words-wortbeutel-modell/)
- [Dimensionsreduktion (Reduzierung der Merkmalsanzahl)](/en/terms/dimensionsreduktion-reduzierung-der-merkmalsanzahl/)
- [Spärliche Matrix (Matrix mit überwiegend Nullen)](/en/terms/spärliche-matrix-matrix-mit-überwiegend-nullen/)
