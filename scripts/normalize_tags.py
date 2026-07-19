#!/usr/bin/env python3
"""
P0b-Step1: 标签规范化
- 统一大小写（nlp → NLP）
- 统一格式（deep_learning → Deep Learning）
- 合并同义词（AI paradigms / AI_Paradigms → AI Paradigms）

使用方式: python3 scripts/normalize_tags.py [--dry-run]
"""

import os
import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content"

# 显式同义词映射（合并为目标形式）
SYNONYM_MAP = {
    # 大小写合并
    "nlp": "NLP",
    "llm": "LLM",
    "ai": "AI",
    "agi": "AGI",
    "api": "API",
    "apis": "API",
    "ml": "ML",
    "dl": "DL",
    "cnn": "CNN",
    "rnn": "RNN",
    "gan": "GAN",
    "bert": "BERT",
    "gpt": "GPT",
    "gpu": "GPU",
    "cpu": "CPU",
    "tpu": "TPU",
    "rl": "RL",
    "mlp": "MLP",
    "svm": "SVM",
    "knn": "KNN",
    "pca": "PCA",
    "sgd": "SGD",
    "rags": "RAG",

    # 格式统一：下划线 → 空格
    "deep_learning": "Deep Learning",
    "machine_learning": "Machine Learning",
    "neural_networks": "Neural Networks",
    "neural_network": "Neural Networks",
    "natural_language_processing": "Natural Language Processing",
    "computer_vision": "Computer Vision",
    "reinforcement_learning": "Reinforcement Learning",
    "transfer_learning": "Transfer Learning",
    "supervised_learning": "Supervised Learning",
    "unsupervised_learning": "Unsupervised Learning",
    "self_supervised_learning": "Self-Supervised Learning",
    "few_shot_learning": "Few-Shot Learning",
    "zero_shot_learning": "Zero-Shot Learning",
    "meta_learning": "Meta-Learning",
    "federated_learning": "Federated Learning",
    "active_learning": "Active Learning",
    "online_learning": "Online Learning",
    "contrastive_learning": "Contrastive Learning",
    "multi_agent_systems": "Multi-Agent Systems",
    "ai_foundations": "AI Foundations",
    "ai_paradigms": "AI Paradigms",
    "ai_ecosystem": "AI Ecosystem",
    "ai_infrastructure": "AI Infrastructure",
    "ai_architecture": "AI Architecture",
    "ai_education": "AI Education",
    "ai_ethics": "AI Ethics",
    "ai_security": "AI Security",
    "ai_theory": "AI Theory",
    "ai_concepts": "AI Concepts",
    "ai_models": "AI Models",
    "ai_types": "AI Types",
    "ai_core": "AI Core",
    "ml_fundamentals": "ML Fundamentals",
    "activation_functions": "Activation Functions",
    "loss_functions": "Loss Functions",
    "data_augmentation": "Data Augmentation",
    "data_pipeline": "Data Pipeline",
    "model_evaluation": "Model Evaluation",
    "model_training": "Model Training",
    "model_deployment": "Model Deployment",
    "model_optimization": "Model Optimization",
    "model_compression": "Model Compression",
    "model_distillation": "Model Distillation",
    "game_ai": "Game AI",
    "edge_computing": "Edge Computing",
    "cloud_computing": "Cloud Computing",
    "distributed_computing": "Distributed Computing",
    "knowledge_graph": "Knowledge Graph",
    "knowledge_base": "Knowledge Base",
    "knowledge_representation": "Knowledge Representation",
    "decision_making": "Decision Making",
    "problem_solving": "Problem Solving",
    "feature_engineering": "Feature Engineering",
    "feature_extraction": "Feature Extraction",
    "anomaly_detection": "Anomaly Detection",
    "fraud_detection": "Fraud Detection",
    "object_detection": "Object Detection",
    "face_recognition": "Face Recognition",
    "speech_recognition": "Speech Recognition",
    "speech_synthesis": "Speech Synthesis",
    "text_generation": "Text Generation",
    "image_generation": "Image Generation",
    "code_generation": "Code Generation",
    "question_answering": "Question Answering",
    "sentiment_analysis": "Sentiment Analysis",
    "named_entity_recognition": "Named Entity Recognition",
    "machine_translation": "Machine Translation",
    "language_model": "Language Model",
    "large_language_model": "Large Language Model",
    "transformer_architecture": "Transformer Architecture",
    "attention_mechanism": "Attention Mechanism",
    "generative_models": "Generative Models",
    "discriminative_models": "Discriminative Models",
    "prompt_engineering": "Prompt Engineering",
    "chain_of_thought": "Chain of Thought",
    "in_context_learning": "In-Context Learning",
    "fine_tuning": "Fine-Tuning",
    "pre_training": "Pre-Training",
    "hyperparameter_tuning": "Hyperparameter Tuning",
    "gradient_descent": "Gradient Descent",
    "backpropagation": "Backpropagation",
    "batch_normalization": "Batch Normalization",
    "dropout": "Dropout",
    "data_preprocessing": "Data Preprocessing",
    "exploratory_analysis": "Exploratory Analysis",
    "dimensionality_reduction": "Dimensionality Reduction",
    "clustering": "Clustering",
    "classification": "Classification",
    "regression": "Regression",
    "optimization": "Optimization",
    "regularization": "Regularization",
    "cross_validation": "Cross Validation",
    "ablation_study": "Ablation Study",
    "benchmark": "Benchmark",
    "evaluation_metrics": "Evaluation Metrics",

    # 大小写合并（带下划线版本）
    "ai_paradigms": "AI Paradigms",
    "ai_foundations": "AI Foundations",

    # 连字符 → 空格
    "deep-learning": "Deep Learning",
    "machine-learning": "Machine Learning",
    "neural-networks": "Neural Networks",
    "natural-language-processing": "Natural Language Processing",
    "computer-vision": "Computer Vision",
    "reinforcement-learning": "Reinforcement Learning",
    "few-shot": "Few-Shot",
    "zero-shot": "Zero-Shot",
    "self-supervised": "Self-Supervised",
    "multi-agent": "Multi-Agent",
    "fine-tuning": "Fine-Tuning",
    "pre-training": "Pre-Training",
    "large-language-model": "Large Language Model",
    "transformer-architecture": "Transformer Architecture",
    "attention-mechanism": "Attention Mechanism",
    "prompt-engineering": "Prompt Engineering",
    "chain-of-thought": "Chain of Thought",
    "in-context-learning": "In-Context Learning",
    "ml-fundamentals": "ML Fundamentals",
    "activation-functions": "Activation Functions",
    "loss-functions": "Loss Functions",
    "data-augmentation": "Data Augmentation",
    "model-deployment": "Model Deployment",
    "model-optimization": "Model Optimization",
    "edge-computing": "Edge Computing",
    "cloud-computing": "Cloud Computing",
    "knowledge-graph": "Knowledge Graph",
    "knowledge-base": "Knowledge Base",
    "feature-engineering": "Feature Engineering",
    "anomaly-detection": "Anomaly Detection",
    "object-detection": "Object Detection",
    "face-recognition": "Face Recognition",
    "speech-recognition": "Speech Recognition",
    "speech-synthesis": "Speech Synthesis",
    "text-generation": "Text Generation",
    "image-generation": "Image Generation",
    "code-generation": "Code Generation",
    "question-answering": "Question Answering",
    "sentiment-analysis": "Sentiment Analysis",
    "named-entity-recognition": "Named Entity Recognition",
    "machine-translation": "Machine Translation",
    "language-model": "Language Model",
    "generative-models": "Generative Models",
    "hyperparameter-tuning": "Hyperparameter Tuning",
    "gradient-descent": "Gradient Descent",
    "batch-normalization": "Batch Normalization",
    "data-preprocessing": "Data Preprocessing",
    "dimensionality-reduction": "Dimensionality Reduction",
    "cross-validation": "Cross Validation",
    "ablation-study": "Ablation Study",
    "evaluation-metrics": "Evaluation Metrics",
    "game-ai": "Game AI",
    "ai-core": "AI Core",
}


