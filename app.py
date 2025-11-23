import streamlit as st
import random

# --- Farben definieren ---
colors_dict = {
    "Rot": "#FF0000", "Blau": "#0000FF", "Grün": "#00FF00", 
    "Gelb": "#FFFF00", "Schwarz": "#000000", "Weiß": "#FFFFFF", 
    "Rosa": "#FFC0CB", "Lila": "#800080", "Orange": "#FFA500",
    "Türkis": "#40E0D0", "Beige": "#F5F5DC", "Braun": "#A52A2A"
}

# --- Dummy-Funktion für Filter (optional) ---
def match_filters(outfit):
    # Hier könntest du die Sidebar-Filters abgleichen
    # Für Demo einfach alles True
    return True

st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits")

# --- Magazin-Stil Layout ---
def generate_magazine_outfit():
    outfit_name = random.choice(["Eleganter Chic", "Sommerfrische", "Urban Casual", "Sporty Style", "Office Glam"])
    desc = random.choice([
        "Perfekt für jeden Anlass und die Saison angepasst.",
        "Leicht, elegant und modisch.",
        "Stylisch, bequem und farblich abgestimmt.",
        "Ein Outfit, das sofort ins Auge fällt.",
        "Perfekt für ein Fotoshooting oder Event."
    ])
    colors = random.sample(list(colors_dict.keys()), k=random.randint(2,4))
    mat = random.sample(["Baumwolle","Wolle","Seide","Denim","Leder","Polyester","Chiffon","Samt"], k=random.randint(1,2))
    occasion_list = random.sample(["Alltag","Party","Date","Urlaub","Arbeit","Sport"], k=random.randint(1,2))
    accessories_list = random.sample(["Hut","Schal","Gürtel","Tasche","Schmuck","Sonnenbrille"], k=random.randint(0,2))
    shoes_list = random.sample(["Sneaker","Stiefel","High Heels","Sandalen","Loafer","Boots"], k=1)
    
    return {
        "Name": outfit_name,
        "Beschreibung": desc,
        "Farben": colors,
        "Material": mat,
        "Anlass": occasion_list,
        "Accessoires": accessories_list,
        "Schuhe": shoes_list
    }

