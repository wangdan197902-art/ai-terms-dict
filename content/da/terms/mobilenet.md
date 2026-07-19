---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
date: "2026-07-18T16:08:04.817444Z"
lastmod: "2026-07-18T17:15:09.312273Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "MobileNet er en familie af letvægts-dybe neurale netværk designet til mobile og indlejrede visionapplikationer."
---
## Definition

MobileNets udnytter dybdeseparable konvolutioner til drastisk at reducere beregningsomkostninger og modellens størrelse sammenlignet med standardkonvolutioner. Denne arkitektur muliggør effektiv funktionsekstraktion på

### Summary

MobileNet er en familie af letvægts-dybe neurale netværk designet til mobile og indlejrede visionapplikationer.

## Key Concepts

- Dybdeseparable konvolutioner
- Model-effektivitet
- Edge computing
- Overførselslæring

## Use Cases

- Objektgenkendelse i realtid på smartphones
- Billedklassificering på IoT-enheder
- Ansigtsgenkendelse i mobilapps

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (ShuffleNet)](/en/terms/shufflenet-shufflenet/)
- [SqueezeNet (SqueezeNet)](/en/terms/squeezenet-squeezenet/)
- [EfficientNet (EfficientNet)](/en/terms/efficientnet-efficientnet/)
- [Konvolutionsneuralt netværk (Convolutional Neural Network)](/en/terms/konvolutionsneuralt-netværk-convolutional-neural-network/)
