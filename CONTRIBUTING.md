# Contributing to AIM TO LEARN

Thank you for wanting to contribute! This guide explains how to add essays, fix bugs, and improve the platform.

## For Content Creators: Adding Essays

### Quick Start

**To add a new essay, you only need to:**

1. Open `data/essays.js`
2. Add a new object to the `essaysData` array
3. Upload PDF and DOCX files
4. Done! ✅

### Step-by-Step Example

#### 1. Add to `data/essays.js`

```javascript
{
  id: 3,
  title: "The Impact of Technology on Society",
  slug: "technology-society",
  category: "Essays",
  description: "Exploring how technology shapes our daily lives, communication, and future.",
  author: "AIM TO LEARN",
  readingTime: "7 min read",
  featured: false,
  quotations: true,
  difficulty: "Intermediate",
  lastUpdated: "2026-07-15",
  thumbnail: "/images/technology-placeholder.svg",
  pdf: "/downloads/technology-society.pdf",
  docx: "/downloads/technology-society.docx",
  keywords: ["technology", "society", "innovation", "digital", "future"]
}
```

#### 2. Required Fields

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `id` | number | Yes | `3` |
| `title` | string | Yes | "The Impact of Technology on Society" |
| `slug` | string | Yes | `technology-society` (no spaces, hyphens ok) |
| `category` | string | Yes | `Essays` |
| `description` | string | Yes | Brief 1-2 sentence summary |
| `author` | string | Yes | `AIM TO LEARN` |
| `readingTime` | string | Yes | `"7 min read"` |
| `featured` | boolean | Yes | `true` or `false` |
| `quotations` | boolean | Yes | `true` if essay contains quotes |
| `difficulty` | string | Yes | `Beginner`, `Intermediate`, `Advanced` |
| `lastUpdated` | string | Yes | `"2026-07-15"` (YYYY-MM-DD) |
| `thumbnail` | string | Yes | `/images/your-image.svg` |
| `pdf` | string | Yes | `/downloads/your-essay.pdf` |
| `docx` | string | Yes | `/downloads/your-essay.docx` |
| `keywords` | array | Yes | `["word1", "word2", "word3"]` |

#### 3. Upload Files

Create two files in `/downloads/`:
- `technology-society.pdf` - Essay PDF
- `technology-society.docx` - Essay DOCX

#### 4. Add Thumbnail (Optional)

Add an image to `/images/`:
- `technology-society.svg` - Recommended (SVG format)
- Or use existing placeholder: `/images/essay-placeholder.svg`

#### 5. Update Sitemap (Optional)

