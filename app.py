import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- Seiteneinstellungen ---
st.set_page_config(
    page_title="Modeberater Deluxe",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body {
    background-color: #1c1c1c;
    color: #f5f5f5;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    background-color: #ff4081;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stSelectbox>div>div>div>select {
    background-color: #2b2b2b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("👗 Fashion Advisor Deluxe – Magazin Style")

# --- Sidebar Filter ---
st.sidebar.header("Filter deine Outfits")

# Geschlecht
gender = st.sidebar.radio("Geschlecht:", ["Keine Auswahl", "Männlich", "Weiblich", "Divers"])

# Anlass
occasion = st.sidebar.multiselect(
    "Anlass:",
    ["Alltag", "Schule", "Arbeit", "Party", "Sport", "Abendessen", "Shopping", "Date", "Urlaub"]
)

# Jahreszeit
season = st.sidebar.selectbox("Jahreszeit:", ["Keine Auswahl", "Frühling", "Sommer", "Herbst", "Winter"])

# Material
material = st.sidebar.multiselect(
    "Material:",
    ["Baumwolle", "Seide", "Wolle", "Leinen", "Leder", "Polyester", "Mischgewebe", "Denim"]
)

# Budget
budget = st.sidebar.slider("Budget (€):", 0, 1000, (0, 200))

# Wetter
weather = st.sidebar.multiselect("Wetter:", ["Sonnig", "Regnerisch", "Schnee", "Windig", "Kalt", "Warm"])

# Farben
st.sidebar.subheader("Farben auswählen:")
colors_dict = {
    "Schwarz": "#000000", "Weiß": "#FFFFFF", "Rot": "#FF0000", "Blau": "#0000FF",
    "Grün": "#00FF00", "Gelb": "#FFFF00", "Pink": "#FFC0CB", "Lila": "#800080",
    "Orange": "#FFA500", "Beige": "#F5F5DC", "Braun": "#A52A2A", "Grau": "#808080"
}

selected_colors = []
for name, hex_code in colors_dict.items():
    if st.sidebar.checkbox(f"{name}", key=name):
        selected_colors.append((name, hex_code))

# Temperatur
temperature = st.sidebar.slider("Temperatur (°C):", -20, 40, (0, 25))

# --- Main Content ---
st.subheader("Dein perfektes Outfit")

# Optional: OpenAI-Key
openai_key = st.sidebar.text_input("OpenAI API Key (optional):", type="password")

# Beispielhafte Outfit-Daten
import random
outfits = [
    {"Name": "Eleganter Anzug", "Bild": "https://i.ibb.co/PrPj0XY/suit.jpg", "Beschreibung": "Perfekt für Arbeit oder Business."},
    {"Name": "Sommerkleid", "Bild": "https://i.ibb.co/3mYyVZ1/summer-dress.jpg", "Beschreibung": "Leicht und luftig für den Sommer."},
    {"Name": "Sportoutfit", "Bild": "https://i.ibb.co/cXxjW1S/sport.jpg", "Beschreibung": "Ideal für Fitness und Sport."},
    {"Name": "Casual Jeans & T-Shirt", "Bild": "https://i.ibb.co/KWqgRkQ/casual.jpg", "Beschreibung": "Alltagstauglich und bequem."}
]

# Filter Logik (vereinfachtes Beispiel)
filtered_outfits = []
for outfit in outfits:
    if gender != "Keine Auswahl" and gender.lower() not in outfit["Name"].lower():
        continue
    if season != "Keine Auswahl" and season.lower() not in outfit["Beschreibung"].lower():
        continue
    filtered_outfits.append(outfit)

# Anzeige
cols = st.columns(2)
for i, outfit in enumerate(filtered_outfits):
    with cols[i % 2]:
        st.image(outfit["Bild"], use_column_width=True)
        st.markdown(f"**{outfit['Name']}**")
        st.write(outfit["Beschreibung"])

# Feedback
st.subheader("Feedback zum Outfit")
feedback = st.text_area("Schreibe uns, wie dir das Outfit gefällt:")

if st.button("Feedback absenden"):
    if feedback:
        st.success("Danke für dein Feedback!")
    else:
        st.warning("Bitte schreibe etwas Feedback, bevor du absendest!")

# Hinweis: OpenAI-Bildgenerierung kann hier eingebaut werden, wenn API-Key vorhanden ist.
