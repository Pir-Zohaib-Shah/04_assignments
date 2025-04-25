import streamlit as st
import pandas as pd

st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

height = st.slider("Select your height (cm)", 100, 250, 170)
weight = st.slider("Select your weight (kg)", 30, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

st.write("#### BMI Categories ####")
st.write("- Underweight: BMI lower than 18.50")
st.write("- Normal weight: BMI between 18.50 and 24.90")
st.write("- Overweight: BMI between 25.00 and 29.90")
st.write("- Obesity: BMI 30.00 or higher")

