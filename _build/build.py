#!/usr/bin/env python3
"""Which Cabin static site builder. Run from repo root.
  python3 _build/build.py            # PREVIEW build for https://joshuaofisrael.github.io/whichcabin/ (noindex, /whichcabin prefix, no beacon, no CNAME)
  python3 _build/build.py --launch   # LAUNCH build for https://whichcabin.com/ (indexable, root paths, CF beacon, GA4 after consent, CNAME file)
Then: python3 _build/check.py [--launch] && python3 _build/legal_gate.py check
check.py --launch fails while GA4_ID is empty, or if any page lacks the Cloudflare beacon or the GA4 loader.
"""
import os, sys, json, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ships import SHIPS, LINES
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAUNCH = "--launch" in sys.argv
BASE_URL = "https://whichcabin.com/"                 # canonical everywhere, in both modes
SITE_URL = BASE_URL if LAUNCH else "https://joshuaofisrael.github.io/whichcabin/"
PREFIX = "" if LAUNCH else "/whichcabin"
BRAND = "Which Cabin"
TODAY = "2026-11-15"; TODAY_H = "15 Nov 2026"
ADDED = "2026-11-16"  # ships added after the 15 Nov 2026 set
MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def humandate(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m)]} {y}"
def join_names(names):
    names = list(names)
    if len(names) < 2: return "".join(names)
    return ", ".join(names[:-1]) + " and " + names[-1]
INDEXNOW_KEY = "6d99be0a8662d09dadd3f19d2857201e"
CF_BEACON_TOKEN = "eac63f2b5dbc4539a2d95249baab6472"  # shared JI Ventures Analytics 2 token (requestHost match), same as Coaster Map. Launch build only.
GA4_ID = "G-HSNXLPKVXV"  # Owner pastes a GA4 measurement id (G-XXXXXXXXXX) before launch. Empty string until then. check.py --launch fails while this is empty.
FORM_ENDPOINT = "https://formsubmit.co/4497ee41a1200e746e967998473d21da"
LEGAL_LINE = "© 2026 Joshua Israel Ventures LLC. All rights reserved. Which Cabin is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company."
E = html.escape
DECKS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "decks.json")))
PAGES = []
CDC = ("CDC Yellow Book: Motion Sickness", "https://www.cdc.gov/yellow-book/hcp/travel-air-sea/motion-sickness.html")

def u(path): return PREFIX + path
def url(path): return BASE_URL + path.lstrip("/")
def write(path, content):
    fp = os.path.join(ROOT, path.lstrip("/"))
    if path.endswith("/"): fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(content)

LOGO = '<svg width="34" height="34" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="14" fill="#0b3954"/><circle cx="32" cy="30" r="17" fill="#e6f4f1" stroke="#ffb347" stroke-width="5"/><path d="M17 33 q7.5-6 15 0 t15 0 v6 a17 17 0 0 1-30 0z" fill="#087e8b"/><rect x="12" y="50" width="40" height="5" rx="2.5" fill="#ffb347"/></svg>'
NAV = [("/", "Home"), ("/ships/", "Ships"), ("/lines/", "Cruise lines"), ("/guides/how-to-choose-a-cruise-cabin/", "How to choose"), ("/guides/quietest-cruise-cabins/", "Quietest decks")]

def clip(d, n=155):
    d = re.sub(r"\s+", " ", d).strip()
    if len(d) <= n: return d
    c = d[:n]
    i = max(c.rfind(". "), c.rfind("? "))
    if i >= 80: return c[:i + 1]
    sp = c.rfind(" ")
    return (c[:sp] if sp > 40 else c).rstrip(",;:") + "."

def org_ld():
    return {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": {"@type": "ImageObject", "url": url("/logo.png")}}
def article_ld(headline, path, modified):
    return {"@context": "https://schema.org", "@type": "Article", "headline": headline, "dateModified": modified, "datePublished": modified,
            "author": {"@type": "Organization", "name": BRAND, "url": BASE_URL}, "publisher": org_ld(), "mainEntityOfPage": url(path)}
def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
def faq_block(faqs):
    return '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>' + "".join(
        f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs) + "</section>"
GUIDE_LINKS = [
    ("/guides/how-to-choose-a-cruise-cabin/", "How to choose a cruise cabin"),
    ("/guides/quietest-cruise-cabins/", "Quietest cabin decks"),
    ("/guides/best-cabin-for-seasickness/", "Best cabin for seasickness"),
    ("/guides/cruise-cabins-to-avoid/", "Cabins to avoid"),
]
def related(path, extra=()):
    seen, items = set(), []
    for p, n in list(extra) + GUIDE_LINKS + [("/ships/", "All ships"), ("/lines/", "Cruise lines")]:
        if p == path or p in seen: continue
        seen.add(p); items.append((p, n))
    return '<p class="related"><strong>Related:</strong> ' + " · ".join(f'<a href="{u(p)}">{E(n)}</a>' for p, n in items) + "</p>"
def ga4_head():
    if not LAUNCH: return ""
    # Consent Mode v2 defaults are denied. gtag.js is not fetched until consent.js runs after Accept.
    return ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            "gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied',"
            "'analytics_storage':'denied','functionality_storage':'denied','personalization_storage':'denied',"
            "'security_storage':'granted','wait_for_update':500});</script>"
            f'<script id="ga4-loader" type="text/plain" data-ga4-id="{E(GA4_ID)}" data-src="https://www.googletagmanager.com/gtag/js?id={E(GA4_ID)}"></script>')
def consent_banner():
    return f'''<div id="consent-banner" class="consent" hidden role="region" aria-label="Cookie settings"><p>Cloudflare Web Analytics does not use cookies. Google Analytics 4 loads only after you accept. <a href="{u('/privacy/')}">Privacy</a></p><div class="btnrow"><button type="button" class="btn" id="consent-accept">Accept</button><button type="button" class="btn alt" id="consent-reject">Reject</button></div></div>'''

