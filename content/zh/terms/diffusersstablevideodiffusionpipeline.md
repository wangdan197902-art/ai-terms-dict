---
title: 'Diffusers: Stable Video Diffusion Pipeline'
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
date: '2026-07-18T11:15:21.633124Z'
lastmod: '2026-07-18T11:44:45.490284Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一个 Hugging Face Diffusers 管道封装，利用 Stable Video Diffusion 模型从静态图像生成视频。
---
## Definition

该术语指 Hugging Face Diffusers 库中专为视频生成设计的特定实现。它集成了 Stable Video Diffusion (SVD) 模型，这是一种潜在视频扩散模型，能够将静态图像转化为动态视频内容。

### Summary

一个 Hugging Face Diffusers 管道封装，利用 Stable Video Diffusion 模型从静态图像生成视频。

## Key Concepts

- 图像到视频生成
- 潜在空间扩散
- Hugging Face Diffusers
- Stable Video Diffusion 模型

## Use Cases

- 为静态艺术作品或照片添加动画效果
- 为社交媒体内容创建短视频片段
- 在电影制作中进行视觉效果的原型设计

## Code Example

```python
from diffusers import StableVideoDiffusionPipeline
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid", torch_dtype=torch.float16)
pipe.enable_model_cpu_offload()
# Usage would involve loading an image and calling pipe(image)
```

## Related Terms

- [Stable Diffusion (稳定扩散)](/en/terms/stable-diffusion-稳定扩散/)
- [Video Diffusion Models (视频扩散模型)](/en/terms/video-diffusion-models-视频扩散模型/)
- [Hugging Face Transformers (Hugging Face 转换器库)](/en/terms/hugging-face-transformers-hugging-face-转换器库/)
- [Latent Diffusion (潜在扩散)](/en/terms/latent-diffusion-潜在扩散/)
