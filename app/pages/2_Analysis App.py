import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .dashboard-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2c5aa0;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Developer credit */
    .developer-credit {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: white;
        color: #666;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        font-size: 0.8rem;
        border: 1px solid #ddd;
        z-index: 1000;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="dashboard-header">
    <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">📊 Analytics Dashboard</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Comprehensive real estate market analysis and insights</p>
</div>
""", unsafe_allow_html=True)

new_df = pd.read_csv('app/datasets/data_viz1.csv')
feature_text = pickle.load(open('app/datasets/feature_text.pkl','rb'))


group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

# Key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(new_df):,}</div>
        <div class="metric-label">Total Properties</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(group_df)}</div>
        <div class="metric-label">Sectors Covered</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_price = new_df['price'].mean()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">₹{avg_price:.1f}Cr</div>
        <div class="metric-label">Avg Price</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_psf = new_df['price_per_sqft'].mean()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">₹{avg_psf:,.0f}</div>
        <div class="metric-label">Avg Price/Sqft</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🗺️ Sector Price per Sqft Geomap</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

fig = px.scatter_map(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  map_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">☁️ Features Wordcloud</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">📈 Area vs Price Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", 
                     title="Area vs Price - Houses", 
                     labels={'built_up_area': 'Built Up Area (sq ft)', 'price': 'Price (Cr)', 'bedRoom': 'Bedrooms'})
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area vs Price - Flats",
                      labels={'built_up_area': 'Built Up Area (sq ft)', 'price': 'Price (Cr)', 'bedRoom': 'Bedrooms'})
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🥧 BHK Distribution</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom', title=f'BHK Distribution - All Sectors')
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom', 
                  title=f'BHK Distribution - {selected_sector}')

fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig2, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">📊 BHK Price Comparison</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', 
              title='Price Range by BHK Configuration',
              labels={'bedRoom': 'Number of Bedrooms', 'price': 'Price (Cr)'})
fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig3, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">📈 Price Distribution by Property Type</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)

fig4 = plt.figure(figsize=(12, 6))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='Houses', alpha=0.7, color='#667eea')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flats', alpha=0.7, color='#764ba2')
plt.xlabel('Price (Cr)')
plt.ylabel('Frequency')
plt.title('Price Distribution Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
st.pyplot(fig4)
st.markdown('</div>', unsafe_allow_html=True)

# Developer credit
st.markdown("""
<div class="developer-credit">
    Developed by SAM
</div>
""", unsafe_allow_html=True)










