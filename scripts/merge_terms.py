#!/usr/bin/env python3
"""合并去重脚本。

从3个数据源（Wikipedia/HuggingFace/arXiv）抓取术语，去重合并到种子库。

策略：
1. 加载现有seed_terms.json（200术语）作为基础
2. 从3个数据源抓取新术语
3. 严格过滤：去除非术语、过短、过长、含数字编号的
4. 多维度去重：term_id + english(lowercase) + aliases
5. 合并到种子库，目标≥1000术语
6. 重新计算importance（基于来源数和频次）
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Set, Tuple

# 行缓冲输出（实时查看进度）
try:
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
except Exception:
    pass


# 项目根（并将项目根加入sys.path以支持 scripts.fetchers 导入）
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
SEED_FILE = PROJECT_ROOT / "data" / "seeds" / "seed_terms.json"
RAW_DIR = PROJECT_ROOT / "data" / "raw"
MERGED_FILE = PROJECT_ROOT / "data" / "seeds" / "seed_terms.json"


# 严格过滤的黑名单
BLACKLIST_TERMS = {
    # 通用词
    "across", "language", "text", "data", "model", "models", "method",
    "methods", "approach", "approaches", "result", "results", "study",
    "studies", "research", "work", "paper", "proposed", "novel", "new",
    "existing", "previous", "recent", "show", "shown", "shows", "present",
    "presents", "introduce", "introduces", "describe", "describes",
    "discuss", "discusses", "analyze", "analyzes", "evaluate", "evaluates",
    "compare", "compares", "however", "although", "though", "while",
    "because", "since", "therefore", "thus", "hence", "based", "using",
    "used", "use", "uses", "able", "ability", "different", "similar",
    "various", "many", "much", "one", "two", "three", "first", "second",
    "third", "last", "final", "initial", "current", "next", "following",
    "real", "world", "real-world", "end-to-end", "state-of-the-art",
    "across", "human", "humans", "machine", "computer", "artificial",
    "intelligence", "deep", "neural", "network", "networks",
    # HuggingFace特定垃圾
    "custom code", "text", "image", "video", "audio", "speech",
    "diffusers:fluxpipeline", "arxiv:2501.12948",
    # 单字母/双字母
    "ai", "ml", "dl", "cv", "nlp", "rl", "api", "url", "id",
}

# 非术语的pattern
NON_TERM_PATTERNS = [
    re.compile(r'^arxiv:\d', re.IGNORECASE),  # arxiv编号
    re.compile(r'^\d{4}\.\d{4,5}'),  # arxiv ID
    re.compile(r'^[a-z]:'),  # xxx:yyy格式
    re.compile(r'v\d+$'),  # 结尾版本号
    re.compile(r'^[A-Z]{1,3}$'),  # 全大写缩写≤3字符（可能是单位）
    re.compile(r'\d{4,}'),  # 含4位以上数字
]


def is_valid_term(name: str) -> bool:
    """判断是否是有效术语。"""
    if not name or len(name) < 3 or len(name) > 60:
        return False

    name_lower = name.lower().strip()

    # 黑名单检查
    if name_lower in BLACKLIST_TERMS:
        return False

    # 全数字
    if name_lower.replace("-", "").replace("_", "").isdigit():
        return False

    # 非术语pattern
    for pattern in NON_TERM_PATTERNS:
        if pattern.search(name):
            return False

    # 检查首字符（必须是字母）
    if not name[0].isalpha():
        return False

    # 检查是否全是常见英文词组合（粗略）
    words = name_lower.replace("-", " ").replace("_", " ").split()
    if not words:
        return False
    # 所有词都在黑名单
    if all(w in BLACKLIST_TERMS for w in words):
        return False

    return True


def slugify(name: str) -> str:
    """slugify函数（与base.py一致）。"""
    s = name.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "_", s)
    s = s.strip("_")
    return s


def categorize(name: str, description: str = "") -> Tuple[str, str]:
    """分类函数（与base.py一致，但返回category+subcategory）。"""
    text = (name + " " + description).lower()

    if any(kw in text for kw in ["ethic", "safety", "fairness", "bias", "privacy",
                                  "alignment", "responsible", "trustworthy", "governance",
                                  "transparency", "accountab", "consent", "gdpr", "harm",
                                  "toxic", "jailbreak", "deepfake", "misinformation",
                                  "watermark", "red team"]):
        return "ethics_safety", "core_principles"

    if any(kw in text for kw in ["training", "learning", "optimization", "gradient",
                                  "backprop", "loss", "regulariz", "dropout", "epoch",
                                  "fine-tun", "fine_tun", "pretrain", "pre-train",
                                  "reinforcement", "supervised", "unsupervised",
                                  "transfer learn", "federated", "quantiz", "pruning",
                                  "distill", "batch norm", "layer norm", "activation",
                                  "attention", "transformer", "embedding", "encoder",
                                  "decoder", "lora", "qlora"]):
        return "training_techniques", "model_training"

    if any(kw in text for kw in ["agent", "rag", "retrieval", "prompt", "chain of thought",
                                  "reason", "planning", "tool use", "function call",
                                  "chatbot", "assistant", "generation", "summariz",
                                  "translation", "search", "recommend",
                                  "vision", "image", "video", "speech", "nlp",
                                  "language model", "llm", "multimodal", "dialogue",
                                  "diffusion", "gan", "vae", "autoencoder"]):
        return "application_paradigms", "applications"

    if any(kw in text for kw in ["api", "server", "deploy", "docker", "kubernetes",
                                  "microservice", "latency", "throughput", "cach",
                                  "scalab", "monitor", "observ", "log", "trace",
                                  "inference", "serv", "endpoint", "rest", "graphql",
                                  "webhook", "sdk", "cli", "framework", "library"]):
        return "engineering_practice", "infrastructure"

    return "basic_concepts", "foundational"


def main():
    print("=" * 60)
    print("合并去重脚本：3源抓取 → 种子库扩展")
    print("=" * 60)

    # 1. 加载现有种子库
    print(f"\n[1] 加载现有种子库: {SEED_FILE}")
    with open(SEED_FILE, "r", encoding="utf-8") as f:
        existing_seeds = json.load(f)
    print(f"  现有术语: {len(existing_seeds)}")

    # 构建去重索引
    existing_index = {}  # term_id -> seed
    existing_english = {}  # english_lower -> seed
    for seed in existing_seeds:
        existing_index[seed["term_id"]] = seed
        existing_english[seed["english"].lower()] = seed

    # 2. 抓取3个数据源
    print(f"\n[2] 开始抓取3个数据源...")

    all_new_terms = []

    # Wikipedia
    try:
        from scripts.fetchers.wikipedia_fetcher import WikipediaFetcher
        wiki_fetcher = WikipediaFetcher()
        wiki_terms = wiki_fetcher.fetch_terms(limit=500)
        print(f"  Wikipedia: {len(wiki_terms)} 术语")
        all_new_terms.extend(wiki_terms)
    except Exception as e:
        print(f"  ✗ Wikipedia抓取失败: {e}")

    # HuggingFace
    try:
        from scripts.fetchers.huggingface_fetcher import HuggingFaceFetcher
        hf_fetcher = HuggingFaceFetcher()
        hf_terms = hf_fetcher.fetch_terms(limit=300)
        print(f"  HuggingFace: {len(hf_terms)} 术语")
        all_new_terms.extend(hf_terms)
    except Exception as e:
        print(f"  ✗ HuggingFace抓取失败: {e}")

    # arXiv
    try:
        from scripts.fetchers.arxiv_fetcher import ArxivFetcher
        arxiv_fetcher = ArxivFetcher()
        arxiv_terms = arxiv_fetcher.fetch_terms(limit=200)
        print(f"  arXiv: {len(arxiv_terms)} 术语")
        all_new_terms.extend(arxiv_terms)
    except Exception as e:
        print(f"  ✗ arXiv抓取失败: {e}")

    print(f"\n  共抓取: {len(all_new_terms)} 术语")

    # 3. 严格过滤+去重
    print(f"\n[3] 严格过滤+去重...")
    new_terms = {}
    source_counts = defaultdict(int)  # term_id -> 出现的源数

    for term in all_new_terms:
        name = term.get("english", "")
        if not is_valid_term(name):
            continue

        term_id = term.get("term_id") or slugify(name)
        if not term_id:
            continue

        # 跳过已存在的
        if term_id in existing_index:
            source_counts[term_id] += 1
            continue
        if name.lower() in existing_english:
            source_counts[existing_english[name.lower()]["term_id"]] += 1
            continue

        # 已在新术语中
        if term_id in new_terms:
            # 合并aliases
            if term.get("english") and term["english"] not in new_terms[term_id]["aliases"]:
                new_terms[term_id]["aliases"].append(term["english"])
            source_counts[term_id] += 1
            continue

        # 重新分类（统一标准）
        category, subcategory = categorize(name)

        new_terms[term_id] = {
            "term_id": term_id,
            "english": name,
            "category": category,
            "subcategory": subcategory,
            "source_url": term.get("source_url", ""),
            "importance": term.get("importance", 3),
            "aliases": term.get("aliases", []),
            "first_seen_year": term.get("first_seen_year"),
        }
        source_counts[term_id] += 1

    print(f"  过滤后唯一新术语: {len(new_terms)}")

    # 4. 根据源数调整importance
    for term_id, term in new_terms.items():
        source_count = source_counts.get(term_id, 1)
        if source_count >= 3:
            term["importance"] = 5
        elif source_count >= 2:
            term["importance"] = max(term["importance"], 4)
        # 标注来源数
        term["source_count"] = source_count

    # 5. 合并到种子库
    print(f"\n[4] 合并到种子库...")
    final_seeds = existing_seeds + list(new_terms.values())
    print(f"  最终术语数: {len(final_seeds)}")

    # 6. 分类分布检查
    from collections import Counter
    cat_counts = Counter(t["category"] for t in final_seeds)
    print(f"  分类分布: {dict(cat_counts)}")

    # 7. 源分布
    source_dist = Counter()
    for t in final_seeds:
        url = t.get("source_url", "")
        if "wikipedia" in url:
            source_dist["wikipedia"] += 1
        elif "huggingface" in url:
            source_dist["huggingface"] += 1
        elif "arxiv" in url:
            source_dist["arxiv"] += 1
        else:
            source_dist["local"] += 1
    print(f"  来源分布: {dict(source_dist)}")

    # 8. 保存
    print(f"\n[5] 保存到: {MERGED_FILE}")
    # 移除source_count（临时字段）
    for t in final_seeds:
        t.pop("source_count", None)
    with open(MERGED_FILE, "w", encoding="utf-8") as f:
        json.dump(final_seeds, f, ensure_ascii=False, indent=2)
    print(f"  ✓ 已保存")

    # 9. 验证
    print(f"\n[6] 验证...")
    with open(MERGED_FILE, "r", encoding="utf-8") as f:
        verify = json.load(f)
    print(f"  术语总数: {len(verify)}")
    if len(verify) >= 1000:
        print(f"  ✓ 达到1000术语目标！")
    else:
        print(f"  ⚠ 未达1000，差 {1000 - len(verify)}")

    # 检查重复term_id
    term_ids = [t["term_id"] for t in verify]
    duplicates = [tid for tid in set(term_ids) if term_ids.count(tid) > 1]
    if duplicates:
        print(f"  ⚠ 发现重复term_id: {len(duplicates)}")
    else:
        print(f"  ✓ 无重复term_id")

    return 0 if len(verify) >= 1000 else 1


if __name__ == "__main__":
    sys.exit(main())
