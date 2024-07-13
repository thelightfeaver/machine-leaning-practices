import streamlit as st
import joblib

model = joblib.load('streamlit/model/weather.pkl')

temperature = st.sidebar.slider('Temperature', -23.3, 33.0)
dewpoint = st.sidebar.slider('Dewpoint', -28.5, 24.4)
humidity = st.sidebar.slider('Humidity',18, 100)
windspeed = st.sidebar.slider('Windspeed', 0, 83)
visibility = st.sidebar.slider('Visibility', 0.2, 48.3)
pressure = st.sidebar.slider('Pressure', 97, 103)


prediction = model.predict([[temperature, 
                             dewpoint, 
                             humidity, 
                             windspeed, 
                             visibility, 
                             pressure]])
weather_data = {
    "Mainly Clear": "🌤️",
    "Mostly Cloudy": "☁️",
    "Cloudy": "🌥️",
    "Clear": "☀️",
    "Snow": "❄️",
    "Rain": "🌧️",
    "Rain Showers": "🌦️",
    "Fog": "🌫️",
    "Rain,Fog": "🌧️🌫️",
    "Drizzle,Fog": "🌦️🌫️",
    "Snow Showers": "🌨️",
    "Drizzle": "🌦️",
    "Snow,Fog": "❄️🌫️",
    "Snow,Blowing Snow": "❄️💨",
    "Rain,Snow": "🌧️❄️",
    "Thunderstorms,Rain Showers": "⛈️🌦️",
    "Haze": "🌫️",
    "Drizzle,Snow,Fog": "🌦️❄️🌫️",
    "Freezing Rain": "🌧️❄️",
    "Freezing Drizzle,Snow": "🌦️❄️",
    "Freezing Drizzle": "🌦️❄️",
    "Snow,Ice Pellets": "❄️🌨️",
    "Freezing Drizzle,Fog": "🌦️❄️🌫️",
    "Snow,Haze": "❄️🌫️",
    "Freezing Fog": "❄️🌫️",
    "Snow Showers,Fog": "🌨️❄️🌫️",
    "Moderate Snow": "🌨️❄️",
    "Rain,Snow,Ice Pellets": "🌧️❄️🌨️",
    "Freezing Rain,Fog": "🌧️❄️🌫️",
    "Freezing Drizzle,Haze": "🌦️❄️🌫️",
    "Rain,Haze": "🌧️🌫️",
    "Thunderstorms,Rain": "⛈️🌧️",
    "Thunderstorms,Rain Showers,Fog": "⛈️🌦️🌫️",
    "Freezing Rain,Haze": "🌧️❄️🌫️",
    "Drizzle,Snow": "🌦️❄️",
    "Rain Showers,Snow Showers": "🌦️❄️",
    "Thunderstorms": "⛈️",
    "Moderate Snow,Blowing Snow": "🌨️❄️💨",
    "Rain Showers,Fog": "🌦️🌫️",
    "Thunderstorms,Moderate Rain Showers,Fog": "⛈️🌦️🌫️",
    "Snow Pellets": "❄️🌨️",
    "Rain,Snow,Fog": "🌧️❄️🌫️",
    "Moderate Rain,Fog": "🌧️🌫️",
    "Freezing Rain,Ice Pellets,Fog": "🌧️❄️🌨️🌫️",
    "Drizzle,Ice Pellets,Fog": "🌦️🌨️🌫️",
    "Thunderstorms,Rain,Fog": "⛈️🌧️🌫️",
    "Rain,Ice Pellets": "🌧️🌨️",
    "Rain,Snow Grains": "🌧️❄️",
    "Thunderstorms,Heavy Rain Showers": "⛈️🌧️🌦️",
    "Freezing Rain,Snow Grains": "🌧️❄️"
}


st.title('Weather Prediction')
emoji = weather_data[prediction[0]]

st.title(f'The current temperature is {temperature} 🌡️')
st.markdown(f"""
    ### Weather: {(prediction[0])} {emoji}
""")