import streamlit as st
import requests

st.title("Addition App using FastAPI and Streamlit")

# Input fields
num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter second number:", value=0.0, step=0.1)

if st.button("Add Numbers"):
    # Send request to FastAPI backend
    response = requests.post("http://127.0.0.1:8000/add", json={"num1": num1, "num2": num2})
    
    if response.status_code == 200:
        result = response.json()["sum"]
        st.success(f"Result: {result}")
    else:
        st.error("Error communicating with the API.")
