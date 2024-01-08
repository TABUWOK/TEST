import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
e,d,c = st.columns(3)

e.image('Imatges/Foto_jugadors.jpg', width=600)
d.image('Imatges/Foto_jugadors.jpg', width=200)
c.image('Imatges/Foto_jugadors.jpg', width=200)



st.button('a', on_click=Formulari.form())