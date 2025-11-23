import streamlit as st
from PIL import Image
import random

# --- Mehrsprachig ---
sprachwahl = st.sidebar.selectbox("Sprache / Language", ["Deutsch", "English", "Français", "Italiano"])

texts = {
    "Deutsch": {
        "title": "👗 Modeberater Deluxe",
        "filter": "Filter auswählen",
        "gender": "Geschlecht",
        "season": "Jahreszeit",
        "occasion": "Anlass",
        "weather": "Wetter",
        "temperature": "Temperatur (°C)",
        "budget": "Budget",
        "material": "Material",
        "pattern": "Muster",
        "accessories": "Accessoires",
        "colors": "Farben",
        "optional": "Optionale Filter anzeigen",
        "outfits": "💃 Generierte Outfits",
        "feedback": "📝 Feedback",
        "feedback_placeholder": "Gib hier dein Feedback zu den Outfits ein:",
        "feedback_submit": "Feedback absenden",
        "feedback_thanks": "Danke für dein Feedback!",
        "no_outfits": "Keine Outfits gefunden. Versuche andere Filter!"
    },
    "English": {
        "title": "👗 Deluxe Fashion Advisor",
        "filter": "Choose Filters",
        "gender": "Gender",
        "season": "Season",
        "occasion": "Occasion",
        "weather": "Weather",
        "temperature": "Temperature (°C)",
        "budget": "Budget",
        "material": "Material",
        "pattern": "Pattern",
        "accessories": "Accessories",
        "colors": "Colors",
        "optional": "Show optional filters",
        "outfits": "💃 Generated Outfits",
        "feedback": "📝 Feedback",
        "feedback_placeholder": "Give your feedback on the outfits:",
        "feedback_submit": "Submit Feedback",
        "feedback_thanks": "Thanks for your feedback!",
        "no_outfits": "No outfits found. Try different filters!"
    },
    "Français": {
        "title": "👗 Conseiller Mode Deluxe",
        "filter": "Choisir des filtres",
        "gender": "Genre",
        "season": "Saison",
        "occasion": "Occasion",
        "weather": "Temps",
        "temperature": "Température (°C)",
        "budget": "Budget",
        "material": "Matériel",
        "pattern": "Motif",
        "accessories": "Accessoires",
        "colors": "Couleurs",
        "optional": "Afficher les filtres optionnels",
        "outfits": "💃 Tenues générées",
        "feedback": "📝 Retour",
        "feedback_placeholder": "Donnez votre avis sur les tenues:",
        "feedback_submit": "Envoyer le feedback",
        "feedback_thanks": "Merci pour votre avis!",
        "no_outfits": "Aucune tenue trouvée. Essayez d'autres filtres!"
    },
    "Italiano": {
        "title": "👗 Consulente di Moda Deluxe",
        "filter": "Seleziona filtri",
        "gender": "Genere",
        "season": "Stagione",
        "occasion": "Occasione",
        "weather": "Meteo",
        "temperature": "Temperatura (°C)",
        "budget": "Budget",
        "material": "Materiale",
        "pattern": "Fantasia",
        "accessories": "Accessori",
        "colors": "Colori",
        "optional": "Mostra filtri opzionali",
        "outfits": "💃 Outfit generati",
        "feedback": "📝 Feedback",
        "feedback_placeholder": "Lascia il tuo feedback sugli outfit:",
        "feedback_submit": "Invia Feedback",
        "feedback_thanks": "Grazie per il tuo feedback!",
        "no_outfits": "Nessun outfit trovato. Prova altri filtri!"
    }
}

t = texts[sprachwahl]

# --- Page Config & Design ---
st.set_page_config(page_title=t["title"], layout="wide", page_icon="👗")

# Custom CSS für Vogue-Style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto&display=swap');

body {
    background-color: #fdf6f0;
    font-family: 'Roboto', sans-serif;
    color: #222;
}

h1 {
    font-family: 'Playfair Display', serif;
    font-size: 50px;
    text-align: center;
    color: #111;
}

h2 {
    font-family: 'Playfair Display', serif;
    color: #333;
}

.stButton>button {
    background-color: #d67d0a;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
    border: none;
}

.stButton>button:hover {
    background-color: #b65e05;
    color: #fff;
    transform: scale(1.05);
    transition: 0.3s;
}

