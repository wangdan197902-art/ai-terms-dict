/**
 * Fuse.js 客户端搜索逻辑
 * 工作流程：
 * 1. 用户首次输入时，异步加载当前语种的 index.json
 * 2. JSON 加载后初始化 Fuse 实例
 * 3. localStorage 缓存 24 小时，避免重复请求
 * 4. 输入防抖 200ms，避免频繁搜索
 */
(function() {
  'use strict';

  const DEBOUNCE_MS = 200;
  const MAX_RESULTS = 20;
  const FUSE_THRESHOLD = 0.3;
  const CACHE_HOURS = 24;
  const CACHE_KEY_PREFIX = 'fuse_data_';
  const CACHE_TIME_KEY = 'fuse_data_time_';

  let fuseInstance = null;
  let isLoading = false;
  let dataLoaded = false;
  let debounceTimer = null;

  const searchInput = document.getElementById('search-input');
  const searchClear = document.getElementById('search-clear');
  const searchResults = document.getElementById('search-results');

  if (!searchInput) return;

  function getCurrentLang() {
    const path = window.location.pathname;
    const match = path.match(/^\/([a-z]{2})\//i);
    if (match) return match[1];
    return 'en';
  }

  function getJsonUrl(lang) {
    return `/${lang}/index.json`;
  }

  async function loadData(lang) {
    const cacheKey = CACHE_KEY_PREFIX + lang;
    const cacheTimeKey = CACHE_TIME_KEY + lang;
    const cachedTime = localStorage.getItem(cacheTimeKey);
    const now = Date.now();

    if (cachedTime && (now - parseInt(cachedTime)) < CACHE_HOURS * 60 * 60 * 1000) {
      const cachedData = localStorage.getItem(cacheKey);
      if (cachedData) {
        try {
          return JSON.parse(cachedData);
        } catch (e) {
          console.warn('Cache parse error, refetching');
        }
      }
    }

    const response = await fetch(getJsonUrl(lang));
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();

    try {
      localStorage.setItem(cacheKey, JSON.stringify(data));
      localStorage.setItem(cacheTimeKey, now.toString());
    } catch (e) {
      console.warn('LocalStorage save failed:', e);
    }

    return data;
  }

  async function ensureDataLoaded() {
    if (dataLoaded && fuseInstance) return;
    if (isLoading) return;

    isLoading = true;
    const lang = getCurrentLang();

    try {
      const data = await loadData(lang);
      fuseInstance = new Fuse(data.terms || [], {
        keys: [
          { name: 'title', weight: 0.4 },
          { name: 'summary', weight: 0.3 },
          { name: 'content', weight: 0.2 },
          { name: 'categories', weight: 0.1 }
        ],
        threshold: FUSE_THRESHOLD,
        includeScore: true,
        minMatchCharLength: 2,
        ignoreLocation: true,
      });
      dataLoaded = true;
    } catch (error) {
      console.error('Failed to load search data:', error);
      if (searchResults) {
        searchResults.innerHTML = '<div class="search-error">Failed to load search data</div>';
      }
    } finally {
      isLoading = false;
    }
  }

  function renderResults(results) {
    if (!searchResults) return;

    if (!results || results.length === 0) {
      searchResults.innerHTML = '<div class="search-no-results">No results found</div>';
      searchResults.style.display = 'block';
      return;
    }

    const html = results.slice(0, MAX_RESULTS).map(result => {
      const item = result.item;
      const title = item.title || 'Untitled';
      const summary = item.summary || '';
      const permalink = item.permalink || '#';
      return `<a href="${permalink}" class="search-result-item">
        <div class="search-result-title">${title}</div>
        <div class="search-result-summary">${summary}</div>
      </a>`;
    }).join('');

    searchResults.innerHTML = html;
    searchResults.style.display = 'block';
  }

  function handleInput() {
    const query = searchInput.value.trim();

    if (!query) {
      if (searchResults) {
        searchResults.style.display = 'none';
        searchResults.innerHTML = '';
      }
      return;
    }

    if (query.length < 2) {
      if (searchResults) {
        searchResults.style.display = 'none';
      }
      return;
    }

    ensureDataLoaded().then(() => {
      if (fuseInstance) {
        const results = fuseInstance.search(query);
        renderResults(results);
      }
    });
  }

  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(handleInput, DEBOUNCE_MS);
  });

  if (searchClear) {
    searchClear.addEventListener('click', () => {
      searchInput.value = '';
      if (searchResults) {
        searchResults.style.display = 'none';
        searchResults.innerHTML = '';
      }
      searchInput.focus();
    });
  }

  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && searchResults && !searchResults.contains(e.target)) {
      searchResults.style.display = 'none';
    }
  });

  searchInput.addEventListener('focus', () => {
    if (searchInput.value.trim().length >= 2 && searchResults) {
      searchResults.style.display = 'block';
    }
  });
})();
