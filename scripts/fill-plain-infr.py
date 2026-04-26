from bs4 import BeautifulSoup
from pathlib import Path

PLAIN_LANGUAGE = {
    # --- Internet / Network Infrastructure ---
    "INFR-NETS-0001": (
        "This policy treats internet and communications networks as public infrastructure — "
        "like roads and bridges — that should be managed for everyone's benefit, not controlled "
        "by private monopolies for profit."
    ),
    "INFR-NETS-0002": (
        "Internet providers can compete on price and service quality, but the physical cables "
        "and wires that carry internet traffic must be shared infrastructure — not locked up by "
        "a single company — so all providers can reach customers and everyone has access."
    ),
    "INFR-NETS-0003": (
        "This policy guarantees high-speed internet access for people in rural, remote, and "
        "underserved communities through public investment, treating it with the same urgency "
        "as bringing electricity to rural America in the 1930s."
    ),
    "INFR-NETS-0004": (
        "This rule requires the FCC to verify internet coverage using independent, address-level "
        "testing — not just take internet companies' word for it. Accurate coverage maps ensure "
        "federal broadband funding actually reaches communities that lack service."
    ),
    "INFR-NETS-0005": (
        "This policy prohibits federal broadband dollars from going to areas that internet "
        "companies falsely claim are already well-served. Residents and local governments can "
        "challenge coverage claims, and agencies must review those challenges before awarding "
        "any funding."
    ),
    # --- Grid / Energy Infrastructure ---
    "INFR-GRDS-0001": (
        "This policy invests in upgrading the national power grid to handle clean energy from "
        "solar and wind, prevent blackouts during extreme weather, and guard against cyberattacks "
        "— so Americans have reliable electricity now and in the future."
    ),
    "INFR-GRDS-0002": (
        "This policy invests in local microgrids — smaller, self-contained power networks that "
        "let neighborhoods keep their lights on even when the main electrical grid goes down "
        "during storms or emergencies, reducing the risk of widespread cascading blackouts."
    ),
    "INFR-GRDS-0003": (
        "This policy requires the national power grid to reach net-zero — and eventually "
        "negative — carbon emissions on a fixed, enforceable schedule with defined milestones. "
        "Cleaning up electricity generation is one of the most direct ways to address climate change."
    ),
    # --- Renewable Energy ---
    "INFR-ENRS-0001": (
        "This policy commits the federal government to invest heavily in solar, wind, and energy "
        "storage on a national scale — treating clean power as essential public infrastructure, "
        "as important to the country's future as the interstate highway system."
    ),
    "INFR-ENRS-0002": (
        "This policy cuts unnecessary red tape for nuclear power projects that meet safety "
        "standards, giving developers predictable approval timelines so reliable, low-carbon "
        "nuclear energy can be built faster without sacrificing safety."
    ),
    "INFR-ENRS-0003": (
        "This policy ends government tax breaks and subsidies for oil and coal companies and "
        "redirects that money toward clean energy development and support for workers and "
        "communities transitioning away from fossil fuels."
    ),
    "INFR-ENRS-0004": (
        "This policy sets a binding, enforceable timeline to end the use of oil and coal in "
        "electricity generation, with defined milestones and support for affected workers and "
        "communities — and no loopholes that allow indefinite delays."
    ),
    "INFR-ENRS-0005": (
        "This policy commits the government to a guaranteed phase-out of oil and coal as energy "
        "sources. Moving away from fossil fuels reduces air pollution, slows climate change, and "
        "shifts public and private investment toward cleaner alternatives."
    ),
    # --- Building Standards ---
    "INFR-BLDS-0001": (
        "This policy updates federal building codes to require new construction to use energy "
        "efficiently, incorporate renewable energy like solar, and use sustainable materials — "
        "with standards that improve over time as better technology becomes available."
    ),
    "INFR-BLDS-0002": (
        "This policy requires major public infrastructure projects — from bridges to transit "
        "stations — to have net-zero or better carbon emissions across their entire life, counting "
        "the emissions from building and operating them, not only from day-to-day operations."
    ),
    # --- Water Systems ---
    "INFR-WATS-0001": (
        "This policy funds drought-resistant water systems — including plants that convert "
        "saltwater to drinking water and water recycling facilities — in dry regions, with "
        "strict rules to prevent these projects from draining underground water supplies or "
        "damaging freshwater ecosystems."
    ),
    "INFR-WATS-0002": (
        "This policy requires all lead water pipes connected to homes, schools, childcare "
        "centers, and public housing to be replaced within 10 years, at federal expense for "
        "low-income households. Until the pipes are replaced, households receive free filters "
        "and water testing to protect children from lead poisoning."
    ),
    "INFR-WATS-0003": (
        "This policy creates a national dam safety program requiring regular inspections of all "
        "dams that could cause serious harm if they failed. High-risk dams must have emergency "
        "action plans, and the federal government can order repairs or decommission dams that "
        "put communities in immediate danger."
    ),
    # --- Data Infrastructure ---
    "INFR-DATA-0001": (
        "This policy requires large data centers — which consume enormous amounts of electricity "
        "— to power themselves with dedicated clean energy sources rather than drawing from "
        "fossil-fuel-powered grids, so the rapid growth of the digital economy does not drive "
        "up carbon emissions."
    ),
    # --- Rail ---
    "INFR-RAIL-0001": (
        "This policy funds major upgrades to U.S. rail infrastructure — including tracks, "
        "signals, electrification, and stations — so that trains become faster, safer, and "
        "more reliable for passengers and for moving freight across the country."
    ),
    "INFR-RAIL-0002": (
        "This policy invests in high-speed rail lines connecting major cities, giving travelers "
        "a fast, comfortable alternative to short-haul flights and congested highways while "
        "reducing pollution and traffic."
    ),
    "INFR-RAIL-0003": (
        "This policy creates an independent public authority to manage the busy rail corridor "
        "from Washington D.C. to Boston, so passenger trains no longer get stuck waiting for "
        "freight trains. It also gives Amtrak trains legal priority on all routes, with real "
        "federal penalties for freight companies that cause delays."
    ),
    "INFR-RAIL-0004": (
        "This policy restructures Amtrak as a public service — not a profit-driven business — "
        "with a guaranteed five-year federal budget that cannot be eliminated in any single "
        "budget cycle. No Amtrak route can be shut down without an independent review confirming "
        "that communities won't lose vital transportation."
    ),
    "INFR-RAIL-0005": (
        "This policy requires all new and substantially renovated federally funded rail lines to "
        "run on electricity. After January 1, 2027, no federal money can go to diesel-only rail "
        "projects, and existing diesel corridors must submit federally funded conversion plans "
        "with full electrification completed within 15 years."
    ),
    "INFR-RAIL-0006": (
        "This policy requires large freight railroads to share their tracks with passenger and "
        "competing freight trains at regulated prices, so no single railroad can monopolize key "
        "routes. It also bans railroads from cutting train crews and route redundancy to boost "
        "profits at the expense of safety and on-time performance."
    ),
    # --- Public Transportation ---
    "INFR-TRAN-0001": (
        "This policy funds major expansion of buses, light rail, subways, and on-demand transit "
        "services in cities, suburbs, and rural areas, so more people have reliable ways to "
        "get where they need to go without depending on a personal vehicle."
    ),
    "INFR-TRAN-0002": (
        "This policy requires every major infrastructure decision to center public transit — "
        "including access for people with disabilities — as a core priority, not an afterthought. "
        "Affordable and reliable transportation is treated as a basic public need."
    ),
    "INFR-TRAN-0003": (
        "This policy sets a firm, credible timeline to end new sales of gasoline-only and "
        "combustion-engine-only passenger vehicles, with support programs for automakers, "
        "workers, and buyers to manage the shift to cleaner alternatives."
    ),
    "INFR-TRAN-0004": (
        "In vehicle categories where full electric options are not yet practical or affordable, "
        "this policy requires plug-in hybrid capability at minimum — so vehicles can run on "
        "electricity for shorter trips while charging infrastructure is built out nationwide."
    ),
    "INFR-TRAN-0005": (
        "While gas-powered vehicles are still being sold, this policy sets and regularly "
        "tightens strict fuel-efficiency standards with no exemptions or rollback provisions, "
        "cutting pollution from the millions of combustion-engine vehicles already on the road."
    ),
    "INFR-TRAN-0006": (
        "This policy funds a national EV charging network ensuring no rural community is more "
        "than 50 miles from a fast charger, apartment buildings must have charging access, and "
        "lower-income communities are specifically targeted for investment — so the shift to "
        "electric vehicles works for everyone, not just homeowners with garages."
    ),
    # --- Transit Funding ---
    "INFR-FUND-0001": (
        "This policy creates a dedicated federal fund for public transit matched in size to the "
        "Highway Trust Fund that pays for roads. Transit agencies receive funding within 90 days "
        "of each fiscal year so that service disruptions caused by budget uncertainty are "
        "eliminated."
    ),
    "INFR-FUND-0002": (
        "This policy requires that every federal dollar spent on new highway lane-miles in "
        "metro areas over 200,000 people be matched with an equal federal investment in public "
        "transit in the same region. Highway expansions can no longer crowd out transit funding."
    ),
    "INFR-FUND-0003": (
        "This policy allows transit agencies to receive federal funding that covers 50% of "
        "day-to-day operating costs — like driver wages, fuel, and maintenance — not just "
        "construction. This prevents transit agencies from cutting service or raising fares "
        "during economic downturns."
    ),
    "INFR-FUND-0004": (
        "This policy prohibits federal transit dollars from being spent on police or surveillance "
        "for fare enforcement. Unpaid fares become civil matters — handled like an administrative "
        "fine — and no one can be arrested or given a criminal record simply for not paying a "
        "bus or train fare."
    ),
    # --- Transit Affordability ---
    "INFR-AFRD-0001": (
        "This policy makes public transit fare-free in cities with more than 500,000 people, "
        "funded by federal subsidies and fees charged to drivers entering congested downtown "
        "areas. Cities going fare-free must maintain the same routes, frequency, and fleet size "
        "— no service cuts allowed."
    ),
    "INFR-AFRD-0002": (
        "This policy prohibits arresting, prosecuting, or giving anyone a criminal record for "
        "not paying a transit fare. Fare evasion becomes a civil infraction with a maximum fine "
        "of $100, and that fine is waived for people earning below twice the federal poverty level."
    ),
    "INFR-AFRD-0003": (
        "This policy requires metro areas with more than 1 million people to charge drivers a "
        "fee to enter the most congested downtown areas within 5 years. All money collected — "
        "after administrative costs — must be spent on public transit in that same region, so "
        "driving fees directly fund better transit options."
    ),
    # --- Rural Transit ---
    "INFR-RURL-0001": (
        "This policy guarantees that every community of 2,500 or more people has at least one "
        "daily, publicly subsidized transit connection to the nearest city or county seat. The "
        "federal government steps in to fund it when states and localities fail to provide the "
        "required service."
    ),
    "INFR-RURL-0002": (
        "This policy restores intercity bus routes in rural areas that lost service when private "
        "bus companies like Greyhound cut their networks. Modeled on the Essential Air Service "
        "program for small airports, it subsidizes carriers — public or private — to run at "
        "least one round trip daily on abandoned rural corridors."
    ),
    "INFR-RURL-0003": (
        "In rural communities where running a regular bus route is not cost-effective, this "
        "policy guarantees residents access to a publicly subsidized, on-demand ride service "
        "for medical, work, and essential trips — bookable by phone or app — with same-day "
        "availability for medical appointments."
    ),
    # --- Transit-Oriented Development ---
    "INFR-TODS-0001": (
        "This policy requires any city receiving federal money to build a transit station to "
        "allow dense, mixed-use, mixed-income development within a half-mile of that station "
        "within 5 years. At least 40 housing units per acre must be permitted without special "
        "review, and cities that refuse lose future federal transit funding."
    ),
    "INFR-TODS-0002": (
        "This policy overrides local zoning laws that limit land near federally funded transit "
        "stations to single-family homes only. Within a quarter mile of any such station, "
        "apartment buildings of at least 3 stories must be allowed by federal right, and "
        "mandatory minimum parking requirements are automatically eliminated."
    ),
    "INFR-TODS-0003": (
        "This policy requires that at least 30% of homes in federally funded developments near "
        "transit stations be affordable to families earning 60% or less of the area median "
        "income, with those affordable rents locked in for a minimum of 40 years. Federal funds "
        "cannot be used for projects that displace lower-income residents without replacing "
        "those homes nearby."
    ),
    # --- ADA / Accessibility ---
    "INFR-ADAX-0001": (
        "This policy fully funds ADA paratransit — the door-to-door transit service for people "
        "with disabilities — and requires same-day service for medical and emergency trips within "
        "4 hours of request. If a transit agency unlawfully denies service, the affected person "
        "can sue in federal court and recover at least $500 per incident."
    ),
    "INFR-ADAX-0002": (
        "This policy requires all new transit vehicles and stations to be fully accessible to "
        "people with disabilities, with no exceptions. Existing inaccessible stations and vehicles "
        "must be fixed within 10 years, and agencies must publish annual public reports tracking "
        "their progress toward full compliance."
    ),
    # --- Streets / Active Transportation ---
    "INFR-STRT-0001": (
        "This policy requires every federally funded road project to include safe sidewalks, "
        "bike lanes, and transit access — no exceptions, no waivers. Roads must be designed for "
        "pedestrians, cyclists, and transit riders, not just for drivers."
    ),
    "INFR-STRT-0002": (
        "This policy funds continuous sidewalks and protected bike lanes connecting neighborhoods "
        "to transit stops within 1 mile, prioritizing low-income areas and neighborhoods with "
        "the highest pedestrian injury rates. All paths must be accessible for wheelchairs and "
        "mobility devices."
    ),
    "INFR-STRT-0003": (
        "This policy blocks new federal highway lane additions in large metro areas over 500,000 "
        "people unless an equal or greater transit investment for the same corridor is fully "
        "funded and ready to build at the same time. Highway widening cannot break ground until "
        "the paired transit investment is secured."
    ),
    "INFR-STRT-0004": (
        "This policy requires major commercial airports receiving $50 million or more a year in "
        "federal grants to have a direct rail or rapid transit connection — or a funded plan to "
        "build one within 10 years. Cost alone is not an acceptable reason to skip the transit "
        "connection requirement."
    ),
    # --- Transit Labor ---
    "INFR-LBRT-0001": (
        "This policy makes it a federal felony to assault any transit worker on the job, with a "
        "mandatory minimum prison sentence of at least 1 year. All federally funded transit "
        "vehicles must install physical barriers protecting drivers and operators from the "
        "passenger area within 3 years."
    ),
    "INFR-LBRT-0002": (
        "This policy strengthens federal rules that tie transit funding to respect for transit "
        "workers' union rights. Transit agencies must certify each year that they have not "
        "undermined workers' collective bargaining or union status — agencies that violate this "
        "must repay up to 3 years of federal transit funding."
    ),
    "INFR-LBRT-0003": (
        "This policy sets federal safety standards for bus drivers: at least 8 consecutive hours "
        "off between shifts, and no split shifts with more than 10 hours from start to finish. "
        "Fatigued drivers are a safety risk to themselves and everyone on the road, and bus "
        "operators have a private right of action if these standards are violated."
    ),
    # --- Utility Regulation ---
    "INFR-UTIL-0001": (
        "This policy prohibits electric utility companies from passing their lobbying and "
        "political advertising costs on to customers through higher rates. Utilities must keep "
        "separate accounting for political spending, and customers can sue to recover three "
        "times any political cost improperly included in their rates."
    ),
    "INFR-UTIL-0002": (
        "This policy requires every state to fund an independent consumer advocate who "
        "represents ratepayers in electric utility rate cases, with full legal standing to "
        "challenge the utility's claims. Rate increases must have at least 45 days of public "
        "notice and a written response to all significant public comments."
    ),
    "INFR-UTIL-0003": (
        "This policy caps the profit electric utility companies can earn at 9.5%, with up to "
        "10.5% allowed only if the utility meets grid reliability, clean energy, and low-income "
        "affordability goals. Utilities that miss those targets must refund excess profits "
        "directly to their customers."
    ),
    "INFR-UTIL-0004": (
        "This policy guarantees every electric customer — including renters who cannot install "
        "rooftop solar — access to community solar programs with bill credits at the full retail "
        "rate. Customers with their own solar panels must be paid a fair rate for the power they "
        "send back to the grid, and utilities cannot charge discriminatory fees to solar customers."
    ),
    "INFR-UTIL-0005": (
        "This policy prohibits electric utilities from shutting off residential power during "
        "extreme heat above 95°F or cold below 32°F, when a household member has a "
        "life-sustaining medical condition, or within 30 days of a customer applying for "
        "assistance. All customers must receive 30 days' written notice and a payment plan "
        "offer before disconnection, and wrongful shutoffs carry a $1,000-per-day penalty "
        "payable directly to the customer."
    ),
    "INFR-UTIL-0006": (
        "This policy gives any city or county the right to take over its local electric "
        "distribution system from a private utility at a fair price, without paying an inflated "
        "franchise premium. State laws that ban cities from forming public utilities are "
        "overridden, and public utility districts must be governed by elected boards."
    ),
    # --- Affordability / Access ---
    "INFR-AFDS-0001": (
        "This policy guarantees that every household can afford basic internet, electricity, "
        "and clean water, with income-based subsidies and tiered pricing for lower-income "
        "families. Service cannot be shut off for non-payment during declared health emergencies "
        "or extreme weather events."
    ),
    "INFR-AFDS-0002": (
        "This policy prohibits states from blocking cities, counties, or community cooperatives "
        "from building and running their own internet networks. In areas where private providers "
        "fail to deliver adequate broadband, communities have the legal right to build their "
        "own — and federal law overrides any state laws that stand in the way."
    ),
    # --- Infrastructure Labor Standards ---
    "INFR-LBRS-0001": (
        "This policy requires every contractor on a federally funded infrastructure project to "
        "pay prevailing wages — the standard rate for that trade in that region — and to classify "
        "workers as employees rather than independent contractors where the work relationship "
        "warrants it. Contractors that cheat workers out of proper wages or status lose federal "
        "funding."
    ),
    "INFR-LBRS-0002": (
        "This policy guarantees income support, paid retraining, and community investment funds "
        "for workers and towns whose jobs and economies are displaced by federally required "
        "transitions — like closing coal plants, electrifying vehicles, or automating "
        "transportation. The people who bear the cost of the transition are not left behind."
    ),
    # --- Environmental Justice ---
    "INFR-EQJS-0001": (
        "This policy requires an environmental justice review before approving highways, power "
        "plants, pipelines, waste facilities, and other major infrastructure projects. Projects "
        "that would put a disproportionate share of pollution or health burdens on low-income "
        "communities or communities of color cannot be approved without meaningful community "
        "input and adequate protections."
    ),
    "INFR-EQJS-0002": (
        "This policy requires federal clean energy investments — like community solar, efficiency "
        "upgrades, and EV charging — to reach disadvantaged communities proportionally. The "
        "clean energy transition must not repeat the historical pattern where wealthy communities "
        "get the benefits while low-income and minority communities bear the environmental and "
        "economic costs."
    ),
    # --- Ports ---
    "INFR-PRTS-0001": (
        "This policy funds modernization of U.S. ports — upgrading equipment, electrifying "
        "operations, and deepening channels — but only if binding agreements protect port "
        "workers displaced by automation with income support, retraining, and first priority "
        "for new technical roles. Federal port funding goes first to ports critical to supply "
        "chains or burdened by environmental impacts on surrounding communities."
    ),
    "INFR-PRTS-0002": (
        "This policy requires the U.S. to maintain minimum domestic production capacity and "
        "strategic stockpiles of critical goods — including medicines, microchips, and power "
        "grid components — so the country is never entirely dependent on a single foreign "
        "country for supplies essential to national security and public health."
    ),
}