def page(path, title, desc, body, jsonld=None, crumbs=None, noindex=False, legal=False, modified=TODAY, og_type="website"):
    if len(title) >= 60: raise SystemExit(f"title {len(title)} chars: {title}")
    desc = clip(desc)
    if len(desc) > 160: raise SystemExit(f"desc {len(desc)} chars: {desc}")
    canon = url(path)
    if not noindex: PAGES.append((path, modified))
    ld = []
    if path == "/":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": BASE_URL,
                   "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": url("/logo.png")}})
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (p, n) in enumerate(crumbs)]})
    if jsonld: ld += jsonld if isinstance(jsonld, list) else [jsonld]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    nav = "".join(f'<a href="{u(p)}"' + (' aria-current="page"' if p == path else "") + f'>{n}</a>' for p, n in NAV)
    bc = ""
    if crumbs:
        bc = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
            (f'<li><a href="{u(p)}">{E(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{E(n)}</li>') for i, (p, n) in enumerate(crumbs)) + "</ol></nav>"
    robots = "noindex, follow" if (noindex or not LAUNCH) else "index, follow, max-image-preview:large"
    beacon = (f"<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{\"token\": \"{CF_BEACON_TOKEN}\"}}'></script><!-- End Cloudflare Web Analytics -->") if LAUNCH else "<!-- cf-beacon: added by launch build -->"
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{url('/og.png')}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{u('/favicon.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{u('/assets/style.css')}?v=2">{ga4_head()}{ldh}
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap"><a class="brand" href="{u('/')}">{LOGO}<span>{BRAND}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
<main id="main" class="wrap">{bc}{body}<!-- ad-slot: below-content (reserved; no ad code) --></main>
<footer class="site"><div class="wrap"><p class="fbrand"><strong>{BRAND}</strong>: which cabin and deck to ask for on the biggest cruise ships, worked out from published deck-by-deck listings. Independent and not affiliated with any cruise line. Layouts change, so always check the line's current deck plan before you book.</p>
<p class="flinks"><a href="{u('/about/')}">About</a> | <a href="{u('/contact/')}">Contact</a> | <a href="{u('/privacy/')}">Privacy</a> | <a href="{u('/terms/')}">Terms of use</a> | <a href="{u('/disclaimer/')}">Disclaimer</a> | <a href="{u('/copyright/')}">Copyright and DMCA</a> | <a href="{u('/ad-disclosure/')}">Advertising disclosure</a> | <a href="{u('/image-policy/')}">Image policy</a> | <a href="{u('/methodology/')}">Sources and methods</a> | <a href="{u('/privacy/')}" id="cookie-settings">Cookie settings</a></p>
{f'<p class="legal-line">{LEGAL_LINE}</p>' if legal else ''}</div></footer>
{consent_banner()}
<script src="{u('/assets/site.js')}?v=1" defer></script><script src="{u('/assets/consent.js')}?v=1" defer></script>{beacon}
</body></html>'''

def link(s): return f'<a href="{s[1]}" rel="nofollow noopener" target="_blank">{E(s[0])}</a>'

# ---------- deck analysis (from CruiseMapper deck labels, which summarise each line's official deck plan) ----------
CABIN_RX = re.compile(r"^(Cabins|Suites?|Studios(\d*| Lower| Upper)?|The Haven(\d*| Lower| Upper)?|Haven\d*|Tower Suite\d*|Loft Suites?\d*|Suite Class\d*|Edge Villas|Iconic Suites|Duplex Suites\d*|Yacht Club Cabins)$")
NEUTRAL_RX = re.compile(r"^(Bridge|Hospital|Crew|Crew Cabins|Tendering|Topdeck|Aerial View)$")
# "Sky" alone is a deck name on some ships (Celebrity's Sky deck). Activity names are listed in full.
ABOVE_RX = re.compile(r"Pool|Lido|Sundeck|Sports|Water|Slide|FlowRider|Golf|Speedway|Racetrack|Ropes|Rollglider|Coaster|Park19|Adventure Trail|Cliffhanger|Spiral|Abyss|Thrill Island|Chill Island|AquaDome|Dome|Sanctuary|SkyDeck|SkyRide|SkyCourse|SkyZone|Skydeck|Serenity|Marketplace|Buffet|Gym|Fitness|Helideck|Rooftop|Retreat|Sea View Terrace|Luminae|Solarium|SeaPlex|NorthStar|RipCord|Vibe Beach Club|Kids|Teens|Splashaway|Magic Carpet", re.I)
NIGHT_RX = re.compile(r"Theater|Music Hall|Casino|Entertainment|Lounge|Promenade|Boardwalk|Central Park|Havana|Studio B|Ice|Absolute Zero|Shops|Plaza|Fiesta|Gala|Cinemas|Lobby|Gateway|Currents|French Quarter|La Piazza|The Shores|Eden|Surfside|Observation|Top Sail|Adults|Wonderland|Family Harbor|Dining|Restaurant|Spa|Enchanted Garden|Sheehan|Crows Nest|Izumi", re.I)
def tokens(label):
    t = [x.strip() for x in label.split("-") if x.strip()]
    return [re.sub(r"\d+$", "", x).strip() if re.search(r"[A-Za-z]\d$", x) else x for x in t]
# Deck names that contain a venue word but are not themselves a venue.
DECK_NAME = {"Upper Promenade", "Lower Promenade"}
def classify(label):
    t = tokens(label)
    cab = [x for x in t if CABIN_RX.match(x)]
    ven = [x for x in t if x not in DECK_NAME and not CABIN_RX.match(x) and not NEUTRAL_RX.match(x) and (ABOVE_RX.search(x) or NIGHT_RX.search(x))]
    return cab, ven, t
def nice(label): return " · ".join(dict.fromkeys(tokens(label)))
def analyse(s):
    ds = DECKS[s["cm"]]["decks"]
    out = []
    for i, d in enumerate(ds):
        cab, ven, t = classify(d["label"])
        up = ds[i + 1] if i + 1 < len(ds) else None
        dn = ds[i - 1] if i > 0 else None
        r = dict(num=str(int(d["deck"])) if d["deck"].isdigit() else d["deck"], label=nice(d["label"]), url=d["url"], cabin=bool(cab), venues=ven, reasons=[], above=[], below=[])
        if cab:
            if up:
                uc, uv, _ = classify(up["label"])
                r["above"] = uv
                if uv: r["reasons"].append(f'below deck {int(up["deck"])} ({", ".join(dict.fromkeys(uv))})')
            if dn:
                dc, dv, _ = classify(dn["label"])
                nv = [x for x in dv if NIGHT_RX.search(x) or ABOVE_RX.search(x)]
                r["below"] = nv
                if nv: r["reasons"].append(f'above deck {int(dn["deck"])} ({", ".join(dict.fromkeys(nv))})')
            if ven: r["reasons"].insert(0, f'shares the deck with {", ".join(dict.fromkeys(ven))}')
            r["status"] = "quiet" if not r["reasons"] else "check"
            r["suite_only"] = all(not x.startswith("Cabins") for x in cab)
        else:
            r["status"] = "public"; r["suite_only"] = False
        out.append(r)
    return out
def rng(nums):
    nums = [int(n) for n in nums]
    if not nums: return ""
    parts, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n is not None and n == prev + 1: prev = n; continue
        parts.append(f"{start}" if start == prev else f"{start} to {prev}")
        if n is not None: start = prev = n
    return ", ".join(parts)
def decks_word(nums): return ("deck " if len(nums) == 1 else "decks ") + rng(nums)

def ship_by(slug): return next(x for x in SHIPS if x["slug"] == slug)
def ship_path(s): return f'/ships/{s["slug"]}/'

def deck_chart(A, s):
    rows = []
    for r in reversed(A):
        lab = {"quiet": "Quiet cabin deck", "check": "Cabins: check above and below", "public": "Public deck (no regular cabins)"}[r["status"]]
        why = ("; " + "; ".join(r["reasons"])) if r["reasons"] else ""
        rows.append(f'<li class="deck {r["status"]}"><span class="dnum">Deck {E(r["num"])}</span><span class="dlab">{E(r["label"])}</span><span class="dtag">{lab}{E(why)}</span></li>')
    return ('<figure class="deckmap" aria-labelledby="dm-cap"><figcaption id="dm-cap"><strong>' + E(s["name"]) + ' deck noise map</strong>, top deck first. Our own diagram, built from deck-by-deck listings of the ship\'s layout (sources below). Green: cabin decks with cabins above and below. Amber: cabin decks that share space with, or sit next to, public venues. Grey: public decks.</figcaption>'
            '<ol class="decks">' + "".join(rows) + '</ol></figure>')

def ship_page(s):
    A = analyse(s); L = LINES[s["line"]]; path = ship_path(s)
    chk = s.get("checked", TODAY); chk_h = humandate(chk)
    cab = [r for r in A if r["cabin"]]; quiet = [r for r in cab if r["status"] == "quiet"]
    POOLY = re.compile(r"Pool|Lido|Sundeck|Sports|Water|Slide|Speedway|Racetrack|Coaster|Dome|Marketplace|Buffet|FlowRider|Golf|Thrill|Chill|Serenity|Sanctuary|Ropes|Rollglider|Park19|Adventure|Cliffhanger|Spiral|Abyss|Solarium|SeaPlex|NorthStar|RipCord|SkyRide|SkyCourse|SkyZone|Vibe Beach Club", re.I)
    under_pool = [r for r in cab if any(POOLY.search(x) for x in r["above"])]
    over_night = [r for r in cab if any(re.search(r"Theater|Music Hall|Casino|Entertainment|Lounge|Promenade|Boardwalk|Havana|Ice|Absolute Zero|Shops|Plaza|Fiesta|Cinemas|Dining|Restaurant|Eden|Gateway|Currents|Lobby", x, re.I) for x in r["below"])]
    shared = [r for r in cab if r["venues"]]
    regular = [r for r in cab if not r["suite_only"]]
    low = regular[:2]
    qn = [r["num"] for r in quiet]
    mid = quiet[len(quiet) // 2]["num"] if quiet else None
    title = f'Which Cabin to Book on {s["name"]}'
    if quiet:
        desc = f'Which cabin to book on {s["name"]}: quiet decks {rng(qn)}. Low and midship if you get seasick. Avoid decks under pools or over nightlife.'
    else:
        desc = f'Which cabin to book on {s["name"]}: deck noise map, seasickness cabins, and which decks to avoid.'
    qa = []
    if quiet: qa.append(f'<li><strong>Light sleepers:</strong> {decks_word(qn)}. These cabin decks have cabins directly above and below.</li>')
    else: qa.append('<li><strong>Light sleepers:</strong> every cabin deck on this ship touches a public area somewhere, so check the line\'s deck plan for what is directly above and below your cabin number.</li>')
    if low: qa.append(f'<li><strong>Seasickness:</strong> a midship cabin on the lowest cabin decks ({decks_word([r["num"] for r in low])}), away from the bow.</li>')
    if under_pool: qa.append(f'<li><strong>Think twice:</strong> {decks_word([r["num"] for r in under_pool])} (directly under pool, sports or buffet areas)' + (f' and {decks_word([r["num"] for r in over_night if r not in under_pool])} (over bars, shops or entertainment)' if [r for r in over_night if r not in under_pool] else "") + '.</li>')
    elif over_night: qa.append(f'<li><strong>Think twice:</strong> {decks_word([r["num"] for r in over_night])} (over bars, shops or entertainment).</li>')
    notes = "".join(f'<h3>{E(t)}</h3><p>{E(b)}</p>' for t, b in s["notes"])
    avoid = []
    for r in under_pool: avoid.append(f'<li><strong>Deck {r["num"]}</strong> sits directly below {E(", ".join(dict.fromkeys(x for x in r["above"] if POOLY.search(x))))}. Expect deck chairs, set-up and activity overhead from early morning.</li>')
    for r in over_night:
        if r in under_pool: continue
        avoid.append(f'<li><strong>Deck {r["num"]}</strong> sits directly above {E(", ".join(dict.fromkeys(r["below"])))}, which can stay busy late.</li>')
    for r in shared:
        if r in under_pool or r in over_night: continue
        avoid.append(f'<li><strong>Deck {r["num"]}</strong> shares the deck with {E(", ".join(dict.fromkeys(r["venues"])))}. Cabins at the other end of the deck are usually quieter; check where the venue is.</li>')
    avoid += ['<li><strong>Lowest forward cabins</strong> are closest to the bow thrusters and anchor gear, which can be loud when the ship docks or anchors early in the morning.</li>',
              '<li><strong>Cabins next to service areas, elevators or stair landings</strong> get more foot traffic and door noise. On the deck plan, look for unlabelled blocks (crew and service rooms) beside a cabin.</li>',
              '<li><strong>Partial or obstructed view categories</strong> usually mean lifeboats or structure in the way. The line labels these on its deck plan, so read the category name before you pay for a view.</li>']
    facts = s["facts"]; fr = []
    for k, lab in (("cls", "Ship class"), ("builder", "Builder"), ("service", "Entered service"), ("gt", "Gross tonnage"), ("guests", "Guest capacity")):
        if facts.get(k): fr.append(f'<tr><th scope="row">{lab}</th><td>{E(facts[k])}</td></tr>')
    fr.append(f'<tr><th scope="row">Cabin decks</th><td>{E(rng([r["num"] for r in cab]))}</td></tr>')
    fr.append(f'<tr><th scope="row">Quiet cabin decks (our analysis)</th><td>{E(rng(qn)) or "None fully enclosed by cabin decks"}</td></tr>')
    wiki = (f'Wikipedia: {s["name"]}' if s["slug"] != "msc-world-america" else "Wikipedia: World-class cruise ship", f'https://en.wikipedia.org/wiki/{s["wiki"]}')
    fsrc = facts.get("src") or wiki
    faqs = []
    faqs.append((f'What is the best deck to stay on {s["name"]}?', (f'For a quiet night, pick a cabin on {decks_word(qn)}, which have cabin decks directly above and below. ' + (f'Deck {mid} is in the middle of that quiet block. ' if mid else "") if quiet else 'Every cabin deck touches a public area somewhere, so choose a cabin whose number is well away from the venues listed on that deck. ') + 'Midship cabins move least in rough seas.'))
    if under_pool or over_night: faqs.append((f'Which decks should I avoid on {s["name"]}?', ("Avoid " + decks_word([r["num"] for r in under_pool]) + " if you dislike noise overhead, because " + ("it sits" if len(under_pool) == 1 else "they sit") + " directly under pool, sports or buffet areas. " if under_pool else "") + ("Light sleepers should also think twice about " + decks_word([r["num"] for r in over_night if r not in under_pool]) + (", which sits" if len([r for r in over_night if r not in under_pool]) == 1 else ", which sit") + " above bars, shops or entertainment venues." if [r for r in over_night if r not in under_pool] else "")))
    if low: faqs.append((f'Where is the best cabin on {s["name"]} for seasickness?', f'Book a midship cabin on the lowest cabin decks ({decks_word([r["num"] for r in low])}). The CDC advises avoiding the parts of a ship with the most motion, such as the bow, and getting a view of the horizon helps, so an oceanview or balcony cabin low and midship is the ideal combination.'))
    faqs.append((f'How many decks have cabins on {s["name"]}?', f'{len(cab)} decks have passenger cabins: {rng([r["num"] for r in cab])}, based on the deck-by-deck listing of the current deck plan. Check the line\'s official deck plan for the exact cabin numbers on each deck.'))
    faqs.append((f'Is a balcony worth it on {s["name"]}?', 'A balcony helps most on scenic or warm-weather itineraries and for anyone prone to seasickness, because a horizon view reduces symptoms. Check the category name first: inward-facing, promenade-view and partial-view balconies cost less but do not give a clear sea view.'))
    sis = "".join(f'<li><a href="{u(ship_path(ship_by(x)))}">{E(ship_by(x)["name"])}</a></li>' for x in s["sister"])
    srcs = [(f'{L["name"]}: official {s["name"]} deck plans', s["official"]), (f'CruiseMapper: {s["name"]} deck plans (deck-by-deck listing)', DECKS[s["cm"]]["index"]), fsrc]
    if fsrc is not wiki: srcs.append(wiki)
    srcs.append(CDC)
    sub_bits = [L["name"]] + ([facts["cls"]] if facts.get("cls") else []) + [f"deck plans checked {chk_h}"]
    body = f'''<article class="prose wide"><h1>Which cabin to book on {E(s["name"])}</h1>
<p class="sub">{E(" · ".join(sub_bits))}</p>
<div class="answer"><p><strong>Quick answer</strong></p><ul>{"".join(qa)}</ul></div>
<p>{E(s["name"])} has {len(cab)} decks with passenger cabins. Below is our deck noise map, which marks every deck by what is on it and what is directly above and below, followed by ship-specific tips and the cabins to think twice about. It is a planning shortcut: the line's own deck plan is always the final word on any cabin number.</p>
{deck_chart(A, s)}
<h2>Best cabins on {E(s["name"])} by traveller</h2>
<ul class="picks">
<li><strong>Light sleepers:</strong> {("cabins on " + decks_word(qn) + ", ideally midship and away from elevators.") if quiet else "a cabin at the far end of a deck from its listed venues."}</li>
<li><strong>Seasickness:</strong> {("midship on " + decks_word([r["num"] for r in low]) + ", with a window or balcony if you can, so you can see the horizon.") if low else "midship and as low as possible."}</li>
<li><strong>Families:</strong> {"decks near the kids' areas (" + decks_word([r["num"] for r in A if any(re.search(r"Kids|Family|Surfside|Splashaway", x) for x in r["venues"])]) + ") save walking, but they are busier." if [r for r in A if any(re.search(r"Kids|Family|Surfside|Splashaway", x) for x in r["venues"])] else "a midship cabin on a quiet deck, close to a bank of elevators."}</li>
<li><strong>Views:</strong> an outward-facing balcony on a quiet deck. Avoid any category the line labels as partial or obstructed view.</li>
<li><strong>Budget:</strong> an interior cabin on a quiet deck gives the best sleep for the money; the deck matters more than the category for noise.</li></ul>
<h2>{E(s["name"])} tips</h2>{notes}
<h2>Cabins to think twice about</h2><ul>{"".join(avoid)}</ul>
<h2>{E(s["name"])} at a glance</h2><div class="tablewrap"><table class="stats"><tbody>{"".join(fr)}</tbody></table></div>
<p class="note">Ship facts from {link(fsrc)}. Cabin decks and deck contents from the deck-by-deck listing on CruiseMapper, checked against the {E(L["short"])} deck plan page.</p>
{('<h2>Sister ships</h2><ul class="cols">' + sis + '</ul>') if sis else ''}
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>{"".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)}</section>
<section class="sources" aria-labelledby="src-h"><h2 id="src-h">Sources</h2><ul>{"".join(f"<li>{link(x)}</li>" for x in srcs)}</ul>
<p class="note">Retrieved {chk_h}. Which Cabin is not affiliated with {E(L["name"])}. Deck layouts and cabin categories can change after refits; always confirm on the line's current deck plan before booking. See <a href="{u('/methodology/')}">how we build these pages</a>.</p></section>
{related(path, [(f'/lines/{s["line"]}/', f'All {L["short"]} ships')])}</article>'''
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": f'Which cabin to book on {s["name"]}', "dateModified": chk, "datePublished": chk,
           "author": {"@type": "Organization", "name": BRAND, "url": BASE_URL}, "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": {"@type": "ImageObject", "url": url("/logo.png")}},
           "mainEntityOfPage": url(path), "about": {"@type": "Thing", "name": s["name"]}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]
    write(path, page(path, title, desc, body, ld, [("/", "Home"), ("/ships/", "Ships"), ("/lines/" + s["line"] + "/", L["short"]), (path, s["name"])], modified=chk, og_type="article"))
    s["_quiet"] = qn; s["_cab"] = [r["num"] for r in cab]; s["_pool"] = [r["num"] for r in under_pool]

def ships_index():
    rows = "".join(f'<tr><td><a href="{u(ship_path(s))}">{E(s["name"])}</a></td><td>{E(LINES[s["line"]]["short"])}</td><td>{E(s["facts"].get("cls", ""))}</td><td>{E(rng(s["_quiet"])) or "None"}</td></tr>' for s in SHIPS)
    faqs = [
        ("Which cabin should I book?", "Open your ship. Each guide gives a quick answer, a deck noise map, the best cabins by traveller and the decks to think twice about."),
        ("What is a quiet cabin deck?", "A cabin deck with cabin decks directly above and below, and no listed public venues on that deck."),
    ]
    body = f'''<h1>Cruise ship cabin guides</h1><p class="answer">Pick your ship for a deck-by-deck noise map, the best cabins to ask for and the ones to avoid. We cover {len(SHIPS)} of the biggest ships at {E(join_names(L["short"] for L in LINES.values()))}.</p>
<p>Browse by <a href="{u('/lines/')}">cruise line</a>, or read <a href="{u('/guides/how-to-choose-a-cruise-cabin/')}">how to choose a cabin</a>, the <a href="{u('/guides/quietest-cruise-cabins/')}">quietest decks</a>, the <a href="{u('/guides/best-cabin-for-seasickness/')}">best cabin for seasickness</a> and <a href="{u('/guides/cruise-cabins-to-avoid/')}">cabins to avoid</a>.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Ship</th><th scope="col">Line</th><th scope="col">Class</th><th scope="col">Quiet cabin decks</th></tr></thead><tbody>{rows}</tbody></table></div>
{faq_block(faqs)}'''
    h1 = "Cruise ship cabin guides"
    write("/ships/", page("/ships/", "Which Ship Cabin Should I Book", f"Which cabin should I book? Open one of {len(SHIPS)} ships for its quiet decks, seasickness cabins and the decks to avoid.", body, [article_ld(h1, "/ships/", ADDED), faq_ld(faqs)], [("/", "Home"), ("/ships/", "Ships")], modified=ADDED, og_type="article"))

def line_pages():
    cards = []
    for k, L in LINES.items():
        ss = [s for s in SHIPS if s["line"] == k]
        classes = list(dict.fromkeys(s["facts"].get("cls") for s in ss if s["facts"].get("cls")))
        def card(s):
            cls = s["facts"].get("cls", "")
            head = f"{E(cls)}. " if cls else ""
            pool = f' Under the pool deck: {E(rng(s["_pool"]))}.' if s["_pool"] else ""
            return f'<li class="card"><h2><a href="{u(ship_path(s))}">{E(s["name"])}</a></h2><p>{head}Quiet cabin decks: {E(rng(s["_quiet"])) or "none fully enclosed"}.{pool}</p></li>'
        items = "".join(card(s) for s in ss)
        klass = f" ({', '.join(classes)})" if classes else ""
        p = f"/lines/{k}/"
        faqs = [
            (f'Which {L["short"]} cabin should I book?', f'Start with a deck that has cabins directly above and below, midship and away from elevators. The cards below list those quiet decks for each {L["short"]} ship we cover.'),
            (f'Which {L["short"]} ships are on this page?', f'{len(ss)} ships: {join_names(s["name"] for s in ss)}.'),
            (f'Do these {L["short"]} ships share cabin decks?', "Ships of the same class share a layout, so the same decks tend to be quiet or noisy on sister ships. Open a ship for its deck noise map."),
        ]
        h1 = f'{L["name"]}: which cabin to book'
        body = f'''<h1>{E(h1)}</h1><p class="answer">Cabin guides for {len(ss)} {E(L["short"])} ships{E(klass)}. Ships of the same class share a layout, so the same decks tend to be quiet or noisy across sister ships.</p>
<ul class="cards">{items}</ul><p class="note">Official fleet pages: {link((L["name"] + " ships", L["url"]))}. Which Cabin is independent and not affiliated with {E(L["name"])}.</p>
{faq_block(faqs)}{related(p)}'''
        desc = f'Which {L["short"]} cabin should I book? Quiet decks, seasickness picks and cabins to avoid on {len(ss)} ships, including {ss[0]["name"]}.'
        write(p, page(p, f'Which {L["short"]} Cabin Should I Book', desc, body, [article_ld(h1, p, ADDED), faq_ld(faqs)], [("/", "Home"), ("/lines/", "Cruise lines"), (p, L["short"])], modified=ADDED, og_type="article"))
        cards.append(f'<li class="card"><h2><a href="{u(p)}">{E(L["name"])}</a></h2><p>{", ".join(E(s["name"]) for s in ss)}</p></li>')
    faqs = [
        ("Which cruise line cabin should I book?", "Pick the line, then the ship. Each line page lists the quiet cabin decks and the deck under the pool for every ship we cover."),
        ("Which cruise lines are covered?", join_names(L["name"] for L in LINES.values()) + "."),
    ]
    h1 = "Cabin guides by cruise line"
    body = f'<h1>{h1}</h1><p class="answer">Choose a cruise line to see every ship we cover, with its quiet decks and the decks under the pool.</p><ul class="cards">{"".join(cards)}</ul>{faq_block(faqs)}{related("/lines/")}'
    write("/lines/", page("/lines/", "Which Cruise Line Cabin to Book", f"Which cruise line cabin should I book? Quiet decks and the deck under the pool on {len(LINES)} lines.", body, [article_ld(h1, "/lines/", ADDED), faq_ld(faqs)], [("/", "Home"), ("/lines/", "Cruise lines")], modified=ADDED, og_type="article"))

def guide(path, title, h1, desc, inner, faqs, srcs, modified=ADDED):
    body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}{faq_block(faqs)}<section class="sources"><h2>Sources</h2><ul>' + "".join(f"<li>{link(x)}</li>" for x in srcs) + f'</ul><p class="note">Retrieved {humandate(modified)}.</p></section>{related(path)}</article>'
    write(path, page(path, title, desc, body, [article_ld(h1, path, modified), faq_ld(faqs)], [("/", "Home"), (path, h1)], modified=modified, og_type="article"))

def guides():
    ex = ship_by("symphony-of-the-seas")
    guide("/guides/how-to-choose-a-cruise-cabin/", "Which Cruise Cabin Should I Book", "How to choose a cruise cabin",
      "How to choose a cruise cabin: pick the deck first, then the spot on the deck, then the room type. Quiet decks, seasickness, views and the cabins to avoid.", f'''
<div class="answer"><p><strong>Short answer:</strong> choose the deck first, then the position on the deck, then the room type. A cabin on a deck with cabins above and below, midship and away from elevators, beats a fancier room under the pool deck.</p></div>
<h2>1. Choose the deck</h2><p>Look at what is directly above and below the deck. The best cabin decks are sandwiched between other cabin decks. The worst for light sleepers sit directly under a pool, sports or buffet deck (deck chairs and set-up start early) or directly above a theatre, casino, nightclub or promenade (busy late). Our <a href="{u('/guides/quietest-cruise-cabins/')}">quietest decks table</a> lists the sandwiched decks for every ship we cover.</p>
<h2>2. Choose the spot on the deck</h2><ul><li><strong>Midship</strong> moves least in a swell and is close to the main elevators.</li><li><strong>Forward</strong> cabins feel the most pitching; the CDC advises avoiding the bow if you are prone to motion sickness. The lowest forward cabins are also close to the bow thrusters and anchor gear.</li><li><strong>Aft</strong> cabins can have wide wake views from corner balconies, and are often quiet at night, but some ships have more vibration at the stern.</li><li>Avoid cabins beside elevator lobbies, stair landings, laundry rooms and service doors (unlabelled blocks on the deck plan) if you are a light sleeper.</li></ul>
<h2>3. Choose the room type</h2><ul><li><strong>Interior:</strong> cheapest and darkest, good for sleep. Some ships sell virtual-window or promenade-view interiors.</li><li><strong>Oceanview:</strong> a window, which helps with seasickness because you can see the horizon.</li><li><strong>Balcony:</strong> private outdoor space. Read the category: inward-facing, promenade-view and partial-view balconies cost less but give a different view.</li><li><strong>Suites and ship-within-a-ship areas</strong> (The Haven, MSC Yacht Club, The Retreat, Disney Concierge) add space and private areas.</li></ul>
<h2>4. Check the category name for warnings</h2><p>Lines flag compromises in the category name or on the deck plan legend: "partial view", "obstructed view", "inward facing", "promenade view". Cabins one deck above the lifeboats are the usual obstructed-view rooms.</p>
<h2>5. Guarantee cabins</h2><p>A guarantee fare means the line picks your cabin within a category. It is cheaper, but you cannot choose the deck, so it is a poor bet for light sleepers or anyone prone to seasickness.</p>
<h2>Worked example: {E(ex["name"])}</h2><p>On <a href="{u(ship_path(ex))}">{E(ex["name"])}</a>, decks {E(rng(ex["_quiet"]))} are the sandwiched cabin decks, while deck {E(rng(ex["_pool"]))} sits directly under the pool and sports deck. So a midship balcony on deck {E(ex["_quiet"][len(ex["_quiet"]) // 2])} is a strong all-round pick.</p>
<h2>Ship-by-ship guides</h2><p>See the <a href="{u('/ships/')}">full list of ship guides</a>.</p>''',
      [("What is the best location for a cruise cabin?", "Midship, on a deck with cabin decks directly above and below, and away from elevators and service doors. That combination gives the least motion and the least noise."),
       ("Is it better to be on a high or low deck on a cruise ship?", "Lower decks move less in rough seas, which helps with seasickness. Higher decks are closer to the pools and buffet and often have more balcony cabins. The deck directly under the pool deck is the one to avoid if you sleep lightly."),
       ("Are aft cabins good on a cruise?", "Aft cabins can have large wake-view balconies and are often quieter at night. Some ships have more vibration and motion at the stern than midship, so if you are prone to seasickness choose midship instead."),
       ("Should I book a guarantee cabin?", "Only if price matters more than location. With a guarantee fare the line assigns the cabin, so you cannot avoid noisy or forward decks.")],
      [CDC] + [(f'{LINES[s["line"]]["name"]}: {s["name"]} deck plans', s["official"]) for s in SHIPS[:3]])

    guide("/guides/best-cabin-for-seasickness/", "Which Cabin Is Best for Seasickness", "Best cruise cabin location for seasickness",
      "The best cruise cabin for seasickness is low and midship with a view of the horizon. Why, what the CDC says, and the exact decks on each ship.", f'''
<div class="answer"><p><strong>Short answer:</strong> book a cabin midship on one of the lowest passenger decks, with a window or balcony if you can. That is where the ship moves least, and a view of the horizon reduces symptoms.</p></div>
<h2>Why low and midship</h2><p>A ship pitches around its middle, so the ends move most and the middle least. The CDC's guidance on motion sickness lists avoiding the locations of maximum motion, such as the bow of a ship, and getting a visual horizon reference among the behavioural countermeasures. Higher decks also sway more in a roll than lower ones.</p>
<h2>Window or no window?</h2><p>The CDC lists obtaining a visual horizon reference as one of the measures shown to give some protection on ships. An oceanview or balcony cabin lets you see the horizon; an interior cabin does not, though you can head to a low, midship public deck with windows instead.</p>
<h2>Lowest cabin decks, ship by ship</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Ship</th><th scope="col">Lowest cabin decks</th></tr></thead><tbody>{"".join(f'<tr><td><a href="{u(ship_path(s))}">{E(s["name"])}</a></td><td>{E(rng(s["_cab"][:2]))}</td></tr>' for s in SHIPS)}</tbody></table></div>
<p class="note">Low decks can share space with dining rooms, kids' clubs or the medical centre, and the lowest forward cabins are near the bow thrusters, so check each ship's page for the trade-offs.</p>
<h2>Other things that help</h2><p>Medication and behavioural tips are covered in the CDC's guidance. This page is general information, not medical advice: talk to a doctor or pharmacist about medication before you sail.</p>''',
      [("Where should I book a cabin if I get seasick?", "Midship on the lowest passenger decks, ideally with a window or balcony so you can see the horizon."),
       ("Is an aft cabin bad for seasickness?", "Aft is better than forward but usually worse than midship, because the ends of the ship move more when it pitches."),
       ("Do balcony cabins help with seasickness?", "They can. The CDC lists a visual horizon reference among the countermeasures shown to give some protection on ships, and a balcony or window gives you one.")],
      [CDC])

    guide("/guides/cruise-cabins-to-avoid/", "Which Cruise Cabins Should I Avoid", "Cruise ship cabins to avoid",
      "Which cruise cabins to avoid: under the pool deck, over the theatre or nightclub, forward low decks, next to elevators, connecting doors and partial views.", f'''
<div class="answer"><p><strong>Short answer:</strong> avoid cabins directly under a pool, sports or buffet deck, directly over a theatre, casino or promenade, low and forward near the thrusters, beside elevators or service doors, and any category labelled partial or obstructed view.</p></div>
<ol class="steps"><li><strong>Under the pool or Lido deck.</strong> Deck chairs, cleaning and set-up start early. Every ship page lists the deck that sits directly under the pools.</li>
<li><strong>Over the theatre, casino, nightclub or promenade.</strong> These stay busy late. Bass carries upward through the structure.</li>
<li><strong>Under the running track or sports court.</strong> Footsteps and ball games overhead.</li>
<li><strong>Low and forward.</strong> Closest to the bow thrusters and anchor gear, which can be loud when docking, and forward cabins feel the most motion.</li>
<li><strong>Next to elevators, stair landings and crew doors.</strong> Foot traffic and doors banging. Unlabelled blocks on a deck plan are usually service areas.</li>
<li><strong>Connecting cabins</strong> if you are not travelling with the people next door: the connecting door lets more sound through than a wall.</li>
<li><strong>Partial or obstructed view.</strong> Usually lifeboats or structure in the way. Lines label these, so read the category name.</li>
<li><strong>Inward-facing or promenade-view balconies</strong> if you want a sea view. They overlook an inside neighbourhood or promenade instead.</li></ol>
<h2>Decks directly under the pool, ship by ship</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Ship</th><th scope="col">Cabin deck under pool, sports or buffet areas</th></tr></thead><tbody>{"".join(f'<tr><td><a href="{u(ship_path(s))}">{E(s["name"])}</a></td><td>{E(rng(s["_pool"])) or "None directly under"}</td></tr>' for s in SHIPS)}</tbody></table></div>''',
      [("Which cabin is the worst on a cruise ship?", "For most people, a cabin directly under the pool deck or directly above a nightclub or theatre, because of noise. For people prone to seasickness, a low forward cabin."),
       ("Are cabins near the elevator bad?", "They are convenient but get more foot traffic and noise. A few doors away from the elevator lobby gives you most of the convenience with less noise."),
       ("What does obstructed view mean on a cruise?", "Something, usually a lifeboat or part of the ship's structure, blocks some of the window or balcony view. Lines price and label these cabins separately.")],
      [CDC] + [(f'{LINES[s["line"]]["name"]}: {s["name"]} deck plans', s["official"]) for s in SHIPS[6:9]])

    rows = "".join(f'<tr><td><a href="{u(ship_path(s))}">{E(s["name"])}</a></td><td>{E(LINES[s["line"]]["short"])}</td><td>{E(rng(s["_quiet"])) or "None"}</td><td>{E(rng(s["_pool"])) or "None"}</td></tr>' for s in SHIPS)
    guide("/guides/quietest-cruise-cabins/", "Which Cruise Cabin Decks Are Quietest", "The quietest cabin decks on every big cruise ship",
      f"The quietest cabin decks on {len(SHIPS)} big cruise ships: decks with cabins directly above and below, plus the deck under the pools to avoid.", f'''
<div class="answer"><p><strong>Short answer:</strong> the quietest cabins are on decks that have other cabin decks directly above and below. This table lists those decks for every ship we cover, plus the cabin deck that sits directly under the pool, sports or buffet areas.</p></div>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Ship</th><th scope="col">Line</th><th scope="col">Quiet cabin decks</th><th scope="col">Cabin deck under pools/sports</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>How we worked it out</h2><p>For each ship we took the deck-by-deck listing of the current deck plan and marked each deck as cabins, public venues or a mix. A cabin deck counts as quiet when the decks directly above and below are also cabin decks. It is a deck-level shortcut: a venue may only fill part of a deck, so a cabin at the far end can still be quiet. Details on our <a href="{u('/methodology/')}">sources and methods</a> page.</p>
<p>You may cite or link this table with a credit to Which Cabin.</p>''',
      [("What is the quietest cabin on a cruise ship?", "A midship cabin on a deck with cabin decks directly above and below, a few doors from the elevators and not next to a connecting door or service area."),
       ("Are higher decks quieter on a cruise ship?", "Not automatically. The top cabin deck is often directly under the pool or sports deck. The quietest decks are usually in the middle of the ship's cabin block.")],
      [(f'CruiseMapper: {s["name"]} deck plans', DECKS[s["cm"]]["index"]) for s in SHIPS[:4]] + [(f'{LINES[s["line"]]["name"]}: {s["name"]} deck plans', s["official"]) for s in SHIPS[:4]])

def home():
    lines = "".join(f'<li class="card"><h3><a href="{u("/lines/" + k + "/")}">{E(L["name"])}</a></h3><p>' + ", ".join(f'<a href="{u(ship_path(s))}">{E(s["name"])}</a>' for s in SHIPS if s["line"] == k) + '</p></li>' for k, L in LINES.items())
    faqs = [
        ("Which cabin should I book on a cruise?", "Choose the deck first, then the spot on the deck, then the room type. A cabin on a deck with cabins above and below, midship and away from elevators, beats a fancier room under the pool deck."),
        ("Which deck is the quietest on a cruise ship?", "The quietest cabin decks have other cabin decks directly above and below. Each ship page maps those decks, and the quietest-decks guide lists them for every ship we cover."),
        ("Which cabin is best if I get seasick?", "Book a midship cabin on one of the lowest passenger decks, with a window or balcony if you can, so you can see the horizon."),
    ]
    body = f'''<section class="hero"><h1>Which cabin should you book on your cruise ship?</h1>
<p class="answer">Deck-by-deck guides to the best cabins and the ones to avoid on {len(SHIPS)} of the biggest cruise ships. We map what is above and below every cabin deck from published deck-by-deck listings, with a link to each line's own deck plan, so you can ask for a quiet cabin before you book.</p>
<p class="btnrow"><a class="btn" href="{u('/ships/')}">Find your ship</a> <a class="btn alt" href="{u('/guides/how-to-choose-a-cruise-cabin/')}">How to choose a cabin</a></p></section>
<h2>Ships by cruise line</h2><ul class="cards">{lines}</ul>
<h2>Guides</h2><ul class="cols"><li><a href="{u('/guides/how-to-choose-a-cruise-cabin/')}">How to choose a cruise cabin</a></li><li><a href="{u('/guides/quietest-cruise-cabins/')}">The quietest cabin decks on every ship</a></li><li><a href="{u('/guides/best-cabin-for-seasickness/')}">Best cabin location for seasickness</a></li><li><a href="{u('/guides/cruise-cabins-to-avoid/')}">Cruise cabins to avoid</a></li></ul>
<h2>How it works</h2><p>For every ship we take the deck-by-deck listing of the current deck plan, mark each deck as cabins, public venues or a mix, and flag cabin decks that sit directly under pools and sports areas or over bars and theatres. Then we add ship-specific tips and cite every source. We are independent: no cruise line pays for coverage. <a href="{u('/methodology/')}">Sources and methods</a>.</p>
{faq_block(faqs)}'''
    write("/", page("/", "Which Cabin Should I Book on a Cruise", f"Which cabin and deck to book on {len(SHIPS)} big cruise ships, and which to avoid: deck noise maps, seasickness picks and quiet decks.", body, [faq_ld(faqs)], modified=ADDED))

def simple(path, title, desc, h1, inner, crumb=None, noindex=False, modified=TODAY):
    write(path, page(path, title, desc, f'<article class="prose"><h1>{E(h1)}</h1>{inner}</article>', None, [("/", "Home"), (path, crumb or h1)], noindex=noindex, modified=modified))

def about_legal():
    lines = ", ".join(L["name"] for L in LINES.values())
    simple("/about/", f"About {BRAND}", "What Which Cabin is, how we pick cruise cabin advice and how we check it.", "About Which Cabin", f'''
<p>Which Cabin is an independent guide to choosing a cabin on the biggest cruise ships. Most cruise sites tell you about the ship; we answer one question: which cabin and deck should you ask for, and which should you avoid?</p>
<h2>What we cover</h2><p>{len(SHIPS)} ships from {E(lines)}. We add ships when we can check their layout against the line's own deck plan.</p>
<h2>How we work</h2><p>Every ship page starts from the deck-by-deck layout of the current deck plan, which we turn into an original deck noise map. Ship facts come from cited sources. We write every tip ourselves and leave out anything we cannot verify. See <a href="{u('/methodology/')}">sources and methods</a>.</p>
<h2>Independence</h2><p>Which Cabin is not affiliated with, endorsed by or sponsored by any cruise line. Ship and line names are used only to identify the ships we describe.</p>
<p>Spotted something out of date after a refit? <a href="{u('/contact/')}">Tell us</a> and we will re-check it.</p>''', modified=ADDED)
    simple("/methodology/", f"Sources and Methods | {BRAND}", "Where Which Cabin's deck layouts, ship facts and cabin advice come from, and how the deck noise map is built.", "Sources and methods", f'''
<h2>Deck layouts</h2><p>For each ship we use the deck-by-deck listing on <a href="https://www.cruisemapper.com/deckplans" rel="nofollow noopener">CruiseMapper</a>, which summarises what is on every deck of the line's current deck plan, and we link the cruise line's own deck plan page on every ship page. The first 25 ships were checked on 15 Nov 2026. Ships added after that were checked on 16 Nov 2026. Each ship page shows its own checked date.</p>
<h2>The deck noise map</h2><p>We mark each deck as a cabin deck, a public deck or a mix. A cabin deck is marked quiet (green) when the decks directly above and below are also cabin decks with no listed venues. It is marked amber when it shares space with venues, sits directly below pools, sports, buffet or similar areas, or sits directly above bars, shops, theatres, dining or entertainment. Bridge, medical and crew areas are treated as neutral. This is a deck-level shortcut: a venue may only fill part of a deck, so always look up your exact cabin number on the line's deck plan.</p>
<h2>Ship facts</h2><p>Class, builder, entry into service, gross tonnage and guest capacity come from each ship's Wikipedia infobox (which cites registers and line fact sheets) or the line's own pages, as credited on each page. If a figure was missing or unclear, we left it out.</p>
<h2>General advice</h2><p>Motion advice follows the <a href="{CDC[1]}" rel="nofollow noopener">CDC Yellow Book chapter on motion sickness</a>. Other tips (noise from pool decks, elevators, connecting doors, partial-view categories) are our general guidance, not cruise line rules.</p>
<h2>What we do not do</h2><p>We do not copy deck plan images or cruise line text. Diagrams on this site are our own. We do not publish prices or availability, which change daily.</p>
<h2>Updates</h2><p>Ships get refitted and categories change. <a href="{u('/contact/')}">Report an error</a> and we will re-check the source.</p>''', "Sources and methods", modified=ADDED)
    simple("/image-policy/", f"Image Policy | {BRAND}", "How Which Cabin creates and credits images and diagrams.", "Image policy", f'''
<p>Last updated {TODAY_H}.</p><h2>Diagrams</h2><p>Deck noise maps and charts on Which Cabin are original diagrams generated by us from cited facts. They are not copies of any cruise line's deck plan artwork.</p>
<h2>Photos</h2><p>The site currently uses no ship photos. We do not use cruise line photos or deck plan images without permission.</p>
<h2>AI-generated images</h2><p>If we add AI-generated illustrations, each will carry a visible "AI-generated image" credit, will not depict real people, and will never be presented as a photo of a real ship or cabin.</p>
<h2>Logos and trademarks</h2><p>We do not display cruise line logos. Names are used only to identify ships.</p>
<h2>Questions</h2><p>If you believe an image on this site uses your work, see our <a href="{u('/copyright/')}">copyright policy</a> or <a href="{u('/contact/')}">contact us</a>.</p>''', "Image policy")
    contact = f'''<p>Questions, corrections after a refit, or a ship you want us to cover next? Send a message and we will reply by email.</p>
<h2>Corrections</h2><p>Include the page address, what looks wrong and, if you can, a link to the cruise line's deck plan that shows it. We update the "checked" date when we re-verify.</p>
<p class="form-status" id="contact-status" role="status" hidden></p>
<form class="contact" id="contact-form" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Which Cabin contact"><input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{SITE_URL}contact/?sent=1">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<input type="hidden" name="_captcha" value="false">
<label for="name">Name</label><input id="name" type="text" name="name" required autocomplete="name">
<label for="email">Email</label><input id="email" type="email" name="email" required autocomplete="email">
<label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea>
<button class="btn" type="submit">Send message</button></form>
<p class="note">Messages are delivered by FormSubmit (formsubmit.co), a form-to-email service. See our <a href="{u('/privacy/')}">privacy policy</a>.</p>'''
    simple("/contact/", f"Contact {BRAND}", "Contact Which Cabin with questions, corrections or ship requests.", "Contact us", contact, "Contact")
    D = TODAY_H
    legal = {
    "/terms/": ("Terms of Use", f'''<p>Last updated {D}. These terms govern your use of whichcabin.com ("Which Cabin", "we", "us"). Which Cabin is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company. By using the site you agree to these terms.</p>
<h2>Information only</h2><p>Which Cabin provides general information to help you plan a cruise. It is not travel, medical or professional advice. Ship layouts, cabin categories and onboard venues are set by each cruise line and can change at any time. Always check the cruise line's current deck plan and booking terms before you book.</p>
<h2>Accuracy</h2><p>We work to keep information accurate and cite our sources, but we make no warranty that any information is complete, current or error free.</p>
<h2>Acceptable use</h2><p>You may view and share links to our pages for personal, non-commercial use. You may not scrape the site in bulk, republish our original text or data compilations without permission, misuse the contact form, or try to disrupt the site.</p>
<h2>Intellectual property</h2><p>Original text, design, diagrams and data compilations on this site belong to Joshua Israel Ventures LLC. Cruise line and ship names and trademarks belong to their owners and are used only to identify the ships described. Their use does not imply affiliation or endorsement.</p>
<h2>Third-party links and services</h2><p>We link to cruise line websites, CruiseMapper, Wikipedia, the CDC and other sources, and use third-party services (GitHub Pages, Cloudflare, FormSubmit). We are not responsible for their content or practices.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided "as is" and "as available". To the fullest extent permitted by law, Joshua Israel Ventures LLC disclaims all warranties, express or implied, and will not be liable for any indirect, incidental, special, consequential or punitive damages, or any loss arising from your use of the site or any booking decision. Our total liability for any claim relating to the site is limited to US$100.</p>
<h2>Indemnity</h2><p>You agree to indemnify Joshua Israel Ventures LLC against claims arising from your misuse of the site or breach of these terms.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida, United States, without regard to conflict-of-law rules. Any dispute will be resolved in the state or federal courts located in Florida, and you consent to their jurisdiction.</p>
<h2>Changes</h2><p>We may update these terms. The date above shows the latest version. Questions: use our <a href="{u('/contact/')}">contact form</a>.</p>'''),
    "/privacy/": ("Privacy Policy", f'''<p>Last updated 16 Nov 2026. This policy explains how Which Cabin (whichcabin.com), a trade name of Joshua Israel Ventures LLC, a Florida limited liability company, handles information.</p>
<h2>Analytics</h2><p>On whichcabin.com we use Cloudflare Web Analytics and, if you accept, Google Analytics 4.</p>
<p>Cloudflare Web Analytics counts page views. It does not use cookies or local storage and does not track you across sites. It records basic, aggregated information such as the page visited, referrer, browser type and country. The launch site includes this beacon on every page.</p>
<p>Google Analytics 4 measures how the site is used. It does not load until you press Accept on the cookie banner, and only when a measurement id is set for the launch build. Before that choice we set Google Consent Mode v2 defaults to denied, including analytics storage, ad storage, ad user data and ad personalisation. If you accept, Google Analytics 4 may set cookies to recognise this browser. If you reject, we do not load it. Ad storage stays denied either way, because the site shows no ads. The Cookie settings link in the footer opens the banner again. We remember the choice in local storage on your device, not in a cookie of our own.</p>
<h2>Contact form</h2><p>If you use the contact form, your name, email address and message are sent through FormSubmit (formsubmit.co), a form-to-email service, so we can reply. We use them only to respond and keep them only as long as needed.</p>
<h2>Advertising</h2><p>The site shows no ads today. If we add ads in future, for example through Google AdSense, third-party vendors including Google may use cookies to serve ads based on your prior visits to this and other websites. You will be able to opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a> and <a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info/choices</a>. Where the law requires it (for example in the EEA, the UK and Switzerland), we will ask for consent through a certified consent management platform before any advertising cookies are set. We will update this policy before any ads go live.</p>
<h2>Cookies</h2><p>Which Cabin does not set its own cookies. Cloudflare Web Analytics does not use cookies. Google Analytics 4 may set cookies only after you accept. You can block or delete cookies in your browser. The site works if you reject analytics. Use Cookie settings in the footer to change your mind, or clear this site's data in your browser to forget the saved choice.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security and operations.</p>
<h2>Your rights</h2><p>You can ask us to access, correct or delete personal information we hold about you via the <a href="{u('/contact/')}">contact form</a>. Residents of some US states and other countries may have additional rights, which we will honour.</p>
<h2>Children</h2><p>The site is for a general audience and is not directed to children under 13. We do not knowingly collect personal information from children.</p>
<h2>Changes</h2><p>We will post any changes here with a new date.</p>'''),
    "/disclaimer/": ("Disclaimer", f'''<p>Last updated {D}.</p>
<h2>Not affiliated with any cruise line</h2><p>Which Cabin is an independent site. It is not affiliated with, endorsed by or sponsored by {E(lines)}, or any other cruise line, shipbuilder or booking site. All names and trademarks belong to their owners and are used only to identify the ships described.</p>
<h2>Layouts change: check the deck plan</h2><p>Deck layouts, venues and cabin categories can change after refits and between sailings. Our pages reflect the sources on the date shown. The cruise line's current deck plan and booking terms always take priority.</p>
<h2>No medical or professional advice</h2><p>Seasickness and other tips are general information. Talk to a doctor or pharmacist about motion sickness medication. Descriptions of noise and suitability are our opinions to help planning.</p>
<h2>Accuracy and corrections</h2><p>We cite our sources and leave out what we cannot verify, but errors can happen. Please <a href="{u('/contact/')}">report errors</a> and we will correct verified mistakes promptly.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, Joshua Israel Ventures LLC is not liable for any loss arising from reliance on this site. See our <a href="{u('/terms/')}">terms of use</a>.</p>'''),
    "/copyright/": ("Copyright and DMCA Policy", f'''<p>Last updated {D}. Original text, design, diagrams and data compilations on Which Cabin are owned by Joshua Israel Ventures LLC. Facts are cited to their sources. The site uses no cruise line photos or deck plan images; see our <a href="{u('/image-policy/')}">image policy</a>.</p>
<h2>Reporting infringement</h2><p>If you believe material on this site infringes your copyright, send a notice through our <a href="{u('/contact/')}">contact form</a> with: (1) your name and contact details; (2) a description of the copyrighted work; (3) the URL of the material on our site; (4) a statement that you have a good-faith belief the use is not authorised by the owner, its agent or the law; (5) a statement, under penalty of perjury, that the information is accurate and you are the owner or authorised to act for the owner; and (6) your physical or electronic signature. We will review notices promptly and remove or disable material where appropriate.</p>
<h2>Counter-notice</h2><p>If material you provided was removed and you believe this was a mistake, you may send a counter-notice through the contact form with the details required by 17 U.S.C. § 512(g).</p>
<h2>Repeat infringers</h2><p>We will act against repeat infringement where appropriate.</p>'''),
    "/ad-disclosure/": ("Advertising and Affiliate Disclosure", f'''<p>Last updated {D}. Which Cabin is free to use. At the moment the site shows no ads and contains no affiliate links. In future we may show advertising, for example through Google AdSense, or add affiliate links to booking sites.</p>
<p>If ads appear they will be clearly separate from our content and labelled. Advertisers will have no influence over our cabin advice. If we add affiliate links, we may earn a commission at no extra cost to you, and we will label those links.</p>
<h2>Editorial independence</h2><p>No cruise line or travel agency pays for coverage or for changes to our advice. Questions: use our <a href="{u('/contact/')}">contact form</a>.</p>'''),
    }
    for p, (t, inner) in legal.items():
        body = f'<article class="prose"><h1>{E(t)}</h1>{inner}<p class="legal-line">{LEGAL_LINE}</p></article>'
        write(p, page(p, f"{t} | {BRAND}", f"{t} for Which Cabin (whichcabin.com), the independent guide to choosing a cruise cabin.", body, None, [("/", "Home"), (p, t)]))

def not_found():
    body = f'<h1>Page not found</h1><p>That page has moved or never existed. Try the <a href="{u("/ships/")}">ship guides</a> or <a href="{u("/guides/how-to-choose-a-cruise-cabin/")}">how to choose a cruise cabin</a>.</p>'
    open(os.path.join(ROOT, "404.html"), "w").write(page("/404.html", f"Page not found | {BRAND}", "Page not found.", body, noindex=True))

def extras():
    cn = os.path.join(ROOT, "CNAME")
    if LAUNCH: open(cn, "w").write("whichcabin.com\n")
    elif os.path.exists(cn): os.remove(cn)
    open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w").write(INDEXNOW_KEY)
    bots = ["*", "Googlebot", "Bingbot", "Mediapartners-Google", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot", "CCBot"]
    open(os.path.join(ROOT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE_URL}sitemap.xml\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{url(p)}</loc><lastmod>{m}</lastmod></url>\n" for p, m in PAGES) + "</urlset>\n")
    ll = [f"# {BRAND}", "", f"> Which Cabin (whichcabin.com) tells cruise passengers which cabin and deck to book, and which to avoid, on {len(SHIPS)} of the biggest cruise ships. Each ship page has a deck noise map built from the current deck plan, quiet decks, seasickness picks and cited sources. Checked {TODAY_H}.", "", "Independent; not affiliated with any cruise line. Layouts change; confirm on the line's deck plan.", "", "## Guides",
          f"- [How to choose a cruise cabin]({url('/guides/how-to-choose-a-cruise-cabin/')})", f"- [Quietest cabin decks on every ship]({url('/guides/quietest-cruise-cabins/')})", f"- [Best cabin for seasickness]({url('/guides/best-cabin-for-seasickness/')})", f"- [Cruise cabins to avoid]({url('/guides/cruise-cabins-to-avoid/')})", f"- [Sources and methods]({url('/methodology/')})", "", "## Ships"]
    for s in SHIPS: ll.append(f"- [{s['name']}]({url(ship_path(s))}) ({LINES[s['line']]['short']}): quiet cabin decks {rng(s['_quiet']) or 'none'}; cabin deck under pools {rng(s['_pool']) or 'none'}")
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(ll) + "\n")
    open(os.path.join(ROOT, "favicon.svg"), "w").write(LOGO.replace('width="34" height="34" ', 'xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true" focusable="false"', ""))

if __name__ == "__main__":
    for s in SHIPS: ship_page(s)
    ships_index(); line_pages(); guides(); home(); about_legal(); not_found(); extras()
    print(len(PAGES), "pages", "LAUNCH" if LAUNCH else "PREVIEW")
