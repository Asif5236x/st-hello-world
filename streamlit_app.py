import streamlit as st
from PIL import Image

# Cover Image
cover_image=r'ref/Front Page.jpg'
st.image(cover_image)



st.write("___")
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Projects</p>', unsafe_allow_html=True)


# Project Thumbnails
col1, col2 = st.columns(2)
Thumbnail_image_Highrise=r'ref/Highrise Thumbnail.jpg'
Thumbnail_image_Residence=r'ref/Residence1.jpg'
with col1:
    st.image(Thumbnail_image_Highrise)
    st.page_link("Pages/Highrise.py", label="Highrise")
with col2:
    st.image(Thumbnail_image_Residence)
    st.page_link("Pages/Residence.py", label="Residence")


# Conclusions
st.header("")
st.write("___")
col1, col2, col3 = st.columns(3)

with col2:
    st.write("Portfolio | Md. Asif Al Mahmud")
