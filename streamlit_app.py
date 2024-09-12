
import streamlit as st

from datetime import datetime, timedelta
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression

import re

import plotly.express as px
import plotly.graph_objects as go

import os

from email.mime.image import MIMEImage

import base64

from streamlit_javascript import st_javascript

# CSS pour masquer le lien GitHub et le footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.image("logo.png", width=150)

st.title("Vitesse Critique")


st.write("Indique tes meileurs temps durant des efforts maximaux sur 1200m et 3600m")

# Données des courses : distances en mètres et temps en secondes
distances_test = {
    "1200 mètres": 1200,
    "3600 mètres": 3600,
}




# Vérification avant de calculer les vitesses
def calculate_speed_safe(distance, minutes, seconds):
    total_seconds = minutes * 60 + seconds
    if total_seconds > 0:
        speed = distance / total_seconds
    else:
        speed = 0
    return speed, total_seconds

def calculate_pace(total_seconds, distance_meters):
        pace_seconds_per_km = total_seconds / (distance_meters / 1000)
        minutes, seconds = divmod(pace_seconds_per_km, 60)
        return f"{int(minutes)} min {int(seconds):02d} s / km"

results = {}
total_seconds = {}
speeds = {}
for distance_text, distance_meters in zip(distances_test.keys(), distances_test.values()):
            st.write(f"**{distance_text}**")
                                            
            col1, col2 = st.columns(2)
            with col1:
                        minutes = st.number_input(f"Minutes", min_value=0, max_value=59, value=0, key=f"{distance_meters}_minutes")
            with col2:
                        seconds = st.number_input(f"Secondes", min_value=0, max_value=59, value=0, key=f"{distance_meters}_seconds")
            results[distance_text] = (minutes, seconds)
            speed, seconds_test = calculate_speed_safe(distance_meters, minutes, seconds)
            total_seconds[distance_text] = seconds_test
            speeds[distance_text] = speed

if 0 not in list(total_seconds.values()):

            if list(total_seconds.values())[0] != list(total_seconds.values())[1]:

                         if list(total_seconds.values())[0] > list(total_seconds.values())[1]:


                                    cs = 1200 / (total_seconds["1200 mètres"] + (total_seconds["3600 mètres"] - (3600/1200)*total_seconds["1200 mètres"])/(3600/1200 - 1))

                                    st.write(f"**Résultats des tests**")
                                    st.write(f"Vitesse Critique : {cs:.2f} m/s, {(cs * 3.6):.2f} km/h")
                                    st.write(f"Allure Critique : {calculate_pace(1, cs)}")

                                    st.write(f"**% de Vitesse Critique pour ton entraînement**")

                                    pourcentage = st.slider('Choisissez un pourcentage', min_value=0, max_value=100, step=1)

                                    st.write("A {pourcentage}%")
                                    percent_cs = percentage * cs
                                    st.write(f"% Vitesse Critique : {percent_cs:.2f} m/s, {(percent_cs * 3.6):.2f} km/h")
                                    st.write(f"% Allure Critique : {calculate_pace(1, percent_cs)}")


                        
                                    

                         else:
                                    st.warning("Le temps de ton test sur 1200 mètres doit être inféreur au temps sur 3600 mètres")
                                     
            else:
                        st.warning("Insère des temps différents pour les deux courses")
else:
            st.warning("Insère des temps non nuls pour les deux tests.")




