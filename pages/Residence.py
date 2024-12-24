import streamlit as st
from PIL import Image


# Cover Image and Description
cover_image=r'ref/Residence.jpg'


col1, col2 = st.columns(2)
with col1:
    st.image(cover_image)
with col2:
    st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">RESIDENCE</p>', unsafe_allow_html=True)
    st.write("Design Studio III")
    st.markdown('<p style="color: Grey; font-size: 25px; font-weight: bold;">Description</p>', unsafe_allow_html=True)
    st.write('Residences are essential for family togetherness and bonding. A key element of traditional Bangladeshi homes is the উঠান, which promotes this connection. The courtyard and landscaped areas provide a breathable environment, enhancing the quality of life.')
st.write("___")



# Form Generation
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Form Generation</p>', unsafe_allow_html=True)
Form_gen=r'ref/Form gen Residence.jpg'
st.image(Form_gen)
st.write("This residence features a central courtyard design, promoting family togetherness and enhancing natural ventilation. The open, communal space fosters connection among family members while providing a peaceful retreat, ideal for Bangladesh’s climate and lifestyle.")
st.write("___")
st.header("")


# Floor Plan
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Floor Plan</p>', unsafe_allow_html=True)
st.header("")
Ground_floor=r'ref/Ground Floor Residence.jpg'
st.image(Ground_floor)
st.header("")
st.header("")
First_floor=r'ref/First Floor Residence.jpg'
st.image(First_floor)
st.write("___")
st.write("")

# Exploded
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Exploded</p>', unsafe_allow_html=True)

Exploded=r'ref/Exploded.jpg'
st.image(Exploded)
st.write("___")


# Visualizations

st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Visualizations</p>', unsafe_allow_html=True)
st.write("")
Axono=r'ref/Axono.jpg'
Ele1=r'ref/Ele1.jpg'
Ele2=r'ref/Ele2.jpg'
col1, col2 = st.columns(2)
with col1:
    st.image(Axono)
    st.write("Birds Eye View")
with col2:
    st.image(Ele1, width=280)
    st.image(Ele2,width=280)
    st.write("Elevations")
st.write("___")


# Sections
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Sections</p>', unsafe_allow_html=True)

Section_Residence=r'ref/Section Residence.jpg'
Section_with_Blowup=r'ref/Section with blowup.jpg'
st.image(Section_Residence)
st.write("Section AA")
st.write("___")
st.image(Section_with_Blowup)
st.write("Section BB")
st.header("")
st.write("___")







