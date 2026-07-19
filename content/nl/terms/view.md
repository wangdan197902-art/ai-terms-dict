---
title: "Weergave"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
date: "2026-07-18T15:31:07.724760Z"
lastmod: "2026-07-18T17:15:08.696589Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een virtuele tabel in een database die voortkomt uit een opgeslagen query, die gegevens uit één of meer tabellen presenteert zonder ze fysiek op te slaan."
---
## Definition

In databasebeheer fungeert een weergave als een opgeslagen SQL-query die zich gedraagt als een tabel, maar geen gegevens zelf bevat. Het biedt een vereenvoudigd of aangepast perspectief op onderliggende gegevens, wat de beveiliging verbetert.

### Summary

Een virtuele tabel in een database die voortkomt uit een opgeslagen query, die gegevens uit één of meer tabellen presenteert zonder ze fysiek op te slaan.

## Key Concepts

- Virtuele tabel
- SQL-query
- Gegevensabstractie
- Beveiliging

## Use Cases

- Het maken van vereenvoudigde rapporten voor niet-technische gebruikers
- Het beperken van de toegang tot gevoelige kolommen in een tabel
- Het standaardiseren van complexe join-logica over applicaties heen

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Tabel](/en/terms/tabel/)
- [Query](/en/terms/query/)
- [Schema](/en/terms/schema/)
- [Gematerialiseerde weergave](/en/terms/gematerialiseerde-weergave/)
