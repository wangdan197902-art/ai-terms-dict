---
title: Yoğun (Dense)
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:49:34.400519Z'
lastmod: '2026-07-18T16:38:07.297436Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Önceki katman veya boyuttaki her bir elemana bağlı olan bir katman veya
  tensör yapısı.
---
## Definition

Sinir ağlarında 'yoğun', her nöronun önceki katmandaki tüm nöronlardan girdi aldığı tamamen bağlı katmanları ifade eder. Bu durum, evrişimli veya seyrek bağlantılı yapıların aksine, tüm nöronlar arası bağlantı kurmayı sağlar.

### Summary

Önceki katman veya boyuttaki her bir elemana bağlı olan bir katman veya tensör yapısı.

## Key Concepts

- Tamamen Bağlı
- Ağırlık Matrisi
- Aktivasyon Fonksiyonu
- Özellik Entegrasyonu

## Use Cases

- Çok Katmanlı Algılayıcılarda (MLP) son sınıflandırma katmanları
- Hibrit modellerde özellik füzyonu
- Basit regresyon görevleri

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [İleri Beslemeli Sinir Ağı (Geri besleme içermeyen sinir ağı mimarisi)](/en/terms/i-leri-beslemeli-sinir-ağı-geri-besleme-içermeyen-sinir-ağı-mimarisi/)
- [Geri Yayılım (Hata hesaplaması ve ağırlık güncelleme yöntemi)](/en/terms/geri-yayılım-hata-hesaplaması-ve-ağırlık-güncelleme-yöntemi/)
- [ReLU (Doğrusal olmayan aktivasyon fonksiyonu)](/en/terms/relu-doğrusal-olmayan-aktivasyon-fonksiyonu/)
- [Yan Terimi (Modelin esnekliğini artıran sabit değer)](/en/terms/yan-terimi-modelin-esnekliğini-artıran-sabit-değer/)
