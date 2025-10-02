#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from string import Template

family_order = [
    "aquatic",
    "citrus",
    "floral",
    "fruity",
    "gourmand",
    "green",
    "spice",
    "woody",
]

collections = {
    "aquatic": {
        "name": "Aquatic",
        "page_title": "Aquatic Fragrance Family – Celestial Candle Studio",
        "background": "#f6f9fb",
        "text_primary": "#1f1c1a",
        "text_secondary": "#58626f",
        "accent": "#6a8ed6",
        "accent_dark": "#4f74bf",
        "border": "#d9e2f0",
        "overlay_rgba": "rgba(32, 43, 63, 0.45)",
        "feature_bg": "rgba(246, 249, 251, 0.9)",
        "hero_image": "https://images.unsplash.com/photo-1518459031867-a89b944bffe4?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(17, 32, 54, 0.78) 18%, rgba(17, 32, 54, 0.45) 45%, rgba(17, 32, 54, 0.15))",
        "hero_kicker": "Aquatic fragrance family",
        "hero_heading": "Salt-kissed botanicals that echo the horizon.",
        "hero_copy": "Our aquatic scents are composed to mirror slow tides, sunlit harbors, and the mineral calm of ocean spray. Clean-burning coconut-soy wax carries each breeze-inspired note from first light to final ember.",
        "description_intro": "Crafted in small batches inside our Brooklyn studio, each aquatic candle blends marine botanicals, citrus zest, and mineral accords. The result is a serene, airy palette that uplifts open windows, breathes life into morning rituals, and transforms homes into coastal retreats.",
        "description_detail": "To minimize environmental impact, every vessel is recyclable and ready for reuse as a bud vase or tumbler once your candle is finished.",
        "meta_secondary": "60 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Refined for open-air spaces",
                "body": "Our aquatic candles deliver a balanced throw that fills airy lofts and breezy patios without overwhelming. Each blend is tested across different room sizes to ensure an even diffusion.",
            },
            {
                "title": "Crafted for mindful rituals",
                "body": "Pairs beautifully with morning journaling, post-yoga stretches, and evening wind-down routines. Layer with ambient playlists and chilled mineral water for a complete retreat.",
            },
        ],
        "palette_intro": "Every aquatic blend balances mineral, floral, and citrus elements to mimic the movement of water.",
        "palette": [
            {"title": "Top", "body": "Sea salt, bergamot zest, frozen pear."},
            {"title": "Heart", "body": "Water lily, blue cypress, neroli petals."},
            {"title": "Base", "body": "Driftwood, mineral musk, sun-warmed amber."},
            {"title": "Pair with", "body": "Soft linen throws, coastal ceramics, field recordings of waves."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=900&q=80",
                "alt": "Minimalist white candle on wooden table",
                "kicker": "Calm waters",
                "title": "Shop aquatic candles",
            },
            {
                "img": "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?auto=format&fit=crop&w=900&q=80",
                "alt": "Soft ocean waves rolling over sand",
                "kicker": "Seaside escapes",
                "title": "Discover coastal rituals",
            },
        ],
        "products": [
            {
                "id": "tide",
                "tag": "Signature",
                "name": "Midnight Tide",
                "description": "Sea salt, ozone, and violet leaf conjure twilight walks on misty shores.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside crashing waves at sunset",
            },
            {
                "id": "terrace",
                "tag": "Limited batch",
                "name": "Sea Terrace",
                "description": "Neroli, petitgrain, and salted amber recreate breezy afternoons on a cliffside villa.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle glowing beside Mediterranean sea view",
            },
            {
                "id": "shoreline",
                "tag": "Best seller",
                "name": "Luminous Shore",
                "description": "Crisp pear, coastal jasmine, and driftwood lighten interiors with marine brightness.",
                "price": "42",
                "image": "https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?auto=format&fit=crop&w=900&q=80",
                "alt": "Minimal candle styled with sea grass",
            },
            {
                "id": "drift",
                "tag": "Customer favorite",
                "name": "Salt & Drift",
                "description": "Frosted eucalyptus, kelp, and mineral musk create a restorative spa moment.",
                "price": "40",
                "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=900&q=80",
                "alt": "White candle beside smooth sea stones",
            },
            {
                "id": "spray",
                "tag": "Studio exclusive",
                "name": "Ocean Spray",
                "description": "Water lily, beach grass, and chilled citrus open windows to a fresh Atlantic breeze.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1528838060453-1f3c9e0f4591?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle in bathroom with flowing water",
            },
            {
                "id": "lagoons",
                "tag": "New arrival",
                "name": "Blue Lagoons",
                "description": "Lotus blossom, chilled coconut, and crystalline ozone celebrate island mornings.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1533135431861-9b1c3ebf36af?auto=format&fit=crop&w=900&q=80",
                "alt": "Turquoise lagoon and candle",
            },
        ],
        "bundle_heading": "Build your own coastal candle trio.",
        "bundle_copy": "Select any three aquatic scents and save 10%. Perfect for gifting or layering across rooms.",
        "best_sellers": ["tide", "terrace", "shoreline", "drift", "spray", "lagoons"],
    },
    "citrus": {
        "name": "Citrus",
        "page_title": "Citrus Fragrance Family – Celestial Candle Studio",
        "background": "#fff8f1",
        "text_primary": "#2c2014",
        "text_secondary": "#8a6542",
        "accent": "#f6a23b",
        "accent_dark": "#e1891f",
        "border": "#ffe2c7",
        "overlay_rgba": "rgba(198, 116, 45, 0.45)",
        "feature_bg": "rgba(255, 248, 241, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(173, 92, 35, 0.8) 20%, rgba(173, 92, 35, 0.52) 48%, rgba(173, 92, 35, 0.2))",
        "hero_kicker": "Citrus fragrance family",
        "hero_heading": "Sun-drenched zest bottled for everyday radiance.",
        "hero_copy": "We capture ripe groves, golden hours, and sparkling aperitivos in bright, effervescent blends. Each candle layers juicy fruits with aromatic herbs for an instant lift of energy.",
        "description_intro": "Hand poured in micro-batches, our citrus candles layer freshly peeled fruits with herbal undertones and airy florals. They wake up sleepy kitchens, boost focus in studios, and bring the warmth of Mediterranean afternoons into every room.",
        "description_detail": "All ingredients are clean-burning and vegan, while each glass tumbler is designed for reuse—rinse with warm water to refill with blooms or cold brew.",
        "meta_secondary": "60 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Designed for instant uplift",
                "body": "Each citrus blend is calibrated to spark joy within the first five minutes of lighting, offering a clean throw that invigorates kitchens, offices, and entryways without overpowering.",
            },
            {
                "title": "Perfect for daily rituals",
                "body": "Pair with morning movement, afternoon focus sprints, or evening mocktails. Layer with playlists that balance bossa nova and soft electronic beats for a sensory reset.",
            },
        ],
        "palette_intro": "Every citrus blend balances fruit, herb, and soft floral notes to bring effortless radiance indoors.",
        "palette": [
            {"title": "Top", "body": "Meyer lemon, pink grapefruit, bergamot peel."},
            {"title": "Heart", "body": "Orange blossom, verbena, crushed mint."},
            {"title": "Base", "body": "Golden amber, white musk, vanilla bean."},
            {"title": "Pair with", "body": "Hand-thrown ceramics, sparkling tonics, sun-warmed playlists."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle surrounded by sliced citrus fruits",
                "kicker": "Golden hour glow",
                "title": "Shop citrus candles",
            },
            {
                "img": "https://images.unsplash.com/photo-1524592099565-3ff1eb892a90?auto=format&fit=crop&w=900&q=80",
                "alt": "Hands zesting fresh citrus over cocktails",
                "kicker": "Citrus rituals",
                "title": "Discover spritz-ready blends",
            },
        ],
        "products": [
            {
                "id": "sunrise",
                "tag": "Signature",
                "name": "Sunrise Grove",
                "description": "Sparkling mandarin, sunlit neroli, and basil leaf brighten breakfast rituals.",
                "price": "42",
                "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside fresh oranges on a breakfast table",
            },
            {
                "id": "amalfi",
                "tag": "Bestseller",
                "name": "Amalfi Spritz",
                "description": "Blood orange, prosecco accord, and tonka bean evoke golden-hour aperitivos.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with citrus cocktail on terrace",
            },
            {
                "id": "clementine",
                "tag": "Limited batch",
                "name": "Clementine Bloom",
                "description": "Sweet clementine, orange blossom, and whipped vanilla soften evening rituals.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1502741338009-cac2772e18bc?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle surrounded by blooming orange blossoms",
            },
            {
                "id": "pomelo",
                "tag": "Customer favorite",
                "name": "Golden Pomelo",
                "description": "Pomelo zest, white tea, and ginger root energize workspaces with crisp clarity.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with sliced pomelos on marble",
            },
            {
                "id": "seville",
                "tag": "New arrival",
                "name": "Seville Siesta",
                "description": "Bitter orange, rosemary, and sun-warmed terracotta transport you to Andalusian courtyards.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1482938288295-86c0ebb67ff8?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle near terracotta and oranges",
            },
            {
                "id": "yuzu",
                "tag": "Refreshing",
                "name": "Yuzu Tonic",
                "description": "Japanese yuzu, lemongrass, and chilled seltzer enliven late-afternoon resets.",
                "price": "41",
                "image": "https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with yuzu slices and sparkling water",
            },
        ],
        "bundle_heading": "Build a zesty candle flight.",
        "bundle_copy": "Select any three citrus blends and save 10%. Mix bright mornings with cozy twilight aromas.",
        "best_sellers": ["sunrise", "amalfi", "clementine", "pomelo", "seville", "yuzu"],
    },
    "floral": {
        "name": "Floral",
        "page_title": "Floral Fragrance Family – Celestial Candle Studio",
        "background": "#fdf7fb",
        "text_primary": "#2c1b22",
        "text_secondary": "#7c5a68",
        "accent": "#d48bb0",
        "accent_dark": "#b86a91",
        "border": "#f4dce7",
        "overlay_rgba": "rgba(214, 139, 176, 0.45)",
        "feature_bg": "rgba(253, 247, 251, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(148, 69, 109, 0.82) 20%, rgba(148, 69, 109, 0.5) 48%, rgba(148, 69, 109, 0.18))",
        "hero_kicker": "Floral fragrance family",
        "hero_heading": "Lush blooms captured at their most romantic.",
        "hero_copy": "Our floral portfolio weaves together heritage blooms, rare petals, and airy musks to mimic bouquets at peak bloom. Each light sets the scene for slow mornings and lingering evenings.",
        "description_intro": "Petal-infused wax pools carry you through sunlit conservatories and moonlit gardens. We sketch every fragrance like a perfumer—layering sparkling tops, abundant hearts, and soft bases for depth.",
        "description_detail": "We work with traceable growers and vegan wax blends to ensure each floral composition is as kind to the planet as it is to your space.",
        "meta_secondary": "60 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Bouquet-inspired storytelling",
                "body": "Each candle mirrors the journey of a real bouquet—from the first cut stem to the final dried petal—so the aroma evolves as it burns.",
            },
            {
                "title": "Soft yet long-lasting",
                "body": "Phthalate-free oils meld with our coconut-soy wax for a velvety throw that lingers without overwhelming sensitive noses.",
            },
        ],
        "palette_intro": "Every floral blend is built like a bouquet with sparkling tops, lush hearts, and gauzy bases.",
        "palette": [
            {"title": "Top", "body": "Pink pepper, dew-kissed rose, bergamot."},
            {"title": "Heart", "body": "Peony, gardenia, night-blooming jasmine."},
            {"title": "Base", "body": "Amber silk, white musk, soft woods."},
            {"title": "Pair with", "body": "Linen table runners, vintage vinyl, handwritten notes."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?auto=format&fit=crop&w=900&q=80",
                "alt": "Soft pink candle surrounded by roses",
                "kicker": "Soft focus",
                "title": "Shop floral bestsellers",
            },
            {
                "img": "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?auto=format&fit=crop&w=900&q=80",
                "alt": "Florist arranging blooms at a worktable",
                "kicker": "Studio blooms",
                "title": "See how we blend petals",
            },
        ],
        "products": [
            {
                "id": "peony",
                "tag": "Signature",
                "name": "Moonlit Peony",
                "description": "Peony, pink pepper, and suede musk bring twilight romance indoors.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with blush peonies at dusk",
            },
            {
                "id": "garden",
                "tag": "Bestseller",
                "name": "Garden Reverie",
                "description": "Rose de mai, freesia, and cashmere woods recall greenhouse strolls.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1448932223592-d1fc686e76ea?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle nestled among garden florals",
            },
            {
                "id": "iris",
                "tag": "Limited batch",
                "name": "Iris Lullaby",
                "description": "Powdery iris, violet leaf, and vanilla orchid whisper in the background.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=900&q=80",
                "alt": "Floral candle atop a vanity",
            },
            {
                "id": "rose",
                "tag": "Cult favorite",
                "name": "Wild Rose Atlas",
                "description": "Damask rose, amber resin, and oud capture moody blooms at midnight.",
                "price": "48",
                "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=900&q=80",
                "alt": "Deep red roses with a glowing candle",
            },
            {
                "id": "lilac",
                "tag": "New arrival",
                "name": "Lilac Postcard",
                "description": "Lilac petals, mimosa, and rain accord deliver first-bloom nostalgia.",
                "price": "42",
                "image": "https://images.unsplash.com/photo-1437750769465-301382cdf094?auto=format&fit=crop&w=900&q=80",
                "alt": "Lilac blossoms in glass beside candle",
            },
            {
                "id": "honeysuckle",
                "tag": "Summer edit",
                "name": "Honeysuckle Haze",
                "description": "Honeysuckle, tuberose, and white tea drift through open windows.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1509305717900-84f40e786d30?auto=format&fit=crop&w=900&q=80",
                "alt": "Honeysuckle vines cascading near a candle",
            },
        ],
        "bundle_heading": "Curate your dream bouquet trio.",
        "bundle_copy": "Select any three floral candles and receive 10% off—perfect for gifting bridesmaids or dressing up bedside tables.",
        "best_sellers": ["peony", "garden", "iris", "rose", "lilac", "honeysuckle"],
    },
    "fruity": {
        "name": "Fruity",
        "page_title": "Fruity Fragrance Family – Celestial Candle Studio",
        "background": "#fff6f8",
        "text_primary": "#271114",
        "text_secondary": "#8a5060",
        "accent": "#f47ba6",
        "accent_dark": "#d65a84",
        "border": "#ffd6e4",
        "overlay_rgba": "rgba(229, 110, 152, 0.45)",
        "feature_bg": "rgba(255, 246, 248, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(212, 93, 132, 0.82) 22%, rgba(212, 93, 132, 0.5) 50%, rgba(212, 93, 132, 0.18))",
        "hero_kicker": "Fruity fragrance family",
        "hero_heading": "Juicy infusions that feel like market mornings.",
        "hero_copy": "Our fruit-forward candles pop with ripe berries, orchard stone fruit, and sparkling accords that brighten any gathering.",
        "description_intro": "Inspired by farmers' market hauls and long brunches, these blends pair lush fruit with cooling botanicals to stay refreshing from first burn to last.",
        "description_detail": "We fortify each fragrance with cold-pressed oils and natural isolates so the sweetness stays balanced and never cloying.",
        "meta_secondary": "58 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Layered for dimension",
                "body": "We balance tart fruits with creamy undertones and sparkling herbs so every burn reveals a new nuance.",
            },
            {
                "title": "Mood boosting by design",
                "body": "Tested to refresh open kitchens, brunch tables, and creative studios with a cheerful, lingering glow.",
            },
        ],
        "palette_intro": "Every fruity blend starts bright and finishes velvety for a balanced, craveable scent journey.",
        "palette": [
            {"title": "Top", "body": "Strawberry pulp, pink guava, passionfruit."},
            {"title": "Heart", "body": "Rosewater, hibiscus, peach nectar."},
            {"title": "Base", "body": "Vanilla bean, amber sugar, soft woods."},
            {"title": "Pair with", "body": "Chilled rosé, linen napkins, weekend playlists."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1467173572719-f14b9fb86e5f?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle surrounded by fresh berries",
                "kicker": "Sweet & bright",
                "title": "Explore fruity favs",
            },
            {
                "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with fruit-filled brunch spread",
                "kicker": "Brunch ready",
                "title": "Style an orchard table",
            },
        ],
        "products": [
            {
                "id": "sangria",
                "tag": "Signature",
                "name": "Sunset Sangria",
                "description": "Stone fruit nectar, ruby berry, and sparkling wine enliven golden hours.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle next to a pitcher of berry sangria",
            },
            {
                "id": "berryfield",
                "tag": "Bestseller",
                "name": "Berry Field Day",
                "description": "Wild strawberry, raspberry leaf, and whipped cream feel like picnic blankets.",
                "price": "42",
                "image": "https://images.unsplash.com/photo-1484980972926-edee96e0960d?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with bowls of mixed berries",
            },
            {
                "id": "peachtea",
                "tag": "Limited batch",
                "name": "Peach Tea Fizz",
                "description": "Sun-kissed peach, jasmine tea, and ginger spritz refresh afternoon breaks.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with iced peach tea and fruit",
            },
            {
                "id": "figjam",
                "tag": "Cult classic",
                "name": "Fig Jam Session",
                "description": "Mission fig, blackcurrant, and amber sugar anchor cozy conversations.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1505577058444-a3dab90d4253?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle styled with figs and cheese board",
            },
            {
                "id": "cassis",
                "tag": "Studio exclusive",
                "name": "Cassis Bloom",
                "description": "Blackcurrant bud, neroli, and soft musk strike a luscious balance.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with citrus and berries on marble",
            },
            {
                "id": "papaya",
                "tag": "Island edit",
                "name": "Papaya Daydream",
                "description": "Juicy papaya, coconut water, and gardenia transport you to tropical rooftops.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1524592099565-3ff1eb892a90?auto=format&fit=crop&w=900&q=80",
                "alt": "Hands slicing tropical fruit near a candle",
            },
        ],
        "bundle_heading": "Mix your own fruit bowl trio.",
        "bundle_copy": "Bundle any three fruity blends and enjoy 10% off—ideal for brunch hosts and housewarming surprises.",
        "best_sellers": ["sangria", "berryfield", "peachtea", "figjam", "cassis", "papaya"],
    },
    "gourmand": {
        "name": "Gourmand",
        "page_title": "Gourmand Fragrance Family – Celestial Candle Studio",
        "background": "#fbf5ef",
        "text_primary": "#2b1c15",
        "text_secondary": "#8a6752",
        "accent": "#c68a55",
        "accent_dark": "#a96f3a",
        "border": "#efd8c6",
        "overlay_rgba": "rgba(150, 94, 50, 0.45)",
        "feature_bg": "rgba(251, 245, 239, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1432139509613-5c4255815697?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(124, 73, 37, 0.82) 20%, rgba(124, 73, 37, 0.5) 48%, rgba(124, 73, 37, 0.2))",
        "hero_kicker": "Gourmand fragrance family",
        "hero_heading": "Decadent treats baked into slow-burning rituals.",
        "hero_copy": "Think buttery pastries, toasted spices, and creamy accords that make every evening feel like dessert at a favorite café.",
        "description_intro": "We blend Madagascan vanilla, caramelized sugars, and roasted beans with modern musks to keep each gourmand candle inviting and never heavy.",
        "description_detail": "Crafted with FSC-certified wooden wicks for a comforting crackle, plus recyclable glass vessels ready for a second life as latte cups.",
        "meta_secondary": "55 hours · 12 oz vessels",
        "highlight_blocks": [
            {
                "title": "Comfort without cloying",
                "body": "Balanced with salt, smoke, or citrus partners so the sweetness stays sophisticated from first burn to last.",
            },
            {
                "title": "Cafe-worthy ambiance",
                "body": "Perfect for dinner parties, reading nooks, and kitchen hangs—pair with vinyl jazz and a chilled dessert wine.",
            },
        ],
        "palette_intro": "Each gourmand blend layers toasted spices, creamy notes, and subtle woods for depth.",
        "palette": [
            {"title": "Top", "body": "Salted caramel, orange zest, fresh espresso."},
            {"title": "Heart", "body": "Warm milk, praline crumble, cardamom."},
            {"title": "Base", "body": "Madagascan vanilla, tonka bean, smoked cedar."},
            {"title": "Pair with", "body": "Ceramic mugs, linen aprons, late-night recipe swaps."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1517686469429-8bdb88b9f907?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle near baked pastries and coffee",
                "kicker": "Sweet comforts",
                "title": "Shop gourmand favorites",
            },
            {
                "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=900&q=80",
                "alt": "Cozy table with dessert and candlelight",
                "kicker": "After-dinner glow",
                "title": "Set the dessert mood",
            },
        ],
        "products": [
            {
                "id": "vanilla",
                "tag": "Signature",
                "name": "Vanilla Bean Cloud",
                "description": "Whipped vanilla, almond milk, and musk swirl into a cashmere-soft haze.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1514278033931-52abc1ab8179?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside vanilla pods and cream",
            },
            {
                "id": "latte",
                "tag": "Bestseller",
                "name": "Salted Caramel Latte",
                "description": "Espresso crema, burnt sugar, and flaky sea salt warm bustling kitchens.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1481391319762-47dff72954d1?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle near coffee mug and caramel drizzle",
            },
            {
                "id": "sugarspice",
                "tag": "Limited batch",
                "name": "Sugar & Spice Tarte",
                "description": "Cinnamon pastry, poached pear, and vanilla bean invite dessert-first nights.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1517089596392-fb9a9033e05c?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside pear tart and spices",
            },
            {
                "id": "cocoa",
                "tag": "Winter edit",
                "name": "Cocoa Hearth",
                "description": "Dark cocoa, marshmallow fluff, and smoked cedar stay cozy fireside.",
                "price": "42",
                "image": "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with mug of hot chocolate",
            },
            {
                "id": "pistachio",
                "tag": "Studio exclusive",
                "name": "Pistachio Biscotti",
                "description": "Roasted pistachio, amaretto, and toasted coconut crunch into memory-making moments.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=900&q=80",
                "alt": "Biscotti stacked beside a candle",
            },
            {
                "id": "maple",
                "tag": "Cozy classic",
                "name": "Maple Cabin",
                "description": "Maple sap, pine smoke, and bourbon vanilla glow like cabin weekends.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=900&q=80",
                "alt": "Rustic candle with maple syrup pitcher",
            },
        ],
        "bundle_heading": "Create a dessert course trio.",
        "bundle_copy": "Pick any three gourmand candles to curate an indulgent tasting flight—save 10% and savor the afterglow.",
        "best_sellers": ["vanilla", "latte", "sugarspice", "cocoa", "pistachio", "maple"],
    },
    "green": {
        "name": "Green",
        "page_title": "Green Fragrance Family – Celestial Candle Studio",
        "background": "#f3f8f4",
        "text_primary": "#1f231e",
        "text_secondary": "#4f6a58",
        "accent": "#7abf96",
        "accent_dark": "#5fa67b",
        "border": "#d0e8d9",
        "overlay_rgba": "rgba(91, 150, 117, 0.45)",
        "feature_bg": "rgba(243, 248, 244, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(72, 122, 94, 0.82) 20%, rgba(72, 122, 94, 0.5) 48%, rgba(72, 122, 94, 0.2))",
        "hero_kicker": "Green fragrance family",
        "hero_heading": "Botanical calm inspired by fresh cut stems.",
        "hero_copy": "Earthy herbs, leafy greens, and forest air mingle for grounded scents that clear the mind and reset the room.",
        "description_intro": "We distill crushed stems, dewy leaves, and moss-covered trails into slow-burning blends that feel like barefoot walks through hidden gardens.",
        "description_detail": "Each pour is fortified with responsible palm alternatives and plant-based dyes so the experience stays pure from wax to wick.",
        "meta_secondary": "62 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Spa-level serenity",
                "body": "Layered galbanum, basil, and vetiver help calm busy spaces—ideal for home offices, yoga corners, or mindful mornings.",
            },
            {
                "title": "Nature-forward sourcing",
                "body": "We partner with regenerative farms and distillers for ingredients that tread lightly on the planet.",
            },
        ],
        "palette_intro": "Each green blend balances fresh-cut brightness with earthy roots for a meditative finish.",
        "palette": [
            {"title": "Top", "body": "Crushed basil, lime leaf, eucalyptus."},
            {"title": "Heart", "body": "Fig leaf, fern, geranium."},
            {"title": "Base", "body": "Vetiver, moss, cedar sap."},
            {"title": "Pair with", "body": "Matte ceramics, botanical prints, grounding playlists."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=80",
                "alt": "Green candle among thriving houseplants",
                "kicker": "Verdant vibes",
                "title": "Shop green favorites",
            },
            {
                "img": "https://images.unsplash.com/photo-1477244075012-5cc28286e465?auto=format&fit=crop&w=900&q=80",
                "alt": "Misty forest pathway",
                "kicker": "Forest bathing",
                "title": "Bring the outdoors in",
            },
        ],
        "products": [
            {
                "id": "fern",
                "tag": "Signature",
                "name": "Fern Canopy",
                "description": "Fern fronds, damp soil, and lemongrass revive city apartments.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle nestled with lush ferns",
            },
            {
                "id": "basil",
                "tag": "Kitchen favorite",
                "name": "Basil Verdure",
                "description": "Crushed basil, lime peel, and spearmint keep counters fresh and focused.",
                "price": "41",
                "image": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside fresh herbs on cutting board",
            },
            {
                "id": "moss",
                "tag": "Bestseller",
                "name": "Moss & Meadow",
                "description": "Green moss, neroli leaf, and meadow grass make grounding afternoons.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with botanical notebooks and moss",
            },
            {
                "id": "sage",
                "tag": "Limited batch",
                "name": "Silver Sage",
                "description": "Clary sage, juniper berry, and frankincense clarify late-night brainstorming sessions.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1505576399279-565b52d4ac77?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with bundles of sage and greenery",
            },
            {
                "id": "terrarium",
                "tag": "Studio exclusive",
                "name": "Glasshouse Terrarium",
                "description": "Fig leaf, ivy, and damp cedar recall greenhouse retreats.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1485637701894-09ad422f6de6?auto=format&fit=crop&w=900&q=80",
                "alt": "Hands tending terrarium next to candle",
            },
            {
                "id": "cedar",
                "tag": "Outdoor edit",
                "name": "Cedar Trail",
                "description": "Cedarwood, pine sap, and oakmoss echo mountain hikes.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle on mossy log in forest",
            },
        ],
        "bundle_heading": "Curate a mindful greenery trio.",
        "bundle_copy": "Pick your favorite three green candles and receive 10% off—perfect for serene studios and plant-filled spaces.",
        "best_sellers": ["fern", "basil", "moss", "sage", "terrarium", "cedar"],
    },
    "spice": {
        "name": "Spice",
        "page_title": "Spice Fragrance Family – Celestial Candle Studio",
        "background": "#fbf3eb",
        "text_primary": "#2b1b12",
        "text_secondary": "#764b3a",
        "accent": "#d0894a",
        "accent_dark": "#b5702f",
        "border": "#f0d5c1",
        "overlay_rgba": "rgba(161, 93, 52, 0.45)",
        "feature_bg": "rgba(251, 243, 235, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1505575967455-40e256f73376?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(124, 65, 32, 0.82) 20%, rgba(124, 65, 32, 0.5) 46%, rgba(124, 65, 32, 0.2))",
        "hero_kicker": "Spice fragrance family",
        "hero_heading": "Smoldering spices that warm every corner.",
        "hero_copy": "Cardamom, clove, and smoked resins mingle for blends that feel like alpine lodges and candlelit dinner parties.",
        "description_intro": "Hand-toasted spices and charred woods create an enveloping warmth without heavy sweetness.",
        "description_detail": "We infuse every pour with slow-burning wicks and recycled glass to keep your rituals grounded and sustainable.",
        "meta_secondary": "58 hours · 12 oz vessels",
        "highlight_blocks": [
            {
                "title": "Layered heat",
                "body": "From chai spices to amber embers, each profile is blended with citrus or herbs so the glow stays refined.",
            },
            {
                "title": "Entertaining ready",
                "body": "Ideal for holiday gatherings, fireside chats, and slow, savory suppers.",
            },
        ],
        "palette_intro": "Every spice blend leads with warmth, balances with brightness, and rests on smoky woods.",
        "palette": [
            {"title": "Top", "body": "Blood orange, pink pepper, black tea."},
            {"title": "Heart", "body": "Cardamom, cinnamon leaf, saffron."},
            {"title": "Base", "body": "Smoked cedar, myrrh, patchouli."},
            {"title": "Pair with", "body": "Copper mugs, knit throws, vinyl jazz records."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1527766833261-b09c3163a791?auto=format&fit=crop&w=900&q=80",
                "alt": "Spice candle alongside whole spices",
                "kicker": "Seasonal glow",
                "title": "Shop spiced favorites",
            },
            {
                "img": "https://images.unsplash.com/photo-1518459031867-a89b944bffe4?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with warm spices on tray",
                "kicker": "Cozy nights",
                "title": "Set the table in amber light",
            },
        ],
        "products": [
            {
                "id": "chai",
                "tag": "Signature",
                "name": "Cardamom Chai",
                "description": "Sticky cardamom, smoked vanilla, and black tea swirl into a cafe glow.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle beside steaming chai and spices",
            },
            {
                "id": "ember",
                "tag": "Bestseller",
                "name": "Amber Ember",
                "description": "Amber resin, charred cedar, and star anise radiate fireside warmth.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?auto=format&fit=crop&w=900&q=80",
                "alt": "Glowing candle on rustic wood with smoke",
            },
            {
                "id": "mulled",
                "tag": "Limited batch",
                "name": "Mulled Velvet",
                "description": "Mulled wine, clove, and cassia bark make holiday gatherings linger.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1478145046317-39f10e56b5e9?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle near mulled wine and spices",
            },
            {
                "id": "embersmoke",
                "tag": "Night collection",
                "name": "Smoked Santal",
                "description": "Sandalwood embers, nutmeg, and ambered suede wrap rooms in depth.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1505575967455-40e256f73376?auto=format&fit=crop&w=900&q=80",
                "alt": "Santal candle with wood and spices",
            },
            {
                "id": "ginger",
                "tag": "Studio exclusive",
                "name": "Ginger Ember",
                "description": "Spicy ginger, brown sugar, and cedar smoke brighten cold mornings.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1485637701894-09ad422f6de6?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle surrounded by ginger and spices",
            },
            {
                "id": "noir",
                "tag": "After dark",
                "name": "Spice Noir",
                "description": "Black cardamom, incense, and leather linger late into the night.",
                "price": "48",
                "image": "https://images.unsplash.com/photo-1505576399279-565b52d4ac77?auto=format&fit=crop&w=900&q=80",
                "alt": "Moody candle with leather-bound books",
            },
        ],
        "bundle_heading": "Bundle a fireside trio.",
        "bundle_copy": "Choose any three spiced candles and save 10%—set the mood for long dinners and storytelling nights.",
        "best_sellers": ["chai", "ember", "mulled", "embersmoke", "ginger", "noir"],
    },
    "woody": {
        "name": "Woody",
        "page_title": "Woody Fragrance Family – Celestial Candle Studio",
        "background": "#f2ede8",
        "text_primary": "#241e18",
        "text_secondary": "#5e5148",
        "accent": "#b39b7b",
        "accent_dark": "#927d61",
        "border": "#e1d6c7",
        "overlay_rgba": "rgba(94, 81, 72, 0.48)",
        "feature_bg": "rgba(242, 237, 232, 0.92)",
        "hero_image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=1400&q=80",
        "hero_gradient": "linear-gradient(120deg, rgba(72, 58, 46, 0.82) 20%, rgba(72, 58, 46, 0.5) 48%, rgba(72, 58, 46, 0.2))",
        "hero_kicker": "Woody fragrance family",
        "hero_heading": "Smoky, grounded, and beautifully lived-in.",
        "hero_copy": "Layered woods, resin, and earthy accords create enveloping warmth reminiscent of forest cabins and well-worn leather chairs.",
        "description_intro": "We blend sandalwood, cedar, and patchouli with airy florals or citrus lifts so each woody profile stays nuanced and modern.",
        "description_detail": "Pouring in reclaimed glass keeps the look refined while our FSC-certified wicks ensure an even, steady burn.",
        "meta_secondary": "65 hours · 13 oz vessels",
        "highlight_blocks": [
            {
                "title": "Depth with clarity",
                "body": "We marry smoky undertones with bright top notes so the atmosphere feels plush—not heavy.",
            },
            {
                "title": "Layer-friendly",
                "body": "Pairs beautifully with our citrus or spice families for a custom signature throughout your home.",
            },
        ],
        "palette_intro": "Each woody blend grounds with resinous bases and lifts with cool air or herbal sparks.",
        "palette": [
            {"title": "Top", "body": "Bergamot peel, cypress needle, chilled air."},
            {"title": "Heart", "body": "Sandalwood, dried cedar, cashmere musk."},
            {"title": "Base", "body": "Patchouli, vetiver, smoked vanilla."},
            {"title": "Pair with", "body": "Stacked design books, record players, organic textiles."},
        ],
        "features": [
            {
                "img": "https://images.unsplash.com/photo-1528747008803-1f5c1cbd04c1?auto=format&fit=crop&w=900&q=80",
                "alt": "Dark woody candle on a coffee table",
                "kicker": "Collected calm",
                "title": "Shop woody icons",
            },
            {
                "img": "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=80",
                "alt": "Forest landscape with golden light",
                "kicker": "Wander outside",
                "title": "Bring the forest home",
            },
        ],
        "products": [
            {
                "id": "cedarwood",
                "tag": "Signature",
                "name": "Cedarwood Study",
                "description": "Aged cedar, leather-bound pages, and smoked vetiver warm late-night reading.",
                "price": "46",
                "image": "https://images.unsplash.com/photo-1505575967455-40e256f73376?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle on wooden desk with books",
            },
            {
                "id": "santal",
                "tag": "Bestseller",
                "name": "Santal Ember",
                "description": "Creamy sandalwood, papyrus, and ambrox invite sophisticated calm.",
                "price": "48",
                "image": "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=80",
                "alt": "Santal candle with forest backdrop",
            },
            {
                "id": "amberwood",
                "tag": "Limited batch",
                "name": "Amberwood Atlas",
                "description": "Smoked amber, labdanum, and atlas cedar linger like well-traveled trunks.",
                "price": "47",
                "image": "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle on mossy stump with sunlight",
            },
            {
                "id": "oakmoss",
                "tag": "Cult favorite",
                "name": "Oakmoss Reverie",
                "description": "Oakmoss, galbanum, and white patchouli create a grounded escape.",
                "price": "45",
                "image": "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=900&q=80",
                "alt": "Green moss and candle in woodland setting",
            },
            {
                "id": "ashwood",
                "tag": "Studio exclusive",
                "name": "Ashwood Loft",
                "description": "Charred cedar, birch tar, and black tea keep loft spaces moody yet airy.",
                "price": "44",
                "image": "https://images.unsplash.com/photo-1528747008803-1f5c1cbd04c1?auto=format&fit=crop&w=900&q=80",
                "alt": "Modern loft coffee table with candle",
            },
            {
                "id": "embertrail",
                "tag": "Après edit",
                "name": "Ember Trail",
                "description": "Smoked pine, incense, and balsam carry you to twilight hikes.",
                "price": "43",
                "image": "https://images.unsplash.com/photo-1505575967455-40e256f73376?auto=format&fit=crop&w=900&q=80",
                "alt": "Candle with wool blankets and pinecones",
            },
        ],
        "bundle_heading": "Assemble a cabin-ready trio.",
        "bundle_copy": "Bundle three woody candles for 10% off—ideal for reading corners, dens, or gifting your favorite host.",
        "best_sellers": ["cedarwood", "santal", "amberwood", "oakmoss", "ashwood", "embertrail"],
    },
}

