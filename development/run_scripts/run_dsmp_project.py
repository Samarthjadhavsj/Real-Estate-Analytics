#!/usr/bin/env python3
"""
DSMP Capstone Project - Gurgaon Real Estate Analysis
Run this script to execute the complete project pipeline
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

def main():
    print('Starting DSMP Capstone Project - Gurgaon Real Estate Analysis')
    print('=' * 70)
    
    # Change to project directory
    os.chdir('dsmp-capstone-project-master')
    
    # Load the dataset
    print('Loading dataset...')
    df = pd.read_csv('gurgaon_properties_post_feature_selection_v2.csv')
    print(f'Dataset loaded: {df.shape[0]} properties, {df.shape[1]} features')
    
    # Display basic info
    print('\nDataset Overview:')
    print(f'Property Types: {df["property_type"].value_counts().to_dict()}')
    print(f'Price Range: Rs {df["price"].min():.2f}Cr - Rs {df["price"].max():.2f}Cr')
    print(f'Average Price: Rs {df["price"].mean():.2f}Cr')
    print(f'Median Price: Rs {df["price"].median():.2f}Cr')
    
    # Prepare features and target
    X = df.drop(columns=['price'])
    y = df['price']
    
    print(f'\nFeatures: {list(X.columns)}')
    print(f'Target: Price (in Crores)')
    
    # Apply log transformation
    y_transformed = np.log1p(y)
    print(f'Applied log transformation to target variable')
    
    # Define preprocessing
    columns_to_encode = ['sector', 'balcony', 'agePossession', 'furnishing_type', 'luxury_category', 'floor_category']
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['bedRoom', 'bathroom', 'built_up_area', 'servant room', 'store room']),
            ('cat', OneHotEncoder(drop='first'), ['property_type'] + columns_to_encode)
        ], 
        remainder='passthrough'
    )
    
    # Create pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', SVR(kernel='rbf'))
    ])
    
    print(f'\nModel: Support Vector Regression with RBF kernel')
    print(f'Preprocessing: StandardScaler + OneHotEncoder')
    
    # Cross-validation
    print(f'\nRunning 10-fold cross-validation...')
    kfold = KFold(n_splits=10, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, X, y_transformed, cv=kfold, scoring='r2')
    
    print(f'R² Scores: {[f"{score:.4f}" for score in scores]}')
    print(f'Mean R² Score: {scores.mean():.4f} ± {scores.std():.4f}')
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y_transformed, test_size=0.2, random_state=42)
    
    print(f'\nTraining model on {X_train.shape[0]} samples...')
    pipeline.fit(X_train, y_train)
    
    # Predictions
    y_pred = pipeline.predict(X_test)
    y_pred_original = np.expm1(y_pred)
    y_test_original = np.expm1(y_test)
    
    # Evaluation
    mae = mean_absolute_error(y_test_original, y_pred_original)
    mse = mean_squared_error(y_test_original, y_pred_original)
    r2 = r2_score(y_test_original, y_pred_original)
    
    print(f'\nModel Performance:')
    print(f'Mean Absolute Error: Rs {mae:.2f} Cr')
    print(f'Root Mean Square Error: Rs {np.sqrt(mse):.2f} Cr')
    print(f'R² Score: {r2:.4f}')
    
    # Save model and data
    print(f'\nSaving model and data...')
    os.makedirs('../models', exist_ok=True)
    
    with open('../models/pipeline.pkl', 'wb') as f:
        pickle.dump(pipeline, f)
    
    with open('../models/df.pkl', 'wb') as f:
        pickle.dump(df, f)
    
    print(f'Model saved to: ../models/pipeline.pkl')
    print(f'Data saved to: ../models/df.pkl')
    
    # Sample predictions
    print(f'\nSample Predictions:')
    sample_indices = np.random.choice(len(X_test), 5, replace=False)
    for i, idx in enumerate(sample_indices):
        actual = y_test_original.iloc[idx]
        predicted = y_pred_original[idx]
        error = abs(actual - predicted)
        print(f'Sample {i+1}: Actual Rs {actual:.2f}Cr, Predicted Rs {predicted:.2f}Cr, Error Rs {error:.2f}Cr')
    
    print(f'\nDSMP Capstone Project executed successfully!')
    print(f'Model ready for deployment in Streamlit app')
    print(f'\nNext Steps:')
    print(f'1. Run: streamlit run ../Home.py')
    print(f'2. Open: http://localhost:8501')
    print(f'3. Explore: Price Predictor, Analytics Dashboard, Recommendations')

if __name__ == "__main__":
    main()
