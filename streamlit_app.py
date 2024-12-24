import streamlit as st
from PIL import Image

# Cover Image and Introduction
cover_image = r'Ref/Front Page.jpg'
st.image(cover_image)
st.title("Md. Asif Al Mahmud's Portfolio")

st.write("___")
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Projects</p>', unsafe_allow_html=True)

# Project Thumbnails
col1, col2 = st.columns(2)
Thumbnail_image_Highrise = r'Ref/Highrise Thumbnail.jpg'
Thumbnail_image_Residence = r'Ref/Residence1.jpg'
with col1:
    st.image(Thumbnail_image_Highrise)
    st.write("[Highrise](./pages/Highrise.py)")
with col2:
    st.image(Thumbnail_image_Residence)
    st.write("[Residence](./pages/Residence.py)")

# Conclusions
st.header("")
st.write("___")
col1, col2, col3 = st.columns(3)

with col2:
    st.write("Portfolio | Md. Asif Al Mahmud")
