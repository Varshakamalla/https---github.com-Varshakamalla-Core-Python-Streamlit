import streamlit as st
st.title("Gross Salary calculator")
basic_salary=st.number_input("Enter your Basic Salary",min_value=1,step=1)
if st.button("Calculate gross Salary"):
    hra=0
    da=0
    if basic_salary<1000:
        hra = (67 / 100) * basic_salary
        da = (73 / 100) * basic_salary
    elif 10000 <= basic_salary <= 20000:
        hra = (69 / 100) * basic_salary
        da = (76 / 100) * basic_salary
    else:
        hra = (73 / 100) * basic_salary
        da = (89 / 100) * basic_salary
    gs = hra + da + basic_salary
    st.write("The gross salary is : ",gs)