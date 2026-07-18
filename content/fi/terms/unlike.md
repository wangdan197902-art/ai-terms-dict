---
title: "Ei kuten"
term_id: "unlike"
category: "basic_concepts"
subcategory: ""
tags: ["SQL", "Logic", "Filtering"]
difficulty: 2
weight: 1
slug: "unlike"
aliases:
  - /fi/terms/unlike/
date: "2026-07-18T15:32:56.079302Z"
lastmod: "2026-07-18T17:15:09.362222Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Logiikkaoperaattori, jota käytetään SQL:ssä ja ohjelmoinnissa suodattamaan ne tietueet, jotka eivät täytä määritettyä ehtoa."
---

## Definition

Tietokantahakuissa ja logiikassa 'Ei kuten' viittaa yleensä operaattoriin NOT LIKE, joka suorittaa vastakkaisen kuvion etsinnän. Se palauttaa totuuden arvon niille riveille, joiden sarakkeen arvo ei vastaa annettua kuvioita.

### Summary

Logiikkaoperaattori, jota käytetään SQL:ssä ja ohjelmoinnissa suodattamaan ne tietueet, jotka eivät täytä määritettyä ehtoa.

## Key Concepts

- Kuvion etsintä
- Villikorttimerkit
- Negaatio
- SQL-suodatus

## Use Cases

- Sähköpostiosoitteiden poissulkeminen tietyiltä verkkotunnuksilta
- Tuotenimien suodattaminen pois, jos ne sisältävät tiettyjä avainsanoja
- Datan siivous poistamalla virheellisen muotoiset merkinnät

## Code Example

```python
SELECT * FROM users WHERE email NOT LIKE '%@spam.com';
```

## Related Terms

- [LIKE (Kuten)](/en/terms/like-kuten/)
- [NOT IN (Ei sisällä)](/en/terms/not-in-ei-sisällä/)
- [EXCEPT (Poislukeminen)](/en/terms/except-poislukeminen/)
- [Wildcard (Villikorttimerkki)](/en/terms/wildcard-villikorttimerkki/)
