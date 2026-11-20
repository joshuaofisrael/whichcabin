# Ship data for Which Cabin. Facts only from the sources named in each entry; notes are our own words.
# facts: from the ship's Wikipedia infobox (retrieved 15 Nov 2026, or 16 Nov 2026 where "checked" says so) unless "src" says otherwise. Omit anything unverified.
# Deck labels for ships added 16 Nov 2026 were read from CruiseMapper's deck-plan index titles that day. No cabin numbers are stored here.
LINES = {
 "royal-caribbean": dict(name="Royal Caribbean", short="Royal Caribbean", url="https://www.royalcaribbean.com/cruise-ships"),
 "carnival": dict(name="Carnival Cruise Line", short="Carnival", url="https://www.carnival.com/cruise-ships"),
 "norwegian": dict(name="Norwegian Cruise Line", short="Norwegian", url="https://www.ncl.com/cruise-ships"),
 "msc": dict(name="MSC Cruises", short="MSC", url="https://www.msccruisesusa.com/"),
 "celebrity": dict(name="Celebrity Cruises", short="Celebrity", url="https://www.celebritycruises.com/cruise-ships"),
 "princess": dict(name="Princess Cruises", short="Princess", url="https://www.princess.com/en-us/ships-and-experience/ships"),
 "disney": dict(name="Disney Cruise Line", short="Disney", url="https://disneycruise.disney.go.com/ships/"),
 "virgin": dict(name="Virgin Voyages", short="Virgin", url="https://www.virginvoyages.com/ships"),
 "holland-america": dict(name="Holland America Line", short="Holland America", url="https://www.hollandamerica.com/en/us/cruise-ships"),
}
RCL = "https://www.royalcaribbean.com/cruise-ships/{}/deck-plans"
CCL = "https://www.carnival.com/cruise-ships/{}/deck-plans"
NCL = "https://www.ncl.com/cruise-ship/{}/deck-plans"
CEL = "https://www.celebritycruises.com/cruise-ships/{}/deck-plans"
PCL = "https://www.princess.com/en-us/ships-and-experience/ships/{}"
DCL = "https://disneycruise.disney.go.com/ships/deck-plans/{}/"
VV = "https://www.virginvoyages.com/ships/{}"
HAL = "https://www.hollandamerica.com/en/us/cruise-ships/{}"

# Shared, class-level notes (our own analysis of the deck layout; CruiseMapper deck pages are the fact source for venue positions)
OASIS = [
 ("Inward-facing balconies are a trade-off", "Oasis-class ships have balcony cabins that face into Central Park (deck 8 and up) and over the Boardwalk at the stern instead of out to sea. They are cheaper than ocean balconies and lively to look at, but you hear the neighbourhood below. CruiseMapper's deck notes flag Boardwalk-view balconies in particular for noise."),
 ("Promenade-view interiors on deck 7", "The interior cabins with windows onto the Royal Promenade sit beneath Park Café or Giovanni's Table on deck 8, according to CruiseMapper, so expect some restaurant noise during opening hours."),
 ("Forward deck 7 sits over the gym", "Forward oceanview and interior cabins on deck 7 are above the Vitality fitness centre on deck 6, where equipment noise can carry during gym hours."),
 ("AquaTheater suites face the show", "The AquaTheater suite categories sit at the stern overlooking the outdoor AquaTheater. Great for watching shows from your balcony; less good if you want quiet evenings."),
]
ICON = [
 ("Surfside is built for small children", "Surfside, at the stern on deck 7, is the neighbourhood designed for families with children under six, with a kids' water area, a carousel and family cabins nearby. Ideal if you have toddlers; skip it if you don't."),
 ("Check the balcony type", "Icon-class plans include Infinite Balcony categories (I1, I3, IF, IB) on decks 9 to 12 alongside classic balconies. They are not the same layout as a standard balcony, so read the line's room description before choosing."),
 ("Inward-facing balconies", "Categories marked Inward Facing Balcony (for example H3 to H5 on decks 12 and 14) look into the ship's neighbourhoods rather than out to sea."),
 ("Low decks near the big venues", "Cabins on decks 3 and 4 share space with the Music Hall, the main dining room, the casino and the Absolute Zero ice arena. Fine for heavy sleepers on a budget; not the pick for light sleepers."),
]
EXCELLENCE = [
 ("Deck 8 is the noisiest cabin deck", "Deck 8 mixes cabins with the promenade bars and the Havana area, and it sits right above the casino and shops on deck 7. CruiseMapper notes live Latin music at the Havana Bar in the evenings."),
 ("Family Harbor on deck 4", "Family Harbor cabins on deck 4 come with access to a lounge reserved for families, which makes the low deck a good family pick."),
 ("Top-deck thrills", "The BOLT roller coaster and the WaterWorks area are on the top decks (18 and 19). Cabins on deck 17 sit closest to that activity."),
]
PRIMA = [
 ("Solo travellers: the Studios", "Studio cabins for solo travellers (category T1 interiors) are on decks 12 and 13. They are interior rooms priced for one person."),
 ("The Haven is aft", "The Haven, NCL's keycard-access suite area, is at the stern on Prima-class ships, with its own sundecks and pools on decks 16 to 18."),
 ("Deck 9 sits over Ocean Boulevard", "Deck 9 is the first cabin deck above Ocean Boulevard on deck 8, the outdoor walkaround with pools and dining. Choose deck 10 or higher if you are a light sleeper."),
 ("Deck 5 is under the casino", "Deck 5 is the lowest cabin deck and sits directly below the casino and shops on deck 6."),
]
BREAKAWAY = [
 ("Solo travellers: the Studios", "Studio cabins for solo travellers are on decks 10 to 12 on Norwegian Encore and 10 to 11 on Norwegian Getaway, according to CruiseMapper's deck plans. Getaway's plan also shows a Studio Lounge reserved for studio guests."),
 ("Deck 8 is mixed", "Deck 8 has cabins plus the indoor promenade shops, and it sits above the entertainment and casino deck (7). Deck 9 cabins are one floor above those shops and bars."),
 ("The Haven is high up", "The Haven suites and their private sundeck are on the upper decks, mixed in with the main pool and sports areas."),
]
SEASIDE = [
 ("Deck 9 sits over the promenade", "Deck 9 cabins are directly above the waterfront promenade on deck 8, which has pools, bars and dining. Pick deck 10 to 14 if quiet matters."),
 ("Yacht Club is forward and high", "The MSC Yacht Club, the ship-within-a-ship suite area, is forward on the upper decks (16 to 19 according to MSC's deck plan PDF)."),
 ("Look for partial-view icons", "MSC's deck plan legend marks cabins with obstructed or partial views. Check the icon on the cabin number before you book a balcony on any deck."),
]
EDGE = [
 ("Know the Infinite Veranda", "Edge-class 'Edge Stateroom with Infinite Veranda' cabins (E1, E2 and single ES) build the veranda space into the room behind a window wall that opens, instead of a separate outdoor balcony. If you want a classic outdoor balcony with a chair and table, look at Sunset Veranda, Concierge Class or the suites instead."),
 ("Avoid the partial-view codes", "Celebrity lists partial-view versions of some categories, such as E3 and C3. If the view matters, book the non-partial category."),
 ("Deck 12 is under the pools", "Deck 12 is the top cabin deck and sits directly below deck 14 (there is no deck 13), home to the main pool, spa and sundeck."),
 ("The Magic Carpet", "The Magic Carpet is a platform that moves up and down the starboard side, used as a bar, restaurant and tender platform. It is part of the ship's profile, so check the deck plan if you are booking a starboard cabin near midship."),
]
SPHERE = [
 ("Cabana mini-suites on deck 9", "Reserve Collection Cabana Mini-Suites (C1, C2) are on deck 9, the Promenade deck, which also has the lobby and Lido Marketplace, so it is busier than the decks above."),
 ("Decks 11, 12 and 14 are the quiet core", "Decks 11, 12 and 14 have cabin decks directly above and below, the safest bet for light sleepers. Deck 10 is one floor above the busy Promenade deck, and deck 15 sits under the Sea View Terrace area on deck 16."),
 ("Top cabin decks meet the Dome", "Deck 17 has cabins plus the Dome and Lido pool area, and deck 18 above it has the Sanctuary and fitness area. Light sleepers should go lower."),
 ("Low decks share space", "Deck 6 mixes cabins with the spa and dining, and sits under the lounges on deck 7."),
]
ROYAL_P = [
 ("Deck 8 sits above the Promenade", "Deck 8 (Emerald) is the first cabin deck above the Promenade deck (7), with its bars and shops. Decks 9 to 14 are quieter."),
 ("Upper cabin decks share space with the pools", "Decks 16 and 17 mix cabins with the Lido pools, sundeck and kids' and teen areas."),
 ("Suites fore and aft", "Suites sit at the ends of the ship: CruiseMapper's deck plans show S3 suites aft and S5 suites forward on several decks."),
]
WISH = [
 ("Deck 2 is near the kids' clubs", "Deck 2 cabins share the deck with the kids' clubs and sit directly below dining venues on deck 3."),
 ("Decks 7 to 9 are the quiet core", "Decks 7, 8 and 9 have cabin decks above and below, the best choice for light sleepers and for families with nap-time toddlers."),
 ("Concierge rooms are by the pools", "Concierge categories (1 to 3) are on decks 10 to 13, near the pool decks, with the two-storey Tower Suite on decks 14 and 15."),
 ("Family rooms", "Deluxe Family Oceanview and Verandah categories (4A to 4E, 8B and 8C) sleep more people and are spread across decks 6 to 11."),
]

