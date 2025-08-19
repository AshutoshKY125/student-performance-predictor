# Student Performance Predictor

## 1. Introduction
This project implements an end-to-end machine learning pipeline to predict student performance based on various factors such as gender, ethnicity, parental education, lunch type, test preparation course, writing score, and reading score. The project includes data ingestion, data transformation, model training, and a Flask-based web application for making predictions.

## 2. Features
*   **End-to-end Machine Learning Pipeline:** Comprehensive pipeline covering data ingestion, preprocessing (data transformation), model training, and prediction.
*   **Web Application:** A user-friendly web interface built with Flask allows users to input student details and receive predicted performance scores.
*   **Exploratory Data Analysis (EDA):** In-depth analysis of the dataset to understand relationships and patterns.
*   **Robust Model Training:** Training and evaluation of multiple machine learning models to identify the best-performing one.
*   **Modular Codebase:** Organized project structure with separate modules for each stage of the ML lifecycle, ensuring maintainability and scalability.
*   **Logging and Exception Handling:** Implemented for better debugging and application robustness.

## 3. Project Structure
The project is structured as follows:
├── app.py # Main Flask application
├── requirements.txt # Project dependencies
├── setup.py # Project setup for installation
├── src/ # Core source code
│ ├── components/ # Individual ML components
│ │ ├── data_ingestion.py # Handles raw data loading
│ │ ├── data_transformation.py # Data cleaning, preprocessing, feature engineering
│ │ └── model_trainer.py # Trains and evaluates ML models
│ ├── pipeline/ # ML Pipelines
│ │ ├── predict_pipeline.py # Defines the prediction workflow
│ │ └── train_pipeline.py # Defines the training workflow
│ ├── exception.py # Custom exception handling
│ ├── logger.py # Logging utility
│ └── utils.py # Helper functions
├── notebook/ # Jupyter notebooks for analysis and training
│ ├── 1 . EDA STUDENT PERFORMANCE .ipynb # Exploratory Data Analysis
│ └── 2. MODEL TRAINING.ipynb # Model training and evaluation
├── templates/ # HTML templates for the Flask application
└── artifacts/ # Stores trained models, preprocessor objects, etc.

## END TO END PROJECT