for details in collections.values():
    if "page_title" in details:
        details["page_title"] = details["page_title"].replace("Celestial Candle Studio", "Sen's Candle Studio")

for slug, data in collections.items():
    # add derived fields where missing
    if "meta_secondary" not in data:
        data["meta_secondary"] = "60 hours · 13 oz vessels"

family_links = "\n".join(
    f'                        <li><a href="collection-{family}.html">{collections[family]["name"]}</a></li>'
    for family in family_order
)

template_text = Template("""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>$page_title</title>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&family=Cinzel+Decorative:wght@400;600&family=Great+Vibes&display=swap\" rel=\"stylesheet\">
    <style>
        :root {
            --background: $background;
            --surface: #ffffff;
            --text-primary: $text_primary;
            --text-secondary: $text_secondary;
            --accent: $accent;
            --accent-dark: $accent_dark;
            --border: $border;
            --nav-height: 72px;
        }
        *, *::before, *::after { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: 'Work Sans', 'Helvetica Neue', Arial, sans-serif;
            color: var(--text-primary);
            background: var(--background);
            line-height: 1.65;
            -webkit-font-smoothing: antialiased;
        }
        a { color: inherit; text-decoration: none; }
        img { max-width: 100%; display: block; }
        .sr-only {
            position: absolute;
            width: 1px; height: 1px;
            padding: 0; margin: -1px;
            overflow: hidden; clip: rect(0, 0, 0, 0);
            white-space: nowrap; border: 0;
        }
        .announcement {
            background: var(--text-primary);
            color: var(--surface);
            text-align: center;
            font-size: 0.85rem;
            letter-spacing: 0.08em;
            padding: 0.75rem 1rem;
        }
        header {
            background: var(--surface);
            position: sticky;
            top: 0;
            z-index: 20;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
        }
        nav {
            max-width: 1200px;
            margin: 0 auto;
            height: var(--nav-height);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
        }
        .brand {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.5rem;
            letter-spacing: 0.08em;
        }
        .brand-logo {
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 0.1rem;
            text-decoration: none;
            letter-spacing: normal;
            color: inherit;
            line-height: 1;
        }
        .brand-logo .brand-script {
            font-family: 'Great Vibes', 'Brush Script MT', cursive;
            font-size: 1.7rem;
            color: #bf2f24;
            letter-spacing: 0.08em;
        }
        .brand-logo .brand-block {
            font-family: 'Cinzel Decorative', 'Playfair Display', serif;
            text-transform: uppercase;
            letter-spacing: 0.35em;
            font-size: 0.8rem;
            color: #1f5d33;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .brand-logo .brand-block span + span {
            margin-top: -0.25rem;
        }
        .nav-links {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }
        .nav-link,
        .nav-links a {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.14em;
        }
        .nav-link {
            background: none;
            border: none;
            font: inherit;
            color: inherit;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0;
        }
        .menu-trigger::after {
            content: '\\25BE';
            font-size: 0.55rem;
            transform-origin: center;
            transition: transform 0.2s ease;
        }
        body.menu-open .menu-trigger::after { transform: rotate(-180deg); }
        .nav-link:hover,
        .nav-link:focus,
        .nav-links a:hover,
        .nav-links a:focus { color: var(--accent-dark); }
        .nav-cta {
            border: 1px solid var(--text-primary);
            padding: 0.5rem 1.2rem;
            border-radius: 999px;
            font-size: 0.85rem;
            transition: background 0.2s ease, color 0.2s ease;
        }
        .nav-cta:hover,
        .nav-cta:focus {
            background: var(--text-primary);
            color: var(--surface);
        }
        .menu-overlay[hidden],
        .mega-menu[hidden] { display: none; }
        .menu-overlay {
            position: fixed;
            inset: 0;
            background: $overlay_rgba;
            backdrop-filter: blur(3px);
            z-index: 30;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        .menu-overlay.is-active {
            opacity: 1;
            pointer-events: auto;
        }
        .mega-menu {
            position: fixed;
            top: clamp(72px, 12vh, 120px);
            left: 50%;
            transform: translate(-50%, -12px);
            max-width: min(1080px, calc(100% - 48px));
            background: var(--surface);
            border-radius: 28px;
            box-shadow: 0 28px 80px rgba(18, 16, 13, 0.24);
            border: 1px solid rgba(0, 0, 0, 0.08);
            z-index: 50;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        .mega-menu.is-active {
            opacity: 1;
            pointer-events: auto;
            transform: translate(-50%, 0);
        }
        .mega-menu__inner {
            padding: 44px 48px 40px;
            display: grid;
            gap: 32px;
        }
        .mega-menu__header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }
        .mega-menu__header h2 {
            margin: 0;
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.5rem;
            letter-spacing: 0.06em;
        }
        .mega-menu__close {
            border: none;
            background: rgba(0, 0, 0, 0.06);
            color: var(--text-primary);
            width: 42px;
            height: 42px;
            border-radius: 50%;
            font-size: 1.4rem;
            line-height: 1;
            cursor: pointer;
            transition: background 0.2s ease, transform 0.2s ease;
        }
        .mega-menu__close:hover,
        .mega-menu__close:focus {
            background: rgba(0, 0, 0, 0.12);
            transform: rotate(90deg);
        }
        .mega-menu__grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 32px;
        }
        .mega-menu__column h3 {
            margin: 0 0 1rem;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.24em;
            color: var(--text-secondary);
        }
        .mega-menu__column ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: grid;
            gap: 0.45rem;
        }
        .mega-menu__column a {
            font-size: 0.95rem;
            letter-spacing: 0.08em;
            color: var(--text-primary);
        }
        .mega-menu__column a:hover,
        .mega-menu__column a:focus { color: var(--accent-dark); }
        .mega-menu__feature { display: grid; gap: 18px; }
        .mega-menu__feature article {
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(0, 0, 0, 0.06);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.1);
        }
        .mega-menu__feature img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        .feature-copy {
            padding: 18px 22px 22px;
            background: $feature_bg;
        }
        .feature-kicker {
            margin: 0 0 0.35rem;
            font-size: 0.75rem;
            letter-spacing: 0.24em;
            text-transform: uppercase;
            color: var(--text-secondary);
        }
        .feature-copy h3 {
            margin: 0;
            font-size: 1.05rem;
            font-family: 'Playfair Display', Georgia, serif;
        }
        body.menu-open { overflow: hidden; }
        body.menu-open main,
        body.menu-open footer {
            filter: blur(10px);
            pointer-events: none;
        }
        main { padding: 0 24px 6rem; transition: filter 0.3s ease; }
        .section { max-width: 1200px; margin: 0 auto; }
        .collection-hero {
            margin: 48px auto 32px;
            border-radius: 28px;
            overflow: hidden;
            position: relative;
            min-height: 420px;
            display: grid;
            align-items: center;
            padding: 72px 64px;
            color: var(--surface);
        }
        .collection-hero::before {
            content: "";
            position: absolute;
            inset: 0;
            background: url('$hero_image') center/cover;
            transform: scale(1.05);
            z-index: 0;
        }
        .collection-hero::after {
            content: "";
            position: absolute;
            inset: 0;
            background: $hero_gradient;
            z-index: 0;
        }
        .collection-hero__content {
            position: relative;
            z-index: 1;
            max-width: 520px;
            display: grid;
            gap: 1.2rem;
        }
        .collection-hero__kicker {
            text-transform: uppercase;
            letter-spacing: 0.24em;
            font-size: 0.78rem;
        }
        .collection-hero h1 {
            margin: 0;
            font-size: clamp(2.6rem, 5vw, 3.6rem);
            font-family: 'Playfair Display', Georgia, serif;
            line-height: 1.05;
        }
        .collection-hero p { margin: 0; font-size: 1.05rem; }
        .collection-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            justify-content: space-between;
            align-items: center;
            background: var(--surface);
            border-radius: 16px;
            padding: 24px 32px;
            border: 1px solid var(--border);
        }
        .collection-meta__group {
            display: grid;
            gap: 0.3rem;
        }
        .collection-meta__group span {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.22em;
            color: var(--text-secondary);
        }
        .collection-meta__group strong {
            font-size: 1.2rem;
        }
        .collection-meta select {
            border: 1px solid var(--border);
            padding: 0.6rem 1rem;
            border-radius: 999px;
            font-size: 0.9rem;
            background: var(--background);
            color: var(--text-primary);
        }
        .collection-description {
            margin: 48px 0 32px;
            display: grid;
            gap: 1rem;
        }
        .collection-description p {
            color: var(--text-secondary);
            max-width: 760px;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 28px;
        }
        .product-card {
            background: var(--surface);
            border-radius: 18px;
            overflow: hidden;
            border: 1px solid rgba(0, 0, 0, 0.04);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
        }
        .product-card figure { position: relative; overflow: hidden; aspect-ratio: 3 / 4; }
        .product-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s ease;
        }
        .product-card:hover img { transform: scale(1.05); }
        .product-info {
            padding: 22px 24px 26px;
            display: grid;
            gap: 0.75rem;
        }
        .product-info span {
            font-size: 0.72rem;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--accent);
        }
        .product-info h2 {
            margin: 0;
            font-size: 1.25rem;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .product-info p { margin: 0; color: var(--text-secondary); }
        .product-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 0.5rem;
        }
        .price { font-weight: 600; letter-spacing: 0.12em; }
        .quick-add {
            border: none;
            background: var(--text-primary);
            color: var(--surface);
            padding: 0.55rem 1.4rem;
            border-radius: 999px;
            font-size: 0.82rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            cursor: pointer;
            transition: transform 0.2s ease, background 0.2s ease;
        }
        .quick-add:hover,
        .quick-add:focus {
            transform: translateY(-2px);
            background: var(--accent-dark);
        }
        .collection-highlights {
            margin: 72px 0 32px;
            background: var(--surface);
            border-radius: 24px;
            padding: 48px 56px;
            border: 1px solid var(--border);
            display: grid;
            gap: 2rem;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        }
        .collection-highlights h3 {
            margin: 0 0 0.75rem;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .collection-highlights p { margin: 0; color: var(--text-secondary); }
        .scent-palette {
            display: grid;
            gap: 24px;
            margin: 72px 0;
        }
        .scent-palette__grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        .scent-chip {
            padding: 20px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid var(--border);
        }
        .scent-chip h4 {
            margin: 0 0 0.5rem;
            font-size: 1rem;
        }
        .scent-chip p {
            margin: 0;
            color: var(--text-secondary);
        }
        .bundle-cta {
            margin: 96px auto 0;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.45), rgba(0, 0, 0, 0.05));
            border-radius: 28px;
            padding: 56px 64px;
            display: grid;
            gap: 1rem;
            text-align: center;
        }
        .bundle-cta h2 {
            margin: 0;
            font-size: 2.1rem;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .bundle-cta p {
            margin: 0;
            color: var(--text-secondary);
        }
        .bundle-cta a {
            justify-self: center;
            border: 1px solid var(--text-primary);
            border-radius: 999px;
            padding: 0.85rem 1.8rem;
            font-weight: 600;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            background: var(--text-primary);
            color: var(--surface);
            transition: transform 0.2s ease, background 0.2s ease;
        }
        .bundle-cta a:hover,
        .bundle-cta a:focus {
            transform: translateY(-2px);
            background: var(--accent-dark);
        }
        footer {
            background: var(--surface);
            padding: 72px 24px 40px;
            border-top: 1px solid var(--border);
            transition: filter 0.3s ease;
        }
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            gap: 48px;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        }
        .footer-brand h3 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.7rem;
            margin: 0 0 1rem;
        }
        .footer-links h4 {
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.22em;
            margin: 0 0 1rem;
        }
        .footer-links ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: grid;
            gap: 0.6rem;
        }
        .footer-links a { color: var(--text-secondary); font-size: 0.95rem; }
        .footer-bottom {
            margin-top: 48px;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-secondary);
        }
        @media (max-width: 900px) {
            nav {
                flex-direction: column;
                gap: 1rem;
                height: auto;
                padding: 16px 24px 24px;
            }
            .collection-hero { padding: 64px 36px; }
            .collection-meta { padding: 24px; }
            .collection-highlights { padding: 36px; }
            .scent-palette__grid { grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); }
            .mega-menu { top: clamp(64px, 10vh, 96px); }
            .mega-menu__inner { padding: 36px; }
            .mega-menu__grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
        }
        @media (max-width: 640px) {
            main { padding: 0 18px 4rem; }
            .announcement { font-size: 0.75rem; }
            .collection-hero { margin: 32px auto; padding: 56px 24px; }
            .collection-meta { gap: 1rem; }
            .collection-highlights { padding: 28px; }
            .bundle-cta { padding: 48px 28px; }
            .mega-menu__inner { padding: 32px 24px; }
            .mega-menu__header { flex-direction: column; align-items: flex-start; }
            .mega-menu__close { align-self: flex-end; }
        }
    </style>
</head>
<body>
    <div class=\"announcement\">Complimentary carbon-neutral shipping on all candle bundles.</div>
    <header>
        <nav aria-label=\"Primary navigation\">
            <a class=\"brand brand-logo\" href=\"index.html\">\n+                <span class=\"brand-script\">Sen's</span>\n+                <span class=\"brand-block\">\n+                    <span>Candle</span>\n+                    <span>Studio</span>\n+                </span>\n+            </a>
            <div class=\"nav-links\">
                <button class=\"nav-link menu-trigger\" type=\"button\" aria-haspopup=\"dialog\" aria-expanded=\"false\" data-menu-open=\"scentMenu\">Shop by Scent</button>
                <a href=\"index.html#collection\">Candles</a>
                <a href=\"index.html#story\">Our Story</a>
                <a href=\"index.html#values\">Sustainability</a>
            </div>
        </nav>
    </header>
    <div class=\"menu-overlay\" data-menu-overlay hidden></div>
    <aside class=\"mega-menu\" id=\"scentMenu\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"scentMenuTitle\" tabindex=\"-1\" hidden>
        <div class=\"mega-menu__inner\">
            <div class=\"mega-menu__header\">
                <h2 id=\"scentMenuTitle\">Shop by scent universe</h2>
                <button class=\"mega-menu__close\" type=\"button\" data-menu-close aria-label=\"Close menu\">&times;</button>
            </div>
            <div class=\"mega-menu__grid\">
                <div class=\"mega-menu__column\">
                    <h3>Shop by scent family</h3>
                    <ul>
$family_links
                    </ul>
                </div>
                <div class=\"mega-menu__column\">
                    <h3>Shop bestselling fragrances</h3>
                    <ul>
$bestseller_links
                    </ul>
                </div>
                <div class=\"mega-menu__feature\">
$feature_cards
                </div>
            </div>
        </div>
    </aside>
    <main>
        <section class=\"collection-hero section\" aria-labelledby=\"hero-title\">
            <div class=\"collection-hero__content\">
                <p class=\"collection-hero__kicker\">$hero_kicker</p>
                <h1 id=\"hero-title\">$hero_heading</h1>
                <p>$hero_copy</p>
            </div>
        </section>
        <section class=\"collection-meta section\" aria-label=\"Collection details\">
            <div class=\"collection-meta__group\">
                <span>Total fragrances</span>
                <strong><span data-product-count>0</span> candles</strong>
            </div>
            <div class=\"collection-meta__group\">
                <span>Burn time</span>
                <strong>$meta_secondary</strong>
            </div>
            <label>
                <span class=\"sr-only\">Sort $collection_lower candles</span>
                <select aria-label=\"Sort $collection_lower candles\">
                    <option>Sort: Featured</option>
                    <option>Sort: Newest</option>
                    <option>Sort: Price (High to Low)</option>
                    <option>Sort: Price (Low to High)</option>
                </select>
            </label>
        </section>
        <section class=\"collection-description section\">
            <p>$description_intro</p>
            <p>$description_detail</p>
        </section>
        <section class=\"section\" aria-label=\"$collection_name candles\">
            <div class=\"product-grid\">
$product_cards
            </div>
        </section>
        <section class=\"collection-highlights section\">
$highlight_blocks
        </section>
        <section class=\"scent-palette section\" aria-label=\"$collection_name scent notes\">
            <div>
                <h2>Palette notes</h2>
                <p>$palette_intro</p>
            </div>
            <div class=\"scent-palette__grid\">
$palette_chips
            </div>
        </section>
        <section class=\"bundle-cta section\">
            <h2>$bundle_heading</h2>
            <p>$bundle_copy</p>
            <a href=\"index.html#collection\">Create a bundle</a>
        </section>
    </main>
    <footer>
        <div class=\"footer-content\">
            <div class=\"footer-brand\">
                <h3>Sen's Candle Studio</h3>
                <p>Hand-poured in Brooklyn using clean ingredients and planet-friendly packaging. Crafted to transport you—wherever you are.</p>
            </div>
            <div class=\"footer-links\">
                <h4>Explore</h4>
                <ul>
                    <li><a href=\"index.html#collection\">Shop Candles</a></li>
                    <li><a href=\"index.html#story\">Our Story</a></li>
                    <li><a href=\"index.html#values\">Sustainability</a></li>
                    <li><a href=\"index.html#journal\">Journal</a></li>
                </ul>
            </div>
            <div class=\"footer-links\">
                <h4>Support</h4>
                <ul>
                    <li><a href=\"#\">Shipping &amp; Returns</a></li>
                    <li><a href=\"#\">Wholesale</a></li>
                    <li><a href=\"#\">Gift Cards</a></li>
                    <li><a href=\"#\">Contact</a></li>
                </ul>
            </div>
            <div class=\"footer-links\">
                <h4>Follow</h4>
                <ul>
                    <li><a href=\"#\">Instagram</a></li>
                    <li><a href=\"#\">Pinterest</a></li>
                    <li><a href=\"#\">Spotify</a></li>
                    <li><a href=\"#\">TikTok</a></li>
                </ul>
            </div>
        </div>
        <div class=\"footer-bottom\">
            <span>&copy; <span id=\"year\"></span> Sen's Candle Studio. All rights reserved.</span>
            <span>Crafted in Brooklyn, NY</span>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const productCountTarget = document.querySelector('[data-product-count]');
            if (productCountTarget) {
                const products = document.querySelectorAll('.product-card');
                productCountTarget.textContent = products.length;
            }
            const year = document.getElementById('year');
            if (year) {
                year.textContent = new Date().getFullYear();
            }
            const overlay = document.querySelector('[data-menu-overlay]');
            const menuTriggers = document.querySelectorAll('[data-menu-open]');
            const closeButtons = document.querySelectorAll('[data-menu-close]');
            let activeMenu = null;
            let activeTrigger = null;
            let closeTimer = null;
            const focusableSelector = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
            function closeMenu() {
                if (!activeMenu) {
                    return;
                }
                if (closeTimer) {
                    clearTimeout(closeTimer);
                    closeTimer = null;
                }
                const menuToHide = activeMenu;
                const triggerToRefocus = activeTrigger;
                overlay?.classList.remove('is-active');
                menuToHide.classList.remove('is-active');
                document.body.classList.remove('menu-open');
                triggerToRefocus?.setAttribute('aria-expanded', 'false');
                activeMenu = null;
                activeTrigger = null;
                closeTimer = window.setTimeout(function () {
                    menuToHide.setAttribute('hidden', '');
                    if (!document.body.classList.contains('menu-open')) {
                        overlay?.setAttribute('hidden', '');
                    }
                    triggerToRefocus?.focus();
                    closeTimer = null;
                }, 300);
            }
            function openMenu(trigger, menu) {
                if (closeTimer) {
                    clearTimeout(closeTimer);
                    closeTimer = null;
                }
                if (activeMenu && activeMenu !== menu) {
                    closeMenu();
                }
                if (menu.hasAttribute('hidden')) {
                    menu.removeAttribute('hidden');
                }
                if (overlay?.hasAttribute('hidden')) {
                    overlay.removeAttribute('hidden');
                }
                requestAnimationFrame(function () {
                    overlay?.classList.add('is-active');
                    menu.classList.add('is-active');
                    document.body.classList.add('menu-open');
                });
                trigger.setAttribute('aria-expanded', 'true');
                activeMenu = menu;
                activeTrigger = trigger;
                const focusTarget = menu.querySelector(focusableSelector);
                if (focusTarget) {
                    focusTarget.focus();
                } else {
                    menu.focus();
                }
            }
            menuTriggers.forEach(function (trigger) {
                trigger.addEventListener('click', function () {
                    const targetId = trigger.getAttribute('data-menu-open');
                    if (!targetId) {
                        return;
                    }
                    const menu = document.getElementById(targetId);
                    if (!menu || !overlay) {
                        return;
                    }
                    if (menu === activeMenu) {
                        closeMenu();
                    } else {
                        openMenu(trigger, menu);
                    }
                });
            });
            overlay?.addEventListener('click', closeMenu);
            closeButtons.forEach(function (button) {
                button.addEventListener('click', closeMenu);
            });
            document.addEventListener('keydown', function (event) {
                if (event.key === 'Escape') {
                    closeMenu();
                }
            });
        });
    </script>
</body>
</html>
""")

