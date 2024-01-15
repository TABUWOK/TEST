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
        st.image('https://futbolcatalunya.com/wp-content/uploads/2022/01/equipmercantil.jpg', width=325)
        st.markdown("<p style='text-align: center; color: black;'>La nostra historia</p>", unsafe_allow_html=True)
    with d:
        d.image('Imatges/Foto_jugadors.jpg', width=325)
        st.markdown("<p style='text-align: center; color: black;'>Equips</p>", unsafe_allow_html=True)
    
    