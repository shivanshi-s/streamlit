import streamlit as st

def page():
    # Heading
    st.markdown("<h1 style='text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)

    # Contact information
    st.write("Email: info@agrosmart.com")
    st.write("Phone: 123-456-7890")

    # Contact form
    st.write("Fill out the form below to get in touch:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Submit"):
        st.write(f"Thank you, {name}! We'll get back to you at {email} soon.")