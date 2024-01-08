import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fpbcollblanc.com%2F&psig=AOvVaw3ey_0TgESdXAwa_0PZMpgY&ust=1704822280120000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNDwr4qszoMDFQAAAAAdAAAAABAI')





st.button('a', on_click=Formulari.form())