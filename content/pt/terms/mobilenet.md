---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
aliases:
  - /pt/terms/mobilenet/
date: "2026-07-18T15:13:14.615740Z"
lastmod: "2026-07-18T15:51:59.513449Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "O MobileNet é uma família de redes neurais profundas leves projetadas para aplicações de visão em dispositivos móveis e embarcados."
---

## Definition

Os MobileNets utilizam convoluções separáveis por profundidade para reduzir drasticamente o custo computacional e o tamanho do modelo em comparação com as convoluções padrão. Essa arquitetura permite a extração eficiente de recursos em dispositivos com recursos limitados.

### Summary

O MobileNet é uma família de redes neurais profundas leves projetadas para aplicações de visão em dispositivos móveis e embarcados.

## Key Concepts

- Convoluções Separáveis por Profundidade
- Eficiência do Modelo
- Computação de Borda
- Aprendizado por Transferência

## Use Cases

- Detecção de objetos em tempo real em smartphones
- Classificação de imagens em dispositivos IoT
- Reconhecimento facial em aplicativos móveis

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (Arquitetura de rede leve)](/en/terms/shufflenet-arquitetura-de-rede-leve/)
- [SqueezeNet (Arquitetura de rede leve)](/en/terms/squeezenet-arquitetura-de-rede-leve/)
- [EfficientNet (Arquitetura de rede eficiente)](/en/terms/efficientnet-arquitetura-de-rede-eficiente/)
- [Convolutional Neural Network (Rede Neural Convolucional)](/en/terms/convolutional-neural-network-rede-neural-convolucional/)
