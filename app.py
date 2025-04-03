import streamlit as st
import joblib
clf=joblib.load('loan_data1 (3).joblib')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Martial status 0:no 1:yes')
ai=st.number_input('Enter Applicant Income in thousands')
la=st.number_input('Enter Loan amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,aif,la]])
    if prediction=='y':
        st.text('Loan is approved')
    else:
        st.text('Loan is rejected')
