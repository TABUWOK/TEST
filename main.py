import streamlit as st
from backend import *

st.write("# FORMULARI INSCRIPCIÓ LES CORTS FC")
st.text_input('Nom:')
st.text_input('Cognoms:')

st.selectbox('Select', [1,2,3])


st.checkbox('Aceptes sortir en les imatges del club')
