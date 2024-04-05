# pages/home.py
import streamlit as st

def render_page():
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    # Use the path to the image file directly
    # st.image("images/home-image.jpg", use_column_width=True, caption="Home Image")
    st.write("## Welcome to Agro Smart")
    st.write("Agro Smart is a leading agricultural technology company dedicated to providing innovative solutions for sustainable farming.")

    # Grid of images
    st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
    # st.markdown("<div class='grid-item'><a href='/crop'><img src='images/image1.jpg' alt='Image 1'></a></div>", unsafe_allow_html=True)
    # st.markdown("<div class='grid-item'><a href='/disease'><img src='images/image2.jpg' alt='Image 2'></a></div>", unsafe_allow_html=True)
    # st.markdown("<div class='grid-item'><a href='/weather'><img src='images/image3.jpg' alt='Image 3'></a></div>", unsafe_allow_html=True)
    # st.markdown("<div class='grid-item'><a href='/soil'><img src='images/image4.jpg' alt='Image 4'></a></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<footer>Copyright &copy; Agro Smart 2023</footer>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)