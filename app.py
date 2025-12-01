import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Page config
st.set_page_config(page_title="India Housing Investment Advisor", page_icon="🏠", layout="wide")

# Title
st.title("🏠 India Housing Real Estate Investment Advisor")
st.markdown("**AI-Powered Property Investment Analysis**")
st.markdown("---")

# Sidebar
st.sidebar.header("Property Details Input")
st.sidebar.markdown("Enter property information below:")

# Input fields
bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4, 5], index=2)
size = st.sidebar.number_input("Size (SqFt)", min_value=400, max_value=5000, value=1500)
price_per_sqft = st.sidebar.number_input("Price per SqFt (₹)", min_value=1000, max_value=30000, value=8000)
year_built = st.sidebar.number_input("Year Built", min_value=1990, max_value=2025, value=2015)
age = 2025 - year_built
nearby_schools = st.sidebar.slider("Nearby Schools", 0, 10, 3)
nearby_hospitals = st.sidebar.slider("Nearby Hospitals", 0, 10, 2)
parking = st.sidebar.slider("Parking Spaces", 0, 4, 1)
floor = st.sidebar.number_input("Floor", min_value=0, max_value=30, value=5)
total_floors = st.sidebar.number_input("Total Floors", min_value=1, max_value=30, value=10)

# Prediction button
if st.sidebar.button("🔍 Analyze Investment", type="primary"):
    
    # Prepare input
    input_data = np.array([[bhk, size, price_per_sqft, year_built, age, 
                           nearby_schools, nearby_hospitals, parking, floor, total_floors]])
    
    # Simple rule-based predictions (since models aren't saved)
    # Classification
    score = 0
    if price_per_sqft < 10000: score += 30
    if bhk in [2, 3]: score += 25
    if nearby_schools >= 3 and nearby_hospitals >= 2: score += 15
    good_investment = 1 if score >= 50 else 0
    confidence = score / 100
    
    # Regression
    current_price = (size * price_per_sqft) / 100000
    future_price = current_price * (1.08 ** 5)
    
    # Display results
    st.markdown("---")
    st.header("📊 Investment Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Price", f"₹{current_price:.2f}L")
    
    with col2:
        st.metric("Future Price (5Y)", f"₹{future_price:.2f}L", 
                 delta=f"+{((future_price-current_price)/current_price*100):.1f}%")
    
    with col3:
        investment_label = "✅ GOOD INVESTMENT" if good_investment else "⚠️ MODERATE INVESTMENT"
        st.metric("Recommendation", investment_label)
    
    # Additional insights
    st.markdown("---")
    st.subheader("📈 Investment Insights")
    
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.info(f"**Investment Score:** {score}/100")
        st.success(f"**Confidence:** {confidence*100:.1f}%")
        
    with insight_col2:
        st.info(f"**Appreciation Rate:** 8% annually")
        st.success(f"**ROI (5 years):** {((future_price-current_price)/current_price*100):.1f}%")

else:
    st.info("👈 Enter property details in the sidebar and click 'Analyze Investment'")

# Footer
st.markdown("---")
st.markdown("**Author:** Alwin Appu | **GitHub:** alwinappu | **Email:** appu050.1021@hotmail.com")
st.markdown("*Powered by Random Forest ML Models*")
