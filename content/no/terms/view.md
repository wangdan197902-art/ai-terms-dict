---
title: "Visning"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
date: "2026-07-18T15:31:59.387206Z"
lastmod: "2026-07-18T16:38:06.950417Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Et virtuelt bord i en database som er resultatet av en lagret spørring, som presenterer data fra ett eller flere bord uten å lagre dem fysisk."
---
## Definition

I databaseadministrasjon fungerer en visning som en lagret SQL-spørring som oppfører seg som et bord, men ikke inneholder data selv. Den gir en forenklet eller tilpasset visning av underliggende data, noe som forbedrer sikkerheten.

### Summary

Et virtuelt bord i en database som er resultatet av en lagret spørring, som presenterer data fra ett eller flere bord uten å lagre dem fysisk.

## Key Concepts

- Virtuelt bord
- SQL-spørring
- Dataabstraksjon
- Sikkerhet

## Use Cases

- Opprettelse av forenklede rapporter for ikke-tekniske brukere
- Begrensning av tilgang til sensitive kolonner i et bord
- Standardisering av kompleks join-logikk på tvers av applikasjoner

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (Bord)](/en/terms/table-bord/)
- [Query (Spørring)](/en/terms/query-spørring/)
- [Schema (Skjema)](/en/terms/schema-skjema/)
- [Materialized View (Materialisert visning)](/en/terms/materialized-view-materialisert-visning/)
