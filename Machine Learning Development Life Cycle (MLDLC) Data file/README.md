# Real Estate Analytics & Price Prediction System

A comprehensive ML project from starting to deploying using MLDLC built to gain practical knowledge by applying theoretical knowledge. This project involves real estate data analysis, comprehensive data analysis, feature engineering, machine learning model development, and building a recommendation system for property suggestions. The project follows a structured approach from data collection to deployment-ready insights.

## Project Phases

### 1. Project Planning & Roadmap
**Objective**: Established project scope, defined objectives, and created a comprehensive roadmap for the real estate analytics pipeline.

**Files Used**: Project documentation and planning artifacts

---

### 2. Data Gathering & Initial Preprocessing
**Objective**: Collected comprehensive real estate data and performed initial data cleaning and preprocessing.

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
**Objective**: Conducted comprehensive exploratory data analysis to understand data patterns, distributions, and relationships.

**Files Used**:
- [eda-univariate-analysis.ipynb](eda-univariate-analysis.ipynb)
- [eda-multivariate-analysis.ipynb](eda-multivariate-analysis.ipynb)
- [eda-pandas-profiling.ipynb](eda-pandas-profiling.ipynb)
- [data-visualization.ipynb](data-visualization.ipynb)

---

### 4. Feature Engineering
**Objective**: Created meaningful features from raw data to improve model performance and extract valuable insights.

**Files Used**:
- [feature-engineering.ipynb](feature-engineering.ipynb)
- [feature-selection-and-feature-engineering.ipynb](feature-selection-and-feature-engineering.ipynb)
- [gurgaon_properties_cleaned_v1.csv](gurgaon_properties_cleaned_v1.csv)
- [gurgaon_properties_cleaned_v2.csv](gurgaon_properties_cleaned_v2.csv)

---

### 5. Outlier Detection & Treatment
**Objective**: Identified and treated outliers in the dataset to improve data quality and model performance.

**Files Used**:
- [outlier-treatment.ipynb](outlier-treatment.ipynb)
- [gurgaon_properties_outlier_treated.csv](gurgaon_properties_outlier_treated.csv)

---

### 6. Missing Value Imputation
**Objective**: Handled missing values systematically using various imputation strategies.

**Files Used**:
- [missing-value-imputation.ipynb](missing-value-imputation.ipynb)
- [gurgaon_properties_missing_value_imputation.csv](gurgaon_properties_missing_value_imputation.csv)

---

### 7. Feature Selection
**Objective**: Selected the most relevant features for model building to improve performance and reduce complexity.

**Files Used**:
- [feature-selection.ipynb](feature-selection.ipynb)
- [gurgaon_properties_post_feature_selection.csv](gurgaon_properties_post_feature_selection.csv)
- [gurgaon_properties_post_feature_selection_v2.csv](gurgaon_properties_post_feature_selection_v2.csv)

---

### 8. Model Building (Price Prediction)
**Objective**: Developed and optimized machine learning models for property price prediction.

**Models Implemented**:
- Linear Regression
- Ridge Regression
- LASSO Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
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
**Objective**: Developed comprehensive analysis modules to extract business insights from the data.

**Files Used**:
- [insights-module.ipynb](insights-module.ipynb)
- [output_report.html](output_report.html)

---

### 10. Recommendation System Development
**Objective**: Built a sophisticated recommendation system for property suggestions based on multiple similarity metrics.

**Files Used**:
- [recommender-system.ipynb](recommender-system.ipynb)
- [appartments.csv](appartments.csv)
- [latlong.csv](latlong.csv)

---

### 11. Deployment & Integration
**Objective**: Prepared the system for deployment with proper model serialization and integration capabilities.

**Files Used**:
- Model pipeline files (pipeline.pkl)
- Feature dataset files (df.pkl)

---

### 12. Documentation
**Objective**: Created comprehensive documentation for the project including technical specifications and usage guidelines.

---

## Technical Requirements

### Dependencies
- pandas>=1.3.0
- numpy>=1.21.0
- scikit-learn>=1.0.0
- xgboost>=1.5.0
- category-encoders>=2.3.0
- matplotlib>=3.4.0
- seaborn>=0.11.0
- plotly>=5.0.0
- scipy>=1.7.0
- statsmodels>=0.12.0
- requests>=2.25.0
- beautifulsoup4>=4.9.0
- selenium>=4.0.0
- pickle-mixin>=1.0.0
- tqdm>=4.62.0

### Installation Steps
1. Clone the repository
2. Install required dependencies
3. Run the notebooks in sequence
4. Use the trained models for predictions

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