# ML-Project
Here’s a concise version of the `README.md` tailored for the updated details:

---

# EURUSD App

**EURUSD App** is a Streamlit-based web application designed to predict EUR/USD currency pair prices using an **LSTM model**. Users can input the price, open value, high, and low values to get precise predictions.

---

## Features

- **LSTM Model**: Utilizes a trained LSTM model for time-series predictions.
- **User-Friendly Interface**: Intuitive design powered by Streamlit.
- **Key Input Parameters**: 
  - Price
  - Open Value
  - High Value
  - Low Value

---

## How to Run the App

### Prerequisites
Ensure the following are installed:
- Python 3.8+
- Required libraries: `streamlit`, `numpy`, `pandas`, `keras`


### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/eurusd_app.git
   cd eurusd-app
   ```

2. Place the trained LSTM model file (`lstm_model.h5`) in the project directory.

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open the provided URL (e.g., `http://localhost:8501`) in your browser.

---

## Usage

1. Enter the input values:
   - Price
   - Open Value
   - High Value
   - Low Value

2. Click **Predict** to view the forecasted value.

---

## Folder Structure

```
.
├── eurusd_app.py                    # Main Streamlit application
├── stock_prediction_model.pkl       # Trained LSTM model     
├── README.md                        # Documentation
```

---

