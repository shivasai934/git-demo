import streamlit as st

a = st.number_input("Enter the first number :")
b = st.number_input("Enter the second number :")
c = a+b
if st.button("Calculate"):
    st.header("The sum of  and b is: "+str(c))