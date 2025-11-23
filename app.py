import streamlit as st
import random

st.set_page_config(page_title="💃 Modeberater 2.0", layout="centered")
st.title("💎 Premium Modeberater")
st.write("Wähle deine Kriterien und ich schlage dir die besten Outfits vor!")

# --- Sidebar Filter ---
st.sidebar.header("Filter auswählen")

# Geschlecht
geschlecht = st.sidebar.radio("Geschlecht:", ["Männlich", "Weiblich", "Divers"])

# Saison
saison = st.sidebar.selectbox("Saison:", ["Frühling", "Sommer", "Herbst", "Winter"])

# Anlass / Occasion
anlass = st.sidebar.selectbox("Allgemeiner Anlass:", ["Alltag", "Arbeit", "Party", "Sportlich", "Elegant"])
occasion = st.sidebar.multiselect("Besondere Anlässe:", ["Hochzeit", "Geburtstag", "Festival", "Date", "Meeting", "Abschlussfeier"])

# Stil
stil = st.sidebar.multiselect("Stil:", ["Casual", "Business", "Elegant", "Sportlich", "Streetwear", "Boho"])

# Wetter & Temperatur
wetter = st.sidebar.selectbox("Wetter:", ["Sonnig", "Regnerisch", "Schnee", "Kalt", "Warm", "Windig"])
temperatur = st.sidebar.slider("Temperatur (°C):", -20, 40, 20)

# Farben mit Vorschau
farben_dict = {
    "Schwarz": "#000000", "Weiß": "#FFFFFF", "Rot": "#FF0000", "Blau": "#0000FF", "Grün": "#00FF00",
    "Gelb": "#FFFF00", "Orange": "#FFA500", "Lila": "#800080", "Rosa": "#FFC0CB", "Braun": "#A52A2A",
    "Grau": "#808080", "Beige": "#F5F5DC", "Türkis": "#40E0D0", "Dunkelblau": "#00008B", "Hellgrün": "#90EE90",
    "Bordeaux": "#800000", "Khaki": "#F0E68C", "Gold": "#FFD700", "Silber": "#C0C0C0", "Marineblau": "#000080",
    "Mint": "#98FF98", "Violett": "#EE82EE", "Pfirsich": "#FFDAB9", "Koralle": "#FF7F50", "Oliv": "#808000"
}
farben = st.sidebar.multiselect(
    "Farben:", options=list(farben_dict.keys()), default=["Schwarz", "Weiß"]
)

# Material & Muster
material = st.sidebar.multiselect("Material:", ["Baumwolle", "Leder", "Wolle", "Seide", "Denim", "Polyester", "Kaschmir"])
muster = st.sidebar.multiselect("Muster:", ["Einfarbig", "Gestreift", "Karriert", "Geblümt", "Animal Print", "Gemustert"])

# Budget
budget = st.sidebar.selectbox("Budget:", ["Günstig (<50€)", "Mittel (50-150€)", "Hoch (>150€)"])

# Schuhe & Accessoires
schuhe = st.sidebar.multiselect("Schuharten:", ["Sneaker", "Stiefel", "Sandalen", "Loafers", "High Heels"])
accessoires = st.sidebar.multiselect("Accessoires:", ["Hut", "Schal", "Tasche", "Gürtel", "Kette", "Ohrringe", "Armbanduhr"])

# Lieblingsmarken
marken = st.sidebar.multiselect("Lieblingsmarken:", ["Nike", "Adidas", "Zara", "H&M", "Gucci", "Prada", "Uniqlo"])

# --- Beispiel-Outfits Datenbank ---
outfits = [
    {"Geschlecht": "Männlich", "Saison": "Sommer", "Anlass": "Alltag", "Occasion": [], "Stil": "Casual",
     "Wetter": "Warm", "Temperatur": 25, "Material": "Baumwolle", "Muster": "Einfarbig",
     "Budget": "Günstig (<50€)", "Kleidungsstücke": ["T-Shirt", "Shorts", "Sneaker"]},
    {"Geschlecht": "Weiblich", "Saison": "Winter", "Anlass": "Arbeit", "Occasion": [], "Stil": "Elegant",
     "Wetter": "Kalt", "Temperatur": 0, "Material": "Wolle", "Muster": "Gestreift",
     "Budget": "Mittel (50-150€)", "Kleidungsstücke": ["Pullover", "Hose", "Mantel", "Stiefel"]},
    {"Geschlecht": "Divers", "Saison": "Herbst", "Anlass": "Party", "Occasion": ["Geburtstag"], "Stil": "Streetwear",
     "Wetter": "Kühl", "Temperatur": 15, "Material": "Denim", "Muster": "Karriert",
     "Budget": "Hoch (>150€)", "Kleidungsstücke": ["Hemd", "Jeans", "Jacke", "Sneaker"]},
    {"Geschlecht": "Weiblich", "Saison": "Frühling", "Anlass": "Alltag", "Occasion": [], "Stil": "Boho",
     "Wetter": "Sonnig", "Temperatur": 22, "Material": "Seide", "Muster": "Geblümt",
     "Budget": "Mittel (50-150€)", "Kleidungsstücke": ["Kleid", "Sandalen", "Sonnenhut"]},
]

# --- Filter-Funktion ---
def filter_outfits(outfits, geschlecht, saison, anlass, occasion, stil, wetter, temperatur, material, muster, budget):
    gefiltert = []
    for outfit in outfits:
        if (outfit["Geschlecht"] == geschlecht or geschlecht == "Divers") \
           and outfit["Saison"] == saison \
           and outfit["Anlass"] == anlass \
           and (not occasion or any(o in outfit["Occasion"] for o in occasion)) \
           and (not stil or outfit["Stil"] in stil) \
           and outfit["Wetter"] == wetter \
           and abs(outfit["Temperatur"] - temperatur) <= 5 \
           and (not material or outfit["Material"] in material) \
           and (not muster or outfit["Muster"] in muster) \
           and (not budget or outfit["Budget"] == budget):
            gefiltert.append(outfit)
    return gefiltert

# --- Filter anwenden ---
gefilterte_outfits = filter_outfits(outfits, geschlecht, saison, anlass, occasion, stil, wetter, temperatur, material, muster, budget)

# --- Outfit anzeigen ---
st.subheader("Dein Outfit:")
if gefilterte_outfits:
    outfit = random.choice(gefilterte_outfits)
    st.write(f"**Kleidungsstücke:** {', '.join(outfit['Kleidungsstücke'])}")
    
    if farben:
        st.write("**Farben:**")
        cols = st.columns(len(farben))
        for i, farbe in enumerate(farben):
            cols[i].markdown(
                f"<div style='background-color:{farben_dict[farbe]}; width:50px; height:50px; border:1px solid black;'></div>",
                unsafe_allow_html=True
            )
    
    if schuhe:
        st.write(f"**Schuhe:** {', '.join(schuhe)}")
    if accessoires:
        st.write(f"**Accessoires:** {', '.join(accessoires)}")
    if marken:
        st.write(f"**Lieblingsmarken:** {', '.join(marken)}")
else:
    st.write("Keine Outfits gefunden. Bitte passe deine Filter an.")

