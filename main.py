import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fpbcollblanc.com%2F&psig=AOvVaw0yD3dngq05j2Pa4OAyQAoJ&ust=1704823845464000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCL0fGxzoMDFQAAAAAdAAAAABAc', width=100)


st.button('a', on_click=Formulari.form())