---
title: "Nem egyezik meg (NOT LIKE)"
term_id: "unlike"
category: "basic_concepts"
subcategory: ""
tags: ["SQL", "Logic", "Filtering"]
difficulty: 2
weight: 1
slug: "unlike"
date: "2026-07-18T15:33:52.822494Z"
lastmod: "2026-07-18T17:15:09.732975Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy logikai operátor, amelyet SQL-ben és programozásban használnak azoknak a rekordoknak a szűrésére, amelyek nem illeszkednek egy megadott feltételhez."
---
## Definition

Az adatbázis-lekérdezésekben és a logikában a 'Unlike' (nem egyezik meg) általában a NOT LIKE operátort jelöli, amely mintaillesztést végez fordított irányban. Igaz értéket ad vissza azoknál a soroknál, ahol az oszlop értéke nem felel meg a megadott mintának.

### Summary

Egy logikai operátor, amelyet SQL-ben és programozásban használnak azoknak a rekordoknak a szűrésére, amelyek nem illeszkednek egy megadott feltételhez.

## Key Concepts

- Mintaillesztés
- Helyettesítő karakterek
- Tagadás
- SQL szűrés

## Use Cases

- E-mail címek kizárása bizonyos tartományokból
- Terméknemek kiszűrése, amelyek tartalmaznak bizonyos kulcsszavakat
- Adattisztítás érvénytelen formátumú bejegyzések eltávolításával

## Code Example

```python
SELECT * FROM users WHERE email NOT LIKE '%@spam.com';
```

## Related Terms

- [LIKE (Illeszkedik)](/en/terms/like-illeszkedik/)
- [NOT IN (Nincs benne)](/en/terms/not-in-nincs-benne/)
- [EXCEPT (Kivéve)](/en/terms/except-kivéve/)
- [Wildcard (Helyettesítő karakter)](/en/terms/wildcard-helyettesítő-karakter/)
