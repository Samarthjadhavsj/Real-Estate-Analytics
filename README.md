## Technical Requirements
###  Dependencies
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-1.3.0-blue)](https://pandas.pydata.org/)
[![numpy](https://img.shields.io/badge/numpy-1.21.0-orange)](https://numpy.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.0-green)](https://scikit-learn.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.4.0-blueviolet)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.11.0-purple)](https://seaborn.pydata.org/)
[![plotly](https://img.shields.io/badge/plotly-5.0.0-pink)](https://plotly.com/python/)
[![scipy](https://img.shields.io/badge/scipy-1.7.0-lightgrey)](https://www.scipy.org/)
[![statsmodels](https://img.shields.io/badge/statsmodels-0.12.0-darkgreen)](https://www.statsmodels.org/)
[![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.9.0-orange)](https://www.crummy.com/software/BeautifulSoup/)
[![pickle-mixin](https://img.shields.io/badge/pickle--mixin-1.0.0-lightblue)](https://pypi.org/project/pickle-mixin/)
[![streamlit](https://img.shields.io/badge/streamlit-1.0.0-ff4b4b)](https://streamlit.io/)
[![wordcloud](https://img.shields.io/badge/wordcloud-1.8.1-lightgrey)](https://amueller.github.io/word_cloud/)
[![shap](https://img.shields.io/badge/shap-0.40.0-lightgreen)](https://shap.readthedocs.io/)

---
# Real Estate Analytics & Price Prediction System

Comprehensive Machine Learning Project | Real-World Real Estate Analytics
Developed a full-scale machine learning project following the Machine Learning Development Life Cycle (MLDLC) to turn theoretical knowledge into practical skills. Leveraged real-world real estate data to perform data collection, preprocessing, exploratory analysis, feature engineering, model development, and recommendation system creation. Delivered deployment-ready insights while gaining hands-on experience to tackle real-world machine learning challenges.

## Project Phases

### 1. Project Planning & Roadmap
Established project scope, defined objectives, and created a comprehensive roadmap for the real estate analytics pipeline.

**Files Used**: Project documentation and planning artifacts

---

### 2. Data Gathering & Initial Preprocessing
Collected comprehensive real estate data and performed initial data cleaning and preprocessing.

**Files Used**:
- [data-preprocessing-flats.ipynb](data-preprocessing-flats.ipynb)
- [data-preprocessing-houses.ipynb](data-preprocessing-houses.ipynb)
- [merge-flats-and-house.ipynb](merge-flats-and-house.ipynb)
- [flats.csv](flats.csv)
- [houses.csv](houses.csv)
- [flats_cleaned.csv](flats_cleaned.csv)
- [house_cleaned.csv](house_cleaned.csv)
- [gurgaon_properties.csv](gurgaon_properties.csv)

---

### 3. Exploratory Data Analysis (EDA)
Conducted comprehensive exploratory data analysis to understand data patterns, distributions, and relationships.

**Files Used**:
- [eda-univariate-analysis.ipynb](eda-univariate-analysis.ipynb)
- [eda-multivariate-analysis.ipynb](eda-multivariate-analysis.ipynb)
- [eda-pandas-profiling.ipynb](eda-pandas-profiling.ipynb)
- [data-visualization.ipynb](data-visualization.ipynb)

---

### 4. Feature Engineering
Created meaningful features from raw data to improve model performance and extract valuable insights.

**Files Used**:
- [feature-engineering.ipynb](feature-engineering.ipynb)
- [feature-selection-and-feature-engineering.ipynb](feature-selection-and-feature-engineering.ipynb)
- [gurgaon_properties_cleaned_v1.csv](gurgaon_properties_cleaned_v1.csv)
- [gurgaon_properties_cleaned_v2.csv](gurgaon_properties_cleaned_v2.csv)

---

### 5. Outlier Detection & Treatment
Identified and treated outliers in the dataset to improve data quality and model performance.

**Files Used**:
- [outlier-treatment.ipynb](outlier-treatment.ipynb)
- [gurgaon_properties_outlier_treated.csv](gurgaon_properties_outlier_treated.csv)

---

### 6. Missing Value Imputation
Handled missing values systematically using various imputation strategies.

**Files Used**:
- [missing-value-imputation.ipynb](missing-value-imputation.ipynb)
- [gurgaon_properties_missing_value_imputation.csv](gurgaon_properties_missing_value_imputation.csv)

---

### 7. Feature Selection
Selected the most relevant features for model building to improve performance and reduce complexity.

**Files Used**:
- [feature-selection.ipynb](feature-selection.ipynb)
- [gurgaon_properties_post_feature_selection.csv](gurgaon_properties_post_feature_selection.csv)
- [gurgaon_properties_post_feature_selection_v2.csv](gurgaon_properties_post_feature_selection_v2.csv)

---

### 8. Model Building (Price Prediction)
Developed and optimized machine learning models for property price prediction.

**Models Implemented**:
- Linear Regression
- Ridge Regression
- LASSO Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor-Final Model 
- Extra Trees Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor
- MLP Regressor

**Files Used**:
- [baseline model.ipynb](baseline%20model.ipynb)
- [model-selection.ipynb](model-selection.ipynb)

---

### 9. Analysis & Insights Module Development
Developed comprehensive analysis modules to extract business insights from the data.

**Files Used**:
- [insights-module.ipynb](insights-module.ipynb)
- [output_report.html](output_report.html)

---

### 10. Recommendation System Development
Built a sophisticated recommendation system for property suggestions based on multiple similarity metrics.

**Files Used**:
- [recommender-system.ipynb](recommender-system.ipynb)
- [appartments.csv](appartments.csv)
- [latlong.csv](latlong.csv)

---

### 11. Deployment & Integration
Prepared the system for deployment with proper model serialization and integration capabilities.

**Files Used**:
- Model pipeline files (pipeline.pkl)
- Feature dataset files (df.pkl)

---

### 12. Documentation
Created comprehensive documentation for the project including technical specifications and usage guidelines.

---
## Project Structure

```
Real Estate Analytics Project
├── Data Files
│   ├── Raw Data
│   │   ├── flats.csv
│   │   └── houses.csv
│   ├── Cleaned Data
│   │   ├── flats_cleaned.csv
│   │   └── house_cleaned.csv
│   └── Processed Data
│       ├── gurgaon_properties_cleaned_v1.csv
│       ├── gurgaon_properties_cleaned_v2.csv
│       ├── gurgaon_properties_outlier_treated.csv
│       ├── gurgaon_properties_missing_value_imputation.csv
│       ├── gurgaon_properties_post_feature_selection.csv
│       └── gurgaon_properties_post_feature_selection_v2.csv
├── Analysis Notebooks
│   ├── data-preprocessing-flats.ipynb
│   ├── data-preprocessing-houses.ipynb
│   ├── merge-flats-and-house.ipynb
│   ├── eda-univariate-analysis.ipynb
│   ├── eda-multivariate-analysis.ipynb
│   ├── eda-pandas-profiling.ipynb
│   ├── data-visualization.ipynb
│   ├── feature-engineering.ipynb
│   ├── feature-selection.ipynb
│   ├── feature-selection-and-feature-engineering.ipynb
│   ├── outlier-treatment.ipynb
│   ├── missing-value-imputation.ipynb
│   ├── baseline model.ipynb
│   ├── model-selection.ipynb
│   ├── insights-module.ipynb
│   └── recommender-system.ipynb
├── Model Files
│   ├── pipeline.pkl
│   └── df.pkl
└── Reports
    └── output_report.html
```

## Key Features

- Comprehensive Data Pipeline
- Advanced Feature Engineering
- Multiple ML Models Implementation
- Recommendation System
- Business Intelligence Analysis
- Production Ready Models

## Model Performance

- R² Score: 0.865
- Mean Absolute Error: Optimized through cross-validation
- Cross-validation: 10-fold CV with consistent performance
