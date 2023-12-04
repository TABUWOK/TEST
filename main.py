import streamlit as st
from backend import *

st.write("# FORMULARI INSCRIPCIÓ LES CORTS FC")
st.text_input('Nom:')
st.text_input('Cognoms:')

st.selectbox('Edat:', [5-7,8-9,10-11,12-13,14-15,16-18])


st.checkbox('Aceptes sortir en les imatges del club')
