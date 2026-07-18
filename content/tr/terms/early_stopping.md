---
title: "Erken Durdurma"
term_id: "early_stopping"
category: "training_techniques"
subcategory: ""
tags: ["regularization", "training", "optimization"]
difficulty: 2
weight: 1
slug: "early_stopping"
aliases:
  - /tr/terms/early_stopping/
date: "2026-07-18T15:50:59.946014Z"
lastmod: "2026-07-18T16:38:07.303043Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Erken durdurma, modelin doğrulama setindeki performansı bozulmaya başladığında eğitim sürecini durduran, aşırı öğrenmeyi önleyen bir düzenlileştirme (regularization) tekniğidir."
---

## Definition

Erken durdurma, gradyan inişi gibi iteratif eğitim süreçlerinde kullanılan bir düzenlileştirme biçimidir. Eğitim sırasında modelin eğitim verisindeki performansı sürekli iyileşse bile, doğrulama verisindeki hata artmaya başladığında eğitim durdurularak modelin genelleme yeteneği korunur.

### Summary

Erken durdurma, modelin doğrulama setindeki performansı bozulmaya başladığında eğitim sürecini durduran, aşırı öğrenmeyi önleyen bir düzenlileştirme (regularization) tekniğidir.

## Key Concepts

- Düzenlileştirme
- Doğrulama Seti
- Aşırı Öğrenmenin Önlenmesi
- Sabır Parametresi

## Use Cases

- Sinir ağları eğitimi
- Gradyan yükseltme algoritmaları
- Zaman serisi tahmin modelleri

## Related Terms

- [L2 Düzenlileştirme (Ağırlık çökmesi olarak da bilinir, parametre büyüklüğünü kısıtlar)](/en/terms/l2-düzenlileştirme-ağırlık-çökmesi-olarak-da-bilinir-parametre-büyüklüğünü-kısıtlar/)
- [Dropout (Rastgele nöronları devre dışı bırakarak aşırı öğrenmeyi önleyen teknik)](/en/terms/dropout-rastgele-nöronları-devre-dışı-bırakarak-aşırı-öğrenmeyi-önleyen-teknik/)
- [Çapraz Doğrulama (Model performansını değerlendirmek için veri bölme yöntemi)](/en/terms/çapraz-doğrulama-model-performansını-değerlendirmek-için-veri-bölme-yöntemi/)
- [Genelleştirme Hatası (Modelin görmediği verilerdeki tahmin hatası)](/en/terms/genelleştirme-hatası-modelin-görmediği-verilerdeki-tahmin-hatası/)
