import streamlit as st
import pandas as pd
st.title("StreamLit ")
st.header("Stremlit Practise")
st.subheader("Form")
name=st.text_input("Enter your name:")

if name:
  st.write(f"Hello {name}")

age= st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}")

options=["Python","Java","C++","Javascript"]
choice=st.selectbox("Choose your favorite language:",options)
st.write(f"Your selected {choice}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
st.write(df)
df.to_csv("./sample_data.csv")

uploaded_file=st.file_uploader("Choose a CSV File",type="csv")
if(uploaded_file is not None):
  st.write(pd.read_csv(uploaded_file))
  

