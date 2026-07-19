#!/usr/bin/env python3
"""IndexNow URL 批量提交脚本

将 public/ 目录下所有 index.html 页面对应的 URL 批量提交到 IndexNow API，
加速 Bing/Yandex/Czech search engine 收录。

IndexNow 协议：
- 官网：https://www.indexnow.org/
- 端点：POST https://api.indexnow.org/IndexNow
- 每次 POST 最多 10,000 个 URL
- 需在网站根目录放一个 {key}.txt 文件用于身份验证

使用方式：
    # 生成密钥并提交所有 URL
    python3 scripts/submit_to_indexnow.py

    # 测试模式（只看会提交什么，不实际调用 API）
    python3 scripts/submit_to_indexnow.py --dry-run

    # 限制提交 100 个用于测试
    python3 scripts/submit_to_indexnow.py --limit 100

    # 使用已有密钥
    python3 scripts/submit_to_indexnow.py --key abc123def456
"""
from __future__ import annotations

import argparse
import sys
import time
import secrets
from pathlib import Path

import requests


# ============================================================================
# 站点配置
# ============================================================================
SITE_HOST: str = "terms.ai-term-hub.com"
SITE_BASE_URL: str = f"https://{SITE_HOST}"

# 项目根目录（脚本位于 scripts/ 下，根目录是上一级）
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
PUBLIC_DIR: Path = PROJECT_ROOT / "public"

# IndexNow API 配置
INDEXNOW_API_URL: str = "https://api.indexnow.org/IndexNow"
INDEXNOW_BATCH_SIZE: int = 10000            # 每批最多 10000 个 URL（API 上限）
INDEXNOW_BATCH_INTERVAL_SEC: int = 1        # 批次之间的间隔（秒），避免触发限流
INDEXNOW_MAX_RETRIES: int = 3               # 单批最大重试次数
INDEXNOW_RETRY_BACKOFF_BASE_SEC: float = 1.0  # 指数退避基数：1s, 2s, 4s

# 需要跳过的目录名（出现在相对路径的任一段都跳过）
# - pagefind: Pagefind 搜索索引目录（如果启用），不应被搜索引擎索引
# - search: 每个语种下的搜索结果页，不应被索引
SKIP_PATH_PARTS: tuple[str, ...] = ("pagefind", "search")


# ============================================================================
# URL 提取
# ============================================================================
def extract_urls_from_public(public_dir: Path) -> list[str]:
    """遍历 public/ 目录下所有 index.html，构造完整 URL 列表。

    转换规则：
        public/en/index.html              -> https://terms.ai-term-hub.com/en/
        public/en/terms/llm/index.html    -> https://terms.ai-term-hub.com/en/terms/llm/
        public/zh/tags/nlp/index.html     -> https://terms.ai-term-hub.com/zh/tags/nlp/
        public/index.html                 -> https://terms.ai-term-hub.com/

    跳过规则：
        - public/pagefind/ 下所有文件（搜索索引）
        - public/{lang}/search/ 下所有文件（搜索结果页）

    Args:
        public_dir: public/ 目录绝对路径

    Returns:
        URL 字符串列表（已去重、已排序）
    """
    if not public_dir.exists():
        raise FileNotFoundError(f"public 目录不存在: {public_dir}")

    urls: set[str] = set()
    skipped: int = 0

    # 递归遍历所有 index.html 文件
    for html_path in public_dir.rglob("index.html"):
        try:
            rel_path = html_path.relative_to(public_dir)
        except ValueError:
            # 理论上不会发生（rglob 返回的路径都在 public_dir 下）
            continue

        rel_parts = rel_path.parts

        # 跳过 pagefind/ 和 search/ 下的文件（按路径段精确匹配，避免误伤如 research 等目录）
        if any(part in SKIP_PATH_PARTS for part in rel_parts):
            skipped += 1
            continue

        # 构造 URL 路径：去掉末尾的 "index.html"，剩余部分拼成 /a/b/ 形式
        path_parts = list(rel_parts[:-1])  # 去掉 "index.html"

        if not path_parts:
            # public/index.html -> 首页根 URL
            url = SITE_BASE_URL + "/"
        else:
            url = SITE_BASE_URL + "/" + "/".join(path_parts) + "/"

        urls.add(url)

    print(f"[URL 提取] 共发现 {len(urls)} 个 URL，跳过 {skipped} 个不需要的页面")
    return sorted(urls)


