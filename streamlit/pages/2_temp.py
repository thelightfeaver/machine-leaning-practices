import joblib
import streamlit as st


model = joblib.load("streamlit/model/temp.pkl")

st.title("Celsius to Fahrenheit 🌡️")
temperature = st.slider("Temperature", 0, 100, 25)

if st.button("Convert"):
    prediction = model.predict([[temperature]])
    st.markdown(
        f"""
        ### Conversion: {round(prediction[0][0])} °F
    """
    )
