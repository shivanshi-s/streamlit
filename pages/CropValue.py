import streamlit as st

def page():
    # Page title
    st.title('Crop Value Analysis')

    # Input fields for crop value analysis
    crop_type = st.selectbox('Select Crop Type', ['Corn', 'Wheat', 'Soybeans', 'Rice'])
    disease_scale = st.slider('Crop Health Scale (1-100)', 1, 100) # Scale for disease
    rainfall = st.slider('Rainfall (in inches)', 0, 50)
    soil_type = st.selectbox('Soil Type', ['Loamy', 'Clay', 'Sandy', 'Limestone'])

    # Dummy analysis function
    def analyze_crop_value(disease_scale, rainfall):
    
        base_value = 10 # Base value in rupees
        disease_factor = 100 - disease_scale # Higher disease scale means lower value
        rainfall_factor = 1 + (rainfall / 100) # Higher rainfall means lower value 
        value = base_value * disease_factor * rainfall_factor
        return value

    # Button to trigger analysis
    if st.button('Analyze Crop Value'):
        # Perform dummy analysis
        predicted_value = analyze_crop_value(disease_scale, rainfall)
        
        st.markdown(f'<p style="font-size: 24px; color: #FFEC9E; font-weight: bold;">Predicted Crop Value: ₹{predicted_value:,.2f}</p>', unsafe_allow_html=True)


    st.markdown("<footer style='display:flex;justify-content:center;padding:40px;color:gray'>2024 Copyrights AgroSmart</footer>", unsafe_allow_html=True)