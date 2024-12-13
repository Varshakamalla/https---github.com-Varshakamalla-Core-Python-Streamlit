import streamlit as st
st.title("Grades of the students")
project=st.number_input("Enter the project Marks",0,100)
internal=st.number_input("Enter internal marks",0,100)
external=st.number_input("Enter external marks",0,100)
if st.button("Calculate the grade"):
    if project < 50:
        st.warning(f'Failed in project, marks are: {project}')
    if internal < 50:
        st.warning(f'Failed in internal, marks are: {internal}')
    if external < 50:
        st.warning(f'Failed in external, marks are: {external}')
    else:
        total_marks = (70 / 100) * project + (10 / 100) * internal + (20 / 100) * external
        st.success(f'Total score is {total_marks:.2f}')
        if total_marks > 90:
            st.success("A grade")
            st.balloons()
        elif total_marks > 80:
            st.success("B grade")
        elif total_marks > 70:
            st.success("C grade")
        else:
            st.success("Below C grade")