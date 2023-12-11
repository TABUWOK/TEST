import streamlit as st
from backend import *

st.write('# FORMULARI INSCRIPCIÓ LES CORTS FC')
st.image('https://www.les-corts.com/wp-content/uploads/cache/images/2-logo-pb-collblanc-rgb-1/2-logo-pb-collblanc-rgb-1-139828099.png')
st.text_input('Cognoms:')
dni=st.text_input(label='DNI', max_chars=9)
st.slider('Edat:', min_value=5, max_value=18)
st.select_slider('Edat:', options=['5','6','7','8','9','10','11','12','13','14','15','16','17','18'])
st.date_input('Data')
st.write('Lloc de naixement:')
st.text_input('Ciutat:') 
st.text_input('Provincia:')
st.selectbox('País:', ['Alemania', 'Austria', 'Andorra', 'Bélgica', 'Chipre', 'Eslovaquia', 'Eslovenia', 'España', 'Estonia', 'Finlandia', 'Francia', 'Grecia', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo', 'Malta', 'Mónaco', 'Montenegro', 'Países Bajos', 'Portugal', 'San Marino', 'Ciudad del Vaticano'])
st.checkbox('Aceptes sortir en les imatges del club')