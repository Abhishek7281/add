import streamlit as st

def add_numbers(num1, num2):
    return num1 + num2

# Streamlit app layout
st.title("Add Two Numbers")

# Input fields for user to enter numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Button to perform addition
if st.button("Add"):
    result = add_numbers(num1, num2)
    st.success(f"The sum of {num1} and {num2} is: {result}")

# HTML code for additional formatting
st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;
        }
        .stButton {
            color: #ffffff;
            background-color: #4CAF50;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        .stButton:hover {
            background-color: #45a049;
        }
        .stNumberInput {
            width: 200px;
        }
    </style>
""", unsafe_allow_html=True)
