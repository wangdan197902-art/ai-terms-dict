---
title: "Scurgere de date"
term_id: "leakage"
category: "basic_concepts"
subcategory: ""
tags: ["data-integrity", "evaluation", "best-practices"]
difficulty: 3
weight: 1
slug: "leakage"
aliases:
  - /ro/terms/leakage/
date: "2026-07-18T16:08:04.656562Z"
lastmod: "2026-07-18T17:15:09.673691Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Scurgerea de date apare atunci când informații din afara setului de antrenare influențează inadvertent modelul, ducând la estimări excesiv optimiste ale performanței."
---

## Definition

Scurgerea de date este o eroare critică în învățarea automată în care modelul accesează informații în timpul antrenamentului care nu ar fi disponibile în momentul predicției. Acest lucru se întâmplă adesea prin manipularea incorectă a datelor sau prin expunerea accidentală a variabilelor viitoare sau a informațiilor din setul de testare în timpul procesului de pregătire a datelor.

### Summary

Scurgerea de date apare atunci când informații din afara setului de antrenare influențează inadvertent modelul, ducând la estimări excesiv optimiste ale performanței.

## Key Concepts

- Scurgere țintă
- Contaminarea antrenament-test
- Separarea corectă a datelor

## Use Cases

- Depanarea suprapotrivirii modelului
- Validarea fluxurilor de lucru pentru ingineria caracteristicilor
- Asigurarea unei evaluări robuste a modelului

## Related Terms

- [Suprapotrivire (Overfitting)](/en/terms/suprapotrivire-overfitting/)
- [Valid încrucișată (Cross-validation)](/en/terms/valid-încrucișată-cross-validation/)
- [Ingineria caracteristicilor (Feature engineering)](/en/terms/ingineria-caracteristicilor-feature-engineering/)
