---
title: "Datenexploration"
term_id: "data_exploration"
category: "training_techniques"
subcategory: ""
tags: ["analysis", "preprocessing", "visualization"]
difficulty: 2
weight: 1
slug: "data_exploration"
date: "2026-07-18T11:09:40.573220Z"
lastmod: "2026-07-18T11:44:44.923969Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Die initiale Analyse von Datensätzen, um Muster zu entdecken, Anomalien zu erkennen und Hypothesen vor der formalen Modellierung zu testen."
---
## Definition

Die Datenexploration, oft auch als Explorative Datenanalyse (EDA) bezeichnet, ist ein kritischer vorbereitender Schritt in Machine-Learning-Workflows. Sie umfasst die Zusammenfassung der Hauptmerkmale der Daten, häufig unter Verwendung statistischer Kennzahlen und visueller Darstellungen, um Einblicke in die Struktur und Qualität der Daten zu gewinnen.

### Summary

Die initiale Analyse von Datensätzen, um Muster zu entdecken, Anomalien zu erkennen und Hypothesen vor der formalen Modellierung zu testen.

## Key Concepts

- Explorative Datenanalyse
- Visualisierung
- Mustererkennung
- Anomalieerkennung

## Use Cases

- Identifizieren von Korrelationen zwischen Merkmalen vor dem Modelltraining
- Erkennen und Behandeln fehlender Werte oder Ausreißer
- Validieren von Datenqualität und Verteilungsannahmen

## Code Example

```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('data.csv')
sns.pairplot(df)
plt.show()
```

## Related Terms

- [feature_engineering (Merkmalsentwicklung)](/en/terms/feature_engineering-merkmalsentwicklung/)
- [data_cleaning (Datenbereinigung)](/en/terms/data_cleaning-datenbereinigung/)
- [EDA (Explorative Datenanalyse)](/en/terms/eda-explorative-datenanalyse/)
- [statistical_analysis (Statistische Analyse)](/en/terms/statistical_analysis-statistische-analyse/)
