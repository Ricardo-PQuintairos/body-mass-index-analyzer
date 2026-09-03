import pandas as pd
import os
import sqlite3
from datetime import datetime

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
   
def database_creation(db_name = "bmi_data.db"):
    conn = sqlite3.connect(db_name)
    conn.execute("""CREATE TABLE if NOT EXISTS bmi_results (
      Name TEXT,
      Weight REAL,
      Height REAL,
      Bmi REAL,
     Category TEXT,
     Timestamp TEXT
    )""")
    return conn

def load_user_history(conn, name):
    query = "SELECT * FROM bmi_results WHERE Name = ?"
    return pd.read_sql_query(query, conn, params= (name,))

def save_entry(conn, name, weight, height, bmi, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("""INSERT INTO bmi_results (Name, Weight, Height, Bmi, Category, Timestamp)
       VALUES(?,?,?,?,?,?)""" params= (Name, Weight, Height, Bmi, Category, Timestamp))

# User input/output
while True:
    try:
        unit = input("Choose unit system: [M]etric (kg, m) or [I]mperial (lbs, inches): ").lower()
        if unit == "i":
            weight = float(input("Enter your weight (lbs): "))
            height = float(input("Enter your height (inches): "))
            
            weight, height = convert_imperial_to_metric(weight, height)
        
        elif unit == "m":
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))

        else:
            print("Invalid unit system. Please choose 'M' for Metric or 'I' for Imperial.\n")
            continue
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be greater than 0\n")
            continue
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nBMI: {bmi:.2f} kg/m²")
        print(f"Category: {category}\n")
        
        # Saving data
        save_bmi_to_csv(weight, height, bmi, category)  
        print("Data saved as csv file in bmi_results.csv")

        # Displaying History of results
        if os.path.exists("bmi_results.csv"):
            df = pd.read_csv("bmi_results.csv")
            print("\nHistory of results: ")
            print(df.to_string(), "\n")

    # Error exception
    except ValueError:
        print("Invalid input. Please enter numeric inputs only.\n")
        continue
   
    # Menu 
    choice = input("Press [R] to repeat or [E] to exit: ").lower()
    
    if choice == "e":
        print("Leaving application.")
        break
    elif choice == "r":
        continue
    else:
        print("Invalid input.\n")
        continue