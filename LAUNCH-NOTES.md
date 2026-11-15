# Which Cabin (whichcabin.com): launch checklist

Status 15 Nov 2026: v1 built and live on the free preview https://joshuaofisrael.github.io/whichcabin/ (noindex on every page).
Repo: https://github.com/joshuaofisrael/whichcabin (branch main, folder /). Repo working copy on the box: /workspace/whichcabin.
Domain whichcabin.com chosen by Joshua 15 Nov 2026. NOT bought (Namecheap sign-in failed; Joshua will buy later). $0 spent.

Everything below is waiting on the domain. Do the steps in order.

## 1. Buy the domain (needs Joshua's yes on the exact price; never on Shabbat)
- Namecheap, whichcabin.com, 1 year: $12.08 + $0.20 ICANN fee = about $12.28 (renews about $15.98/yr). Free WHOIS privacy, auto-renew on.
- Log it straight away: P&L (/workspace/JI_Ventures_PnL.xlsx, LLC expense: domain, order number, amount, card) and the running total in /workspace/new-sites/evergreen-build-queue.md.

## 2. DNS in Namecheap (Domain List > Manage > Advanced DNS)
- Delete the default parking records (CNAME www -> parkingpage, URL redirect @).
- Add 4 A records on @: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- Add CNAME www -> joshuaofisrael.github.io.
- Add the Google Search Console TXT record on @ (step 5) at the same time to save a round trip.

## 3. Switch the repo to launch mode and enable the custom domain
```
cd /workspace/whichcabin && ./deploy.sh --launch "Launch on whichcabin.com"
```
This rebuilds with root paths (no /whichcabin prefix), removes noindex from every page, adds the Cloudflare beacon, writes the CNAME file (whichcabin.com), runs check.py --launch and the legal gate, then pushes.
- Set the custom domain: `gh api -X PUT repos/joshuaofisrael/whichcabin/pages -f cname=whichcabin.com`
- When the certificate is issued (check `gh api repos/joshuaofisrael/whichcabin/pages` until `https_certificate.state` is `approved`): `gh api -X PUT repos/joshuaofisrael/whichcabin/pages -F https_enforced=true`
- Verify: `dig +short whichcabin.com`, `dig +short www.whichcabin.com`, `curl -sI https://whichcabin.com/` and `https://www.whichcabin.com/` (both 200 or www -> apex redirect), `curl -s https://whichcabin.com/ | grep -c noindex` = 0.
- Note: after launch the github.io preview URL redirects to whichcabin.com automatically.

## 4. Cloudflare Web Analytics (beacon)
- The launch build already puts the shared JI Ventures Analytics 2 beacon token (eac63f2b..., the same token Coaster Map uses, requestHost match) on every page. Both CF accounts were at the Web Analytics site limit, so no new site entry was created; a site entry needs the live hostname anyway.
- Confirm the beacon loads on the live site, then add whichcabin.com (requestHost) to /workspace/seo/tools/cf_rum_live.py / the daily "Stats" site list and the traffic sheet (JI_Ventures_Traffic.xlsx). Check the next day that non-bot views appear.

## 5. Google Search Console
- Add a Domain property for whichcabin.com, put the TXT record in Namecheap, check with `dig +short TXT whichcabin.com`, verify, then submit https://whichcabin.com/sitemap.xml.

## 6. Bing
- Add the site in Bing Webmaster Tools (import from GSC is fine) and submit the sitemap.
- IndexNow: key file is already in the repo (https://whichcabin.com/6d99be0a8662d09dadd3f19d2857201e.txt). After launch run `./indexnow.sh` (all sitemap URLs) and expect HTTP 200/202.

## 7. Routines
- Add whichcabin.com to the Batched daily SEO routine site list (seo-growth-operator skill) and to the Monday 11:30 AM ET weekly SEO tuning pass.
- Add it to the Monday domain-expiry check (21-day lookahead) once bought.
- AdSense: not yet. Rule is apply once the site gets 100 views in one day (check ad-network requirements incl. domain age first). The privacy and ad-disclosure pages already say "no ads today" and will need the AdSense wording confirmed at that point.

## 8. Finish
- Mark line 1 in /workspace/new-sites/evergreen-build-queue.md DONE with date + domain; record status (domain, live URL, tracking live, GSC verified, sitemap submitted, Bing added, AdSense status).

## What v1 contains (15 Nov 2026)
- 25 ship pages (/ships/<slug>/): deck noise map (original diagram), quick answer, best cabins by traveller, ship tips, cabins to avoid, facts table, FAQ + FAQPage/Article/Breadcrumb JSON-LD, cited sources.
- 7 line hubs, ships index, 4 guides (how to choose, quietest decks table, seasickness, cabins to avoid), about, methodology, image policy, contact (FormSubmit), terms, privacy, disclaimer, copyright/DMCA, ad disclosure, 404, sitemap.xml (48 URLs), robots.txt (AI crawlers allowed), llms.txt, IndexNow key file.
- Legal gate: _build/legal_gate.py check -> 49 pages, 0 HOLD_REVIEW (15 Nov 2026).
- Sources retrieved 15 Nov 2026: CruiseMapper deck-by-deck listings (raw cache in /workspace/new-sites/whichcabin/raw/cm, not in the repo), cruise line deck plan pages, Wikipedia infoboxes, MSC Cruises fact pages, CDC Yellow Book (motion sickness).
