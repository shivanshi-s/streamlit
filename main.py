import streamlit as st
from pathlib import Path

# Set page configuration
st.set_page_config(page_title="Agro Smart", page_icon=":seedling:", layout="wide")

# Load custom CSS
with open("styles.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render the landing page by default
def main():
    pages = [p.stem for p in Path("pages").glob("*.py") if p.stem != "__init__"]
    selected_page = st.selectbox("Navigation", ["Home"] + pages)
    if selected_page == "Home":
        render_landing_page()
    else:
        page = __import__(f"pages.{selected_page}", fromlist=["page"])
        page.page()

# Function to render the landing page
def render_landing_page():
    # Header
    st.markdown("<h1 style='text-align: center;'>Welcome to Agro Smart</h1>", unsafe_allow_html=True)

    # Space for an image
    st.image("images/image.jpg", caption="Your Image Caption", use_column_width=True)

    # Four paragraphs with headings
    st.markdown("<h2>Heading 1</h2>", unsafe_allow_html=True)
    st.write("This is the first paragraph.")
    st.markdown("<h2>Heading 2</h2>", unsafe_allow_html=True)
    st.write("This is the second paragraph.")
    st.markdown("<h2>Heading 3</h2>", unsafe_allow_html=True)
    st.write("This is the third paragraph.")
    st.markdown("<h2>Heading 4</h2>", unsafe_allow_html=True)
    st.write("This is the fourth paragraph.")

if __name__ == "__main__":
    main()