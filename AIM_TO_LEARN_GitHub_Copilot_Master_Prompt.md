# AIM TO LEARN -- Master GitHub Copilot Project Prompt

You are a senior UI/UX designer, front-end architect, SEO specialist,
and JavaScript developer.

## Objective

Build a **production-ready educational platform** called **AIM TO
LEARN**. It must be a **100% static website** deployable on **Netlify**
with no backend.

## Tech Stack

-   HTML5
-   CSS3
-   Bootstrap 5
-   Vanilla JavaScript (ES6)
-   Bootstrap Icons
-   Google Fonts

Do **not** use React, Vue, Angular, Next.js, ASP.NET, Node.js, Express,
Python, PHP, SQL, MongoDB, Firebase, authentication, APIs, or
server-side rendering.

## Vision

The platform starts with English Essays but must be architected to later
support: - Essays - Applications - Letters - Stories - Paragraphs -
Grammar - Notes - Computer Science - AI - Cloud Computing - Career
Guides - Research Papers - Downloads

Use a component-based architecture so new content can be added by
editing data files only.

## Design

Premium SaaS look inspired by Stripe, Vercel, GitHub, Notion, and
Coursera.

Requirements: - Clean, modern UI - White/light theme with optional dark
mode - Rounded cards - Glassmorphism where appropriate - Responsive -
Accessible - Fast loading - Mobile first - Smooth animations - Sticky
navbar - Professional typography

## Folder Structure

    /
    ├── index.html
    ├── essays.html
    ├── essay.html
    ├── 404.html
    ├── sitemap.xml
    ├── robots.txt
    ├── manifest.json
    ├── favicon.ico
    ├── css/
    ├── js/
    ├── data/
    │   └── essays.js
    ├── downloads/
    ├── images/
    ├── assets/
    └── components/

## Routing

Never create separate HTML pages for every essay.

Instead use:

`essay.html?slug=my-best-friend`

Load all content dynamically from `data/essays.js`.

Adding a new essay must require only: 1. Add one object to
`data/essays.js` 2. Place PDF/DOCX inside `/downloads` 3. Add thumbnail
if desired

No HTML edits.

## Data Model

``` javascript
{
 id:1,
 title:"",
 slug:"",
 category:"",
 description:"",
 author:"",
 readingTime:"",
 featured:true,
 quotations:true,
 difficulty:"",
 lastUpdated:"",
 thumbnail:"",
 pdf:"",
 docx:"",
 keywords:[]
}
```

## Pages

### Home

-   Hero
-   Categories dashboard
-   Popular Essays
-   Latest Uploads
-   Statistics
-   FAQ
-   CTA
-   Footer

### Essays

-   Dynamic cards
-   Search
-   Filters
-   Pagination

### Essay Page

Display: - Title - Description - Reading time - Category - Last
updated - Breadcrumb - Related essays - Download PDF - Download DOCX

Do **not** display the full essay.

## Initial Essays

-   My Best Friend Essay
-   Television Essay

## Search

Search title, description, category, and keywords.

## Downloads

Downloads point directly to static files in `/downloads`.

## Branding

Use placeholders: - logo.png - watermark.png

Documents will later contain a centered watermark (\~10% opacity) plus
footer: - © AIM TO LEARN - Website - YouTube - Page number

## SEO

Include: - Meta tags - Open Graph - Twitter Cards - Canonical URL -
JSON-LD - Breadcrumb Schema - Semantic HTML

## Performance

-   Lazy loading
-   Optimized assets
-   Core Web Vitals
-   Minimal JavaScript

## Accessibility

-   ARIA labels
-   Keyboard navigation
-   Proper contrast
-   Alt text

## Code Quality

-   Modular
-   Reusable
-   Commented
-   DRY
-   Maintainable

## Future Ready

Structure the project so an admin panel or backend can be integrated
later without redesigning the UI.

## Final Deliverable

Produce a complete production-ready Netlify project with: - Professional
SaaS UI - Dynamic routing - Dynamic data model - Search & filters - Dark
mode - Related essays - Breadcrumbs - 404 page - Responsive design -
SEO - Reusable components - Clean architecture - Easy scalability
