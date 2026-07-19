---
title: "Objek"
term_id: "object"
category: "basic_concepts"
subcategory: ""
tags: ["Programming", "OOP", "Software Engineering"]
difficulty: 2
weight: 1
slug: "object"
date: "2026-07-18T15:27:51.902538Z"
lastmod: "2026-07-18T16:38:07.398571Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Entitas terpisah dalam program yang berisi data dan metode untuk memanipulasi data tersebut, yang menjadi pusat pemrograman berorientasi objek."
---
## Definition

Objek adalah konsep dasar dalam ilmu komputer, khususnya dalam pemrograman berorientasi objek (OOP). Objek mewakili instans dari sebuah kelas, yang mengenkapsulasi baik keadaan (atribut atau data) maupun perilaku (metode) dari entitas tersebut.

### Summary

Entitas terpisah dalam program yang berisi data dan metode untuk memanipulasi data tersebut, yang menjadi pusat pemrograman berorientasi objek.

## Key Concepts

- Enkapsulasi
- Instans Kelas
- Atribut
- Metode

## Use Cases

- Desain arsitektur perangkat lunak
- Mengelola data gambar di OpenCV
- Menyusun entri dataset

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

- [class (Kelas)](/en/terms/class-kelas/)
- [oop (Pemrograman Berorientasi Objek)](/en/terms/oop-pemrograman-berorientasi-objek/)
- [encapsulation (Enkapsulasi)](/en/terms/encapsulation-enkapsulasi/)
- [instance (Instans)](/en/terms/instance-instans/)
