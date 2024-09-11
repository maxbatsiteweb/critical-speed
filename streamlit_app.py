
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

# Fonction pour calculer la vitesse en m/s
def calculate_speed(distance, hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    speed = distance / total_seconds
    return speed, total_seconds


# Vérification avant de calculer les vitesses
def calculate_speed_safe(distance, hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if total_seconds > 0:
        speed = distance / total_seconds
    else:
        speed = 0
    return speed, total_seconds

results = {}
total_seconds = []
speeds = []
for distance_text, distance_meters in zip(distances_test.keys(), distances_test.values()):
            st.write(f"**{distance_text}**")
                                            
            col1, col2 = st.columns(2)
            with col1:
                        minutes = st.number_input(f"Minutes", min_value=0, max_value=59, value=0, key=f"{distance_meters}_minutes")
            with col2:
                        seconds = st.number_input(f"Secondes", min_value=0, max_value=59, value=0, key=f"{distance_meters}_seconds")
            results[distance_text] = (minutes, seconds)
            speed, seconds_race = calculate_speed_safe(distance, hours, minutes, seconds)
            total_seconds.append(seconds_race)
            speeds.append(speed) 

if 0 not in total_seconds:
            st.write(total_secondes)
else:
            st.warning("Insère des temps non nuls pour les deux tests.")




