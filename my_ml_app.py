import pandas as pd
import numpy as np
import joblib
import time
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #ccccb3;
    color:#ff0000;
    }
div.stHeader {
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)


model = joblib.load('pipeline.joblib')

st.markdown(f'<h1 style="color:#bf8040;font-size:44px;">{"PREDICT YOUR MEDICAL INSURANCE COST HERE..."}</h1>', unsafe_allow_html=True)
# st.title('PREDICT YOUR MEDICAL INSURANCE COST HERE...')
st.subheader('Please enter yours Details:')
col1, col2 = st.columns(2)
with col1:
    age = st.text_input("ENTER AGE",placeholder="Enter your Age")
with col2:
    bmi = st.text_input("ENTER BMI",placeholder="Enter your BMI value")
region = st.selectbox("SELECT REGION",('Northeast','Northwest','Southeast','Southwest'))
children = st.text_input("NO. OF CHILDREN",placeholder="Enter the number of children you have")
col3, col4 = st.columns(2)
with col3:
    gender = st.radio("SELECT GENDER",('Male','Female'))
with col4:
    smoke = st.radio("SMOKING HABIT",('Yes','No'),index=1)
agree = st.checkbox('I agree to the Terms and Conditions')
st.subheader('  ')
st.subheader('  ')
button = st.button('GET AMOUNT')
if age.isdigit() and bmi and children.isdigit() and agree and button:
    with st.spinner('Please wait...we are generating the result'):
        time.sleep(3)
    st.success('Successfully generated the result!!!')
    northeast = northwest = southeast = southwest = 0
    if region == 'Northeast':
       northeast = 1
    elif region == 'Northwest':
        northwest = 1
    elif region == 'Southeast':
        southeast = 1
    elif region == 'Southwest':
        southwest = 1
    if gender=='Male':
        gen = 1
    else:
        gen = 0
    if smoke == 'Yes':
        smoker = 1
    else:
        smoker = 0

    inputs = [int(age),float(bmi),int(children),northeast,northwest,southeast,southwest,smoker,gen]
    output = model.predict([inputs])
    st.subheader('  ')
    col5, col6 = st.columns(2)
    with col5:
        st.write("YOUR PREDICTED INSURANCE AMOUNT IS: ")
    op = "$ %.2f"%(output[0])
    with col6:
        st.subheader(op)
    st.balloons()
else:
    if button:
        st.warning('Please enter all the fields correctly!!')
    else:
        st.write('  ')
with st.sidebar:
    st.subheader('MENU')
    with st.expander("CONTACT US",expanded=0):
        st.subheader('  ')
        st.text("Reach us at")
        st.text("E-mail: predict.cost@co.in")
        st.text("Mobile: +91 9078922310")
    with st.expander("ABOUT US",expanded=1):
        st.subheader('  ')
        st.text("We provide the best amount of ")
        st.text("insurance prediction for you...")
        st.image("team.jpg")