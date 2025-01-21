import streamlit as st
import pandas as pd
import pickle
import joblib


import requests

model = joblib.load('C:/Users/SERKAN/OneDrive/Masaüstü/vsc son deneme/deneme/best_xgboost_modelvsc89.joblib')




# Modeli yükle
#with open('C:\\Users\\SERKAN\\OneDrive\\Masaüstü\\vsc son deneme\\deneme\\best_xgboost_modelvsc89.pkl', 'rb') as f:
#    model = pickle.load(f)

# Sayfa yapılandırması
st.set_page_config(page_title="Footballer Market Value Prediction", layout="centered")

# Girişe fotoğraf ekleme
st.image("C:/Users/SERKAN/OneDrive/Masaüstü/vsc son deneme/deneme/pic1.png", use_container_width=True)



# Streamlit başlık
st.title("Footballer Market Value Prediction")


# Kullanıcıdan giriş alınacak alanlar
ovr = st.number_input("OVR", min_value=0, max_value=100, value=50)
pac = st.number_input("PAC", min_value=0, max_value=100, value=50)
sho = st.number_input("SHO", min_value=0, max_value=100, value=50)
pas = st.number_input("PAS", min_value=0, max_value=100, value=50)
dri = st.number_input("DRI", min_value=0, max_value=100, value=50)
defe = st.number_input("DEF", min_value=0, max_value=100, value=50)
phy = st.number_input("PHY", min_value=0, max_value=100, value=50)
acceleration = st.number_input("Acceleration", min_value=0, max_value=100, value=50)
positioning = st.number_input("Positioning", min_value=0, max_value=100, value=50)
shot_power = st.number_input("Shot Power", min_value=0, max_value=100, value=50)
penalties = st.number_input("Penalties", min_value=0, max_value=100, value=50)
vision = st.number_input("Vision", min_value=0, max_value=100, value=50)
crossing = st.number_input("Crossing", min_value=0, max_value=100, value=50)
free_kick_accuracy = st.number_input("Free Kick Accuracy", min_value=0, max_value=100, value=50)
short_passing = st.number_input("Short Passing", min_value=0, max_value=100, value=50)
curve = st.number_input("Curve", min_value=0, max_value=100, value=50)
agility = st.number_input("Agility", min_value=0, max_value=100, value=50)
balance = st.number_input("Balance", min_value=0, max_value=100, value=50)
reactions = st.number_input("Reactions", min_value=0, max_value=100, value=50)
composure = st.number_input("Composure", min_value=0, max_value=100, value=50)
heading_accuracy = st.number_input("Heading Accuracy", min_value=0, max_value=100, value=50)
jumping = st.number_input("Jumping", min_value=0, max_value=100, value=50)
stamina = st.number_input("Stamina", min_value=0, max_value=100, value=50)
strength = st.number_input("Strength", min_value=0, max_value=100, value=50)
aggression = st.number_input("Aggression", min_value=0, max_value=100, value=50)
height = st.number_input("Height", min_value=150, max_value=250, value=180)
weight = st.number_input("Weight", min_value=50, max_value=150, value=75)
age = st.number_input("Age", min_value=16, max_value=45, value=25)
gk_features = st.number_input("GK Features", min_value=0, max_value=500, value=50)
ovr_pac = st.number_input("OVR_PAC", min_value=0, max_value=10000, value=50)

# Lig seçimi
league = st.selectbox("League", [
    'League_Bundesliga', 'League_Bundesliga 2', 'League_EFL Championship',
    'League_Eredivisie', 'League_LALIGA EA SPORTS', 'League_LALIGA HYPERMOTION',
    'League_Libertadores', 'League_Liga Portugal', "League_Ligue 1 McDonald's",
    'League_MLS', 'League_Premier League', 'League_ROSHN Saudi League',
    'League_Serie A Enilive', 'League_Serie BKT', 'League_Sudamericana',
    'League_Trendyol Süper Lig'
])

# Pozisyon kategorisi
position_category = st.selectbox("Position Category", [
    "Position_Category_Attacker",'Position_Category_Defender', 'Position_Category_Goalkeeper', 'Position_Category_Midfielder'
])

# Bölge seçimi
region = st.selectbox("Region", ['Europe', 'Non-Europe'])

# Weak foot ve Skill moves
weak_foot = st.selectbox("Weak Foot", [1, 2, 3, 4, 5])
skill_moves = st.selectbox("Skill Moves", [1, 2, 3, 4, 5])

# Yaş grubu seçimi
age_group = st.selectbox("Age Group", ['Teen','Young Adult', 'Adult'])

# Giriş verilerini birleştirin
input_data_dict = {
    'OVR': ovr,
    'PAC': pac,
    'SHO': sho,
    'PAS': pas,
    'DRI': dri,
    'DEF': defe,
    'PHY': phy,
    'Acceleration': acceleration,
    'Positioning': positioning,
    'Shot Power': shot_power,
    'Penalties': penalties,
    'Vision': vision,
    'Crossing': crossing,
    'Free Kick Accuracy': free_kick_accuracy,
    'Short Passing': short_passing,
    'Curve': curve,
    'Agility': agility,
    'Balance': balance,
    'Reactions': reactions,
    'Composure': composure,
    'Heading Accuracy': heading_accuracy,
    'Jumping': jumping,
    'Stamina': stamina,
    'Strength': strength,
    'Aggression': aggression,
    'Height': height,
    'Weight': weight,
    'Age': age,
    'OVR_PAC': ovr_pac,
    'gk_features': gk_features,
    league: 1,
    position_category: 1,
    'Region_Non-Europe': 1 if region == 'Non-Europe' else 0,
    f'Weak foot_{weak_foot}': 1,
    f'Skill moves_{skill_moves}': 1,
    f'Age_Group_{age_group.replace(" ", "_")}': 1
}

# DataFrame'e dönüştür
input_data = pd.DataFrame([input_data_dict], columns=model.feature_names_in_).fillna(0)

# Predict
if st.button("Predicted Market Value"):
    prediction = model.predict(input_data)
    #st.write(f"Predicted Market Value: {prediction[0]:,.2f} €")
    st.balloons()
    st.markdown(f"""
    <div style="font-size:30px; font-weight:bold; color:#4CAF50; text-align:center;">
        Predicted Market Value: {prediction[0]:,.2f} €
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
        .custom-text {
            font-size: 20px;
        }
    </style>
    <div class="custom-text">
        ---
        This site was created by Fehmi Serkan Kazankaya and Mert Basar.
    </div>
""", unsafe_allow_html=True)