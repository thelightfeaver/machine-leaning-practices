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

st.title(f'The current temperature is {temperature} 🌡️')
st.markdown(f"""
    ### Weather: {(prediction[0])}
""")