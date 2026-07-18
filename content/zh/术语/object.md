---
title: "对象"
term_id: "object"
category: "basic_concepts"
subcategory: ""
tags: ["Programming", "OOP", "Software Engineering"]
difficulty: 2
weight: 1
slug: "object"
aliases:
  - /zh/terms/object/
date: "2026-07-18T10:53:26.248992Z"
lastmod: "2026-07-18T11:44:45.379619Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "程序中的一个独立实体，包含数据和操作该数据的方法，是面向对象编程的核心。"
---

## Definition

对象是计算机科学中的一个基本概念，特别是在面向对象编程（OOP）中。它代表类的一个实例，封装了状态（属性或数据）和行为

### Summary

程序中的一个独立实体，包含数据和操作该数据的方法，是面向对象编程的核心。

## Key Concepts

- 封装
- 类实例
- 属性
- 方法

## Use Cases

- 软件架构设计
- 在OpenCV中管理图像数据
- 结构化数据集条目

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

- [class (类)](/en/terms/class-类/)
- [oop (面向对象编程)](/en/terms/oop-面向对象编程/)
- [encapsulation (封装)](/en/terms/encapsulation-封装/)
- [instance (实例)](/en/terms/instance-实例/)
