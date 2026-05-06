import streamlit as st
import pandas as pd
import os

st.title("BMI analyser")
st.write("Calculate your Body Mass Index easily with this application!")

# Defining functions
def calculate_bmi(weight: float, height: float) -> float:
    return weight / height ** 2

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Class 1 Obesity"
    elif bmi < 40:
        return "Class 2 Obesity"
    else:
        return "Class 3 Obesity"

def convert_imperial_to_metric(weight: float, height: float) -> tuple[float, float]: 
    weight_kg = weight * 0.453592
    height_m = height * 0.0254
    return weight_kg, height_m

def save_to_csv(weight: float, height: float, bmi: float, category: str) -> None:
    file_name = "bmi_results.csv"
    new_data = pd.DataFrame({
        "Weight (kg)": [weight],
        "Height (m)": [height],
        "BMI": [bmi],
        "Category": [category]
    })
    
    # Check if file already exists
    if not os.path.exists(file_name):
        new_data.to_csv(file_name, index=False)
    else:
        new_data.to_csv(file_name, mode="a", header=False, index=False)

# User input section
unit = st.radio("Choose your metric system", ("Imperial", "Metric"))

if unit == "Imperial":
    weight = st.number_input("Input your weight (lbs): ", min_value=1.0, value=150.0)
    height = st.number_input("Input your height (inches): ", min_value=1.0, value=75.0)
    weight, height = convert_imperial_to_metric(weight, height)
else:
    weight = st.number_input("Input your weight (kg): ", min_value=1.0, value=70.0)
    height = st.number_input("Input your height (m): ", min_value=0.5, value=1.75)

if st.button("Calculate BMI"):
    if weight <= 0 or height <= 0:
        st.error("Weight and Height must be greater than 0.")
    else:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        st.success(f"BMI: {bmi:.2f} kg/m²")
        st.info(f"Category: {category}")

        save_to_csv(weight, height, bmi, category)
        st.caption("Results saved to bmi_results.csv")

        # Display results history table
        if os.path.exists("bmi_results.csv"):
            df = pd.read_csv("bmi_results.csv")
            st.write("### History of Results")
            st.dataframe(df)