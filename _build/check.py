#!/usr/bin/env python3
"""Site QA. Usage: check.py [--launch]

Preview: noindex, no Cloudflare beacon, no GA4 loader, no CNAME.
Launch: root-relative paths, CNAME whichcabin.com, beacon and GA4 loader on every page,
Consent Mode v2 defaults denied. Fails if GA4_ID in _build/build.py is empty.
Also checks titles under 60 characters, unique titles and descriptions, canonical,
Open Graph, JSON-LD, footer policy links, sitemap lastmod, robots, llms.txt and the IndexNow key.
"""
import glob, re, json, os, sys, html

# Paths in _build/thin-noindex.txt are intentionally noindex (AdSense low-value-content fix, 20 Nov 2026).
import os as _os
_THIN = set()
try:
    with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "thin-noindex.txt"), encoding="utf-8") as _fh:
        _THIN = {l.strip().strip("/") for l in _fh if l.strip() and not l.startswith("#")}
except FileNotFoundError:
    pass


def _thin_rel(rel):
    r = str(rel).replace("\\", "/")
    if r.endswith("index.html"):
        r = r[: -len("index.html")]
    return r.strip("/") in _THIN


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAUNCH = "--launch" in sys.argv
PREFIX = "" if LAUNCH else "/whichcabin"
LEGAL = {"terms", "privacy", "disclaimer", "copyright", "ad-disclosure"}
INDEXNOW = "6d99be0a8662d09dadd3f19d2857201e"
FOOTER = (">About<", ">Contact<", ">Privacy<", "Terms of use", ">Disclaimer<", "Copyright",
          "Advertising disclosure", "Image policy", ">Cookie settings<")
ROBOTS = ("Googlebot", "Bingbot", "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot",
          "Claude-SearchBot", "PerplexityBot", "Perplexity-User", "Google-Extended",
          "Amazonbot", "CCBot", "Applebot-Extended")

def ga4_id():
    src = open(os.path.join(ROOT, "_build", "build.py"), encoding="utf-8").read()
    m = re.search(r'^GA4_ID\s*=\s*"([^"]*)"', src, re.M)
    return m.group(1) if m else ""

def need_ld(h, rel, types, bad):
    for typ in types:
        if f'"@type": "{typ}"' not in h:
            print("jsonld", typ, rel)
            bad[0] += 1

