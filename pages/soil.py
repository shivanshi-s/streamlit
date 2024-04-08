import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model and scalers
model = pickle.load(open('soil_analysis/model.pkl', 'rb'))
sc = pickle.load(open('soil_analysis/standscaler.pkl', 'rb'))
ms = pickle.load(open('soil_analysis/minmaxscaler.pkl', 'rb'))

# Create a dictionary to map the crop IDs to their names
crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
             7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
             12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
             17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
             21: "Chickpea", 22: "Coffee"}

def recommend_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    # Create the feature list
    feature_list = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]

    # Scale the input features
    single_pred = np.array(feature_list).reshape(1, -1)
    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)

    # Make the prediction
    prediction = model.predict(final_features)

    # Determine the recommended crop
    if prediction[0] in crop_dict:
        recommended_crop = crop_dict[prediction[0]]
    else:
        recommended_crop = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    return recommended_crop

def page():
    st.title("Soil Analysis and Crop Recommendation")

    # Input fields
    nitrogen = st.number_input("Nitrogen", min_value=0.0, step=1)
    phosphorus = st.number_input("Phosphorus", min_value=0.0, step=1)
    potassium = st.number_input("Potassium", min_value=0.0, step=1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, step=1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, step=1)
    ph = st.number_input("pH", min_value=0.0, step=1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1)

    if st.button("Analyze and Recommend"):
        recommended_crop = recommend_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
        st.write(f"The recommended crop is: {recommended_crop}")

# if __name__ == "__main__":
#     main()