# ============================================================================
# IndexNow 密钥管理
# ============================================================================
def generate_indexnow_key() -> str:
    """生成 IndexNow API 密钥（32 位十六进制字符串）。

    IndexNow 规范要求：
    - 长度 8~128 字符
    - 只能包含：a-z A-Z 0-9 -
    - 推荐使用 16~32 位十六进制字符串

    Returns:
        32 位十六进制字符串
    """
    # secrets.token_hex(16) 生成 16 字节 = 32 个十六进制字符
    return secrets.token_hex(16)


def ensure_key_file(public_dir: Path, key: str) -> Path:
    """确保 public/{key}.txt 文件存在，内容为 key 本身（纯文本）。

    部署后可通过 https://terms.ai-term-hub.com/{key}.txt 访问。
    IndexNow 收到提交后会请求该 URL 验证密钥，必须返回纯文本的 key。

    Args:
        public_dir: public/ 目录绝对路径
        key: IndexNow 密钥

    Returns:
        key 文件绝对路径
    """
    key_file_path = public_dir / f"{key}.txt"

    if key_file_path.exists():
        existing = key_file_path.read_text(encoding="utf-8").strip()
        if existing == key:
            print(f"[密钥文件] 已存在且内容匹配: {key_file_path.name}")
            return key_file_path
        # 内容不匹配（旧密钥残留），覆盖
        print(f"[密钥文件] 已存在但内容不匹配，将覆盖: {key_file_path.name}")

    key_file_path.write_text(key, encoding="utf-8")
    print(f"[密钥文件] 已创建: {key_file_path.name}")
    return key_file_path


# ============================================================================
# IndexNow API 提交
# ============================================================================
def submit_batch(
    urls: list[str],
    key: str,
    dry_run: bool = False,
) -> tuple[bool, int, str]:
    """向 IndexNow API 提交一批 URL。

    Args:
        urls: 本批要提交的 URL 列表（最多 10000 个）
        key: IndexNow API 密钥
        dry_run: 是否为试运行模式（不实际调用 API）

    Returns:
        (是否成功, HTTP 状态码, 状态描述/错误信息)
        - dry-run 模式返回 (True, 0, "dry-run")
    """
    payload = {
        "host": SITE_HOST,
        "key": key,
        "keyLocation": f"{SITE_BASE_URL}/{key}.txt",
        "urlList": urls,
    }

    if dry_run:
        # dry-run 模式：只打印请求体摘要，不实际调用 API
        print(f"  [DRY-RUN] 将提交 {len(urls)} 个 URL（不实际调用 API）")
        show_count = min(len(urls), 20)
        print(f"  [DRY-RUN] URL 示例（前 {show_count} 个）：")
        for u in urls[:show_count]:
            print(f"    - {u}")
        if len(urls) > show_count:
            print(f"    ... 等共 {len(urls)} 个")
        return True, 0, "dry-run"

    # 实际调用 API，带指数退避重试
    last_status: int = 0
    last_msg: str = ""

    for attempt in range(1, INDEXNOW_MAX_RETRIES + 1):
        try:
            response = requests.post(
                INDEXNOW_API_URL,
                json=payload,
                headers={"Content-Type": "application/json; charset=utf-8"},
                timeout=60,
            )
            last_status = response.status_code
            last_msg = (response.text or "").strip()[:200]

            # 200 = 已接受，URL 将被立即抓取
            # 202 = 已接受但待处理
            if response.status_code in (200, 202):
                return True, response.status_code, last_msg

            # 4xx 客户端错误（除 429 限流外）通常重试无意义
            #   400 = 错误请求（URL 格式错误等）
            #   422 = 密钥不匹配（keyLocation 返回的内容与 key 不一致）
            if 400 <= response.status_code < 500 and response.status_code != 429:
                print(f"  [API 错误] HTTP {response.status_code}: {last_msg or '(无响应体)'}")
                if response.status_code == 422:
                    print(f"  [422 提示] 请确认 https://{SITE_HOST}/{key}.txt 已部署且内容为密钥本身")
                return False, response.status_code, last_msg

            # 5xx 服务端错误 / 429 限流：可重试
            print(f"  [重试 {attempt}/{INDEXNOW_MAX_RETRIES}] HTTP {response.status_code}: {last_msg or '(无响应体)'}")

        except requests.exceptions.RequestException as e:
            last_status = -1
            last_msg = str(e)
            print(f"  [网络异常 {attempt}/{INDEXNOW_MAX_RETRIES}] {e}")

        # 指数退避：1s, 2s, 4s
        if attempt < INDEXNOW_MAX_RETRIES:
            backoff = INDEXNOW_RETRY_BACKOFF_BASE_SEC * (2 ** (attempt - 1))
            print(f"  等待 {backoff:.1f}s 后重试...")
            time.sleep(backoff)

    return False, last_status, last_msg


