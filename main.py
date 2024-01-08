import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
e,d = st.columns(2)
with e:
    st.image('Imatges/Foto_jugadors.jpg', width=325)
    st.markdown("<p style='text-align: center; color: black;'>Titols</p>", unsafe_allow_html=True)
with d:
    d.image('Imatges/Foto_jugadors.jpg', width=325)
    st.markdown("<p style='text-align: center; color: black;'>Equips</p>", unsafe_allow_html=True)


if st.button("a"):
    Formulari.form()
