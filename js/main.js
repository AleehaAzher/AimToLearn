const categories = [
  { name: 'Essays', count: 2, icon: 'bi-journal-text' },
  { name: 'Applications', count: 0, icon: 'bi-file-earmark-text' },
  { name: 'Letters', count: 0, icon: 'bi-envelope-paper' },
  { name: 'Grammar', count: 0, icon: 'bi-spellcheck' }
];

const renderCategories = () => {
  const container = document.getElementById('categories-grid');
  if (!container) return;

  const palette = ['category-card--blue', 'category-card--purple', 'category-card--amber', 'category-card--cyan'];

  container.innerHTML = categories
    .map((category, index) => `
      <div class="col-md-3 col-sm-6">
        <div class="category-card ${palette[index % palette.length]} p-4 h-100">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <div class="hero-icon"><i class="bi ${category.icon}"></i></div>
            <span class="badge-soft">${category.count} items</span>
          </div>
          <h3 class="h5 mb-2">${category.name}</h3>
          <p class="text-muted mb-0">Ready for future expansion and new educational content.</p>
        </div>
      </div>
    `)
    .join('');
};

const getEssayBadge = (essay) => {
  const updated = new Date(essay.lastUpdated);
  const isRecent = !Number.isNaN(updated.getTime()) && (Date.now() - updated.getTime()) <= 30 * 24 * 60 * 60 * 1000;

  if (essay.featured && isRecent) return 'Popular';
  if (essay.featured) return 'Popular';
  if (isRecent) return 'Recently Updated';
  return 'New';
};

const renderEssayCards = (items, targetId, showBadge = false) => {
  const container = document.getElementById(targetId);
  if (!container) return;

  container.innerHTML = items
    .map((essay) => `
      <div class="col-lg-4 col-md-6">
        <article class="essay-card h-100">
          <div class="essay-card-media">
            <img src="${essay.thumbnail}" loading="lazy" alt="${essay.title}" />
            <div class="essay-card-overlay">
              <span class="pill pill--primary">${essay.category}</span>
              ${showBadge ? `<span class="pill pill--neutral">${getEssayBadge(essay)}</span>` : `<span class="pill pill--neutral">${essay.readingTime}</span>`}
            </div>
          </div>
          <div class="card-body">
            <div class="essay-meta">
              <span><i class="bi bi-folder2-open me-1"></i>${essay.category}</span>
              <span><i class="bi bi-clock me-1"></i>${essay.readingTime}</span>
            </div>
            <h3 class="h5 mb-1">${essay.title}</h3>
            <p class="text-muted mb-2">${essay.description}</p>
            <div class="d-flex flex-wrap gap-2 mb-3">
              ${essay.keywords.slice(0, 3).map((keyword) => `<span class="badge-soft badge-soft--purple">${keyword}</span>`).join('')}
            </div>
            <a class="btn btn-outline-primary rounded-pill mt-auto" href="/essay.html?slug=${essay.slug}">Read more</a>
          </div>
        </article>
      </div>
    `)
    .join('');
};

const renderFeaturedEssays = () => {
  const featured = essaysData.filter((essay) => essay.featured).slice(0, 6);
  renderEssayCards(featured, 'featured-essays', true);
};

const renderEssaysPage = () => {
  const cardsContainer = document.getElementById('essayCards');
  const resultsSummary = document.getElementById('resultsSummary');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  const searchInput = document.getElementById('searchInput');
  const paginationContainer = document.getElementById('pagination');
  const clearFilters = document.getElementById('clearFilters');

  if (!cardsContainer || !resultsSummary) return;

  const perPage = 6;
  let currentPage = 1;
  let filteredEssays = [...essaysData];

  const populateCategories = () => {
    const categories = [...new Set(essaysData.map((essay) => essay.category))];
    categoryFilter.innerHTML = '<option value="all">All categories</option>' + categories.map((category) => `<option value="${category}">${category}</option>`).join('');
  };

  const applyFilters = () => {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedCategory = categoryFilter.value;
    const selectedDifficulty = difficultyFilter.value;

    filteredEssays = essaysData.filter((essay) => {
      const matchesSearch = [essay.title, essay.description, essay.category, ...essay.keywords].join(' ').toLowerCase().includes(searchTerm);
      const matchesCategory = selectedCategory === 'all' || essay.category === selectedCategory;
      const matchesDifficulty = selectedDifficulty === 'all' || essay.difficulty === selectedDifficulty;
      return matchesSearch && matchesCategory && matchesDifficulty;
    });

    currentPage = 1;
    renderPage();
  };

  const renderPage = () => {
    const totalPages = Math.max(1, Math.ceil(filteredEssays.length / perPage));
    const start = (currentPage - 1) * perPage;
    const visible = filteredEssays.slice(start, start + perPage);

    cardsContainer.innerHTML = visible.length
      ? visible.map((essay) => `
          <div class="col-lg-4 col-md-6">
            <article class="essay-card h-100">
              <div class="essay-card-media">
                <img src="${essay.thumbnail}" loading="lazy" alt="${essay.title}" />
                <div class="essay-card-overlay">
                  <span class="pill pill--primary">${essay.category}</span>
                  <span class="pill pill--neutral">${essay.readingTime}</span>
                </div>
              </div>
              <div class="card-body">
                <div class="essay-meta">
                  <span><i class="bi bi-folder2-open me-1"></i>${essay.category}</span>
                  <span><i class="bi bi-clock me-1"></i>${essay.readingTime}</span>
                </div>
                <h3 class="h5 mb-1">${essay.title}</h3>
                <p class="text-muted mb-2">${essay.description}</p>
                <div class="d-flex flex-wrap gap-2 mb-3">
                  ${essay.keywords.slice(0, 3).map((keyword) => `<span class="badge-soft badge-soft--purple">${keyword}</span>`).join('')}
                </div>
                <a class="btn btn-outline-primary rounded-pill mt-auto" href="/essay.html?slug=${essay.slug}">Read more</a>
              </div>
            </article>
          </div>
        `).join('')
      : '<div class="col-12"><div class="alert alert-light">No essays match the selected filters.</div></div>';

    resultsSummary.innerHTML = `${filteredEssays.length} result${filteredEssays.length === 1 ? '' : 's'} found`;

    const pages = [];
    for (let page = 1; page <= totalPages; page += 1) {
      pages.push(`<li class="page-item ${page === currentPage ? 'active' : ''}"><button class="page-link" data-page="${page}">${page}</button></li>`);
    }
    paginationContainer.innerHTML = pages.join('');
  };

  paginationContainer.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-page]');
    if (!button) return;
    currentPage = Number(button.dataset.page);
    renderPage();
  });

  [searchInput, categoryFilter, difficultyFilter].forEach((element) => {
    if (element) element.addEventListener('input', applyFilters);
    if (element) element.addEventListener('change', applyFilters);
  });

  if (clearFilters) {
    clearFilters.addEventListener('click', () => {
      searchInput.value = '';
      categoryFilter.value = 'all';
      difficultyFilter.value = 'all';
      applyFilters();
    });
  }

  populateCategories();
  renderPage();
};

