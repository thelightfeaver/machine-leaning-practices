import joblib
import streamlit as st

model = joblib.load('streamlit/model/salary.pkl')

st.title('Salary Prediction')

data = {
    'unit':{'Finance': 0, 'IT': 1, 'Marketing': 3, 'Operations': 4, 'Web': 5, 'Management': 2},
    'deparment':{'Analyst': 0, 'Senior Analyst': 4, 'Associate': 1, 'Senior Manager': 5, 'Manager': 3, 'Director': 2}
}


experience = st.slider('Experience:', 0, 23, 5)
unit = st.selectbox('Unit:', data['unit'].keys())
deparment = st.selectbox('Department:', data['deparment'].keys())

model_input = [[ data["unit"].get(unit), data['deparment'].get(deparment), experience]]
prediction = model.predict(model_input)
value = prediction[0]
st.markdown(f'## Predicted Salary: {value:,.2f} USD')