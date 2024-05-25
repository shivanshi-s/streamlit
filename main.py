import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components


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
    st.markdown("<h1 style='text-align: center;'>Welcome to Agro Smart 🌱</h1>", unsafe_allow_html=True)

    # Space for an image
    st.image("images/image.jpg", caption="Agro Smart", use_column_width=True)

    # About the Project Section
    st.markdown("<h2>About the Project</h2>", unsafe_allow_html=True)
    st.write("AgroSmart is a Smart Farming project. Smart farming basically is a data-driven approach to agriculture that uses digital technologies to improve crop yields, reduce costs,and minimize environmental impact. It encompasses a wide range of technologies, in-cluding artificial intelligence (AI), machine learning (ML), remote sensing, and precision agriculture.")
    st.write("AI and ML can be used to develop smart farming tools that can help farmers make informed decisions about crop selection, planting times, irrigation, and pest management. Precision agriculture techniques, such as GPS-guided tractors and variable rate application of fertilizers and pesticides, can help farmers to apply inputs more precisely and efficiently. This can reduce costs and environmental impact, while also improving crop yields.")
    st.write("By combining these technologies, smart farming can help farmers to improve climate resilience and build a more sustainable agricultural sector.")

    # Features Section
    st.markdown("<h2>Features of Agro Smart</h2>", unsafe_allow_html=True)
    st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='grid-item'>
            <img src='https://www.agrivi.com/wp-content/uploads/2017/01/Blog-Soil-Analysis.jpg' alt='Feature'>
            <h4>Soil Analysis</h4>
            <p>Soil quality is a fundamental factor in agriculture, and smart farming leverages AI and ML to optimize soil analysis. </p>
            
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class='grid-item'>
            <img src='https://www.rsipvision.com/wp-content/uploads/2018/12/Farmer-using-tablet-corn-planting.jpg' alt='Feature'>
            <h4>Crop Prediction</h4>
            <p>Machine learning algorithms can find and figure out the right crops that can be planted based on the contents of soil and weather data.</p>
            
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class='grid-item'>
            <img src='https://blog.plantwise.org/wp-content/uploads/sites/7/2022/02/CAI_focusimage-1-1024x622.jpg' alt='Feature'>
            <h4>Crop Health Prediction</h4>
            <p>AI and ML have revolutionized crop health monitoring, enabling real-time detection of diseases, pests, and stress factors. Advanced image recognition and sensor technologies facilitate the early identification of crop issues. </p>
            
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class='grid-item'>
            <img src='https://pureecoindia.in/wp-content/uploads/2021/07/Dry-soil-and-green-landscape-juxtaposition-Pure-Eco-India.jpg' alt='Feature'>
            <h4>Real time Climate Analysis</h4>
            <p>As climate change disrupts traditional weather patterns, smart farming integrates AI and ML for climate change adaptation and crop prediction. These technologies use historical climate data and real-time weather information to forecast growing conditions,</p>
            
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Contact Section
    st.markdown("<h2>Curious to know more?</h2>", unsafe_allow_html=True)
    st.write("Contact the expert.")

    # Create three columns with adjusted widths
    col1, col2, col3 = st.columns((4.2, 1, 4))

    # Place the button in the middle column
    with col2:
        if st.button("Contact Us"):
            page = __import__("pages.contact", fromlist=["page"])
            page.page()
    
    st.markdown("<footer style='display:flex;justify-content:center;padding:40px;color:gray'>2024 Copyrights AgroSmart</footer>", unsafe_allow_html=True)



if __name__ == "__main__":
    main()