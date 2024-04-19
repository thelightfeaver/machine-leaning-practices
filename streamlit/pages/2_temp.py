import streamlit as st
import joblib



model = joblib.load('streamlit/model/temp.pkl')

temperature = st.sidebar.slider('Temperature', 0, 100, 25)

prediction = model.predict([[temperature]])

st.title(f'The current temperature is {temperature}°C 🌡️')
st.markdown(f"""
    ### Convertion {round(prediction[0][0]) } °H
""")





