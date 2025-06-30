# Market Volatility (VIX) Prediction Using Machine Learning

Predicting the VIX (Volatility Index) based on historical financial data using ML models.

Scores:
  >> Linear Regression Model Results
     RMSE: 1.52
     R² Score: 0.93

  >> Random Forest Model Results
     RMSE: 1.69
     R² Score: 0.91
---

## Features

- Collects financial data via `yfinance` API  
- Performs data cleaning, feature engineering, and creates lag features  
- Implements Linear Regression and Random Forest models  
- Provides an interactive Streamlit app for VIX prediction  
- Uses Pandas, Seaborn for data analysis and visualization  

---

## Tech Stack

- Python, Pandas, NumPy  
- scikit-learn  
- Streamlit  
- yfinance  
- Matplotlib, Seaborn  

---

## How to Run

1. Clone the repository  
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
