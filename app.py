import streamlit as st
import pickle

model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0.0,
    max_value=72.0,
    value=12.0
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=18.0,
    max_value=120.0,
    value=50.0
)

if st.button("Predict"):

    features = [[
        0,
        0,
        0,
        0,
        tenure,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        monthly,
        monthly * tenure
    ]]

    prediction = model.predict(features)
    proba = model.predict_proba(features)

    stay_prob = round(proba[0][0] * 100, 2)
    churn_prob = round(proba[0][1] * 100, 2)

    st.write(f"Stay Probability: {stay_prob}%")
    st.write(f"Churn Probability: {churn_prob}%")

    if prediction[0] == 1:
        st.error("Customer Likely To Churn")
    else:
        st.success("Customer Likely To Stay")