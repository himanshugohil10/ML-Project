import streamlit as st
import numpy as np
import joblib  # For loading your trained model

# Load your trained model
model = joblib.load('stock_prediction_model.pkl')


# Function to make predictions
def predict_eurusd(price, open_value, high_value, low_value):
    # Prepare input data for prediction
    # Duplicate the input values to create a 60-timestep sequence, each with 4 features
    data = np.tile([price, open_value, high_value, low_value], (60, 1)).reshape(1, 60, 4)
    
    # Prediction
    prediction = model.predict(data)
    predicted_high, predicted_low = prediction[0][0], prediction[0][1]
    return predicted_high, predicted_low

# Function to provide investment suggestion based on predicted range
def investment_suggestion(predicted_high, predicted_low, price):
    avg_range = (predicted_high + predicted_low) / 2
    if avg_range > price * 1.01:  # Example threshold for a bullish prediction
        return "Consider investing, as the prediction indicates a potential increase in value."
    elif avg_range < price * 0.99:  # Example threshold for a bearish prediction
        return "Consider holding off, as the prediction suggests a potential decrease in value."
    else:
        return "The predicted range is close to the current value. Consider a cautious approach."

# Streamlit app layout
st.title("EURUSD High-Low Prediction and Investment Suggestion")

# User inputs
price = st.number_input("Enter the Price:", value=1.33, step=0.001)
open_value = st.number_input("Enter the Open Value:", value=1.33, step=0.001)
high_value = st.number_input("Enter the High Value:", value=1.34, step=0.001)
low_value = st.number_input("Enter the Low Value:", value=1.32, step=0.001)

# Predict and show results
if st.button("Predict"):
    predicted_high, predicted_low = predict_eurusd(price, open_value, high_value, low_value)
    st.write(f"Predicted High: {predicted_high:.4f}")
    st.write(f"Predicted Low: {predicted_low:.4f}")
    
    suggestion = investment_suggestion(predicted_high, predicted_low, price)
    st.write("Investment Suggestion:", suggestion)
