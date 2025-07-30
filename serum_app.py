import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("serum_predictor_model.pkl")

st.set_page_config(page_title="Smart Serum Predictor", layout="centered")

# App Title
st.title("🌿 Smart Serum Property Predictor")

# Description
st.markdown(
    "Predict the properties of your **silver nanoparticle-infused serum** based on custom inputs. "
    "This is a prototype model for demo purposes."
)

# Input fields
input_1 = st.number_input("Enter value for Feature 1 (e.g., AgNO₃ concentration)", min_value=0.0, step=0.1)
input_2 = st.number_input("Enter value for Feature 2 (e.g., pH level)", min_value=0.0, step=0.1)

# Prediction button
if st.button("🔍 Predict"):
    input_array = np.array([[input_1, input_2]])
    prediction = model.predict(input_array)
    st.success(f"📊 Predicted Property Value: **{prediction[0]:.2f}**")
