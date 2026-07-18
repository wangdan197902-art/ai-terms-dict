#!/usr/bin/env python3
"""HuggingFace AI术语抓取器。

从huggingface.co/api/models抓取热门模型的tags和pipeline_tag，提取AI术语。

API: https://huggingface.co/api/models?limit=N&sort=likes&direction=-1
"""
import json
import time
from typing import List, Dict, Any

from scripts.fetchers.base import BaseFetcher, fetch_url


class HuggingFaceFetcher(BaseFetcher):
    """HuggingFace抓取器。"""

    name = "huggingface"

    # HuggingFace pipeline_tag到我们分类的映射
    PIPELINE_TO_CATEGORY = {
        "text-generation": "application_paradigms",
        "text2text-generation": "application_paradigms",
        "text-classification": "application_paradigms",
        "token-classification": "application_paradigms",
        "question-answering": "application_paradigms",
        "fill-mask": "training_techniques",
        "summarization": "application_paradigms",
        "translation": "application_paradigms",
        "feature-extraction": "training_techniques",
        "sentence-similarity": "application_paradigms",
        "zero-shot-classification": "application_paradigms",
        "image-classification": "application_paradigms",
        "object-detection": "application_paradigms",
        "image-segmentation": "application_paradigms",
        "image-to-text": "application_paradigms",
        "image-to-image": "application_paradigms",
        "text-to-image": "application_paradigms",
        "text-to-speech": "application_paradigms",
        "speech-to-text": "application_paradigms",
        "automatic-speech-recognition": "application_paradigms",
        "audio-classification": "application_paradigms",
        "conversational": "application_paradigms",
        "table-question-answering": "application_paradigms",
        "visual-question-answering": "application_paradigms",
        "document-question-answering": "application_paradigms",
        "reinforcement-learning": "training_techniques",
        "robotics": "application_paradigms",
        "time-series-forecasting": "application_paradigms",
    }

    def fetch_models(self, limit: int = 500) -> List[Dict[str, Any]]:
        """抓取热门模型列表。"""
        all_models = []
        batch_size = 100

        for offset in range(0, limit, batch_size):
            url = f"https://huggingface.co/api/models?limit={batch_size}&sort=likes&direction=-1&skip={offset}"
            print(f"  抓取: {url}")
            content = fetch_url(url, timeout=20, retries=3, delay=2.0)

            if not content:
                break

            try:
                models = json.loads(content)
                if not models:
                    break
                all_models.extend(models)
                print(f"    ✓ 获取 {len(models)} 模型")
            except json.JSONDecodeError:
                print(f"  ✗ JSON解析失败")
                break

            time.sleep(1.0)

            if len(all_models) >= limit:
                break

        return all_models[:limit]

    def extract_terms_from_models(self, models: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """从模型列表提取术语（tags + pipeline_tag）。"""
        terms_dict = {}  # 用english去重

        for model in models:
            model_id = model.get("id", "")
            tags = model.get("tags", [])
            pipeline_tag = model.get("pipeline_tag")
            library_name = model.get("library_name")

            # 从tags提取术语
            for tag in tags:
                if not tag or len(tag) < 3:
                    continue
                # 跳过非术语tag
                if tag.startswith("license:") or tag.startswith("region:") or tag.startswith("base_model:"):
                    continue
                if tag in ["transformers", "pytorch", "tf", "jax", "safetensors",
                          "onnx", "coreml", "gguf", "llama.cpp", "endpoints_compatible",
                          "dataset", "eval-results", "conversational"]:
                    continue

                # 转为术语
                term_name = self.normalize_term(tag.replace("-", " ").replace("_", " ").title())
                if len(term_name) < 3 or len(term_name) > 60:
                    continue

                key = term_name.lower()
                if key not in terms_dict:
                    term_id = self.slugify(term_name)
                    category = self.PIPELINE_TO_CATEGORY.get(
                        pipeline_tag,
                        self.categorize(term_name)
                    )

                    terms_dict[key] = {
                        "term_id": term_id,
                        "english": term_name,
                        "category": category,
                        "subcategory": pipeline_tag or "",
                        "source": "huggingface",
                        "source_url": f"https://huggingface.co/models?pipeline_tag={pipeline_tag}" if pipeline_tag else "https://huggingface.co/models",
                        "aliases": [],
                        "importance": 3,
                        "first_seen_year": None,
                    }

            # 从pipeline_tag提取术语
            if pipeline_tag:
                term_name = self.normalize_term(pipeline_tag.replace("-", " ").title())
                key = term_name.lower()
                if key not in terms_dict and len(term_name) >= 3:
                    term_id = self.slugify(term_name)
                    terms_dict[key] = {
                        "term_id": term_id,
                        "english": term_name,
                        "category": self.PIPELINE_TO_CATEGORY.get(pipeline_tag, "application_paradigms"),
                        "subcategory": pipeline_tag,
                        "source": "huggingface",
                        "source_url": f"https://huggingface.co/models?pipeline_tag={pipeline_tag}",
                        "aliases": [],
                        "importance": 4,
                        "first_seen_year": None,
                    }

        return list(terms_dict.values())

    def fetch_terms(self, limit: int = 300) -> List[Dict[str, Any]]:
        """抓取HuggingFace术语。"""
        print(f"[HuggingFaceFetcher] 开始抓取，目标: {limit} 术语")
        models = self.fetch_models(limit=300)
        print(f"  ✓ 共抓取模型: {len(models)}")

        terms = self.extract_terms_from_models(models)
        print(f"  ✓ 提取唯一术语: {len(terms)}")

        return terms[:limit]


if __name__ == "__main__":
    fetcher = HuggingFaceFetcher()
    terms = fetcher.fetch_terms(limit=300)
    filepath = fetcher.save_raw(terms, "huggingface_terms.json")
    print(f"✓ 保存到: {filepath}")
    from collections import Counter
    cat_counts = Counter(t["category"] for t in terms)
    print(f"分类分布: {dict(cat_counts)}")
