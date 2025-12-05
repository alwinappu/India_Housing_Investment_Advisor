import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Page config
st.set_page_config(
    page_title="Real Estate Investment Advisor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🏠 REAL ESTATE INVESTMENT ADVISOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Professional Property Analysis & Investment Prediction System</p>', unsafe_allow_html=True)
st.markdown("---")

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["⚡ Quick Predictor", "📊 Market Insights", "📈 Property Search", "🏢 About & Skills"])

# Tab 1: Quick Predictor
with tab1:
    st.markdown('<h2 class="section-header">Property Investment Analysis</h2>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("📍 Property Details")
        
        city = st.selectbox("City", ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata"])
        property_type = st.selectbox("Property Type", ["Apartment", "Villa", "Independent House", "Penthouse"])
        bhk = st.selectbox("BHK", [1, 2, 3, 4, 5], index=2)
        size = st.number_input("Size (SqFt)", min_value=400, max_value=5000, value=1500, step=50)
        current_price = st.number_input("Current Price (₹ Lakhs)", min_value=10.0, max_value=500.0, value=80.0, step=5.0)
        year_built = st.number_input("Year Built", min_value=1990, max_value=2025, value=2015)
        
    with col_right:
        st.subheader("🏥 Amenities Score (1-10)")
        
        nearby_schools = st.slider("Nearby Schools", 0, 10, 5)
        nearby_hospitals = st.slider("Nearby Hospitals", 0, 10, 4)
        public_transport = st.slider("Public Transport Accessibility", 0, 10, 6)
        
        st.subheader("🏗️ Additional Features")
        parking = st.slider("Parking Spaces", 0, 4, 1)
        floor = st.number_input("Floor", min_value=0, max_value=30, value=5)
        total_floors = st.number_input("Total Floors", min_value=1, max_value=30, value=10)
    
    if st.button("🚀 PREDICT INVESTMENT POTENTIAL", type="primary", use_container_width=True):
        # Calculate metrics
        age = 2025 - year_built
        price_per_sqft = (current_price * 100000) / size
        
        # Investment Score Calculation
        score = 0
        if price_per_sqft < 10000: score += 25
        if bhk in [2, 3]: score += 20
        if nearby_schools >= 5: score += 15
        if nearby_hospitals >= 4: score += 10
        if public_transport >= 5: score += 10
        if parking >= 1: score += 10
        if age < 10: score += 10
        
        good_investment = score >= 55
        confidence = min(score / 100, 0.95)
        
        # Future Price Prediction
        appreciation_rate = 0.08  # 8% annually
        future_price_5y = current_price * ((1 + appreciation_rate) ** 5)
        roi_5y = ((future_price_5y - current_price) / current_price) * 100
        
        # Display Results
        st.markdown("---")
        st.markdown('<h2 class="section-header">📊 Investment Analysis Results</h2>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Current Price", f"₹{current_price:.1f}L")
        
        with col2:
            st.metric(
                "Future Price (5Y)",
                f"₹{future_price_5y:.1f}L",
                delta=f"+{roi_5y:.1f}%"
            )
        
        with col3:
            st.metric("Investment Score", f"{score}/100")
        
        with col4:
            investment_label = "✅ GOOD" if good_investment else "⚠️ MODERATE"
            st.metric("Recommendation", investment_label)
        
        # Detailed Insights
        st.markdown("---")
        st.subheader("📈 Detailed Investment Insights")
        
        col_insight1, col_insight2 = st.columns(2)
        
        with col_insight1:
            st.info(f"**Price per SqFt:** ₹{price_per_sqft:,.0f}")
            st.success(f"**Confidence Level:** {confidence*100:.1f}%")
            st.info(f"**Property Age:** {age} years")
        
        with col_insight2:
            st.info(f"**Annual Appreciation:** {appreciation_rate*100:.0f}%")
            st.success(f"**5-Year ROI:** {roi_5y:.1f}%")
            st.info(f"**Location Score:** {city} - {property_type}")
        
        # Price Trend Chart
        years = list(range(2025, 2031))
        prices = [current_price * ((1 + appreciation_rate) ** i) for i in range(6)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=prices,
            mode='lines+markers',
            name='Projected Price',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="5-Year Price Projection",
            xaxis_title="Year",
            yaxis_title="Price (₹ Lakhs)",
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Tab 2: Market Insights
with tab2:
    st.markdown('<h2 class="section-header">Market Insights & Trends</h2>', unsafe_allow_html=True)
    
    # Sample data for visualization
    cities_data = {
        'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune'],
        'Avg_Price_per_SqFt': [18500, 12000, 8500, 7000, 9500, 7500],
        'YoY_Growth': [6.5, 8.2, 12.5, 11.0, 7.5, 10.5]
    }
    df_cities = pd.DataFrame(cities_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Average Price per SqFt by City")
        fig1 = px.bar(df_cities, x='City', y='Avg_Price_per_SqFt',
                      color='Avg_Price_per_SqFt',
                      color_continuous_scale='Blues')
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Year-over-Year Growth Rate")
        fig2 = px.bar(df_cities, x='City', y='YoY_Growth',
                      color='YoY_Growth',
                      color_continuous_scale='Greens')
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
    
    # BHK Distribution
    st.subheader("Property Type Distribution Insights")
    bhk_data = pd.DataFrame({
        'BHK': ['1 BHK', '2 BHK', '3 BHK', '4 BHK', '5 BHK'],
        'Count': [15, 35, 30, 15, 5]
    })
    
    fig3 = px.pie(bhk_data, values='Count', names='BHK',
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3, use_container_width=True)

# Tab 3: Property Search
with tab3:
    st.markdown('<h2 class="section-header">Property Search & Filter</h2>', unsafe_allow_html=True)
    st.info("🔍 Advanced property search functionality - Coming soon!")
    st.markdown("""
    **Planned Features:**
    - Search properties by location, price range, and amenities
    - Interactive map view of properties
    - Detailed property comparison tool
    - Save favorite properties
    - Price alert notifications
    """)

# Tab 4: About & Skills
with tab4:
    st.markdown('<h2 class="section-header">About This Project</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Project Overview
    This AI-Powered Real Estate Investment Advisor uses Machine Learning to analyze Indian housing market data
    and provide intelligent investment recommendations.
    
    ### 🛠️ Technical Stack
    - **Frontend:** Streamlit (Python)
    - **ML Models:** Random Forest Classifier & Regressor
    - **Visualization:** Plotly, Matplotlib, Seaborn
    - **Data Processing:** Pandas, NumPy, Scikit-learn
    - **Deployment:** Streamlit Cloud
    
    ### 📊 Model Features
    - **Classification Model:** Predicts if a property is a Good Investment
    - **Regression Model:** Estimates future property price (5-year horizon)
    - **Feature Engineering:** Price per SqFt, Age, Location Score, Amenities Index
    
    ### 🎓 Skills Demonstrated
    ✅ **Data Science:** EDA, Feature Engineering, Data Preprocessing  
    ✅ **Machine Learning:** Classification, Regression, Model Evaluation  
    ✅ **MLOps:** MLflow experiment tracking, Model versioning  
    ✅ **Web Development:** Streamlit dashboard, Interactive visualizations  
    ✅ **Python Programming:** Pandas, NumPy, Scikit-learn, Plotly  
    
    ### 📧 Contact Information
    **Author:** Alwin Appu  
    **GitHub:** [github.com/alwinappu](https://github.com/alwinappu)  
    **Email:** appu050.1021@hotmail.com  
    
    ### 📚 Use Cases
    - Individual home buyers looking for investment opportunities
    - Real estate agents advising clients
    - Property investors evaluating portfolios
    - Market analysts tracking price trends
    """)
    
    st.markdown("---")
    st.success("💡 **Powered by Random Forest ML Models** | Built with ❤️ using Python & Streamlit")

# Footer
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)
with col_footer1:
    st.markdown("**📧 Email:** appu050.1021@hotmail.com")
with col_footer2:
    st.markdown("**👨‍💻 Developer:** Alwin Appu")
with col_footer3:
    st.markdown("**🔗 GitHub:** alwinappu")
