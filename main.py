# main.py
import streamlit as st
import os

# Import pages
from pages import home, about, crop_rec, soil, weather, disease

# Navigation dictionary
nav_links = {
    "Home": home,
    "About": about,
    "Soil": soil,
    "Crop Rec": crop_rec,
    "Disease Pred": disease,
    "Weather Pred": weather,
}

# Navbar function
def render_navbar():
    st.markdown(f"""
    <style>
        .navbar {{
            background-color: #1B4242;
            color: white;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .navbar h1 {{
            margin: 0;
            font-size: 24px;
        }}

        .navbar nav {{
            display: flex;
            gap: 20px;
        }}

        .navbar a {{
            color: white;
            text-decoration: none;
            font-size: 16px;
            transition: color 0.3s;
        }}

        .navbar a:hover {{
            color: #ddd;
        }}
    </style>
    <div class="navbar">
        <h1>Agro Smart</h1>
        <nav>
            {"".join([f"<a href='/{link.lower()}'>{link}</a>" for link in nav_links])}
        </nav>
    </div>
    """, unsafe_allow_html=True)

    # Import CSS styles
    styles_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(styles_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render the appropriate page based on the URL
def main():
    st.set_page_config(page_title="Agro Smart", page_icon=":seedling:", layout="wide")
    render_navbar()

    if "page" in st.query_params:
        page_name = st.query_params["page"][0].capitalize()
        if page_name in nav_links:
            nav_links[page_name].render_page()
        else:
            home.render_page()
    else:
        home.render_page()

if __name__ == "__main__":
    main()