# Notes below are from the 16 Nov 2026 deck listings (what each deck label places above, below and beside the cabins).
QUANTUM = [
 ("Deck 3 shares space with the casino", "On every Quantum-class ship in this guide, deck 3 is a cabin deck that also lists the casino. Deck 4 above it is the lobby and shops."),
 ("Deck 6 is above Two70", "Deck 6 is the first full cabin deck above the Royal Promenade and Two70 lounge on deck 5, and the listing puts the helideck on deck 6 as well."),
 ("Kids share deck 11", "Deck 11 mixes cabins with the kids' area. On Anthem of the Seas and Ovation of the Seas the listing also puts a kids' area on deck 12."),
 ("Deck 13 is under the pool deck", "Deck 14 is the lido and pools. There is no deck between them, so deck 13 is directly underneath."),
 ("North Star is up top", "Deck 16 lists the North Star, RipCord and the FlowRider. Suites are on that deck on some ships in the class and not on others, so read the plan for the ship you are booking."),
]
FREEDOM = [
 ("Low decks sit with the ice rink and Studio B", "Deck 2 mixes cabins with the ice rink, and deck 3 mixes cabins with Studio B."),
 ("The pool deck is a cabin deck", "Deck 11 mixes cabins with the lido pools and sundeck. Deck 12 mixes cabins with the spa and the kids' and teen areas, and it sits under the sports deck."),
]
VOYAGER = [
 ("Low decks sit with the ice rink and Studio B", "Deck 2 mixes cabins with the ice rink, and deck 3 mixes cabins with Studio B. Deck 4 above that is the casino and lounge, with no cabins."),
 ("The pool deck is a cabin deck", "Deck 11 mixes cabins with the lido pools. Deck 12 mixes cabins with the kids' and teen areas and the spa, under the sports deck."),
]
VISTA = [
 ("Family Harbor is on deck 2", "The listing puts Family Harbor on deck 2, sharing that deck with cabins."),
 ("Havana is on deck 5", "Deck 5 mixes cabins with the Havana area and the promenade shops, and it sits directly above the casino and shops on deck 4."),
 ("Pools above and on the cabin decks", "Deck 10 mixes cabins with the lido pools. Deck 14 mixes cabins with SkyRide and SkyCourse, under the Serenity deck."),
]
VISTA_EX = [
 ("Promenade cabins on deck 5", "Deck 5 mixes cabins with the promenade and sits directly above the casino and shops on deck 4."),
 ("The lido and the top cabin deck", "Deck 10 mixes cabins with the lido pools. Deck 14 mixes cabins with the waterslides and ropes course, and it sits under the Serenity adults' deck."),
]
DREAM_C = [
 ("Low cabins, then a public block", "Decks 1 and 2 are cabin decks. Decks 3, 4 and 5 are the lobby, dining, teens, promenade, casino and shops, with no cabins in the listing."),
 ("Deck 10 is the pool cabin deck", "Deck 10 mixes cabins with the lido pools, and deck 11 mixes cabins with the kids' area, under the sports and WaterWorks decks."),
 ("Deck 9 is only a name in the listing", "Deck 9 is listed as Vista, with no cabins and no venues named. Check Carnival's plan for that deck before you count on deck 8 being fully enclosed by cabins."),
]
CONQUEST = [
 ("The promenade is deck 5", "Decks 1 and 2 are cabin decks. Deck 5 is the promenade, lounge, casino and shops, with no cabins."),
 ("Deck 9 is on the lido", "Deck 9 mixes cabins with the lido pools. Deck 10 mixes cabins with a waterslide and sits under the spa and sports deck."),
]
SUNSHINE = [
 ("Deck 5 is the noisy low deck", "Deck 5 mixes cabins with the promenade, lounge, casino and shops."),
 ("The lido starts at deck 9", "Deck 9 mixes cabins with the lido pools. Deck 10 mixes cabins with the spa, the kids' area and WaterWorks."),
]
BPLUS = [
 ("Deck 8 is the promenade cabin deck", "Deck 8 mixes cabins with the promenade shops and sits directly above the entertainment and casino deck."),
 ("The Haven is up with the pools", "Haven cabins are on the upper decks, mixed with sundecks and pools rather than in a separate quiet block."),
]
EPIC_N = [
 ("Cabins start above the promenade", "Decks 5, 6 and 7 are the lobby, entertainment, casino, promenade and shops. Deck 8 is the first cabin deck."),
 ("Studios on decks 11 and 12", "The listing puts Studio cabins on decks 11 and 12."),
 ("Deck 14 is under the waterpark", "Deck 15 is the lido, pools, sundeck and waterpark, with no cabins, so deck 14 (cabins, spa and kids) sits directly under it. Haven cabins are on decks 16 and 17, and the Vibe Beach Club is above them."),
]
AQUA_N = [
 ("Deck 5 is under the casino", "Deck 5 is the lowest cabin deck and sits directly below the casino and shops on deck 6."),
 ("Deck 9 is above the lido promenade", "Deck 8 is the promenade with the lido pools and shops, so deck 9 is the first cabin deck above that activity."),
 ("Studios on decks 12 and 13", "Studio cabins are listed on decks 12 and 13. Haven cabins share decks 16 and 17 with a sundeck and pools."),
]
JEWEL_N = [
 ("Deck 5 is under the casino", "Deck 5 is a full cabin deck directly below the casino and dining on deck 6."),
 ("A bar on deck 8", "Deck 8 mixes cabins with O'Sheehan's and sits above the promenade, lounge and shops on deck 7."),
 ("Haven on the top cabin decks", "Deck 12 is the spa, lido, pools, kids and teens, so deck 11 is directly under it. Deck 14 mixes Haven cabins with a sundeck and the Vibe Beach Club, and deck 15 continues the Haven."),
]
WORLD = [
 ("Deck 9 sits over the promenade", "Deck 9 is the first cabin deck above deck 8, which lists the promenade and the spa."),
 ("Two deck numbers are skipped", "The listing has no deck 13 and no deck 17, so deck 12 is directly below deck 14, and deck 16 is directly below deck 18, where the lido and pools are."),
 ("The top deck is the Yacht Club sundeck", "The highest deck lists the Yacht Club sundeck, waterslides and The Spiral. The cabin deck beneath it is the closest passenger deck to that activity."),
]
MERAVIGLIA = [
 ("Deck 8 is above the promenade", "Deck 7 lists the promenade, spa, Carousel Lounge and casino. Deck 8 is the first full cabin deck above it, and decks 9 to 13 are cabin decks, with the bridge on deck 14."),
]
SEASIDE_O = [
 ("Deck 9 is above the lido", "On this ship the promenade is deck 6. Deck 8 is the lido and spa, and deck 9 is the first cabin deck above that."),
 ("Yacht Club shares the pool deck", "Deck 16 lists suites, the Yacht Club lounge, a sundeck and the lido pools together. The waterslides and adventure trail are on deck 20."),
]
DIVINA_N = [
 ("A public block under the cabin stack", "Deck 5 mixes cabins with the lobby. Decks 6 and 7 are restaurants, the casino, shops, the promenade and a lounge. Deck 8 is the first cabin deck above them."),
 ("Deck 13 is under the lido", "Deck 14 is the lido, pools and spa, so deck 13 sits directly under it. Yacht Club areas are listed on decks 15 and 16 with the kids' pool, sports and a waterslide."),
]
SOLSTICE = [
 ("Deck 6 starts the cabin stack", "Decks 4 and 5 are the promenade, casino, entertainment and shops. Deck 6 is the first of the cabin decks that run up through deck 11."),
 ("The lawn is deck 15", "Deck 15 lists the lawn, sports and the kids' and teen areas, above the lido deck."),
]
ROYAL_CORE = [
 ("Deck 8 sits above the Promenade", "Deck 8 (Emerald) is the first cabin deck above the Promenade deck (7), with its bars and shops."),
 ("Upper cabin decks meet the pools", "Deck 16 mixes cabins with the lido pools, and deck 17 mixes cabins with the sundeck and the kids' and teen areas."),
]
ROYAL_RM = [
 ("Deck 8 sits above the Promenade", "Deck 8 (Emerald) is the first cabin deck above the Promenade deck (7)."),
 ("Deck 16 is under the activity deck", "Deck 16 mixes cabins with the lido pools and sits directly below deck 17, which the listing gives to the sundeck, the adults' area, kids and teens, with no cabins on 17."),
]
RUBY_N = [
 ("Cabins start on deck 5", "Deck 5 mixes cabins with the plaza, dining and the lobby, under the casino and shops on deck 6."),
 ("A pool on deck 14", "Deck 14 mixes cabins with the bridge and a pool. Deck 15 mixes cabins with the lido pools, under the sundeck and spa on deck 16."),
]
DREAM_D = [
 ("Deck 2 shares a restaurant", "Deck 2 mixes cabins with Enchanted Garden and sits directly below the lobby, shops and dining on deck 3."),
 ("Kids and teens on deck 5", "Deck 5 mixes cabins with the kids' and teen clubs. Decks 6 to 10 are cabin decks, with the bridge on deck 10, under the lido, pools and spa on deck 11."),
]
MAGIC_D = [
 ("Deck 5 is the kids' deck", "Deck 5 mixes cabins with the kids' club and sits above the promenade and shops on deck 4."),
 ("Deck 8 is under the lido", "Deck 9 is the lido, pools and spa, so deck 8 is directly underneath. Deck 10 above that is the adults' area, sports and a waterslide."),
]
LADY = [
 ("Deck 5 shares the spa", "Deck 5 mixes cabins with the spa and a dining venue. Decks 6 and 7 are the lounge, casino, shops and lobby, with no cabins."),
 ("A long cabin run, then the pool", "Decks 8 to 14 are cabin decks, with the bridge on deck 14. Deck 15 mixes suites with the lido pools and sundeck. Decks 16 and 17 are sports, sundeck, the helideck and a jogging track."),
]
PINNACLE = [
 ("Cabins above a short public block", "Deck 1 mixes cabins with the lobby. Decks 2 and 3 are lounges, shops, the casino and dining. Decks 4 to 8 are cabin decks, with the bridge on deck 8."),
 ("Deck 8 is under the lido", "Deck 9 is the lido, pools, spa and sundeck, so deck 8 sits directly under it. Deck 10 mixes cabins with the kids' and teen areas, and deck 11 mixes cabins with sports."),
 ("The Retreat is deck 12", "Deck 12 lists the Explorations Lounge, The Retreat and an adults' sundeck, with no cabins."),
]
SIGNATURE = [
 ("Deck 1 includes the lobby", "Deck 1 mixes cabins with the lobby. Decks 2 and 3 are the promenade, casino, lounge, shops and dining."),
 ("Deck 8 is under the lido", "Decks 4 to 8 are cabin decks, and deck 7 also lists a suite lounge. Deck 9 is the lido, pools and spa, so deck 8 is directly under it."),
 ("Kids on deck 10, Crow's Nest on deck 11", "Deck 10 mixes cabins with the kids' and teen areas. Deck 11 mixes cabins with the observation area, sports and the Crow's Nest."),
]

