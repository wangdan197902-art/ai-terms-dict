---
title: تقييم المصنفات الثنائية
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T15:57:09.174166Z'
lastmod: '2026-07-18T17:15:08.502191Z'
draft: false
source: agnes_llm
status: published
language: ar
description: عملية تقييم أداء نماذج تعلم الآلة التي تتنبأ بأحد النتيجتين المحتملتين.
---
## Definition

يتضمن هذا المجال تحليل مقاييس مثل الدقة، والدقة الإيجابية، والاسترجاع، ودرجة F1، ومنطقة تحت منحنى التشغيل الخاص بالمستقبل (AUC-ROC). يساعد ذلك في تحديد مدى جودة قدرة النموذج على التمييز بين الفئتين.

### Summary

عملية تقييم أداء نماذج تعلم الآلة التي تتنبأ بأحد النتيجتين المحتملتين.

## Key Concepts

- مصفوفة الارتباك
- المفاضلة بين الدقة والاسترجاع
- منحنى ROC
- درجة F1

## Use Cases

- فحص الأمراض الطبية
- تصفية البريد العشوائي
- تقييم مخاطر الائتمان

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (مصفوفة الارتباك)](/en/terms/confusion_matrix-مصفوفة-الارتباك/)
- [roc_auc (منطقة تحت منحنى ROC)](/en/terms/roc_auc-منطقة-تحت-منحنى-roc/)
- [precision_recall (الدقة والاسترجاع)](/en/terms/precision_recall-الدقة-والاسترجاع/)
- [cross_validation (التحقق المتبادل)](/en/terms/cross_validation-التحقق-المتبادل/)
