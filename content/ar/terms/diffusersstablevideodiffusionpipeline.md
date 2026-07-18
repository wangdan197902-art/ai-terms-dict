---
title: "Diffusers: خط أنابيب الانتشار المستقر للفيديو"
term_id: "diffusersstablevideodiffusionpipeline"
category: "application_paradigms"
subcategory: ""
tags: ["video-generation", "hugging-face", "diffusion-models", "computer-vision"]
difficulty: 4
weight: 1
slug: "diffusersstablevideodiffusionpipeline"
aliases:
  - /ar/terms/diffusersstablevideodiffusionpipeline/
date: "2026-07-18T15:54:18.285263Z"
lastmod: "2026-07-18T17:15:08.497817Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "غلاف لخط أنابيب مكتبة Hugging Face Diffusers يستخدم نموذج الانتشار المستقر للفيديو لتوليد مقاطع فيديو من صور ثابتة."
---

## Definition

يشير هذا المصطلح إلى تنفيذ محدد داخل مكتبة Hugging Face Diffusers مصمم لتوليد الفيديو. يدمج هذا النموذج نموذج الانتشار المستقر للفيديو (SVD)، وهو نموذج يعتمد على الانتشار في الفضاء الكامن (latent space) لتوليد مقاطع فيديو متحركة انطلاقاً من إطارات صور ثابتة، مع الحفاظ على الاتساق البصري عبر الزمن.

### Summary

غلاف لخط أنابيب مكتبة Hugging Face Diffusers يستخدم نموذج الانتشار المستقر للفيديو لتوليد مقاطع فيديو من صور ثابتة.

## Key Concepts

- توليد الفيديو من الصور
- انتشار الفضاء الكامن
- مكتبة Hugging Face Diffusers
- نموذج الانتشار المستقر للفيديو

## Use Cases

- تحريك الأعمال الفنية أو الصور الفوتوغرافية الثابتة
- إنشاء مقاطع فيديو قصيرة لمحتوى وسائل التواصل الاجتماعي
- النماذج الأولية للتأثيرات البصرية في إنتاج الأفلام

## Code Example

```python
from diffusers import StableVideoDiffusionPipeline
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid", torch_dtype=torch.float16)
pipe.enable_model_cpu_offload()
# Usage would involve loading an image and calling pipe(image)
```

## Related Terms

- [Stable Diffusion (الانتشار المستقر)](/en/terms/stable-diffusion-الانتشار-المستقر/)
- [Video Diffusion Models (نماذج انتشار الفيديو)](/en/terms/video-diffusion-models-نماذج-انتشار-الفيديو/)
- [Hugging Face Transformers (مكتبة هوجينج فيس ترانسفورمرز)](/en/terms/hugging-face-transformers-مكتبة-هوجينج-فيس-ترانسفورمرز/)
- [Latent Diffusion (الانتشار الكامن)](/en/terms/latent-diffusion-الانتشار-الكامن/)
