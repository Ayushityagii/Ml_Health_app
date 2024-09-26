import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Set page configuration
st.set_page_config(page_title="Disease Prediction System", layout="wide")

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            "Parkinson's Prediction"],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Header style
st.markdown("<h1 style='text-align: center;'>Disease Prediction Using Machine Learning</h1>", unsafe_allow_html=True)

def diabetes_prediction():
    st.subheader('Diabetes Prediction')
    
    # User input form
    with st.form(key='diabetes_form'):
        input_fields = {
            "Pregnancies": "Number of Pregnancies",
            "Glucose": "Glucose Level",
            "BloodPressure": "Blood Pressure value",
            "SkinThickness": "Skin Thickness value",
            "Insulin": "Insulin Level",
            "BMI": "BMI value",
            "DiabetesPedigreeFunction": "Diabetes Pedigree Function value",
            "Age": "Age of the Person"
        }
        
        user_input = []
        for label, placeholder in input_fields.items():
            user_input.append(st.number_input(placeholder, min_value=0.0, format="%.2f"))

        # Submit button
        submit_button = st.form_submit_button(label='Predict Diabetes')

        if submit_button:
            diab_prediction = diabetes_model.predict([user_input])
            diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diagnosis)

def heart_disease_prediction():
    st.subheader('Heart Disease Prediction')

    # User input form
    with st.form(key='heart_form'):
        heart_input_fields = {
            "age": "Age",
            "sex": "Sex (1 = Male; 0 = Female)",
            "cp": "Chest Pain types",
            "trestbps": "Resting Blood Pressure",
            "chol": "Serum Cholesterol in mg/dl",
            "fbs": "Fasting Blood Sugar > 120 mg/dl",
            "restecg": "Resting Electrocardiographic results",
            "thalach": "Maximum Heart Rate achieved",
            "exang": "Exercise Induced Angina (1 = Yes; 0 = No)",
            "oldpeak": "ST depression induced by exercise",
            "slope": "Slope of the peak exercise ST segment",
            "ca": "Major vessels colored by fluoroscopy",
            "thal": "Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect"
        }

        heart_user_input = []
        for label, placeholder in heart_input_fields.items():
            heart_user_input.append(st.number_input(placeholder, min_value=0))

        # Submit button
        submit_button = st.form_submit_button(label='Predict Heart Disease')

        if submit_button:
            heart_prediction = heart_disease_model.predict([heart_user_input])
            diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(diagnosis)

def parkinsons_prediction():
    st.subheader("Parkinson's Disease Prediction")

    # User input form
    with st.form(key='parkinsons_form'):
        parkinsons_input_fields = {
            "fo": "MDVP:Fo(Hz)",
            "fhi": "MDVP:Fhi(Hz)",
            "flo": "MDVP:Flo(Hz)",
            "Jitter_percent": "MDVP:Jitter(%)",
            "Jitter_Abs": "MDVP:Jitter(Abs)",
            "RAP": "MDVP:RAP",
            "PPQ": "MDVP:PPQ",
            "DDP": "Jitter:DDP",
            "Shimmer": "MDVP:Shimmer",
            "Shimmer_dB": "MDVP:Shimmer(dB)",
            "APQ3": "Shimmer:APQ3",
            "APQ5": "Shimmer:APQ5",
            "APQ": "MDVP:APQ",
            "DDA": "Shimmer:DDA",
            "NHR": "NHR",
            "HNR": "HNR",
            "RPDE": "RPDE",
            "DFA": "DFA",
            "spread1": "spread1",
            "spread2": "spread2",
            "D2": "D2",
            "PPE": "PPE"
        }

        parkinsons_user_input = []
        for label, placeholder in parkinsons_input_fields.items():
            parkinsons_user_input.append(st.number_input(placeholder, min_value=0.0, format="%.2f"))

        # Submit button
        submit_button = st.form_submit_button(label="Predict Parkinson's Disease")

        if submit_button:
            parkinsons_prediction = parkinsons_model.predict([parkinsons_user_input])
            diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(diagnosis)

# Call the appropriate prediction function based on user selection
if selected == 'Diabetes Prediction':
    diabetes_prediction()
elif selected == 'Heart Disease Prediction':
    heart_disease_prediction()
elif selected == "Parkinson's Prediction":
    parkinsons_prediction()

# Footer
st.markdown("<footer style='text-align: center; margin-top: 50px;'><p>Made with ❤️ by Ayushi Tyagi</p></footer>", unsafe_allow_html=True)


