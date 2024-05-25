import streamlit as st

def page():
    # Heading
    st.markdown("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)

    # Placeholder paragraph
    st.write("""
    Agriculture is one of the most critical sector in India. It accounts for around 19.9 percent of India's GDP.AgroSmart is a Smart Farming project. Smart farming basically is a data-driven approach to agriculture that uses digital technologies to improve crop yields, reduce costs, and minimize environmental impact. It encompasses a wide range of technologies, including artificial intelligence (AI), machine learning (ML), remote sensing, and precision agriculture. 
    """)
    st.write("""
    By combining these technologies, smart farming can help farmers to improve climate resilience and build a more sustainable agricultural sector.
    """)

    # Title - Why This Project?
    st.markdown("<h2 style='text-align: center;'>Why This Project?</h2>", unsafe_allow_html=True)
    st.write("""
    As global climate patterns continue to evolve, agriculture faces unprecedented challenges. Climate change severely impacts weather, shifts in seasons, and increased pests. These issues pose a significant threat to crop yield stability and food security in India.
    """)

    # Problem and Its Solution
    st.markdown("<h2 style='text-align: center;'>Problem and Its Solution</h2>", unsafe_allow_html=True)
    st.write("""Over 40 percent of India's crops are wasted before reaching consumers, with a significant portion of this loss attributed to climate factors. This waste undermines India's food security and sustainable development goals.
    Specific Challenges:
    """)
    st.write("""
    1. Climate Variability -  Unpredictable weather patterns, including erratic rainfall, extreme temperatures, and increased pestilence, are disrupting crop cycles and reducing yields.
    """)
    st.write("""2. Lack of Climate-Adaptive Practices - Traditional farming methods are often ill-equipped to handle the challenges posed by climate change, leading to inefficient resource utilization and increased crop losses.
    """)
    st.write("""3. Limited Access to Information and Technology - Smallholder farmers often lack access to real-time weather data, climate forecasts, and tailored agricultural advisories, hindering informed decision-making.
    """)
    st.write("""4. Technology Adoption Barriers - The integration of advanced technologies like AI and machine learning into agricultural practices faces hurdles due to limited digital literacy, infrastructure gaps, and affordability concerns among farmers.    """)
    st.write("""5. Need for Localized Solutions - Diverse agro-climatic conditions across India demand customized solutions that cater to specific regional challenges and crop varieties""")
    st.markdown("<h4 style='text-align: center;'>Scope of the Project</h4>", unsafe_allow_html=True)
    st.write("""
    Development of a smart farming platform that uses AI and ML to provide recommendations for crop selection, planting times, and pest management to smallholder farmers in India. This will involve developing algorithms to analyze real-time weather and climate data, soil analysis, and other relevant factors to generate personalized recommendations for each farmer. 
    """)
    st.write("""
    Evaluation of the effectiveness of the smart farming platform in helping smallholder farmers to improve crop resilience and reduce crop losses due to climate change. This will involve conducting field trials with smallholder farmers to assess the impact of the platform on crop yields, income, and other indicators of resilience.
    """)

    # Contact Us
    st.markdown("<h2 style='text-align: center;'>Meet the Team</h2>", unsafe_allow_html=True)

    # Links to LinkedIn profiles laid down horizontally
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[Ukkasha Farqaleet](https://www.linkedin.com/in/ukkasha-farqaleet-b7449225a/)")
    with col2:
        st.markdown("[Shivanshi Saxena](https://www.linkedin.com/in/shivanshi-saxena12/)")
    with col3:
        st.markdown("[Anjali Choudhary](https://www.linkedin.com/in/anjali-choudhary-67a38a1b9/)")

# Call the function to render the page
# page()
