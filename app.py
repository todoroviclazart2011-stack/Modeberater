import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import openai

# --- OpenAI API Key ---
openai.api_key = "DEIN_OPENAI_API_KEY_HIER"

# --- Seitenlayout ---
st.set_page_config(
    page_title="Modeberater",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Style (dunkel, Magazin-Ästhetik) ---
st.markdown("""
<style>
body {
    background-color: #1C1C1C;
    color: #EDEDED;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.stButton>button {
    background-color: #FF6F61;
    color: white;
    font-weight: bold;
}
.stSidebar {
    background-color: #2C2C2C;
}
h1, h2, h3 {
    color: #FF6F61;
}
</style>
""", unsafe_allow_html=True)

st.title("👗 Modeberater Deluxe")

# --- Sprachwahl ---
language = st.sidebar.selectbox("Sprache / Language", ["Deutsch", "English", "Français", "Italiano", "Español", "Arabisch", "Mandarin", "Serbisch"])

# --- Filter Sidebar ---
st.sidebar.header("Filter")
geschlecht = st.sidebar.selectbox("Geschlecht", ["Männlich", "Weiblich", "Divers"])
jahreszeit = st.sidebar.selectbox("Jahreszeit", ["Frühling", "Sommer", "Herbst", "Winter"])
anlass = st.sidebar.multiselect("Anlass", ["Schule", "Arbeit", "Party", "Freizeit", "Date", "Sport"])
budget = st.sidebar.slider("Budget (€)", 10, 1000, (50, 300))
material = st.sidebar.multiselect("Material", ["Baumwolle", "Seide", "Wolle", "Leder", "Polyester", "Jeans"])
farben = st.sidebar.multiselect(
    "Farben auswählen",
    ["Schwarz","Weiß","Rot","Blau","Gelb","Grün","Rosa","Lila","Orange","Beige","Braun","Türkis","Gold","Silber","Dunkelblau","Bordeaux"],
    default=["Schwarz"]
)

wetter = st.sidebar.selectbox("Wetter", ["Sonnig", "Regen", "Schnee", "Windig", "Bewölkt"])
temperatur = st.sidebar.slider("Temperatur (°C)", -20, 40, 20)

# --- Optional: KI-Generierte Bildfunktion ---
def generate_outfit_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.error(f"Fehler beim Generieren des Bildes: {e}")
        return None

# --- Outfit-Generator ---
if st.button("Outfit generieren"):
    # Text-Prompt für KI
    prompt_text = f"Erstelle ein modisches Outfit für {geschlecht}, Jahreszeit: {jahreszeit}, Anlass: {', '.join(anlass)}, Budget: {budget}, Material: {', '.join(material)}, Farben: {', '.join(farben)}, Wetter: {wetter}, Temperatur: {temperatur}°C, im Stil einer eleganten Modezeitschrift."

    st.subheader("Vorgeschlagenes Outfit")
    st.markdown(f"**Beschreibung:** {prompt_text}")

    # KI-Bild generieren
    img = generate_outfit_image(prompt_text)
    if img:
        st.image(img, caption="KI-generiertes Outfit", use_column_width=True)

# --- Feedback-Funktion ---
st.subheader("Feedback geben")
feedback_text = st.text_area("Was gefällt dir am Outfit? Was sollte besser sein?")
if st.button("Feedback absenden"):
    st.success("Danke für dein Feedback!")

# --- Farb-Preview ---
st.subheader("Ausgewählte Farben")
cols = st.columns(len(farben))
for i, farbe in enumerate(farben):
    cols[i].markdown(f"<div style='background-color:{farbe.lower()};padding:20px;border-radius:5px;text-align:center;color:white;'>{farbe}</div>", unsafe_allow_html=True)