def submit_all_urls(
    urls: list[str],
    key: str,
    dry_run: bool = False,
) -> tuple[int, int]:
    """将 URL 列表分批提交到 IndexNow API。

    Args:
        urls: 完整 URL 列表
        key: IndexNow API 密钥
        dry_run: 是否为试运行模式

    Returns:
        (成功批次数, 失败批次数)
    """
    total_urls = len(urls)
    total_batches = (total_urls + INDEXNOW_BATCH_SIZE - 1) // INDEXNOW_BATCH_SIZE

    print(f"\n[提交计划] 共 {total_urls} 个 URL，将分 {total_batches} 批提交")
    print(f"[提交计划] 每批最多 {INDEXNOW_BATCH_SIZE} 个 URL，批次间隔 {INDEXNOW_BATCH_INTERVAL_SEC}s\n")

    success_batches = 0
    failed_batches = 0

    for i in range(0, total_urls, INDEXNOW_BATCH_SIZE):
        batch_num = i // INDEXNOW_BATCH_SIZE + 1
        batch = urls[i : i + INDEXNOW_BATCH_SIZE]
        print(f"===== 第 {batch_num}/{total_batches} 批提交中（{len(batch)} 个 URL）=====")

        ok, status, msg = submit_batch(batch, key, dry_run=dry_run)
        if ok:
            success_batches += 1
            if not dry_run:
                print(f"  ✓ 提交成功（HTTP {status}）")
        else:
            failed_batches += 1
            print(f"  ✗ 提交失败（HTTP {status}）: {msg}")

        # 批次间隔（最后一批不用等）
        if batch_num < total_batches and not dry_run:
            print(f"  批次间隔等待 {INDEXNOW_BATCH_INTERVAL_SEC}s...")
            time.sleep(INDEXNOW_BATCH_INTERVAL_SEC)

        print()

    return success_batches, failed_batches


# ============================================================================
# 主入口
# ============================================================================
def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="批量提交 URL 到 IndexNow API 加速 Bing/Yandex 收录",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
使用示例:
  # 生成密钥并提交所有 URL
  python3 scripts/submit_to_indexnow.py

  # 测试模式（只看会提交什么）
  python3 scripts/submit_to_indexnow.py --dry-run

  # 限制提交 100 个用于测试
  python3 scripts/submit_to_indexnow.py --limit 100

  # 使用已有密钥
  python3 scripts/submit_to_indexnow.py --key abc123def456
