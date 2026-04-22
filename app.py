import streamlit as st
import requests

st.title("calculator using API")

a=st.number_input("Enter A")
b=st.number_input("Enter B")

if st.button("Add"):
    res=requests.get(f"http://127.0.0.1:8000/add?a={a}&b={b}")
    st.write(res.json())