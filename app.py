import streamlit as st
import numpy as np
import pickle

# Load model & encoders
model_data = pickle.load(open("customer_churn_model.pkl", "rb"))
model = model_data["model"]
encoders = pickle.load(open("encoders.pkl", "rb"))

st.title("📊 Customer Churn Prediction")

# ---------------- INPUTS ---------------- #

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure", 0, 72, 12)

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox("Payment Method",
                       ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# ---------------- ENCODING FUNCTION ---------------- #

def encode(col, val):
    return encoders[col].transform([val])[0]

# ---------------- FINAL INPUT (ORDER MATTERS) ---------------- #

input_data = np.array([[ 
    encode("gender", gender),
    senior,
    encode("Partner", partner),
    encode("Dependents", dependents),
    tenure,
    encode("PhoneService", phone),
    encode("MultipleLines", multiple),
    encode("InternetService", internet),
    encode("OnlineSecurity", online_sec),
    encode("OnlineBackup", online_backup),
    encode("DeviceProtection", device),
    encode("TechSupport", tech),
    encode("StreamingTV", tv),
    encode("StreamingMovies", movies),
    encode("Contract", contract),
    encode("PaperlessBilling", paperless),
    encode("PaymentMethod", payment),
    monthly,
    total
]])

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):

    prob = model.predict_proba(input_data)[0][1]
    threshold = 0.3

    answer = "Yes" if prob > threshold else "No"

    st.subheader("Will this customer churn?")
    st.write(f"### {answer}")