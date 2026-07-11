const siteNav = document.getElementById('site-nav');
const siteFooter = document.getElementById('site-footer');

if (siteNav) {
  siteNav.innerHTML = `
    <nav class="navbar navbar-expand-lg sticky-top" aria-label="Primary navigation">
      <div class="container">
        <a class="navbar-brand fw-bold d-flex align-items-center gap-2" href="/index.html">
          <img src="/images/aimtolearnlogo.jpeg" alt="AIM TO LEARN logo" class="navbar-logo rounded-circle" width="40" height="40" onerror="this.style.display='none'" />
          <span>AIM TO LEARN</span>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="mainNav">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0 gap-lg-3">
            <li class="nav-item"><a class="nav-link" href="/index.html">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/essays.html">Essays</a></li>
            <li class="nav-item"><a class="nav-link" href="/privacy.html">Privacy</a></li>
            <li class="nav-item"><a class="nav-link" href="/terms.html">Terms</a></li>
            <li class="nav-item"><a class="nav-link" href="/index.html#faq">FAQ</a></li>
          </ul>
          <button id="themeToggle" class="btn btn-outline-secondary rounded-pill ms-lg-3" type="button" aria-label="Toggle dark mode">
            <i class="bi bi-moon-fill"></i>
          </button>
        </div>
      </div>
    </nav>
  `;
}

if (siteFooter) {
  siteFooter.innerHTML = `
    <footer class="py-5 border-top mt-5" role="contentinfo">
      <div class="container">
        <div class="row g-4 mb-4">
          <div class="col-md-4">
            <div class="d-flex align-items-center gap-2 mb-3">
              <img src="/images/aimtolearnlogo.jpeg" alt="AIM TO LEARN logo" class="footer-logo rounded-circle" width="40" height="40" onerror="this.style.display='none'" />
              <strong class="text-dark mb-0">AIM TO LEARN</strong>
            </div>
            <p class="text-muted small mb-0">Helpful essays and study materials for students, parents, and teachers.</p>
          </div>
          <div class="col-md-4">
            <h3 class="h6 mb-3">Navigation</h3>
            <nav aria-label="Footer links">
              <ul class="list-unstyled gap-2 d-flex flex-column text-muted small">
                <li><a href="/index.html">Home</a></li>
                <li><a href="/essays.html">Essays</a></li>
                <li><a href="/privacy.html">Privacy Policy</a></li>
                <li><a href="/terms.html">Terms & Conditions</a></li>
                <li><a href="/index.html#faq">FAQ</a></li>
              </ul>
            </nav>
          </div>
          <div class="col-md-4">
            <h3 class="h6 mb-3">Useful links</h3>
            <nav aria-label="Useful links">
              <ul class="list-unstyled gap-2 d-flex flex-column text-muted small">
                <li><a href="/index.html#about">About</a></li>
                <li><a href="/index.html#contact">Contact</a></li>
                <li><a href="/index.html#faq">FAQ</a></li>
              </ul>
            </nav>
          </div>
        </div>
        <hr class="my-3" />
        <div class="d-flex flex-column flex-md-row justify-content-between gap-3 text-muted small">
          <div>© 2026 AIM TO LEARN. All rights reserved.</div>
          <div>Free study resources for everyday learning</div>
        </div>
      </div>
    </footer>
  `;
}

const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
  const getStoredTheme = () => localStorage.getItem('aim-theme') || 'light';
  const applyTheme = (theme) => {
    document.documentElement.setAttribute('data-bs-theme', theme);
    localStorage.setItem('aim-theme', theme);
    const icon = themeToggle.querySelector('i');
    if (icon) {
      icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
    }
  };

  applyTheme(getStoredTheme());
  themeToggle.addEventListener('click', () => {
    const nextTheme = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
  });
}
