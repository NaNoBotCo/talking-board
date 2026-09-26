#!/usr/bin/env python3
"""index.html (the artifact page) -> docs/ for GitHub Pages: full document, share tags, card, sitemap."""
import pathlib, re, subprocess, sys, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
URL = "https://nanobotco.github.io/talking-board/"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DESC = "A parlour talking board. Bots take the empty seats, a lens rides the planchette, and a notebook reads what comes through. For entertainment."
DESC_TH = "กระดานวิญญาณในห้องรับแขก บอทนั่งแทนที่ว่าง แผ่นชี้มีเลนส์ขยาย สมุดจดคำที่ได้รับ เพื่อความบันเทิง"

src = (ROOT / "index.html").read_text()
head, body = src.split("</style>\n", 1)
head += "</style>\n"
head = re.sub(r'<meta charset="utf-8">\n', "", head)
head = re.sub(r'<meta name="description"[^>]*>\n', "", head)
meta = f"""<meta charset="utf-8">
<meta name="description" content="{DESC}">
<meta name="google" content="notranslate">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="Talking Board · กระดานวิญญาณ">
<meta property="og:description" content="{DESC} {DESC_TH}">
<meta property="og:image" content="{URL}card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{URL}card.png">
<meta name="theme-color" content="#150e0a">
"""
page = f'<!doctype html>\n<html lang="en" translate="no" class="notranslate">\n<head>\n{meta}{head}</head>\n<body>\n{body}</body>\n</html>\n'
DOCS.mkdir(exist_ok=True)
(DOCS / "index.html").write_text(page)
(DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n")
(DOCS / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{URL}</loc><lastmod>{time.strftime('%Y-%m-%d')}</lastmod></url>\n</urlset>\n")
(DOCS / ".nojekyll").write_text("")

if "--card" in sys.argv:
    # photograph the page itself at share-card size
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "card.png"
        subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--force-prefers-reduced-motion=0",
                        "--window-size=1200,630", "--timeout=5000", f"--user-data-dir={tmp}/p",
                        f"--screenshot={out}", (DOCS / "index.html").as_uri()], check=False, timeout=40,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        (DOCS / "card.png").write_bytes(out.read_bytes())
print("built", DOCS / "index.html")
