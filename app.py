import streamlit as st

# --- Seiteneinstellungen ---
st.set_page_config(
    page_title="Modeberater Deluxe",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Styling (Vogue-ähnlich) ---
st.markdown("""
<style>
body {
    background-color: #121212;
    color: #fdfdfd;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
h1 {
    color: #ff4081;
    font-size: 3em;
}
h2 {
    color: #ffffff;
    font-size: 2em;
}
h3 {
    color: #ff80ab;
}
.stButton>button {
    background-color: #ff4081;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 1em;
    font-weight: bold;
}
.stSelectbox>div>div>div>select {
    background-color: #2b2b2b;
    color: white;
}
.stMultiselect>div>div>div>div {
    background-color: #2b2b2b;
    color: white;
}
.stSlider>div>div>div>input {
    background-color: #2b2b2b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- Haupttitel ---
st.title("👗 Modeberater Deluxe – Vogue-Edition")

# --- Sidebar Filter ---
st.sidebar.header("Filtern Sie Ihre Outfits")

# Geschlecht
gender = st.sidebar.radio("Geschlecht:", ["Keine Auswahl", "Männlich", "Weiblich", "Divers"])

# Anlass
occasion = st.sidebar.multiselect(
    "Anlass:",
    ["Alltag", "Schule", "Arbeit", "Party", "Sport", "Abendessen", "Shopping", "Date", "Urlaub", "Fotoshooting"]
)

# Saison
season = st.sidebar.selectbox("Saison:", ["Keine Auswahl", "Frühling", "Sommer", "Herbst", "Winter"])

# Material
material = st.sidebar.multiselect(
    "Material:",
    ["Baumwolle", "Seide", "Wolle", "Leinen", "Leder", "Polyester", "Mischgewebe", "Denim", "Kaschmir"]
)

# Budget
budget = st.sidebar.slider("Budget (€):", 0, 2000, (0, 250))

# Wetter
weather = st.sidebar.multiselect("Wetter:", ["Sonnig", "Regnerisch", "Schnee", "Windig", "Kalt", "Warm", "Heiß", "Neblig"])

# Temperaturen
temperature = st.sidebar.slider("Temperatur (°C):", -20, 45, (0, 30))

# Farben
st.sidebar.subheader("Farben auswählen:")
colors_dict = {
    "Schwarz": "#000000", "Weiß": "#FFFFFF", "Rot": "#FF0000", "Blau": "#0000FF",
    "Grün": "#00FF00", "Gelb": "#FFFF00", "Pink": "#FFC0CB", "Lila": "#800080",
    "Orange": "#FFA500", "Beige": "#F5F5DC", "Braun": "#A52A2A", "Grau": "#808080",
    "Türkis": "#40E0D0", "Gold": "#FFD700", "Silber": "#C0C0C0", "Dunkelblau": "#00008B",
    "Bordeaux": "#800000", "Khaki": "#F0E68C", "Oliv": "#808000", "Koralle": "#FF7F50"
}

selected_colors = []
for name, hex_code in colors_dict.items():
    if st.sidebar.checkbox(f"{name}  ", key=name):
        selected_colors.append((name, hex_code))

# Accessoires
st.sidebar.subheader("Accessoires:")
accessories = st.sidebar.multiselect(
    "Wählen Sie Accessoires aus:",
    ["Hut", "Schal", "Gürtel", "Tasche", "Schmuck", "Sonnenbrille", "Handschuhe", "Uhr"]
)

# Schuhe
st.sidebar.subheader("Schuhe:")
shoes = st.sidebar.multiselect(
    "Schuhe auswählen:",
    ["Sneaker", "Stiefel", "High Heels", "Sandalen", "Loafer", "Turnschuhe", "Boots"]
)

# --- Main Content: Outfits generieren ---
st.subheader("✨ Ihre Outfit-Vorschläge:")

# Beispielhafte Outfit-Daten
import random

outfits = [
    {
        "Name": "Eleganter Anzug",
        "Beschreibung": "Perfekt für Arbeit, Business oder elegante Abendveranstaltungen.",
        "Geschlecht": "Männlich",
        "Saison": ["Herbst", "Winter"],
        "Farben": ["Schwarz", "Grau"],
        "Material": ["Wolle", "Baumwolle"],
        "Anlass": ["Arbeit", "Abendessen"]
    },
    {
        "Name": "Sommerkleid",
        "Beschreibung": "Leichtes, luftiges Kleid für Sommer und Frühling.",
        "Geschlecht": "Weiblich",
        "Saison": ["Sommer", "Frühling"],
        "Farben": ["Rot", "Blau", "Gelb", "Pink", "Türkis"],
        "Material": ["Leinen", "Baumwolle"],
        "Anlass": ["Alltag", "Urlaub", "Party"]
    },
    {
        "Name": "Sportoutfit",
        "Beschreibung": "Bequem und funktional für Sport und Fitness.",
        "Geschlecht": "Keine Auswahl",
        "Saison": ["Sommer", "Frühling", "Herbst", "Winter"],
        "Farben": ["Schwarz", "Blau", "Weiß"],
        "Material": ["Polyester", "Mischgewebe"],
        "Anlass": ["Sport"]
    },
    {
        "Name": "Casual Jeans & T-Shirt",
        "Beschreibung": "Bequemes Outfit für Alltag, Schule oder Freizeit.",
        "Geschlecht": "Keine Auswahl",
        "Saison": ["Frühling", "Sommer", "Herbst"],
        "Farben": ["Blau", "Weiß", "Grau", "Schwarz"],
        "Material": ["Denim", "Baumwolle"],
        "Anlass": ["Alltag", "Schule", "Shopping"]
    },
]

# --- Filter Logik ---
def match_outfit(outfit):
    if gender != "Keine Auswahl" and gender != outfit["Geschlecht"] and outfit["Geschlecht"] != "Keine Auswahl":
        return False
    if season != "Keine Auswahl" and season not in outfit["Saison"]:
        return False
    if occasion and not any(o in outfit["Anlass"] for o in occasion):
        return False
    if material and not any(m in outfit["Material"] for m in material):
        return False
    if selected_colors and not any(c[0] in outfit["Farben"] for c in selected_colors):
        return False
    return True

filtered_outfits = [o for o in outfits if match_outfit(o)]

# --- Anzeige der Outfits ---
cols = st.columns(2)
for i, outfit in enumerate(filtered_outfits):
    with cols[i % 2]:
        st.markdown(f"### {outfit['Name']}")
        st.markdown(f"**Beschreibung:** {outfit['Beschreibung']}")
        st.markdown(f"**Farben:** " + ", ".join(outfit['Farben']))
        st.markdown(f"**Material:** " + ", ".join(outfit['Material']))
        st.markdown(f"**Anlass:** " + ", ".join(outfit['Anlass']))
        st.markdown("---")

# --- Feedback Bereich ---
st.subheader("💬 Feedback zu deinem Outfit")
feedback = st.text_area("Schreibe uns, wie dir das Outfit gefällt:")

if st.button("Feedback absenden"):
    if feedback:
        st.success("Danke für dein Feedback!")
    else:
        st.warning("Bitte schreibe etwas Feedback, bevor du absendest!")

# --- Footer ---
st.markdown("""
<style>
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("© 2025 Modeberater Deluxe | Designed like Vogue | Mehr Filter, mehr Farben, mehr Optionen!")
