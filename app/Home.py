import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Real Estate Analytics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
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
    
    /* Global styles */
    .stApp {
        background-color: var(--primary-bg);
        color: var(--text-primary);
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 300;
        color: var(--text-primary);
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
        line-height: 1.6;
    }
    
    .feature-card {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        color: var(--text-primary);
        margin: 1rem 0;
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: var(--accent-color);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(74, 158, 255, 0.1);
    }
    
    .feature-title {
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 1rem;
        color: var(--accent-color);
    }
    
    .feature-description {
        font-size: 0.95rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    .stats-container {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        color: var(--text-primary);
        text-align: center;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
    }
    
    .stat-number {
        font-size: 2.2rem;
        font-weight: 300;
        margin-bottom: 0.5rem;
        color: var(--accent-color);
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .cta-button {
        background: var(--accent-color);
        color: var(--primary-bg);
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 4px;
        font-size: 0.9rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 1rem;
    }
    
    .cta-button:hover {
        background: #3a8ae6;
        transform: translateY(-1px);
    }
    
    .hero-section {
        background: var(--secondary-bg);
        padding: 4rem 2rem;
        border-radius: 8px;
        color: var(--text-primary);
        text-align: center;
        margin-bottom: 3rem;
        border: 1px solid var(--border-color);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--secondary-bg);
    }
    
    .css-1lcbmhc .css-1d391kg {
        background-color: var(--secondary-bg);
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
    }
    
    p {
        color: var(--text-secondary);
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
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">Real Estate Analytics</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced AI-Powered Property Analysis & Price Prediction Platform</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Stats section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">3,554</div>
        <div class="stat-label">Properties Analyzed</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">104</div>
        <div class="stat-label">Sectors Covered</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">88%</div>
        <div class="stat-label">Prediction Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-container">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Available</div>
    </div>
    """, unsafe_allow_html=True)

# Features section
st.markdown("## Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Price Predictor</div>
        <div class="feature-description">
            Get accurate property price predictions using advanced machine learning algorithms. 
            Input property details and receive instant price estimates with confidence intervals.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Analytics Dashboard</div>
        <div class="feature-description">
            Comprehensive data visualization with interactive maps, charts, and insights. 
            Analyze market trends, sector-wise pricing, and property distributions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Smart Recommendations</div>
        <div class="feature-description">
            AI-powered property recommendations based on your preferences and similar properties. 
            Find your perfect match using advanced similarity algorithms.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Location Intelligence</div>
        <div class="feature-description">
            Advanced location-based search with radius filtering. 
            Find properties within your preferred distance from key locations.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Call to action
st.markdown("## Get Started")
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 2rem;">
        Ready to explore the real estate market? Choose your preferred tool from the sidebar.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: var(--text-secondary); padding: 2rem 0;">
    <p>© 2024 Real Estate Analytics Platform | Powered by AI & Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# Developer credit
st.markdown("""
<div class="developer-credit">
    Developed by SAM
</div>
""", unsafe_allow_html=True)