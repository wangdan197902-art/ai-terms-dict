---
title: "לא דומה (Not Like)"
term_id: "unlike"
category: "basic_concepts"
subcategory: ""
tags: ["SQL", "Logic", "Filtering"]
difficulty: 2
weight: 1
slug: "unlike"
date: "2026-07-18T15:31:58.343245Z"
lastmod: "2026-07-18T17:15:09.490462Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "אופרטור לוגי המשמש ב-SQL ובתכנות כדי לסנן רשומות שאינן תואמות לתנאי מסוים."
---
## Definition

בשאילתות מסדי נתונים ולוגיקה, המונח 'לא דומה' מתייחס בדרך כלל לאופרטור NOT LIKE, המבצע התאמת תבניות הפוכה. הוא מחזיר ערך אמת עבור שורות בהן עמודה אינה מתאימה לתבנית שצוינה.

### Summary

אופרטור לוגי המשמש ב-SQL ובתכנות כדי לסנן רשומות שאינן תואמות לתנאי מסוים.

## Key Concepts

- התאמת תבניות
- תווים כלליים (Wildcards)
- שלילה
- סינון SQL

## Use Cases

- החרגת כתובות אימייל מדומיינים ספציפיים
- סינון שמות מוצרים הכוללים מילות מפתח מסוימות
- ניקוי נתונים על ידי הסרת רשומות בעלות פורמט לא תקין

## Code Example

```python
SELECT * FROM users WHERE email NOT LIKE '%@spam.com';
```

## Related Terms

- [LIKE (דומה - התאמת תבניות חיובית)](/en/terms/like-דומה-התאמת-תבניות-חיובית/)
- [NOT IN (לא בקבוצה - סינון ערכים ספציפיים)](/en/terms/not-in-לא-בקבוצה-סינון-ערכים-ספציפיים/)
- [EXCEPT (הפרש - השוואת קבוצות נתונים)](/en/terms/except-הפרש-השוואת-קבוצות-נתונים/)
- [Wildcard (תו כללי - תו המייצג אחד או יותר תווים אחרים)](/en/terms/wildcard-תו-כללי-תו-המייצג-אחד-או-יותר-תווים-אחרים/)
