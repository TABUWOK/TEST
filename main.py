import streamlit as st
from backend import *

st.write("Hello, World")
# st.write(pythontest(2))

if st.button('Balloons?'):
    st.balloons()

if st.button("hi!"):
    st.write("hi!")
st.checkbox('Check me out')