for slug in family_order:
    data = collections[slug]
    product_lookup = {p["id"]: p["name"] for p in data["products"]}
    bestseller_links = "\n".join(
        f'                        <li><a href="collection-{slug}.html#{pid}">{product_lookup[pid]}</a></li>'
        for pid in data["best_sellers"]
    )
    feature_cards = "\n".join(
        "                    <article>\n"
        f"                        <img src=\"{feature['img']}\" alt=\"{feature['alt']}\">\n"
        "                        <div class=\"feature-copy\">\n"
        f"                            <p class=\"feature-kicker\">{feature['kicker']}</p>\n"
        f"                            <h3>{feature['title']}</h3>\n"
        "                        </div>\n"
        "                    </article>"
        for feature in data["features"]
    )
    product_cards = []
    for product in data["products"]:
        card = (
            f"                <article class=\"product-card\" id=\"{product['id']}\">\n"
            "                    <figure>\n"
            f"                        <img src=\"{product['image']}\" alt=\"{product['alt']}\" loading=\"lazy\">\n"
            "                    </figure>\n"
            "                    <div class=\"product-info\">\n"
            f"                        <span>{product['tag']}</span>\n"
            f"                        <h2>{product['name']}</h2>\n"
            f"                        <p>{product['description']}</p>\n"
            "                        <div class=\"product-meta\">\n"
            f"                            <span class=\"price\">${product['price']}</span>\n"
            "                            <button class=\"quick-add\" type=\"button\">Add to cart</button>\n"
            "                        </div>\n"
            "                    </div>\n"
            "                </article>"
        )
        product_cards.append(card)
    product_cards = "\n".join(product_cards)
    highlight_blocks = "\n".join(
        "            <div>\n"
        f"                <h3>{block['title']}</h3>\n"
        f"                <p>{block['body']}</p>\n"
        "            </div>"
        for block in data["highlight_blocks"]
    )
    palette_chips = "\n".join(
        "                <div class=\"scent-chip\">\n"
        f"                    <h4>{chip['title']}</h4>\n"
        f"                    <p>{chip['body']}</p>\n"
        "                </div>"
        for chip in data["palette"]
    )
    html = template_text.substitute(
        page_title=data["page_title"],
        background=data["background"],
        text_primary=data["text_primary"],
        text_secondary=data["text_secondary"],
        accent=data["accent"],
        accent_dark=data["accent_dark"],
        border=data["border"],
        overlay_rgba=data["overlay_rgba"],
        feature_bg=data["feature_bg"],
        hero_image=data["hero_image"],
        hero_gradient=data["hero_gradient"],
        hero_kicker=data["hero_kicker"],
        hero_heading=data["hero_heading"],
        hero_copy=data["hero_copy"],
        meta_secondary=data["meta_secondary"],
        description_intro=data["description_intro"],
        description_detail=data["description_detail"],
        collection_lower=data["name"].lower(),
        collection_name=data["name"],
        family_links=family_links,
        bestseller_links=bestseller_links,
        feature_cards=feature_cards,
        product_cards=product_cards,
        highlight_blocks=highlight_blocks,
        palette_intro=data["palette_intro"],
        palette_chips=palette_chips,
        bundle_heading=data["bundle_heading"],
        bundle_copy=data["bundle_copy"],
    )
    Path(f"collection-{slug}.html").write_text(html, encoding="utf-8")

print("Generated collection pages:", ", ".join(f"collection-{slug}.html" for slug in family_order))