def display_magazine_outfit(outfit):
    color_circles = " ".join([f'<span style="display:inline-block;width:20px;height:20px;background-color:{colors_dict[c]};border-radius:50%;margin:2px;"></span>' for c in outfit['Farben']])
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:20px;">
        <div style="background-color:#2a2a2a; border-radius:20px; padding:25px; width:80%; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
            <h2 style="color:#ff4081; font-size:2.5em; text-align:center;">{outfit['Name']}</h2>
            <p style="color:#e0e0e0; font-size:1.2em; text-align:center;">{outfit['Beschreibung']}</p>
            <p style="text-align:center;"><b>Farben:</b> {color_circles}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Material:</b> {", ".join(outfit['Material'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Anlass:</b> {", ".join(outfit['Anlass'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Accessoires:</b> {", ".join(outfit['Accessoires'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Schuhe:</b> {", ".join(outfit['Schuhe'])}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Generierung von mehreren Magazin-Outfits ---
num_outfits = st.slider("Wie viele Outfits möchtest du sehen?", 1, 6, 3)

for _ in range(num_outfits):
    outfit = generate_magazine_outfit()
    if match_filters(outfit):
        display_magazine_outfit(outfit)
import streamlit as st
import random

# --- Farben definieren ---
colors_dict = {
    "Rot": "#FF0000", "Blau": "#0000FF", "Grün": "#00FF00", 
    "Gelb": "#FFFF00", "Schwarz": "#000000", "Weiß": "#FFFFFF", 
    "Rosa": "#FFC0CB", "Lila": "#800080", "Orange": "#FFA500",
    "Türkis": "#40E0D0", "Beige": "#F5F5DC", "Braun": "#A52A2A"
}

# --- Dummy-Funktion für Filter (optional) ---
def match_filters(outfit):
    # Hier könntest du die Sidebar-Filters abgleichen
    # Für Demo einfach alles True
    return True

st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits")

# --- Magazin-Stil Layout ---
def generate_magazine_outfit():
    outfit_name = random.choice(["Eleganter Chic", "Sommerfrische", "Urban Casual", "Sporty Style", "Office Glam"])
    desc = random.choice([
        "Perfekt für jeden Anlass und die Saison angepasst.",
        "Leicht, elegant und modisch.",
        "Stylisch, bequem und farblich abgestimmt.",
        "Ein Outfit, das sofort ins Auge fällt.",
        "Perfekt für ein Fotoshooting oder Event."
    ])
    colors = random.sample(list(colors_dict.keys()), k=random.randint(2,4))
    mat = random.sample(["Baumwolle","Wolle","Seide","Denim","Leder","Polyester","Chiffon","Samt"], k=random.randint(1,2))
    occasion_list = random.sample(["Alltag","Party","Date","Urlaub","Arbeit","Sport"], k=random.randint(1,2))
    accessories_list = random.sample(["Hut","Schal","Gürtel","Tasche","Schmuck","Sonnenbrille"], k=random.randint(0,2))
    shoes_list = random.sample(["Sneaker","Stiefel","High Heels","Sandalen","Loafer","Boots"], k=1)
    
    return {
        "Name": outfit_name,
        "Beschreibung": desc,
        "Farben": colors,
        "Material": mat,
        "Anlass": occasion_list,
        "Accessoires": accessories_list,
        "Schuhe": shoes_list
    }

def display_magazine_outfit(outfit):
    color_circles = " ".join([f'<span style="display:inline-block;width:20px;height:20px;background-color:{colors_dict[c]};border-radius:50%;margin:2px;"></span>' for c in outfit['Farben']])
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:20px;">
        <div style="background-color:#2a2a2a; border-radius:20px; padding:25px; width:80%; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
            <h2 style="color:#ff4081; font-size:2.5em; text-align:center;">{outfit['Name']}</h2>
            <p style="color:#e0e0e0; font-size:1.2em; text-align:center;">{outfit['Beschreibung']}</p>
            <p style="text-align:center;"><b>Farben:</b> {color_circles}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Material:</b> {", ".join(outfit['Material'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Anlass:</b> {", ".join(outfit['Anlass'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Accessoires:</b> {", ".join(outfit['Accessoires'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Schuhe:</b> {", ".join(outfit['Schuhe'])}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Generierung von mehreren Magazin-Outfits ---
num_outfits = st.slider("Wie viele Outfits möchtest du sehen?", 1, 6, 3)

for _ in range(num_outfits):
    outfit = generate_magazine_outfit()
    if match_filters(outfit):
        display_magazine_outfit(outfit)
import streamlit as st
import random

# --- Farben definieren ---
colors_dict = {
    "Rot": "#FF0000", "Blau": "#0000FF", "Grün": "#00FF00", 
    "Gelb": "#FFFF00", "Schwarz": "#000000", "Weiß": "#FFFFFF", 
    "Rosa": "#FFC0CB", "Lila": "#800080", "Orange": "#FFA500",
    "Türkis": "#40E0D0", "Beige": "#F5F5DC", "Braun": "#A52A2A"
}

# --- Dummy-Funktion für Filter (optional) ---
def match_filters(outfit):
    # Hier könntest du die Sidebar-Filters abgleichen
    # Für Demo einfach alles True
    return True

st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits")

# --- Magazin-Stil Layout ---
def generate_magazine_outfit():
    outfit_name = random.choice(["Eleganter Chic", "Sommerfrische", "Urban Casual", "Sporty Style", "Office Glam"])
    desc = random.choice([
        "Perfekt für jeden Anlass und die Saison angepasst.",
        "Leicht, elegant und modisch.",
        "Stylisch, bequem und farblich abgestimmt.",
        "Ein Outfit, das sofort ins Auge fällt.",
        "Perfekt für ein Fotoshooting oder Event."
    ])
    colors = random.sample(list(colors_dict.keys()), k=random.randint(2,4))
    mat = random.sample(["Baumwolle","Wolle","Seide","Denim","Leder","Polyester","Chiffon","Samt"], k=random.randint(1,2))
    occasion_list = random.sample(["Alltag","Party","Date","Urlaub","Arbeit","Sport"], k=random.randint(1,2))
    accessories_list = random.sample(["Hut","Schal","Gürtel","Tasche","Schmuck","Sonnenbrille"], k=random.randint(0,2))
    shoes_list = random.sample(["Sneaker","Stiefel","High Heels","Sandalen","Loafer","Boots"], k=1)
    
    return {
        "Name": outfit_name,
        "Beschreibung": desc,
        "Farben": colors,
        "Material": mat,
        "Anlass": occasion_list,
        "Accessoires": accessories_list,
        "Schuhe": shoes_list
    }

def display_magazine_outfit(outfit):
    color_circles = " ".join([f'<span style="display:inline-block;width:20px;height:20px;background-color:{colors_dict[c]};border-radius:50%;margin:2px;"></span>' for c in outfit['Farben']])
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:20px;">
        <div style="background-color:#2a2a2a; border-radius:20px; padding:25px; width:80%; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
            <h2 style="color:#ff4081; font-size:2.5em; text-align:center;">{outfit['Name']}</h2>
            <p style="color:#e0e0e0; font-size:1.2em; text-align:center;">{outfit['Beschreibung']}</p>
            <p style="text-align:center;"><b>Farben:</b> {color_circles}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Material:</b> {", ".join(outfit['Material'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Anlass:</b> {", ".join(outfit['Anlass'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Accessoires:</b> {", ".join(outfit['Accessoires'])}</p>
            <p style="color:#fdfdfd; text-align:center;"><b>Schuhe:</b> {", ".join(outfit['Schuhe'])}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Generierung von mehreren Magazin-Outfits ---
num_outfits = st.slider("Wie viele Outfits möchtest du sehen?", 1, 6, 3)

for _ in range(num_outfits):
    outfit = generate_magazine_outfit()
    if match_filters(outfit):
        display_magazine_outfit(outfit)
