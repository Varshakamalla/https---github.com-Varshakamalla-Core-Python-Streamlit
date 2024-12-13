import streamlit as st
st.title("Shopping Bill")
a=st.number_input("enter your salary",min_value=1)
x=st.number_input("First shopping amount",min_value=1)
y=st.number_input("Second shopping amount",min_value=1)
z=st.number_input("Third shopping amount",min_value=1)
Total=x+y+z
percent=(Total/a)*100
if st.button("submit"):
    st.info(f'The percentage of amount spend on shopping is : {percent}%')