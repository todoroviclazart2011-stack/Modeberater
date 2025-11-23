# --- Magazin-Stil Mitte ---
st.markdown("---")
st.subheader("✨ Deine individuell generierten Outfits")

def display_magazine_outfit(outfit):
    # Farbkreise HTML
    color_circles = " ".join([
        f'<span class="color-circle" style="background-color:{colors_dict[c]};" title="{c}"></span>' 
        for c in outfit['Farben']
    ])
    
    st.markdown(f"""
    <div style="
        background-color:#2a2a2a; 
        border-radius:20px; 
        padding:25px; 
        margin-bottom:25px; 
        box-shadow: 0 15px 30px rgba(0,0,0,0.6);
        transition: transform 0.2s;
    " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
        <h2 style="color:#ff4081; font-size:2.8em; text-align:center; margin-bottom:10px;">{outfit['Name']}</h2>
        <p style="color:#e0e0e0; font-size:1.3em; text-align:center; margin-bottom:15px;">{outfit['Beschreibung']}</p>
        <p style="text-align:center; margin-bottom:10px;"><b>Farben:</b> {color_circles}</p>
        <p style="color:#fdfdfd; text-align:center; margin-bottom:5px;"><b>Material:</b> {', '.join(outfit['Material'])}</p>
        <p style="color:#fdfdfd; text-align:center; margin-bottom:5px;"><b>Anlass:</b> {', '.join(outfit['Anlass'])}</p>
        <p style="color:#fdfdfd; text-align:center; margin-bottom:5px;"><b>Accessoires:</b> {', '.join(outfit['Accessoires'])}</p>
        <p style="color:#fdfdfd; text-align:center;"><b>Schuhe:</b> {', '.join(outfit['Schuhe'])}</p>
    </div>
    """, unsafe_allow_html=True)

# --- Outfits generieren ---
num_outfits = st.slider("Wie viele Outfits möchtest du sehen?", 1, 6, 3)

for _ in range(num_outfits):
    outfit = generate_outfit()
    if match_filters(outfit):
        display_magazine_outfit(outfit)
