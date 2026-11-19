
import streamlit as st

# Main title
st.title("Employee Management Dashboard")

# Sidebar
st.sidebar.title("Employee Details")

name = st.sidebar.text_input("Enter Employee Name")

age = st.sidebar.number_input(
    "Enter Age", min_value=18, max_value=60
)

department = st.sidebar.selectbox(
    "Select Department",
    ["IT", "HR", "Finance", "Sales"]
)

# Checkbox
active = st.checkbox("Employee is currently active")

# Button
if st.button("Submit"):

    if name:
        st.success("Employee Details Submitted!")

        st.subheader("Employee Information")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Department:", department)
        st.write("Active Status:", active)

    else:
        st.error("Please enter employee name")