# Ship-only notes added 20 Nov 2026. Facts are from the source named in the sentence.
# Rendered above the shared class notes so sister ships do not read as copies.
SHIP_EXTRA = {
 "freedom-of-the-seas": [
  ("A larger ship than Mariner, not a copy of it",
   "Freedom of the Seas is Freedom class, not Voyager class. Wikipedia's infobox, checked 20 Nov 2026, lists a length of 338.774 metres, gross tonnage of 156,271 since 2015 (154,407 from 2006 to 2015), and 3,782 guests at double occupancy, with a maximum of 4,515. Mariner of the Seas, on the same check, is listed at 311.12 metres and 139,863 gross tons, with capacity shown as 3,114 passengers and not labelled double occupancy. The waterline beam is about 38.6 metres on both infoboxes. Freedom's extreme beam, including the bridge wings, is listed at 56.08 metres, against Mariner's maximum beam of 48.0 metres. The quiet-deck shortcut can look similar. The ships are not the same size."),
  ("Deck labels re-checked 20 Nov 2026",
   "CruiseMapper's Freedom of the Seas deck-plan index, opened 20 Nov 2026, still labels deck 4 as casino, lounge and dining, with no cabins. Liberty of the Seas puts cabins on that deck. Freedom's deck 5 label is promenade, lobby, shops and the helideck, with no dining room in the label. Mariner's deck 5 label on the same day includes a third dining room. Freedom's deck 15 label is still Royal Escape Room, and that deck has no cabins. The cabin-deck map on this page did not need a redraw."),
  ("What the 2020 refit changed, and what January 2025 did not",
   "CruiseMapper's Amplified notes, still on that page, record the conversions already easy to miss on a class diagram: the deck 2 conference center became 25 inside cabins, the deck 3 On Air Club became 12 inside cabins, the deck 6 loyalty desk became 4 inside cabins, and an aft suite on deck 6 was replaced with 4 balcony cabins. The new deck 2 rooms share a deck with the ice rink. The new deck 3 rooms share a deck with Studio B and a dining room. CruiseMapper's overview also dates a later refurbishment to January 2025. It does not show a new cabin deck in the 20 Nov 2026 labels, so this page keeps the same noise map and records the date."),
 ],
 "mariner-of-the-seas": [
  ("Shorter, earlier, and a different class",
   "Mariner of the Seas entered service on 16 November 2003, built at Kvaerner Masa-Yards in Turku. Wikipedia's infobox, checked 20 Nov 2026, lists 139,863 gross tons, a length of 311.12 metres and a maximum beam of 48.0 metres, and it shows capacity as 3,114 passengers without calling that figure double occupancy. Freedom of the Seas, checked the same day, is a later Freedom-class ship: 338.774 metres, 156,271 gross tons since 2015, and 3,782 guests at double occupancy. Treat the shared 'ice rink below, pools above' pattern as a family resemblance, then use the numbers and the deck labels below."),
  ("The 2018 drydock moved cabins, not just slides",
   "CruiseMapper's refurbishment review dates Mariner's Royal Amplified drydock to 8 May through 24 June 2018 in Freeport. On deck 3, The Golden Room and Dragon's Lair, both nightclubs, were converted into staterooms. Deck 4, which has no cabins in the current label, became Izumi and Playmakers. Deck 12 aft gained the Slashaway Bay children's aqua park in place of the outdoor youth area. Deck 15 lost the Skylight Chapel and gained The Observatorium escape room. Deck 13 gained the Cyclone and Typhoon slides and a FlowRider. The new deck 3 cabins are the detail that changes a booking: they sit on a deck that still lists Studio B and a dining room, not in the quiet run of decks 6 to 10."),
  ("A March 2026 refit, with the same cabin decks",
   "CruiseMapper's Mariner overview, checked 20 Nov 2026, dates a later refurbishment to March 2026. The deck labels that day still match this page: deck 2 cabins with the ice rink, deck 4 casino, lounge and dining with no cabins, deck 5 promenade plus a dining room Freedom's label does not list, and deck 15 an escape room with no cabins. Until Royal Caribbean's own plan shows a cabin deck added or removed, the noise map stands, with the March 2026 date noted beside it."),
 ],
 "carnival-celebration": [
  ("In service November 2022, and not the same ship as Jubilee",
   "Wikipedia's infobox for Carnival Celebration, checked 20 Nov 2026, lists completion on 2 November 2022, a maiden voyage on 6 November 2022, builder Meyer Turku, 183,521 gross tons, and 5,374 guests at double occupancy (6,500 maximum). Carnival Jubilee's infobox on the same check lists completion on 4 December 2023, builder Meyer Werft in Papenburg, the same 183,521 gross tons, and 5,228 guests at double occupancy (6,631 maximum). Same class tonnage. Different year, different yard, different double-occupancy count."),
  ("The Gateway sits under the first busy cabin deck",
   "Carnival's Celebration ship page, checked 20 Nov 2026, describes six zones and names The Gateway as one of them. It does not number the decks. CruiseMapper's deck index the same day does: deck 6 is lobby, shops, lounge and Gateway, and deck 7 is casino, shops and Gateway, with no cabins on either. Deck 8 is cabins, the promenade and Havana. Jubilee's index uses Currents on decks 6 and 7, and it adds The Shores to the deck 8 label beside Havana. On Celebration, a deck 8 cabin is the room directly above the Gateway casino level and beside Havana, not beside a zone called The Shores."),
  ("Suite access and the Family Harbor lounge",
   "Carnival's page says a Carnival Excel suite includes access to Loft 19, the retreat with an infinity whirlpool on the top of the ship. CruiseMapper still labels deck 19 as Loft 19 and the BOLT coaster, with no cabins, so deck 17 remains the cabin deck nearest that activity. The same Carnival page places Family Harbor staterooms near the Family Harbor Lounge. CruiseMapper still puts Family Harbor on deck 4 with cabins and the kids' area. CruiseMapper also counts 2,641 staterooms on Celebration, against 2,626 on Jubilee. Those are room counts, not the double-occupancy figures above."),
 ],
 "carnival-jubilee": [
  ("Third Excel ship, different yard, fewer double-occupancy berths",
   "Wikipedia's infobox for Carnival Jubilee, checked 20 Nov 2026, lists completion on 4 December 2023, a maiden voyage on 23 December 2023, builder Meyer Werft in Papenburg, 183,521 gross tons, and 5,228 guests at double occupancy (6,631 maximum). Celebration, checked the same day, is Meyer Turku, in service from November 2022, with 5,374 guests at double occupancy. The gross tonnage matches. The yard, the year and the double-occupancy count do not. Carnival's Jubilee page calls this the ship that follows Mardi Gras and Celebration."),
  ("Currents and The Shores are the zones Celebration's labels do not use",
   "Carnival's Jubilee page, checked 20 Nov 2026, says two of the six zones, Currents and The Shores, are the new ones. It describes Grand Central, the atrium, and names Emeril's Bistro 717. It does not assign deck numbers. CruiseMapper's index that day labels deck 6 as lobby, shops, lounge and Currents, and deck 7 as casino, shops and Currents, with no cabins. Deck 8 is cabins, the promenade, Havana and The Shores. Celebration's deck 8 label stops at Havana. A Jubilee cabin on deck 8 shares the deck with Havana and The Shores and sits above the Currents casino level."),
  ("Same skeleton, a smaller stateroom count",
   "CruiseMapper's Jubilee index, checked 20 Nov 2026, counts 2,626 staterooms, against 2,641 on Celebration. Family Harbor is still on deck 4 with cabins and the kids' area, which matches Carnival's line that Family Harbor staterooms sit near that lounge. Deck 19 is still Loft 19 and BOLT, with no cabins, so deck 17 is still the cabin deck under the coaster and the adult Serenity area on deck 18. Use Jubilee's own labels for the neighbourhood names. Do not copy them across from Celebration."),
 ],
}

