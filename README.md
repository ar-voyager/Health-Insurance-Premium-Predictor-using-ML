# 🏥 Health-Insurance-Premium-Predictor-using-ML

An end-to-end machine learning project that predicts annual health insurance premiums based on demographic, medical, and lifestyle factors.
Built using **Scikit-learn** and deployed as an interactive **Streamlit web application** with real-time predictions.


## Overview

Insurance premiums depend on multiple risk factors such as age, BMI, smoking habits, income, and medical history.
This project leverages **supervised machine learning** to estimate premium costs with improved accuracy using an age-based modeling strategy.


## Machine Learning Approach

### Data Preprocessing

* Categorical encoding
* Feature scaling using `StandardScaler`
* Medical risk transformation
* Age-group-specific scaling

### Model Strategy

To improve prediction performance, two separate models were trained:

* **Young Model** → Age < 25
* **Adult Model** → Age ≥ 25

This segmentation helps capture different risk behaviors across age groups.

### Saved Artifacts

* `model_young.joblib`
* `model_rest.joblib`
* `scaler_young.joblib`
* `scaler_rest.joblib`

Each scaler includes:

* Fitted scaler object
* Feature columns used during training


## Web Application (Streamlit)

An interactive UI allows users to input details and receive instant premium predictions.

### Features

* Real-time prediction
* Automatic model selection based on age
* Clean and responsive UI
* Gradient background design
* Cached model loading for performance


## Features Used

* Age
* Gender
* Marital Status
* Region
* Number of Dependents
* BMI Category
* Smoking Status
* Employment Status
* Annual Income (Lakhs)
* Medical History
* Insurance Plan
* Genetic Risk Score


## Project Structure

```
Health-Insurance-Premium-Predictor-using-ML/
│
├── app/
│   ├── main.py
│   └── artifacts/
│       ├── model_young.joblib
│       ├── model_rest.joblib
│       ├── scaler_young.joblib
│       └── scaler_rest.joblib
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Health-Insurance-Premium-Predictor-using-ML.git
cd Health-Insurance-Premium-Predictor-using-ML/app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run main.py
```

## Future Improvements

* SHAP-based model explainability
* Model comparison dashboard
* Prediction confidence intervals
* User authentication system
* Database integration for history tracking
* REST API using FastAPI
* CI/CD pipeline for deployment
* Enhanced UI/UX and animations

## Author
**Ankit Rathaur**
