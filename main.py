import streamlit as st
import Formulari

st.session_state["Pagina"] = "main"

if st.button("a"):
    st.session_state["Pagina"] = "Formulari"

if st.session_state["Pagina"] == "Formulari":
    Formulari.form()
elif st.session_state["Pagina"] == "main":
    st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
    e,d = st.columns(2)
    with e:
        st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Ffutbolcatalunya.com%2Fmurtro-adeu-a-un-gran-del-futbol-catala%2F&psig=AOvVaw39KDkFBAt9YN5cKXugr5CN&ust=1705426356183000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPCQ7bv234MDFQAAAAAdAAAAABAQ', width=325)
        st.markdown("<p style='text-align: center; color: black;'>La nostra historia</p>", unsafe_allow_html=True)
    with d:
        d.image('Imatges/Foto_jugadors.jpg', width=325)
        st.markdown("<p style='text-align: center; color: black;'>Equips</p>", unsafe_allow_html=True)
    
    