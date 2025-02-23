
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Stroke Predictor")

# input widget for getting user values for X (feature matrix value)
age = st.slider("age", min_value=0, max_value=100, value=0)
bmi = st.slider("bmi", min_value=0, max_value=100, value=10)
avg_glucose_level = st.slider("avg_glucose_level", min_value=0, max_value=500, value=50)

# After selecting stroke, the user then submits the stroke value
if st.button("Predict"):
  # take the stroke value, and format the value the right way
    prediction = model.predict([[age, bmi, avg_glucose_level]])[0].round(0)
  # Map the prediction to the corresponding message
  # Show result
    if prediction == 1: 
        st.success("**Stroke**")
    else:
        st.error("**No Stroke**")

# Display the result on the Streamlit app
st.write("The predicted stroke status is", {prediction})
