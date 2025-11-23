import streamlit as st
from random import choice

# --- Seite ---
st.set_page_config(page_title="Vogue Fashion Outfit Generator", layout="wide", page_icon="👗")

# --- CSS für Vogue-Look ---
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #f8f8f8, #eaeaea);
    font-family: 'Roboto', sans-serif;
}
h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    text-align: center;
    color: #222;
    margin-bottom: 1rem;
}
.outfit-card {
    background: #fff;
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    transition: transform 0.2s;
}
.outfit-card:hover {
    transform: scale(1.02);
}
.filter-container {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 30px;
}
.filter-item {
    background: #fff;
    padding: 12px 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
.color-circle {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 5px;
    cursor: pointer;
    border: 2px solid #ccc;
}
.language-select {
    text-align: right;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Sprache auswählen ---
language = st.selectbox("Sprache / Language / Langue:", ["Deutsch", "English", "Français"], key="lang")

# --- Titel ---
st.markdown("<h1>Vogue Fashion Outfit Generator</h1>", unsafe_allow_html=True)

# --- Filter-Container ---
st.markdown("<div class='filter-container'>", unsafe_allow_html=True)

# Geschlecht
gender = st.selectbox("Geschlecht / Gender:", ["Weiblich","Männlich","Divers","Keine Präferenz"])

# Saison
season = st.selectbox("Saison / Season:", ["Frühling","Sommer","Herbst","Winter","Keine Präferenz"])

# Anlass
occasion = st.multiselect("Anlass / Occasion:", ["Schule","Arbeit","Party","Date","Sport","Freizeit","Andere"])

# Wetter
weather = st.selectbox("Wetter / Weather:", ["Sonnig","Regnerisch","Schnee","Windig","Keine Präferenz"])

# Temperatur
temperature = st.slider("Temperatur (°C) / Temperature:", -10,40,(10,25))

# Budget
budget = st.selectbox("Budget / Budget:", ["€","€€","€€€","Keine Präferenz"])

# Material
material = st.multiselect("Material / Material:", ["Baumwolle","Wolle","Seide","Leder","Kunstfaser","Denim"])

# Muster
pattern = st.multiselect("Muster / Pattern:", ["Uni","Gestreift","Kariert","Gemustert","Floral","Andere"])

# Accessoires
accessories = st.multiselect("Accessoires / Accessories:", ["Schal","Hut","Handtasche","Schmuck","Brille","Keine"])

# Schuhe
shoes = st.multiselect("Schuhe / Shoes:", ["Sneaker","Stiefel","Sandalen","Loafers","High Heels"])

# Taschen
bags = st.multiselect("Taschen / Bags:", ["Rucksack","Clutch","Handtasche","Shopper","Keine"])

# Schmuck
jewelry = st.multiselect("Schmuck / Jewelry:", ["Ohrringe","Kette","Armband","Ringe","Keine"])

# Farben mit Kreisen
color_options = ["Schwarz","Weiß","Rot","Blau","Gelb","Grün","Orange","Lila","Pink","Beige","Braun","Türkis","Grau","Gold","Silber"]
selected_colors = st.multiselect("Farben / Colors:", options=color_options)
color_html = "".join([f"<div class='color-circle' style='background:{c.lower()};'></div>" for c in selected_colors])
st.markdown(color_html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Outfit Generator ---
def generate_outfit():
    tops = ["T-Shirt","Bluse","Pullover","Hemd","Tanktop","Hoodie"]
    bottoms = ["Jeans","Rock","Shorts","Hose","Leggings"]
    shoes_choice = shoes if shoes else ["Sneaker","Stiefel","Sandalen","Loafers","High Heels"]
    accessories_choice = accessories if accessories else ["Keine"]
    colors_choice = selected_colors if selected_colors else color_options
    outfit = {
        "Oberteil": choice(tops),
        "Unterteil": choice(bottoms),
        "Schuhe": choice(shoes_choice),
        "Accessoire": choice(accessories_choice),
        "Farbe": choice(colors_choice),
        "Tasche": choice(bags) if bags else "Keine",
        "Schmuck": choice(jewelry) if jewelry else "Keine"
    }
    return outfit

if st.button("Outfit generieren / Generate Outfit"):
    outfit = generate_outfit()
    st.markdown("<div class='outfit-card'>", unsafe_allow_html=True)
    st.markdown(f"**Oberteil / Top:** {outfit['Oberteil']} ({outfit['Farbe']})")
    st.markdown(f"**Unterteil / Bottom:** {outfit['Unterteil']} ({outfit['Farbe']})")
    st.markdown(f"**Schuhe / Shoes:** {outfit['Schuhe']} ({outfit['Farbe']})")
    st.markdown(f"**Accessoire / Accessory:** {outfit['Accessoire']}")
    st.markdown(f"**Tasche / Bag:** {outfit['Tasche']}")
    st.markdown(f"**Schmuck / Jewelry:** {outfit['Schmuck']}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feedback
    feedback = st.text_area("Feedback zu diesem Outfit / Feedback on this outfit:", placeholder="Deine Meinung hier / Your opinion here")
    if st.button("Feedback absenden / Submit Feedback"):
        st.success("Danke für dein Feedback / Thanks for your feedback!")

# --- Footer ---
st.markdown("<p style='text-align:center;color:#888;'>© 2025 Vogue Fashion App</p>", unsafe_allow_html=True)
