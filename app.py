st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits")

# --- Magazin-Stil Layout ---
def generate_magazine_outfit():
    # Zufällige Auswahl für Demo
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
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:20px;">
        <div style="background-color:#2a2a2a; border-radius:20px; padding:25px; width:80%; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
            <h2 style="color:#ff4081; font-size:2.5em; text-align:center;">{outfit['Name']}</h2>
            <p style="color:#e0e0e0; font-size:1.2em; text-align:center;">{outfit['Beschreibung']}</p>
            <p style="text-align:center;">
                <b>Farben:</b> {" ".join([f'<span class="color-circle" style="background-color:{colors_dict[c]}"></span>' for c in outfit['Farben']])}
            </p>
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
