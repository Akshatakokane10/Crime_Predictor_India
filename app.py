import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Set page config
st.set_page_config(
    page_title="Crime Type Predictor",
    page_icon="\U0001F46E",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f2f6fc;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        height: 3rem;
        font-size: 1rem;
    }
    .stButton>button {
        background-color: #2c7be5;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1a5fbe;
    }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("""
    <div class='main'>
        <h1 style='text-align: center; color: #2c3e50;'>🔍 Indian Crime Domain Predictor</h1>
        <p style='text-align: center; font-size: 1.1rem;'>Enter a short description of a crime and our AI model will predict the crime domain.</p>
    </div>
""", unsafe_allow_html=True)

# Input
user_input = st.text_input("\nEnter Crime Description:", placeholder="e.g. Man caught with illegal firearm")

# Prediction
if st.button("Predict Crime Domain"):
    if user_input.strip() == "":
        st.warning("Please enter a crime description to get a prediction.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"\U0001F4C8 Predicted Crime Domain: **{prediction}**")

# Footer
st.markdown("""
    <hr style="margin-top: 3rem;">
    <p style="text-align: center; font-size: 0.9rem; color: #888;">
        Made with ❤️ using Streamlit | Crime Prediction Project 2025
    </p>
""", unsafe_allow_html=True)
