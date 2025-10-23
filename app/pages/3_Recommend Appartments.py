import streamlit as st
import pandas as pd
import numpy as np
import re
import json
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Property Recommendations",
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
    
    .recommendation-header {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        color: var(--text-primary);
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid var(--border-color);
    }
    
    .section-container {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 8px;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
    }
    
    .recommendation-card {
        background: var(--secondary-bg);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .recommendation-card:hover {
        border-color: var(--accent-color);
        transform: translateY(-2px);
    }
    
    .similarity-score {
        background: var(--accent-color);
        color: var(--primary-bg);
        padding: 0.5rem 1rem;
        border-radius: 4px;
        font-weight: 500;
        display: inline-block;
        margin-top: 0.5rem;
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

# Load and process data
@st.cache_data
def load_and_process_data():
    try:
        # Load the apartments dataset
        df = pd.read_csv('app/data/appartments.csv').drop(22)
        
        # Process facilities for TF-IDF
        def extract_list(s):
            return re.findall(r"'(.*?)'", s)
        
        df['TopFacilities'] = df['TopFacilities'].apply(extract_list)
        df['FacilitiesStr'] = df['TopFacilities'].apply(' '.join)
        
        # Create TF-IDF matrix for facilities
        tfidf_vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['FacilitiesStr'])
        cosine_sim1 = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Process price details
        def refined_parse_modified_v2(detail_str):
            try:
                details = json.loads(detail_str.replace("'", "\""))
            except:
                return {}

            extracted = {}
            for bhk, detail in details.items():
                # Extract building type
                extracted[f'building type_{bhk}'] = detail.get('building_type')

                # Parsing area details
                area = detail.get('area', '')
                area_parts = area.split('-')
                if len(area_parts) == 1:
                    try:
                        value = float(area_parts[0].replace(',', '').replace(' sq.ft.', '').strip())
                        extracted[f'area low {bhk}'] = value
                        extracted[f'area high {bhk}'] = value
                    except:
                        extracted[f'area low {bhk}'] = None
                        extracted[f'area high {bhk}'] = None
                elif len(area_parts) == 2:
                    try:
                        extracted[f'area low {bhk}'] = float(area_parts[0].replace(',', '').replace(' sq.ft.', '').strip())
                        extracted[f'area high {bhk}'] = float(area_parts[1].replace(',', '').replace(' sq.ft.', '').strip())
                    except:
                        extracted[f'area low {bhk}'] = None
                        extracted[f'area high {bhk}'] = None

                # Parsing price details
                price_range = detail.get('price-range', '')
                price_parts = price_range.split('-')
                if len(price_parts) == 2:
                    try:
                        extracted[f'price low {bhk}'] = float(price_parts[0].replace('₹', '').replace(' Cr', '').replace(' L', '').strip())
                        extracted[f'price high {bhk}'] = float(price_parts[1].replace('₹', '').replace(' Cr', '').replace(' L', '').strip())
                        if 'L' in price_parts[0]:
                            extracted[f'price low {bhk}'] /= 100
                        if 'L' in price_parts[1]:
                            extracted[f'price high {bhk}'] /= 100
                    except:
                        extracted[f'price low {bhk}'] = None
                        extracted[f'price high {bhk}'] = None

            return extracted
        
        # Apply the refined parsing and generate the new DataFrame structure
        data_refined = []

        for _, row in df.iterrows():
            features = refined_parse_modified_v2(row['PriceDetails'])
            
            # Construct a new row for the transformed dataframe
            new_row = {'PropertyName': row['PropertyName']}
            
            # Populate the new row with extracted features
            for config in ['1 BHK', '2 BHK', '3 BHK', '4 BHK', '5 BHK', '6 BHK', '1 RK', 'Land']:
                new_row[f'building type_{config}'] = features.get(f'building type_{config}')
                new_row[f'area low {config}'] = features.get(f'area low {config}')
                new_row[f'area high {config}'] = features.get(f'area high {config}')
                new_row[f'price low {config}'] = features.get(f'price low {config}')
                new_row[f'price high {config}'] = features.get(f'price high {config}')
            
            data_refined.append(new_row)

        df_final_refined_v2 = pd.DataFrame(data_refined).set_index('PropertyName')
        df_final_refined_v2['building type_Land'] = df_final_refined_v2['building type_Land'].replace({'':'Land'})
        
        # One-hot encoding and normalization for price features
        categorical_columns = df_final_refined_v2.select_dtypes(include=['object']).columns.tolist()
        ohe_df = pd.get_dummies(df_final_refined_v2, columns=categorical_columns, drop_first=True)
        ohe_df.fillna(0, inplace=True)
        
        scaler = StandardScaler()
        ohe_df_normalized = pd.DataFrame(scaler.fit_transform(ohe_df), columns=ohe_df.columns, index=ohe_df.index)
        cosine_sim2 = cosine_similarity(ohe_df_normalized)
        
        # Process location advantages
        def distance_to_meters(distance_str):
            try:
                if 'Km' in distance_str or 'KM' in distance_str:
                    return float(distance_str.split()[0]) * 1000
                elif 'Meter' in distance_str or 'meter' in distance_str:
                    return float(distance_str.split()[0])
                else:
                    return None
            except:
                return None
        
        # Extract distances for each location
        location_matrix = {}
        for index, row in df.iterrows():
            distances = {}
            try:
                for location, distance in ast.literal_eval(row['LocationAdvantages']).items():
                    distances[location] = distance_to_meters(distance)
            except:
                continue
            location_matrix[index] = distances

        # Convert the dictionary to a dataframe
        location_df = pd.DataFrame.from_dict(location_matrix, orient='index')
        location_df.index = df.PropertyName
        location_df.fillna(54000, inplace=True)
        
        # Normalize location data
        scaler = StandardScaler()
        location_df_normalized = pd.DataFrame(scaler.fit_transform(location_df), columns=location_df.columns, index=location_df.index)
        cosine_sim3 = cosine_similarity(location_df_normalized)
        
        return df, cosine_sim1, cosine_sim2, cosine_sim3, location_df
        
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None, None, None

# Load data
df, cosine_sim1, cosine_sim2, cosine_sim3, location_df = load_and_process_data()

if df is not None:
    # Header
    st.markdown("""
    <div class="recommendation-header">
        <h1 style="font-size: 2.5rem; margin-bottom: 1rem; font-weight: 300;">Property Recommendations</h1>
        <p style="font-size: 1.1rem; color: var(--text-secondary);">AI-powered property recommendations based on facilities, pricing, and location</p>
    </div>
    """, unsafe_allow_html=True)

    # Location-Based Search Section
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: var(--accent-color); margin-bottom: 1.5rem;">Location-Based Search</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        if location_df is not None:
            selected_location = st.selectbox(
                'Select Location',
                sorted(location_df.columns.to_list()),
                help="Choose a location to search for nearby properties"
            )
        else:
            st.error("Location data not available")

    with col2:
        radius = st.number_input(
            'Radius (Kms)',
            min_value=1.0,
            max_value=100.0,
            value=20.0,
            step=1.0,
            help="Search radius in kilometers"
        )
    

    if st.button('Search Nearby Properties'):
        if location_df is not None:
            try:
                # Find properties within radius
                result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()
                
                if len(result_ser) > 0:
                    st.success(f"Found {len(result_ser)} properties within {radius} km of {selected_location}")
                    
                    # Get properties in the selected sectors
                    nearby_properties = result_ser.index.tolist()
                    
                    # Show top 10 properties
                    for i, property_name in enumerate(nearby_properties[:10]):
                        distance_km = result_ser[property_name] / 1000
                        
                        # Get property details from main dataframe
                        prop_details = df[df['PropertyName'] == property_name].iloc[0]
                        
                        st.markdown(f"""
                        <div class="recommendation-card">
                            <h4 style="color: var(--accent-color);">{property_name}</h4>
                            <p><strong>Property Name:</strong> {property_name}</p>
                            <p><strong>Distance:</strong> {distance_km:.1f} km from {selected_location}</p>
                            <p><strong>Sub Name:</strong> {prop_details['PropertySubName']}</p>
                            <p><strong>Nearby Locations:</strong> {prop_details['NearbyLocations'][:100]}...</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning(f"No properties found within {radius} km of {selected_location}")
                    st.write("**💡 Try increasing the search radius or selecting a different location.**")
            except Exception as e:
                st.error(f"Error in location search: {str(e)}")
        else:
            st.error("Location data not available")

    st.markdown('</div>', unsafe_allow_html=True)

    # AI Property Recommendations Section
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: var(--accent-color); margin-bottom: 1.5rem;">AI Property Recommendations</h2>', unsafe_allow_html=True)

    # Create property options with actual property names
    property_names = df['PropertyName'].tolist()

    selected_property_name = st.selectbox(
        'Select a property name to find similar ones:', 
        property_names,
        help="Choose a property name to get AI-powered recommendations for similar properties"
    )

    if st.button('Get Similar Properties'):
        if cosine_sim1 is not None and cosine_sim2 is not None and cosine_sim3 is not None:
            try:
                with st.spinner('Finding similar properties...'):
                    # Combined similarity matrix (weights from notebook)
                    cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
                    
                    # Get similarity scores
                    sim_scores = list(enumerate(cosine_sim_matrix[df[df['PropertyName'] == selected_property_name].index[0]]))
                    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                    top_indices = [i[0] for i in sorted_scores[1:6]]  # Get top 5 similar properties
                    
                    st.success(f"Found {len(top_indices)} similar properties!")
                    
                    for i, prop_idx in enumerate(top_indices):
                        prop = df.iloc[prop_idx]
                        similarity_score = sorted_scores[i+1][1]  # +1 because we skip the first (same property)
                        
                        st.markdown(f"""
                        <div class="recommendation-card">
                            <h4 style="color: var(--accent-color);">{prop['PropertyName']}</h4>
                            <p><strong>Property Name:</strong> {prop['PropertyName']}</p>
                            <p><strong>Sub Name:</strong> {prop['PropertySubName']}</p>
                            <p><strong>Nearby Locations:</strong> {prop['NearbyLocations'][:100]}...</p>
                            <p><strong>Top Facilities:</strong> {', '.join(prop['TopFacilities'][:5])}</p>
                            <div class="similarity-score">
                                Similarity: 100%
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error in AI recommendations: {str(e)}")
        else:
            st.error("Similarity matrices not available")

    st.markdown('</div>', unsafe_allow_html=True)

    # Information section
    st.markdown("""
    <div style="background: var(--card-bg); padding: 2rem; border-radius: 8px; margin: 2rem 0; border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-color); margin-bottom: 1rem;">How Recommendations Work</h3>
        <p style="color: var(--text-secondary); line-height: 1.6;">
            Our AI recommendation system uses three similarity matrices:<br>
            • <strong>Facilities Similarity (30x weight):</strong> Based on TF-IDF analysis of property facilities<br>
            • <strong>Price Similarity (20x weight):</strong> Based on normalized price and area features<br>
            • <strong>Location Similarity (8x weight):</strong> Based on distance to key locations<br>
            The system combines these matrices to find the most similar properties to your selection.
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("Failed to load data. Please check if all required files are present.")

# Developer credit
st.markdown("""
<div class="developer-credit">
    Developed by SAM
</div>
""", unsafe_allow_html=True)