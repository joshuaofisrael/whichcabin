# Which Cabin (whichcabin.com)

Which cabin and deck to book, and which to avoid, on the biggest cruise ships. Static site, GitHub Pages (branch `main`, folder `/`).

- Status 15 Nov 2026: v1 PREVIEW at https://joshuaofisrael.github.io/whichcabin/ (noindex). Domain whichcabin.com chosen by Joshua 15 Nov 2026, not bought yet.
  Launch steps: /workspace/new-sites/whichcabin/LAUNCH.md on the box (copy in LAUNCH-NOTES.md).
- Build: `python3 _build/build.py` (preview) or `python3 _build/build.py --launch` (whichcabin.com: root paths, indexable, CF beacon, CNAME file). Then `python3 _build/check.py [--launch]` and `python3 _build/legal_gate.py check`.
  `./deploy.sh [--launch]` does build + check + legal gate + commit + push, and stops if the gate holds anything.
- Canonicals, sitemap, robots, llms.txt and JSON-LD always use https://whichcabin.com/. Preview mode only changes the link prefix (/whichcabin), adds noindex and leaves out the beacon and CNAME.
- Data (`_build/`): `ships.py` (25 ships: line, official deck plan URL, CruiseMapper id, Wikipedia title, facts, our own ship notes), `decks.json` (deck number, label and URL per deck from CruiseMapper's deck-by-deck listing, retrieved 15 Nov 2026; labels only, no copied text). Scraper and raw pages live outside the repo in /workspace/new-sites/whichcabin/.
- Deck noise map logic: `analyse()` in build.py. Cabin deck = quiet when the decks directly above and below are cabin/neutral decks with no venues; amber when it shares space with venues, sits under pool/sports/buffet decks or over bars/shops/theatres/dining.
- Rules: never add an unsourced spec; omit if unsure. No copied text or deck plan images. Diagrams are original. No prices or availability. Wording stays evergreen.
- IndexNow key: 6d99be0a8662d09dadd3f19d2857201e (key file in repo root). `./indexnow.sh` pings every sitemap URL (launch only).
- Contact form: FormSubmit hashed endpoint shared with sibling sites. Analytics: shared JI Ventures Analytics 2 beacon token (launch build only).
- Legal gate: `_build/legal_gate.py` (adapted from Pick Your Row's). HOLD_REVIEW items go to /workspace/content-review/queue.jsonl and drafts/whichcabin/.
