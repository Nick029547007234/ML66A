# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:03:42 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

riding_model = pickle.load(open("Riding_model.sav",'rb'))
loan_model = pickle.load(open("loan_model.sav",'rb'))
bmi_model = pickle.load(open("bmi_model.sav",'rb'))


with st.sidebar:
    selected = option_menu(
        'Classification',['Loan','Riding','BMI']
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

if selected == 'BMI':
    st.title('BMI Classification')
    
    # รับค่า Input 3 ตัว
    # หมายเหตุ: ต้องแน่ใจว่ามีการประกาศ gender_map ไว้ก่อนหน้า เช่น gender_map = {'Male': 0, 'Female': 1}
    person_gender = st.selectbox('Gender', gender_map.keys())
    person_height = st.text_input('Height (cm)')
    person_weight = st.text_input('Weight (kg)')
    
    bmi_result = ''
    
    if st.button('Predict'):
        try:
            # นำค่าทั้ง 3 ไปเข้าโมเดล (เปลี่ยนชื่อจาก loan_model เป็น bmi_model)
            # ลำดับของ Input ต้องตรงกับตอนที่คุณเทรนโมเดลมา
            prediction = bmi_model.predict([
                [
                    gender_map[person_gender],
                    float(person_height),
                    float(person_weight)
                ]
            ])
            
            # แปลงผลลัพธ์การทำนาย (ปรับแก้ตัวเลขและข้อความให้ตรงกับคลาสที่คุณเทรนมา)
            if prediction[0] == 0:
                bmi_result = 'Underweight (น้ำหนักต่ำกว่าเกณฑ์)'
            elif prediction[0] == 1:
                bmi_result = 'Normal (น้ำหนักปกติ)'
            elif prediction[0] == 2:
                bmi_result = 'Overweight (ท้วม)'
            else:
                bmi_result = 'Obese (อ้วน)'
                
            st.success(bmi_result)
            
        except ValueError:
            # ป้องกันกรณีผู้ใช้งานกรอกตัวหนังสือลงในช่องน้ำหนัก/ส่วนสูง
            st.error("กรุณากรอกข้อมูล Height และ Weight เป็นตัวเลข")




