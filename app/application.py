import streamlit as st
import pickle
import numpy as np

model_path = r'D:\Projects\-Market-Volatility-VIX-Prediction-\src\rf_model.pkl'
scaler_path = r'D:\Projects\-Market-Volatility-VIX-Prediction-\src\scaler.pkl'

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Market Volatility (VIX) Predictor")
st.subheader("Enter yesterday’s values:")

sp500 = st.number_input("S&P 500", value=4000.0)
gold = st.number_input("Gold Price", value=1800.0)
oil = st.number_input("Oil Price", value=70.0)
vix = st.number_input("VIX", value=15.0)

if st.button("Predict Today's VIX"):
    user_input = np.array([[sp500, gold, oil, vix]])
    scaled_input = scaler.transform(user_input)
    prediction = model.predict(scaled_input)[0]
    st.success(f"Predicted VIX for Today: {prediction:.2f}")
