import streamlit as st

def page():
    # Heading
    st.markdown("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)

    # Placeholder paragraph
    st.write("""
    This is a placeholder paragraph for the About Us page. Here, you can provide information about the team, the mission of the company, or any other relevant details.
    """)

    # Links to LinkedIn profiles
    st.markdown("""
    - [Person 1's Name](https://www.linkedin.com/in/person1)
    - [Person 2's Name](https://www.linkedin.com/in/person2)
    - [Person 3's Name](https://www.linkedin.com/in/person3)
    """, unsafe_allow_html=True)