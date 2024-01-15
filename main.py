import streamlit as st
import Formulari

st.session_state["Pagina"] = "main"

if st.button("a"):
    st.session_state["Pagina"] = "Formulari"
    st.write(st.session_state["Pagina"])
else:
    st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS</h1>", unsafe_allow_html=True)
    e,d = st.columns(2)
    with e:
        st.image('Imatges/Foto_jugadors.jpg', width=325)
        st.markdown("<p style='text-align: center; color: black;'>Titols</p>", unsafe_allow_html=True)
    with d:
        d.image('Imatges/Foto_jugadors.jpg', width=325)
        st.markdown("<p style='text-align: center; color: black;'>Equips</p>", unsafe_allow_html=True)




if st.session_state["Pagina"] == "Formulari":
    Formulari.form()
    