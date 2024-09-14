import streamlit as st
import pickle
import numpy as np

st.title('Heart Disease Prediction')

data_model = pickle.load(open('./heart_model.sav', 'rb'))

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
with col2:
    sex = st.text_input('Sex')
with col3:
    cp = st.text_input('Chest Pain Types')
with col1:
    trestbps = st.text_input('Resting Blood Pressure')
with col2:
    chol = st.text_input('Serum Cholesterol in mg/dL')
with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
with col1:
    restecg = st.text_input('Reasting Electrocardiographic results')
with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')
with col3:
    exang = st.text_input('Exercise Included Angina')
with col1:
    oldpeak = st.text_input('ST depression induced by exercise')
with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')
with col3:
    ca = st.text_input('Major vessels colored by fluorosopy')
with col1:
    thal = st.text_input('thal: 0 =normal; 1 = fixed defective; 2 = reversable defect')

#code for prediction 
#creating button for prediction
heart_diagnosis = ''
if st.button('Heart Disease Test Result'):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    user_input = [float(x) for x in user_input]
    heart_prediction = data_model.predict([user_input])  
    if(heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
st.success(heart_diagnosis)                    