import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)

custom_html = """
<div class="banner">
    <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 160%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""




st.button('a', on_click=Formulari.form())