def normalize_tag(tag: str) -> str:
    """规范化单个标签"""
    if not tag or not isinstance(tag, str):
        return tag

    # 去除首尾空格
    tag = tag.strip()

    # 1. 显式同义词映射
    lower_tag = tag.lower()
    if lower_tag in SYNONYM_MAP:
        return SYNONYM_MAP[lower_tag]

    # 2. 原标签如果已经在映射表中（保留原大小写匹配）
    if tag in SYNONYM_MAP:
        return SYNONYM_MAP[tag]

    # 3. 如果是全小写且有下划线/连字符，转换为 Title Case
    if tag.islower() and ("_" in tag or "-" in tag):
        # 转换分隔符为空格
        normalized = tag.replace("_", " ").replace("-", " ")
        # Title Case，但保留常见缩写全大写
        words = normalized.split()
        result_words = []
        for w in words:
            if w.upper() in {"NLP", "LLM", "AI", "AGI", "API", "ML", "DL", "CNN", "RNN",
                            "GAN", "BERT", "GPT", "GPU", "CPU", "TPU", "RL", "MLP",
                            "SVM", "KNN", "PCA", "SGD", "RAG", "RLHF", "DPO"}:
                result_words.append(w.upper())
            else:
                result_words.append(w.capitalize())
        return " ".join(result_words)

    # 4. 如果是全大写且长度<=5，保持原样（缩写）
    if tag.isupper() and len(tag) <= 5:
        return tag

    # 5. 其他情况保持原样
    return tag


