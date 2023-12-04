import streamlit as st
from backend import *

st.write("# FORMULARI INSCRIPCIÓ LES CORTS FC")
st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fcelescortsbarcelona.com%2F&psig=AOvVaw1ueEw9wYWHQ4X-gFRZsVN6&ust=1701795643076000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKCrmPeg9oIDFQAAAAAdAAAAABAE')
st.text_input('Nom:')
st.text_input('Cognoms:')
dni=st.text_input(label='DNI', max_chars=9)
st.selectbox('Edat:', ['5-7 (Prebenjamí)','8-9 (Benjamí)','10-11 (Aleví)','12-13 (Infantil)','14-15(Cadet)','16-18 (Juvenil)'])
st.date_input('Data')
st.checkbox('Aceptes sortir en les imatges del club')
