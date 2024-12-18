import streamlit as st

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit App
def calculator():
    st.title("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")
    
    # Dropdown for selecting operation
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))
    
    # Performing the operation based on user choice
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    # Display the result
    st.write(f"Result: {result}")

if __name__ == "__main__":
    calculator()