def process_file(file_path: Path, dry_run: bool = False) -> tuple:
    """处理单个 md 文件，返回 (修改前标签数, 修改后标签数, 是否有变化)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return (0, 0, False)

        parts = content.split('---', 2)
        if len(parts) < 3:
            return (0, 0, False)

        fm_text = parts[1]
        body = parts[2]

        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError:
            return (0, 0, False)

        if not fm or 'tags' not in fm:
            return (0, 0, False)

        original_tags = fm.get('tags', [])
        if not isinstance(original_tags, list):
            return (0, 0, False)

        # 规范化所有标签
        normalized_tags = [normalize_tag(t) for t in original_tags if t]

        # 去重（保持顺序）
        seen = set()
        deduped_tags = []
        for t in normalized_tags:
            if t not in seen:
                seen.add(t)
                deduped_tags.append(t)

        if deduped_tags == original_tags:
            return (len(original_tags), len(deduped_tags), False)

        # 修改 front matter
        fm['tags'] = deduped_tags

        # 重新序列化（保持原格式风格：检测是 YAML 还是 TOML）
        new_fm = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
        new_content = f"---\n{new_fm}---{body}"

        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return (len(original_tags), len(deduped_tags), True)

    except Exception as e:
        print(f"  ✗ 处理 {file_path.name} 出错: {e}")
        return (0, 0, False)


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("🔍 DRY RUN 模式（不写入文件）\n")

    # 处理所有语种的所有术语文件
    all_langs = [
        "en", "es", "de", "ja", "fr", "zh", "pt", "ru", "ko", "ar",
        "it", "nl", "pl", "tr", "vi", "th", "id", "sv", "cs", "da",
        "fi", "no", "he", "ro", "hu", "el"
    ]

    total_files = 0
    total_modified = 0
    total_tags_before = 0
    total_tags_after = 0
    lang_stats = {}

    for lang in all_langs:
        lang_dir = CONTENT_DIR / lang / "terms"
        if not lang_dir.exists():
            continue

        lang_files = 0
        lang_modified = 0
        lang_tags_before = 0
        lang_tags_after = 0

        for md_file in lang_dir.glob("*.md"):
            lang_files += 1
            tags_before, tags_after, modified = process_file(md_file, dry_run)
            lang_tags_before += tags_before
            lang_tags_after += tags_after
            if modified:
                lang_modified += 1

        lang_stats[lang] = {
            "files": lang_files,
            "modified": lang_modified,
            "tags_before": lang_tags_before,
            "tags_after": lang_tags_after,
        }
        total_files += lang_files
        total_modified += lang_modified
        total_tags_before += lang_tags_before
        total_tags_after += lang_tags_after

        if lang_modified > 0:
            print(f"  {lang}: {lang_files} 文件, {lang_modified} 修改, 标签 {lang_tags_before}→{lang_tags_after}")

    print(f"\n{'='*60}")
    print(f"✅ {'DRY RUN ' if dry_run else ''}规范化完成")
    print(f"{'='*60}")
    print(f"总文件数: {total_files}")
    print(f"修改文件数: {total_modified}")
    print(f"修改率: {total_modified/total_files*100:.1f}%")
    print(f"标签总数: {total_tags_before} → {total_tags_after}")
    print(f"减少标签数: {total_tags_before - total_tags_after}")


if __name__ == "__main__":
    main()
