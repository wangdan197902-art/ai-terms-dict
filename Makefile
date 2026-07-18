.PHONY: serve build clean init generate generate-batch translate translate-batch validate content mock-content search-index all full-pipeline config-check health-check test-agnes preview stop

# ============================================
# AI Terms Dictionary - Makefile
# 全链路自动化：generate → translate → validate → content → build → search-index
# ============================================

PYTHON ?= python3
HUGO ?= hugo
PAGEFIND ?= pagefind
PORT ?= 1313

# 默认目标：全链路构建（不含serve）
all: full-pipeline
	@echo ""
	@echo "========================================"
	@echo "✓ 全链路完成"
	@echo "========================================"
	@echo "预览: make preview"
	@echo "URL:  http://localhost:$(PORT)/"
	@echo "========================================"

# ============================================
# Phase 0: 环境初始化
# ============================================

init:
	@echo "[1/4] 创建 Python 虚拟环境..."
	$(PYTHON) -m venv .venv
	@echo "[2/4] 安装 Python 依赖..."
	@.venv/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
	@echo "[3/4] 检查 Hugo..."
	@command -v $(HUGO) >/dev/null 2>&1 || { echo "✗ Hugo 未安装。请运行: brew install hugo"; exit 1; }
	@echo "[4/4] 检查 Pagefind..."
	@command -v $(PAGEFIND) >/dev/null 2>&1 || { echo "✗ Pagefind 未安装。请运行: npm install -g pagefind"; exit 1; }
	@echo "✓ 环境初始化完成"

config-check:
	@$(PYTHON) scripts/check_config.py

health-check:
	@bash scripts/health_check.sh

test-agnes:
	@$(PYTHON) scripts/test_agnes_connection.py

# ============================================
# Phase 1-2: AI内容生成（单术语 + 批量）
# ============================================

# 单术语生成（垂直切片验证用）
generate:
	@$(PYTHON) scripts/generate_definitions.py

# 批量生成定义（20术语×1次API调用×5批次）
generate-batch:
	@$(PYTHON) scripts/generate_definitions_batch.py

# 单术语翻译
translate:
	@$(PYTHON) scripts/translate.py

# 批量翻译（20术语×5语种=100翻译）
translate-batch:
	@$(PYTHON) scripts/translate_batch.py

# ============================================
# Phase 2: 数据校验
# ============================================

validate:
	@$(PYTHON) scripts/validate.py

# ============================================
# Phase 2-3: 内容构建（JSON → Markdown）
# ============================================

# 构建真实AI内容（20术语×6语种）
content:
	@$(PYTHON) scripts/build_content.py

# 构建Mock内容（180术语×6语种，status=preview）
mock-content:
	@$(PYTHON) scripts/build_mock_content.py

# ============================================
# Phase 4: 站点构建 + 搜索索引
# ============================================

# 构建静态站点
build:
	@echo "构建 Hugo 静态站点..."
	$(HUGO) --gc --quiet
	@echo "✓ Hugo 构建完成: $$(find public -name '*.html' | wc -l | tr -d ' ') 页面"

# 构建Pagefind搜索索引
search-index:
	@echo "构建 Pagefind 搜索索引..."
	$(PAGEFIND) --site public/ 2>&1 | grep -E "Indexed|Finished|Error" || true
	@echo "✓ 搜索索引完成"

# ============================================
# Phase 5: 全链路一键执行
# ============================================

# 完整全链路（真实AI内容）
full-pipeline: generate-batch translate-batch validate content build search-index
	@echo "✓ 全链路（真实内容）完成"

# Mock全链路（无需API，快速预览）
mock-pipeline: mock-content build search-index
	@echo "✓ 全链路（Mock内容）完成"

# ============================================
# 开发服务器
# ============================================

# 启动预览服务器
serve:
	$(HUGO) server --bind 0.0.0.0 --port $(PORT) --buildDrafts --disableFastRender

# 构建并预览
preview: build search-index serve

# 停止运行中的Hugo server
stop:
	@pkill -f "hugo server" 2>/dev/null || true
	@echo "✓ 已停止 Hugo server"

# ============================================
# 清理
# ============================================

clean:
	rm -rf public resources .hugo_build.lock
	@echo "✓ 已清理构建产物"

clean-cache:
	rm -rf .cache/agnes/
	@echo "✓ 已清理API缓存"
