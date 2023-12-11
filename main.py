import streamlit as st
from backend import *

st.write('# FORMULARI INSCRIPCIÓ LES CORTS FC')
st.image('https://www.les-corts.com/wp-content/uploads/cache/images/2-logo-pb-collblanc-rgb-1/2-logo-pb-collblanc-rgb-1-139828099.png')
st.text_input('Cognoms:')
dni=st.text_input(label='DNI', max_chars=9)
st.selectbox('Edat:', ['5-7 (Prebenjamí)','8-9 (Benjamí)','10-11 (Aleví)','12-13 (Infantil)','14-15(Cadet)','16-18 (Juvenil)'])
st.date_input('Data')
st.write('Lloc de naixement:')
st.text_input('Ciutat:') st.text_input('Provincia:')
st.selectbox('País:', ['Alemania', 'Austria', 'Andorra', 'Bélgica', 'Chipre', 'Eslovaquia', 'Eslovenia', 'España', 'Estonia', 'Finlandia', 'Francia', 'Grecia', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo', 'Malta', 'Mónaco', 'Montenegro', 'Países Bajos', 'Portugal', 'San Marino', 'Ciudad del Vaticano'])
st.checkbox('Aceptes sortir en les imatges del club')