SHIP_FAQS = {
 "freedom-of-the-seas": [
  ("Is Freedom of the Seas the same layout as Mariner of the Seas?",
   "No. Freedom is Freedom class and longer: Wikipedia lists 338.774 metres and 156,271 gross tons, against Mariner's 311.12 metres and 139,863 gross tons. CruiseMapper's labels on 20 Nov 2026 also differ on deck 5 (no dining room in Freedom's label) and on deck 4 (no cabins on Freedom; Liberty, not Mariner, is the sister with cabins there)."),
  ("Did Freedom of the Seas change cabins after the 2020 refit?",
   "CruiseMapper's Amplified notes say yes: inside cabins replaced the deck 2 conference center, the deck 3 On Air Club and the deck 6 loyalty desk, and an aft suite on deck 6 became balcony cabins. A later refurbishment is dated January 2025 on the same site. The 20 Nov 2026 deck labels do not add a new cabin deck."),
 ],
 "mariner-of-the-seas": [
  ("Did Mariner of the Seas add cabins in the 2018 refit?",
   "CruiseMapper's 2018 drydock review says The Golden Room and Dragon's Lair on deck 3 were converted into staterooms. Those cabins share deck 3 with Studio B and a dining room. Deck 4 did not gain cabins. It is where Izumi and Playmakers went."),
  ("Was Mariner of the Seas refurbished in 2026?",
   "CruiseMapper's ship overview, checked 20 Nov 2026, dates the latest refurbishment to March 2026. The deck labels that day still match the noise map on this page, including the escape room on deck 15 and cabins beside the ice rink on deck 2."),
 ],
 "carnival-celebration": [
  ("How is Carnival Celebration different from Carnival Jubilee?",
   "Both are Excellence class at 183,521 gross tons. Wikipedia, checked 20 Nov 2026, lists Celebration as Meyer Turku, in service November 2022, with 5,374 guests at double occupancy, and Jubilee as Meyer Werft, completed December 2023, with 5,228 at double occupancy. CruiseMapper labels Celebration's midship zones Gateway, and Jubilee's Currents, and only Jubilee's deck 8 label includes The Shores."),
  ("Which deck is above The Gateway on Carnival Celebration?",
   "CruiseMapper's index, checked 20 Nov 2026, puts Gateway on decks 6 and 7, which have no cabins, and puts cabins on deck 8 with the promenade and Havana. Deck 8 is the cabin deck directly above that casino level."),
 ],
 "carnival-jubilee": [
  ("Which Jubilee zones are not on Celebration's deck labels?",
   "Carnival's Jubilee page names Currents and The Shores as the new zones. CruiseMapper's index, checked 20 Nov 2026, puts Currents on decks 6 and 7 and adds The Shores to deck 8 beside Havana. Celebration's matching labels say Gateway, and deck 8 stops at Havana."),
  ("When did Carnival Jubilee enter service?",
   "Wikipedia's infobox, checked 20 Nov 2026, lists completion on 4 December 2023 and a maiden voyage on 23 December 2023. Builder is Meyer Werft in Papenburg. Gross tonnage is 183,521, the same figure listed for Celebration."),
 ],
}

