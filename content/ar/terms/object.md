---
title: "كائن"
term_id: "object"
category: "basic_concepts"
subcategory: ""
tags: ["Programming", "OOP", "Software Engineering"]
difficulty: 2
weight: 1
slug: "object"
date: "2026-07-18T15:28:58.920554Z"
lastmod: "2026-07-18T17:15:08.444328Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "كيان متميز داخل البرنامج يحتوي على بيانات وطرق للتعامل مع تلك البيانات، وهو محوري في البرمجة كائنية التوجه."
---
## Definition

الكائن هو مفهوم أساسي في علوم الكمبيوتر، خاصة في البرمجة كائنية التوجه (OOP). فهو يمثل مثيلًا لفئة ما، ويجمع بين الحالة (السمات أو البيانات) والسلوك (الطرق) في وحدة واحدة.

### Summary

كيان متميز داخل البرنامج يحتوي على بيانات وطرق للتعامل مع تلك البيانات، وهو محوري في البرمجة كائنية التوجه.

## Key Concepts

- التغليف (Encapsulation)
- مثيل الفئة (Class Instance)
- السمات (Attributes)
- الطرق (Methods)

## Use Cases

- تصميم هندسة البرمجيات
- إدارة بيانات الصور في مكتبة OpenCV
- هيكلة إدخالات مجموعات البيانات

## Code Example

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says woof!"
my_dog = Dog('Buddy')
print(my_dog.bark())
```

## Related Terms

- [class (فئة)](/en/terms/class-فئة/)
- [oop (البرمجة كائنية التوجه)](/en/terms/oop-البرمجة-كائنية-التوجه/)
- [encapsulation (التغليف)](/en/terms/encapsulation-التغليف/)
- [instance (مثيل)](/en/terms/instance-مثيل/)