html_path = Path("docs/pillars/infrastructure-and-public-goods.html")
soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

updated = 0
skipped_already_filled = 0
missing_ids = []

for card in soup.find_all("div", class_="policy-card"):
    card_id = card.get("id", "")
    if not card_id or card_id not in PLAIN_LANGUAGE:
        if card_id:
            missing_ids.append(card_id)
        continue

    # If rule-plain already exists and is filled, skip it
    plain_p = card.find("p", class_="rule-plain")
    if plain_p is not None:
        if plain_p.get_text(strip=True):
            skipped_already_filled += 1
            continue
        plain_p.string = PLAIN_LANGUAGE[card_id]
        updated += 1
        continue

    # Insert new <p class="rule-plain"> after <p class="rule-title">
    title_p = card.find("p", class_="rule-title")
    if title_p is None:
        continue
    new_p = soup.new_tag("p", attrs={"class": "rule-plain"})
    new_p.string = PLAIN_LANGUAGE[card_id]
    title_p.insert_after(new_p)
    updated += 1

html_path.write_text(str(soup), encoding="utf-8")
print(f"Updated {updated} cards")
if skipped_already_filled:
    print(f"Skipped {skipped_already_filled} cards already filled")
if missing_ids:
    print(f"WARNING: {len(missing_ids)} card IDs not in PLAIN_LANGUAGE dict: {missing_ids}")
