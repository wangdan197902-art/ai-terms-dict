---
title: "Vista"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /es/terms/view/
date: "2026-07-18T10:27:37.326796Z"
lastmod: "2026-07-18T11:44:44.754586Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una tabla virtual en una base de datos resultante de una consulta almacenada, que presenta datos de una o más tablas sin almacenarlos físicamente."
---

## Definition

En la gestión de bases de datos, una vista actúa como una consulta SQL guardada que se comporta como una tabla pero no contiene datos propios. Proporciona una perspectiva simplificada o personalizada de los datos subyacentes, mejorando la seguridad y la abstracción.

### Summary

Una tabla virtual en una base de datos resultante de una consulta almacenada, que presenta datos de una o más tablas sin almacenarlos físicamente.

## Key Concepts

- Tabla virtual
- Consulta SQL
- Abstracción de datos
- Seguridad

## Use Cases

- Crear informes simplificados para usuarios no técnicos
- Restringir el acceso a columnas sensibles en una tabla
- Estandarizar la lógica de uniones complejas entre aplicaciones

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (Tabla)](/en/terms/table-tabla/)
- [Query (Consulta)](/en/terms/query-consulta/)
- [Schema (Esquema)](/en/terms/schema-esquema/)
- [Materialized View (Vista materializada)](/en/terms/materialized-view-vista-materializada/)
