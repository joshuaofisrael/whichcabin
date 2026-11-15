# Ship data for Which Cabin. Facts only from the sources named in each entry; notes are our own words.
# facts: from the ship's Wikipedia infobox (retrieved 15 Nov 2026) unless "src" says otherwise. Omit anything unverified.
LINES = {
 "royal-caribbean": dict(name="Royal Caribbean", short="Royal Caribbean", url="https://www.royalcaribbean.com/cruise-ships"),
 "carnival": dict(name="Carnival Cruise Line", short="Carnival", url="https://www.carnival.com/cruise-ships"),
 "norwegian": dict(name="Norwegian Cruise Line", short="Norwegian", url="https://www.ncl.com/cruise-ships"),
 "msc": dict(name="MSC Cruises", short="MSC", url="https://www.msccruisesusa.com/"),
 "celebrity": dict(name="Celebrity Cruises", short="Celebrity", url="https://www.celebritycruises.com/cruise-ships"),
 "princess": dict(name="Princess Cruises", short="Princess", url="https://www.princess.com/en-us/ships-and-experience/ships"),
 "disney": dict(name="Disney Cruise Line", short="Disney", url="https://disneycruise.disney.go.com/ships/"),
}
RCL = "https://www.royalcaribbean.com/cruise-ships/{}/deck-plans"
CCL = "https://www.carnival.com/cruise-ships/{}/deck-plans"
NCL = "https://www.ncl.com/cruise-ship/{}/deck-plans"
CEL = "https://www.celebritycruises.com/cruise-ships/{}/deck-plans"
PCL = "https://www.princess.com/en-us/ships-and-experience/ships/{}"
DCL = "https://disneycruise.disney.go.com/ships/deck-plans/{}/"

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

