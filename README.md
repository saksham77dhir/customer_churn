# 📊 Customer Churn Prediction

A machine learning web app built with **Streamlit** that predicts whether a telecom customer is likely to churn or stay, based on their account and service details.

---

## 🚀 Demo

-🌐 Live App: https://customerchurn-hyper7.streamlit.app/
-Enter customer details in the sidebar → Click **Predict** → Get a **Yes / No** answer instantly.

---

## 🗂️ Project Structure

```
Customer Churn/
│
├── app.py                          # Streamlit web app
├── customer_churn_prediction.ipynb # Model training notebook
├── customer_churn_model.pkl        # Saved trained model (RandomForest)
├── encoders.pkl                    # Saved label encoders
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── requirements.txt                # Python dependencies
└── README.md
```

---

## 🧠 Model Details

| Detail | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Imbalance Handling | SMOTE (Synthetic Minority Oversampling) |
| Prediction Threshold | 0.3 |
| Target | Churn (Yes / No) |

---



## 📥 Input Features

The app takes the following customer details as input:

- **Demographics** — Gender, Senior Citizen, Partner, Dependents
- **Account Info** — Tenure, Contract type, Paperless Billing, Payment Method, Monthly & Total Charges
- **Services** — Phone, Multiple Lines, Internet, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV & Movies

---

## 📦 Dataset

[Telco Customer Churn — IBM Sample Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Pandas, NumPy, Matplotlib, Seaborn
