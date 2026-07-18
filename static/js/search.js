// Pagefind Search UI Integration
// Loads Pagefind search index and renders results dynamically

let pagefindSearch = null;

async function loadPagefind() {
  if (pagefindSearch) return pagefindSearch;
  try {
    // Pagefind generates /pagefind/pagefind.js during build
    pagefindSearch = await import('/pagefind/pagefind.js');
    pagefindSearch.init();
    return pagefindSearch;
  } catch (e) {
    console.error('[Search] Failed to load Pagefind:', e);
    return null;
  }
}

function debounce(fn, wait) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), wait);
  };
}

function escapeHtml(s) {
  if (s == null) return '';
  return String(s).replace(/[&<>"']/g, (c) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

function renderResult(result, query) {
  const url = result.url || '#';
  const meta = result.meta || {};
  const title = meta.title || result.meta?.term || url;
  const termId = meta.term_id ? `<span class="search-term-id">${escapeHtml(meta.term_id)}</span>` : '';
  const category = meta.category ? `<span class="search-category">${escapeHtml(meta.category)}</span>` : '';
  const excerpt = result.excerpt
    ? `<div class="search-excerpt">${result.excerpt}</div>`
    : (meta.description ? `<div class="search-excerpt">${escapeHtml(meta.description)}</div>` : '');
  const lang = meta.lang ? `<span class="search-lang">${escapeHtml(meta.lang)}</span>` : '';

  return `
    <article class="search-result-item">
      <h3 class="search-result-title">
        <a href="${escapeHtml(url)}">${escapeHtml(title)}</a>
      </h3>
      <div class="search-result-meta">
        ${termId}${category}${lang}
      </div>
      ${excerpt}
    </article>`;
}

async function performSearch(query, resultsContainer) {
  const pf = await loadPagefind();
  if (!pf) {
    resultsContainer.innerHTML = '<p class="search-error">Search index unavailable. Please run <code>make search-index</code> first.</p>';
    return;
  }

  const trimmed = (query || '').trim();
  if (trimmed.length < 1) {
    resultsContainer.innerHTML = '';
    return;
  }

  resultsContainer.innerHTML = '<p class="search-loading">Searching...</p>';

  try {
    const search = await pf.search(trimmed);
    const total = search?.results?.length || 0;

    if (total === 0) {
      resultsContainer.innerHTML = `<p class="search-empty">No results found for "<strong>${escapeHtml(trimmed)}</strong>"</p>`;
      return;
    }

    // Limit to top 30 results for performance
    const top = search.results.slice(0, 30);
    const rendered = await Promise.all(top.map((r) => r.data()));
    const html = `<p class="search-count">${total} result${total === 1 ? '' : 's'} for "<strong>${escapeHtml(trimmed)}</strong>"</p>` +
      rendered.map((r) => renderResult(r, trimmed)).join('');
    resultsContainer.innerHTML = html;
  } catch (e) {
    console.error('[Search] query failed:', e);
    resultsContainer.innerHTML = '<p class="search-error">Search failed. Please try again.</p>';
  }
}

function initSearchPage() {
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  if (!input || !results) return;

  // Read ?q= from URL for deep linking
  const params = new URLSearchParams(window.location.search);
  const initialQuery = params.get('q') || '';
  if (initialQuery) {
    input.value = initialQuery;
    performSearch(initialQuery, results);
  }

  const debouncedSearch = debounce((q) => performSearch(q, results), 250);
  input.addEventListener('input', (e) => debouncedSearch(e.target.value));

  // Update URL on search without reloading
  input.addEventListener('input', (e) => {
    const q = e.target.value.trim();
    const newUrl = q
      ? `${window.location.pathname}?q=${encodeURIComponent(q)}`
      : window.location.pathname;
    window.history.replaceState({}, '', newUrl);
  });
}

function initHeaderSearchBox() {
  // Header search box: redirect to search page with ?q=
  const headerInput = document.querySelector('.site-header .search-box input');
  if (!headerInput) return;
  const lang = document.documentElement.lang || 'en';
  const searchPath = lang === 'en' ? '/en/search/' : `/${lang}/search/`;
  headerInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const q = headerInput.value.trim();
      if (q) {
        window.location.href = `${searchPath}?q=${encodeURIComponent(q)}`;
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initSearchPage();
  initHeaderSearchBox();
});
