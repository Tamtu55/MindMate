import streamlit as st
import pandas as pd
import pickle

# Load the trained model
pickle_in = open("synthetic.pkl", "rb")
classifier = pickle.load(pickle_in)

# Function to make predictions
def predict_mental_health(Gender, Age, Screentime, Most_used_App, Emotional_Support, Self_Care, Anxiety, Panic_Attack):
    # Preprocessing user input
    Gender_encoded = 1 if Gender == "Female" else 0
    Most_used_App_encoded = 1 if Most_used_App == "Youtube" else 0
    Self_Care_encoded = 1 if Self_Care == "Yes" else 0
    
    # Making predictions
    prediction = classifier.predict([[Gender_encoded, Age, Screentime, Most_used_App_encoded, Emotional_Support, Self_Care_encoded, Anxiety, Panic_Attack]])
    return "You are absolutely Fine" if prediction[0] == 1 else "No You are not fine"

# Streamlit app code
def main():
    st.title("Mental Health Prediction")

    # Input fields for user to input data
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=0, max_value=150, value=25)
    Screentime = st.number_input("Screentime (hours per day)", min_value=0, value=0)
    Most_used_App = st.selectbox("Most used App", ["Chrome", "Youtube"])
    Emotional_Support = st.slider("Emotional Support (1-10)", min_value=1, max_value=10, value=5)
    Self_Care = st.selectbox("Self Care", ["Yes", "No"])
    Anxiety = st.number_input("Anxiety (0 or 1)", min_value=0, max_value=1, value=0)
    Panic_Attack = st.number_input("Panic Attack (0 or 1)", min_value=0, max_value=1, value=0)
    
    result = ""
    if st.button("Predict"):
        result = predict_mental_health(Gender, Age, Screentime, Most_used_App, Emotional_Support, Self_Care, Anxiety, Panic_Attack)
        st.success(f"The predicted mental health status is: {result}")

    if st.button("About"):
        st.text("This is a Streamlit app for predicting mental health status based on user inputs.")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
