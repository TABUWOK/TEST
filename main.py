import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
st.image('Imatges\Foto_jugadors.jpg', width=100)


st.button('a', on_click=Formulari.form())