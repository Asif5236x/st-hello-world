import streamlit as st
from PIL import Image
import os

# Define paths
cover_image = os.path.join('ref', 'Front Page.jpg')
Thumbnail_image_Highrise = os.path.join('ref', 'Highrise Thumbnail.jpg')
Thumbnail_image_Residence = os.path.join('ref', 'Residence1.jpg')

# Cover Image
if os.path.exists(cover_image):
    st.image(cover_image)
else:
    st.error(f"File not found: {cover_image}")

st.write("___")
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Projects</p>', unsafe_allow_html=True)

# Project Thumbnails
col1, col2 = st.columns(2)

if os.path.exists(Thumbnail_image_Highrise):
    with col1:
        st.image(Thumbnail_image_Highrise)
        if st.button("Highrise"):
            st.experimental_set_query_params(page="Highrise")
else:
    st.error(f"File not found: {Thumbnail_image_Highrise}")

if os.path.exists(Thumbnail_image_Residence):
    with col2:
        st.image(Thumbnail_image_Residence)
        if st.button("Residence"):
            st.experimental_set_query_params(page="Residence")
else:
    st.error(f"File not found: {Thumbnail_image_Residence}")

# Conclusions
st.write("___")
col1, col2, col3 = st.columns(3)

with col2:
    st.write("Portfolio | Md. Asif Al Mahmud")
