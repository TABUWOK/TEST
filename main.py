import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
e,d = st.columns(2)

e.image('Imatges/Foto_jugadors.jpg', width=325, caption = "Titols")
d.image('Imatges/Foto_jugadors.jpg', width=325, caption = "Equips")




st.button('a', on_click=Formulari.form())