# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Function to load the pre-trained model
def load_model():
    # Load the pre-trained model from the pickle file
    with open('Loan Status predictions.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Streamlit app
def main():
    with open('Loan Status predictions.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    st.title('Loan Status Prediction App')

    st.sidebar.header('User Input Features')

    # Collect user input
    married = st.sidebar.selectbox('Married', ['Yes', 'No'])
    education = st.sidebar.selectbox('Education', ['Graduate', 'Not Graduate'])
    applicant_income = st.sidebar.number_input('Applicant Income')
    coapplicant_income = st.sidebar.number_input('Coapplicant Income')
    loan_amount = st.sidebar.number_input('Loan Amount')
    credit_history = st.sidebar.selectbox('Credit History', [0, 1])
    property_area = st.sidebar.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

    # Make prediction
    input_data = {
        'Married': [married],
        'Education': [education],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    }

    input_df = pd.DataFrame(input_data)

    # Preprocess user input
    input_df = pd.get_dummies(input_df, columns=['Married', 'Education', 'Property_Area'], drop_first=True)

    # Make prediction
    prediction = model.predict(input_df)

    # Display prediction
    st.subheader('Prediction')
    st.write(f'The loan status is predicted to be: {prediction[0]}')

if __name__ == '__main__':
    main()
