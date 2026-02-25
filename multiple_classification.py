# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:03:42 2026
@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# --- Load Models ---
# อย่าลืมตรวจสอบชื่อไฟล์ model ของ BMI ให้ถูกต้องนะครับ
riding_model = pickle.load(open("Riding_model.sav", 'rb'))
loan_model = pickle.load(open("loan_model.sav", 'rb'))
bmi_model = pickle.load(open("bmi_model.sav", 'rb')) # เพิ่มการโหลด model BMI

# --- Sidebar Menu ---
with st.sidebar:
    selected = option_menu(
        'Classification', ['Loan', 'Riding', 'BMI']
    )

# --- Mappings ---
gender_map = {'Male': 1, 'Female': 0}

education_map = {
    'Associate': 0, 'Bachelor': 1, 'Doctorate': 2,
    'High School': 3, 'Master': 4
}

home_map = {'MORTGAGE': 0, 'OTHER': 1, 'OWN': 2, 'RENT': 3}

intent_map = {
    'DEBTCONSOLIDATION': 0, 'EDUCATION': 1, 'HOMEIMPROVEMENT': 2,
    'MEDICAL': 3, 'PERSONAL': 4, 'VENTURE': 5
}

default_map = {'No': 0, 'Yes': 1}

# --- BMI Section (แก้ไขตามรูปภาพ: ไม่เอา Index เป็น Input) ---
if selected == 'BMI':
    st.title('BMI Classification')
    
    # รับค่าเพียง 3 อย่างตามตาราง (Gender, Height, Weight)
    person_gender = st.selectbox('Gender', list(gender_map.keys()))
    person_height = st.text_input('Height (cm)')
    person_weight = st.text_input('Weight (kg)')
    
    bmi_prediction_result = ''

    if st.button('Predict BMI'):
        try:
            # เตรียมข้อมูล Input (แปลง Gender เป็นตัวเลข)
            input_data = [
                gender_map[person_gender],
                float(person_height),
                float(person_weight)
            ]
            
            # ทำนายผล (ผลลัพธ์ที่ได้คือค่า Index 0-5)
            prediction = bmi_model.predict([input_data])
            
            # แปลงค่า Index เป็นข้อความอธิบาย (อ้างอิงตามมาตรฐาน BMI Index)
            bmi_labels = {
                0: "Extremely Weak",
                1: "Weak",
                2: "Normal",
                3: "Overweight",
                4: "Obesity",
                5: "Extreme Obesity"
            }
            
            bmi_prediction_result = bmi_labels.get(prediction[0], f"Index: {prediction[0]}")
            st.success(f'Prediction Result: {bmi_prediction_result}')
            
        except ValueError:
            st.error("กรุณากรอกตัวเลขในช่องส่วนสูงและน้ำหนัก")

# --- Loan Section ---
if selected == 'Loan':
    st.title('Loan Classification')
    person_age = st.text_input('person_age')
    person_gender = st.selectbox('person_gender', list(gender_map.keys()))
    person_education = st.selectbox('person_education', list(education_map.keys()))
    person_income = st.text_input('person_income') 
    person_emp_exp = st.text_input('person_emp_exp')
    person_home_ownership = st.selectbox('person_home_ownership', list(home_map.keys()))
    loan_amnt = st.text_input('loan_amnt')
    loan_intent = st.selectbox('loan_intent', list(intent_map.keys()))
    loan_int_rate = st.text_input('loan_int_rate')
    loan_percent_income = st.text_input('loan_percent_income')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist_length')
    credit_score = st.text_input('credit_score')
    previous_loan_defaults_on_file = st.selectbox('previous_loan_defaults_on_file', list(default_map.keys()))

    if st.button('Predict Loan'):
        loan_prediction = loan_model.predict([[
            float(person_age), gender_map[person_gender], education_map[person_education],
            float(person_income), float(person_emp_exp), home_map[person_home_ownership],
            float(loan_amnt), intent_map[loan_intent], float(loan_int_rate),
            float(loan_percent_income), float(cb_person_cred_hist_length),
            float(credit_score), default_map[previous_loan_defaults_on_file]
        ]])
        
        result = 'Accept' if loan_prediction[0] == 1 else 'Not Accept'
        st.success(result)

# --- Riding Section ---
if selected == 'Riding':
    st.title('Riding Mower Classification')
    Income = st.text_input('รายได้')
    LotSize = st.text_input('พื้นที่บ้าน')

    if st.button('Predict Riding'):
        riding_pred = riding_model.predict([[float(Income), float(LotSize)]])
        result = 'Owner' if riding_pred[0] == 1 else 'Non Owner'
        st.success(result)


