---
title: "Egy-kivételes keresztvalidáció"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /hu/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:10:20.616951Z"
lastmod: "2026-07-18T17:15:09.802440Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Szigorú újramintavételi technika, ahol a modellt az összes mintán kívül egyen tanítják, és az egyetlen kihagyott mintán tesztelik, ezt minden adathoz pontra megismételve."
---

## Definition

Az egy-kivételes keresztvalidáció (LOOCV) a k-részes keresztvalidáció egy speci esete, ahol k megegyezik az adathalmazban lévő minták számával. Szinte torzítatlan becslést nyújt a modell teljesítményéről, mivel minden egyes adatpont egyszer szerepel validációs halmazként.

### Summary

Szigorú újramintavételi technika, ahol a modellt az összes mintán kívül egyen tanítják, és az egyetlen kihagyott mintán tesztelik, ezt minden adathoz pontra megismételve.

## Key Concepts

- Újramintavétel
- Modellértékelés
- Torzítás-variancia kereskedés
- Számítási költség

## Use Cases

- Modellek értékelése kis orvosi adathalmazokon
- Hipertparaméter-beállítás, amikor az adat szegényes
- Algoritmusok teljesítményének szigorú összehasonlítása

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-részes keresztvalidáció (k-fold cross-validation)](/en/terms/k-részes-keresztvalidáció-k-fold-cross-validation/)
- [adattöredékek felosztása tanító és teszt készletre (train_test_split)](/en/terms/adattöredékek-felosztása-tanító-és-teszt-készletre-train_test_split/)
- [bootstrap módszer (bootstrap)](/en/terms/bootstrap-módszer-bootstrap/)
- [keresztvalidációs pontszám (cross_validation_score)](/en/terms/keresztvalidációs-pontszám-cross_validation_score/)
