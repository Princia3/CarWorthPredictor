# 🚗 CarWorthPredictor
CarWorthPredictor is a machine learning-based web application built with Flask that predicts the price of a used car based on various input features such as brand, model, year, mileage, fuel type, and more.

The application takes user inputs, processes them, and outputs an estimated car price using trained ML models.

# 📌 Features

User-friendly Web Interface with brand/model selection and input sliders.
Predicts used car prices dynamically based on multiple features.
Trained on cleaned and preprocessed dataset with all categorical values converted to numerical form.
Built using Jupyter Notebook for model training and Flask for deployment.

Multiple ML models tested and compared:

Linear Regression
XGBoost Regression
Random Forest Regression (Best Performing)

# 🛠 Tech Stack

Python (Data Science & Backend)
Flask (Web Framework)
HTML/CSS/JavaScript (Frontend)
Scikit-learn, XGBoost (ML Libraries)
Pandas, NumPy (Data Preprocessing)
Jupyter Notebook (Model Development)

# 📊 Model Performance (R² Score)

Model	R² Score
Linear Regression	0.575
XGBoost Regression	0.673
Random Forest	0.880 ✅ (Best Accuracy)

# 📂 Project Workflow

Data Preprocessing & Cleaning
Removed duplicates and missing values.
Converted all categorical values into numerical form.
Scaled/normalized numerical values for model input.
Model Training
Trained Linear Regression, XGBoost, and Random Forest models.
Compared model performance using R² Score.
Flask Web App
Created interactive HTML form for input.
Integrated trained model for real-time predictions.
Displayed output price dynamically on the webpage.