.stSelectbox, .stSlider, .stMultiselect, .stTextArea {
    border-radius: 8px;
    padding: 5px;
    background-color: #fff;
}

.outfit-container {
    border-radius: 15px;
    padding: 15px;
    background-color: #fff3e6;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.color-box {
    display: inline-block;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    margin-right: 5px;
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)

# --- Sidebar Filters ---
st.sidebar.header(t["filter"])
geschlecht = st.sidebar.selectbox(t["gender"], ["Beliebig", "Männlich", "Weiblich", "Divers"])
jahreszeit = st.sidebar.selectbox(t["season"], ["Beliebig", "Frühling", "Sommer", "Herbst", "Winter"])
anlass = st.sidebar.multiselect(t["occasion"], ["Schule", "Party", "Arbeit", "Casual", "Sport", "Date"])
wetter = st.sidebar.selectbox(t["weather"], ["Beliebig", "Sonnig", "Regnerisch", "Schnee", "Windig"])
temperatur = st.sidebar.slider(t["temperature"], -10, 40, (10, 25))
budget = st.sidebar.selectbox(t["budget"], ["Beliebig", "Günstig", "Mittel", "Teuer"])
material = st.sidebar.multiselect(t["material"], ["Baumwolle", "Wolle", "Seide", "Leder", "Synthetik", "Denim"])

farben = ["Schwarz","Weiß","Rot","Blau","Grün","Gelb","Rosa","Lila","Braun","Orange","Beige","Grau",
          "Türkis","Mint","Khaki","Bordeaux","Dunkelblau","Gold","Silber","Bronze","Lavendel","Pfirsich",
          "Koralle","Oliv","Magenta","Cyan","Violett","Pastellblau"]
selected_colors = st.sidebar.multiselect(t["colors"], farben)

optionale_filter = st.sidebar.checkbox(t["optional"])
if optionale_filter:
    muster = st.sidebar.multiselect(t["pattern"], ["Uni", "Gestreift", "Karriert", "Blumen", "Animal"])
    accessoires = st.sidebar.multiselect(t["accessories"], ["Hut", "Schal", "Tasche", "Schuhe", "Brille"])

# --- Dummy-Outfit-Datenbank ---
outfits = [
    {"Name": "Casual Sommer Outfit", "Bild": "bilder/casual1.jpg", "Farben": ["Blau", "Weiß"], "Anlass": ["Casual","Schule"], "Geschlecht":"Beliebig","Jahreszeit":"Sommer"},
    {"Name": "Business Winter Outfit", "Bild": "bilder/business1.jpg", "Farben": ["Schwarz","Grau"], "Anlass":["Arbeit"], "Geschlecht":"Beliebig","Jahreszeit":"Winter"},
    {"Name": "Party Look", "Bild": "bilder/party1.jpg", "Farben": ["Rot","Schwarz"], "Anlass":["Party"], "Geschlecht":"Beliebig","Jahreszeit":"Herbst"},
    # Weitere Outfits hier
]

# --- Outfit Filter ---
def filter_outfits(outfits):
    filtered = []
    for o in outfits:
        if geschlecht != "Beliebig" and o["Geschlecht"] != geschlecht: continue
        if jahreszeit != "Beliebig" and o["Jahreszeit"] != jahreszeit: continue
        if anlass and not any(a in o["Anlass"] for a in anlass): continue
        if selected_colors and not any(c in o["Farben"] for c in selected_colors): continue
        filtered.append(o)
    return filtered

filtered_outfits = filter_outfits(outfits)

# --- Outfits anzeigen ---
st.header(t["outfits"])
if filtered_outfits:
    for o in filtered_outfits:
        st.markdown("<div class='outfit-container'>", unsafe_allow_html=True)
        st.subheader(o["Name"])
        try:
            img = Image.open(o["Bild"])
            st.image(img, use_column_width=True)
        except:
            st.text("Bild nicht gefunden")
        # Farben anzeigen
        farben_html = "".join([f"<span class='color-box' style='background-color:{c.lower()}' title='{c}'></span>" for c in o["Farben"]])
        st.markdown(farben_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.write(t["no_outfits"])

# --- Feedback ---
st.header(t["feedback"])
feedback = st.text_area(t["feedback_placeholder"])
if st.button(t["feedback_submit"]):
    st.success(t["feedback_thanks"])