GA4 = ga4_id()
bad = [0]
titles, descs = {}, {}
files = [f for f in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_build/" not in f]
if LAUNCH and not GA4:
    print("ga4-id-empty: set GA4_ID in _build/build.py to a G-XXXXXXXXXX measurement id")
    bad[0] += 1
elif LAUNCH and not re.fullmatch(r"G-[A-Z0-9]+", GA4):
    print("ga4-id-invalid", GA4)
    bad[0] += 1
for f in files:
    h = open(f, encoding="utf-8").read()
    rel = os.path.relpath(f, ROOT)
    top = rel.split("/")[0]
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h):
        try:
            json.loads(m)
        except Exception as e:
            print("JSONLD", rel, e)
            bad[0] += 1
    vis = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    if top not in LEGAL and re.search(r"Joshua|Israel Ventures|©", vis):
        print("LLC/©", rel)
        bad[0] += 1
    if top in LEGAL and "is a trade name of Joshua Israel Ventures LLC" not in h:
        print("nolegalline", rel)
        bad[0] += 1
    if not re.search(r'<link rel="canonical" href="https://whichcabin.com/', h):
        print("canonical", rel)
        bad[0] += 1
    if h.count("<h1") != 1:
        print("h1count", rel, h.count("<h1"))
        bad[0] += 1
    for prop in ("og:title", "og:description", "og:url", "og:image", "og:type"):
        if f'property="{prop}"' not in h:
            print("og", prop, rel)
            bad[0] += 1
    md = re.search(r'<meta name="description" content="(.*?)">', h)
    desc = html.unescape(md.group(1)).strip() if md else ""
    if not desc:
        print("nodesc", rel)
        bad[0] += 1
    elif len(desc) > 160:
        print("longdesc", len(desc), rel)
        bad[0] += 1
    else:
        descs.setdefault(desc, []).append(rel)
    if LAUNCH:
        if "static.cloudflareinsights.com/beacon.min.js" not in h:
            print("nobeacon", rel)
            bad[0] += 1
        if "https://www.googletagmanager.com/gtag/js?id=" not in h or (GA4 and f"https://www.googletagmanager.com/gtag/js?id={GA4}" not in h):
            print("noga4", rel)
            bad[0] += 1
        if "gtag('consent','default'" not in h or "analytics_storage':'denied'" not in h:
            print("noconsent", rel)
            bad[0] += 1
        if "noindex" in h and rel != "404.html" and not _thin_rel(rel):
            print("noindex", rel)
            bad[0] += 1
        if 'href="/whichcabin' in h or 'src="/whichcabin' in h:
            print("not-root-relative", rel)
            bad[0] += 1
    else:
        if "noindex" not in h:
            print("preview-missing-noindex", rel)
            bad[0] += 1
        if "static.cloudflareinsights.com/beacon.min.js" in h:
            print("preview-beacon", rel)
            bad[0] += 1
        if "googletagmanager.com/gtag/js" in h:
            print("preview-ga4", rel)
            bad[0] += 1
    if "—" in h or "–" in h:
        print("dash", rel)
    t = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
    if len(t) >= 60:
        print("longtitle", len(t), t)
        bad[0] += 1
    titles.setdefault(t, []).append(rel)
    foot = re.search(r'<footer class="site">.*?</footer>', h, re.S)
    foot = foot.group(0) if foot else ""
    for needle in FOOTER:
        if needle not in foot:
            print("footer", needle, rel)
            bad[0] += 1
    for img in re.finditer(r"<img\b[^>]*>", h, re.I):
        start = h.rfind("<a ", 0, img.start())
        end = h.find("</a>", img.end())
        chunk = h[start:end] if start != -1 and img.start() - start < 400 and end != -1 else ""
        if "image-policy" not in chunk:
            print("photo-policy", rel)
            bad[0] += 1
    if rel == "index.html":
        need_ld(h, rel, ("WebSite", "FAQPage"), bad)
    elif rel != "404.html":
        kinds = ("BreadcrumbList",)
        if top in ("ships", "guides", "lines"):
            kinds = ("Article", "FAQPage", "BreadcrumbList")
        need_ld(h, rel, kinds, bad)
    for l in re.findall(r'(?:href|src)="(/[^"#?]*)', h):
        if not l.startswith(PREFIX + "/") and l != PREFIX + "/":
            print("prefix", rel, l)
            bad[0] += 1
            continue
        p = os.path.join(ROOT, l[len(PREFIX):].lstrip("/"))
        if not (os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))):
            print("broken", rel, l)
            bad[0] += 1
for t, fs in titles.items():
    if len(fs) > 1:
        print("duptitle", t, fs)
        bad[0] += 1
for d, fs in descs.items():
    if len(fs) > 1:
        print("dupdesc", d, fs)
        bad[0] += 1
cname = os.path.join(ROOT, "CNAME")
if LAUNCH:
    got = open(cname, encoding="utf-8").read().strip() if os.path.isfile(cname) else ""
    if got != "whichcabin.com":
        print("cname", got or "(missing)")
        bad[0] += 1
elif os.path.exists(cname):
    print("preview-cname")
    bad[0] += 1
robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
for bot in ROBOTS:
    if f"User-agent: {bot}\nAllow: /" not in robots:
        print("robots", bot)
        bad[0] += 1
if "Sitemap: https://whichcabin.com/sitemap.xml" not in robots:
    print("robots-sitemap")
    bad[0] += 1
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(https://whichcabin.com/[^<]*)</loc>", sm)
mods = re.findall(r"<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>", sm)
if not locs or len(locs) != len(mods):
    print("sitemap-lastmod", len(locs), len(mods))
    bad[0] += 1
key_path = os.path.join(ROOT, INDEXNOW + ".txt")
if not os.path.isfile(key_path) or open(key_path, encoding="utf-8").read().strip() != INDEXNOW:
    print("indexnow")
    bad[0] += 1
llms = os.path.join(ROOT, "llms.txt")
if not os.path.isfile(llms) or "whichcabin.com" not in open(llms, encoding="utf-8").read():
    print("llms")
    bad[0] += 1
ads = os.path.join(ROOT, "ads.txt")
if LAUNCH:
    if os.path.isfile(ads) and "pub-5681559774142917" in open(ads, encoding="utf-8").read():  # AdSense detached 21 Nov 2026 until the account is approved (see seo-central/site-seo-rules.md). Do not re-add.
        print("ads.txt")
        bad[0] += 1
    home = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    if 'name="google-adsense-account"' in home or "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" in home:
        print("adsense-head")
        bad[0] += 1
print("files", len(files), "issues", bad[0])
sys.exit(1 if bad[0] else 0)
