---
title: "View"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
date: "2026-07-18T10:54:59.289492Z"
lastmod: "2026-07-18T11:44:44.886892Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine virtuelle Tabelle in einer Datenbank, die aus einer gespeicherten Abfrage resultiert und Daten aus einer oder mehreren Tabellen darstellt, ohne sie physikalisch zu speichern."
---
## Definition

Im Datenbankmanagement fungiert eine View als gespeicherte SQL-Abfrage, die sich wie eine Tabelle verhält, aber keine Daten selbst enthält. Sie bietet eine vereinfachte oder angepasste Perspektive auf die zugrunde liegenden Daten und erhöht die Sicherheit.

### Summary

Eine virtuelle Tabelle in einer Datenbank, die aus einer gespeicherten Abfrage resultiert und Daten aus einer oder mehreren Tabellen darstellt, ohne sie physikalisch zu speichern.

## Key Concepts

- Virtuelle Tabelle
- SQL-Abfrage
- Datenabstraktion
- Sicherheit

## Use Cases

- Erstellung vereinfachter Berichte für nichttechnische Benutzer
- Einschränkung des Zugriffs auf sensible Spalten in einer Tabelle
- Standardisierung komplexer Join-Logik über Anwendungen hinweg

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Tabelle](/en/terms/tabelle/)
- [Abfrage](/en/terms/abfrage/)
- [Schema](/en/terms/schema/)
- [Materialized View (Materialisierte Sicht)](/en/terms/materialized-view-materialisierte-sicht/)
