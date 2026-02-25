# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:03:42 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

riding_model = pickle.load(open("C:/Users/Lab/Desktop/ML/Riding_model.sav",'rb'))
loan_model = pickle.load(open("C:/Users/Lab/Desktop/ML/loan_model.sav",'rb'))


with st.sidebar:
    selected = option_menu(
        'Classification',['Loan','Riding']
        )

gender_map = {
    'Male':1,
    'Female':0
    }

education_map = {
    'Associate': 0,
    'Bachelor': 1,
    'Doctorate': 2,
    'High School': 3,
    'Master': 4
}

home_map = {
    'MORTGAGE': 0,
    'OTHER': 1,
    'OWN': 2,
    'RENT': 3
}

intent_map = {
    'DEBTCONSOLIDATION': 0,
    'EDUCATION': 1,
    'HOMEIMPROVEMENT': 2,
    'MEDICAL': 3,
    'PERSONAL': 4,
    'VENTURE': 5
}

default_map = {
    'No': 0,
    'Yes': 1
}



if(selected == 'Loan'):
    st.title('Loan Classification')
    
    person_age = st.text_input('person_age')
    person_gender = st.selectbox('person_gender', gender_map)
    person_education = st.selectbox('person_education', education_map)
    person_income = st.text_input('person_income') 
    person_emp_exp = st.text_input('person_emp_exp')
    person_home_ownership = st.selectbox('person_home_ownership', home_map)
    loan_amnt = st.text_input('loan_amnt')
    loan_intent = st.selectbox('loan_intent', intent_map)
    loan_int_rate = st.text_input('loan_int_rate')
    loan_percent_income = st.text_input('loan_percent_income')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist_length')
    credit_score = st.text_input('credit_score')
    previous_loan_defaults_on_file = st.selectbox(
        'previous_loan_defaults_on_file',
        default_map)
    
    loan_prediction = ''
    
    if st.button('Predict'):
        loan_prediction = loan_model.predict([
            [
                float(person_age),
                gender_map[person_gender],
                education_map[person_education],
                float(person_income),
                float(person_emp_exp),
                home_map[person_home_ownership],
                float(loan_amnt),
                intent_map[loan_intent],
                float(loan_int_rate),
                float(loan_percent_income),
                float(cb_person_cred_hist_length),
                float(credit_score),
                default_map[previous_loan_defaults_on_file]
            ]
        ])
        
        if (loan_prediction[0] == 0):
            
          loan_prediction = 'Not Accept'
          
        else:
            
          loan_prediction = 'Accept'
          
    st.success(loan_prediction)

if(selected == 'Riding'):
    st.title('Riding Mower Classification')
    
    Income = st.text_input('รายได้')
    LotSize = st.text_input('พื้นที่บ้าน')
    
    Riding_prediction = ''
    
    if st.button('Predict'):
        Riding_prediction = riding_model.predict([
            [float(Income),float(LotSize)]
        ])
        
        if (Riding_prediction[0] == 0):
            
          Riding_prediction = 'Non Owner'
          
        else:
            
          Riding_prediction = 'Owner'
          
    st.success(Riding_prediction)