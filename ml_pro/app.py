import streamlit as st
import pickle
import pandas as pd

# Load the trained model and feature names
with open("model.pkl", "rb") as file:
    model, feature_names = pickle.load(file)

st.title("Sales Prediction App")

# User input fields
ship_mode = st.selectbox("Ship Mode", ["Standard Class", "Second Class", "First Class", "Same Day"])
segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])
region = st.selectbox("Region", ["West", "East", "Central", "South"])
category = st.selectbox("Category", ["Furniture", "Office Supplies", "Technology"])
sub_category = st.selectbox("Sub-Category", ["Bookcases", "Chairs", "Labels", "Tables", "Storage", "Binders"])
postal_code = st.number_input("Postal Code", min_value=10000, max_value=99999, step=1)

# Encode categorical values
label_encoders = {
    "Ship Mode": {"Standard Class": 0, "Second Class": 1, "First Class": 2, "Same Day": 3},
    "Segment": {"Consumer": 0, "Corporate": 1, "Home Office": 2},
    "Region": {"West": 0, "East": 1, "Central": 2, "South": 3},
    "Category": {"Furniture": 0, "Office Supplies": 1, "Technology": 2},
    "Sub-Category": {"Bookcases": 0, "Chairs": 1, "Labels": 2, "Tables": 3, "Storage": 4, "Binders": 5},
}

# Convert user input to numerical format
input_data = pd.DataFrame([[
    label_encoders["Ship Mode"][ship_mode], 
    label_encoders["Segment"][segment], 
    label_encoders["Region"][region], 
    label_encoders["Category"][category], 
    label_encoders["Sub-Category"][sub_category], 
    postal_code
]], columns=feature_names)  # ✅ Use exact feature names from training

# Prediction
if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.write(f"Estimated Sales: **${prediction[0]:.2f}**")
