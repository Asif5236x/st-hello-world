import streamlit as st
from PIL import Image

st.markdown('<p style="font-size: 30px; font-weight: bold;">CONTACT INFORMATION</p>', unsafe_allow_html=True)
st.write("___")
st.subheader("Asif Al Mahmud")
st.write("Architecture student")


image_1= r'ref/Me2.jpg'

icon_1=r'ref/Mail.png'
icon_2=r'ref/Address.png'
icon_3=r'ref/Phone.png'
icon_4=r'ref/Linkedin logo .png'
icon_5=r'ref/Institution logo.png'
icon_6=r'ref/Facebook logo.png'

col1, icons, contact = st.columns([3,1,6])
with col1:
    st.image(image_1,width=400)
with icons:
    st.image(icon_1,width=47)
    st.image(icon_2,width=47)
    st.image(icon_3,width=47)
    st.image(icon_4,width=47)
    st.image(icon_6,width=47)
    st.image(icon_5,width=47)

with contact:
    st.markdown('<p style="font-size: 16px;">Mail: asif5236x@ gmail.com</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">Phone: 01676233714</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">Address: Salimullah Road, Mohamadpur, Dhaka-1207  </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">www.linkedin.com/in/Md. Asif al Mahmud</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">www.Facebook.com/Profile/Md.Asif Al Mahmud </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">Bangladesh University of Engineering and Technology </p>', unsafe_allow_html=True)



st.header("Profile")
st.write("Architecture should be centered on enhancing human well-being through thoughtful design and aesthetics, rather than merely creating costly, visually striking structures. I am dedicated to becoming more involved in practical, impactful design processes. With strong skills in 3D modeling, rendering, and architectural photography and cinematography, I bring a comprehensive, creative approach to the profession.")
st.subheader("")


#  Software Skills
st.header("Software Skills")
st.write("___")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">4 years+</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">3-4 years</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">1-3 years</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">1 yearor less</p>', unsafe_allow_html=True)
with col2:
    st.write("SKetchup, Adobe Photoshop")
    st.write("Autocad, Rhino")
    st.write("Lumion, Blender,Archicad")
    st.write("Twinmotion, Archicad, Enscape")        
st.header("")



#  Experience
st.header("Experience")
st.write("___")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2024</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2023</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2020-2024</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2024</p>', unsafe_allow_html=True)
with col2:
    st.write("Graphic Designer and Animator at ANIMATA")
    st.write("Interior Design")
    st.write("Mentor At UDVASH")
    st.write("Model making: Academic Projects, Thesis Projects")
st.header("")



#  Participation
st.header("Participation")
st.write("___")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Workshop</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Workshop</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Workshop</p>', unsafe_allow_html=True)
    
with col2:
    st.write("Seine and Buriganga")
    st.write("Architecture in the Digital Age")
    st.write("A thousands Words")
    
with col3:
    st.write("Alliance Francise de Dhaka")
    st.write("The Prestige Megazine")
    st.write("Obscure Artists of BD")
st.header("")



#  Education
st.header("Education")
st.write("___")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Year</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2017</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2019</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 17px; font-weight: bold;">2020-Present</p>', unsafe_allow_html=True)
    
with col2:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Level</p>', unsafe_allow_html=True)
    st.write("SSC")
    st.write("HSC")
    st.write("UNDERGRAD")
with col3:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Institute</p>', unsafe_allow_html=True)
    st.write("DRMC")
    st.write("DRMC")
    st.write("BUET")

with col4:
    st.markdown('<p style="font-size: 17px; font-weight: bold;">Result</p>', unsafe_allow_html=True)
    st.write("GPA 5")
    st.write("GPA 5")
    st.write("_")
st.header("")

#  Language
st.header("Language")
st.write("___")
st.write("Bangla")
st.write("English")
st.header("")



#  Hobby
st.header("Hobby")
st.write("___")
st.write("Art")
st.write("Photography")
st.write("Cinematography")
st.write("Rendering")
st.write("Travelling")
st.header("")

   
#  Education
st.header("Reference")
st.write("___")
st.markdown('<p style="font-size: 17px; font-weight: bold;">Dr. SM Najmul Imam</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 17px; font-weight: bold;">Bristi Majumder</p>', unsafe_allow_html=True)



# Conclusions

st.write("___")
col1, col2, col3 = st.columns(3)

with col2:
    st.write("Resume | Md. Asif Al Mahmud")







