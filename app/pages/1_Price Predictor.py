import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Price Predictor",
    page_icon="",
    layout="wide"
)

# Custom CSS for clean dark theme
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-bg: #0a0a0a;
        --secondary-bg: #1a1a1a;
        --card-bg: #2a2a2a;
        --accent-color: #4a9eff;
        --text-primary: #ffffff;
        --text-secondary: #b0b0b0;
        --border-color: #404040;
    }
    
    .prediction-card {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        color: var(--text-primary);
        text-align: center;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
    }
    
    .prediction-price {
        font-size: 2.5rem;
        font-weight: 300;
        margin: 1rem 0;
        color: var(--accent-color);
    }
    
    .prediction-range {
        font-size: 1rem;
        color: var(--text-secondary);
    }
    
    .form-container {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
    }
    
    .section-header {
        font-size: 1.2rem;
        font-weight: 500;
        color: var(--accent-color);
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    .metric-card {
        background: var(--secondary-bg);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid var(--border-color);
    }
    
    .metric-card h4 {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card h3 {
        color: var(--accent-color);
        font-size: 1.5rem;
        font-weight: 300;
        margin: 0;
    }
    
    .stButton > button {
        background: var(--accent-color);
        color: var(--primary-bg);
        border: none;
        border-radius: 4px;
        padding: 0.8rem 2rem;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: #3a8ae6;
        transform: translateY(-1px);
    }
    
    /* Form styling */
    .stSelectbox > div > div {
        background-color: var(--secondary-bg);
        border-color: var(--border-color);
    }
    
    .stNumberInput > div > div > input {
        background-color: var(--secondary-bg);
        border-color: var(--border-color);
        color: var(--text-primary);
    }
    
    /* Developer credit */
    .developer-credit {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: var(--card-bg);
        color: var(--text-secondary);
        padding: 0.5rem 1rem;
        border-radius: 4px;
        font-size: 0.8rem;
        border: 1px solid var(--border-color);
        z-index: 1000;
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
    }
    
    p, label {
        color: var(--text-secondary);
    }
</style>
""", unsafe_allow_html=True)

# Load models
with open('app/models/df.pkl','rb') as file:
    df = pickle.load(file)
with open('app/models/pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

# Header
st.markdown("""
<div style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.5rem; color: var(--text-primary); margin-bottom: 1rem; font-weight: 300;">Property Price Predictor</h1>
    <p style="font-size: 1.1rem; color: var(--text-secondary);">Get accurate price predictions using advanced AI algorithms</p>
</div>
""", unsafe_allow_html=True)

# Main form
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">Property Details</div>', unsafe_allow_html=True)
        
        # Property type
        property_type = st.selectbox(
            'Property Type',
            ['flat', 'house'],
            help="Select the type of property"
        )
        
        # Sector
        sector = st.selectbox(
            'Sector',
            sorted(df['sector'].unique().tolist()),
            help="Choose the sector where the property is located"
        )
        
        # Bedrooms and Bathrooms
        col_bed, col_bath = st.columns(2)
        with col_bed:
            bedrooms = float(st.selectbox(
                'Number of Bedrooms',
                sorted(df['bedRoom'].unique().tolist()),
                help="Number of bedrooms in the property"
            ))
        
        with col_bath:
            bathroom = float(st.selectbox(
                'Number of Bathrooms',
                sorted(df['bathroom'].unique().tolist()),
                help="Number of bathrooms in the property"
            ))
        
        # Built up area
        built_up_area = st.number_input(
            'Built Up Area (sq ft)',
            min_value=100.0,
            max_value=10000.0,
            value=1000.0,
            step=50.0,
            help="Total built-up area in square feet"
        )
    
    with col2:
        st.markdown('<div class="section-header">Additional Features</div>', unsafe_allow_html=True)
        
        # Balcony and Property Age
        balcony = st.selectbox(
            'Number of Balconies',
            sorted(df['balcony'].unique().tolist()),
            help="Number of balconies in the property"
        )
        
        property_age = st.selectbox(
            'Property Age',
            sorted(df['agePossession'].unique().tolist()),
            help="Age of the property"
        )
        
        # Furnishing and Luxury
        furnishing_type = st.selectbox(
            'Furnishing Type',
            sorted(df['furnishing_type'].unique().tolist()),
            help="Furnishing status of the property"
        )
        
        luxury_category = st.selectbox(
            'Luxury Category',
            sorted(df['luxury_category'].unique().tolist()),
            help="Luxury level of the property"
        )
        
        floor_category = st.selectbox(
            'Floor Category',
            sorted(df['floor_category'].unique().tolist()),
            help="Floor level category"
        )
        
        # Additional rooms
        col_servant, col_store = st.columns(2)
        with col_servant:
            servant_room = float(st.selectbox(
                'Servant Room',
                [0.0, 1.0],
                help="Does the property have a servant room?"
            ))
        
        with col_store:
            store_room = float(st.selectbox(
                'Store Room',
                [0.0, 1.0],
                help="Does the property have a store room?"
            ))
    
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction button and results
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button('Predict Property Price', use_container_width=True):
        with st.spinner('Analyzing property details...'):
            # Form a dataframe
            data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, 
                    built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
            columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                       'agePossession', 'built_up_area', 'servant room', 'store room',
                       'furnishing_type', 'luxury_category', 'floor_category']

            # Convert to DataFrame
            one_df = pd.DataFrame(data, columns=columns)

            # Predict
            base_price = np.expm1(pipeline.predict(one_df))[0]
            low = base_price - 0.22
            high = base_price + 0.22

            # Display results
            st.markdown("""
            <div class="prediction-card">
                <h2 style="margin-bottom: 1rem; color: var(--text-primary);">Price Prediction</h2>
                <div class="prediction-price">₹{:.2f} Cr</div>
                <div class="prediction-range">
                    Estimated Range: ₹{:.2f} Cr - ₹{:.2f} Cr
                </div>
                <p style="margin-top: 1rem; color: var(--text-secondary);">
                    *Price prediction based on similar properties in the area
                </p>
            </div>
            """.format(base_price, low, high), unsafe_allow_html=True)
            
            # Additional metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>Price per Sq Ft</h4>
                    <h3>₹{base_price * 10000000 / built_up_area:,.0f}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>Property Type</h4>
                    <h3>{property_type.title()}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>Location</h4>
                    <h3>{sector}</h3>
                </div>
                """, unsafe_allow_html=True)

# Information section
st.markdown("---")
st.markdown("""
<div style="background: var(--card-bg); padding: 2rem; border-radius: 8px; margin: 2rem 0; border: 1px solid var(--border-color);">
    <h3 style="color: var(--accent-color); margin-bottom: 1rem;">How It Works</h3>
    <p style="color: var(--text-secondary); line-height: 1.6;">
        Our AI-powered price prediction model analyzes thousands of property transactions 
        to provide accurate price estimates. The model considers factors like location, property size, 
        amenities, and market trends to give you the most reliable price prediction.
    </p>
</div>
""", unsafe_allow_html=True)

# Developer credit
st.markdown("""
<div class="developer-credit">
    Developed by SAM
</div>
""", unsafe_allow_html=True)