""",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="试运行模式：只输出将要提交的 URL，不实际调用 API",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="限制提交的 URL 数量（0 = 不限制，用于测试）",
    )
    parser.add_argument(
        "--key",
        type=str,
        default="",
        help="指定已有的 IndexNow API Key（不指定则自动生成新密钥）",
    )
    parser.add_argument(
        "--public-dir",
        type=str,
        default=str(PUBLIC_DIR),
        help=f"public 目录路径（默认：{PUBLIC_DIR}）",
    )
    return parser.parse_args()


def main() -> int:
    """主入口函数。"""
    print("=" * 70)
    print("IndexNow URL 批量提交脚本")
    print(f"目标站点：{SITE_BASE_URL}")
    print(f"API 端点：{INDEXNOW_API_URL}")
    print("=" * 70)

    args = parse_args()

    public_dir = Path(args.public_dir)
    if not public_dir.exists():
        print(f"✗ 错误：public 目录不存在：{public_dir}")
        print("  请先运行 `hugo --minify` 构建站点。")
        return 1

    # 1. 提取 URL
    print("\n[Step 1] 从 public/ 目录提取 URL...")
    try:
        urls = extract_urls_from_public(public_dir)
    except Exception as e:
        print(f"✗ URL 提取失败：{e}")
        return 1

    if not urls:
        print("✗ 警告：未发现任何 URL，请检查 public/ 目录是否包含 index.html 文件。")
        return 1

    # 应用 --limit
    if args.limit > 0 and args.limit < len(urls):
        print(f"[Step 1] 应用 --limit {args.limit}，截取前 {args.limit} 个 URL 用于测试")
        urls = urls[: args.limit]

    print(f"[Step 1] 最终待提交 URL 数量：{len(urls)}")

    # 2. 处理密钥
    print("\n[Step 2] 准备 IndexNow 密钥...")
    if args.key:
        key = args.key
        print(f"[Step 2] 使用指定密钥：{key}")
        # 简单校验密钥格式（应为 8~128 位的十六进制或含连字符）
        valid_chars = set("0123456789abcdefABCDEF-")
        if not (8 <= len(key) <= 128) or not all(c in valid_chars for c in key):
            print("  ⚠ 警告：密钥格式不符合 IndexNow 规范（建议 16~32 位十六进制）")
    else:
        key = generate_indexnow_key()
        print(f"[Step 2] 已生成新密钥：{key}")

    # 创建/校验密钥文件
    try:
        key_file = ensure_key_file(public_dir, key)
        print(f"[Step 2] 密钥文件路径：{key_file}")
        print(f"[Step 2] 密钥文件 URL：https://{SITE_HOST}/{key}.txt")
        print(f"         （部署后必须可通过此 URL 访问，否则 IndexNow 会返回 422）")
    except Exception as e:
        print(f"✗ 密钥文件创建失败：{e}")
        return 1

    # 3. 提交
    print("\n[Step 3] 提交 URL 到 IndexNow API...")
    if args.dry_run:
        print("[Step 3] 【DRY-RUN 模式】不会实际调用 API\n")

    success_batches, failed_batches = submit_all_urls(urls, key, dry_run=args.dry_run)

    # 4. 汇总
    print("=" * 70)
    print("提交结果汇总")
    print("=" * 70)
    print(f"  总 URL 数：{len(urls)}")
    print(f"  成功批次：{success_batches}")
    print(f"  失败批次：{failed_batches}")
    if args.dry_run:
        print(f"  模式：DRY-RUN（未实际提交）")
    elif failed_batches == 0:
        print(f"  状态：✓ 全部成功")
    else:
        print(f"  状态：✗ 有 {failed_batches} 批失败，请检查上方日志")

    print("\n注意事项：")
    print(f"  1. 请确保密钥文件已部署：https://{SITE_HOST}/{key}.txt")
    print(f"  2. IndexNow 提交后通常 1~24 小时内 Bing/Yandex 开始抓取")
    print(f"  3. 可在 Bing Webmaster Tools 查看提交状态")
    print(f"  4. 同一 URL 24 小时内重复提交无意义，建议有内容更新时再提交")

    return 0 if (failed_batches == 0 or args.dry_run) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n[中断] 用户取消操作")
        sys.exit(130)
