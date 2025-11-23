import streamlit as st
import random

# --- Seiteneinstellungen ---
st.set_page_config(
    page_title="Modeberater Deluxe",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Styling ---
st.markdown("""
<style>
body {
    background-color: #1c1c1c;
    color: #fdfdfd;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
h1 {
    color: #ff4081;
    font-size: 3.5em;
    text-align: center;
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
.stSlider>div>div>div>input, .stSelectbox>div>div>div>select, .stMultiselect>div>div>div>div {
    background-color: #2b2b2b;
    color: white;
}
.stTextArea>div>textarea {
    background-color: #2b2b2b;
    color: white;
}
.outfit-box {
    background-color: #2a2a2a;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
}
.color-circle {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 5px;
    border: 1px solid #fff;
}
</style>
""", unsafe_allow_html=True)

# --- Haupttitel ---
st.title("👗 Modeberater Deluxe – Vogue-Edition")

# --- Sidebar Filter ---
st.sidebar.header("🔍 Filteroptionen")

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
    ["Baumwolle", "Seide", "Wolle", "Leinen", "Leder", "Polyester", "Mischgewebe", "Denim", "Kaschmir", "Chiffon", "Samt", "Nylon"]
)

# Budget
budget = st.sidebar.slider("Budget (€):", 0, 5000, (0, 300))

# Wetter
weather = st.sidebar.multiselect("Wetter:", ["Sonnig", "Regnerisch", "Schnee", "Windig", "Kalt", "Warm", "Heiß", "Neblig", "Feucht", "Trocken"])

# Temperaturen
temperature = st.sidebar.slider("Temperatur (°C):", -20, 45, (0, 30))

# Farben
st.sidebar.subheader("Farben auswählen:")
colors_dict = {
    "Schwarz": "#000000", "Weiß": "#FFFFFF", "Rot": "#FF0000", "Blau": "#0000FF",
    "Grün": "#00FF00", "Gelb": "#FFFF00", "Pink": "#FFC0CB", "Lila": "#800080",
    "Orange": "#FFA500", "Beige": "#F5F5DC", "Braun": "#A52A2A", "Grau": "#808080",
    "Türkis": "#40E0D0", "Gold": "#FFD700", "Silber": "#C0C0C0", "Dunkelblau": "#00008B",
    "Bordeaux": "#800000", "Khaki": "#F0E68C", "Oliv": "#808000", "Koralle": "#FF7F50",
    "Magenta": "#FF00FF", "Mint": "#98FF98", "Pfirsich": "#FFDAB9", "Senf": "#FFDB58"
}

selected_colors = []
for name, hex_code in colors_dict.items():
    if st.sidebar.checkbox(f"{name}  ", key=name):
        selected_colors.append((name, hex_code))

# Accessoires
accessories = st.sidebar.multiselect(
    "Accessoires:",
    ["Hut", "Schal", "Gürtel", "Tasche", "Schmuck", "Sonnenbrille", "Handschuhe", "Uhr", "Ohrringe", "Armband"]
)

# Schuhe
shoes = st.sidebar.multiselect(
    "Schuhe:",
    ["Sneaker", "Stiefel", "High Heels", "Sandalen", "Loafer", "Turnschuhe", "Boots", "Mokassins", "Slipper"]
)

# Extra Filter
st.sidebar.subheader("Extras:")
patterns = st.sidebar.multiselect("Muster:", ["Uni", "Gestreift", "Karomuster", "Punkte", "Animal Print", "Floral", "Paisley"])
necklines = st.sidebar.multiselect("Ausschnitt:", ["Rundhals", "V-Ausschnitt", "Rollkragen", "Schulterfrei", "Hoodie", "Stehkragen"])
lengths = st.sidebar.multiselect("Länge:", ["Kurz", "Midi", "Lang", "Knielang", "Maxi", "Mini"])

# --- Generierung Mitte ---
st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits:")

def generate_outfit():
    # Zufällige Auswahl für Demo, in Realität hier KI-Integration möglich
    outfit_name = random.choice(["Eleganter Chic", "Sommerfrische", "Urban Casual", "Sporty Style", "Office Glam"])
    desc = random.choice([
        "Perfekt für jeden Anlass und die Saison angepasst.",
        "Leicht, elegant und modisch.",
        "Stylisch, bequem und farblich abgestimmt.",
        "Ein Outfit, das sofort ins Auge fällt.",
        "Perfekt für ein Fotoshooting oder Event."
    ])
    colors = random.sample(list(colors_dict.keys()), k=random.randint(1,4))
    mat = random.sample(["Baumwolle","Wolle","Seide","Denim","Leder","Polyester","Chiffon","Samt"], k=random.randint(1,3))
    occasion_list = random.sample(["Alltag","Party","Date","Urlaub","Arbeit","Sport"], k=random.randint(1,3))
    accessories_list = random.sample(["Hut","Schal","Gürtel","Tasche","Schmuck","Sonnenbrille","Handschuhe","Uhr"], k=random.randint(0,3))
    shoes_list = random.sample(["Sneaker","Stiefel","High Heels","Sandalen","Loafer","Boots"], k=random.randint(1,2))
    
    return {
        "Name": outfit_name,
        "Beschreibung": desc,
        "Farben": colors,
        "Material": mat,
        "Anlass": occasion_list,
        "Accessoires": accessories_list,
        "Schuhe": shoes_list
    }

# --- Filter Logik ---
def match_filters(outfit):
    if gender != "Keine Auswahl" and gender != "Divers":  # Divers passt zu allem
        pass  # Hier könnte Gender spezifisch gefiltert werden
    if season != "Keine Auswahl":
        pass  # Saison Filter
    if occasion and not any(o in outfit["Anlass"] for o in occasion):
        return False
    if material and not any(m in outfit["Material"] for m in material):
        return False
    if selected_colors and not any(c in outfit["Farben"] for c,_ in selected_colors):
        return False
    if accessories and not any(a in outfit["Accessoires"] for a in accessories):
        return False
    if shoes and not any(s in outfit["Schuhe"] for s in shoes):
        return False
    if patterns:
        pass
    if necklines:
        pass
    if lengths:
        pass
    return True

# --- Generierung von mehreren Outfits ---
num_outfits = st.slider("Wie viele Outfits möchtest du sehen?", 1, 6, 3)

for _ in range(num_outfits):
    outfit = generate_outfit()
    if match_filters(outfit):
        st.markdown(f"""
        <div class="outfit-box">
        <h2>{outfit['Name']}</h2>
        <p>{outfit['Beschreibung']}</p>
        <p><b>Farben:</b> {" ".join([f'<span class="color-circle" style="background-color:{colors_dict[c]}"></span>' for c in outfit['Farben']])}</p>
        <p><b>Material:</b> {", ".join(outfit['Material'])}</p>
        <p><b>Anlass:</b> {", ".join(outfit['Anlass'])}</p>
        <p><b>Accessoires:</b> {", ".join(outfit['Accessoires'])}</p>
        <p><b>Schuhe:</b> {", ".join(outfit['Schuhe'])}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Feedback ---
st.subheader("💬 Feedback zu deinen Outfits")
feedback = st.text_area("Dein Feedback:")
if st.button("Feedback absenden"):
    if feedback:
        st.success("Danke für dein Feedback!")
    else:
        st.warning("Bitte schreibe etwas Feedback.")

# Footer
st.markdown("""
<style>
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("© 2025 Modeberater Deluxe | Vogue-Edition | Mehr Filter, mehr Farben, mehr Optionen!")
