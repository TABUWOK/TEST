import streamlit as st
from backend import *

st.write("# FORMULARI INSCRIPCIÓ LES CORTS FC")
img = cv2.imread("https://www.les-corts.com/wp-content/uploads/cache/images/2-logo-pb-collblanc-rgb-1/2-logo-pb-collblanc-rgb-1-139828099.png")
res = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)st.text_input('Nom:')
st.text_input('Cognoms:')
dni=st.text_input(label='DNI', max_chars=9)
st.selectbox('Edat:', ['5-7 (Prebenjamí)','8-9 (Benjamí)','10-11 (Aleví)','12-13 (Infantil)','14-15(Cadet)','16-18 (Juvenil)'])
st.date_input('Data')
st.checkbox('Aceptes sortir en les imatges del club')
