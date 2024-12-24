import streamlit as st
from PIL import Image


# Cover Image and Description
cover_image=r'ref/1. Asif Base Render.jpg'


col1, col2 = st.columns(2)
with col1:
    st.image(cover_image, width=700)
with col2:
    st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">HIGHRISE</p>', unsafe_allow_html=True)
    st.write("Design Studio VI")
    st.write("Site: Hatirjheel")
    st.markdown('<p style="color: Grey; font-size: 25px; font-weight: bold;">Description</p>', unsafe_allow_html=True)
    st.write('The project was developed in Design Studio VI, located in Hatirjheel. The structural system utilized a diagrid design to enhance stability and efficiency. The form was inspired by principles of aerodynamics to optimize performance.')
st.write("___")



# Form Generation
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Form Generation</p>', unsafe_allow_html=True)
Form_gen=r'ref/Form Gen.jpg'
st.image(Form_gen)
st.write("The building features a narrow top for improved aerodynamics, reducing wind resistance and enhancing stability. This design helps defend against lateral forces, making the structure more resilient to high winds and extreme weather.")
st.write("___")
st.header("")

# Floor Plan
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Floor Plan</p>', unsafe_allow_html=True)
st.header("")
Ground_floor=r'ref/Ground floor.jpg'
st.image(Ground_floor)
st.write("Ground Floor Plan")

st.header("")
Basement_floor=r'ref/Basment floor plan.jpg'
st.image(Basement_floor)
st.write("Basement Floor Plan")


st.header("")
Typical_floor=r'ref/Typical Floor Plan.jpg'
st.image(Typical_floor)
st.write("Typical Floor Plan")
st.write("___")



# Structure

st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Structure</p>', unsafe_allow_html=True)
Structure_1=r'ref/Structure1.jpg'
Structure_2=r'ref/Structure2.jpg'
st.subheader("")
col1, col2 = st.columns(2)
with col1:
    st.image(Structure_1, width=300)
    st.write("Structural Floor Connection")
with col2:
	st.image(Structure_2, width=300)
	st.write("Structural Joinery Details")
st.write("___")


# Sectional and Model Images
st.markdown('<p style="color: Grey; font-size: 30px; font-weight: bold;">Sectional and Model Images</p>', unsafe_allow_html=True)
st.header("")
Structure_1=r'ref/Structure1.jpg'
Model1=r'ref/Model1.jpg'
Model2=r'ref/Model2.jpg'
Section=r'ref/Section.jpg'
col1, col2 = st.columns(2)
with col1:
    st.image(Section)
    st.write("Section")
with col2:
	st.image(Model1, width=200)
	st.image(Model2,width=195)
	st.write("Model Images")
st.header("")
st.write("___")



