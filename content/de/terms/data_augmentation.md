---
title: "Datenaugmentierung"
term_id: "data_augmentation"
category: "training_techniques"
subcategory: ""
tags: ["machine_learning", "preprocessing", "cv"]
difficulty: 2
weight: 1
slug: "data_augmentation"
aliases:
  - /de/terms/data_augmentation/
date: "2026-07-18T11:09:31.371385Z"
lastmod: "2026-07-18T11:44:44.923504Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Datenaugmentierung ist eine Technik zur Erhöhung der Vielfalt und Größe von Trainingsdatensätzen durch Anwendung von Transformationen auf vorhandene Datenpunkte."
---

## Definition

Diese Methode erweitert den Trainingsdatensatz künstlich, indem modifizierte Versionen bestehender Stichproben erstellt werden, wie z. B. das Drehen von Bildern, das Hinzufügen von Rauschen zu Audiodaten oder der Austausch von Synonymen im Text. Sie hilft, Überanpassung zu verhindern,

### Summary

Datenaugmentierung ist eine Technik zur Erhöhung der Vielfalt und Größe von Trainingsdatensätzen durch Anwendung von Transformationen auf vorhandene Datenpunkte.

## Key Concepts

- Verhinderung von Überanpassung
- Erweiterung des Datensatzes
- Generalisierung
- Transformationen

## Use Cases

- Verbesserung der Robustheit von Computer-Vision-Modellen
- Steigerung der Leistung von NLP-Modellen bei begrenzten Textdaten
- Ausgewichtung unausgeglichener Datensätze

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularisierung (Regularization)](/en/terms/regularisierung-regularization/)
- [Synthetische Daten (Synthetic Data)](/en/terms/synthetische-daten-synthetic-data/)
- [Transferlernen (Transfer Learning)](/en/terms/transferlernen-transfer-learning/)
- [Überanpassung (Overfitting)](/en/terms/überanpassung-overfitting/)
