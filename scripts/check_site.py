#!/usr/bin/env python3
"""Static checks for the Mini-Cassia Chiropractic website (no dependencies)."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://minicassiachiropractic.com"
PAGES = [
    "index.html", "about/index.html", "services/index.html",
    "contact/index.html", "areas-we-serve/index.html",
    "areas-we-serve/rupert/index.html", "areas-we-serve/burley/index.html",
    "areas-we-serve/heyburn/index.html", "areas-we-serve/paul/index.html",
    "privacy/index.html"
]
HOURS = {"Monday", "Wednesday", "Friday"}
LINKS = re.compile(r'\b(?:href|src)="([^"]+)"')
JSONLD = re.compile(r'<script\s+type="application/ld\+json">([\s\S]*?)</script>')
H1 = re.compile(r'<h1(?:\s[^>]*)?>', re.I)
IMG = re.compile(r'<img\b[^>]*>', re.I)
ALT = re.compile(r'\balt="[^"]*"', re.I)
TITLE = re.compile(r'<title>([\s\S]*?)</title>', re.I)
DESC = re.compile(r'<meta name="description" content="([^"]+)"', re.I)
CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)"', re.I)


def target_file(page, href):
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith("//"):
        return None
    if not parsed.path:
        return page
    path = unquote(parsed.path)
    target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
    if path.endswith("/") or target.is_dir():
        target /= "index.html"
    return target.resolve()


def main():
    errors, titles = [], set()
    for name in PAGES + ["404.html"]:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"{name}: missing page")
            continue
        html = path.read_text(encoding="utf-8")
        heading_count = len(H1.findall(html))
        if heading_count != 1:
            errors.append(f"{name}: {heading_count} H1 headings (expected 1)")
        for image in IMG.findall(html):
            if not ALT.search(image):
                errors.append(f"{name}: image missing alt text")
        for href in LINKS.findall(html):
            target = target_file(path, href)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{name}: link escapes website root: {href}")
                continue
            if not target.is_file():
                errors.append(f"{name}: broken link or asset: {href}")
            elif urlsplit(href).fragment and target.suffix == ".html":
                fragment = urlsplit(href).fragment
                if f'id="{fragment}"' not in target.read_text(encoding="utf-8"):
                    errors.append(f"{name}: missing anchor: {href}")
        if name == "404.html":
            if 'name="robots" content="noindex' not in html:
                errors.append("404.html: add noindex for search engines")
            continue
        title = TITLE.search(html)
        description = DESC.search(html)
        canonical = CANONICAL.search(html)
        expected = DOMAIN + "/" + name.removesuffix("index.html")
        if not title or not title.group(1).strip() or title.group(1) in titles:
            errors.append(f"{name}: missing or duplicate title")
        else:
            titles.add(title.group(1))
        if not description or len(description.group(1).strip()) < 35:
            errors.append(f"{name}: missing or short meta description")
        if not canonical or canonical.group(1) != expected:
            errors.append(f"{name}: incorrect canonical URL")
        if not all(x in html for x in [
            "Mon, Wed &amp; Fri: 10 AM–5 PM",
            "Tue, Thu &amp; Sat: By appointment only"
        ]):
            errors.append(f"{name}: office hours absent from footer")
        matches = JSONLD.findall(html)
        if not matches:
            errors.append(f"{name}: missing JSON-LD structured data")
        for match in matches:
            try:
                data = json.loads(match)
                if data.get("@type") == "MedicalBusiness":
                    specs = data.get("openingHoursSpecification", [])
                    if not any(set(x.get("dayOfWeek", [])) == HOURS
                               and x.get("opens") == "10:00"
                               and x.get("closes") == "17:00" for x in specs):
                        errors.append(f"{name}: regular structured hours mismatch")
            except (ValueError, AttributeError, TypeError) as err:
                errors.append(f"{name}: invalid JSON-LD: {err}")
    try:
        namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        root = ElementTree.parse(ROOT / "sitemap.xml").getroot()
        actual = {e.text for e in root.iter(namespace + "loc")}
        expected = {DOMAIN + "/" + x.removesuffix("index.html") for x in PAGES}
        if actual != expected:
            errors.append("sitemap.xml: URLs do not match the ten pages")
    except (ElementTree.ParseError, OSError) as err:
        errors.append(f"sitemap.xml: {err}")
    if errors:
        print(f"FAIL: {len(errors)} issue(s):")
        for issue in errors:
            print(" - " + issue)
        return 1
    print(f"PASS: {len(PAGES)} HTML pages, assets, metadata, hours, sitemap and 404.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
