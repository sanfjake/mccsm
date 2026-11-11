# Mini-Cassia Chiropractic & Sports Medicine — Website

This repository contains the public-facing **static clinic website** for Mini-Cassia Chiropractic & Sports Medicine, located at **518 Oneida Street, Rupert, Idaho 83350**.

## Current project status

- The redesigned ten-page website (navy/gold/white design, circular doctor portrait and authentic clinic photos) was merged into **`main`** through pull request #1 on **November 11, 2026**.
- **`main` is the current GitHub source**, but updating GitHub does not by itself prove that the public domain is serving these files. The owner uses GoDaddy; confirm whether GoDaddy is providing only the domain registration or also the actual web hosting before changing deployment settings.
- No DNS or GitHub Pages settings should be changed without first establishing the active hosting/deployment arrangement.
- A branded `404.html` is included. Hosting environments differ in how they serve custom 404 pages.

## Pages

Home (`/`), About (`/about/`), Services (`/services/`), Contact (`/contact/`), Areas We Serve (`/areas-we-serve/`), Rupert, Burley, Heyburn, Paul (all under `/areas-we-serve/`), and Website Privacy (`/privacy/`). There is **one physical clinic in Rupert**; the other cities are communities whose residents may visit that location.

## Contact and office hours

- **Call or text:** (208) 260-0917. Texting is the preferred contact method for general questions and scheduling. If a call goes unanswered while the doctor is assisting a patient, leave a voicemail.
- **Monday, Wednesday, Friday:** 10:00 AM–5:00 PM.
- **Tuesday, Thursday, Saturday:** by appointment only.
- **Sunday:** not specified by the owner; do not assume public hours.
- Text messages and voicemail do **not** confirm appointments. Patients should not send sensitive medical details over ordinary SMS, email or voicemail.

## Technology and layout

The site uses plain HTML, CSS and JavaScript with **no build process or third-party runtime framework**. Assets are in `assets/` and optimized clinic photographs use WebP. The family's photograph is intentionally not included. Standard navigation is based on actual URLs, not JavaScript-only page switching.

The site includes page-specific titles, descriptions, canonical URLs, structured business data, `robots.txt` and `sitemap.xml`. Appointment-only days are described in visible text rather than incorrectly represented as regular open hours in structured data.

## Checking changes

Run the dependency-free validation script from the repository root:

```bash
python3 scripts/check_site.py
```

This checks the ten pages, local links and images, SEO titles and canonical URLs, structured opening hours, sitemap, and the custom 404 page. A GitHub Actions workflow runs the same check for pushes and pull requests involving `main`.

To preview a local working copy, open the repository in VS Code. A local server is **optional** when you are evaluating the public website, but helpful for reviewing changes before deployment:

```bash
python3 -m http.server 8000
```

For GitHub Desktop: choose the `mccsm` repository, switch to `main`, select **Fetch origin** / **Pull origin** as applicable, then **Repository → Open in Visual Studio Code**.

## Required owner review before considering the public site finalized

1. Verify the exact physical address, published services and scope of care, prices if any, and photographs.
2. Test the text and call links on a real phone, and confirm how voicemail and patient communications are handled.
3. Review the **Website Privacy** page against the real hosting, analytics and messaging arrangements. It is a draft **and is not the clinic's full HIPAA Notice of Privacy Practices**.
4. Check mobile display, keyboard accessibility, page performance, and content accuracy on the actual public domain.
5. Check the live hosting/deployment source rather than assuming a GitHub merge updates a GoDaddy-hosted site.

For historical project context, see `PHASE1_STATUS.md`.