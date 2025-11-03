import streamlit as st

# ============================
# 🧮 Simple Calculator App
# ============================

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations using Streamlit.")

# Input fields
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Choose operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
