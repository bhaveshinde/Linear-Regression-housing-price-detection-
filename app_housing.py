import streamlit as st
import joblib
import pandas as pd

# Load the trained linear regression model
model = joblib.load("model_housing.pkl")

# Define the UI
def main():
    st.title("Housing Price Prediction")

    # Add input fields for user input
    area = st.text_input("Area (sqft)")
    bedrooms = st.text_input("Bedrooms")
    bathrooms = st.text_input("Bathrooms")

    # Make prediction
    if st.button("Predict"):
        input_data = {'area': float(area), 'bedrooms': float(bedrooms), 'bathrooms': float(bathrooms)}
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        st.success(f"The predicted price is RS {prediction[0]:,.2f}")

# Run the app
if __name__ == "__main__":
    main()
