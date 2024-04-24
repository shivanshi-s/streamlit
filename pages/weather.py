import streamlit as st
import pyowm

# Your OpenWeatherMap API key
api_key = 'a8994b7a3a45753f99d9a2131cf06848'
owm = pyowm.OWM(api_key)

# Create a weather manager instance
mgr = owm.weather_manager()

def display_weather(city):
    obs = mgr.weather_at_place(city)
    weather = obs.weather
    st.write(f"### Weather in {city}")
    st.write(f"#### Temperature: {weather.temperature('celsius')['temp']}°C")
    st.write(f"#### Description: {weather.detailed_status}")
    st.write(f"#### Wind Speed: {weather.wind()['speed']} m/s")

def page():
    st.title("India Weather App")
    # Provide a unique key for the text input widget
    city = st.text_input('Enter a city name:', 'New Delhi, IN', key='unique_city_input')
    if st.button('Get Weather', key='unique_get_weather_button'):
        display_weather(city)

# Call the page function to render the app
# page()