Add to `sitemap.xml`:
```xml
<url>
  <loc>https://aimtolearn.netlify.app/essay.html?slug=technology-society</loc>
  <lastmod>2026-07-15</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

#### 6. Commit & Push

```bash
git add data/essays.js downloads/ images/
git commit -m "Add essay: The Impact of Technology on Society"
git push origin main
```

Site updates automatically! 🎉

## For Developers: Code Contributions

### Reporting Issues

Create a GitHub issue with:
- **Title**: Clear, concise description
- **Description**: Steps to reproduce
- **Screenshots**: If UI-related
- **Browser/OS**: Your environment

### Suggesting Features

Open a discussion with:
- Use case/problem
- Proposed solution
- Benefits to users
- Examples if relevant

### Code Contribution Process

1. **Fork** the repository
2. **Create branch**: `git checkout -b feature/your-feature`
3. **Make changes**: Follow code style below
4. **Test**: Verify in all browsers
5. **Commit**: `git commit -m "Add: [clear description]"`
6. **Push**: `git push origin feature/your-feature`
7. **Pull Request**: Provide description and context

### Code Style

#### HTML
- Use semantic tags (`<article>`, `<nav>`, `<main>`)
- Include `alt` text on all images
- Add `aria-label` for interactive elements
- Validate with [W3C](https://validator.w3.org/)

#### CSS
- Use existing CSS variables for colors
- Follow mobile-first approach
- Group related rules
- Add comments for complex sections
- Test dark mode

#### JavaScript
- Use vanilla ES6+ (no frameworks)
- Avoid global variables
- Comment non-obvious logic
- Test in Chrome, Firefox, Safari, Edge
- Keep functions under 50 lines when possible

### Testing Checklist

Before submitting PR, verify:

- ✅ No JavaScript errors (F12 console)
- ✅ Works on mobile (responsive)
- ✅ Dark mode toggle works
- ✅ Search/filters work correctly
- ✅ All links are valid
- ✅ Images load properly
- ✅ 404 page displays
- ✅ Keyboard navigation works
- ✅ Print layout looks good

### Browser Support

Must work on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari (iOS 14+)
- Chrome Mobile

## Adding New Content Types

### Architecture for New Categories

To add support for "Applications" essays:

#### 1. Create Data File

`data/applications.js`:
```javascript
const applicationsData = [
  {
    id: 1,
    title: "University Application Essay",
    slug: "university-application",
    // ... same structure as essays
  }
];
```

#### 2. Create Page

`applications.html`:
```html
<!-- Copy structure from essays.html -->
<!-- Change main container ID to #applicationCards -->
<!-- Change script src to /data/applications.js -->
```

#### 3. Create Component

In `js/main.js`, add:
```javascript
const renderApplicationsPage = () => {
  // Same logic as renderEssaysPage
  // Filter by applications data
};
```

#### 4. Update Navigation

In `js/components.js`:
```javascript
<li class="nav-item"><a class="nav-link" href="/applications.html">Applications</a></li>
```

#### 5. Deploy!

No other changes needed. The data-driven approach handles everything.

## Documentation

### For Changes
- Update relevant docs (README.md, DEPLOYMENT.md)
- Add comments to complex code
- Update this CONTRIBUTING.md if process changed

### For New Features
- Add to README.md features section
- Create example in comments
- Document in DEPLOYMENT.md if deployment-related

## Git Workflow

### Branch Naming
- `feature/short-description` - New features
- `fix/short-description` - Bug fixes
- `docs/short-description` - Documentation
- `style/short-description` - Code formatting

### Commit Messages
```
Type: Brief description

Detailed explanation of changes if needed.
Fixes #123 (if fixing issue)
```

Examples:
- ✅ `feat: Add dark mode toggle`
- ✅ `fix: Correct essay search pagination`
- ✅ `docs: Update deployment guide`
- ❌ `updates` (too vague)

## Performance Guidelines

When adding new features:

- ⚡ No render-blocking resources
- 📦 Minimize bundle size
- 🖼️ Lazy-load images
- 🎯 Defer non-critical CSS/JS
- 📱 Mobile-first responsive design
- 🔍 Maintain SEO best practices

## Accessibility Guidelines

All changes must:

- ♿ Pass WCAG 2.1 AA standards
- ⌨️ Support keyboard navigation
- 🎨 Have proper color contrast (7:1)
- 📝 Include ARIA labels where needed
- 🏷️ Use semantic HTML
- 🖥️ Work with screen readers

Test with:
- Keyboard only (no mouse)
- High contrast mode
- Screen reader (NVDA, JAWS)
- Mobile accessibility (VoiceOver, TalkBack)

## Review Process

Pull requests are reviewed for:

1. ✅ Code quality
2. ✅ Performance impact
3. ✅ Accessibility compliance
4. ✅ Browser compatibility
5. ✅ SEO impact
6. ✅ Documentation updates
7. ✅ Testing coverage

## Questions?

- Check README.md
- Review existing code
- Open an issue for discussion
- Comment on relevant PRs

## Code of Conduct

Be respectful, inclusive, and constructive. All contributors are valued! 🌟

---

**Thank you for making AIM TO LEARN better!** 💙