SHIPS = [
 dict(slug="icon-of-the-seas", name="Icon of the Seas", line="royal-caribbean", cm="Icon-Of-The-Seas-2110", official=RCL.format("icon-of-the-seas"), wiki="Icon_of_the_Seas",
      facts=dict(cls="Icon class", builder="Meyer Turku", service="January 2024", gt="248,663", guests="5,610 (double occupancy)"), notes=ICON, sister=["star-of-the-seas"]),
 dict(slug="star-of-the-seas", name="Star of the Seas", line="royal-caribbean", cm="Star-Of-The-Seas-2112", official=RCL.format("star-of-the-seas"), wiki="Star_of_the_Seas",
      facts=dict(cls="Icon class", builder="Meyer Turku", service="August 2025", gt="248,663"), notes=ICON, sister=["icon-of-the-seas"]),
 dict(slug="utopia-of-the-seas", name="Utopia of the Seas", line="royal-caribbean", cm="Utopia-Of-The-Seas-2180", official=RCL.format("utopia-of-the-seas"), wiki="Utopia_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", gt="236,473"),
      notes=OASIS + [("Deck 3 forward", "On Utopia, CruiseMapper notes that forward oceanview cabins on deck 3 sit under the comedy club, a loyalty lounge and the casino on deck 4, so late-night noise is possible.")], sister=["wonder-of-the-seas", "symphony-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="wonder-of-the-seas", name="Wonder of the Seas", line="royal-caribbean", cm="Wonder-Of-The-Seas-2165", official=RCL.format("wonder-of-the-seas"), wiki="Wonder_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", service="March 2022", gt="235,600", guests="5,734 (double occupancy)"), notes=OASIS, sister=["utopia-of-the-seas", "symphony-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="symphony-of-the-seas", name="Symphony of the Seas", line="royal-caribbean", cm="Symphony-Of-The-Seas-1730", official=RCL.format("symphony-of-the-seas"), wiki="Symphony_of_the_Seas",
      facts=dict(cls="Oasis class", builder="Chantiers de l'Atlantique", service="April 2018", gt="228,081", guests="5,518 (double occupancy)"), notes=OASIS, sister=["utopia-of-the-seas", "wonder-of-the-seas", "oasis-of-the-seas"]),
 dict(slug="oasis-of-the-seas", name="Oasis of the Seas", line="royal-caribbean", cm="Oasis-Of-The-Seas-690", official=RCL.format("oasis-of-the-seas"), wiki="Oasis_of_the_Seas",
      facts=dict(cls="Oasis class", builder="STX Europe, Turku", service="December 2009", gt="226,838", guests="5,606 (double occupancy)"), notes=OASIS, sister=["utopia-of-the-seas", "wonder-of-the-seas", "symphony-of-the-seas"]),
 dict(slug="carnival-celebration", name="Carnival Celebration", line="carnival", cm="Carnival-Celebration-2106", official=CCL.format("carnival-celebration"), wiki="Carnival_Celebration",
      facts=dict(cls="Excellence class", builder="Meyer Turku", gt="183,521", guests="5,374 (double occupancy)"), notes=EXCELLENCE, sister=["mardi-gras", "carnival-jubilee"]),
 dict(slug="mardi-gras", name="Mardi Gras", line="carnival", cm="Carnival-Mardi-Gras-2105", official=CCL.format("mardi-gras"), wiki="Mardi_Gras_(2020_ship)",
      facts=dict(cls="Excellence class", builder="Meyer Turku", service="July 2021", gt="181,808", guests="5,282 (double occupancy)"), notes=EXCELLENCE, sister=["carnival-celebration", "carnival-jubilee"]),
 dict(slug="carnival-jubilee", name="Carnival Jubilee", line="carnival", cm="Carnival-Jubilee-2077", official=CCL.format("carnival-jubilee"), wiki="Carnival_Jubilee",
      facts=dict(cls="Excellence class", builder="Meyer Werft", service="December 2023", gt="183,521"), notes=EXCELLENCE, sister=["carnival-celebration", "mardi-gras"]),
 dict(slug="norwegian-prima", name="Norwegian Prima", line="norwegian", cm="Norwegian-Prima-2216", official=NCL.format("prima"), wiki="Norwegian_Prima",
      facts=dict(cls="Prima class", builder="Fincantieri", service="2022", gt="143,535"), notes=PRIMA, sister=["norwegian-viva"]),
 dict(slug="norwegian-viva", name="Norwegian Viva", line="norwegian", cm="Norwegian-Viva-2217", official=NCL.format("viva"), wiki="Norwegian_Viva",
      facts=dict(cls="Prima class", service="August 2023", gt="143,535"), notes=PRIMA, sister=["norwegian-prima"]),
 dict(slug="norwegian-encore", name="Norwegian Encore", line="norwegian", cm="Norwegian-Encore-1518", official=NCL.format("encore"), wiki="Norwegian_Encore",
      facts=dict(cls="Breakaway Plus class", builder="Meyer Werft", service="November 2019", gt="169,116", guests="3,998 (lower beds)"), notes=BREAKAWAY, sister=["norwegian-getaway"]),
 dict(slug="norwegian-getaway", name="Norwegian Getaway", line="norwegian", cm="Norwegian-Getaway-793", official=NCL.format("getaway"), wiki="Norwegian_Getaway",
      facts=dict(cls="Breakaway class", builder="Meyer Werft", service="February 2014", gt="145,655", guests="3,963"),
      notes=BREAKAWAY + [("Kids' areas on decks 12 and 13", "On Norwegian Getaway, CruiseMapper's deck plan places kids' areas on cabin decks 12 and 13. Handy for families; others may prefer decks 9 to 11.")], sister=["norwegian-encore"]),
 dict(slug="msc-world-america", name="MSC World America", line="msc", cm="MSC-World-America-2184", official="https://www.msccruisesusa.com/cruise/ships/msc-world-america", wiki="World-class_cruise_ship",
      facts=dict(cls="World class", gt="216,638", guests="6,764", src=("MSC Cruises: MSC World America in numbers", "https://www.msccruises.co.uk/ships/msc-world-america")),
      notes=[("Deck 9 sits over the promenade", "Deck 9 is the first cabin deck above deck 8, which has the promenade and the spa. Decks 10 to 15 are the quiet core."),
             ("Promenade-view balconies", "MSC sells balcony categories with a promenade view at the stern. They look over the ship's aft promenade rather than open sea, and the promenade is a social space."),
             ("Yacht Club is forward and high", "MSC Cruises says the Yacht Club spans the seven upper foredecks, with 152 suites. Suite-only areas mean fewer passers-by near those cabins."),
             ("Deck 16 sits under the main pool deck", "There is no deck 17, so deck 16 cabins are directly below deck 18 with its lido and pools.")], sister=[]),
 dict(slug="msc-seascape", name="MSC Seascape", line="msc", cm="MSC-Seascape-2144", official="https://www.msccruises.com/int/our-cruises/ships/msc-seascape", wiki="MSC_Seascape",
      facts=dict(cls="Seaside EVO class", gt="170,412", guests="4,540 (double occupancy)"), notes=SEASIDE, sister=["msc-seashore"]),
 dict(slug="msc-seashore", name="MSC Seashore", line="msc", cm="MSC-Seashore-2143", official="https://www.msccruises.com/int/our-cruises/ships/msc-seashore", wiki="MSC_Seashore",
      facts=dict(cls="Seaside EVO class", gt="170,412", guests="4,540 (double occupancy)"), notes=SEASIDE, sister=["msc-seascape"]),
 dict(slug="celebrity-beyond", name="Celebrity Beyond", line="celebrity", cm="Celebrity-Beyond-1690", official=CEL.format("celebrity-beyond"), wiki="Celebrity_Beyond",
      facts=dict(cls="Edge class", builder="Chantiers de l'Atlantique", service="April 2022", gt="141,420", guests="3,260 (double occupancy)"), notes=EDGE, sister=["celebrity-ascent", "celebrity-edge"]),
 dict(slug="celebrity-ascent", name="Celebrity Ascent", line="celebrity", cm="Celebrity-Ascent-2194", official=CEL.format("celebrity-ascent"), wiki="Celebrity_Ascent",
      facts=dict(cls="Edge class", builder="Chantiers de l'Atlantique", gt="141,420", guests="3,260 (double occupancy)"), notes=EDGE, sister=["celebrity-beyond", "celebrity-edge"]),
 dict(slug="celebrity-edge", name="Celebrity Edge", line="celebrity", cm="Celebrity-Edge-1588", official=CEL.format("celebrity-edge"), wiki="Celebrity_Edge",
      facts=dict(cls="Edge class", builder="STX France", service="December 2018", gt="130,818", guests="2,918"), notes=EDGE, sister=["celebrity-beyond", "celebrity-ascent"]),
 dict(slug="sun-princess", name="Sun Princess", line="princess", cm="Sun-Princess-2167", official=PCL.format("su-sun-princess"), wiki="Sun_Princess_(2024)",
      facts=dict(cls="Sphere class", builder="Fincantieri", service="February 2024", gt="177,882", guests="4,300"),
      notes=SPHERE + [("Solo interiors", "Sun Princess lists a single-occupancy inside category (IS) on deck 10, according to CruiseMapper.")], sister=["star-princess"]),
 dict(slug="star-princess", name="Star Princess", line="princess", cm="Star-Princess-2168", official=PCL.format("st-star-princess"), wiki="Star_Princess_(2024)",
      facts=dict(cls="Sphere class", service="October 2025", gt="177,882", guests="4,300"), notes=SPHERE, sister=["sun-princess"]),
 dict(slug="discovery-princess", name="Discovery Princess", line="princess", cm="Discovery-Princess-2157", official=PCL.format("xp-discovery-princess"), wiki="Discovery_Princess",
      facts=dict(cls="Royal class", builder="Fincantieri", service="March 2022", gt="145,000", guests="3,660"), notes=ROYAL_P, sister=[]),
 dict(slug="disney-wish", name="Disney Wish", line="disney", cm="Disney-Wish-2127", official=DCL.format("wish"), wiki="Disney_Wish",
      facts=dict(cls="Wish class", builder="Meyer Werft", service="July 2022", gt="144,000", guests="2,508 (double occupancy)"), notes=WISH, sister=["disney-treasure", "disney-destiny"]),
 dict(slug="disney-treasure", name="Disney Treasure", line="disney", cm="Disney-Treasure-2128", official=DCL.format("treasure"), wiki="Disney_Treasure",
      facts=dict(cls="Wish class", builder="Meyer Werft", gt="144,256", guests="2,492 (double occupancy)"), notes=WISH, sister=["disney-wish", "disney-destiny"]),
 dict(slug="disney-destiny", name="Disney Destiny", line="disney", cm="Disney-Destiny-2129", official=DCL.format("destiny"), wiki="Disney_Destiny",
      facts=dict(cls="Wish class", builder="Meyer Werft", service="November 2025", gt="144,000", guests="2,508 (double occupancy)"), notes=WISH, sister=["disney-wish", "disney-treasure"]),
]