SHIPS = [
 dict(slug="icon-of-the-seas", name="Icon of the Seas", line="royal-caribbean", cm="Icon-Of-The-Seas-2110", official=RCL.format("icon-of-the-seas"), wiki="Icon_of_the_Seas",
      facts=dict(cls="Icon class", builder="Meyer Turku", service="January 2024", gt="248,663", guests="5,610 (double occupancy)"), notes=ICON, sister=["star-of-the-seas"]),
 dict(slug="star-of-the-seas", name="Star of the Seas", line="royal-caribbean", cm="Star-Of-The-Seas-2112", official=RCL.format("star-of-the-seas"), wiki="Star_of_the_Seas",
      facts=dict(cls="Icon class", builder="Meyer Turku", service="August 2025", gt="248,663"), notes=ICON, sister=["icon-of-the-seas"]),
 dict(slug="utopia-of-the-seas", name="Utopia of the Seas", line="royal-caribbean", cm="Utopia-Of-The-Seas-2180", official=RCL.format("utopia-of-the-seas"), wiki="Utopia_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", gt="236,473"),
      notes=OASIS + [("Deck 3 forward", "On Utopia, CruiseMapper notes that forward oceanview cabins on deck 3 sit under the comedy club, a loyalty lounge and the casino on deck 4, so late-night noise is possible.")], sister=["allure-of-the-seas", "harmony-of-the-seas", "wonder-of-the-seas", "symphony-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="wonder-of-the-seas", name="Wonder of the Seas", line="royal-caribbean", cm="Wonder-Of-The-Seas-2165", official=RCL.format("wonder-of-the-seas"), wiki="Wonder_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", service="March 2022", gt="235,600", guests="5,734 (double occupancy)"), notes=OASIS, sister=["allure-of-the-seas", "harmony-of-the-seas", "utopia-of-the-seas", "symphony-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="symphony-of-the-seas", name="Symphony of the Seas", line="royal-caribbean", cm="Symphony-Of-The-Seas-1730", official=RCL.format("symphony-of-the-seas"), wiki="Symphony_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", service="April 2018", gt="228,081", guests="5,518 (double occupancy)"), notes=OASIS, sister=["allure-of-the-seas", "harmony-of-the-seas", "utopia-of-the-seas", "wonder-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="oasis-of-the-seas", name="Oasis of the Seas", line="royal-caribbean", cm="Oasis-Of-The-Seas-690", official=RCL.format("oasis-of-the-seas"), wiki="Oasis_of_the_Seas",
      facts=dict(cls="Oasis class", builder="STX Europe, Turku", service="December 2009", gt="226,838", guests="5,606 (double occupancy)"), notes=OASIS, sister=["allure-of-the-seas", "harmony-of-the-seas", "utopia-of-the-seas", "wonder-of-the-seas", "symphony-of-the-seas"]),
 dict(slug="allure-of-the-seas", name="Allure of the Seas", line="royal-caribbean", cm="Allure-Of-The-Seas-662", official=RCL.format("allure-of-the-seas"), wiki="Allure_of_the_Seas",
      facts=dict(cls="Oasis class", builder="STX Europe, Turku", service="December 2010", gt="226,637", guests="5,484 (double occupancy)"), notes=OASIS, sister=["harmony-of-the-seas", "oasis-of-the-seas", "symphony-of-the-seas", "wonder-of-the-seas", "utopia-of-the-seas"], checked="2026-11-16"),
 dict(slug="harmony-of-the-seas", name="Harmony of the Seas", line="royal-caribbean", cm="Harmony-Of-The-Seas-1067", official=RCL.format("harmony-of-the-seas"), wiki="Harmony_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", service="May 2016", gt="226,963", guests="5,479 (double occupancy)"),
      notes=OASIS + [("Cabins on deck 4", "Harmony's deck listing puts cabins on deck 4 with the entertainment rooms, casino and Studio B. On Oasis of the Seas that deck is public rooms only.")],
      sister=["allure-of-the-seas", "oasis-of-the-seas", "symphony-of-the-seas", "wonder-of-the-seas", "utopia-of-the-seas"], checked="2026-11-16"),
 dict(slug="quantum-of-the-seas", name="Quantum of the Seas", line="royal-caribbean", cm="Quantum-Of-The-Seas-802", official=RCL.format("quantum-of-the-seas"), wiki="Quantum_of_the_Seas",
      facts=dict(cls="Quantum class", builder="Meyer Werft", service="November 2014", gt="168,666", guests="4,180 (double occupancy)"), notes=QUANTUM, sister=["anthem-of-the-seas", "ovation-of-the-seas", "odyssey-of-the-seas", "spectrum-of-the-seas"], checked="2026-11-16"),
 dict(slug="anthem-of-the-seas", name="Anthem of the Seas", line="royal-caribbean", cm="Anthem-of-the-Seas-801", official=RCL.format("anthem-of-the-seas"), wiki="Anthem_of_the_Seas",
      facts=dict(cls="Quantum class", builder="Meyer Werft", service="April 2015", gt="168,666", guests="4,180 (double occupancy)"), notes=QUANTUM, sister=["quantum-of-the-seas", "ovation-of-the-seas", "odyssey-of-the-seas", "spectrum-of-the-seas"], checked="2026-11-16"),
 dict(slug="ovation-of-the-seas", name="Ovation of the Seas", line="royal-caribbean", cm="Ovation-Of-The-Seas-1065", official=RCL.format("ovation-of-the-seas"), wiki="Ovation_of_the_Seas",
      facts=dict(cls="Quantum class", builder="Meyer Werft", service="April 2016", gt="168,666", guests="4,180 (double occupancy)"), notes=QUANTUM, sister=["quantum-of-the-seas", "anthem-of-the-seas", "odyssey-of-the-seas", "spectrum-of-the-seas"], checked="2026-11-16"),
 dict(slug="odyssey-of-the-seas", name="Odyssey of the Seas", line="royal-caribbean", cm="Odyssey-Of-The-Seas-1862", official=RCL.format("odyssey-of-the-seas"), wiki="Odyssey_of_the_Seas",
      facts=dict(cls="Quantum class", builder="Meyer Werft", service="2021", guests="4,284 (double occupancy)"), notes=QUANTUM, sister=["quantum-of-the-seas", "anthem-of-the-seas", "ovation-of-the-seas", "spectrum-of-the-seas"], checked="2026-11-16"),
 dict(slug="spectrum-of-the-seas", name="Spectrum of the Seas", line="royal-caribbean", cm="Spectrum-Of-The-Seas-1861", official=RCL.format("spectrum-of-the-seas"), wiki="Spectrum_of_the_Seas",
      facts=dict(cls="Quantum Ultra class", builder="Meyer Werft", service="April 2019", gt="169,379", guests="4,246 (double occupancy)"),
      notes=QUANTUM + [("Spa on deck 13, suites up top", "Spectrum's listing puts the spa on deck 13 with the cabins, and suites on decks 15 and 16 with the SeaPlex and the top-deck activities.")],
      sister=["quantum-of-the-seas", "anthem-of-the-seas", "ovation-of-the-seas", "odyssey-of-the-seas"], checked="2026-11-16"),
 dict(slug="freedom-of-the-seas", name="Freedom of the Seas", line="royal-caribbean", cm="Freedom-Of-The-Seas-654", official=RCL.format("freedom-of-the-seas"), wiki="MS_Freedom_of_the_Seas",
      facts=dict(cls="Freedom class", builder="Aker Yards, Turku", service="June 2006", gt="156,271", guests="3,782 (double occupancy)"),
      notes=FREEDOM + [
        ("2020 Royal Amplified added cabins on decks 2, 3 and 6", "CruiseMapper's Freedom of the Seas deck plan notes (refit completed March 2020) record that the Deck 2 conference center became 25 inside cabins, the Deck 3 On Air Club became 12 inside cabins, and the Deck 6 loyalty desk became 4 inside cabins. Those new insides sit on decks that already mix cabins with the ice rink (deck 2) or Studio B and dining (deck 3), so treat them like any other cabin beside late venues: check the exact cabin number on the line's deck plan."),
        ("Sports deck thrills sit above deck 12", "The same 2020 drydock added the Cyclone and Typhoon waterslides on deck 13 beside the FlowRider. Deck 12 remains the cabin deck under that sports deck, so morning and afternoon activity overhead is the main cabin trade-off after the Amplified refit."),
      ],
      sister=["liberty-of-the-seas", "independence-of-the-seas"], checked="2026-11-20", published="2026-11-19"),
 dict(slug="liberty-of-the-seas", name="Liberty of the Seas", line="royal-caribbean", cm="Liberty-Of-The-Seas-731", official=RCL.format("liberty-of-the-seas"), wiki="Liberty_of_the_Seas",
      facts=dict(cls="Freedom class", builder="Aker Yards, Turku", service="May 2007", gt="155,889", guests="3,798 (double occupancy)"),
      notes=FREEDOM + [("Cabins beside the casino", "Liberty's deck 4 lists cabins with the casino and lounge. Freedom of the Seas and Independence of the Seas keep deck 4 as public rooms.")],
      sister=["freedom-of-the-seas", "independence-of-the-seas"], checked="2026-11-16"),
 dict(slug="independence-of-the-seas", name="Independence of the Seas", line="royal-caribbean", cm="Independence-Of-The-Seas-531", official=RCL.format("independence-of-the-seas"), wiki="Independence_of_the_Seas",
      facts=dict(cls="Freedom class", builder="Aker Finnyards, Turku", service="May 2008", gt="155,889"), notes=FREEDOM, sister=["freedom-of-the-seas", "liberty-of-the-seas"], checked="2026-11-16"),
 dict(slug="navigator-of-the-seas", name="Navigator of the Seas", line="royal-caribbean", cm="Navigator-Of-The-Seas-704", official=RCL.format("navigator-of-the-seas"), wiki="Navigator_of_the_Seas",
      facts=dict(cls="Voyager class", builder="Kvaerner Masa-Yards, Turku", service="December 2002", gt="139,999"), notes=VOYAGER, sister=["voyager-of-the-seas", "mariner-of-the-seas", "adventure-of-the-seas"], checked="2026-11-16"),
 dict(slug="voyager-of-the-seas", name="Voyager of the Seas", line="royal-caribbean", cm="Voyager-Of-The-Seas-541", official=RCL.format("voyager-of-the-seas"), wiki="Voyager_of_the_Seas",
      facts=dict(cls="Voyager class", builder="Kvaerner Masa-Yards, Turku", service="November 1999", gt="137,276", guests="3,602 (double occupancy)"), notes=VOYAGER, sister=["navigator-of-the-seas", "mariner-of-the-seas", "adventure-of-the-seas"], checked="2026-11-16"),
 dict(slug="mariner-of-the-seas", name="Mariner of the Seas", line="royal-caribbean", cm="Mariner-Of-The-Seas-609", official=RCL.format("mariner-of-the-seas"), wiki="Mariner_of_the_Seas",
      facts=dict(cls="Voyager class", builder="Kvaerner Masa-Yards, Turku", service="November 2003", gt="139,863"),
      notes=VOYAGER + [
        ("Deck 15's chapel became an escape room", "Mariner's 2018 Royal Amplified refit replaced the Skylight Chapel on deck 15 with The Observatorium, a timed escape-room attraction (Puzzle Break), according to CruiseMapper's deck plan notes. Deck 15 has no cabins either way."),
        ("Dining shares the low decks", "CruiseMapper's Mariner deck listing puts dining rooms on decks 3, 4 and 5 with Studio B, the casino/lounge and the promenade. Adventure of the Seas keeps dining off those mid-public decks in its listing, so Mariner's cabin neighbours on decks 2 and 3 sit closer to mealtime traffic."),
        ("Entered service later than Adventure", "Mariner entered service in November 2003 (Wikipedia infobox, checked 19 Nov 2026), two years after Adventure of the Seas. Gross tonnage is listed as 139,863, a touch larger than Adventure's 138,193."),
      ],
      sister=["navigator-of-the-seas", "voyager-of-the-seas", "adventure-of-the-seas"], checked="2026-11-20", published="2026-11-19"),
 dict(slug="adventure-of-the-seas", name="Adventure of the Seas", line="royal-caribbean", cm="Adventure-Of-The-Seas-533", official=RCL.format("adventure-of-the-seas"), wiki="Adventure_of_the_Seas",
      facts=dict(cls="Voyager class", builder="Kvaerner Masa-Yards, Turku", service="November 2001", gt="138,193", guests="3,807 (max)"),
      notes=VOYAGER + [
        ("First in its class with waterslides", "Adventure of the Seas was the first Voyager-class ship fitted with the Cyclone and Typhoon waterslides and a FlowRider surf simulator, added on the sports deck (13) during its 2016 drydock, according to CruiseMapper's refurbishment notes."),
        ("Deck 15 still lists a Skylight", "CruiseMapper's Adventure deck listing still labels deck 15 as Skylight, not an escape room. Mariner of the Seas converted that space to The Observatorium in its 2018 Amplified refit, so the top public deck differs between the two sisters even though neither deck has cabins."),
        ("Casino deck without dining rooms", "Adventure's deck 4 listing is Casino-Lounge only. Mariner's matching deck also lists Dining2, so Adventure's public midship block is thinner on dining rooms than Mariner's, based on the deck-by-deck labels checked 19 Nov 2026."),
      ],
      sister=["navigator-of-the-seas", "voyager-of-the-seas", "mariner-of-the-seas"], checked="2026-11-19"),
 dict(slug="carnival-celebration", name="Carnival Celebration", line="carnival", cm="Carnival-Celebration-2106", official=CCL.format("carnival-celebration"), wiki="Carnival_Celebration",
      facts=dict(cls="Excellence class", builder="Meyer Turku", service="November 2022", gt="183,521", guests="5,374 (double occupancy)"),
      notes=[
        ("Deck 8 cabins sit on top of The Gateway", "Carnival's own Celebration page describes The Gateway as a zone and does not give it a deck number. CruiseMapper's index, checked 20 Nov 2026, puts Gateway on decks 6 and 7, which have no cabins, and puts cabins on deck 8 with the promenade and Havana. Live Latin music at the Havana Bar is the evening noise CruiseMapper flags on that deck. Deck 9 sits directly over that mix, so it is not a fully enclosed cabin deck."),
        ("Family Harbor is a deck 4 choice, not a quiet one", "Carnival's page puts Family Harbor staterooms next to the Family Harbor Lounge, with breakfast, snacks, games and a block of Night Owls babysitting. CruiseMapper still lists that lounge on deck 4 beside cabins and the kids' area. Take it for the lounge. Do not take it for silence."),
        ("Loft 19 access is a suite perk, and the coaster is above deck 17", "Carnival's page says a Carnival Excel suite includes Loft 19, the top-deck retreat with an infinity whirlpool. CruiseMapper labels deck 19 as Loft 19 and the BOLT coaster, with no cabins. Deck 17 cabins are the ones under the teen and sundeck level, closest to that machinery."),
      ],
      sister=["mardi-gras", "carnival-jubilee"], checked="2026-11-20", published="2026-11-15"),
 dict(slug="mardi-gras", name="Mardi Gras", line="carnival", cm="Carnival-Mardi-Gras-2105", official=CCL.format("mardi-gras"), wiki="Mardi_Gras_(2020_ship)",
      facts=dict(cls="Excellence class", builder="Meyer Turku", service="July 2021", gt="181,808", guests="5,282 (double occupancy)"), notes=EXCELLENCE, sister=["carnival-celebration", "carnival-jubilee"]),
 dict(slug="carnival-jubilee", name="Carnival Jubilee", line="carnival", cm="Carnival-Jubilee-2077", official=CCL.format("carnival-jubilee"), wiki="Carnival_Jubilee",
      facts=dict(cls="Excellence class", builder="Meyer Werft", service="December 2023", gt="183,521", guests="5,228 (double occupancy)"),
      notes=[
        ("Deck 8 is shared with Havana and The Shores", "Jubilee's deck index on CruiseMapper, checked 20 Nov 2026, is the one that adds The Shores to deck 8. Cabins, the promenade and Havana are on that same deck, directly over Currents on deck 7 (casino and shops, no cabins). Celebration's matching label stops at Havana and calls the public decks Gateway. If the neighbourhood name on your booking does not say The Shores, you are not looking at Jubilee's deck 8."),
        ("The Family Harbor lounge is still on deck 4", "Carnival's Jubilee page seats Family Harbor staterooms by that lounge. The deck index puts the lounge on deck 4 with cabins and the kids' area. It is the family location on this ship, and it is the lowest cabin deck on the listing, so the forward-cabin caution on this page still applies."),
        ("BOLT and Serenity are above the top cabin deck", "Deck 18 on the Jubilee index is Serenity, sports and WaterWorks. Deck 19 is Loft 19 and the BOLT coaster. Neither has cabins. Deck 17, which does, also lists teens and the sundeck, so it takes traffic from both. Decks 10, 11, 12 and 14 are the cabin decks with cabin decks above and below. Deck 15 is the one directly under the lido."),
      ],
      sister=["carnival-celebration", "mardi-gras"], checked="2026-11-20", published="2026-11-15"),
 dict(slug="carnival-vista", name="Carnival Vista", line="carnival", cm="Carnival-Vista-1039", official=CCL.format("carnival-vista"), wiki="Carnival_Vista",
      facts=dict(cls="Vista class", builder="Fincantieri", service="May 2016", gt="133,596", guests="3,934 (double occupancy)"),
      notes=VISTA + [("IMAX on deck 7", "Deck 7 mixes cabins with the IMAX theater.")],
      sister=["carnival-horizon", "carnival-panorama", "carnival-venezia", "carnival-firenze"], checked="2026-11-16"),
 dict(slug="carnival-horizon", name="Carnival Horizon", line="carnival", cm="Carnival-Horizon-1355", official=CCL.format("carnival-horizon"), wiki="Carnival_Horizon",
      facts=dict(cls="Vista class", builder="Fincantieri", service="April 2018", gt="133,596", guests="3,960 (double occupancy)"),
      notes=VISTA + [("IMAX on deck 7", "Deck 7 mixes cabins with the IMAX theater.")],
      sister=["carnival-vista", "carnival-panorama", "carnival-venezia", "carnival-firenze"], checked="2026-11-16"),
 dict(slug="carnival-panorama", name="Carnival Panorama", line="carnival", cm="Carnival-Panorama-2099", official=CCL.format("carnival-panorama"), wiki="Carnival_Panorama",
      facts=dict(cls="Vista class", builder="Fincantieri", service="December 2019", gt="133,868", guests="4,008 (double occupancy)"),
      notes=VISTA + [("SkyZone on deck 7", "Deck 7 mixes cabins with SkyZone. Vista and Horizon list an IMAX theater on that deck instead.")],
      sister=["carnival-vista", "carnival-horizon", "carnival-venezia", "carnival-firenze"], checked="2026-11-16"),
 dict(slug="carnival-venezia", name="Carnival Venezia", line="carnival", cm="Carnival-Venezia-1651", official=CCL.format("carnival-venezia"), wiki="Carnival_Venezia",
      facts=dict(cls="Vista class", builder="Fincantieri", service="May 2023", gt="135,225", guests="4,208 (double occupancy)"),
      notes=VISTA_EX + [("Teens on deck 3", "Deck 3 mixes cabins with dining and the teen area.")],
      sister=["carnival-firenze", "carnival-vista", "carnival-horizon", "carnival-panorama"], checked="2026-11-16"),
 dict(slug="carnival-firenze", name="Carnival Firenze", line="carnival", cm="Carnival-Firenze-2120", official=CCL.format("carnival-firenze"), wiki="Carnival_Firenze",
      facts=dict(cls="Vista class", builder="Fincantieri", service="April 2024", gt="135,156", guests="4,208 (double occupancy)"),
      notes=VISTA_EX + [("Kids on deck 3", "Deck 3 mixes cabins with dining and the kids' area.")],
      sister=["carnival-venezia", "carnival-vista", "carnival-horizon", "carnival-panorama"], checked="2026-11-16"),
 dict(slug="carnival-magic", name="Carnival Magic", line="carnival", cm="Carnival-Magic-681", official=CCL.format("carnival-magic"), wiki="Carnival_Magic",
      facts=dict(cls="Dream class", builder="Fincantieri", service="May 2011", gt="130,000", guests="3,690 (double occupancy)"), notes=DREAM_C, sister=["carnival-dream", "carnival-breeze"], checked="2026-11-16"),
 dict(slug="carnival-dream", name="Carnival Dream", line="carnival", cm="Carnival-Dream-680", official=CCL.format("carnival-dream"), wiki="Carnival_Dream",
      facts=dict(cls="Dream class", builder="Fincantieri", service="September 2009", gt="128,250", guests="3,646"), notes=DREAM_C, sister=["carnival-magic", "carnival-breeze"], checked="2026-11-16"),
 dict(slug="carnival-breeze", name="Carnival Breeze", line="carnival", cm="Carnival-Breeze-703", official=CCL.format("carnival-breeze"), wiki="Carnival_Breeze",
      facts=dict(cls="Dream class", builder="Fincantieri", service="June 2012", gt="130,000", guests="3,690"), notes=DREAM_C, sister=["carnival-magic", "carnival-dream"], checked="2026-11-16"),
 dict(slug="carnival-liberty", name="Carnival Liberty", line="carnival", cm="Carnival-Liberty-568", official=CCL.format("carnival-liberty"), wiki="Carnival_Liberty",
      facts=dict(cls="Conquest class", builder="Fincantieri", service="July 2005", gt="110,000", guests="2,974"), notes=CONQUEST, sister=[], checked="2026-11-16"),
 dict(slug="carnival-sunshine", name="Carnival Sunshine", line="carnival", cm="Carnival-Sunshine-546", official=CCL.format("carnival-sunshine"), wiki="Carnival_Sunshine",
      facts=dict(cls="Sunshine class", builder="Fincantieri", gt="102,853", guests="3,002"), notes=SUNSHINE, sister=[], checked="2026-11-16"),
 dict(slug="norwegian-prima", name="Norwegian Prima", line="norwegian", cm="Norwegian-Prima-2216", official=NCL.format("prima"), wiki="Norwegian_Prima",
      facts=dict(cls="Prima class", builder="Fincantieri", service="2022", gt="143,535"), notes=PRIMA, sister=["norwegian-viva", "norwegian-aqua"]),
 dict(slug="norwegian-viva", name="Norwegian Viva", line="norwegian", cm="Norwegian-Viva-2217", official=NCL.format("viva"), wiki="Norwegian_Viva",
      facts=dict(cls="Prima class", service="August 2023", gt="143,535"), notes=PRIMA, sister=["norwegian-prima", "norwegian-aqua"]),
 dict(slug="norwegian-encore", name="Norwegian Encore", line="norwegian", cm="Norwegian-Encore-1518", official=NCL.format("encore"), wiki="Norwegian_Encore",
      facts=dict(cls="Breakaway Plus class", builder="Meyer Werft", service="November 2019", gt="169,116", guests="3,998 (lower beds)"), notes=BREAKAWAY, sister=["norwegian-bliss", "norwegian-escape", "norwegian-joy", "norwegian-getaway"]),
 dict(slug="norwegian-getaway", name="Norwegian Getaway", line="norwegian", cm="Norwegian-Getaway-793", official=NCL.format("getaway"), wiki="Norwegian_Getaway",
      facts=dict(cls="Breakaway class", builder="Meyer Werft", service="February 2014", gt="145,655", guests="3,963"),
      notes=BREAKAWAY + [("Kids' areas on decks 12 and 13", "On Norwegian Getaway, CruiseMapper's deck plan places kids' areas on cabin decks 12 and 13. Handy for families; others may prefer decks 9 to 11.")], sister=["norwegian-encore", "norwegian-breakaway"]),
 dict(slug="norwegian-escape", name="Norwegian Escape", line="norwegian", cm="Norwegian-Escape-878", official=NCL.format("escape"), wiki="Norwegian_Escape",
      facts=dict(cls="Breakaway Plus class", builder="Meyer Werft", service="2015", gt="164,998", guests="4,266"),
      notes=BPLUS + [("Studios on decks 10 to 12", "Studio cabins are listed on decks 10, 11 and 12. Deck 5 also mixes cabins with the kids' area.")],
      sister=["norwegian-bliss", "norwegian-joy", "norwegian-encore"], checked="2026-11-16"),
 dict(slug="norwegian-bliss", name="Norwegian Bliss", line="norwegian", cm="Norwegian-Bliss-1454", official=NCL.format("bliss"), wiki="Norwegian_Bliss",
      facts=dict(cls="Breakaway Plus class", builder="Meyer Werft", service="June 2018", gt="168,028", guests="4,002 (double occupancy)"),
      notes=BPLUS + [("Studios on decks 11 and 12", "Studio cabins are listed on decks 11 and 12. Deck 16 is the spa, lido and pools with no cabins, so deck 15 sits directly under the pool deck. A racetrack is listed on deck 19.")],
      sister=["norwegian-escape", "norwegian-joy", "norwegian-encore"], checked="2026-11-16"),
 dict(slug="norwegian-joy", name="Norwegian Joy", line="norwegian", cm="Norwegian-Joy-1166", official=NCL.format("joy"), wiki="Norwegian_Joy",
      facts=dict(cls="Breakaway Plus class", builder="Meyer Werft", service="2017", gt="167,725"),
      notes=BPLUS + [("No Studios on the deck listing", "Joy's deck listing does not show the Studio cabins that Escape and Bliss place on decks 10 to 12. Confirm on NCL's current plan if you want one. A racetrack is listed on decks 18 and 19.")],
      sister=["norwegian-escape", "norwegian-bliss", "norwegian-encore"], checked="2026-11-16"),
 dict(slug="norwegian-breakaway", name="Norwegian Breakaway", line="norwegian", cm="Norwegian-Breakaway-584", official=NCL.format("breakaway"), wiki="Norwegian_Breakaway",
      facts=dict(cls="Breakaway class", builder="Meyer Werft", service="April 2013", gt="145,655", guests="3,963"),
      notes=BPLUS + [("Studios on decks 10 and 11", "Studio cabins are listed on decks 10 and 11. Decks 12 and 13 mix cabins with the kids' areas, and deck 15 mixes cabins with the spa, lido, pools and the Haven.")],
      sister=["norwegian-getaway"], checked="2026-11-16"),
 dict(slug="norwegian-epic", name="Norwegian Epic", line="norwegian", cm="Norwegian-Epic-642", official=NCL.format("epic"), wiki="Norwegian_Epic",
      facts=dict(cls="Epic class", builder="STX France", service="July 2010", gt="155,873", guests="4,100 (double occupancy)"), notes=EPIC_N, sister=[], checked="2026-11-16"),
 dict(slug="norwegian-aqua", name="Norwegian Aqua", line="norwegian", cm="Norwegian-Aqua-2218", official=NCL.format("aqua"), wiki="Norwegian_Aqua",
      facts=dict(cls="Prima class", builder="Fincantieri", service="2025", gt="156,300", guests="3,571"), notes=AQUA_N, sister=["norwegian-prima", "norwegian-viva"], checked="2026-11-16"),
 dict(slug="norwegian-jewel", name="Norwegian Jewel", line="norwegian", cm="Norwegian-Jewel-583", official=NCL.format("jewel"), wiki="Norwegian_Jewel",
      facts=dict(cls="Jewel class", builder="Meyer Werft", service="August 2005", gt="93,502", guests="2,376"), notes=JEWEL_N, sister=[], checked="2026-11-16"),
 dict(slug="msc-world-america", name="MSC World America", line="msc", cm="MSC-World-America-2184", official="https://www.msccruisesusa.com/cruise/ships/msc-world-america", wiki="World-class_cruise_ship",
      facts=dict(cls="World class", gt="216,638", guests="6,764", src=("MSC Cruises: MSC World America in numbers", "https://www.msccruises.co.uk/ships/msc-world-america")),
      notes=[("Deck 9 sits over the promenade", "Deck 9 is the first cabin deck above deck 8, which has the promenade and the spa. Decks 10 to 15 are the quiet core."),
             ("Promenade-view balconies", "MSC sells balcony categories with a promenade view at the stern. They look over the ship's aft promenade rather than open sea, and the promenade is a social space."),
             ("Yacht Club is forward and high", "MSC Cruises says the Yacht Club spans the seven upper foredecks, with 152 suites. Suite-only areas mean fewer passers-by near those cabins."),
             ("Deck 16 sits under the main pool deck", "There is no deck 17, so deck 16 cabins are directly below deck 18 with its lido and pools.")], sister=["msc-world-europa"]),
 dict(slug="msc-seascape", name="MSC Seascape", line="msc", cm="MSC-Seascape-2144", official="https://www.msccruises.com/int/our-cruises/ships/msc-seascape", wiki="MSC_Seascape",
      facts=dict(cls="Seaside EVO class", gt="170,412", guests="4,540 (double occupancy)"), notes=SEASIDE, sister=["msc-seashore", "msc-seaside"]),
 dict(slug="msc-seashore", name="MSC Seashore", line="msc", cm="MSC-Seashore-2143", official="https://www.msccruises.com/int/our-cruises/ships/msc-seashore", wiki="MSC_Seashore",
      facts=dict(cls="Seaside EVO class", gt="170,412", guests="4,540 (double occupancy)"), notes=SEASIDE, sister=["msc-seascape", "msc-seaside"]),
 dict(slug="msc-world-europa", name="MSC World Europa", line="msc", cm="MSC-World-Europa-2183", official="https://www.msccruisesusa.com/cruise/ships/msc-world-europa", wiki="MSC_World_Europa",
      facts=dict(cls="World class", builder="Chantiers de l'Atlantique", service="December 2022", gt="215,863", guests="6,762", src=("MSC Cruises: MSC World Europa", "https://www.msccruisesusa.com/cruise/ships/msc-world-europa")),
      notes=WORLD, sister=["msc-world-america"], checked="2026-11-16"),
 dict(slug="msc-meraviglia", name="MSC Meraviglia", line="msc", cm="MSC-Meraviglia-1187", official="https://www.msccruises.com/int/our-cruises/ships/msc-meraviglia", wiki="MSC_Meraviglia",
      facts=dict(cls="Meraviglia class", builder="STX France", service="June 2017", gt="171,598", guests="4,488 (double occupancy)"),
      notes=MERAVIGLIA + [("Yacht Club cabins on the lido deck", "Deck 15 lists the lido pools and Yacht Club cabins together.")],
      sister=["msc-grandiosa", "msc-virtuosa"], checked="2026-11-16"),
 dict(slug="msc-grandiosa", name="MSC Grandiosa", line="msc", cm="MSC-Grandiosa-1008", official="https://www.msccruises.com/int/our-cruises/ships/msc-grandiosa", wiki="MSC_Grandiosa",
      facts=dict(cls="Meraviglia Plus class", builder="Chantiers de l'Atlantique", service="2019", gt="181,541", guests="4,842 (double occupancy)"),
      notes=MERAVIGLIA + [("Deck 14 is under the pools", "Deck 15 is the lido and pools with no cabins in the listing, so deck 14 sits directly under the pool deck. Yacht Club areas are listed on decks 16 and 19.")],
      sister=["msc-meraviglia", "msc-virtuosa"], checked="2026-11-16"),
 dict(slug="msc-virtuosa", name="MSC Virtuosa", line="msc", cm="MSC-Virtuosa-1981", official="https://www.msccruises.com/int/our-cruises/ships/msc-virtuosa", wiki="MSC_Virtuosa",
      facts=dict(cls="Meraviglia Plus class", builder="Chantiers de l'Atlantique", service="2021", gt="181,541", guests="4,842 (double occupancy)"),
      notes=MERAVIGLIA + [("Suites on the lido deck", "Deck 15 lists suites with the lido pools. More suites are listed on decks 16 and 18 with the Yacht Club, sports, kids and teens.")],
      sister=["msc-meraviglia", "msc-grandiosa"], checked="2026-11-16"),
 dict(slug="msc-seaside", name="MSC Seaside", line="msc", cm="MSC-Seaside-1205", official="https://www.msccruises.com/int/our-cruises/ships/msc-seaside", wiki="MSC_Seaside",
      facts=dict(cls="Seaside class", builder="Fincantieri", service="November 2017", gt="153,516", guests="4,132 (double occupancy)"), notes=SEASIDE_O, sister=["msc-seashore", "msc-seascape"], checked="2026-11-16"),
 dict(slug="msc-divina", name="MSC Divina", line="msc", cm="MSC-Divina-549", official="https://www.msccruises.com/int/our-cruises/ships/msc-divina", wiki="MSC_Divina",
      facts=dict(cls="Fantasia class", builder="Chantiers de l'Atlantique", service="May 2012", gt="139,072", guests="3,502"), notes=DIVINA_N, sister=[], checked="2026-11-16"),
 dict(slug="celebrity-beyond", name="Celebrity Beyond", line="celebrity", cm="Celebrity-Beyond-1690", official=CEL.format("celebrity-beyond"), wiki="Celebrity_Beyond",
      facts=dict(cls="Edge class", builder="Chantiers de l'Atlantique", service="April 2022", gt="141,420", guests="3,260 (double occupancy)"), notes=EDGE, sister=["celebrity-apex", "celebrity-ascent", "celebrity-edge"]),
 dict(slug="celebrity-ascent", name="Celebrity Ascent", line="celebrity", cm="Celebrity-Ascent-2194", official=CEL.format("celebrity-ascent"), wiki="Celebrity_Ascent",
      facts=dict(cls="Edge class", builder="Chantiers de l'Atlantique", gt="141,420", guests="3,260 (double occupancy)"), notes=EDGE, sister=["celebrity-apex", "celebrity-beyond", "celebrity-edge"]),
 dict(slug="celebrity-edge", name="Celebrity Edge", line="celebrity", cm="Celebrity-Edge-1588", official=CEL.format("celebrity-edge"), wiki="Celebrity_Edge",
      facts=dict(cls="Edge class", builder="STX France", service="December 2018", gt="130,818", guests="2,918"), notes=EDGE, sister=["celebrity-apex", "celebrity-beyond", "celebrity-ascent"]),
 dict(slug="celebrity-apex", name="Celebrity Apex", line="celebrity", cm="Celebrity-Apex-1587", official=CEL.format("celebrity-apex"), wiki="Celebrity_Apex",
      facts=dict(cls="Edge class", builder="Chantiers de l'Atlantique", service="March 2020", gt="130,818", guests="2,910"), notes=EDGE, sister=["celebrity-edge", "celebrity-beyond", "celebrity-ascent"], checked="2026-11-16"),
 dict(slug="celebrity-reflection", name="Celebrity Reflection", line="celebrity", cm="Celebrity-Reflection-685", official=CEL.format("celebrity-reflection"), wiki="Celebrity_Reflection",
      facts=dict(cls="Solstice class", builder="Meyer Werft", service="October 2012", gt="125,366", guests="3,046"),
      notes=SOLSTICE + [("Spa on deck 12, suites on the lido", "Deck 12 mixes cabins with the spa. Deck 14 lists suites with the lido, sundeck and pools.")],
      sister=["celebrity-equinox", "celebrity-solstice"], checked="2026-11-16"),
 dict(slug="celebrity-equinox", name="Celebrity Equinox", line="celebrity", cm="Celebrity-Equinox-739", official=CEL.format("celebrity-equinox"), wiki="Celebrity_Equinox",
      facts=dict(cls="Solstice class", builder="Meyer Werft", service="July 2009", gt="121,878", guests="2,850"),
      notes=SOLSTICE + [("Pools on the top cabin deck", "Deck 12 mixes cabins with the spa and pools, under the lido sundeck on deck 14.")],
      sister=["celebrity-reflection", "celebrity-solstice"], checked="2026-11-16"),
 dict(slug="celebrity-solstice", name="Celebrity Solstice", line="celebrity", cm="Celebrity-Solstice-676", official=CEL.format("celebrity-solstice"), wiki="Celebrity_Solstice",
      facts=dict(cls="Solstice class", builder="Meyer Werft", service="November 2008", gt="121,878", guests="2,852"),
      notes=SOLSTICE + [("Pools and the solarium on deck 12", "Deck 12 mixes cabins with the spa, solarium, pools and a sundeck, under the lido on deck 14.")],
      sister=["celebrity-reflection", "celebrity-equinox"], checked="2026-11-16"),
 dict(slug="sun-princess", name="Sun Princess", line="princess", cm="Sun-Princess-2167", official=PCL.format("su-sun-princess"), wiki="Sun_Princess_(2024)",
      facts=dict(cls="Sphere class", builder="Fincantieri", service="February 2024", gt="177,882", guests="4,300"),
      notes=SPHERE + [("Solo interiors", "Sun Princess lists a single-occupancy inside category (IS) on deck 10, according to CruiseMapper.")], sister=["star-princess"]),
 dict(slug="star-princess", name="Star Princess", line="princess", cm="Star-Princess-2168", official=PCL.format("st-star-princess"), wiki="Star_Princess_(2024)",
      facts=dict(cls="Sphere class", service="October 2025", gt="177,882", guests="4,300"), notes=SPHERE, sister=["sun-princess"]),
 dict(slug="discovery-princess", name="Discovery Princess", line="princess", cm="Discovery-Princess-2157", official=PCL.format("xp-discovery-princess"), wiki="Discovery_Princess",
      facts=dict(cls="Royal class", builder="Fincantieri", service="March 2022", gt="145,000", guests="3,660"), notes=ROYAL_P, sister=["enchanted-princess", "sky-princess", "royal-princess", "majestic-princess"]),
 dict(slug="enchanted-princess", name="Enchanted Princess", line="princess", cm="Enchanted-Princess-2156", official=PCL.format("ex-enchanted-princess"), wiki="Enchanted_Princess",
      facts=dict(cls="Royal class", builder="Fincantieri", service="November 2021", gt="145,281", guests="3,660"), notes=ROYAL_CORE, sister=["sky-princess", "discovery-princess", "royal-princess", "majestic-princess"], checked="2026-11-16"),
 dict(slug="sky-princess", name="Sky Princess", line="princess", cm="Sky-Princess-2154", official=PCL.format("yp-sky-princess"), wiki="Sky_Princess_(2019)",
      facts=dict(cls="Royal class", builder="Fincantieri", service="October 2019", gt="145,281", guests="3,660"), notes=ROYAL_CORE, sister=["enchanted-princess", "discovery-princess", "royal-princess", "majestic-princess"], checked="2026-11-16"),
 dict(slug="royal-princess", name="Royal Princess", line="princess", cm="Royal-Princess-650", official=PCL.format("rp-royal-princess"), wiki="Royal_Princess_(2012)",
      facts=dict(cls="Royal class", builder="Fincantieri", service="June 2013", gt="142,714", guests="3,600"), notes=ROYAL_RM, sister=["majestic-princess", "discovery-princess", "enchanted-princess", "sky-princess"], checked="2026-11-16"),
 dict(slug="majestic-princess", name="Majestic Princess", line="princess", cm="Majestic-Princess-1194", official=PCL.format("mj-majestic-princess"), wiki="Majestic_Princess",
      facts=dict(cls="Royal class", builder="Fincantieri", service="April 2017", gt="144,216", guests="3,560"), notes=ROYAL_RM, sister=["royal-princess", "discovery-princess", "enchanted-princess", "sky-princess"], checked="2026-11-16"),
 dict(slug="ruby-princess", name="Ruby Princess", line="princess", cm="Ruby-Princess-593", official=PCL.format("ru-ruby-princess"), wiki="Ruby_Princess",
      facts=dict(cls="Crown class", service="November 2008", gt="113,561", guests="3,080"), notes=RUBY_N, sister=[], checked="2026-11-16"),
 dict(slug="disney-wish", name="Disney Wish", line="disney", cm="Disney-Wish-2127", official=DCL.format("wish"), wiki="Disney_Wish",
      facts=dict(cls="Wish class", builder="Meyer Werft", service="July 2022", gt="144,000", guests="2,508 (double occupancy)"), notes=WISH, sister=["disney-treasure", "disney-destiny"]),
 dict(slug="disney-treasure", name="Disney Treasure", line="disney", cm="Disney-Treasure-2128", official=DCL.format("treasure"), wiki="Disney_Treasure",
      facts=dict(cls="Wish class", builder="Meyer Werft", gt="144,256", guests="2,492 (double occupancy)"), notes=WISH, sister=["disney-wish", "disney-destiny"]),
 dict(slug="disney-destiny", name="Disney Destiny", line="disney", cm="Disney-Destiny-2129", official=DCL.format("destiny"), wiki="Disney_Destiny",
      facts=dict(cls="Wish class", builder="Meyer Werft", service="November 2025", gt="144,000", guests="2,508 (double occupancy)"), notes=WISH, sister=["disney-wish", "disney-treasure"]),
 dict(slug="disney-dream", name="Disney Dream", line="disney", cm="Disney-Dream-548", official=DCL.format("dream"), wiki="Disney_Dream",
      facts=dict(cls="Dream class", builder="Meyer Werft", service="January 2011", gt="129,690", guests="2,500 (double occupancy)"), notes=DREAM_D, sister=["disney-fantasy"], checked="2026-11-16"),
 dict(slug="disney-fantasy", name="Disney Fantasy", line="disney", cm="Disney-Fantasy-649", official=DCL.format("fantasy"), wiki="Disney_Fantasy",
      facts=dict(cls="Dream class", builder="Meyer Werft", service="March 2012", guests="2,500 (double occupancy)"), notes=DREAM_D, sister=["disney-dream"], checked="2026-11-16"),
 dict(slug="disney-magic", name="Disney Magic", line="disney", cm="Disney-Magic-684", official=DCL.format("magic"), wiki="Disney_Magic",
      facts=dict(cls="Magic class", builder="Fincantieri", service="July 1998", gt="83,338", guests="1,750 (double occupancy)"), notes=MAGIC_D, sister=["disney-wonder"], checked="2026-11-16"),
 dict(slug="disney-wonder", name="Disney Wonder", line="disney", cm="Disney-Wonder-692", official=DCL.format("wonder"), wiki="Disney_Wonder",
      facts=dict(cls="Magic class", builder="Fincantieri", service="August 1999", gt="84,130"), notes=MAGIC_D, sister=["disney-magic"], checked="2026-11-16"),
 dict(slug="scarlet-lady", name="Scarlet Lady", line="virgin", cm="Scarlet-Lady-1976", official=VV.format("scarlet-lady"), wiki="Scarlet_Lady_(ship)",
      facts=dict(builder="Fincantieri", service="February 2020", gt="110,000", guests="2,770"), notes=LADY, sister=["valiant-lady", "resilient-lady", "brilliant-lady"], checked="2026-11-16"),
 dict(slug="valiant-lady", name="Valiant Lady", line="virgin", cm="Valiant-Lady-1977", official=VV.format("valiant-lady"), wiki="Valiant_Lady_(ship)",
      facts=dict(builder="Fincantieri", service="March 2022", gt="110,000", guests="2,770"), notes=LADY, sister=["scarlet-lady", "resilient-lady", "brilliant-lady"], checked="2026-11-16"),
 dict(slug="resilient-lady", name="Resilient Lady", line="virgin", cm="Resilient-Lady-1978", official=VV.format("resilient-lady"), wiki="Resilient_Lady",
      facts=dict(builder="Fincantieri", service="May 2023", gt="110,000", guests="2,770"), notes=LADY, sister=["scarlet-lady", "valiant-lady", "brilliant-lady"], checked="2026-11-16"),
 dict(slug="brilliant-lady", name="Brilliant Lady", line="virgin", cm="Brilliant-Lady-1979", official=VV.format("brilliant-lady"), wiki="Brilliant_Lady",
      facts=dict(builder="Fincantieri", service="September 2025", gt="110,000", guests="2,770"), notes=LADY, sister=["scarlet-lady", "valiant-lady", "resilient-lady"], checked="2026-11-16"),
 dict(slug="rotterdam", name="Rotterdam", line="holland-america", cm="ms-Rotterdam-2166", official=HAL.format("rotterdam/0"), wiki="MS_Rotterdam_(2020)",
      facts=dict(cls="Pinnacle class", builder="Fincantieri", service="October 2021", gt="99,935", guests="2,668"), notes=PINNACLE, sister=["nieuw-statendam", "koningsdam"], checked="2026-11-16"),
 dict(slug="nieuw-statendam", name="Nieuw Statendam", line="holland-america", cm="ms-Nieuw-Statendam-1337", official=HAL.format("nieuw-statendam/1"), wiki="MS_Nieuw_Statendam",
      facts=dict(cls="Pinnacle class", builder="Fincantieri", service="November 2018", gt="99,902", guests="2,666"), notes=PINNACLE, sister=["rotterdam", "koningsdam"], checked="2026-11-16"),
 dict(slug="koningsdam", name="Koningsdam", line="holland-america", cm="ms-Koningsdam-1036", official=HAL.format("koningsdam/3"), wiki="MS_Koningsdam",
      facts=dict(cls="Pinnacle class", builder="Fincantieri", service="March 2016", gt="99,863", guests="2,650 (double occupancy)"), notes=PINNACLE, sister=["rotterdam", "nieuw-statendam"], checked="2026-11-16"),
 dict(slug="eurodam", name="Eurodam", line="holland-america", cm="ms-Eurodam-709", official=HAL.format("eurodam/0"), wiki="MS_Eurodam",
      facts=dict(cls="Signature class", builder="Fincantieri", service="July 2008", gt="86,273", guests="2,104"),
      notes=SIGNATURE + [("A later deck plan is posted", "Holland America's Eurodam page links a separate deck plan for sailings after March 24, 2027. This page follows the current deck listing, so check the plan for the date you book.")],
      sister=["nieuw-amsterdam"], checked="2026-11-16"),
 dict(slug="nieuw-amsterdam", name="Nieuw Amsterdam", line="holland-america", cm="ms-Nieuw-Amsterdam-559", official=HAL.format("nieuw-amsterdam/4"), wiki="MS_Nieuw_Amsterdam_(2009)",
      facts=dict(cls="Signature class", builder="Fincantieri", service="July 2010", gt="86,700", guests="2,106"), notes=SIGNATURE, sister=["eurodam"], checked="2026-11-16"),
]
