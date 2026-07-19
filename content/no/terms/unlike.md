---
title: "ULIKE"
term_id: "unlike"
category: "basic_concepts"
subcategory: ""
tags: ["SQL", "Logic", "Filtering"]
difficulty: 2
weight: 1
slug: "unlike"
date: "2026-07-18T15:31:59.387115Z"
lastmod: "2026-07-18T16:38:06.949927Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En logisk operator brukt i SQL og programmering for å filtrere poster som ikke samsvarer med en spesifisert betingelse."
---
## Definition

I databasespørringer og logikk refererer 'ULIKE' typisk til operatoren NOT LIKE, som utfører mønstergjenkjenning omvendt. Den returnerer sant for rader der kolonneverdien ikke passer inn i det spesifiserte mønsteret.

### Summary

En logisk operator brukt i SQL og programmering for å filtrere poster som ikke samsvarer med en spesifisert betingelse.

## Key Concepts

- Mønstergjenkjenning
- Wildcardsymboler
- Negasjon
- SQL-filtering

## Use Cases

- Ekskludering av e-postadresser fra spesifikke domener
- Filtrering ut av produktnavner som inneholder bestemte nøkkelord
- Datarensing ved å fjerne oppføringer med ugyldig format

## Code Example

```python
SELECT * FROM users WHERE email NOT LIKE '%@spam.com';
```

## Related Terms

- [LIKE (Ligner på)](/en/terms/like-ligner-på/)
- [NOT IN (Ikke i)](/en/terms/not-in-ikke-i/)
- [EXCEPT (Unntak)](/en/terms/except-unntak/)
- [Wildcard (Wildcardsymbol)](/en/terms/wildcard-wildcardsymbol/)
