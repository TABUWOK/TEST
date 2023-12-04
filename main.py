import streamlit as st
from backend import *

st.write("# FORMULARI INSCRIPCIÓ LES CORTS FC")
st.text_input('Nom:')
st.text_input('Cognoms:')

st.selectbox('Edat:', ['5-7 (Prebenjamí)','8-9 (Benjamí)','10-11 (Aleví)','12-13 (Infantil)','14-15(Cadet)','16-18 (Juvenil)'])
st.date_input('Data')
st.checkbox('Aceptes sortir en les imatges del club')
