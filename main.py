import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
st.image('http://pbcollblanc.com/wp-content/uploads/2019/01/foto-balon-cabecera-3-1-e1548841828911.jpg')





st.button('a', on_click=Formulari.form())