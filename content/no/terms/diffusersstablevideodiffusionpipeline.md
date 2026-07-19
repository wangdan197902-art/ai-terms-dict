---
title: 'Diffusers: Stable Video Diffusion-pipeline'
term_id: diffusersstablevideodiffusionpipeline
category: application_paradigms
subcategory: ''
tags:
- Video Generation
- Hugging Face
- Diffusion Models
- Computer Vision
difficulty: 4
weight: 1
slug: diffusersstablevideodiffusionpipeline
date: '2026-07-18T15:52:12.215112Z'
lastmod: '2026-07-18T16:38:06.994912Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En Hugging Face Diffusers-pipeline-wrapper som bruker Stable Video Diffusion-modellen
  til å generere videoer fra statiske bilder.
---
## Definition

Dette begrepet refererer til en spesifikk implementering i Hugging Face Diffusers-biblioteket, designet for videogenrering. Den integrerer Stable Video Diffusion (SVD)-modellen, som er en latent videodiffusjonsmodell.

### Summary

En Hugging Face Diffusers-pipeline-wrapper som bruker Stable Video Diffusion-modellen til å generere videoer fra statiske bilder.

## Key Concepts

- Bilde-til-video-generering
- Latent rom-diffusjon
- Hugging Face Diffusers
- Stable Video Diffusion-modell

## Use Cases

- Animere statisk kunst eller fotografier
- Lage korte videoklipp til innhold på sosiale medier
- Prototyping av visuelle effekter i filmproduksjon

## Code Example

```python
from diffusers import StableVideoDiffusionPipeline
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid", torch_dtype=torch.float16)
pipe.enable_model_cpu_offload()
# Usage would involve loading an image and calling pipe(image)
```

## Related Terms

- [Stable Diffusion (Stabil diffusjon)](/en/terms/stable-diffusion-stabil-diffusjon/)
- [Videodiffusjonsmodeller](/en/terms/videodiffusjonsmodeller/)
- [Hugging Face Transformers (Transformer-modeller)](/en/terms/hugging-face-transformers-transformer-modeller/)
- [Latent Diffusion (Latent diffusjon)](/en/terms/latent-diffusion-latent-diffusjon/)