const renderEssayDetail = () => {
  const container = document.getElementById('essayContent');
  if (!container) return;

  const params = new URLSearchParams(window.location.search);
  const slug = params.get('slug');
  const essay = essaysData.find((item) => item.slug === slug);

  if (!essay) {
    container.innerHTML = '<div class="alert alert-warning">Essay not found.</div>';
    return;
  }

  const related = essaysData.filter((item) => item.slug !== essay.slug).slice(0, 2);

  document.title = `${essay.title} | AIM TO LEARN`;
  const canonical = document.querySelector('link[rel="canonical"]');
  if (canonical) canonical.href = `https://aimtolearn.netlify.app/essay.html?slug=${essay.slug}`;

  // Add Breadcrumb JSON-LD
  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://aimtolearn.netlify.app/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Essays",
        "item": "https://aimtolearn.netlify.app/essays.html"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": essay.title,
        "item": `https://aimtolearn.netlify.app/essay.html?slug=${essay.slug}`
      }
    ]
  };

  // Add Article JSON-LD
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": essay.title,
    "description": essay.description,
    "image": essay.thumbnail,
    "author": {
      "@type": "Organization",
      "name": essay.author
    },
    "datePublished": essay.lastUpdated,
    "dateModified": essay.lastUpdated,
    "keywords": essay.keywords.join(", "),
    "url": `https://aimtolearn.netlify.app/essay.html?slug=${essay.slug}`
  };

  const schemaScript = document.getElementById('essaySchema');
  if (schemaScript) {
    schemaScript.textContent = JSON.stringify(articleSchema);
  }

  container.innerHTML = `
    <script type="application/ld+json">
      ${JSON.stringify(breadcrumbSchema)}
    </script>

    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="/index.html">Home</a></li>
        <li class="breadcrumb-item"><a href="/essays.html">Essays</a></li>
        <li class="breadcrumb-item active" aria-current="page">${essay.title}</li>
      </ol>
    </nav>

    <div class="row g-4">
      <div class="col-lg-8">
        <div class="card p-4 shadow-sm border-0">
          <div class="badge-soft mb-3">${essay.category}</div>
          <h1 class="h2 fw-bold mb-3">${essay.title}</h1>
          <p class="text-muted lead">${essay.description}</p>
          <div class="essay-meta mb-4">
            <span><i class="bi bi-person me-1" aria-hidden="true"></i><span aria-label="Author">By ${essay.author}</span></span>
            <span><i class="bi bi-clock me-1" aria-hidden="true"></i><span aria-label="Reading time">${essay.readingTime}</span></span>
            <span><i class="bi bi-calendar3 me-1" aria-hidden="true"></i><span aria-label="Last updated">${essay.lastUpdated}</span></span>
            <span><i class="bi bi-bar-chart me-1" aria-hidden="true"></i><span aria-label="Difficulty level">${essay.difficulty}</span></span>
          </div>
          <div class="d-flex flex-wrap gap-3 mb-4">
            <a class="btn btn-primary rounded-pill" href="${essay.pdf}" download aria-label="Download essay as PDF">Download PDF</a>
          </div>
          <div class="border-top pt-4">
            <h2 class="h5 mb-3">Why this essay matters</h2>
            <p class="text-muted mb-0">This page is intentionally optimized for preview and download flows. The full essay content can be added later in a document-friendly format without changing the site structure.</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card p-4 shadow-sm border-0 mb-4">
          <h2 class="h5 mb-3">Related essays</h2>
          <div class="d-grid gap-3">
            ${related.map((item) => `
              <a class="card p-3 border-0 bg-light" href="/essay.html?slug=${item.slug}" aria-label="Related essay: ${item.title}">
                <h3 class="h6 mb-1">${item.title}</h3>
                <p class="text-muted small mb-0">${item.description}</p>
              </a>
            `).join('')}
          </div>
        </div>
        <div class="card p-4 shadow-sm border-0">
          <h2 class="h5 mb-3">Keywords</h2>
          <div class="d-flex flex-wrap gap-2" role="list">
            ${essay.keywords.map((keyword) => `<span class="badge-soft" role="listitem">${keyword}</span>`).join('')}
          </div>
        </div>
      </div>
    </div>
  `;
};

document.addEventListener('DOMContentLoaded', () => {
  renderCategories();
  renderFeaturedEssays();
  renderEssaysPage();
  renderEssayDetail();
});
