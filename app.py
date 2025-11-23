# app.py
import streamlit as st
import random
import textwrap
from datetime import datetime

# --- Optional: OpenAI only if user added key in Streamlit Secrets ---
try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

# ---------------------------
# Seite konfigurieren & CSS
# ---------------------------
st.set_page_config(page_title="Modeberater – Magazin", layout="wide", initial_sidebar_state="expanded")

# Styles: Magazin-like, schöne Typo und Karten
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body { background:#faf7f5; color: #111; font-family: 'Inter', sans-serif; }
        h1, h2, h3 { font-family: 'Playfair Display', serif; }
        .hero { background: linear-gradient(135deg, #fff 0%, #f3e9e6 100%); border-radius:12px; padding:22px; margin-bottom:18px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
        .card { background: white; border-radius:12px; padding:16px; box-shadow: 0 8px 24px rgba(15,15,15,0.06); }
        .muted { color: #666; }
        .swatch { width:28px; height:28px; display:inline-block; border-radius:6px; border:1px solid #ddd; margin-right:8px; vertical-align:middle; }
        .big-title { font-size:36px; margin:0; }
        .accent { color:#b84a62; }
        .filters-header { font-weight:600; margin-bottom:6px; }
        .tag { background:#f2f0ef; padding:6px 10px; border-radius:999px; margin-right:6px; display:inline-block; color:#333; }
        .outfit-item { font-weight:600; margin-bottom:6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Datenquellen / Inventar
# ---------------------------
# (Erweitere beliebig; für "Note 6" kannst du noch hunderte Items hinzufügen)
GENDERS = ["Damen", "Herren", "Unisex / Divers"]
SEASONS = ["Frühling", "Sommer", "Herbst", "Winter"]
OCCASIONS = ["Alltag", "Schule", "Arbeit", "Date", "Party", "Hochzeit", "Festival", "Sport", "Reisen", "Interview", "Fotoshooting"]
WEATHERS = ["Sonnig", "Regnerisch", "Windig", "Schnee", "Bewölkt"]
TEMPS_LABEL = "Aktuelle Temperatur (°C)"

STYLES = ["Casual", "Chic", "Sportlich", "Business", "Vintage", "Streetwear", "Minimalistisch", "Boho", "Elegant", "Kreativ"]
MATERIALS = ["Baumwolle", "Wolle", "Denim", "Leder", "Seide", "Leinen", "Kunstfaser", "Kaschmir"]
PATTERNS = ["Einfarbig", "Gestreift", "Karriert", "Geblümt", "Animal Print", "Polka Dots"]
BUDGETS = ["Günstig (<50€)", "Mittel (50–150€)", "Premium (>150€)"]
BODY_TYPES = ["Schlank", "Athletisch", "Kurvig", "Groß", "Klein", "Standard"]

SHOE_TYPES = ["Sneaker", "Boots", "Loafers", "Sandalen", "Pumps", "Wanderschuhe"]
ACCESSORIES = ["Hut", "Schal", "Tasche", "Gürtel", "Uhr", "Sonnenbrille", "Schmuck"]

# Große Farbpalette (Noch mehr Farben kannst du hier ergänzen)
COLOR_PALETTE = {
    "Schwarz": "#000000", "Weiß": "#FFFFFF", "Asphalt": "#2E2E2E", "Anthrazit": "#3B3B3B",
    "Grau": "#808080", "Beige": "#F5F5DC", "Sand": "#EEDFCC",
    "Rot": "#FF0000", "Dunkelrot": "#8B0000", "Bordeaux": "#6B0F1A",
    "Orange": "#FF8C42", "Koralle": "#FF7F50", "Pfirsich": "#FFDAB9",
    "Gelb": "#FFD400", "Ocker": "#CC7722",
    "Grün": "#00A86B", "Oliv": "#808000", "Mint": "#98FF98",
    "Türkis": "#2BC4B6", "Aqua": "#00CED1",
    "Blau": "#0F52BA", "Marineblau": "#000080", "Himmelblau": "#87CEEB",
    "Lila": "#800080", "Violett": "#8A2BE2", "Lavendel": "#E6E6FA",
    "Rosa": "#FFC0CB", "Altrosa": "#D78FAF",
    "Braun": "#8B4513", "Kaffee": "#4B2E2A",
    "Gold": "#FFD700", "Silber": "#C0C0C0"
}

# Basis-Inventar (kann stark erweitert werden; hier sensible Beispiele)
TOPS = ["T-Shirt", "Hemd", "Bluse", "Pullover", "Cardigan", "Blazer", "Crop-Top", "Tanktop"]
BOTTOMS = ["Jeans", "Stoffhose", "Chino", "Rock", "Shorts", "Leggings"]
OUTER = ["Bomberjacke", "Mantel", "Regenjacke", "Lederjacke", "Trenchcoat", "Daunenjacke"]
DRESSES = ["Sommerkleid", "Maxikleid", "Etuikleid"]
SHOES = SHOE_TYPES
BAGS = ["Crossbody", "Tote", "Clutch", "Rucksack"]

# ---------------------------
# Sidebar: Filter UI
# ---------------------------
with st.sidebar:
    st.markdown("<div class='filters-header'>Filter</div>", unsafe_allow_html=True)

    # optional filters toggles
    st.sidebar.caption("Wähle Filter (optional). Lass Felder leer = offen für Vorschläge.")
    sel_gender = st.selectbox("Geschlecht", options=["(egal)"] + GENDERS)
    sel_season = st.selectbox("Saison", options=["(egal)"] + SEASONS)
    sel_occ = st.multiselect("Anlass(e)", options=OCCASIONS, default=[])
    sel_weather = st.selectbox("Wetter", options=["(egal)"] + WEATHERS)
    sel_temp = st.slider(TEMPS_LABEL, -20, 40, 18)

    sel_styles = st.multiselect("Stilrichtungen", options=STYLES, default=[])
    sel_materials = st.multiselect("Materialien", options=MATERIALS, default=[])
    sel_patterns = st.multiselect("Muster", options=PATTERNS, default=[])
    sel_budget = st.selectbox("Budget", options=["(egal)"] + BUDGETS)

    sel_body = st.selectbox("Körperform (optional)", options=["(egal)"] + BODY_TYPES)
    sel_shoes = st.multiselect("Schuharten (optional)", options=SHOE_TYPES, default=[])
    sel_accessories = st.multiselect("Accessoires (optional)", options=ACCESSORIES, default=[])

    # Marken & Extras
    sel_brands = st.multiselect("Marken (optional)", options=["Zara","H&M","Nike","Adidas","Uniqlo","Gucci","Prada"], default=[])

    st.markdown("---")
    st.markdown("**Farbpalette** (klicke die Farben an):")

    # Color swatch grid with checkboxes (sidebar)
    color_keys = list(COLOR_PALETTE.keys())
    selected_colors = []
    # Display in rows of 4
    cols_per_row = 4
    for i in range(0, len(color_keys), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, key in enumerate(color_keys[i:i+cols_per_row]):
            with cols[j]:
                # show color patch and checkbox
                st.markdown(f"<div style='display:flex;align-items:center;gap:6px;'>"
                            f"<div class='swatch' style='background:{COLOR_PALETTE[key]};'></div>"
                            f"<div style='font-size:12px'>{key}</div></div>", unsafe_allow_html=True)
                checked = st.checkbox("", key=f"color_{key}")
    # Collect selections from session state
    for k in color_keys:
        if st.session_state.get(f"color_{k}", False):
            selected_colors.append(k)

    st.markdown("---")
    st.markdown("### KI-Option")
    use_ai = st.checkbox("Outfitbeschreibung mit ChatGPT generieren (API-Key nötig)", value=False)
    if use_ai:
        st.caption("Stelle sicher, dass du OPENAI_API_KEY in Streamlit Secrets gesetzt hast.")

    # small help
    st.markdown("---")
    st.write("Tipp: Lass Felder leer um vielfältige Vorschläge zu erhalten.")

# ---------------------------
# Helper: Local outfit generator
# ---------------------------
def local_generate_outfit(filters):
    # Simple rule-based generator that respects filters where possible
    # Build a pool of items filtered by season, material, budget, etc. (minimal example)
    pool_tops = TOPS.copy()
    pool_bottoms = BOTTOMS.copy()
    pool_outer = OUTER.copy()
    pool_dresses = DRESSES.copy()
    pool_shoes = SHOES.copy()
    pool_bags = BAGS.copy()

    # Season adjustments
    if filters['season'] == "Winter":
        pool_tops += ["Rollkragenpullover", "Strickpulli"]
        pool_outer += ["Daunenjacke", "Wollmantel"]
        pool_shoes += ["Stiefel"]
    elif filters['season'] == "Sommer":
        pool_tops += ["Leichtes Tanktop", "Leinenhemd"]
        pool_bottoms += ["Leichte Shorts", "Leinenhose"]
        pool_shoes += ["Sandalen"]
    elif filters['season'] == "Herbst":
        pool_outer += ["Trenchcoat", "Lederjacke"]
    elif filters['season'] == "Frühling":
        pool_tops += ["Leichter Cardigan"]
        pool_outer += ["Windjacke"]

    # Temperature adjustments
    if filters['temp'] <= 5:
        pool_tops = [t for t in pool_tops if "T-Shirt" not in t]
    if filters['temp'] >= 25:
        # more light choices
        pool_tops = [t for t in pool_tops if "Pullover" not in t and "Cardigan" not in t] + ["Sommerbluse"]

    # Material preference: push materials by adding items containing material keyword (simple)
    if filters['materials']:
        if "Leder" in filters['materials']:
            pool_outer.append("Lederjacke")

    # Style influence (simple mapping)
    if "Business" in filters['styles']:
        pool_tops += ["Businesshemd", "Blazer"]
        pool_bottoms += ["Anzughose", "Stoffhose"]
        pool_shoes += ["Loafers"]
    if "Sportlich" in filters['styles']:
        pool_tops += ["Sporttop", "Trainingsjacke"]
        pool_shoes += ["Sneaker"]

    # Build final outfit: either dress or top+bottom
    use_dress = False
    if filters['occasion'] and any(o in ["Party","Hochzeit","Date"] for o in filters['occasion']):
        # higher chance for dress if female or unisex
        if filters['gender'] in ["Damen", "Unisex / Divers"]:
            use_dress = random.random() < 0.5

    if use_dress and pool_dresses:
        dress = random.choice(pool_dresses)
        shoes = random.choice(pool_shoes)
        bag = random.choice(pool_bags)
        accessories = random.sample(ACCESSORIES, k=min(2, len(ACCESSORIES)))
        items = [dress, shoes, bag] + accessories
    else:
        top = random.choice(pool_tops)
        bottom = random.choice(pool_bottoms)
        outer = random.choice(pool_outer) if random.random() < 0.6 else None
        shoes = random.choice(pool_shoes)
        bag = random.choice(pool_bags) if random.random() < 0.7 else None
        accessories = random.sample(ACCESSORIES, k=min(2, len(ACCESSORIES)))
        items = [top, bottom] + ([outer] if outer else []) + [shoes] + ([bag] if bag else []) + accessories

    # color selection
    colors = filters['colors'] if filters['colors'] else random.sample(list(COLOR_PALETTE.keys()), k=2)

    # Prepare structured result
    result = {
        "items": items,
        "colors": colors,
        "info": {
            "gender": filters['gender'],
            "season": filters['season'],
            "occasion": filters['occasion'],
            "styles": filters['styles'],
            "materials": filters['materials'],
            "budget": filters['budget']
        }
    }
    return result

# ---------------------------
# Main: Collect filters into dict
# ---------------------------
filters = {
    "gender": sel_gender if sel_gender != "(egal)" else None,
    "season": sel_season if sel_season != "(egal)" else None,
    "occasion": sel_occ,
    "weather": sel_weather if sel_weather != "(egal)" else None,
    "temp": sel_temp,
    "styles": sel_styles,
    "materials": sel_materials,
    "patterns": sel_patterns,
    "budget": sel_budget if sel_budget != "(egal)" else None,
    "body": sel_body if sel_body != "(egal)" else None,
    "shoes": sel_shoes,
    "accessories": sel_accessories,
    "brands": sel_brands,
    "colors": selected_colors
}

# ---------------------------
# Generate: KI or local
# ---------------------------
st.markdown("<div class='hero card'><h1 class='big-title'><span class='accent'>Modeberater</span> — Dein persönliches Lookbook</h1>"
            "<p class='muted'>Interaktiver, AI-gestützter Outfit-Generator im Magazin-Stil. Filter links wählen und 'Outfit generieren' klicken.</p></div>",
            unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    if st.button("✨ Outfit generieren"):
        # If AI requested and key available, call OpenAI
        ai_ok = False
        if use_ai and OPENAI_AVAILABLE and st.secrets.get("OPENAI_API_KEY"):
            # configure OpenAI
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            ai_ok = True
        elif use_ai:
            st.warning("OpenAI API Key nicht gefunden in Streamlit Secrets. Die App nutzt stattdessen die lokale Generator-Logik.")
            ai_ok = False

        # local outfit first
        local = local_generate_outfit(filters)

        # If AI requested and available, ask AI to produce a beautiful description
        ai_description = None
        if ai_ok:
            prompt = textwrap.dedent(f"""
                Du bist ein Modeberater. Erstelle eine elegante, klare Outfit-Beschreibung für folgende Ausgangslage.
                Kriterien:
                Geschlecht: {filters['gender']}
                Saison: {filters['season']}
                Anlass: {', '.join(filters['occasion']) if filters['occasion'] else 'Beliebig'}
                Wetter: {filters['weather']}
                Temperatur: {filters['temp']}°C
                Stile: {', '.join(filters['styles']) if filters['styles'] else 'Beliebig'}
                Materialien: {', '.join(filters['materials']) if filters['materials'] else 'Beliebig'}
                Farben: {', '.join(local['colors'])}
                Kleidungsstücke: {', '.join(local['items'])}
                
                Beschreibe das Outfit in 2 Versionen:
                1) Kurze, prägnante Beschreibung für eine App (2–3 Sätze).
                2) Eine detaillierte Stil-Begründung (3–4 Punkte), warum diese Kombination gut wirkt.
                Gib das Ergebnis als klares JSON-ähnliches Format mit 'short' und 'detail' Feldern.
            """)
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=350,
                    temperature=0.8
                )
                ai_text = response['choices'][0]['message']['content'].strip()
                ai_description = ai_text
            except Exception as e:
                st.error("Fehler beim OpenAI-Aufruf: " + str(e))
                ai_description = None

        # Display outfit as magazine cards
        st.markdown("<div style='display:flex;gap:18px;flex-wrap:wrap'>", unsafe_allow_html=True)
        # Primary card
        items_html = "".join([f"<li>{it}</li>" for it in local['items']])
        colors_html = "".join([f"<span style='display:inline-block;margin-right:8px;'><div style='width:22px;height:22px;background:{COLOR_PALETTE[c]};border-radius:6px;border:1px solid #ddd;display:inline-block;vertical-align:middle;margin-right:6px;'></div><small>{c}</small></span>" for c in local['colors']])
        left_card = f"""
            <div class='card' style='width:65%;'>
                <h3 style='margin-bottom:6px;'>Look-Vorschlag</h3>
                <p class='muted'>Basierend auf deinen Filtern</p>
                <div style='margin-top:10px;'>
                    <p class='outfit-item'>Kleidungsstücke:</p>
                    <ul>{items_html}</ul>
                    <p class='outfit-item'>Farben:</p>
                    <div>{colors_html}</div>
                </div>
            </div>
        """
        st.markdown(left_card, unsafe_allow_html=True)

        # Right card: meta + accessories + brand + budget
        meta_html = f"""
            <div class='card' style='width:30%;'>
                <h4>Details</h4>
                <p class='muted'>Geschlecht: {local['info']['gender'] or 'Beliebig'}</p>
                <p class='muted'>Saison: {local['info']['season'] or 'Beliebig'}</p>
                <p class='muted'>Budget: {local['info']['budget'] or 'Beliebig'}</p>
                <hr/>
                <p class='muted'>Stil: {', '.join(local['info']['styles']) if local['info']['styles'] else 'Beliebig'}</p>
                <p class='muted'>Material: {local['info']['materials'] if local['info']['materials'] else 'Beliebig'}</p>
            </div>
        """
        st.markdown(meta_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # show AI text if present
        if ai_description:
            st.markdown("<div style='margin-top:14px;' class='card'>", unsafe_allow_html=True)
            st.markdown("### ✨ AI-Beschreibung")
            st.markdown(f"<pre style='white-space:pre-wrap'>{ai_description}</pre>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            # Local generated short textual suggestion
            st.markdown("<div style='margin-top:14px;' class='card'>", unsafe_allow_html=True)
            st.markdown("### ✨ Kurze Beschreibung")
            short = f"Ein stylishes Outfit mit {', '.join(local['colors'])}. Trage {local['items'][0]} kombiniert mit {local['items'][1]} und dazu {local['items'][2]}."
            st.write(short)
            st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Quick Tips")
    st.markdown("- Nutze mehrere Filter für präzisere Looks.")
    st.markdown("- Lasse Felder frei für abwechslungsreichere Vorschläge.")
    st.markdown("- Mit OpenAI aktiviert bekommst du eine kreative, natürliche Outfit-Beschreibung.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer / small print
st.markdown("<div style='margin-top:18px' class='muted'>Erstellt mit ❤️ für dein Medieninformatik-Projekt. Passe das Inventar in der Datei an, um mehr Looks zu generieren.</div>", unsafe_allow_html=True)
