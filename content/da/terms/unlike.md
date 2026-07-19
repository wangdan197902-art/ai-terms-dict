---
title: "Ikke-lignende"
term_id: "unlike"
category: "basic_concepts"
subcategory: ""
tags: ["SQL", "Logic", "Filtering"]
difficulty: 2
weight: 1
slug: "unlike"
date: "2026-07-18T15:31:17.708963Z"
lastmod: "2026-07-18T17:15:09.236547Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En logisk operator, der bruges i SQL og programmering til at filtrere poster, der ikke matcher en angivet betingelse."
---
## Definition

I databasestyring og logik refererer 'Unlike' typisk til operatøren NOT LIKE, som udfører mønstergenkendelse omvendt. Den returnerer sand for rækker, hvor kolonneværdien ikke passer til den specificerede mønsterstruktur.

### Summary

En logisk operator, der bruges i SQL og programmering til at filtrere poster, der ikke matcher en angivet betingelse.

## Key Concepts

- Mønstergenkendelse
- Jokerteikener
- Negation
- SQL-filtering

## Use Cases

- Ekskludering af e-mailadresser fra specifikke domæner
- Filtrering af produktnavne, der indeholder bestemte nøgleord
- Datarensning ved at fjerne poster med ugyldigt format

## Code Example

```python
SELECT * FROM users WHERE email NOT LIKE '%@spam.com';
```

## Related Terms

- [LIKE (Ligner)](/en/terms/like-ligner/)
- [NOT IN (Ikke i)](/en/terms/not-in-ikke-i/)
- [EXCEPT (Undtagen)](/en/terms/except-undtagen/)
- [Wildcard (Jokertegn)](/en/terms/wildcard-jokertegn/)
