import streamlit as st

st.markdown("<h1 style='text-align: center; color: #ab2a3e;'>COLLBLANC SANTS: EQUIPS</h1>", unsafe_allow_html=True)
e,m,d = st.columns(3)
with e:
    st.write("**1ra Divisió:**")
    lst = ['a']

    for i in lst:
        st.markdown("- " + "Pre-benjami A")
        st.markdown("- " + "Pre-benjami B")
        st.markdown("- " + "Benjami A")
        st.markdown("- " + "Alevi A")
        st.markdown("- " + "Infantil A")
        st.markdown("- " + "Infantil B")
        st.markdown("- " + "Cadet A")
        st.markdown("- " + "Juvenil A")

    st.write("**2na Divisió:**", )
    lst = ['a']

    for i in lst:
        st.markdown("- " + "Pre-benjami C")
        st.markdown("- " + "Benjami B")
        st.markdown("- " + "Benjami C")
        st.markdown("- " + "Alevi B")
        st.markdown("- " + "Infantil C")
        st.markdown("- " + "Cadet B")
        st.markdown("- " + "Cadet C")
        st.markdown("- " + "Juvenil B")
        st.markdown("- " + "Juvenil C")
with m:
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/1.-JUVENIL-A.jpeg", width=325)
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/6.-INFANTIL-B.jpg", width=325)
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/3.-CADET-B.jpeg", width=325)

with d:
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/PREA.jpg", width=325)
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/alevin-a-1.jpeg", width=325)
    st.image("https://pbcollblanc.com/wp-content/uploads/2016/06/5.-INFANTIL-A.jpg", width=325)
    