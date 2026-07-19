---
title: "הסבריות (Explainability)"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
date: "2026-07-18T15:36:22.156421Z"
lastmod: "2026-07-18T17:15:09.499039Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "הסבריות מתייחסת למידה שבה אדם יכול להבין את הגורם להחלטה שהתקבלה על ידי מודל בינה מלאכותית."
---
## Definition

מושג זה מטפל בבעיית 'הקופסה השחורה' במערכות AI מורכבות על ידי מתן תובנות כיצד מודלים מגיעים לתחזיות ספציפיות. טכניקות כמו SHAP או LIME עוזרות לנרמל חשיבות תכונות.

### Summary

הסבריות מתייחסת למידה שבה אדם יכול להבין את הגורם להחלטה שהתקבלה על ידי מודל בינה מלאכותית.

## Key Concepts

- פרשנות (Interpretability)
- בעיית הקופסה השחורה (Black Box Problem)
- אמון (Trust)
- זיהוי הטיה (Bias Detection)

## Use Cases

- ביקורת על אלגוריתמים לאישור הלוואות לשקיפות והוגנות
- אבחון מודלי הדמיה רפואית עבור קלינאים
- עמידה ברגולציה בהערכת סיכונים פיננסיים

## Code Example

```python
import shap
import numpy as np

# Assuming model is a trained scikit-learn model
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## Related Terms

- [SHAP (שיטת שווי שחקן)](/en/terms/shap-שיטת-שווי-שחקן/)
- [LIME (הסברים ניתנים להבנה)](/en/terms/lime-הסברים-ניתנים-להבנה/)
- [AI Ethics (אתיקה של בינה מלאכותית)](/en/terms/ai-ethics-אתיקה-של-בינה-מלאכותית/)
- [Transparency (שקיפות)](/en/terms/transparency-שקיפות/)
