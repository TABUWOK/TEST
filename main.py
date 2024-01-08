import streamlit as st
import Formulari

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)

st.markdown(<div class="banner">
    <img src="https://www.les-corts.com/wp-content/uploads/cache/images/2-logo-pb-collblanc-rgb-1/2-logo-pb-collblanc-rgb-1-139828099.png" alt="Banner Image">
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
, unsafe_allow_html=True)




st.button('a', on_click=Formulari.form())