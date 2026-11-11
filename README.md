# Mini-Cassia Chiropractic & Sports Medicine — Website redesign

**Development-only:** This site is intended for review in the GitHub `feature/clinic-site-redesign` branch. Do not merge into `main` or publish until the clinic approves it. 

## What's included

- Full responsive multi-page, no-build HTML/CSS/JS website, matching the navy/gold/white design.
- Four actual clinic photos (entrance, reception, treatment space, doctor's portrait) supplied by the owner, optimized as WebP. Family photo deliberately excluded for privacy.
- Editable custom mountain SVG logo.
- Pages: Home, About, Services, Areas We Serve, Rupert, Burley, Heyburn, Paul, Contact, Website Privacy draft.
- Text and call actions to the owner-verified cell phone number (208) 260-0917.
- Enhanced About, Services, Contact, and all four service-area pages with practical, distinctive visitor guidance.
- Circular portrait styling carries from the approved homepage to About.
- Checked page-specific Open Graph images and links where applicable.
- Owner-confirmed hours: Monday, Wednesday, Friday 10:00 AM–5:00 PM; Tuesday, Thursday, Saturday by appointment only. Sunday hours have not been supplied.
- Actual Rupert location at 518 Oneida Street, with no false Burley/Heyburn/Paul locations.
- Per-page canonical URL, title, description, Open Graph metadata, actual-business structured data, `robots.txt` and `sitemap.xml`.
- Contact-first design with no unreviewed PHI intake form or fabricated patient reviews.

## Local preview

From this directory, run `python3 -m http.server 8000`, then visit http://localhost:8000/ . Open directly via a file browser in basic cases, but HTTP preview works more reliably for multi-page links.

## Still to confirm before launch

1. All current services and offered treatments are accurate and within scope.
2. Clinic address and entrance should be verified in person before launch. Office hours have been confirmed by the owner and added to the site; Sunday has not been specified.
3. SMS links work on an actual phone; general texts are not secure medical intake, and messages are not confirmed bookings.
4. The website privacy notice reflects actual hosting and communications practices. Clinic owner should review it before publishing; it is not a complete HIPAA Notice of Privacy Practices.
5. SEO city pages provide enough genuine value and are not doorway pages. Each clearly points to the one physical office in Rupert.
6. Accessibility, responsive layouts, forms (none), image cropping and text contrast pass review.
7. Public use of the supplied portrait and office photographs is authorized; no patient information appears in uploaded photos.

## Important GitHub Pages note

The live website currently serves the default branch. The feature branch must be reviewed and merged deliberately after testing. Do not change DNS or GitHub Pages settings as part of this work.

## Structure

- `index.html`
- `about/index.html`
- `services/index.html`
- `areas-we-serve/index.html`
- `areas-we-serve/rupert/index.html`
- `areas-we-serve/burley/index.html`
- `areas-we-serve/heyburn/index.html`
- `areas-we-serve/paul/index.html`
- `contact/index.html`
- `privacy/index.html`
- `assets/css/site.css`, `assets/js/site.js`
- `assets/brand/*.svg`, `favicon.svg`
- `assets/images/*.webp`
- `CNAME`, `robots.txt`, `sitemap.xml`
