import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load trained model
model = joblib.load(r"C:\Users\navya\Documents\rainfall\models\cat.pkl")

# Function to get user input via Streamlit
def get_user_input():
    # DATE
    date = st.text_input('Enter Date (YYYY-MM-DD)', '2024-09-09')
    try:
        day = float(pd.to_datetime(date).day)
        month = float(pd.to_datetime(date).month)
    except:
        st.error("Invalid date format. Please use YYYY-MM-DD.")
        return None

    # Numeric Features
    MinTemp = st.number_input('MinTemp', 0.0, 50.0, 13.4)
    MaxTemp = st.number_input('MaxTemp', 0.0, 50.0, 22.9)
    Rainfall = st.number_input('Rainfall', 0.0, 500.0, 0.6)
    Evaporation = st.number_input('Evaporation', 0.0, 50.0, 2.4)
    Sunshine = st.number_input('Sunshine', 0.0, 15.0, 8.3)
    WindGustSpeed = st.number_input('WindGustSpeed', 0.0, 200.0, 44.0)
    WindSpeed9am = st.number_input('WindSpeed9am', 0.0, 100.0, 20.0)
    WindSpeed3pm = st.number_input('WindSpeed3pm', 0.0, 100.0, 24.0)
    Humidity9am = st.number_input('Humidity9am', 0.0, 100.0, 71.0)
    Humidity3pm = st.number_input('Humidity3pm', 0.0, 100.0, 22.0)
    Pressure9am = st.number_input('Pressure9am', 900.0, 1100.0, 1007.7)
    Pressure3pm = st.number_input('Pressure3pm', 900.0, 1100.0, 1007.1)
    Temp9am = st.number_input('Temp9am', 0.0, 50.0, 16.9)
    Temp3pm = st.number_input('Temp3pm', 0.0, 50.0, 21.8)
    Cloud9am = st.number_input('Cloud9am', 0.0, 10.0, 8.0)
    Cloud3pm = st.number_input('Cloud3pm', 0.0, 10.0, 0.0)

    # Categorical Features
    Location = st.text_input('Location', 'SomeLocation')  # Assuming this is categorical
    WindDir9am = st.selectbox('WindDir9am', ['N', 'S', 'E', 'W'])
    WindDir3pm = st.selectbox('WindDir3pm', ['N', 'S', 'E', 'W'])
    WindGustDir = st.selectbox('WindGustDir', ['N', 'S', 'E', 'W'])
    RainToday = st.selectbox('RainToday', ['True', 'False'])

    # Creating a DataFrame from the input
    data = {
        'MinTemp': MinTemp, 'MaxTemp': MaxTemp, 'Rainfall': Rainfall, 
        'Evaporation': Evaporation, 'Sunshine': Sunshine, 'WindGustSpeed': WindGustSpeed, 
        'WindSpeed9am': WindSpeed9am, 'WindSpeed3pm': WindSpeed3pm, 'Humidity9am': Humidity9am, 
        'Humidity3pm': Humidity3pm, 'Pressure9am': Pressure9am, 'Pressure3pm': Pressure3pm, 
        'Temp9am': Temp9am, 'Temp3pm': Temp3pm, 'Cloud9am': Cloud9am, 'Cloud3pm': Cloud3pm,
        'Location': Location, 'WindDir9am': WindDir9am, 'WindDir3pm': WindDir3pm, 
        'WindGustDir': WindGustDir, 'RainToday': RainToday
    }

    return pd.DataFrame([data])

# Main function
def main():
    st.title("Rainfall Prediction")

    # Get user input
    user_input = get_user_input()

    # Check if input is valid
    if user_input is not None:
        # Show user input
        st.subheader('User Input:')
        st.write(user_input)

        # Add "Predict" button
        if st.button('Predict'):
            # Handle categorical features (dummy encoding, etc.)
            # Assuming the model was trained with dummy encoded features
            user_input_processed = pd.get_dummies(user_input)  # Adjust this based on your preprocessing during training

            try:
                # Predict and show the result
                prediction = model.predict(user_input_processed)

                # Show prediction result
                if prediction[0] == 0:
                    st.success("Prediction: No Rain Tomorrow (Sunny)")
                else:
                    st.warning("Prediction: Rain Tomorrow")
            except Exception as e:
                st.error(f"Error during prediction: {e}")

# Run the app
if __name__ == '__main__':
    main()
