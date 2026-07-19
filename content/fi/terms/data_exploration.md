---
title: "Datankartoitus"
term_id: "data_exploration"
category: "training_techniques"
subcategory: ""
tags: ["analysis", "preprocessing", "visualization"]
difficulty: 2
weight: 1
slug: "data_exploration"
date: "2026-07-18T15:51:01.333331Z"
lastmod: "2026-07-18T17:15:09.397051Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Alkuperäinen analyysi tietojoukoista kuvioiden löytämiseksi, poikkeavuuksien havaitsemiseksi ja hypoteesien testaamiseksi ennen virallista mallintamista."
---
## Definition

Datankartoitus, jota kutsutaan usein myös eksploratiiviseksi data-analyysiksi (EDA), on kriittinen alustava vaihe koneoppimisessa. Se sisältää datan pääominaisuuksien tiivistämisen, usein käyttäen visualisointia ja tilastollisia menetelmiä ymmärtääkseen datan rakennetta ja laatua ennen mallin kehitystä.

### Summary

Alkuperäinen analyysi tietojoukoista kuvioiden löytämiseksi, poikkeavuuksien havaitsemiseksi ja hypoteesien testaamiseksi ennen virallista mallintamista.

## Key Concepts

- Eksploratiivinen data-analyysi
- Visualisointi
- Kuviontunnistus
- Poikkeavuuden havaitseminen

## Use Cases

- Ominaisuuksien välisten korrelaatioiden tunnistaminen ennen mallin koulutusta
- Puuttuvien arvojen tai ääriarvojen havaitseminen ja käsittely
- Datalaadun ja jakauma-oletusten validointi

## Code Example

```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('data.csv')
sns.pairplot(df)
plt.show()
```

## Related Terms

- [feature_engineering (ominaisuuksien muotoilu)](/en/terms/feature_engineering-ominaisuuksien-muotoilu/)
- [data_cleaning (datan siivous)](/en/terms/data_cleaning-datan-siivous/)
- [EDA (eksploratiivinen data-analyysi)](/en/terms/eda-eksploratiivinen-data-analyysi/)
- [statistical_analysis (tilastollinen analyysi)](/en/terms/statistical_analysis-tilastollinen-analyysi/)
